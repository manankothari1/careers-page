#!/usr/bin/env python3
"""
Fallback Slack message sender for the daily chief-of-staff automation.
Requires SLACK_BOT_TOKEN environment variable (set as a Cursor secret).

Usage:
    python3 send_slack_message.py <channel_id> <message_text>

Or import and call send_message() directly.
"""

import os
import sys
import json
from datetime import datetime


def send_message(channel: str, text: str) -> bool:
    """Send a message to a Slack channel using the Web API."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN environment variable is not set.")
        print("Add it as a Cursor secret at: Cursor Dashboard → Cloud Agents → Secrets")
        return False

    try:
        from slack_sdk import WebClient
        from slack_sdk.errors import SlackApiError

        client = WebClient(token=token)
        response = client.chat_postMessage(
            channel=channel,
            text=text,
            mrkdwn=True,
        )
        print(f"Message sent successfully. Timestamp: {response['ts']}")
        return True

    except ImportError:
        # Fallback to raw HTTP if slack_sdk isn't installed
        import urllib.request
        import urllib.error

        payload = json.dumps({
            "channel": channel,
            "text": text,
            "mrkdwn": True,
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://slack.com/api/chat.postMessage",
            data=payload,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {token}",
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode())
                if result.get("ok"):
                    print(f"Message sent successfully. Timestamp: {result.get('ts')}")
                    return True
                else:
                    print(f"Slack API error: {result.get('error')}")
                    return False
        except urllib.error.URLError as e:
            print(f"Network error sending to Slack: {e}")
            return False

    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        return False


def build_daily_summary_message(date_str: str, meetings_data: dict) -> str:
    """
    Build the formatted daily summary message.
    This is a template — the AI agent composes the actual content each day.
    """
    return f"Chief of Staff Daily Summary for {date_str}\n\n{meetings_data}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_slack_message.py <channel_id> <message>")
        print("Example: python3 send_slack_message.py D06E4QMHCNN 'Hello!'")
        sys.exit(1)

    channel_id = sys.argv[1]
    message = sys.argv[2]

    success = send_message(channel_id, message)
    sys.exit(0 if success else 1)
