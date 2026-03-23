#!/usr/bin/env python3
"""
Chief of Staff Daily Summary Script
Posts a Slack Block Kit message to the configured channel.
Usage: python3 daily_summary.py '<blocks_json>'
Requires SLACK_TOKEN env var (Slack Bot Token with chat:write scope).
If SLACK_TOKEN is missing, prints preview and exits 1.
"""

import sys
import os
import json
import urllib.request
import urllib.error

CHANNEL_ID = "D06E4QMHCNN"


def post_to_slack(blocks: list, text: str = "Daily Summary") -> None:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("⚠️  SLACK_TOKEN not set — preview only:\n")
        print(json.dumps({"channel": CHANNEL_ID, "text": text, "blocks": blocks}, indent=2))
        sys.exit(1)

    payload = json.dumps({
        "channel": CHANNEL_ID,
        "text": text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
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
    except urllib.error.URLError as e:
        print(f"❌ Network error posting to Slack: {e}")
        sys.exit(2)

    if body.get("ok"):
        print(f"✅ Message posted to {CHANNEL_ID} (ts={body.get('ts')})")
    else:
        print(f"❌ Slack API error: {body.get('error')}")
        print(json.dumps(body, indent=2))
        sys.exit(3)


def divider():
    return {"type": "divider"}


def header(text: str) -> dict:
    return {
        "type": "header",
        "text": {"type": "plain_text", "text": text, "emoji": True},
    }


def section(text: str) -> dict:
    return {
        "type": "section",
        "text": {"type": "mrkdwn", "text": text},
    }


def context(text: str) -> dict:
    return {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": text}],
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 daily_summary.py '<blocks_json>'")
        sys.exit(1)

    raw = sys.argv[1]
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)

    # Support either bare list or {blocks, text} object
    if isinstance(data, list):
        blocks = data
        fallback_text = "Daily Summary from your Chief of Staff"
    else:
        blocks = data.get("blocks", [])
        fallback_text = data.get("text", "Daily Summary from your Chief of Staff")

    post_to_slack(blocks, fallback_text)
