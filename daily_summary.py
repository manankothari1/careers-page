#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
Runs at 5pm PDT daily via Cursor Cloud Agent cron (0 0 * * * UTC).

Fetches Granola meeting notes for today and sends a decision/action-item
summary to Slack DM D06E4QMHCNN.

Required secrets (add via Cursor Dashboard → Cloud Agents → Secrets):
  SLACK_BOT_TOKEN   — Slack bot token (xoxb-...)
  GRANOLA_API_KEY   — Granola API key (grn_...)
"""

import os
import sys
import json
from datetime import datetime, timezone, timedelta
from typing import Optional

import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
GRANOLA_API_KEY = os.environ.get("GRANOLA_API_KEY")
SLACK_CHANNEL_ID = "D06E4QMHCNN"
GRANOLA_BASE_URL = "https://public-api.granola.ai"

# Pacific Daylight Time (UTC-7) — adjust to PST (UTC-8) in winter if needed
PDT = timezone(timedelta(hours=-7))


# ── Granola helpers ───────────────────────────────────────────────────────────

def granola_headers() -> dict:
    if not GRANOLA_API_KEY:
        raise RuntimeError("GRANOLA_API_KEY is not set. Add it to your Cursor Cloud Agent secrets.")
    return {"Authorization": f"Bearer {GRANOLA_API_KEY}"}


def get_today_meetings() -> list[dict]:
    """Return all Granola notes created today (PDT)."""
    now_pdt = datetime.now(PDT)
    start = now_pdt.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now_pdt.replace(hour=23, minute=59, second=59, microsecond=0)

    notes = []
    cursor = None
    while True:
        params: dict = {
            "created_after": start.isoformat(),
            "created_before": end.isoformat(),
        }
        if cursor:
            params["cursor"] = cursor

        resp = requests.get(
            f"{GRANOLA_BASE_URL}/v1/notes",
            headers=granola_headers(),
            params=params,
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        notes.extend(data.get("notes", []))
        if not data.get("hasMore"):
            break
        cursor = data.get("cursor")

    return notes


def get_note_detail(note_id: str) -> dict:
    """Fetch full note detail (summary, attendees, etc.) for one note."""
    resp = requests.get(
        f"{GRANOLA_BASE_URL}/v1/notes/{note_id}",
        headers=granola_headers(),
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


# ── Message formatting ────────────────────────────────────────────────────────

def format_date(dt: datetime) -> str:
    return dt.strftime("%A, %B %-d, %Y")


def build_slack_message(notes: list[dict], date_str: str) -> str:
    """
    Build a rich, encouraging Slack message that surfaces:
    - Key decisions + rationale
    - Action items & follow-ups per meeting
    - An overall motivating close
    """
    if not notes:
        return (
            f":wave: *Daily Decision Summary — {date_str}*\n\n"
            "Hey Manan! No meetings recorded today — enjoy the open space. "
            "A clear calendar is a rare gift; use it for deep work or recharging. "
            "See you tomorrow for the debrief! :rocket:"
        )

    lines = [
        f":star2: *Daily Decision Summary — {date_str}*",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "",
        f"Hey Manan! You had a *packed day* — {len(notes)} meeting{'s' if len(notes) != 1 else ''} "
        "down and some really solid moves made. Here's your complete debrief so nothing falls through "
        "the cracks. :dart:",
        "",
    ]

    all_actions: list[str] = []

    for i, note in enumerate(notes, 1):
        title = note.get("title", "Untitled Meeting")
        summary = note.get("summary_markdown") or note.get("summary") or ""
        attendees_raw = note.get("attendees", [])
        attendee_names = [
            a.get("name", "") for a in attendees_raw if a.get("name") and a.get("name") != "Manan Kothari"
        ]

        lines.append(f"━━ *{i}. {title}*" + (f"  _(with {', '.join(attendee_names[:4])})_" if attendee_names else ""))

        if summary:
            # Strip markdown headers for cleaner Slack rendering (Slack uses *bold*)
            clean = summary.replace("### ", "*").replace("## ", "*").replace("# ", "*")
            # Close any opened bold from headers
            import re
            clean = re.sub(r"\*([^\n*]+)\n", r"*\1*\n", clean)
            lines.append(clean.strip())
        else:
            lines.append("_No summary available for this meeting._")

        lines.append("")

        # Collect action items from "Next Steps" sections
        if "Next Steps" in summary or "next steps" in summary.lower():
            ns_start = summary.lower().find("next steps")
            ns_section = summary[ns_start:]
            # Grab bullet lines
            for line in ns_section.split("\n"):
                stripped = line.strip()
                if stripped.startswith("- ") or stripped.startswith("* "):
                    all_actions.append(f"• {stripped[2:].strip()} _(from: {title})_")

    # Consolidated action items section
    if all_actions:
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append(":white_check_mark: *Consolidated Action Items*")
        lines.append("")
        lines.extend(all_actions)
        lines.append("")

    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append(
        ":muscle: *You crushed it today, Manan!* The strategy is sharp and the team is moving fast. "
        "Tomorrow, pick the ONE action item above that will create the most leverage and start there. "
        "You've got this. :fire:"
    )

    return "\n".join(lines)


def build_fallback_message(prebuilt_summary: str) -> str:
    """Used when Granola API isn't available but we have MCP-sourced data."""
    return prebuilt_summary


# ── Slack posting ─────────────────────────────────────────────────────────────

def send_slack_message(message: str) -> bool:
    if not SLACK_BOT_TOKEN:
        print(
            "ERROR: SLACK_BOT_TOKEN is not set.\n"
            "Add it as a secret in Cursor Dashboard → Cloud Agents → Secrets.\n"
            "\nPrepared message (copy-paste into Slack if needed):\n"
            + "=" * 60
            + "\n"
            + message
        )
        return False

    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=message,
            mrkdwn=True,
            unfurl_links=False,
            unfurl_media=False,
        )
        print(f"✅ Slack message sent! ts={response['ts']}")
        return True
    except SlackApiError as e:
        print(f"❌ Slack API error: {e.response['error']}")
        print(f"Full error: {e.response}")
        return False


# ── Main ──────────────────────────────────────────────────────────────────────

def main(prebuilt_message: Optional[str] = None):
    today_str = format_date(datetime.now(PDT))

    if prebuilt_message:
        # Used when running from the cloud agent with MCP-sourced data
        print(f"Using pre-built message for {today_str}")
        success = send_slack_message(prebuilt_message)
    else:
        # Full standalone mode: fetch from Granola API directly
        if not GRANOLA_API_KEY:
            print("ERROR: GRANOLA_API_KEY is not set.")
            sys.exit(1)

        print(f"Fetching Granola meetings for {today_str}...")
        try:
            notes_list = get_today_meetings()
        except requests.HTTPError as e:
            print(f"Granola API error: {e}")
            sys.exit(1)

        print(f"Found {len(notes_list)} meeting(s)")

        notes_detail = []
        for note in notes_list:
            note_id = note.get("id")
            if note_id:
                try:
                    detail = get_note_detail(note_id)
                    notes_detail.append(detail)
                except requests.HTTPError as e:
                    print(f"Warning: could not fetch detail for {note_id}: {e}")
                    notes_detail.append(note)

        message = build_slack_message(notes_detail, today_str)
        success = send_slack_message(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
