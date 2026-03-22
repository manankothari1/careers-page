#!/usr/bin/env python3
"""
Chief of Staff Daily Summary — Slack sender utility.

Usage (called by the Cursor automation agent):
    python3 daily_summary.py '<json_blocks_payload>'

The agent (daily_summary automation) handles all Granola queries and message
construction. This script's sole job is to POST the pre-built Slack Block Kit
payload to the Slack API.

Required environment variable:
    SLACK_TOKEN  — Slack Bot Token with chat:write scope
                   Add via Cursor Dashboard > Cloud Agents > Secrets

Slack DM channel:
    D06E4QMHCNN  (Manan Kothari)
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_API_URL = "https://slack.com/api/chat.postMessage"


def send_slack_message(blocks: list, text_fallback: str = "") -> dict:
    """POST a Block Kit message to Slack. Returns the API response dict."""
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("[daily_summary] WARNING: SLACK_TOKEN not set. Message not sent.")
        print("[daily_summary] Add SLACK_TOKEN in Cursor Dashboard > Cloud Agents > Secrets")
        print("\n--- MESSAGE PREVIEW ---")
        print(json.dumps({"channel": SLACK_CHANNEL, "blocks": blocks}, indent=2, ensure_ascii=False))
        return {"ok": False, "error": "no_token"}

    payload = {
        "channel": SLACK_CHANNEL,
        "text": text_fallback or "Daily summary from your Chief of Staff.",
        "blocks": blocks,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        SLACK_API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"[daily_summary] ✓ Message sent successfully (ts={result.get('ts')})")
            else:
                print(f"[daily_summary] ✗ Slack API error: {result.get('error')}")
            return result
    except urllib.error.HTTPError as e:
        print(f"[daily_summary] HTTP error {e.code}: {e.reason}")
        return {"ok": False, "error": str(e)}
    except urllib.error.URLError as e:
        print(f"[daily_summary] Network error: {e.reason}")
        return {"ok": False, "error": str(e)}


def build_no_meetings_block(date_str: str, context: str = "") -> list:
    """Block Kit layout for days with no recorded meetings."""
    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"📋 Daily Brief — {date_str}", "emoji": True},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "No meetings recorded today — battery recharged. Here's what matters right now:",
            },
        },
    ]
    if context:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": context}})
    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"_Your Chief of Staff • {date_str} • 5:00 PM PT_",
                }
            ],
        }
    )
    return blocks


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 daily_summary.py '<blocks_json>'")
        print("       The agent passes the pre-built Block Kit JSON array as argv[1].")
        sys.exit(1)

    try:
        blocks = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"[daily_summary] Invalid JSON payload: {e}")
        sys.exit(1)

    result = send_slack_message(blocks)
    sys.exit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
