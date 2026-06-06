#!/usr/bin/env python3
"""
Daily Decision Summary - Homebase PM Chief of Staff
Runs at end of business day, reviews all Granola meetings,
and sends a Slack summary of decisions, action items, and follow-ups.

Required environment variables:
  GRANOLA_API_TOKEN  - Granola API token
  SLACK_BOT_TOKEN    - Slack bot token (xoxb-...)
  SLACK_CHANNEL_ID   - Slack channel/DM ID (default: D06E4QMHCNN)
"""

import os
import json
import requests
from datetime import datetime, timezone, timedelta
from typing import Optional


SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
GRANOLA_API_TOKEN = os.environ.get("GRANOLA_API_TOKEN", "")

# Eastern timezone offset (EDT = UTC-4)
EDT = timezone(timedelta(hours=-4))


def get_today_edt() -> tuple[str, str]:
    """Return today's start and end in UTC ISO format based on EDT."""
    now_edt = datetime.now(EDT)
    start = datetime(now_edt.year, now_edt.month, now_edt.day, 0, 0, 0, tzinfo=EDT)
    end = datetime(now_edt.year, now_edt.month, now_edt.day, 23, 59, 59, tzinfo=EDT)
    return start.astimezone(timezone.utc).isoformat(), end.astimezone(timezone.utc).isoformat()


def send_slack_message(token: str, channel: str, text: str, blocks: Optional[list] = None) -> dict:
    """Send a message to Slack using the Web API."""
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks
    response = requests.post(url, headers=headers, json=payload, timeout=10)
    return response.json()


def build_slack_blocks(date_str: str, meetings_summary: list[dict]) -> list:
    """Build rich Slack blocks for the daily summary."""
    blocks = []

    # Header
    blocks.append({
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"🌅 Your Daily Decision Summary — {date_str}",
            "emoji": True
        }
    })

    blocks.append({"type": "divider"})

    # Intro section
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! 👋 Here's your end-of-day recap. "
                "You crushed a packed day — here's everything that matters, "
                "so you can close out clean and hit tomorrow ready to go. 💪"
            )
        }
    })

    blocks.append({"type": "divider"})

    for meeting in meetings_summary:
        if not meeting.get("decisions") and not meeting.get("action_items"):
            continue

        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*📋 {meeting['title']}* — _{meeting['time']}_"
            }
        })

        if meeting.get("decisions"):
            decisions_text = "\n".join(f"• {d}" for d in meeting["decisions"])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Decisions Made:*\n{decisions_text}"
                }
            })

        if meeting.get("action_items"):
            actions_text = "\n".join(f"☑️ {a}" for a in meeting["action_items"])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Action Items:*\n{actions_text}"
                }
            })

        if meeting.get("rationale"):
            blocks.append({
                "type": "context",
                "elements": [{
                    "type": "mrkdwn",
                    "text": f"💡 *Why it matters:* {meeting['rationale']}"
                }]
            })

        blocks.append({"type": "divider"})

    return blocks


def main():
    """Main entry point for the daily summary automation."""
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN environment variable not set.")
        print("Add it to your Cursor Cloud Agent secrets.")
        return

    today_edt = datetime.now(EDT).strftime("%A, %B %-d, %Y")

    # This data is populated by the Cursor agent via Granola MCP
    # For standalone script execution, wire in Granola API calls here
    meetings_summary = build_todays_summary()

    blocks = build_slack_blocks(today_edt, meetings_summary)

    # Plain text fallback
    text = f"Daily Decision Summary for {today_edt}"

    result = send_slack_message(SLACK_BOT_TOKEN, SLACK_CHANNEL_ID, text, blocks)

    if result.get("ok"):
        print(f"✅ Summary sent to {SLACK_CHANNEL_ID}")
    else:
        print(f"❌ Slack error: {result.get('error', 'Unknown error')}")
        print(json.dumps(result, indent=2))


def build_todays_summary() -> list[dict]:
    """
    Returns today's meetings summary data.
    In production, this is populated by the Cursor agent using Granola MCP.
    """
    return [
        {
            "title": "Jatin / Manan",
            "time": "11:00 AM EDT",
            "decisions": [],
            "action_items": [],
            "rationale": ""
        },
        {
            "title": "Hiring Leads Standup",
            "time": "11:30 AM EDT",
            "decisions": [
                "Q3 Plans due Monday morning (not over the weekend) — Manan submitting Monday AM",
                "Redshift being deprecated this month; full migration to Databricks as single data warehouse",
                "Looker being replaced by Omni over next 1–2 months (minimize new Looker additions now)",
                "Lean into product-led growth experimentation and make product benefits more obvious to users",
                "Name testing for 'Homebase Recruit' to move forward (Facebook test + Katie's initial positive signal)",
            ],
            "action_items": [
                "Submit Q3 plan Monday morning — center on ICP, Q3-specific timeline, and concrete impact numbers",
                "Flag any data pipeline mismatches to Nelson during Databricks transition",
                "Coordinate with Dana on intake experiment learnings to inform PLG strategy",
                "Set up Facebook name testing for 'Homebase Recruit' branding",
                "Get Ivana to provide CS candidate conversation examples for intake experiment expansion",
            ],
            "rationale": (
                "Q3 planning is the highest-stakes near-term deliverable. The data infrastructure shift "
                "(Redshift → Databricks, Looker → Omni) affects how all teams measure success, so flagging "
                "pipeline issues early prevents metric drift. The Boost first organic sale is a green shoot "
                "that validates the product direction — keep the momentum going."
            )
        },
        {
            "title": "Michael / Manan — Boost Modal & Job Flagging",
            "time": "12:00 PM EDT",
            "decisions": [
                "Boost modal experiment will target syndicated companies with no/low-risk jobs post job creation",
                "Three experiment pillars confirmed: tapping talent pool, easier OAM spending, funnel optimization",
                "OAMs inability to edit jobs in review status identified as a major product issue requiring fix",
                "Contact info flags may need reclassification from low → medium risk (to be evaluated)",
            ],
            "action_items": [
                "Discuss with Bob: how to handle flagged jobs that were already boosted (refund/re-boost flow)",
                "Schedule 4-person flow review meeting next week to align on the full boost + flagging workflow",
                "Investigate job editing capabilities in V2 platform — current 'copy job' workaround is broken UX",
                "Build admin dashboard for easy refund tracking on flagged+boosted jobs",
                "Explore real-time job validation to prevent contact info flagging before submission",
            ],
            "rationale": (
                "The boost modal is a direct revenue lever — but it only works if the downstream flagging "
                "and review flow doesn't create a broken experience for OAMs. Right now, 50% of flagged jobs "
                "are legitimate companies with formatting issues, and they can't even edit their job when "
                "it's in review. Fix the editing bug and the Bob conversation are the two most urgent unblocks."
            )
        },
        {
            "title": "Customer Outreach Calls",
            "time": "9:41–9:43 AM EDT",
            "decisions": [
                "Reached out to Kara Patterson about low applicant volume for her DocMaster role posting",
            ],
            "action_items": [
                "Wait for callback from Kara Patterson at 310-936-5253 (re: DocMaster posting on Homebase)",
                "Follow up with Kara if no response within reasonable timeframe",
            ],
            "rationale": (
                "Direct customer outreach = signal on product-market fit and urgency. "
                "Kara's DocMaster role is a concrete use case to track to conversion."
            )
        }
    ]


if __name__ == "__main__":
    main()
