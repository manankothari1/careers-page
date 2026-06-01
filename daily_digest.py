#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Runs daily at midnight UTC (5pm PDT) to summarize Granola meetings and send to Slack.

Required setup:
  - SLACK_BOT_TOKEN: Add as a Cursor Secret (Cloud Agents > Secrets)
  - Granola MCP: Configured in Cursor MCP settings
  - Slack MCP: Authenticated in Cursor MCP settings (or use SLACK_BOT_TOKEN)

Slack channel: D06E4QMHCNN
"""

import os
import sys
import json
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SLACK_CHANNEL_ID = "D06E4QMHCNN"
PDT_OFFSET = timedelta(hours=-7)  # PDT = UTC-7


def get_pdt_today() -> tuple[str, str]:
    """Return (start_iso, end_iso) for today in PDT as UTC ISO strings."""
    now_utc = datetime.now(timezone.utc)
    pdt_tz = timezone(PDT_OFFSET)
    now_pdt = now_utc.astimezone(pdt_tz)
    today_pdt = now_pdt.date()
    start = datetime(today_pdt.year, today_pdt.month, today_pdt.day, 0, 0, 0, tzinfo=pdt_tz)
    end = datetime(today_pdt.year, today_pdt.month, today_pdt.day, 23, 59, 59, tzinfo=pdt_tz)
    return start.astimezone(timezone.utc).isoformat(), end.astimezone(timezone.utc).isoformat()


def send_slack_message(text: str, blocks: Optional[list] = None) -> bool:
    """Send a message to Slack using the bot token."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        log.error("SLACK_BOT_TOKEN not set. Add it in Cursor Dashboard > Cloud Agents > Secrets.")
        log.info("--- Message that would have been sent ---\n%s", text)
        return False

    try:
        from slack_sdk import WebClient
        from slack_sdk.errors import SlackApiError

        client = WebClient(token=token)
        kwargs = {"channel": SLACK_CHANNEL_ID, "text": text}
        if blocks:
            kwargs["blocks"] = blocks

        response = client.chat_postMessage(**kwargs)
        log.info("Slack message sent successfully: ts=%s", response["ts"])
        return True

    except ImportError:
        log.error("slack_sdk not installed. Run: pip install slack_sdk")
        return False
    except SlackApiError as e:
        log.error("Slack API error: %s", e.response["error"])
        return False


def build_no_meetings_message(date_str: str) -> tuple[str, list]:
    """Build message for days with no meetings."""
    text = f"*Daily Decision Summary — {date_str}*\n\nNo meetings recorded today. Enjoy the rest! 🌅"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📋 Daily Decision Summary — {date_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "✅ *No meetings recorded today.* Your calendar was clear — great time to think, write, or recharge.",
            },
        },
    ]
    return text, blocks


def build_daily_summary_message(date_str: str, summary_content: str) -> tuple[str, list]:
    """Build the main daily summary Slack message with blocks."""
    fallback_text = f"Daily Decision Summary — {date_str}\n\n{summary_content}"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📋 Daily Decision Summary — {date_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": summary_content},
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Automatically generated from your Granola meeting notes by your Chief of Staff AI_ 🤝",
                }
            ],
        },
    ]
    return fallback_text, blocks


if __name__ == "__main__":
    # When run standalone (not via the Cursor Cloud Agent), this logs what would be sent.
    # In normal operation, the Cloud Agent uses the MCP tools directly and calls send_slack_message().
    start, end = get_pdt_today()
    pdt_tz = timezone(PDT_OFFSET)
    today_str = datetime.now(timezone.utc).astimezone(pdt_tz).strftime("%A, %B %-d, %Y")
    log.info("Daily digest for: %s (UTC range: %s to %s)", today_str, start, end)
    log.info("SLACK_BOT_TOKEN present: %s", bool(os.environ.get("SLACK_BOT_TOKEN")))
    log.info("This script is intended to be driven by the Cursor Cloud Agent + Granola MCP.")
    log.info("See README.md for setup instructions.")
