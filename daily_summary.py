#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
Runs daily at 5pm PDT (midnight UTC), reviews Granola meetings, and sends
a Slack DM to Manan with all decisions, action items, follow-ups, and rationale.

Required secrets (set in Cursor Dashboard → Cloud Agents → Secrets):
    SLACK_BOT_TOKEN: Slack bot token (xoxb-...) with chat:write scope

Usage:
    python3 daily_summary.py                            # send for today
    python3 daily_summary.py --date 2026-05-28          # specific date
    python3 daily_summary.py --dry-run                  # preview without sending
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, date, timedelta, timezone
from typing import Optional

SLACK_CHANNEL_ID = "D06E4QMHCNN"
PACIFIC_UTC_OFFSET = -7  # PDT (UTC-7); change to -8 for PST


def get_target_date(date_str: Optional[str] = None) -> date:
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    utc_now = datetime.now(timezone.utc)
    pacific_now = utc_now + timedelta(hours=PACIFIC_UTC_OFFSET)
    return pacific_now.date()


def send_slack_message(text: str, dry_run: bool = False) -> bool:
    if dry_run:
        print("=" * 70)
        print("DRY RUN — Slack message preview:")
        print("=" * 70)
        print(text)
        print("=" * 70)
        return True

    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN not set.")
        print("Add your Slack bot token to Cursor Dashboard → Cloud Agents → Secrets")
        print("\nMessage that would be sent:")
        print("-" * 70)
        print(text)
        return False

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={"channel": SLACK_CHANNEL_ID, "text": text, "unfurl_links": False},
        timeout=15,
    )
    result = resp.json()
    if result.get("ok"):
        print(f"SUCCESS: Message sent to Slack channel {SLACK_CHANNEL_ID}")
        return True

    error = result.get("error", "unknown_error")
    print(f"ERROR: Slack API error: {error}")
    if error == "invalid_auth":
        print("  → Your SLACK_BOT_TOKEN is invalid. Check it in Cursor Secrets.")
    elif error in ("channel_not_found", "not_in_channel"):
        print(f"  → Bot can't reach channel {SLACK_CHANNEL_ID}. Make sure the bot is added.")
    return False


def build_message(target_date: date, meeting_summaries: list[dict]) -> str:
    date_str = target_date.strftime("%A, %B %-d, %Y")
    weekday = target_date.strftime("%A")

    header = (
        f":sunrise: *Your Daily Decision Brief — {date_str}*\n"
        f"Hey Manan! Here's your end-of-{weekday} wrap-up. "
        f"You had a strong day — let's break down every decision, action item, and follow-up. :muscle:\n"
    )

    if not meeting_summaries:
        return (
            header
            + "\n_No meetings were recorded in Granola today. Enjoy the breathing room! "
            "If you had calls that weren't captured, they won't appear here._\n\n"
            "_— Your Chief of Staff_ :briefcase:"
        )

    divider = "\n" + "─" * 50 + "\n"
    blocks = []

    for m in meeting_summaries:
        parts = [f":calendar: *{m['title']}*", f"_{m['time']}_ | _{m['attendees']}_\n"]

        if m.get("decisions"):
            parts.append(":white_check_mark: *Key Decisions*")
            for d in m["decisions"]:
                parts.append(f"• {d}")
            parts.append("")

        if m.get("action_items"):
            parts.append(":dart: *Your Action Items*")
            for a in m["action_items"]:
                parts.append(f"   :black_small_square: {a}")
            parts.append("")

        if m.get("follow_ups"):
            parts.append(":arrows_counterclockwise: *Follow-Ups & Open Questions*")
            for f in m["follow_ups"]:
                parts.append(f"   :small_orange_diamond: {f}")
            parts.append("")

        if m.get("rationale"):
            parts.append(f":brain: *Why It Matters:* {m['rationale']}")

        blocks.append("\n".join(parts))

    body = divider.join(blocks)

    footer = (
        "\n" + "─" * 50 + "\n"
        ":trophy: *Bottom line:* Crisp decisions, clear direction — that's the Manan way. "
        "Go make tomorrow even bigger! :rocket:\n"
        "_— Your Chief of Staff_ :briefcase:"
    )

    return header + divider + body + footer


def main():
    parser = argparse.ArgumentParser(description="Daily Decision Summary — Chief of Staff")
    parser.add_argument("--date", help="Target date YYYY-MM-DD (default: today PDT)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without sending to Slack")
    parser.add_argument("--summaries-json", help="Path to JSON file with pre-built meeting summaries")
    args = parser.parse_args()

    target_date = get_target_date(args.date)
    print(f"Daily summary for: {target_date.strftime('%A, %B %-d, %Y')}")

    # Load meeting summaries from JSON file or env var (populated by the Cursor agent)
    meeting_summaries = []
    summaries_src = args.summaries_json or os.getenv("SUMMARIES_JSON_PATH")
    if summaries_src and os.path.exists(summaries_src):
        with open(summaries_src) as f:
            meeting_summaries = json.load(f)
        print(f"Loaded {len(meeting_summaries)} meeting(s) from {summaries_src}")
    else:
        inline_json = os.getenv("PREBUILT_SUMMARIES_JSON")
        if inline_json:
            meeting_summaries = json.loads(inline_json)
            print(f"Loaded {len(meeting_summaries)} meeting(s) from PREBUILT_SUMMARIES_JSON")
        else:
            print("No meeting summaries provided — sending empty-day message")

    message = build_message(target_date, meeting_summaries)
    success = send_slack_message(message, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
