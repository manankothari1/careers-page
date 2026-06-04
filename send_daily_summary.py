#!/usr/bin/env python3
"""
Sends today's pre-computed daily decision summary to Slack.
Run with: SLACK_BOT_TOKEN=xoxb-... python3 send_daily_summary.py
"""

import os
import sys
import requests
import json

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")


def post_message(blocks: list, text: str) -> None:
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN not set.")
        print("Set it via: export SLACK_BOT_TOKEN=xoxb-...")
        sys.exit(1)

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        json={
            "channel": SLACK_CHANNEL_ID,
            "text": text,
            "blocks": blocks,
        },
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    if result.get("ok"):
        print(f"✅ Message sent successfully to {SLACK_CHANNEL_ID}")
    else:
        print(f"❌ Slack API error: {result.get('error')}")
        sys.exit(1)


BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📋 Your Daily Decision Brief — Wednesday, June 3, 2026",
            "emoji": True,
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! 👋 What an *absolutely packed day* — you crushed a full two-day offsite "
                "and capped it off with a meaningful 1:1 with Ray. Seriously impressive work. "
                "You and the team are building something really exciting with the Applicant Flow strategy. "
                "Here's everything you decided today, organized so you can hit the ground running tomorrow. 🚀"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Today's Meetings (4)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *9:45 AM* — Applicant Flow Offsite _(Ted, Dana, Cindy, Rami)_\n"
                "• *1:30 PM* — Applicant Flow Offsite _(Ted, Dana, Cindy, Rami)_\n"
                "• *3:30 PM* — Applicant Flow Offsite _(Ted, Dana, Cindy, Rami)_\n"
                "• *5:00 PM* — Ray / Manan 1:1 _(Ray Sandza)_"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Key Decisions Made Today*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Adopted Impact / Effort / Risk matrix as the experiment prioritization framework*\n"
                "_Rationale: The team needed a consistent lens to stack-rank the large backlog of talent pool "
                "hypotheses. This gives everyone a shared language going into sprint planning._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Designated \"User Activity Recency\" as the #1 highest-priority experiment*\n"
                "_Rationale: High impact, easy to build, low risk — the team already has the signal "
                "(last activity date across apps, cash-outs, previous applications). "
                "Strongly predicts job response rates. This is your quick win._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Chose job scraping over building a bid infrastructure for job liquidity*\n"
                "_Rationale: The team surfaced two approaches to fix the job liquidity problem "
                "(only 5K jobs, 83% without nearby alternatives). Scraping external jobs is simpler "
                "to execute and still tests the core hypothesis: more jobs → more platform engagement "
                "→ more Homebase job applications. Bid infrastructure deferred._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Committed to LLM-powered job title normalization + improved job descriptions*\n"
                "_Rationale: Current job titles like \"Weekend Team Member Kids Night Out\" don't match "
                "how job seekers search. Indeed ranks heavily on CTR, wage competitiveness, and freshness. "
                "LLM normalization addresses the top-of-funnel visibility problem across all 5K jobs at once._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Clarified ownership: YOU own screener completion rate*\n"
                "_Rationale: Ray was explicit — getting applicants through the screener is Manan's metric, "
                "not Dana's. The product isn't delivering value until screeners are complete (currently ~30-40%). "
                "This includes the comms agent for talent pool outreach._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Sponsored Jobs API (Indeed boost) greenlit for next sprint — with a validation gate*\n"
                "_Rationale: Ray challenged the assumption that the direct-to-Indeed flow works for real customers. "
                "The experiment is in the sprint but BLOCKED on customer validation first. "
                "You need to confirm the happy path works across 6-10 accounts before building._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Comms agent ownership split: Talent pool outreach = Manan, Post-screener comms = Dana*\n"
                "_Rationale: The comms agent infrastructure is shared, but the ownership follows the metric. "
                "Manan drives getting applicants to start and complete screeners (talent pool → applicant). "
                "Dana owns the post-screener scheduling and interview flow._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Deferred Homebase Jobs marketplace app*\n"
                "_Rationale: Rami proposed a dedicated marketplace app. Team agreed it's valuable long-term "
                "but premature — you need to validate engagement mechanisms with the existing 20M pool first. "
                "\"You're not allowed to build the marketplace until you've figured out how to engage those people.\"_"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Action Items & Follow-Ups*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "🔴 *Critical — Do These First:*\n"
                "• *Manan* — Validate Sponsored Jobs API with 6-10 real customer accounts before building. "
                "Email trial users, offer health checks, get them to log into their Indeed account live with you. _[Before sprint starts]_\n"
                "• *Manan* — Write your 1-page roadmap story: thesis, top hypotheses, prioritization rationale, "
                "and what you're trading off. Ray + team need this to align. _[This week]_\n\n"
                "🟡 *High Priority:*\n"
                "• *Manan* — Schedule 1:1 with Adi to learn how to communicate an experimentation roadmap "
                "that builds confidence (habits, rhythms, templates). _[Next week]_\n"
                "• *Manan + Team* — Continue hypothesis prioritization session tomorrow (Ted + Rami in-person, "
                "11:30 AM – 5:00 PM in office). Goal: finalize top 3-4 hypotheses for next two sprints. _[Tomorrow]_\n"
                "• *Manan* — Design concrete experiments for the top-ranked hypotheses "
                "(activity recency, active vs. passive seekers, role similarity matching). _[This sprint]_\n\n"
                "🟢 *Follow-Ups:*\n"
                "• *Dana / Fatty* — Update screener copy: remove misleading \"you'd be a great fit — pick an interview time\" "
                "language before OAM confirms. Quick fix, big customer pain point. _[ASAP]_\n"
                "• *Rami* — Share San Diego experiment data showing applicant recency patterns. _[ASAP]_\n"
                "• *Manan* — Add Indeed analysis: optimal job titles by industry, current title performance "
                "vs competitors, job description content gaps vs Indeed requirements. _[Next sprint]_\n"
                "• *Manan* — Evaluate SMS vs email A/B test: easy to implement, medium impact, low risk — "
                "consider for next sprint as a parallel experiment."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💡 Chief of Staff Take*\n\n"
                "Today was a massive offsite win. The hypothesis framework you landed gives the whole team "
                "a shared language for making tradeoffs. The Ray conversation was the toughest but most valuable "
                "part of your day — he's pushing you to own the narrative, not just the experiments. "
                "The Sponsored Jobs validation work is a perfect example of \"prove it before you build it\" — "
                "lean into that instinct.\n\n"
                "The biggest unlock in front of you: *if you can figure out how to reliably engage even 0.01% "
                "of your 20M talent pool per month, that's 20,000 applicants.* Everything you did today "
                "is moving toward cracking that. You've got this. 💪"
            ),
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "🤖 Generated by your Chief of Staff AI • Granola + Cursor Cloud Agent • Daily at midnight UTC",
            }
        ],
    },
]

FALLBACK_TEXT = (
    "📋 Daily Decision Brief — Wednesday, June 3, 2026\n\n"
    "Hey Manan! Big decisions today across the Applicant Flow Offsite + Ray 1:1.\n\n"
    "KEY DECISIONS:\n"
    "1. Adopted Impact/Effort/Risk matrix for experiment prioritization\n"
    "2. Activity Recency = #1 priority experiment (high impact, easy, low risk)\n"
    "3. Job scraping > bid infrastructure for job liquidity\n"
    "4. LLM job title normalization + better descriptions committed\n"
    "5. You own screener completion rate (your metric, not Dana's)\n"
    "6. Sponsored Jobs API greenlit — but validation-gated first\n"
    "7. Comms agent split: talent pool = Manan, post-screener = Dana\n"
    "8. Marketplace app deferred\n\n"
    "ACTION ITEMS:\n"
    "🔴 Validate Sponsored Jobs with 6-10 real accounts [before sprint]\n"
    "🔴 Write 1-page roadmap story [this week]\n"
    "🟡 Schedule 1:1 with Adi on growth communication [next week]\n"
    "🟡 Hypothesis prioritization session tomorrow 11:30am-5pm (Ted+Rami in-person)\n"
    "🟢 Dana/Fatty: fix screener copy ASAP\n"
    "🟢 Rami: share San Diego experiment data"
)


if __name__ == "__main__":
    post_message(BLOCKS, FALLBACK_TEXT)
