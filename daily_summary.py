#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff for Manan Kothari @ Homebase
Runs at midnight UTC (5pm PT) and reviews today's Granola meetings,
then sends a Slack summary of decisions, action items, and follow-ups.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, date, timezone, timedelta


SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL_ID = "D06E4QMHCNN"

# Granola MCP is called externally - this script handles the Slack posting
# Meeting summaries are passed in as JSON via stdin or as a JSON file argument


def send_slack_message(channel: str, text: str, blocks: list = None) -> dict:
    """Post a message to Slack using the Web API."""
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
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        print(f"Slack HTTP error: {e.code} {e.reason}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Slack error: {e}", file=sys.stderr)
        raise


def build_slack_blocks(summary_text: str, today_str: str) -> list:
    """Build rich Slack Block Kit message."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🌅 Your Daily Decision Summary — {today_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": summary_text,
            },
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "✨ You crushed it today, Manan. Tomorrow is another chance to move the needle. 💪",
                }
            ],
        },
    ]
    return blocks


def format_summary(meetings_data: list) -> str:
    """Format the meetings data into a clean Slack summary."""
    lines = []

    for meeting in meetings_data:
        title = meeting.get("title", "Untitled Meeting")
        time = meeting.get("time", "")
        participants = meeting.get("participants", "")
        decisions = meeting.get("decisions", [])
        action_items = meeting.get("action_items", [])
        rationale = meeting.get("rationale", "")

        lines.append(f"*📅 {title}*" + (f" _{time}_" if time else ""))
        if participants:
            lines.append(f"_With: {participants}_")
        lines.append("")

        if decisions:
            lines.append("*Decisions Made:*")
            for d in decisions:
                lines.append(f"• {d}")
            lines.append("")

        if action_items:
            lines.append("*Action Items / Follow-ups:*")
            for a in action_items:
                lines.append(f"✅ {a}")
            lines.append("")

        if rationale:
            lines.append(f"*Why it matters:* {rationale}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN environment variable not set.", file=sys.stderr)
        print(
            "Please add SLACK_BOT_TOKEN to your Cursor Cloud Agent secrets.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Accept summary JSON from stdin or first argument
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    today_str = data.get("date", date.today().strftime("%A, %B %d, %Y"))
    meetings = data.get("meetings", [])
    summary_text = data.get("summary_text", "")

    if not summary_text and meetings:
        summary_text = format_summary(meetings)

    if not summary_text:
        summary_text = "No meetings recorded today."

    blocks = build_slack_blocks(summary_text, today_str)
    fallback_text = f"Daily Decision Summary for {today_str}\n\n{summary_text}"

    print(f"Sending summary for {today_str} to {SLACK_CHANNEL_ID}...")
    result = send_slack_message(SLACK_CHANNEL_ID, fallback_text, blocks)

    if result.get("ok"):
        print("✅ Summary sent successfully!")
    else:
        print(f"❌ Slack error: {result.get('error', 'unknown')}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
