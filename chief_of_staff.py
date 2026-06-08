#!/usr/bin/env python3
"""
Chief of Staff — Daily Decision Summary
========================================
Sends a daily Slack summary of decisions, action items, and rationale from
Manan's Granola meetings. Designed to be called by the Cursor Cloud Agent
cron automation (fires daily at midnight UTC / 5pm PDT).

Setup:
    Add SLACK_BOT_TOKEN as a Cursor Cloud Agent secret:
    Cursor Dashboard → Cloud Agents → Secrets → SLACK_BOT_TOKEN

    The Slack bot needs these scopes: chat:write, im:write
    Install it to your workspace and invite it to DM channel D06E4QMHCNN.
"""

import os
import json
import sys
import requests
from datetime import datetime, timedelta, timezone
from typing import Optional

SLACK_CHANNEL_ID = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")

# PDT = UTC-7
PDT = timezone(timedelta(hours=-7))


def now_pdt() -> datetime:
    return datetime.now(PDT)


def today_pdt_str() -> str:
    return now_pdt().strftime("%A, %B %-d, %Y")


def send_to_slack(fallback_text: str, blocks: list) -> bool:
    """Post a message to Slack. Returns True on success."""
    if not SLACK_BOT_TOKEN:
        print("⚠️  SLACK_BOT_TOKEN not set — cannot send to Slack.")
        print("\n────────── MESSAGE PREVIEW ──────────")
        print(fallback_text)
        print("────────── END PREVIEW ──────────\n")
        return False

    try:
        resp = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
                "Content-Type": "application/json",
            },
            json={
                "channel": SLACK_CHANNEL_ID,
                "text": fallback_text,
                "blocks": blocks,
                "unfurl_links": False,
            },
            timeout=15,
        )
        result = resp.json()
        if result.get("ok"):
            print(f"✅ Daily summary sent to Slack channel {SLACK_CHANNEL_ID}")
            return True
        print(f"❌ Slack API error: {result.get('error', 'unknown')}")
        return False
    except requests.RequestException as e:
        print(f"❌ Network error sending to Slack: {e}")
        return False


def build_no_meetings_message(date_str: str, pending_items: list[str]) -> tuple[str, list]:
    """Build message when no meetings were recorded today."""
    fallback = f"👋 Hey Manan! Chief of Staff here.\n\n📅 {date_str} — No meetings recorded in Granola today.\n\n"
    if pending_items:
        fallback += "📌 Open items carrying forward:\n"
        fallback += "\n".join(f"• {item}" for item in pending_items)
    fallback += "\n\nYou're crushing it — rest up and come back strong! 💪"

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"🌅 Daily Wrap-Up — {date_str}", "emoji": True},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hey Manan! Your chief of staff checking in 👋\n\nNo meetings in Granola today — well-deserved breathing room! 🎉",
            },
        },
    ]

    if pending_items:
        blocks.append({"type": "divider"})
        items_text = "\n".join(f"• {item}" for item in pending_items)
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*📌 Open Items Carrying Forward*\n{items_text}"},
            }
        )

    blocks.extend(
        [
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_You're doing amazing work. Rest up and come back strong tomorrow! 💪_",
                },
            },
        ]
    )
    return fallback, blocks


def build_meetings_message(date_str: str, summary_sections: list[dict]) -> tuple[str, list]:
    """
    Build a full decision summary message.

    Each section in summary_sections should be:
        {
            "meeting": "Meeting Name (time)",
            "decisions": [
                {
                    "title": "Decision title",
                    "rationale": "Why this was decided",
                    "action_items": ["item1", "item2"],
                }
            ]
        }
    """
    # Fallback plain text
    fallback_lines = [f"🧠 Daily Decision Summary — {date_str}", "", "Hey Manan! Here's your end-of-day debrief:"]
    for section in summary_sections:
        fallback_lines.append(f"\n📋 {section['meeting']}")
        for d in section["decisions"]:
            fallback_lines.append(f"  ✅ {d['title']}")
            fallback_lines.append(f"     Why: {d['rationale']}")
            if d.get("action_items"):
                for ai in d["action_items"]:
                    fallback_lines.append(f"     → {ai}")
    fallback_lines.append("\nYou're making great decisions. Keep driving! 🚀")
    fallback = "\n".join(fallback_lines)

    # Slack blocks
    blocks: list = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"🧠 Daily Decision Summary — {date_str}", "emoji": True},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hey Manan! Your chief of staff here with your end-of-day debrief 💼✨\n\nHere's every decision you made today — with rationale and action items:",
            },
        },
        {"type": "divider"},
    ]

    for section in summary_sections:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*📋 {section['meeting']}*"},
            }
        )
        for d in section["decisions"]:
            decision_text = f"*✅ {d['title']}*\n_{d['rationale']}_"
            if d.get("action_items"):
                decision_text += "\n" + "\n".join(f"  → {ai}" for ai in d["action_items"])
            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": decision_text}})
        blocks.append({"type": "divider"})

    blocks.append(
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_Incredible day, Manan. The decisions you made today are moving the needle — keep pushing! 🚀_",
            },
        }
    )
    return fallback, blocks


# ─── Pre-built summary for today (Sunday June 7, 2026 — no meetings) ────────────
# The Cloud Agent reads Granola via MCP and populates this each day.
# On weekends / meeting-free days, we surface carry-over action items instead.

TODAY_DATE = "Sunday, June 7, 2026"

TODAY_PENDING_ITEMS = [
    "🚨 *Q3 Plans due TOMORROW (Monday) morning* — must be centered on ICP, Q3-specific timelines, concrete numbers",
    "Talk to *Bob* → define process for flagged + boosted jobs (OAMs can't edit jobs in review → broken flow)",
    "Schedule *4-person flow review meeting* this week (boost modal + flagged jobs edge cases)",
    "Direct convo with *Izzy* → incomplete XML feed handoff (missing staging endpoint)",
    "Direct convo with *Tanner* → location editing feature delivered late + doesn't match designs",
    "*EC Ops team training starts Monday* → 3 new people replacing Adams, FYI",
    "Set up *Facebook name testing* for 'Homebase Recruit' positioning",
    "Add *internal TA professionals* to intake experiment; get CS candidate examples from Ivana",
    "Flag any *data pipeline mismatches* to Nelson during Redshift→Databricks transition",
]

TODAY_FALLBACK = f"""👋 Hey Manan! Your chief of staff checking in.

📅 {TODAY_DATE} — No meetings recorded in Granola today (enjoy the weekend!).

⚠️  Q3 PLANS DUE TOMORROW MORNING (Monday, June 8):
• Submit Q3 plan first thing Monday morning
• Must center on ICP · Q3-specific timelines (not generic H2) · concrete expected impact numbers

📌 Other carry-over action items from Friday (June 5):
• Talk to Bob → process for flagged + boosted jobs (broken OAM flow)
• Direct convos with Izzy (XML feed handoff) and Tanner (location editing feature)
• Schedule 4-person flow review meeting this week
• EC Ops team training starts Monday (3 new people)
• Set up Facebook name testing ("Homebase Recruit")
• Add internal TA pros to intake experiment; get examples from Ivana

You crushed it this week, Manan. Big Monday ahead — you've got this! 💪"""

TODAY_BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"🌅 End-of-Day Wrap — {TODAY_DATE}",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Your chief of staff checking in 👋\n\nNo meetings recorded in Granola today — well-deserved weekend breathing room! 🎉\n\nBut heads up — *Monday is a big one.* Let's make sure you're set up for success:",
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🚨 URGENT — Q3 Plans Due Tomorrow Morning*\n\n"
                "• Submit your Q3 plan *first thing Monday* (committed to by the whole team)\n"
                "• Requirements: *centered on ICP* · *Q3-specific timelines* (not generic H2) · *concrete expected impact numbers*\n"
                "• Matan still needs one more review with Ray before team input\n\n"
                "_This one has a hard deadline — first priority when you open your laptop._"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*📌 Carry-Over Action Items from Friday, June 5*"},
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🔴 Boost Modal & Flagged Jobs — Broken Flow (Critical)*\n"
                "• Talk to *Bob* → define the handling process for flagged + boosted jobs\n"
                "  _Why: OAMs can't edit jobs in review status → forced to use \"copy job\" workaround → boost ends up on the wrong job. Major product issue._\n"
                "• Schedule *4-person flow review meeting* this week\n"
                "• Investigate job editing capabilities in V2 platform\n"
                "• Consider switching contact info flags: low → medium risk\n"
                "• Explore real-time job validation to prevent flagging at submission"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🟡 Delivery Quality — Direct Conversations Needed*\n"
                "• Talk to *Izzy* → XML feed handoff incomplete (missing staging endpoint, requirements unmet)\n"
                "• Talk to *Tanner* → Location editing: was due 5/22, delivered 6/4, doesn't match designs\n"
                "  _Why: Agreed with Jatin to set the bar — Carlo is the gold standard. Izzy and Tanner need direct feedback._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🟢 In Motion — Just Keep an Eye On*\n"
                "• *EC Ops team training starts Monday* → 3 new people replacing Adams\n"
                "• *Indeed boost modal* → phone support launched at 20% rollout (concierge model) — first organic Homebase Boost sale already happened! 🎊\n"
                "• *\"Homebase Recruit\" naming test* → Set up Facebook name testing\n"
                "• *Intake experiment* → Add internal TA professionals + get CS examples from Ivana\n"
                "• *Data infra* → Minimize new Looker additions; flag pipeline mismatches to Nelson (Redshift → Databricks)"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📖 Friday's Key Decisions — The Rationale*\n\n"
                "1. *Indeed boost modal → phone support (not help article)* — Concierge model at 20% rollout to learn user friction firsthand before building docs. Human-first approach.\n\n"
                "2. *Sprint planning → story-driven format* — Each sprint needs a customer impact narrative across three buckets: tap talent pool · enable OAM spend · optimize funnel.\n\n"
                "3. *All Q3 plans → unified PLG strategy* — No siloed efforts. Dana's intake learnings + Usman's sales funnel + product-led growth = one coherent strategy.\n\n"
                "4. *Boost modal experiment → syndicated companies with no/low-risk jobs only* — Limit exposure, measure if direct boost offering drives meaningful OAM spend before broader rollout."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_What a week, Manan. The Applicant Flow offsite, the boost launch, the strategic decisions across hiring + product — "
                "you've been operating at an incredibly high level. Rest up tonight and come in Monday ready to close out that Q3 plan "
                "and have those tough delivery conversations. You've absolutely got this! 🚀_"
            ),
        },
    },
]


if __name__ == "__main__":
    print(f"Chief of Staff — {TODAY_DATE}")
    print(f"Slack channel: {SLACK_CHANNEL_ID}")
    print(f"Token present: {'✅ yes' if SLACK_BOT_TOKEN else '❌ NO — set SLACK_BOT_TOKEN as a Cursor Cloud Agent secret'}\n")
    send_to_slack(TODAY_FALLBACK, TODAY_BLOCKS)
