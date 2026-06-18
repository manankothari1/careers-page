#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
Runs daily at 5pm PDT, reviews all Granola meetings for the day,
and sends a structured summary to Slack channel D06E4QMHCNN.
"""

import os
import json
import datetime
import requests
from zoneinfo import ZoneInfo

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")

# ── Helpers ──────────────────────────────────────────────────────────────────

def slack_post(text: str, blocks: list | None = None) -> dict:
    """Send a message to Slack via the Web API."""
    if not SLACK_BOT_TOKEN:
        raise RuntimeError(
            "SLACK_BOT_TOKEN is not set. "
            "Add it as a Cursor secret in the Dashboard (Cloud Agents > Secrets)."
        )
    payload: dict = {"channel": SLACK_CHANNEL, "text": text}
    if blocks:
        payload["blocks"] = blocks
    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}", "Content-Type": "application/json"},
        json=payload,
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("ok"):
        raise RuntimeError(f"Slack API error: {data.get('error')}")
    return data


def today_pdt() -> tuple[str, str]:
    """Return ISO date strings for start/end of today in PDT."""
    pdt = ZoneInfo("America/Los_Angeles")
    now = datetime.datetime.now(tz=pdt)
    start = now.replace(hour=0, minute=0, second=0, microsecond=0).astimezone(ZoneInfo("UTC"))
    end = now.replace(hour=23, minute=59, second=59, microsecond=0).astimezone(ZoneInfo("UTC"))
    return start.isoformat(), end.isoformat()


# ── Message builder ───────────────────────────────────────────────────────────

def build_message(summary_text: str, date_label: str) -> tuple[str, list]:
    """Return (fallback_text, blocks) for the Slack message."""
    fallback = f"Daily Decision Summary — {date_label}"
    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"📋 Daily Decision Summary — {date_label}", "emoji": True},
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": summary_text},
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Generated automatically by your Chief of Staff 🤝 · Powered by Granola + Cursor_",
                }
            ],
        },
    ]
    return fallback, blocks


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # This script is invoked by the Cursor Cloud Agent cron automation.
    # The Granola data is fetched via MCP; the composed summary is passed in
    # via stdin or a JSON file written by the agent.  The script's sole job
    # is to POST the final message to Slack.
    import sys

    if len(sys.argv) < 2:
        print("Usage: python daily_summary.py <summary_json_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        payload = json.load(f)

    date_label = payload["date_label"]
    summary_text = payload["summary"]

    fallback, blocks = build_message(summary_text, date_label)
    result = slack_post(fallback, blocks)
    print(f"✅ Message sent — ts={result.get('ts')}")
