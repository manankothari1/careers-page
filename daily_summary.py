#!/usr/bin/env python3
"""
Daily Decision Summary - Homebase PM Chief of Staff
Runs at 5pm PDT (midnight UTC) via Cursor cron automation.
Pulls today's Granola meetings and sends a summary to Slack.

Requires: SLACK_BOT_TOKEN environment variable
"""

import os
import sys
from datetime import datetime, timezone, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_CHANNEL = "D06E4QMHCNN"

def send_slack_message(message: str) -> bool:
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN environment variable not set.")
        print("Please add it in the Cursor Dashboard → Cloud Agents → Secrets.")
        print("\n--- MESSAGE THAT WOULD HAVE BEEN SENT ---")
        print(message)
        return False

    client = WebClient(token=token)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message,
            mrkdwn=True,
        )
        print(f"Message sent successfully. ts={response['ts']}")
        return True
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        return False


def build_daily_summary(date_str: str, meetings: list[dict]) -> str:
    """
    Build the Slack message from a list of meeting dicts.
    Each dict has: title, time, decisions, action_items
    """
    lines = []
    lines.append(f":sunrise: *Daily Decision Summary — {date_str}* :sunrise:")
    lines.append(f"Hey Manan! Here's everything you accomplished and decided today. You crushed it — 4 meetings, a ton of momentum across Hiring, Applicants, and the Iterable pipeline. Let's make it stick! :rocket:\n")
    lines.append("─" * 60)

    for i, m in enumerate(meetings, 1):
        lines.append(f"\n*{i}. {m['title']}* _{m['time']}_")
        if m.get("decisions"):
            lines.append("  *Key Decisions:*")
            for d in m["decisions"]:
                lines.append(f"  • {d}")
        if m.get("action_items"):
            lines.append("  *Action Items / Follow-ups:*")
            for a in m["action_items"]:
                lines.append(f"  ✅ {a}")

    lines.append("\n" + "─" * 60)
    lines.append("\n:trophy: *Top 5 Things to NOT Drop This Week:*")
    lines.append("  1️⃣  Make the call on 'Drive off the lot' — keep it live or pause for message test?")
    lines.append("  2️⃣  Send Anudeep the final talent pool table schema *today*.")
    lines.append("  3️⃣  Set up Iterable recruiter vs. generic email templates + attribution URLs.")
    lines.append("  4️⃣  Decide on Indeed headless browser approach with Izzy.")
    lines.append("  5️⃣  Follow up with Jenna (marketing) on SEO indexing guidance.")
    lines.append("\n_You've got this. Talk tomorrow! 💪_")
    return "\n".join(lines)


if __name__ == "__main__":
    # This script is meant to be called by the Cursor cron automation,
    # but can also be run standalone with the meeting data passed in.
    # When run from the Cursor agent, meeting content is passed as an argument.

    pdt = timezone(timedelta(hours=-7))
    today = datetime.now(pdt).strftime("%A, %B %-d, %Y")

    # Pre-built summary for June 22, 2026 (populated by Cursor agent at runtime)
    if len(sys.argv) > 1 and sys.argv[1] == "--today":
        print(f"Today is: {today}")
        print("Run this script from the Cursor cron agent for live data.")
        sys.exit(0)

    meetings = [
        {
            "title": "Hiring - Week in Review",
            "time": "8:15 AM PDT",
            "decisions": [
                "Sprint 2612 officially marked *off track* — root causes: unexpected OOOs and over-scoped domain events work.",
                "Starter plan removed from self-serve → ASP jumped as expected; still available for franchise sales.",
                "'Drive off the lot' experiment (49% ICP lift) — consensus leaning toward *keeping it live*; defer formal decision to a separate discussion today.",
                "SEO strategy: *optimize tagging and indexing first* before converting JS job pages to HTML. Carlo to keep capacity ready.",
                "Prospecting: 'delegation' framing resonates most across Usman's 11 pitches.",
                "Indeed silent job failures — two root causes: (1) copied jobs flagged as duplicates, (2) OEMs can't reactivate. Both spikes assigned.",
                "Source claiming framed as a *named benefit of the $100/month plan*, not an implementation step.",
            ],
            "action_items": [
                "Decide whether to keep 'Drive off the lot' live (Manan — today)",
                "Enable Amplitude recordings on zero state page to track tile engagement (Manan)",
                "Unblock zero state page launch — get Jatine's input on HB1 ICP calculation incompatibility (Manan)",
                "Listen to Usman's 11 prospecting pitch recordings — due EOD Jun 22 (team)",
                "Set up Slack alert for new trial starts → immediate call to pitch and gather feedback (Manan)",
                "Analyze starter plan removal: funnel shape, price elasticity, who opted out (Manan)",
                "Determine how much job description change prevents Indeed duplicate flagging (Carlo, Izzy)",
            ],
        },
        {
            "title": "Anudeep / Manan",
            "time": "9:59 AM PDT",
            "decisions": [
                "*Preferred integration route: High Touch* (analytics team / Rohit) — simpler than joining into existing data engineering pipeline.",
                "Fallback if High Touch fails: Anudeep joins the new table into existing Iterable pipeline.",
                "New talent pool table fields confirmed: job request ID, email, first/last name, job city, job link (Rami adds role type, distance).",
                "Table to be ready *end of day Jun 22*.",
            ],
            "action_items": [
                "Send final talent pool table name + schema to Anudeep once finalized with Rami (Manan — EOD Jun 22)",
                "Talk to Rohit about High Touch path; if it doesn't work, reply to thread and tag Anudeep (Manan)",
            ],
        },
        {
            "title": "Hiring: Sprint Planning - Applicants",
            "time": "10:30 AM PDT",
            "decisions": [
                "New Linear convention: 'hiring-applicants' label on all issues; engineering lead = single point of contact per issue.",
                "Homebase Boost source tagging ready to release — stored as 'TellRoot' on backend, displayed as 'Homebase Boost' to customers.",
                "Healthy boolean to Salesforce: no engineering needed — Nelson using HiTouch directly for Usman.",
                "Headless browser spike is top priority for Izzy after current release; *not time-boxable to one day* — needs infra sync first.",
                "Manan to make the call on Indeed relationship risk (automated account management) for headless browser approach.",
                "Alternative Indeed path: have customers add Homebase as an admin on their Indeed account.",
                "HTML/SEO job pages: *no JS→HTML conversion yet* — optimize SEO tagging + indexing first.",
                "Indeed silent failures — two spikes: copy+description tweak vs. reactivation path.",
                "Lightweight sponsored jobs API: likely deferred until silent failures fixed (depends on 3LO + source claiming UI).",
                "Role/salary/job description recommendations: data science heavy; Tanner to partner on UI design with Fatty this sprint.",
            ],
            "action_items": [
                "Verify 'Homebase Boost' source display and close the ticket (Manan)",
                "Post QA rundown for Datadog logging in Slack (Carlo)",
                "Follow up with Jenna on SEO indexing guidance — already messaged her (Manan)",
                "Decide on headless browser vs. admin-access approach for Indeed (Manan — this sprint)",
                "Indeed silent failure spikes: what's needed to tweak job description on copy? Is reactivation a simple status flag? (Carlo, Izzy)",
                "Loop Tanner into job description + salary recommendation UI design with Fatty this sprint (Manan)",
                "Schedule points estimation call for sprint 2613 (Jatin)",
            ],
        },
        {
            "title": "Rami/Manan (+ Rohit)",
            "time": "12:00 PM PDT",
            "decisions": [
                "Talent pool table grain confirmed: *job × applicant* (one row per user per job); Rami adding 'processed_date' to avoid reprocessing.",
                "Iterable user profile = most recent job row per sync cycle; historical job sends tracked via Iterable campaign data.",
                "Two talent sources unified under *talent_id + talent_type* (archived users vs. previous applicants).",
                "Experiment design: *two treatments* — recruiter-style email vs. generic email; control gets no email.",
                "Randomization via hashing (role type, business type, city, lat/long) — same business/role stays in same group across runs.",
                "Adding *within-location randomization* so the same role can have both variants.",
                "Treatment naming: required 'treatment_name' field (e.g. 'recruiter', 'generic') rather than treatment_1/treatment_2.",
                "Experiment name ('salt') added to hash string so groups reshuffle across experiments.",
                "For now: *one email per user per day*, prioritizing the closest open job not yet applied to.",
                "Role normalization: split into cached system prompt + small user message to reduce token usage; deduplicate on role + business type before calling OpenAI.",
                "Active jobs filter added: WHERE jr.status = 'active' in job request query.",
                "Role recommendations + salary work *deferred to tomorrow's meeting with Ted*; Manan to bring Fatty (design) and a front-end engineer.",
            ],
            "action_items": [
                "Update talent pool table with: processed_date, treatment_name, talent_id/type columns, active job filter, within-location randomization; send final schema to Rohit (Rami)",
                "Confirm High Touch destination schema and request write access from analytics team (Rohit)",
                "Set up Iterable campaign + recruiter vs. generic email templates; add query params to job URLs for attribution tracking (Manan)",
                "Resolve Databricks job secrets for OpenAI API key — get Applied AI team to handle secret injection (Rami)",
                "Bring Fatty + front-end engineer to tomorrow's meeting with Ted for role recommendations + salary work (Manan)",
            ],
        },
    ]

    message = build_daily_summary(today, meetings)
    send_slack_message(message)
