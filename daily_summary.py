#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff for Manan Kothari @ Homebase
Runs daily at 5pm PDT. Reviews Granola meetings and sends a Slack summary.

Required env vars:
  SLACK_BOT_TOKEN   — Slack bot token (xoxb-...) with chat:write scope
  SLACK_CHANNEL_ID  — Defaults to D06E4QMHCNN

Optional env vars:
  GRANOLA_API_KEY   — grn_... key for direct Granola API access
  DRY_RUN           — Set to "1" to print message without sending
"""

import os
import sys
import json
import datetime
import requests
from typing import Optional


SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
GRANOLA_API_KEY = os.environ.get("GRANOLA_API_KEY", "")
DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"

GRANOLA_BASE = "https://public-api.granola.ai/v1"


def get_today_range_pdt():
    """Returns start/end ISO timestamps for today in PDT (UTC-7)."""
    now_utc = datetime.datetime.utcnow()
    pdt_offset = datetime.timedelta(hours=7)
    now_pdt = now_utc - pdt_offset
    today_pdt = now_pdt.date()
    start = datetime.datetime(today_pdt.year, today_pdt.month, today_pdt.day)
    end = start + datetime.timedelta(days=1)
    start_utc = start + pdt_offset
    end_utc = end + pdt_offset
    return start_utc.isoformat() + "Z", end_utc.isoformat() + "Z"


def fetch_granola_meetings(start_iso: str, end_iso: str) -> list[dict]:
    """Fetch meetings from Granola API for the given time range."""
    if not GRANOLA_API_KEY:
        raise ValueError("GRANOLA_API_KEY not set")

    headers = {"Authorization": f"Bearer {GRANOLA_API_KEY}"}
    params = {
        "created_after": start_iso,
        "created_before": end_iso,
        "page_size": 30,
    }
    meetings = []
    cursor = None

    while True:
        if cursor:
            params["cursor"] = cursor
        resp = requests.get(f"{GRANOLA_BASE}/notes", headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        notes = data.get("notes", [])
        meetings.extend(notes)
        if not data.get("hasMore") or not data.get("cursor"):
            break
        cursor = data["cursor"]

    return meetings


def get_meeting_detail(meeting_id: str) -> Optional[dict]:
    """Fetch full meeting detail including transcript and summary."""
    if not GRANOLA_API_KEY:
        return None
    headers = {"Authorization": f"Bearer {GRANOLA_API_KEY}"}
    resp = requests.get(
        f"{GRANOLA_BASE}/notes/{meeting_id}",
        headers=headers,
        params={"include": "transcript,summary,notes"},
        timeout=30,
    )
    if resp.ok:
        return resp.json()
    return None


def send_slack_message(channel: str, blocks: list, text: str) -> bool:
    """Send a message to Slack using the Web API."""
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN not set. Cannot send Slack message.", file=sys.stderr)
        return False

    if DRY_RUN:
        print("=== DRY RUN — Slack message would be sent ===")
        print(f"Channel: {channel}")
        print(json.dumps(blocks, indent=2))
        return True

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        json={
            "channel": channel,
            "text": text,
            "blocks": blocks,
            "unfurl_links": False,
        },
        timeout=15,
    )
    result = resp.json()
    if not result.get("ok"):
        print(f"ERROR sending Slack message: {result.get('error')}", file=sys.stderr)
        return False
    print(f"Slack message sent successfully (ts={result.get('ts')})")
    return True


def build_no_meetings_message(date_str: str) -> tuple[list, str]:
    """Build a friendly message for days with no recorded meetings."""
    text = f"Daily Summary for {date_str} — No meetings recorded today"
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your Daily Briefing — {date_str}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! Looks like a quiet day with no recorded Granola meetings. "
                    "Enjoy the breather — you've earned it! Use this time to reflect, "
                    "get ahead on async work, or just recharge. See you tomorrow!"
                ),
            },
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"_Your Chief of Staff | {date_str} | Homebase_",
                }
            ],
        },
    ]
    return blocks, text


def build_summary_message(date_str: str, meetings_data: list[dict]) -> tuple[list, str]:
    """
    Build the Slack message blocks from pre-processed meeting data.
    `meetings_data` is a list of dicts with keys: title, time, attendees, summary
    """
    meeting_count = len(meetings_data)
    text = f"Daily Summary for {date_str} — {meeting_count} meeting{'s' if meeting_count != 1 else ''} reviewed"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your Daily Briefing — {date_str}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"Hey Manan! You absolutely crushed it today — "
                    f"{meeting_count} meeting{'s' if meeting_count != 1 else ''} packed "
                    f"with real progress on Homebase's hiring product. "
                    f"Here's your complete decision log and what needs to happen next."
                ),
            },
        },
        {"type": "divider"},
    ]

    for i, mtg in enumerate(meetings_data, 1):
        title = mtg.get("title", "Untitled Meeting")
        time_str = mtg.get("time", "")
        attendees = mtg.get("attendees", "")
        summary_text = mtg.get("summary", "")

        meeting_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"*{i}. {title}*"
                    + (f"  |  _{time_str}_" if time_str else "")
                    + (f"\n_With: {attendees}_" if attendees else "")
                    + f"\n\n{summary_text}"
                ),
            },
        }
        blocks.append(meeting_block)

        if i < meeting_count:
            blocks.append({"type": "divider"})

    blocks.append({"type": "divider"})
    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"_Your Chief of Staff | {date_str} | Homebase_",
                }
            ],
        }
    )
    return blocks, text


def main():
    now_utc = datetime.datetime.utcnow()
    pdt_offset = datetime.timedelta(hours=7)
    now_pdt = now_utc - pdt_offset
    date_str = now_pdt.strftime("%A, %B %-d, %Y")

    if GRANOLA_API_KEY:
        start_iso, end_iso = get_today_range_pdt()
        print(f"Fetching Granola meetings for {date_str} ({start_iso} – {end_iso})")
        try:
            raw_meetings = fetch_granola_meetings(start_iso, end_iso)
        except Exception as e:
            print(f"ERROR fetching from Granola API: {e}", file=sys.stderr)
            raw_meetings = []
    else:
        print("GRANOLA_API_KEY not set. Pass meeting data via stdin or set the env var.")
        raw_meetings = []

    if "--meetings-json" in sys.argv:
        idx = sys.argv.index("--meetings-json")
        with open(sys.argv[idx + 1]) as f:
            raw_meetings = json.load(f)

    if not raw_meetings:
        print(f"No meetings found for {date_str}. Sending 'quiet day' message.")
        blocks, text = build_no_meetings_message(date_str)
    else:
        meetings_data = []
        for m in raw_meetings:
            meeting_id = m.get("id", "")
            title = m.get("title", "Untitled")
            created_at = m.get("createdAt", "")
            if created_at:
                try:
                    dt = datetime.datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    dt_pdt = dt - pdt_offset
                    time_str = dt_pdt.strftime("%-I:%M %p PDT")
                except Exception:
                    time_str = created_at
            else:
                time_str = ""

            participants = m.get("participants", [])
            attendees = ", ".join(
                p.get("name", p.get("email", "")) for p in participants if p.get("name") or p.get("email")
            )

            summary = m.get("summary", "") or m.get("notes", "")
            if not summary and meeting_id:
                detail = get_meeting_detail(meeting_id)
                if detail:
                    summary = detail.get("summary", "") or detail.get("notes", "")

            meetings_data.append(
                {
                    "title": title,
                    "time": time_str,
                    "attendees": attendees,
                    "summary": summary,
                }
            )
        blocks, text = build_summary_message(date_str, meetings_data)

    success = send_slack_message(SLACK_CHANNEL_ID, blocks, text)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
