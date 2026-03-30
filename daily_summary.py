#!/usr/bin/env python3
"""
Chief of Staff Daily Summary Sender
Posts a Slack Block Kit message to the configured DM channel.
Usage: python3 daily_summary.py '<block_kit_json_string>'
Requires SLACK_TOKEN env var (bot token with chat:write scope).
"""

import sys
import os
import json
import urllib.request
import urllib.error

CHANNEL_ID = "D06E4QMHCNN"


def send_slack_message(blocks: list, text: str = "Daily Summary") -> None:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("⚠️  SLACK_TOKEN not set — printing preview instead:\n")
        print(text)
        print("\n--- Block Kit payload ---")
        print(json.dumps(blocks, indent=2))
        return

    payload = json.dumps({
        "channel": CHANNEL_ID,
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
                print(f"✅  Slack message sent! ts={body.get('ts')}")
            else:
                print(f"❌  Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f"❌  Network error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 daily_summary.py '<block_kit_json>'")
        sys.exit(1)
    blocks = json.loads(sys.argv[1])
    fallback = sys.argv[2] if len(sys.argv) > 2 else "Daily Decision Summary"
    send_slack_message(blocks, fallback)
