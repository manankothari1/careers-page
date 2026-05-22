#!/usr/bin/env python3
"""
Send a pre-composed daily summary to Slack.
Usage: python send_daily_summary.py
Requires: SLACK_BOT_TOKEN env var
"""

import os
import sys
import requests

SLACK_CHANNEL_ID = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")


def send_slack_blocks(token: str, channel: str, blocks: list, fallback_text: str):
    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "channel": channel,
            "text": fallback_text,
            "blocks": blocks,
            "unfurl_links": False,
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("ok"):
        raise RuntimeError(f"Slack API error: {data.get('error')} — {data}")
    return data


def main():
    if not SLACK_BOT_TOKEN:
        print(
            "\n⚠️  SLACK_BOT_TOKEN is not set.\n"
            "To enable Slack notifications, add your bot token as a Cursor Cloud Agent secret:\n"
            "  1. Go to cursor.com → Cloud Agents → Secrets\n"
            "  2. Add secret: SLACK_BOT_TOKEN = xoxb-your-bot-token\n"
            "  3. The bot needs scopes: chat:write, im:write\n\n"
            "--- TODAY'S SUMMARY (would have been sent) ---\n"
        )
        # Print the message content so the user can see it
        for block in BLOCKS:
            if block.get("type") == "section":
                text = block.get("text", {}).get("text", "")
                if text:
                    print(text)
            elif block.get("type") == "header":
                print("\n" + block.get("text", {}).get("text", "") + "\n")
            elif block.get("type") == "divider":
                print("-" * 60)
            elif block.get("type") == "context":
                for el in block.get("elements", []):
                    print(el.get("text", ""))
        return

    print(f"📤 Sending daily summary to Slack channel {SLACK_CHANNEL_ID}...")
    result = send_slack_blocks(
        SLACK_BOT_TOKEN,
        SLACK_CHANNEL_ID,
        BLOCKS,
        FALLBACK_TEXT,
    )
    print(f"✅ Message delivered! (ts={result.get('ts')})")


# ---------------------------------------------------------------------------
# MESSAGE CONTENT — regenerated daily by the Cloud Agent
# ---------------------------------------------------------------------------

FALLBACK_TEXT = "🌟 Your Daily Debrief — May 21, 2026 | Manan, here's your day in decisions!"

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌟 Daily Debrief — Thursday, May 21, 2026",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! 👋 You had a *seriously productive* day. Here's everything you decided, committed to, and need to follow up on. Let's make sure nothing falls through the cracks! 🚀",
        },
    },
    {"type": "divider"},
    # --- Meeting ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Rami / Manan — Working Session*\n_8:15 AM PDT · Rami Abou-Seido_",
        },
    },
    # --- Decisions ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🎯 KEY DECISIONS MADE*\n\n"
                "1️⃣  *North Star Metric: % of Jobs with Healthy Applicant Flow*\n"
                "   • Defined \"healthy\" = 20+ applicants *and* 5+ top matches\n"
                "   • Rationale: Gives a single, unambiguous signal that both volume *and* quality are met — avoids optimizing one at the expense of the other\n\n"
                "2️⃣  *June 1st as A/B Test Launch Target*\n"
                "   • First talent pool expansion experiment must be running by June 1st\n"
                "   • Rationale: Creates urgency to ship early learnings before Q2 ends; June 1st gives enough buffer to course-correct before end of quarter\n\n"
                "3️⃣  *Binary Role Matching (Fit/No Fit) as Starting Point*\n"
                "   • Decided to start with binary matching before moving to a sliding scale\n"
                "   • Rationale: Simpler to ship, easier to A/B test cleanly, and avoids premature complexity before the baseline is validated\n\n"
                "4️⃣  *Expand Matching Pool to Full 10M Employee/Applicant Database*\n"
                "   • Current system uses a small sample — decision to go full scale\n"
                "   • Rationale: Sample set is too limited to generate statistically meaningful A/B results; need the full pool to see real signal\n\n"
                "5️⃣  *Smart Job Title & Wage Suggestions in Job Creation Flow*\n"
                "   • Scope locked for Sprint 2612 (starts June 8th)\n"
                "   • Titles: Normalize away multi-title listings (e.g. \"Sandwich Artist/FOH Staff\") using existing role normalization data\n"
                "   • Wages: Frame as *informational* (market rate context), NOT prescriptive — avoids compliance/price-coordination concerns\n"
                "   • Rationale: Cleaner job titles improve Indeed ranking; wage context reduces friction for SMB employers who don't know market rates"
            ),
        },
    },
    {"type": "divider"},
    # --- Action Items ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*⚡ ACTION ITEMS & FOLLOW-UPS*\n\n"
                "🔵 *Rami (by EOD tomorrow, May 22nd)*\n"
                "   → Investigate current role matching formula and surface technical requirements\n"
                "   → Determine feasibility of June 1st A/B test launch — timeline check-in tomorrow\n\n"
                "🟢 *You — Manan*\n"
                "   → Align with Personas team on user type definitions (Previous Applicant vs. Previous Employee)\n"
                "   → Access Indeed job listing dataset through Databricks\n"
                "   → Design A/B test structure for talent pool expansion with Rami\n"
                "   → Confirm Sprint 2612 scope for smart job suggestions with eng\n\n"
                "🟡 *Sprint Planning*\n"
                "   → Sprint 2611 (next week): Sponsored Jobs API delivery\n"
                "   → Sprint 2612 (June 8th): Talent pool experiments + job creation smart suggestions launch\n"
                "   → Scope LLM work for job descriptions separately (may need additional time estimate)"
            ),
        },
    },
    {"type": "divider"},
    # --- Secondary metrics ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📊 SECONDARY QUALITY METRICS TO TRACK*\n"
                "_(Agreed on in today's session — make sure dashboards reflect these)_\n\n"
                "• % of applicants that are top matches\n"
                "• % of top matches that get an interview\n"
                "• % of top matches that get hired"
            ),
        },
    },
    {"type": "divider"},
    # --- Open questions ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*❓ OPEN QUESTIONS TO RESOLVE*\n\n"
                "• Radius thresholds for matching: 10 vs 15 vs 20 miles (currently 25) — test in A/B\n"
                "• Time window for job history: past 2 years vs 3 years vs current approach\n"
                "• Commute time vs geographic distance as matching criterion\n"
                "• Email sender persona for outreach campaigns (recruiter, business owner, OEM custom) — analyze San Diego experiment results (350 targeted / 250 opened)\n"
                "• Referral incentive mechanic for network effects — worth scoping?"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "💡 1 meeting · Sourced from Granola · Generated by your Chief of Staff bot at 5:00 PM PDT",
            }
        ],
    },
]


if __name__ == "__main__":
    main()
