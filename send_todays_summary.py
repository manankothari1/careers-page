#!/usr/bin/env python3
"""
Script to send today's pre-built summary to Slack.
Attempts using SLACK_BOT_TOKEN environment variable.
"""

import os
import json
import requests

SLACK_API_BASE = "https://slack.com/api"
SLACK_CHANNEL_ID = "D06E4QMHCNN"


def build_todays_message():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Chief of Staff Digest \u2014 Friday, June 11, 2026",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":sunny: Hey Manan! You had *4 meetings* today and made some seriously impactful decisions. "
                    "Here\u2019s your end-of-day rundown \u2014 every decision, every owner, every follow-up. "
                    "You crushed it today. Let\u2019s make sure nothing slips. :rocket:"
                )
            }
        },
        {"type": "divider"},

        # Meeting 1
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*1\ufe0f\u20e3 Hiring Leads Standup* \u2014 _8:45 AM PDT_ \u00b7 Fadi, Dana, Matan, Cindy, Jatin, Ray, Nelson, Jeff, Usman"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Decisions Made:*\n"
                    "\u2022 *PAUSE Indeed source claiming* \u2014 3\u20136 month process, 4\u20135 day turnaround cycles draining eng bandwidth. Engineers redirected to higher-impact items immediately.\n"
                    "\u2022 *Validate Jack & Jill value prop before building* \u2014 Matan\u2019s \u201cpersonal recruiter\u201d framing must be tested with *5 real customers first*. The value prop is not yet validated.\n"
                    "\u2022 *Adopt \u201cno regrets\u201d work framing* \u2014 Comms agent, UX paper cuts, deprecating V1, domain events, scheduling fixes proceed regardless of which value prop wins.\n"
                    "\u2022 *Auto-trigger unhealthy trial outreach in 24h* \u2014 Salesforce fires automatically if trial has <5 applicants in first week. No manual rep check.\n"
                    "\u2022 *Admin-side boost tool* \u2014 Reps can boost on behalf of customers (1 click). $50 cost vs. subscription = net positive. Worth testing as a closing lever."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Action Items:*\n"
                    ":small_red_triangle: *Dana + Matan* \u2014 Map hypothesis tree, identify big swings to validate \u2192 _Today_\n"
                    ":small_red_triangle: *Dana + Jatin* \u2014 Align on intake experiment build approach \u2192 _Today_\n"
                    ":small_orange_diamond: *Fadi + Dana + Jatin + FE* \u2014 Schedule product walkthrough to surface no-regrets burndown list \u2192 _ASAP_\n"
                    ":small_orange_diamond: *Usman* \u2014 Design Salesforce auto-trigger: <5 applicants in week 1 = sales motion fires in 24h\n"
                    ":small_orange_diamond: *Manan + Usman* \u2014 Align on boost positioning + unhealthy trial sales playbook"
                )
            }
        },
        {"type": "divider"},

        # Meeting 2
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*2\ufe0f\u20e3 Product/Sales Bi-Weekly* \u2014 _9:00 AM PDT_ \u00b7 _(Meeting canceled mid-call \u2014 Bobby joined before cancellation)_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Key Signal Captured:*\n"
                    "\u2022 *Cadence:* Front-loaded (2x/day) is too aggressive. Every 2\u20133 days after first contact is working better.\n"
                    "\u2022 *Contact overlap is a live problem* \u2014 No shared outreach tracking in Salesforce. Multiple reps are hitting the same prospect. A customer already complained. Needs fixing.\n"
                    "\u2022 *Best call windows:* 10am\u2013noon or 1\u20133pm in prospect\u2019s time zone.\n\n"
                    "*Action Item:*\n"
                    ":small_orange_diamond: *Usman / RevOps* \u2014 Implement contact-level outreach tracking in Salesforce to prevent duplicate touchpoints"
                )
            }
        },
        {"type": "divider"},

        # Meeting 3
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*3\ufe0f\u20e3 Hackathon Unlimited Show & Tell* \u2014 _10:30 AM PDT_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_No meeting notes recorded. Worth following up to capture hackathon outputs and any commits from the team._"
            }
        },
        {"type": "divider"},

        # Meeting 4
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*4\ufe0f\u20e3 Applicant Flow T-Shirt Sizing* \u2014 _1:30 PM PDT_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Sizing Decisions Locked In:*\n"
                    "```\n"
                    "Feature                              Eng      Design   Deps\n"
                    "Homebase Boost (admin for sales)     Low      None     \u2014\n"
                    "Dollar-for-dollar matching           Low      None     Billing\n"
                    "Sponsored jobs API (OEM\u2194Indeed)      Medium   Small    \u2014\n"
                    "Job seeker manual intake             Low      Low      \u2014\n"
                    "Single vs. multi-job email           Low      Low      \u2014\n"
                    "SMS vs. email vs. push               Low      Low      \u2014\n"
                    "HTML job pages (JS\u2192HTML)             Medium   None     Claude vibe-code\n"
                    "Automated email outreach             Medium   None     DE/Iterable pattern\n"
                    "Employee referral                    Medium   Medium   Abigail (buffer!)\n"
                    "Show talent pool to OEM              Large    Medium   \u2014\n"
                    "Job creation flow (all 3 combined)   High     High     One design pass\n"
                    "Auto go-live (skip in review)        High     Medium   \u2014\n"
                    "Job description optimization (LLM)  Medium   Low      LLM + DE\n"
                    "Salary recommendations               Low      Low      LLM\n"
                    "```"
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Key Decisions:*\n"
                    "\u2022 *Job creation flow = one design workstream.* Fraud check + role recs + salary recs all touch the same screen. Design together, not separately.\n"
                    "\u2022 *Employee referral \u2192 Abigail.* Share modal exists already \u2014 reuse it. Build explicit timeline buffer.\n"
                    "\u2022 *Automated email outreach may be zero product eng.* If DE already has a pattern to hit Iterable directly, product eng may not be needed at all. Critical to confirm.\n\n"
                    "*Action Items:*\n"
                    ":small_red_triangle: *Manan* \u2014 Confirm with DE: do they have an existing Iterable API call pattern? (Could eliminate a full medium-eng project)\n"
                    ":small_orange_diamond: *Manan + Cindy* \u2014 Align on job creation flow design pass (fraud check + role recs + salary recs as one)\n"
                    ":small_orange_diamond: *Manan* \u2014 Assign employee referral to Abigail with explicit timeline + buffer built in"
                )
            }
        },
        {"type": "divider"},

        # Top follow-ups callout
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:fire: Today\u2019s Top 3 Follow-Ups \u2014 Don\u2019t Let These Slip*\n\n"
                    ":red_circle: *DE Iterable check* \u2014 Could remove a whole medium-eng project from the roadmap. Confirm today or first thing tomorrow.\n"
                    ":red_circle: *Salesforce contact overlap* \u2014 Customers are already getting burned by duplicate outreach. Needs a fix before it kills more deals.\n"
                    ":large_yellow_circle: *Dana + Matan hypothesis tree* \u2014 This is the strategic foundation of Q3. Verify it happened as planned."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": ":robot_face: Generated by your Chief of Staff bot \u2014 5:00 PM PDT \u00b7 Friday, June 11, 2026 \u00b7 4 meetings reviewed"
                }
            ]
        }
    ]

    return {
        "channel": SLACK_CHANNEL_ID,
        "text": "Chief of Staff Digest \u2014 Friday, June 11, 2026",
        "blocks": blocks
    }


def main():
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN is not set.")
        print("\nHere is the full Slack Block Kit payload that would be sent:\n")
        payload = build_todays_message()
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    payload = build_todays_message()
    resp = requests.post(
        f"{SLACK_API_BASE}/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        data=json.dumps(payload),
        timeout=30,
    )
    result = resp.json()
    if result.get("ok"):
        print(f"Message sent! ts={result.get('ts')}")
    else:
        print(f"Slack error: {result.get('error')}")


if __name__ == "__main__":
    main()
