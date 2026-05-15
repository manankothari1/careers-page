#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
Runs at 5 PM PDT every day, reviews Granola meetings, and posts a
structured decision summary to Slack channel D06E4QMHCNN.

Required env vars:
  SLACK_BOT_TOKEN  — Slack bot token (xoxb-...)
  GRANOLA_API_KEY  — Granola API key (if not using MCP)

Usage:
  python daily_summary.py [--date YYYY-MM-DD]
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone, timedelta

import requests

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")

PDT = timezone(timedelta(hours=-7))


def get_today_pdt() -> str:
    """Return today's date in PDT as YYYY-MM-DD."""
    return datetime.now(PDT).strftime("%Y-%m-%d")


def send_slack_message(text: str, blocks: list | None = None) -> dict:
    """Post a message to the configured Slack channel."""
    if not SLACK_BOT_TOKEN:
        print("[WARN] SLACK_BOT_TOKEN not set — printing message to stdout instead.")
        print("=" * 60)
        print(text)
        print("=" * 60)
        return {"ok": False, "error": "no_token"}

    payload = {
        "channel": SLACK_CHANNEL,
        "text": text,
    }
    if blocks:
        payload["blocks"] = blocks

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=15,
    )
    data = resp.json()
    if not data.get("ok"):
        print(f"[ERROR] Slack API error: {data.get('error')}")
    else:
        print(f"[OK] Message posted to {SLACK_CHANNEL}")
    return data


def build_slack_blocks(summary_md: str, date_label: str) -> list:
    """Convert the markdown summary into Slack Block Kit blocks."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📋 Your Daily Decision Summary — {date_label}",
                "emoji": True,
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": summary_md[:2900],  # Slack block text limit
            },
        },
    ]
    # If summary is long, split into additional sections
    if len(summary_md) > 2900:
        remaining = summary_md[2900:]
        chunks = [remaining[i : i + 2900] for i in range(0, len(remaining), 2900)]
        for chunk in chunks[:8]:  # max ~10 sections
            blocks.append(
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": chunk},
                }
            )
    blocks.append({"type": "divider"})
    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Your Chief of Staff • Powered by Granola + Cursor_",
                }
            ],
        }
    )
    return blocks


def build_summary_from_meetings(meetings: list, date_label: str) -> str:
    """
    Build a human-friendly Slack-formatted summary string from a list of
    meeting dicts (each with 'title', 'time', 'summary' keys).
    """
    if not meetings:
        return (
            f"*No meetings recorded in Granola for {date_label}.*\n\n"
            "Enjoy the clear schedule — or check if Granola synced correctly! 🎉"
        )

    lines = []
    lines.append(f"*Hey Manan! Here's your full day in review for {date_label}.* 🚀\n")
    lines.append("You crushed it today — here's every decision you made with full context:\n")

    for i, m in enumerate(meetings, 1):
        lines.append(f"{'─' * 48}")
        lines.append(f"*{i}. {m['title']}* — _{m.get('time', '')}_ ")
        summary = m.get("summary", "").strip()
        if summary:
            lines.append(summary)
        else:
            lines.append("_No notes recorded for this meeting._")
        lines.append("")

    lines.append("─" * 48)
    lines.append("\n*That's a wrap on today! You're doing great work. 💪*")
    lines.append("_See you tomorrow at 5 PM with your next summary._")

    return "\n".join(lines)


def load_summary_file(date_str: str) -> str | None:
    """Load a pre-generated markdown summary file if it exists."""
    path = os.path.join(os.path.dirname(__file__), "summaries", f"{date_str}.md")
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return None


def main():
    parser = argparse.ArgumentParser(description="Send daily Granola decision summary to Slack")
    parser.add_argument("--date", default=None, help="Date override (YYYY-MM-DD, defaults to today PDT)")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending to Slack")
    args = parser.parse_args()

    date_str = args.date or get_today_pdt()
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"[ERROR] Invalid date format: {date_str}")
        sys.exit(1)

    date_label = date_obj.strftime("%A, %B %-d, %Y")
    print(f"[INFO] Generating summary for {date_label} ...")

    # Try to load a pre-generated summary file first
    summary_md = load_summary_file(date_str)

    if summary_md:
        print(f"[INFO] Loaded pre-generated summary from summaries/{date_str}.md")
        slack_text = f"📋 *Daily Decision Summary — {date_label}*\n\nHey Manan! See your full summary below."
        # Convert markdown to Slack mrkdwn (basic cleanup)
        slack_body = (
            summary_md
            .replace("###", "*")
            .replace("##", "*")
            .replace("# ", "*")
            .replace("**", "*")
            .replace("🔴", "🔴")
            .replace("🟡", "🟡")
            .replace("🟢", "🟢")
        )
        blocks = build_slack_blocks(slack_body, date_label)
    else:
        print(f"[WARN] No pre-generated summary found for {date_str}. Sending placeholder.")
        slack_text = f"📋 *Daily Decision Summary — {date_label}*\nNo meetings found in Granola for today."
        blocks = None

    if args.dry_run:
        print("[DRY RUN] Would send the following to Slack:")
        print(json.dumps(blocks or slack_text, indent=2))
        return

    send_slack_message(slack_text, blocks)


if __name__ == "__main__":
    main()
