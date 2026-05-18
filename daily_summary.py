#!/usr/bin/env python3
"""
Daily PM Summary Bot — Chief of Staff for Manan @ Homebase
Cron: 0 0 * * * (5pm PT / midnight UTC)

This script is called by the Cursor Cloud Agent automation with the
pre-synthesized summary and meeting list as command-line arguments.
It formats and posts to Slack via the Web API.

Usage:
    python3 daily_summary.py '<summary_text>' '<meetings_json>' '<date_str>'

Environment:
    SLACK_BOT_TOKEN  — Required. Slack Bot OAuth token (xoxb-...)
"""

import os
import sys
import json
import urllib.request
import urllib.error

SLACK_CHANNEL_ID = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def send_slack_message(channel: str, text: str, blocks: list = None) -> bool:
    if not SLACK_BOT_TOKEN:
        print("❌ SLACK_BOT_TOKEN not set. Add it as a Cursor secret.")
        print("   Go to: Cursor Dashboard → Cloud Agents → Secrets")
        return False

    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks
        payload["unfurl_links"] = False

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"✅ Message sent to Slack channel {channel}")
                return True
            print(f"❌ Slack error: {result.get('error', 'unknown')}")
            return False
    except urllib.error.URLError as exc:
        print(f"❌ Network error: {exc}")
        return False


def build_blocks(date_str: str, summary: str, meeting_titles: list) -> list:
    titles_str = "  •  ".join(meeting_titles) if meeting_titles else "_None recorded today_"

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your Daily Debrief — {date_str}",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hey Manan! Your chief of staff here with today's wrap-up. You had a full day — here's everything that matters. :muscle:",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Meetings reviewed:* {titles_str}",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": summary,
            },
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Your AI chief of staff — powered by Granola + Cursor Automation — sent every weekday at 5pm PT_",
                }
            ],
        },
    ]


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 daily_summary.py '<summary>' '<meetings_json>' '<date_str>'")
        sys.exit(1)

    summary = sys.argv[1]
    meetings = json.loads(sys.argv[2])
    date_str = sys.argv[3]
    meeting_titles = [m.get("title", "Untitled") for m in meetings]

    blocks = build_blocks(date_str, summary, meeting_titles)
    fallback = f"Daily Debrief for {date_str} — {len(meetings)} meetings reviewed."

    success = send_slack_message(SLACK_CHANNEL_ID, fallback, blocks)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
