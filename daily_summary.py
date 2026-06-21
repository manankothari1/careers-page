#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
Formats the Granola meeting summary and sends it to Slack.

This script is called by the Cursor Cloud Agent after it has gathered
meeting data via the Granola MCP. Pass the formatted message as an
argument, or run it standalone to test Slack connectivity.

Environment variables required:
  SLACK_BOT_TOKEN   — Slack bot token (xoxb-...) with chat:write scope
  SLACK_CHANNEL_ID  — Slack channel/DM ID (default: D06E4QMHCNN)
"""

import os
import sys
import argparse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")


def send_slack_message(message: str, channel: str = SLACK_CHANNEL_ID) -> bool:
    if not SLACK_BOT_TOKEN:
        print("[WARN] SLACK_BOT_TOKEN not set. Message preview:\n")
        print(message)
        print("\n[INFO] Add SLACK_BOT_TOKEN to Cursor Cloud Agent Secrets to enable delivery.")
        return False

    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        resp = client.chat_postMessage(channel=channel, text=message, mrkdwn=True)
        print(f"[OK] Message delivered to {channel} (ts={resp['ts']})")
        return True
    except SlackApiError as e:
        print(f"[ERROR] Slack API: {e.response['error']}")
        return False


def build_no_meetings_message(date_str: str) -> str:
    return (
        f"*📋 Daily Briefing — {date_str}*\n\n"
        "No meetings recorded today. Enjoy the downtime! 🎉\n\n"
        "_— Your Chief of Staff_"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send daily summary to Slack")
    parser.add_argument("--message", "-m", help="Pre-formatted Slack message to send")
    parser.add_argument("--channel", "-c", default=SLACK_CHANNEL_ID, help="Slack channel ID")
    parser.add_argument("--test", action="store_true", help="Test Slack connectivity with a ping")
    args = parser.parse_args()

    if args.test:
        send_slack_message("👋 Chief of Staff automation is connected and running!", args.channel)
    elif args.message:
        send_slack_message(args.message, args.channel)
    else:
        print("Usage: python daily_summary.py --message 'your message' [--channel CHANNEL_ID]")
        print("       python daily_summary.py --test")
        sys.exit(1)
