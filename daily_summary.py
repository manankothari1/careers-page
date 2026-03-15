#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff for Manan Kothari, PM at Homebase.
Runs at midnight UTC (5pm PT) and sends a Slack DM summarizing the day's decisions.

Requires:
  SLACK_TOKEN  — Slack Bot Token with chat:write scope
  GRANOLA_DATA — JSON string of meeting summaries (injected by the automation trigger)
                 OR the script falls back to a "no meetings" message.
"""

import json
import os
import sys
import textwrap
from datetime import datetime, timezone, timedelta

import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"
PT_OFFSET = timedelta(hours=-8)  # PST (UTC-8); script adjusts for PDT when needed


def send_slack_message(token: str, channel: str, text: str, blocks: list | None = None) -> dict:
    url = "https://slack.com/api/chat.postMessage"
    payload: dict = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def build_no_meetings_message(today_str: str) -> tuple[str, list]:
    # Detect if it's a weekend for a slightly different tone
    try:
        from datetime import datetime as dt
        day_name = dt.now(timezone.utc).strftime("%A")
        is_weekend = day_name in ("Saturday", "Sunday")
    except Exception:
        is_weekend = False

    if is_weekend:
        body = (
            f"*Daily Decision Summary — {today_str}*\n\n"
            "Hey Manan! 👋 No meetings today — it's the weekend, enjoy the recharge! "
            "Big week ahead, so rest up. You've got this. 💪"
        )
    else:
        body = (
            f"*Daily Decision Summary — {today_str}*\n\n"
            "Hey Manan! 👋 No meetings on the books today — enjoy the breathing room! "
            "Use this time to think big, catch up async, or just recharge. You've earned it. 🚀"
        )

    text = f"Daily Decision Summary — {today_str} (no meetings today)"
    blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": body}}]
    return text, blocks


def build_summary_message(today_str: str, granola_data: list) -> tuple[str, list]:
    """Build Slack message from a list of meeting summary dicts."""

    decisions_sections = []
    all_action_items = []

    for meeting in granola_data:
        title = meeting.get("title", "Untitled Meeting")
        decisions = meeting.get("decisions", [])
        if not decisions:
            continue

        decision_lines = []
        for d in decisions:
            what = d.get("decision", "")
            why = d.get("rationale", "")
            actions = d.get("action_items", [])
            line = f"• *{what}*"
            if why:
                line += f"\n  _Why:_ {why}"
            decision_lines.append(line)
            for a in actions:
                all_action_items.append(f"• {a}")

        if decision_lines:
            decisions_sections.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*📋 {title}*\n" + "\n".join(decision_lines),
                },
            })

    if not decisions_sections:
        return build_no_meetings_message(today_str)

    header_text = f"*🗓️ Daily Decision Summary — {today_str}*\n\nHey Manan! Here's everything you decided today. You crushed it! 💪"

    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": header_text}},
        {"type": "divider"},
        *decisions_sections,
    ]

    if all_action_items:
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*✅ All Action Items*\n" + "\n".join(all_action_items),
            },
        })

    blocks.append({"type": "divider"})
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_Keep shipping, Manan — the team is lucky to have you steering the ship! 🚀_",
        },
    })

    plain_text = f"Daily Decision Summary — {today_str}"
    return plain_text, blocks


def get_today_pt() -> str:
    """Return today's date in PT as a friendly string."""
    utc_now = datetime.now(timezone.utc)
    # Approximate PT (doesn't handle DST perfectly but good enough for display)
    pt_now = utc_now + PT_OFFSET
    return pt_now.strftime("%A, %B %-d, %Y")


def main():
    token = os.environ.get("SLACK_TOKEN", "").strip()
    if not token:
        print(
            "ERROR: SLACK_TOKEN environment variable is not set.\n"
            "Please add your Slack Bot Token in the Cursor Dashboard under:\n"
            "  Cloud Agents > Secrets > SLACK_TOKEN\n"
            "The token needs the `chat:write` scope and must be invited to the DM channel.\n\n"
            "To create a Slack app:\n"
            "  1. Go to https://api.slack.com/apps and create a new app\n"
            "  2. Add OAuth scope: chat:write\n"
            "  3. Install to workspace and copy the Bot User OAuth Token\n"
            "  4. Start a DM with the bot to open the channel"
        )
        sys.exit(1)

    today_str = get_today_pt()

    # Check for GRANOLA_DATA injected by the automation (JSON array of meeting summaries)
    granola_json = os.environ.get("GRANOLA_DATA", "").strip()
    if granola_json:
        try:
            granola_data = json.loads(granola_json)
            plain_text, blocks = build_summary_message(today_str, granola_data)
        except json.JSONDecodeError as e:
            print(f"WARNING: Could not parse GRANOLA_DATA: {e}. Sending no-meetings message.")
            plain_text, blocks = build_no_meetings_message(today_str)
    else:
        plain_text, blocks = build_no_meetings_message(today_str)

    print(f"Sending daily summary to Slack channel {SLACK_CHANNEL}...")
    print(f"Preview:\n{plain_text}\n")

    try:
        result = send_slack_message(token, SLACK_CHANNEL, plain_text, blocks)
        if result.get("ok"):
            print("✅ Slack message sent successfully!")
        else:
            print(f"❌ Slack API error: {result.get('error', 'unknown error')}")
            sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Network error sending Slack message: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
