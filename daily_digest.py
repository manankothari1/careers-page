#!/usr/bin/env python3
"""
Daily Meeting Digest - Chief of Staff Automation
Fetches Granola meeting notes for the current day and sends a summary to Slack.

Requires: SLACK_BOT_TOKEN environment variable with a Slack bot token
          that has chat:write permissions.
"""

import os
import sys
from datetime import datetime, timezone, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


SLACK_CHANNEL = "D06E4QMHCNN"


def build_digest_message(date_label: str, meetings_summary: str) -> str:
    """Format the full digest message for Slack."""
    return f"""🌟 *Hey Manan! Your Chief of Staff here — here's your daily wrap-up for {date_label}* 🌟

You crushed it today. Here's a full breakdown of every key decision, action item, and follow-up from your calls:

{meetings_summary}

---
_You've got a lot of irons in the fire and you're handling it all with clarity and speed. Keep crushing it! 💪_
_— Your Chief of Staff_"""


def send_slack_message(token: str, channel: str, message: str) -> bool:
    """Send a message to Slack. Returns True on success."""
    client = WebClient(token=token)
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message,
            mrkdwn=True,
        )
        print(f"Message sent successfully. ts={response['ts']}")
        return True
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}", file=sys.stderr)
        return False


def main():
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print(
            "ERROR: SLACK_BOT_TOKEN environment variable not set.\n"
            "Please add your Slack Bot Token as a secret in the Cursor Cloud Agent dashboard.\n"
            "The token needs the 'chat:write' scope.",
            file=sys.stderr,
        )
        sys.exit(1)

    # This script is called with the pre-compiled digest as stdin or as an arg.
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        message = sys.stdin.read()

    success = send_slack_message(token, SLACK_CHANNEL, message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
