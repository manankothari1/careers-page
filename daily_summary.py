#!/usr/bin/env python3
"""
Daily PM Summary — Chief of Staff Automation
Sends a daily Slack summary of Granola meeting decisions, action items, and follow-ups.

This script is the fallback sender for the Cursor Cloud Agent automation.
It reads a pre-built message payload and sends it via the Slack Web API.

Required environment variable:
  SLACK_BOT_TOKEN - Slack bot OAuth token (xoxb-...)

Optional environment variable:
  SLACK_CHANNEL   - Override the default channel (defaults to D06E4QMHCNN)
"""

import os
import json
import sys
import urllib.request
import urllib.error


SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def send_slack_message(text: str, blocks: list = None) -> dict:
    """Send a message to Slack via the Web API."""
    if not SLACK_BOT_TOKEN:
        raise ValueError(
            "SLACK_BOT_TOKEN environment variable is not set.\n"
            "Add your Slack bot token as a secret in:\n"
            "  Cursor Dashboard > Cloud Agents > Secrets > SLACK_BOT_TOKEN\n\n"
            "Alternatively, authenticate the Slack MCP server in Cursor IDE."
        )

    payload = {"channel": SLACK_CHANNEL, "text": text}
    if blocks:
        payload["blocks"] = blocks

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}")

    return result


def build_blocks(meetings: list, date_str: str, top_priorities: list, cos_take: str) -> list:
    """Build Slack Block Kit blocks from structured meeting data."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your Daily PM Briefing -- {date_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    for meeting in meetings:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": meeting},
            }
        )
        blocks.append({"type": "divider"})

    priorities_text = "*Your Top Priorities for Tomorrow:*\n\n" + "\n".join(
        f"{i + 1}. {p}" for i, p in enumerate(top_priorities)
    )
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": priorities_text}})
    blocks.append({"type": "divider"})
    blocks.append(
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Chief of Staff Take:*\n{cos_take}"},
        }
    )
    blocks.append({"type": "divider"})
    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"_Your Chief of Staff -- powered by Granola + Cursor Cloud Agent | {date_str}_",
                }
            ],
        }
    )
    return blocks


if __name__ == "__main__":
    # Read JSON payload from stdin or first argument
    if len(sys.argv) > 1:
        payload = json.loads(sys.argv[1])
    else:
        payload = json.loads(sys.stdin.read())

    result = send_slack_message(
        text=payload.get("text", "Daily PM Briefing"),
        blocks=payload.get("blocks"),
    )
    print(f"Sent: ts={result.get('ts')}, channel={result.get('channel')}")
