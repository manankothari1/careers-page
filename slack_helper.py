#!/usr/bin/env python3
"""
Slack message sender fallback for daily decision summary automation.
Uses SLACK_BOT_TOKEN environment variable to send messages via Slack Web API.

Usage:
    python3 slack_helper.py <channel_id> <message>

Or import and use send_message() directly.
"""

import os
import sys
import json
import urllib.request
import urllib.parse


def send_message(channel: str, text: str, token: str | None = None) -> dict:
    """
    Send a message to a Slack channel using the Slack Web API.

    Args:
        channel: Slack channel ID (e.g. "D06E4QMHCNN")
        text: Message text (supports Slack mrkdwn formatting)
        token: Slack bot token. If None, uses SLACK_BOT_TOKEN env variable.

    Returns:
        dict: Slack API response

    Raises:
        ValueError: If no token is available
        RuntimeError: If the API call fails
    """
    token = token or os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError(
            "No Slack bot token available. "
            "Set SLACK_BOT_TOKEN environment variable or pass token argument."
        )

    payload = {
        "channel": channel,
        "text": text,
        "mrkdwn": True,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown error')}")

    return result


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <channel_id> <message>", file=sys.stderr)
        sys.exit(1)

    channel = sys.argv[1]
    message = sys.argv[2]

    try:
        result = send_message(channel, message)
        print(f"Message sent successfully! ts={result.get('ts')}")
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Send failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
