#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Runs at 5pm PDT every day, reviews Granola meetings, and sends a Slack summary
of all decisions made during the day with action items and rationale.

Required environment variables:
  GRANOLA_API_KEY   - from Granola desktop app: Settings → Connectors → API keys
  SLACK_BOT_TOKEN   - Slack bot token with chat:write scope
  SLACK_CHANNEL_ID  - Slack channel/DM ID (default: D06E4QMHCNN)
"""

import os
import sys
import json
import requests
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

PDT = ZoneInfo("America/Los_Angeles")
GRANOLA_API_BASE = "https://public-api.granola.ai/v1"
SLACK_API_BASE = "https://slack.com/api"
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")


def granola_headers():
    key = os.environ.get("GRANOLA_API_KEY", "")
    if not key:
        raise ValueError("GRANOLA_API_KEY environment variable is not set.")
    return {"Authorization": f"Bearer {key}"}


def slack_headers():
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
    }


def get_today_meetings():
    now_pdt = datetime.now(PDT)
    start_of_day = now_pdt.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = now_pdt.replace(hour=23, minute=59, second=59, microsecond=0)

    params = {
        "created_after": start_of_day.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "created_before": end_of_day.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    all_notes = []
    cursor = None
    while True:
        if cursor:
            params["cursor"] = cursor
        resp = requests.get(
            f"{GRANOLA_API_BASE}/notes",
            headers=granola_headers(),
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        all_notes.extend(data.get("notes", []))
        if not data.get("hasMore"):
            break
        cursor = data.get("cursor")

    return all_notes


def get_note_detail(note_id):
    resp = requests.get(
        f"{GRANOLA_API_BASE}/notes/{note_id}",
        headers=granola_headers(),
        params={"include": "transcript"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def format_time_pdt(iso_str):
    if not iso_str:
        return "Unknown time"
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return dt.astimezone(PDT).strftime("%-I:%M %p")


def build_slack_message(meetings_detail, date_str):
    """Build a rich Slack Block Kit message from meeting details."""

    total = len(meetings_detail)
    header_text = (
        f":sunny: *Daily Decision Digest — {date_str}*\n"
        f"Here's your end-of-day rundown, Manan! You had *{total} meeting{'s' if total != 1 else ''}* today. "
        f"Below are all the key decisions, action items, and context I pulled together for you. "
        f"You crushed it today — let's make sure nothing slips through the cracks. :rocket:"
    )

    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": f"Chief of Staff Digest — {date_str}", "emoji": True}},
        {"type": "section", "text": {"type": "mrkdwn", "text": header_text}},
        {"type": "divider"},
    ]

    for idx, meeting in enumerate(meetings_detail):
        title = meeting.get("title") or meeting.get("name") or "Untitled Meeting"
        started_at = format_time_pdt(meeting.get("started_at") or meeting.get("created_at", ""))
        summary = meeting.get("summary") or meeting.get("ai_summary") or ""

        meeting_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{idx + 1}. {title}* — _{started_at} PDT_",
            },
        }
        blocks.append(meeting_block)

        if summary:
            summary_lines = summary.strip().split("\n")
            trimmed = "\n".join(summary_lines[:60])
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": trimmed},
            })
        else:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "_No summary available for this meeting._"},
            })

        if idx < len(meetings_detail) - 1:
            blocks.append({"type": "divider"})

    blocks.append({"type": "divider"})
    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": f":robot_face: Generated automatically by your Chief of Staff bot at 5pm PDT • {date_str}",
            }
        ],
    })

    return {
        "channel": SLACK_CHANNEL_ID,
        "text": f"Daily Decision Digest — {date_str}",
        "blocks": blocks,
    }


def send_slack_message(payload):
    resp = requests.post(
        f"{SLACK_API_BASE}/chat.postMessage",
        headers=slack_headers(),
        data=json.dumps(payload),
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}")
    return result


def main():
    print(f"[Chief of Staff] Starting daily summary run at {datetime.now(PDT).strftime('%Y-%m-%d %I:%M %p PDT')}")

    try:
        print("[Chief of Staff] Fetching today's meetings from Granola...")
        notes = get_today_meetings()
        print(f"[Chief of Staff] Found {len(notes)} meetings.")

        if not notes:
            print("[Chief of Staff] No meetings today. Sending a light check-in to Slack.")
            date_str = datetime.now(PDT).strftime("%A, %B %-d, %Y")
            payload = {
                "channel": SLACK_CHANNEL_ID,
                "text": f":calendar: *Daily Check-in — {date_str}*\nNo Granola meetings recorded today, Manan! Enjoy the quiet day — you've earned it. :tada:",
            }
        else:
            detailed = []
            for note in notes:
                note_id = note.get("id")
                if note_id:
                    try:
                        detail = get_note_detail(note_id)
                        detailed.append(detail)
                    except Exception as e:
                        print(f"[Chief of Staff] Warning: could not fetch detail for {note_id}: {e}")
                        detailed.append(note)

            date_str = datetime.now(PDT).strftime("%A, %B %-d, %Y")
            payload = build_slack_message(detailed, date_str)

        print("[Chief of Staff] Sending Slack message...")
        result = send_slack_message(payload)
        print(f"[Chief of Staff] Message sent successfully! ts={result.get('ts')}")

    except ValueError as e:
        print(f"[Chief of Staff] Configuration error: {e}")
        print("Please set the required environment variables (GRANOLA_API_KEY, SLACK_BOT_TOKEN).")
        sys.exit(1)
    except Exception as e:
        print(f"[Chief of Staff] Unexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
