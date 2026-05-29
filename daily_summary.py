#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Runs daily at 5pm PDT, reviews Granola meetings, sends Slack summary to Manan.

Required secrets (set in Cursor Dashboard > Secrets):
    SLACK_BOT_TOKEN: Slack bot token (xoxb-...) with chat:write scope
    GRANOLA_API_TOKEN: (optional) Granola access token for direct API calls

Usage:
    python3 daily_summary.py
    python3 daily_summary.py --date 2026-05-28   # specific date
    python3 daily_summary.py --dry-run            # print without sending to Slack
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, date, timedelta, timezone
from typing import Optional


SLACK_CHANNEL_ID = "D06E4QMHCNN"
GRANOLA_API_BASE = "https://api.granola.ai/v1"
PACIFIC_UTC_OFFSET = -7  # PDT (UTC-7); adjust to -8 for PST


def get_target_date(date_str: Optional[str] = None) -> date:
    """Get the target date — today in Pacific time, or a custom date."""
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    # Convert UTC now to Pacific
    utc_now = datetime.now(timezone.utc)
    pacific_now = utc_now + timedelta(hours=PACIFIC_UTC_OFFSET)
    return pacific_now.date()


def get_granola_meetings_for_date(target_date: date) -> list[dict]:
    """
    Fetch meetings from Granola API for a specific date.
    Requires GRANOLA_API_TOKEN environment variable.
    """
    token = os.getenv("GRANOLA_API_TOKEN")
    if not token:
        print("WARNING: GRANOLA_API_TOKEN not set. Cannot fetch meetings directly.")
        print("Please add GRANOLA_API_TOKEN to your Cursor Dashboard secrets.")
        return []

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-client-version": "6.0.0",
    }

    try:
        response = requests.post(
            f"{GRANOLA_API_BASE}/get-documents",
            headers=headers,
            json={},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        docs = data.get("documents", data) if isinstance(data, dict) else data

        # Filter to target date (Pacific time)
        day_meetings = []
        for doc in docs:
            start_time = doc.get("created_at") or doc.get("startTime") or ""
            if not start_time:
                continue
            try:
                dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
                pacific_dt = dt + timedelta(hours=PACIFIC_UTC_OFFSET)
                if pacific_dt.date() == target_date:
                    day_meetings.append(doc)
            except (ValueError, AttributeError):
                continue

        return sorted(day_meetings, key=lambda d: d.get("created_at", ""))

    except requests.RequestException as e:
        print(f"ERROR: Failed to fetch Granola meetings: {e}")
        return []


def extract_notes_text(notes) -> str:
    """Recursively extract plain text from Granola notes structure."""
    if not notes:
        return ""
    if isinstance(notes, str):
        return notes

    def extract(content):
        if not content:
            return ""
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "\n".join(extract(item) for item in content if extract(item))
        if isinstance(content, dict):
            if content.get("type") == "text":
                return content.get("text", "")
            parts = []
            if content.get("content"):
                parts.append(extract(content["content"]))
            if content.get("text"):
                parts.append(content["text"])
            return "\n".join(p for p in parts if p)
        return ""

    return extract(notes)


def extract_attendees(doc: dict) -> list[str]:
    """Extract attendee names from a Granola document."""
    names = []
    people = doc.get("people") or {}
    if isinstance(people, dict):
        for attendee in people.get("attendees", []):
            if isinstance(attendee, dict):
                details = attendee.get("details", {})
                person = details.get("person", {})
                name = person.get("name", {})
                full_name = name.get("fullName") or attendee.get("email", "")
                if full_name and full_name not in names:
                    names.append(full_name)

    cal_attendees = (doc.get("google_calendar_event") or {}).get("attendees") or []
    for attendee in cal_attendees:
        name = attendee.get("displayName") or attendee.get("email", "")
        if name and name not in names:
            names.append(name)

    return names


def format_meeting_block(title: str, time_str: str, attendees: list[str], summary: str) -> str:
    """Format a single meeting section for Slack."""
    attendee_str = ", ".join(attendees) if attendees else "No attendees recorded"
    lines = [
        f"*{title}*",
        f"_{time_str}_  |  {attendee_str}",
        "",
        summary.strip(),
    ]
    return "\n".join(lines)


def build_slack_message(
    target_date: date,
    meetings: list[dict],
    prebuilt_summaries: Optional[list[dict]] = None,
) -> str:
    """
    Compose the full daily decision summary Slack message.

    Args:
        target_date: The date being summarized
        meetings: Raw meeting docs from Granola API
        prebuilt_summaries: Pre-fetched meeting summaries (used when API token unavailable)
    """
    date_str = target_date.strftime("%A, %B %-d, %Y")
    weekday = target_date.strftime("%A")

    header = (
        f":sunrise: *Your Daily Decision Brief — {date_str}*\n"
        f"Hey Manan! Here's your end-of-{weekday} wrap-up. "
        f"You had a strong day — here's everything you decided, with full context and next steps. Let's go! :muscle:\n"
    )

    if not meetings and not prebuilt_summaries:
        return (
            header
            + "\n_No meetings recorded in Granola for today. Enjoy the clear calendar! "
            "If you had unrecorded calls, they won't appear here._"
        )

    divider = "\n" + "─" * 48 + "\n"
    meeting_blocks = []

    # Use pre-built summaries if raw API data isn't available
    source = prebuilt_summaries or []
    for m in source:
        block_parts = []

        # Header
        block_parts.append(f":calendar: *{m['title']}*")
        block_parts.append(f"_{m['time']}_ | _{m['attendees']}_\n")

        # Decisions
        if m.get("decisions"):
            block_parts.append(":white_check_mark: *Key Decisions Made*")
            for d in m["decisions"]:
                block_parts.append(f"• {d}")
            block_parts.append("")

        # Action items
        if m.get("action_items"):
            block_parts.append(":dart: *Your Action Items*")
            for item in m["action_items"]:
                block_parts.append(f"   :black_small_square: {item}")
            block_parts.append("")

        # Rationale
        if m.get("rationale"):
            block_parts.append(f":brain: *Why it matters:* {m['rationale']}")

        meeting_blocks.append("\n".join(block_parts))

    body = divider.join(meeting_blocks)

    footer = (
        "\n" + "─" * 48 + "\n"
        ":trophy: *Bottom line:* You're making crisp, decisive calls today, Manan. "
        "Cutting what doesn't work and doubling down on what does — that's the playbook. "
        "Go crush those customer calls tomorrow! :rocket:\n"
        "_— Your Chief of Staff_ :briefcase:"
    )

    return header + divider + body + footer


def send_slack_message(text: str, dry_run: bool = False) -> bool:
    """Send a message to the configured Slack channel."""
    if dry_run:
        print("=" * 60)
        print("DRY RUN — Message that would be sent to Slack:")
        print("=" * 60)
        print(text)
        print("=" * 60)
        return True

    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN not set.")
        print("Please add your Slack bot token to Cursor Dashboard > Secrets > SLACK_BOT_TOKEN")
        print("\nFalling back to dry-run output:")
        print(text)
        return False

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "channel": SLACK_CHANNEL_ID,
            "text": text,
            "unfurl_links": False,
            "unfurl_media": False,
        },
        timeout=15,
    )

    result = response.json()
    if result.get("ok"):
        print(f"SUCCESS: Message sent to Slack channel {SLACK_CHANNEL_ID}")
        return True
    else:
        error = result.get("error", "unknown error")
        print(f"ERROR: Slack API returned: {error}")
        if error == "invalid_auth":
            print("Your SLACK_BOT_TOKEN appears to be invalid. Please check it in Cursor Secrets.")
        elif error == "channel_not_found":
            print(f"Channel {SLACK_CHANNEL_ID} not found. Ensure the bot has been added to this DM.")
        elif error == "not_in_channel":
            print("Bot is not in this channel. For DMs, the bot must have been invited.")
        return False


def main():
    parser = argparse.ArgumentParser(description="Daily Decision Summary — Chief of Staff")
    parser.add_argument("--date", help="Target date (YYYY-MM-DD). Defaults to today in PDT.")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending to Slack.")
    args = parser.parse_args()

    target_date = get_target_date(args.date)
    print(f"Generating daily summary for: {target_date.strftime('%A, %B %-d, %Y')}")

    # Try to fetch meetings from Granola API
    meetings = get_granola_meetings_for_date(target_date)
    print(f"Found {len(meetings)} meeting(s) via Granola API")

    # Build the message
    # NOTE: prebuilt_summaries is populated by the Cursor agent when running as MCP automation
    # and passed in via the PREBUILT_SUMMARIES_JSON env var (set by the agent before calling this script)
    prebuilt_json = os.getenv("PREBUILT_SUMMARIES_JSON")
    prebuilt_summaries = json.loads(prebuilt_json) if prebuilt_json else None

    message = build_slack_message(
        target_date=target_date,
        meetings=meetings,
        prebuilt_summaries=prebuilt_summaries,
    )

    success = send_slack_message(message, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
