#!/usr/bin/env python3
"""Send a daily decision summary to Slack via Block Kit JSON passed as argv[1]."""

import os
import sys
import json
import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"


def send_to_slack(blocks: list, fallback_text: str) -> bool:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("⚠️  SLACK_TOKEN not set — printing preview instead:\n")
        print(fallback_text)
        print("\n--- Block Kit JSON ---")
        print(json.dumps(blocks, indent=2))
        return False

    payload = json.dumps({
        "channel": SLACK_CHANNEL,
        "text": fallback_text,
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
                print(f"✅ Slack message sent to {SLACK_CHANNEL}")
                return True
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                return False
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: daily_summary.py '<blocks_json>'")
        sys.exit(1)

    raw = sys.argv[1]
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)

    blocks = data.get("blocks", [])
    fallback = data.get("text", "Daily decision summary")

    ok = send_to_slack(blocks, fallback)
    sys.exit(0 if ok else 1)
