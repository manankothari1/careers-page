#!/usr/bin/env python3
"""
Minimal Slack message sender utility.
Used by the chief-of-staff cron agent to post the daily summary.

Usage:
    echo "message text" | python3 send_slack.py
    python3 send_slack.py --message "text here"
    python3 send_slack.py --file summary.txt

Requires: SLACK_BOT_TOKEN env var with chat:write scope
"""

import os
import sys
import argparse
import json
import urllib.request
import urllib.parse


SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_API_URL = "https://slack.com/api/chat.postMessage"


def post_message(token: str, channel: str, text: str) -> bool:
    payload = json.dumps({"channel": channel, "text": text, "mrkdwn": True}).encode()
    req = urllib.request.Request(
        SLACK_API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            if data.get("ok"):
                print(f"[Slack] Sent. ts={data.get('ts')}")
                return True
            else:
                print(f"[Slack Error] {data.get('error')}")
                return False
    except Exception as e:
        print(f"[Slack Error] {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", "-m", help="Message text to send")
    parser.add_argument("--file", "-f", help="File containing message text")
    parser.add_argument("--channel", default=SLACK_CHANNEL, help="Slack channel/DM ID")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            text = f.read().strip()
    elif args.message:
        text = args.message
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        print("Error: provide --message, --file, or pipe text via stdin")
        sys.exit(1)

    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("[Error] SLACK_BOT_TOKEN not set.")
        print("Add it to Cursor Cloud Secrets: https://cursor.com/dashboard → Cloud Agents → Secrets")
        sys.exit(1)

    success = post_message(token, args.channel, text)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
