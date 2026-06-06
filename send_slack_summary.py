#!/usr/bin/env python3
"""
Send a pre-built Slack message to a channel/DM.
Usage: python3 send_slack_summary.py
Requires: SLACK_BOT_TOKEN environment variable
"""

import os
import json
import sys
import requests

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")


def send_message(token: str, channel: str, blocks: list, text: str) -> dict:
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"channel": channel, "text": text, "blocks": blocks},
        timeout=15,
    )
    return response.json()


def main():
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN not set. Add it to your Cursor Cloud Agent secrets.")
        sys.exit(1)

    # Today's summary blocks — built by the agent from Granola MCP data
    text = "🌅 Your Daily Decision Summary — Friday, June 5, 2026"

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "🌅 Your Daily Decision Summary — Friday, June 5, 2026", "emoji": True}
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! 👋 Big day — you had 4 meaningful conversations and made some important calls. "
                    "Here's everything distilled so you can close out clean and hit Monday with full momentum. 💪\n\n"
                    "_(7 recorded sessions · 3 substantive meetings · 4 phone calls)_"
                )
            }
        },
        {"type": "divider"},
        # ---- Meeting 1: Hiring Leads Standup ----
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📋 Hiring Leads Standup* — _11:30 AM EDT_\n_With: Fadi, Dana, Matan, Jatin, Ray, Nelson, Jeff, Martin, Usman_"}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*✅ Decisions Made:*\n"
                    "• Q3 plans due *Monday morning* — you're submitting Monday AM (not over the weekend ✊)\n"
                    "• *Redshift deprecated this month* → single data warehouse: Databricks\n"
                    "• *Looker → Omni* migration starting (1–2 months); minimize new Looker additions *now*\n"
                    "• Lean into *product-led growth* experimentation across all initiatives\n"
                    "• Move forward with *'Homebase Recruit' name testing* (Facebook test + Katie's early positive signal)"
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*☑️ Action Items:*\n"
                    "☑️ Submit Q3 plan Monday AM — must center on *ICP*, *Q3-specific timelines*, and *concrete impact numbers*\n"
                    "☑️ Flag any data pipeline mismatches to *Nelson* during transition\n"
                    "☑️ Coordinate with *Dana* on intake experiment learnings → feed into PLG strategy\n"
                    "☑️ Set up Facebook name testing for *'Homebase Recruit'* branding\n"
                    "☑️ Get *Ivana* to provide CS candidate conversation examples for intake experiment expansion"
                )
            }
        },
        {
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": (
                    "💡 *Why it matters:* Q3 plan is the #1 near-term deliverable — expect multiple revisions. "
                    "The Databricks/Omni migration affects how all teams measure success, so early pipeline "
                    "flagging prevents metric drift. The Boost first organic sale is a *real green shoot* — "
                    "the product is working, now accelerate."
                )
            }]
        },
        {"type": "divider"},
        # ---- Meeting 2: Michael / Manan ----
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📋 Michael / Manan — Boost Modal & Job Flagging*  — _12:00 PM EDT_\n_With: Michael Heistand_"}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*✅ Decisions Made:*\n"
                    "• Boost modal experiment will target *syndicated companies with no/low-risk jobs* post job creation\n"
                    "• Three pillars confirmed: talent pool, easier OAM spend, funnel optimization\n"
                    "• *OAMs can't edit jobs in review status* = major product bug — must fix (current workaround: 'copy job' is broken UX)\n"
                    "• Contact info flags may need reclassification: *low → medium risk* (50% of all flags are this issue)"
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*☑️ Action Items:*\n"
                    "☑️ *Talk to Bob* — define handling for flagged jobs that were already boosted (refund/re-boost flow)\n"
                    "☑️ *Schedule 4-person flow review* next week to align on boost + flagging end-to-end workflow\n"
                    "☑️ *Investigate V2 job editing* — can OAMs edit flagged jobs in V2? This is the core UX unblock\n"
                    "☑️ *Build admin dashboard* for easy refund tracking on flagged+boosted jobs\n"
                    "☑️ *Explore real-time job validation* — catch contact info issues before submission, not after"
                )
            }
        },
        {
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": (
                    "💡 *Why it matters:* Boost is a direct revenue lever — 588 of 1,183 jobs flagged in May (49.7%). "
                    "80% are *legitimate companies with formatting issues*. Right now they get charged AND can't edit. "
                    "The Bob conversation + V2 editing fix are the two fastest paths to unblocking real revenue."
                )
            }]
        },
        {"type": "divider"},
        # ---- Phone calls ----
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📞 Customer Outreach Calls* — _9:41–9:43 AM EDT_"}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*✅ Actions Taken:*\n"
                    "• Called *Kara Patterson* about low applicant volume on her DocMaster job posting\n"
                    "• Positioned Homebase as the solution to increase candidate flow\n\n"
                    "*☑️ Follow-up:*\n"
                    "☑️ Wait for callback from Kara at *310-936-5253* — follow up if no response by end of next week"
                )
            }
        },
        {
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": "💡 Direct outreach = fast signal on activation. Track Kara to conversion for product-market fit data."
            }]
        },
        {"type": "divider"},
        # ---- Monday Preview ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🗓️ Monday Morning Priorities:*\n"
                    "1️⃣ *Submit Q3 plan* (ICP-centered, Q3-specific, concrete numbers — expect revisions)\n"
                    "2️⃣ *Talk to Bob* about flagged+boosted job handling\n"
                    "3️⃣ *Kara Patterson follow-up* if no callback over weekend\n"
                    "4️⃣ *EC Ops training starts* — Adams replacements (3 new people) onboarding"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": "🤖 Sent by your AI Chief of Staff · Powered by Granola + Cursor Automation · _Have a great weekend!_ 🌟"
            }]
        }
    ]

    print(f"Sending summary to {SLACK_CHANNEL_ID}...")
    result = send_message(SLACK_BOT_TOKEN, SLACK_CHANNEL_ID, blocks, text)

    if result.get("ok"):
        print(f"✅ Daily summary sent successfully!")
        print(f"   Channel: {result.get('channel')}")
        print(f"   Timestamp: {result.get('ts')}")
    else:
        print(f"❌ Failed to send: {result.get('error', 'unknown error')}")
        if result.get("needed"):
            print(f"   Needed scopes: {result.get('needed')}")
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
