#!/usr/bin/env python3
"""Send daily decision summary to Slack channel."""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL_ID = "D06E4QMHCNN"


def send_slack_message(blocks: list, fallback_text: str) -> bool:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("ERROR: SLACK_TOKEN environment variable not set.")
        print("Add your Slack Bot Token at: Cursor Dashboard > Cloud Agents > Secrets")
        print("\n--- PREVIEW (would have been sent) ---")
        print(fallback_text)
        print("--- END PREVIEW ---")
        return False

    payload = {
        "channel": CHANNEL_ID,
        "text": fallback_text,
        "blocks": blocks,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"Message sent successfully to {CHANNEL_ID}")
                return True
            else:
                print(f"Slack API error: {result.get('error', 'unknown')}")
                return False
    except urllib.error.URLError as e:
        print(f"Network error sending to Slack: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: daily_summary.py '<blocks_json>'")
        sys.exit(1)

    blocks = json.loads(sys.argv[1])
    fallback = sys.argv[2] if len(sys.argv) > 2 else "Daily Decision Summary"
    success = send_slack_message(blocks, fallback)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
