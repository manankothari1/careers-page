#!/usr/bin/env python3
"""
Chief of Staff daily summary sender.
Usage: python3 daily_summary.py '<blocks_json>'
Reads SLACK_TOKEN from environment. Channel is hardcoded as DM with Manan.
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"


def send_slack_message(blocks: list, text: str = "Daily Decision Summary") -> None:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("⚠️  SLACK_TOKEN not set — printing preview only.\n")
        print("=" * 70)
        print(text)
        print("=" * 70)
        print(json.dumps(blocks, indent=2))
        return

    payload = json.dumps({
        "channel": CHANNEL,
        "text": text,
        "blocks": blocks,
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
                print(f"✅  Message sent to {CHANNEL}")
            else:
                print(f"❌  Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f"❌  Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 daily_summary.py '<blocks_json>'")
        sys.exit(1)
    blocks = json.loads(sys.argv[1])
    fallback = sys.argv[2] if len(sys.argv) > 2 else "Daily Decision Summary"
    send_slack_message(blocks, fallback)
