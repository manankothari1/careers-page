#!/usr/bin/env python3
"""
Daily Digest Automation for Manan Kothari @ Homebase
Runs at midnight UTC (5pm PDT) to summarize all Granola meetings from the day
and send a Slack message with decisions, action items, and rationale.

Requires:
  - SLACK_BOT_TOKEN environment variable (Slack Bot OAuth token with chat:write scope)
  - Granola MCP server authenticated in Cursor
  - SLACK_CHANNEL_ID environment variable (default: D06E4QMHCNN)

Usage:
  python daily_digest.py [--date YYYY-MM-DD]
"""

import os
import sys
import json
import subprocess
import argparse
import requests
from datetime import datetime, timedelta, timezone


SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def send_slack_message(text: str, blocks: list = None) -> dict:
    """Send a message to Slack via Web API."""
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN not set. Cannot send Slack message.")
        print("Please add SLACK_BOT_TOKEN to your Cursor Cloud Agent secrets.")
        print("\n--- MESSAGE THAT WOULD HAVE BEEN SENT ---\n")
        print(text)
        print("\n--- END MESSAGE ---\n")
        return {"ok": False, "error": "missing_token"}

    payload = {
        "channel": SLACK_CHANNEL_ID,
        "text": text,
        "mrkdwn": True,
    }
    if blocks:
        payload["blocks"] = blocks

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )
    result = response.json()
    if not result.get("ok"):
        print(f"Slack API error: {result.get('error')}")
    return result


def format_daily_digest(meetings_summary: str, date_str: str) -> str:
    """Format the daily digest as a Slack-friendly message."""
    return meetings_summary


def build_digest_message(meetings_data: list, date_label: str) -> str:
    """Build a formatted digest message from meeting data."""
    # This is called when the script is used programmatically with pre-fetched data
    lines = [f":sun_with_face: *Your Daily Digest — {date_label}*\n"]
    for m in meetings_data:
        lines.append(f"• *{m.get('title')}* ({m.get('time')})")
        for item in m.get("action_items", []):
            lines.append(f"  - [ ] {item}")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send daily Granola digest to Slack")
    parser.add_argument("--date", help="Date to summarize (YYYY-MM-DD), defaults to today PDT")
    parser.add_argument("--message", help="Pre-built message text to send directly")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending")
    args = parser.parse_args()

    if args.message:
        msg = args.message
    else:
        print("Usage: pass --message 'your pre-built message' or extend this script with Granola API calls.")
        sys.exit(1)

    if args.dry_run:
        print("--- DRY RUN ---")
        print(msg)
    else:
        result = send_slack_message(msg)
        if result.get("ok"):
            print("Slack message sent successfully!")
        else:
            print(f"Failed to send: {result}")
            sys.exit(1)
