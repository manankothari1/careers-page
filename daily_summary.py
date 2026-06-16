#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Automation
===================================================
Runs at midnight UTC (5:00 PM PDT) via Cursor cron trigger.

This script is the standalone reference implementation. The live automation runs
inside a Cursor Cloud Agent that has native MCP access to Granola and Slack.
Use this script as a local fallback or for testing.

Setup:
  pip install requests python-dateutil

Secrets (add via Cursor Dashboard → Cloud Agents → Secrets):
  SLACK_BOT_TOKEN  — xoxb-... Slack bot OAuth token (needs chat:write scope)

Slack target: D06E4QMHCNN
"""

import os
import sys
import json
import requests
from datetime import datetime, timezone, timedelta
from typing import Any

# ── Config ──────────────────────────────────────────────────────────────────
SLACK_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL = "D06E4QMHCNN"
PDT = timezone(timedelta(hours=-7))


# ── Slack helpers ─────────────────────────────────────────────────────────────
def post_slack_message(token: str, channel: str, blocks: list[dict], fallback_text: str) -> dict:
    """Send a Block Kit message. Raises on HTTP or API errors."""
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
    payload = resp.json()
    if not payload.get("ok"):
        raise RuntimeError(f"Slack API error: {payload.get('error')} — {payload}")
    return payload


def header(text: str) -> dict[str, Any]:
    return {"type": "header", "text": {"type": "plain_text", "text": text, "emoji": True}}


def md(text: str) -> dict[str, Any]:
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}


def fields(*texts: str) -> dict[str, Any]:
    return {
        "type": "section",
        "fields": [{"type": "mrkdwn", "text": t} for t in texts],
    }


DIVIDER: dict[str, Any] = {"type": "divider"}


# ── Message builder ───────────────────────────────────────────────────────────
def build_daily_summary_blocks(
    date_label: str,
    meetings: list[dict],
    decisions: list[dict],
    my_actions: list[str],
    team_actions: list[tuple[str, str]],
    open_questions: list[str],
    closing: str,
) -> list[dict]:
    """
    Assemble Slack Block Kit blocks for the daily briefing.

    Args:
        date_label:     Human-readable date string.
        meetings:       List of {title, time} dicts.
        decisions:      List of {title, source, decision, rationale, owners} dicts.
        my_actions:     List of action strings owned by Manan.
        team_actions:   List of (owner, task) tuples.
        open_questions: List of question strings.
        closing:        Upbeat closing note.
    """
    blocks: list[dict] = []

    # Header
    blocks.append(header(f"Your Daily Decision Briefing — {date_label}"))
    meeting_titles = " · ".join(f"_{m['title']}_" for m in meetings)
    blocks.append(md(
        f"Hey Manan! Your Chief of Staff here with your end-of-day rundown. "
        f"You had a *packed, high-impact day* — {len(meetings)} meetings, "
        f"{len(decisions)} key decisions, {len(my_actions)} personal action items.\n\n"
        f"*Meetings:* {meeting_titles}"
    ))

    # Decisions
    blocks.append(DIVIDER)
    blocks.append(md("📋 *DECISIONS MADE TODAY*"))
    for i, d in enumerate(decisions, 1):
        body = f"*{i}. {d['title']}* _({d['source']})_\n"
        body += f"• *Decision:* {d['decision']}\n"
        body += f"• *Rationale:* {d['rationale']}"
        if d.get("owners"):
            body += f"\n• *Owners:* {d['owners']}"
        blocks.append(md(body))

    # My action items
    blocks.append(DIVIDER)
    action_lines = "\n".join(
        f"{i}\u20e3 {a}" for i, a in enumerate(my_actions, 1)
    )
    blocks.append(md(f"✅ *YOUR ACTION ITEMS (Manan owns)*\n\n{action_lines}"))

    # Team action items
    blocks.append(DIVIDER)
    blocks.append(md("🔁 *TEAM ACTION ITEMS TO TRACK*"))
    for i in range(0, len(team_actions), 2):
        chunk = team_actions[i : i + 2]
        texts = [f"*{owner}*\n{task}" for owner, task in chunk]
        blocks.append(fields(*texts))

    # Open questions
    blocks.append(DIVIDER)
    q_lines = "\n".join(f"• {q}" for q in open_questions)
    blocks.append(md(f"🔮 *KEY OPEN QUESTIONS*\n\n{q_lines}"))

    # Closing
    blocks.append(DIVIDER)
    blocks.append(md(closing))

    return blocks


# ── Data for June 15, 2026 ────────────────────────────────────────────────────
# This data was sourced from Granola meeting notes via the MCP integration.
# In the live automation the AI agent pulls this dynamically.
JUNE_15_DATA = dict(
    date_label="Monday, June 15, 2026",
    meetings=[
        {"title": "Hiring – Week in Review", "time": "9:00 AM PDT"},
        {"title": "Applicant Flow Sprint Planning", "time": "10:00 AM PDT"},
        {"title": "Manan/Dana 1:1", "time": "12:30 PM PDT"},
        {"title": "Job Level Details in Salesforce", "time": "1:30 PM PDT"},
    ],
    decisions=[
        {
            "title": "Salesforce Data Pipeline: Phased Approach",
            "source": "1:30 PM — Job Level Details in Salesforce",
            "decision": "Ship an unhealthy-job flag first (≤ threshold applicants by day 5), then build full per-job detail in Phase 2.",
            "rationale": (
                "Flag-only ships fast, is enough to trigger outreach cadences, and lets reps "
                "god-mode in for specifics. Full job object is a heavier build (schema creation, "
                "upsert logic, nightly insert + update cycles). Ship fast → learn fast."
            ),
            "owners": "Nelson (Databricks notebook), Rich (Hightouch), Lee (Salesforce config + cadence)",
        },
        {
            "title": "Communications Agent: Stay the Course",
            "source": "12:30 PM — Manan/Dana 1:1",
            "decision": "Divij continues building — no course change.",
            "rationale": (
                "Reversing again creates perpetual churn. Text engagement is validated; agentic "
                "texting is an incremental evolution. Risk to watch: if low screener completion is "
                "a trust/scam-perception issue, RCS or a verified profile may matter more than tone. "
                "This week's personalization test will provide signal."
            ),
            "owners": "Divij",
        },
        {
            "title": "Project Lead Model: Mandatory for Every Sprint Project",
            "source": "10:00 AM — Applicant Flow Sprint Planning",
            "decision": (
                "Each project gets a named lead owning: partner interface, unblocking teammates, "
                "end-to-end QA, and handoff doc."
            ),
            "rationale": (
                "Accountability at sprint boundaries. Stretch/incomplete tickets must be moved to "
                "backlog with priority set before handoff (engineering definition of done)."
            ),
            "owners": "Jatin (automating definition-of-done checklist via Linear skill)",
        },
        {
            "title": "Indeed Headless Browser: Gate on Explicit Go/No-Go",
            "source": "10:00 AM — Applicant Flow Sprint Planning",
            "decision": "No greenlight yet — explicit go/no-go required before any further build.",
            "rationale": (
                "John surfaced real reputational risk if Indeed detects the browser. "
                "Bob (ex-Wonolo) may have relevant context. Customers care about applicant quantity "
                "and quality, not source — this is purely a supply and risk calculation."
            ),
            "owners": "Manan to drive decision this week",
        },
        {
            "title": "Sales Trial Extensions: Annual Plans + True ICP Only",
            "source": "9:00 AM — Hiring Week in Review",
            "decision": (
                "Trial extensions to capture credit cards should apply only to annual-plan customers "
                "who are genuine ICPs (frequent hirers)."
            ),
            "rationale": (
                "Broad extensions risk a month-2 churn spike. Some churned accounts never posted "
                "a job after subscribing — broad extensions subsidize non-ICP risk."
            ),
            "owners": "Usman to align sales team on guardrails this week",
        },
        {
            "title": '"Homebase = Your Personal Recruiter": Validate via AI Intake',
            "source": "9:00 AM — Hiring Week in Review",
            "decision": (
                "Fast-build digital AI intake on Vercel (~1-2 weeks) to collect transcripts "
                "and validate the framing at scale. Human intake continues in parallel."
            ),
            "rationale": (
                "Manual intake showed promising signal. Sequential testing: burn down bad signal "
                "fast, double down on good. Usman to run 20+ prospecting calls explicitly pitching "
                "the personal recruiter framing."
            ),
            "owners": "Dana / Ted (Vercel build), Usman (prospecting calls)",
        },
        {
            "title": "Applicant Flow: Three-Pillar Sequencing Locked In",
            "source": "12:30 PM — Manan/Dana 1:1",
            "decision": (
                "Front-load OEM spend enablement while talent pool experiments run in parallel. "
                "Funnel quick wins (HTML job pages for crawlability, instant live posting) already scoped."
            ),
            "rationale": (
                "Boosted jobs reach healthy status at ~50% vs. 26% unboosted, yet only 1.5% of Q2 "
                "jobs were boosted — fixing that gap is the highest-leverage move available right now."
            ),
            "owners": "Manan (overall), engineering leads per pillar",
        },
    ],
    my_actions=[
        "*Meet with Usman* — define exact fields/logic for the Salesforce unhealthy-job flag (threshold value, column spec) → feeds Nelson's Databricks build",
        "*Resend the applicant flow plan doc* to Dana",
        "*Share personalization screener test results* with Dana's team once complete — key input for the comms agent hypothesis",
        "*Follow up on checkout drawer update status* in the relevant Slack thread (billing team owns; flagged as in limbo)",
        "*Share the project lead responsibilities doc* with the engineering team",
        "*Message Matan (PMM) for sign-off* on screener copy messaging before Carlo implements",
        "*Assess Indeed headless browser feasibility* — decision expected this week; consider looping in Bob",
    ],
    team_actions=[
        ("Nelson", "Build Databricks notebook with unhealthy-job flag column"),
        ("Rich + Lee", "Hightouch connection + Salesforce cadence automation"),
        ("Jatin", 'Build Linear "work completed" audit skill for definition-of-done enforcement'),
        ("Carlo", "Check with Kristen/growth on Statsig feasibility for screener copy"),
        ("Tanner", "QA + handoff doc for post-job-creation boost; confirm Facebook taxonomy has no data team dependency"),
        ("Izzy", "Sync with Busman on boost button UI; lead Salesforce data pipeline sprint"),
        ("Usman", "Schedule V1→V2 migration call training for sales team; run 20+ personal recruiter prospecting calls"),
        ("Dana / Ted", "Fast-build AI intake on Vercel; begin collecting transcripts (~1 week)"),
        ("Each engineer", "Assess capacity today; flag to Manan by tomorrow AM if pulling from backlog"),
    ],
    open_questions=[
        "Is low screener completion a *personalization problem* or a *trust/scam-perception problem*? Watch CTR from this week's test closely.",
        "Day-5 unhealthy trial intervention: *sales* or *CS/support* as the owning function?",
        "Indeed headless browser: *go or no-go*? Get Bob's input first.",
        "Phase 2 Salesforce full job-level object: who leads scoping, and when does it kick off?",
    ],
    closing=(
        "You moved big rocks today, Manan — the phased Salesforce approach was a sharp call "
        "(ship fast, learn fast), the project lead model will pay dividends starting next sprint, "
        "and locking in the three-pillar sequencing gives the team a clear north star. "
        "Proud to be your chief of staff. Now go enjoy your evening! 🚀"
    ),
)


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    today = datetime.now(PDT).strftime("%A, %B %-d, %Y")
    print(f"Daily summary automation — {today}")

    blocks = build_daily_summary_blocks(**JUNE_15_DATA)

    if not SLACK_TOKEN:
        print(
            "\nERROR: SLACK_BOT_TOKEN not set.\n"
            "To enable Slack delivery:\n"
            "  1. Create a Slack app with the chat:write scope\n"
            "  2. Install it to your workspace\n"
            "  3. Copy the bot OAuth token (xoxb-...)\n"
            "  4. Add it as SLACK_BOT_TOKEN in Cursor Dashboard → Cloud Agents → Secrets\n\n"
            "Alternatively, authenticate the Slack MCP server in Cursor Desktop IDE\n"
            "so the Cloud Agent can use it directly.\n"
        )
        print("Message that WOULD be sent:")
        print(json.dumps(blocks, indent=2, ensure_ascii=False))
        sys.exit(1)

    fallback = f"Your Daily Decision Briefing — {JUNE_15_DATA['date_label']}"
    result = post_slack_message(SLACK_TOKEN, SLACK_CHANNEL, blocks, fallback)
    print(f"Sent! ts={result['ts']}, channel={result['channel']}")


if __name__ == "__main__":
    main()
