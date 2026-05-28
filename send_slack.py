#!/usr/bin/env python3
"""
Slack message sender helper.
Called by the daily summary automation with a JSON payload.

Usage:
    python3 send_slack.py '<json_payload>'

Requires: SLACK_BOT_TOKEN environment variable
"""

import os
import sys
import json
import requests


def send_slack_message(channel: str, blocks: list, fallback_text: str) -> bool:
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN not set. Add it to Cursor Cloud Agent Secrets.")
        print("\n--- Message preview ---")
        print(fallback_text)
        print("-----------------------")
        return False

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={"channel": channel, "text": fallback_text, "blocks": blocks},
        timeout=10,
    )
    result = resp.json()
    if result.get("ok"):
        print(f"✅ Sent to Slack channel {channel}")
        return True
    else:
        print(f"❌ Slack error: {result.get('error', 'unknown')}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_slack.py '<json_payload>'")
        sys.exit(1)

    payload = json.loads(sys.argv[1])
    success = send_slack_message(
        channel=payload["channel"],
        blocks=payload["blocks"],
        fallback_text=payload["text"],
    )
    sys.exit(0 if success else 1)
