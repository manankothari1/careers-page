#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Reads Granola meetings for the day and posts a summary to Slack.

Required environment variable:
  SLACK_BOT_TOKEN - A Slack bot token with chat:write scope

Usage:
  python daily_summary.py --message "your summary" --channel D06E4QMHCNN
  python daily_summary.py --file daily_summaries/2026-06-25.md --channel D06E4QMHCNN
"""

import argparse
import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone


SLACK_CHANNEL = "D06E4QMHCNN"


def post_to_slack(message: str, channel: str = SLACK_CHANNEL) -> bool:
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN environment variable is not set.")
        print("Please add it as a Cloud Agent secret in the Cursor Dashboard.")
        return False

    payload = json.dumps({
        "channel": channel,
        "text": message,
        "mrkdwn": True,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✓ Message posted to Slack channel {channel}")
                return True
            else:
                print(f"Slack API error: {body.get('error', 'unknown')}")
                return False
    except urllib.error.URLError as e:
        print(f"Network error posting to Slack: {e}")
        return False


def load_message(args) -> str:
    if args.message:
        return args.message
    if args.file:
        with open(args.file, "r") as f:
            return f.read()
    print("ERROR: Provide --message or --file.")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Post daily summary to Slack")
    parser.add_argument("--message", help="Summary text to post")
    parser.add_argument("--file", help="Path to a markdown file to post")
    parser.add_argument("--channel", default=SLACK_CHANNEL, help="Slack channel/DM ID")
    parser.add_argument("--dry-run", action="store_true", help="Print message without posting")
    args = parser.parse_args()

    message = load_message(args)

    if args.dry_run:
        print("--- DRY RUN ---")
        print(message)
        print("--- END ---")
        return

    success = post_to_slack(message, args.channel)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
