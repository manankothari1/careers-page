#!/usr/bin/env python3
"""Send a daily decision summary to Slack via the Web API."""

import os
import sys
import json
import urllib.request
import urllib.error


SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(blocks: list, text: str = "Daily Decision Summary") -> None:
    token = os.environ.get("SLACK_TOKEN", "").strip()
    if not token:
        print("⚠️  SLACK_TOKEN not set — printing preview instead:\n")
        print(json.dumps(blocks, indent=2))
        sys.exit(1)

    payload = json.dumps({
        "channel": SLACK_CHANNEL,
        "text": text,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        sys.exit(1)

    if not result.get("ok"):
        print(f"Slack API error: {result.get('error')}", file=sys.stderr)
        sys.exit(1)

    print(f"✅  Message sent to {SLACK_CHANNEL} (ts={result.get('ts')})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: daily_summary.py '<blocks_json>'", file=sys.stderr)
        sys.exit(1)

    try:
        blocks = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        sys.exit(1)

    send_slack_message(blocks)
