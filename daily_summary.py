#!/usr/bin/env python3
"""
Daily Meeting Summary - Chief of Staff Automation
Reads meeting data from Granola and sends a daily summary to Slack.

Required environment variable:
  SLACK_BOT_TOKEN: A Slack Bot OAuth token (xoxb-...) with chat:write permissions
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(token: str, channel: str, blocks: list, text: str) -> dict:
    """Send a message to Slack using the Web API."""
    url = "https://slack.com/api/chat.postMessage"
    payload = json.dumps({
        "channel": channel,
        "text": text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=10) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}")

    return result


def build_summary_blocks(date_str: str, summary_sections: list) -> list:
    """Build Slack block kit message for the daily summary."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📋 Your Daily Debrief — {date_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    for section in summary_sections:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": section,
            },
        })
        blocks.append({"type": "divider"})

    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Your Chief of Staff — powered by Granola + Cursor AI_ ✨",
            }
        ],
    })

    return blocks


def main():
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN environment variable is not set.")
        print("Please add it as a secret in Cursor Cloud Agents > Secrets.")
        sys.exit(1)

    # Summary is passed in as a JSON file argument or via stdin
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    date_str = data.get("date", datetime.now(timezone.utc).strftime("%B %d, %Y"))
    sections = data.get("sections", [])
    plain_text = data.get("plain_text", "Daily meeting summary from your Chief of Staff.")

    blocks = build_summary_blocks(date_str, sections)

    print(f"Sending daily summary to Slack channel {SLACK_CHANNEL}...")
    result = send_slack_message(token, SLACK_CHANNEL, blocks, plain_text)
    print(f"Message sent successfully! ts={result.get('ts')}")


if __name__ == "__main__":
    main()
