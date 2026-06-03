#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Bot
============================================
Runs daily (cron: 0 0 * * * = midnight UTC / ~5pm PDT), reviews all Granola
meeting notes for the current day, and DMs a beautifully formatted summary to
Slack channel D06E4QMHCNN.

Setup:
  Add SLACK_BOT_TOKEN as a secret in your Cursor Cloud Agent dashboard.
  The token needs: chat:write scope on the Homebase workspace.

Usage:
  python daily_summary.py                 # auto-fetches today's meetings
  python daily_summary.py --date 2026-06-02  # fetch a specific day
  python daily_summary.py --dry-run       # print message, don't send
"""

import os
import sys
import json
import argparse
import datetime
import textwrap
import requests
from pathlib import Path


SLACK_CHANNEL_ID = "D06E4QMHCNN"
SUMMARIES_DIR = Path(__file__).parent / "summaries"
GRANOLA_API_BASE = "https://api.granola.so/v1"  # placeholder — replace with real endpoint if self-calling


# ---------------------------------------------------------------------------
# Slack helpers
# ---------------------------------------------------------------------------

def send_slack_message(token: str, channel: str, blocks: list, fallback_text: str) -> dict:
    """Post a message to Slack using the Web API."""
    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "channel": channel,
            "text": fallback_text,
            "blocks": blocks,
            "unfurl_links": False,
            "unfurl_media": False,
        },
        timeout=20,
    )
    resp.raise_for_status()
    result = resp.json()
    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}")
    return result


def build_blocks(date_label: str, summary_md: str) -> list:
    """Wrap the markdown summary in Slack Block Kit blocks."""
    # Slack mrkdwn max per section block = 3000 chars; chunk if needed
    chunks = [summary_md[i : i + 2900] for i in range(0, len(summary_md), 2900)]

    blocks: list = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🌟 Your Daily Decision Brief — {date_label}",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    for chunk in chunks:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": chunk},
            }
        )

    blocks += [
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "📬 Compiled by your Chief of Staff bot · Powered by Granola + Cursor AI",
                }
            ],
        },
    ]
    return blocks


# ---------------------------------------------------------------------------
# Summary loader
# ---------------------------------------------------------------------------

def load_summary(date_str: str) -> str:
    """Load a pre-generated summary markdown file for the given date."""
    SUMMARIES_DIR.mkdir(exist_ok=True)
    path = SUMMARIES_DIR / f"{date_str}.md"
    if not path.exists():
        raise FileNotFoundError(
            f"No summary found for {date_str} at {path}.\n"
            "The Cursor Cloud Agent should generate this file before calling send."
        )
    return path.read_text()


def save_summary(date_str: str, content: str) -> Path:
    """Persist a summary to disk."""
    SUMMARIES_DIR.mkdir(exist_ok=True)
    path = SUMMARIES_DIR / f"{date_str}.md"
    path.write_text(content)
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Send daily Granola decision brief to Slack.")
    parser.add_argument("--date", default=None, help="ISO date override (YYYY-MM-DD). Defaults to today.")
    parser.add_argument("--dry-run", action="store_true", help="Print the message but don't send it.")
    args = parser.parse_args()

    # Determine target date
    if args.date:
        target_date = args.date
    else:
        # Cron runs at midnight UTC; business day in PDT is "yesterday UTC"
        today_utc = datetime.datetime.utcnow().date()
        target_date = today_utc.isoformat()

    print(f"📅 Building daily brief for: {target_date}")

    # Load summary
    try:
        summary_text = load_summary(target_date)
    except FileNotFoundError as e:
        print(f"⚠️  {e}", file=sys.stderr)
        sys.exit(1)

    # Format for Slack
    date_label = datetime.date.fromisoformat(target_date).strftime("%A, %B %-d")
    blocks = build_blocks(date_label, summary_text)

    if args.dry_run:
        print("\n" + "=" * 60)
        print(f"DRY RUN — would send to channel {SLACK_CHANNEL_ID}:")
        print("=" * 60)
        print(summary_text)
        return

    # Send
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print(
            "❌  SLACK_BOT_TOKEN is not set.\n"
            "    Add it as a secret in Cursor Cloud Agent > Secrets.\n"
            "    The token needs the chat:write scope.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"📨 Sending to Slack channel {SLACK_CHANNEL_ID}...")
    result = send_slack_message(token, SLACK_CHANNEL_ID, blocks, f"Daily Decision Brief — {date_label}")
    print(f"✅  Message sent! ts={result.get('ts')}")


if __name__ == "__main__":
    main()
