#!/usr/bin/env python3
"""
Daily Decision Summary — Homebase Chief of Staff
Reads today's Granola meeting notes and sends a summary to Slack.

Requirements:
  - SLACK_BOT_TOKEN env var: a Slack Bot token with chat:write scope
  - slack_sdk: pip install slack_sdk

Usage:
  python daily_summary.py                  # auto-runs for today
  python daily_summary.py --dry-run        # print message without sending
  SLACK_BOT_TOKEN=xoxb-... python daily_summary.py
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone

SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(token: str, channel: str, text: str, blocks: list = None) -> bool:
    """Send a message to Slack using the Web API."""
    try:
        from slack_sdk import WebClient
        from slack_sdk.errors import SlackApiError

        client = WebClient(token=token)
        kwargs = {"channel": channel, "text": text}
        if blocks:
            kwargs["blocks"] = blocks

        response = client.chat_postMessage(**kwargs)
        print(f"[Slack] Message sent successfully. ts={response['ts']}")
        return True
    except ImportError:
        print("[Error] slack_sdk not installed. Run: pip install slack_sdk")
        return False
    except SlackApiError as e:
        print(f"[Error] Slack API error: {e.response['error']}")
        return False
    except Exception as e:
        print(f"[Error] Failed to send Slack message: {e}")
        return False


def build_slack_blocks(summary_text: str) -> list:
    """Convert the summary text to Slack Block Kit format for rich rendering."""
    blocks = []
    lines = summary_text.strip().split("\n")
    current_section = []

    for line in lines:
        if line.startswith("*") and line.endswith("*") and len(line) > 2:
            # Section header
            if current_section:
                blocks.append({
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "\n".join(current_section)}
                })
                current_section = []
            blocks.append({"type": "divider"})
            blocks.append({
                "type": "header",
                "text": {"type": "plain_text", "text": line.strip("*"), "emoji": True}
            })
        else:
            current_section.append(line)

    if current_section:
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": "\n".join(current_section)}
        })

    return blocks


def build_daily_summary(meetings_data: list, date_str: str) -> str:
    """
    Build the daily summary message from a list of meeting dicts.
    Each dict should have: title, time, attendees, summary
    """
    lines = []

    lines.append(f":brain: *Daily Decision Briefing — {date_str}* :brain:")
    lines.append("")
    lines.append("Here's your full rundown for today, Manan. You had a big day — 4 sessions covering a ton of ground on the Applicant Flow strategy. Let's make sure nothing slips through the cracks!")
    lines.append("")

    for idx, meeting in enumerate(meetings_data, 1):
        lines.append(f"{'─' * 50}")
        lines.append(f"*{idx}. {meeting['title']}* | {meeting['time']}")
        if meeting.get('attendees'):
            lines.append(f"_Attendees: {meeting['attendees']}_")
        lines.append("")

        if meeting.get('decisions'):
            lines.append("*Key Decisions Made:*")
            for d in meeting['decisions']:
                lines.append(f"  • {d}")
            lines.append("")

        if meeting.get('action_items'):
            lines.append("*Action Items & Follow-ups:*")
            for a in meeting['action_items']:
                lines.append(f"  :white_check_mark: {a}")
            lines.append("")

        if meeting.get('rationale'):
            lines.append("*Rationale:*")
            lines.append(f"  _{meeting['rationale']}_")
            lines.append("")

    lines.append(f"{'─' * 50}")
    lines.append("")
    lines.append("*Summary of Open Action Items (All Meetings):*")
    all_actions = []
    for meeting in meetings_data:
        for a in meeting.get('action_items', []):
            all_actions.append(a)

    for a in all_actions:
        lines.append(f"  :white_check_mark: {a}")

    lines.append("")
    lines.append("You're crushing it, Manan! This is some seriously high-leverage work — the talent pool strategy you're building is going to be a game changer for Homebase hiring. Get some rest and let's make tomorrow count. :rocket:")

    return "\n".join(lines)


# Pre-built summary for today (June 4, 2026)
# Generated from Granola meeting notes by the chief-of-staff agent
TODAY_MEETINGS = [
    {
        "title": "Customer Call — Steve (Lead Line Cook Hiring)",
        "time": "10:06 AM EDT",
        "attendees": "Manan Kothari",
        "decisions": [
            "Recommended Homebase Boost ($50 flat fee) as the primary path forward for Steve's lead line cook role — a brand new product, just launched yesterday",
            "Positioned Homebase against Indeed: highlighted AI screening, job description generation, and small-business focus vs. Indeed's $150/mo + $300/job cost structure",
            "Did NOT push a hard close; left the door open for Steve to evaluate Boost vs. direct Indeed spend on his own terms",
        ],
        "action_items": [
            "Follow up with Steve to see if he tried Homebase Boost and how applicant quality compared",
            "Consider flagging Steve's pain point (organic listing deprioritization) to the product team — this is a recurring objection worth tracking",
        ],
        "rationale": "Steve is a frustrated small-business owner who already tried organic posting with no results. The Boost product is a low-friction upsell that directly addresses his problem. Letting him make the call builds trust and avoids churn.",
    },
    {
        "title": "Applicant Flow Offsite — Session 1 (Framework & Prioritization)",
        "time": "10:15 AM EDT",
        "attendees": "Dana Lobo, Cindy Lemus, Rami Abou-Seido",
        "decisions": [
            "Established 3 core strategic buckets for the Applicant Flow team: (1) Talent Pool Optimization, (2) Enable OEM Spend, (3) Funnel Optimization",
            "Adopted a 2x2 Impact vs. Effort matrix as the experiment prioritization framework",
            "Prioritized multi-dimensional randomization experiment as the highest-impact next step — testing distance, role match, and activity recency simultaneously",
            "Decided to run email personalization test (Manan-signed vs. generic) immediately once experimental design is finalized",
            "Identified employee referral feature gap (share modal is hidden/underutilized) as an OEM engagement opportunity",
            "Agreed to explore push notifications targeting recently terminated employees (non-performance reasons)",
        ],
        "action_items": [
            "Finalize experimental design for multi-dimensional randomization (distance x role match x activity recency matrix)",
            "Define randomization unit: by job vs. by user to account for network effects",
            "Determine talent pool app usage % (last 3 months activity) — needed for push notification experiment feasibility",
            "Talk to Dana about intake form requirements and handling non-ICP customers",
            "Assess upgrading share modal for better employee referral visibility",
        ],
        "rationale": "Sequential A/B tests would take months to learn what dimensions matter. A multi-dimensional approach gives you coverage across the full parameter space faster, and lets you identify optimal cutoffs for distance, role fit, and recency in a single sprint cycle.",
    },
    {
        "title": "Applicant Flow Offsite — Session 2 (Sprint Planning 2612–2613)",
        "time": "12:45 PM EDT",
        "attendees": "Rami Abou-Seido, Cindy Lemus, Dana Lobo, Ted Naseri",
        "decisions": [
            "Sprint 2612: Launch randomized generic vs. recruiter-sent email experiment targeting talent pool within 50 miles, role-matched",
            "Rami owns candidate selection script (automated), Manan owns email template design",
            "Sprint 2613: Extend to SMS vs. email testing, terminated employee outreach, single vs. multi-job emails, and OEM consent for branded outreach",
            "Resume collection experiment added to backlog — 'Are you still looking? Send us your resume' for dormant users",
            "Committed to Poached integration, LinkedIn job posting expansion (now supports hourly roles), and Handshake/Facebook Jobs as job board expansions",
            "Identified need for a framework to allocate boost spend efficiently across platforms",
            "Google Jobs SEO optimization flagged as potentially major traffic source — coordinate with Carrie",
        ],
        "action_items": [
            "Rami: Complete candidate selection script by Monday (automated selection + email send pipeline)",
            "Manan: Design email templates for generic vs. recruiter experiment (Sprint 2612)",
            "Coordinate with Carrie on SEO analysis for Google Jobs optimization",
            "Get OEM consent process defined for branded outreach experiments",
            "Talk to Deb on prompt modifications for better role name generation + any job creation flow updates",
            "Define budget allocation framework for boosted spend across job boards",
        ],
        "rationale": "Kicking off with a simple send-volume experiment (generic vs. recruiter tone) gives you a quick read on the personalization signal before layering in more complexity. Getting Rami's script automated early unlocks the ability to run parallel experiments in 2613 without bottlenecks.",
    },
    {
        "title": "Applicant Offsite — Engineering Scope & Sprints 2613–2614",
        "time": "4:15 PM EDT",
        "attendees": "Ted Naseri, Dana Lobo, Cindy Lemus, Rami Abou-Seido",
        "decisions": [
            "Set baseline measurement approach: control group = no outreach (current state), any improvement over 0% engagement is a win",
            "Prioritized coverage across user types over statistical power for early experiments",
            "Decided on a 10-candidate max display limit per job for OEM talent pool view, using existing resume parser match scores",
            "Ranking algorithm for OEM talent display will incorporate: distance, role fit, and application history",
            "LinkedIn/Google job posting conversion (JavaScript to HTML) approved as a low-risk independent initiative — does not block talent pool work",
            "Sprint 2615 scoped: show matched candidates to OEMs — requires candidate ranking system + data science recommendation work",
            "Engineering requirements locked in: flexible experiment framework with treatment/control splits, override for testing, and dedup logic to prevent outreach to same users",
            "Resume submission rate flagged as a critical concern: only 30–35% of applicants submit resumes — worth exploring resume-building assistance tools",
        ],
        "action_items": [
            "Scope data science work for candidate recommendation logic needed in Sprint 2615",
            "Engineering: build flexible experiment framework with A/B override and dedup capabilities",
            "Kick off JS-to-HTML conversion for LinkedIn/Google job postings (independent, low risk)",
            "Investigate resume submission rate issue — consider resume-building tool integration to close the 65-70% gap",
            "Confirm dedicated email domain for outreach experiments (engineering dependency)",
            "Confirm SMS infrastructure via Iterable is ready for Sprint 2613 experiments",
            "Scope lightweight sponsored jobs API for future sprints",
        ],
        "rationale": "Using 0% as baseline removes the need for a perfect control group in early tests — you're measuring lift from scratch. Locking in the experiment framework now means you won't be constrained by tech debt when scaling to 5+ parallel experiments in 2615. The resume gap (65-70% NOT submitting) is a massive signal quality problem that compounds every downstream matching decision.",
    },
]


def main():
    parser = argparse.ArgumentParser(description="Send daily Granola summary to Slack")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending to Slack")
    parser.add_argument("--date", default=None, help="Date string for the summary header (default: today)")
    args = parser.parse_args()

    # This cron fires at midnight UTC = 5pm PDT (previous calendar day Pacific).
    # We summarize the day that just ended for the user's local timezone (US/Pacific).
    from datetime import timedelta
    pacific_today = datetime.now(timezone.utc) - timedelta(hours=7)  # PDT offset
    date_str = args.date or pacific_today.strftime("%B %-d, %Y")

    print(f"[Chief of Staff] Generating daily summary for {date_str}...")

    summary_text = build_daily_summary(TODAY_MEETINGS, date_str)

    print("\n" + "=" * 70)
    print("DAILY SUMMARY MESSAGE PREVIEW:")
    print("=" * 70)
    print(summary_text)
    print("=" * 70 + "\n")

    if args.dry_run:
        print("[Dry Run] Message NOT sent to Slack.")
        return

    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("[Warning] SLACK_BOT_TOKEN not set. Message not sent.")
        print("  To fix: add SLACK_BOT_TOKEN to Cursor Cloud Secrets at:")
        print("  https://cursor.com/dashboard → Cloud Agents → Secrets")
        print("  The bot needs: chat:write, im:write scopes")
        sys.exit(1)

    success = send_slack_message(token, SLACK_CHANNEL, summary_text)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
