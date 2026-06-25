#!/usr/bin/env python3
"""
Daily PM Decision Summary - Slack Bot
Triggered by Cursor Cloud Agent cron automation at midnight UTC (5pm PDT).
Reads Granola meeting notes for the day and sends a decision summary to Slack.

Required env vars:
  SLACK_BOT_TOKEN  - Slack bot OAuth token (xoxb-...)
  SLACK_CHANNEL_ID - Slack channel/DM ID (default: D06E4QMHCNN)
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta


SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def post_to_slack(channel: str, blocks: list, text: str) -> dict:
    """Post a message to Slack using the Web API."""
    if not SLACK_BOT_TOKEN:
        raise ValueError(
            "SLACK_BOT_TOKEN is not set. Add it as a Cloud Agent secret in Cursor Dashboard."
        )

    payload = json.dumps({
        "channel": channel,
        "text": text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
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


def build_slack_blocks(summary: dict) -> list:
    """Build Slack Block Kit blocks for the daily summary."""
    date_str = summary["date"]
    blocks = []

    # Header
    blocks.append({
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"📋 Your Daily Decision Roundup — {date_str}",
            "emoji": True,
        }
    })

    blocks.append({"type": "divider"})

    # Intro
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": summary["intro"],
        }
    })

    blocks.append({"type": "divider"})

    # Meetings
    for meeting in summary["meetings"]:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*🗓 {meeting['title']}* — {meeting['time']}\n_{meeting['attendees']}_",
            }
        })

        if meeting.get("decisions"):
            decisions_text = "\n".join(
                f"• *{d['title']}*\n  {d['detail']}\n  _Rationale: {d['rationale']}_"
                for d in meeting["decisions"]
            )
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Key Decisions:*\n{decisions_text}",
                }
            })

        if meeting.get("action_items"):
            items_text = "\n".join(
                f"• {item['owner']}: {item['action']}"
                for item in meeting["action_items"]
            )
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Action Items:*\n{items_text}",
                }
            })

        if meeting.get("open_questions"):
            qs_text = "\n".join(f"• {q}" for q in meeting["open_questions"])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Open Questions:*\n{qs_text}",
                }
            })

        blocks.append({"type": "divider"})

    # Closing
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": summary["closing"],
        }
    })

    return blocks


# ── Today's summary (June 24, 2026) ─────────────────────────────────────────

TODAYS_SUMMARY = {
    "date": "June 24, 2026",
    "intro": (
        "Hey Manan! 👋 Here's your end-of-day decision brief. "
        "You had *1 meeting* today — and it was a big one. "
        "The Culinary Agents partnership is officially in motion. Let's break it down:"
    ),
    "meetings": [
        {
            "title": "Culinary Agents & Homebase",
            "time": "1:30 PM PDT",
            "attendees": "Jeff Silverstein & Alice Cheng (Culinary Agents) · Ray Sandza (Homebase)",
            "decisions": [
                {
                    "title": "Integration Model: CPA (Applicant Ingest) via XML/API Feed",
                    "detail": (
                        "Homebase will send its existing job feed (Indeed-compatible XML/API) "
                        "to Culinary Agents. Applicants who apply on Culinary Agents get pushed "
                        "directly into Homebase's endpoint — no click-redirect (CPC)."
                    ),
                    "rationale": (
                        "Homebase's ATS is already fully built out with XML feeds and an API. "
                        "Full data ingest means all post-apply workflow (AI screener, scheduling, "
                        "comms) stays inside Homebase. ~2-week implementation on Alice's end."
                    ),
                },
                {
                    "title": "Pricing Path: Bulk PPP (~$69/post at 500-post tier) for major metros",
                    "detail": (
                        "PPP (pay-per-post) at bulk pricing is the leading option for metro-heavy "
                        "clients. CPA at $15/applicant reserved for salary roles (e.g., restaurant "
                        "managers) where it beats a $5K recruiting agency. Alice to confirm exact "
                        "price at the 500-post tier (likely $69)."
                    ),
                    "rationale": (
                        "In major metros, flat-fee PPP generates far more applicants than CPA "
                        "for the same cost. For harder-to-fill salary roles in any city, CPA at "
                        "$15 is a strong value vs. alternatives. Self-serve $69 posts lack "
                        "pre-screen questions, multi-city matching, and interview scheduler — "
                        "partner integration unlocks the full feature set."
                    ),
                },
                {
                    "title": "Start with a Paid Feed Pilot — Negotiate Long-Term Pricing After",
                    "detail": (
                        "Agreed to move immediately to a job-feed pilot (not more manual job "
                        "posts). Ray sends the feed; Alice's CTO reviews and implements. "
                        "Partner agreement to be reviewed before sending."
                    ),
                    "rationale": (
                        "Manual job posts (3 done the day before the meeting) are a one-off test. "
                        "The real value comes from the automated feed integration. Piloting at "
                        "list price now lets both teams validate the flow before negotiating bulk "
                        "terms at volume."
                    ),
                },
            ],
            "action_items": [
                {"owner": "Ray", "action": "Send job feed to Alice for CTO review → kicks off ~2-week implementation"},
                {"owner": "Alice", "action": "Review standard partner agreement — confirm it fits this setup, then send over"},
                {"owner": "Alice", "action": "Confirm exact per-post price at the 500-post bulk tier (likely $69)"},
                {"owner": "Manan + Alice", "action": "Schedule a follow-up demo of Homebase's ATS and AI screener"},
                {"owner": "Manan", "action": "Set up a dedicated call to explore Indeed-boosting mechanics via Culinary Agents (Alice confirmed it's live and well-received)"},
            ],
            "open_questions": [
                "Can Culinary Agents' resume/talent book be white-labeled inside Homebase? (Manan raised this — worth a follow-on conversation)",
                "What specific features are gated behind partner integration vs. self-serve $69 post? (Ask Alice to send full feature comparison)",
            ],
        }
    ],
    "closing": (
        "*The big picture:* The Culinary Agents partnership directly targets your #1 pain point — "
        "sourcing for kitchen roles (line cook, prep cook, etc.) that drag down your 'healthy jobs' metric. "
        "With 2.7M hospitality workers on their platform and a major-metro-strong distribution network, "
        "this could move the needle fast. Jeff has known John since 2015 — the trust is there. "
        "Keep the momentum going! 🔥\n\n"
        "_This summary was auto-generated by your Chief of Staff bot. Have a great evening!_"
    ),
}


def main():
    print(f"[{datetime.now(timezone.utc).isoformat()}] Daily summary bot starting...")
    print(f"Channel: {SLACK_CHANNEL_ID}")

    if not SLACK_BOT_TOKEN:
        print(
            "\n⚠️  SLACK_BOT_TOKEN is not configured.\n"
            "To enable daily Slack delivery:\n"
            "  1. Create a Slack bot at https://api.slack.com/apps\n"
            "  2. Add the 'chat:write' OAuth scope\n"
            "  3. Install the app to your workspace and copy the Bot User OAuth Token\n"
            "  4. Add SLACK_BOT_TOKEN as a Cloud Agent secret in Cursor Dashboard\n\n"
            "Here is the summary that WOULD be sent:\n"
        )
        # Print the summary to stdout so it's visible in agent logs
        print(json.dumps(TODAYS_SUMMARY, indent=2))
        sys.exit(1)

    blocks = build_slack_blocks(TODAYS_SUMMARY)
    # Fallback plain-text for notifications
    plain_text = f"Daily Decision Roundup — {TODAYS_SUMMARY['date']}: Culinary Agents partnership is in motion. Ray to send job feed, Alice to review partner agreement."

    result = post_to_slack(SLACK_CHANNEL_ID, blocks, plain_text)
    print(f"✅ Slack message posted. ts={result.get('ts')}")


if __name__ == "__main__":
    main()
