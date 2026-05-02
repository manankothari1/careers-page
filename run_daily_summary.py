#!/usr/bin/env python3
"""
Orchestrator: Pulls today's Granola meetings (already fetched and provided as JSON),
formats them into a rich daily decision summary, and posts to Slack.

This script is designed to be called by the Cursor Cloud Agent automation
with the Granola meeting data already collected via MCP.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import date


SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL_ID = "D06E4QMHCNN"


def send_slack_message(channel: str, text: str, blocks: list = None) -> dict:
    url = "https://slack.com/api/chat.postMessage"
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_message(summary_markdown: str, today_str: str) -> tuple[str, list]:
    """Returns (fallback_text, blocks)."""
    fallback = f"Daily Decision Summary — {today_str}\n\n{summary_markdown}"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🌅 Daily Decision Summary — {today_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    # Slack blocks have a 3000 char limit per section; split into chunks
    chunk_size = 2900
    text = summary_markdown
    while text:
        chunk = text[:chunk_size]
        text = text[chunk_size:]
        blocks.append(
            {"type": "section", "text": {"type": "mrkdwn", "text": chunk}}
        )

    blocks += [
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "✨ You crushed it today, Manan. Every decision moves Homebase forward. Keep being awesome! 💪🏽",
                }
            ],
        },
    ]

    return fallback, blocks


def main(summary_markdown: str, today_str: str):
    if not SLACK_BOT_TOKEN:
        print(
            "❌ SLACK_BOT_TOKEN not set. Add it to Cursor Cloud Agent secrets.",
            file=sys.stderr,
        )
        sys.exit(1)

    fallback, blocks = build_message(summary_markdown, today_str)

    print(f"📤 Sending daily summary to Slack ({SLACK_CHANNEL_ID})...")
    result = send_slack_message(SLACK_CHANNEL_ID, fallback, blocks)

    if result.get("ok"):
        print("✅ Daily summary sent successfully!")
    else:
        error = result.get("error", "unknown error")
        print(f"❌ Slack API error: {error}", file=sys.stderr)
        if error == "token_revoked" or error == "invalid_auth":
            print(
                "   → Check that SLACK_BOT_TOKEN is valid and has chat:write scope.",
                file=sys.stderr,
            )
        sys.exit(1)


if __name__ == "__main__":
    # Called with (summary_markdown, today_str) from the agent
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            d = json.load(f)
        main(d["summary"], d["date"])
    else:
        d = json.load(sys.stdin)
        main(d["summary"], d["date"])
