#!/usr/bin/env python3
"""Send a Slack Block Kit message to Manan's DM channel."""

import sys
import os
import json
import urllib.request
import urllib.error


CHANNEL_ID = "D06E4QMHCNN"


def send_slack_message(blocks: list, fallback_text: str = "Daily Decision Summary") -> None:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("=== SLACK PREVIEW (no SLACK_TOKEN set) ===")
        print(json.dumps(blocks, indent=2))
        print("==========================================")
        sys.exit(1)

    payload = json.dumps({
        "channel": CHANNEL_ID,
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
                print(f"Message sent successfully. ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')}", file=sys.stderr)
                sys.exit(2)
    except urllib.error.URLError as e:
        print(f"Network error: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: daily_summary.py '<blocks_json>'", file=sys.stderr)
        sys.exit(1)

    blocks = json.loads(sys.argv[1])
    send_slack_message(blocks)
