#!/usr/bin/env python3
"""
Daily Decision Summary - April 16, 2026
Chief of Staff briefing for Manan Kothari, PM @ Homebase
Covers: Cindy / Manan 1:1 (Apr 15 10:30 AM) - Boost Strategy & Entry Points
"""
import os
import json
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Summary \u2014 Wednesday, April 16 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Another solid day in the books. You had one meeting today \u2014 a meaty Boost strategy session with Cindy & Matan. Here\u2019s everything you decided, why it matters, and what needs to happen next. Let\u2019s go! \U0001f680"
        }
    },
    {"type": "divider"},

    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 1: Three Official Boost Entry Points Locked*\n*Meeting:* Cindy / Manan \u2014 Apr 15 @ 10:30 AM\n\n*What you decided:* Boost will be surfaced in exactly three places: (1) the Job Creation Flow, (2) the Jobs section (rocket icon \u2192 'Sponsor Your Job'), and (3) Email/Push notifications.\n\n*Why:* Boost is currently too hidden. Customers don\u2019t know it exists. Making it visible in the creation funnel, on the job detail, and via async messaging builds awareness at every stage of the job lifecycle.\n\n*Rationale:* Cindy surfaced that the rocket icon means nothing to users. Naming it 'Sponsor Your Job' borrows familiar language from Indeed/LinkedIn and removes ambiguity. Awareness = the #1 bottleneck right now."
        }
    },
    {"type": "divider"},

    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 2: 'Boost' \u2192 'Sponsored Job' Rebrand*\n\n*What you decided:* Kill 'Boost Your Job' language. Shift to 'Sponsor Your Job' / 'Sponsored Job Post' across all touchpoints \u2014 modal, to-dos, emails.\n\n*Why:* 'Boost' is jargon. 'Sponsored' is the industry-standard term users recognize from Indeed/LinkedIn. Alignment on language = less cognitive friction at purchase.\n\n*Immediate impact:* Modal copy needs updating today. The '8x more applicants' claim is repetitive and needs to be cut."
        }
    },
    {"type": "divider"},

    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 3: Phase 1 = Free Boost for Every Trial User (Remove Zip & Craigslist Options)*\n\n*What you decided:* For the next 3 weeks (through Launch Week), every trial user gets a Home Base Boost automatically. We tell them: 'We\u2019re boosting your job for free \u2014 $50 value.' Zip Recruiter and Craigslist options are removed from the modal for now.\n\n*Why:* You\u2019re already boosting every job via Taru. This is a no-engineering-lift win \u2014 just surface the fact that you\u2019re doing it. Removing Zip/Craigslist simplifies the decision and makes the free value crystal clear.\n\n*Rational:* Cindy\u2019s framing was sharp: 'We\u2019re not asking them to choose. We\u2019re telling them we did it.' May is the right window to build the intelligent threshold (if job already has 10+ applicants, suppress the boost CTA)."
        }
    },
    {"type": "divider"},

    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 4: Boost Attribution Display on Job Detail Page*\n\n*What you decided:* When a job is boosted, surface that fact on the job detail page \u2014 succinctly (e.g. 'Boosted \u2022 13 applicants generated'). No modal. Think green badge / live indicator, not a banner.\n\n*Why:* Matan\u2019s concern: if Homebase is spending $35/job on 5,000 trial users (~$175k/quarter), you need to *get credit* for driving applicant volume. If users don\u2019t know the boost caused the applicants, they won\u2019t pay for it post-trial.\n\n*Key insight:* The $1.75/applicant cost via Taru is the benchmark. Cindy\u2019s framing: 'We spent $50 and got you 15 applicants' \u2014 make that equation visible in the product."
        }
    },
    {"type": "divider"},

    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 5: Email/Push Trigger = Day 1, <5 Applicants, Max 2 Notifications*\n\n*What you decided:* Lifecycle email/push notif fires on Day 1 if a job has fewer than 5 applicants. Cap at 2 sends per user. Evergreen awareness email (non-triggered) also goes out to all OEMs.\n\n*Why:* Two data points you cited with high confidence: (1) Job boards prioritize jobs <3 days old. (2) Jobs that don\u2019t get ~5-7 applicants on Day 1 almost never become healthy. The window to intervene is Day 1.\n\n*Balance:* Don\u2019t pound users with notifications. Cindy noted the job-live email is already busy. Keep push restrained. One lifecycle awareness email + max 2 trigger notifications = the ceiling."
        }
    },
    {"type": "divider"},

    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decision 6: Intelligent Boost Threshold = Phase 2 (End of May)*\n\n*What you decided:* Building logic to suppress boost for jobs that are already healthy (10+ applicants Day 1) is *not* mission critical for Launch Week. That\u2019s a May deliverable.\n\n*Why:* Phase 1 is just awareness. It\u2019s OK to boost every trial job for 3 weeks. The threshold logic is important but requires engineering context on what\u2019s actually feasible. Don\u2019t block Launch Week on it.\n\n*Cindy + Manan alignment:* Unanimous. Phase 1 ships as-is; Phase 2 refines targeting in May."
        }
    },
    {"type": "divider"},

    # Action Items
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a1 Action Items \u2014 Yours to Own*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *[TODAY - EOD]* Update Boost modal copy: kill '8x more applicants,' rename to 'Sponsor Your Job,' clean up radio button cards to show price clearly\n\u2022 *[TODAY - EOD]* Share updated modal copy + messaging ideas with Cindy & Matan async\n\u2022 *[TOMORROW AM]* Regroup with Cindy + Matan to finalize decisions \u2014 meeting already set\n\u2022 *[TOMORROW AM]* Post Boost plan update to #leads channel (Phase 1 vs Phase 2 framing, rationale for Ray)\n\u2022 *[TOMORROW AM]* Create Linear ticket for Boost entry points + attribution work\n\u2022 *[ASAP]* Confirm with engineering: TLWA company-level syndication pre-approved? Job-level syndication instant? (Cindy thinks yes \u2014 verify before LW)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a1 Action Items \u2014 Matan*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *[TODAY - EOD]* Draft one-liner on Boost value prop for all copy surfaces\n\u2022 *[THIS WEEK]* Define messaging for trigger email: subject line, body, timing, CTA"
        }
    },
    {"type": "divider"},

    # Carry-forward items
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd34 Still Overdue \u2014 Don't Let These Slip*\n\n\u2022 *TLWA Launch Week Brief \u2192 Ted* \u2014 NOW 14 DAYS OVERDUE. Cindy literally mentioned TLWA briefs in today\u2019s meeting. Do this before you sleep.\n\u2022 *Manual Mode green light* \u2014 Cindy QA is done. It\u2019s on you. Greenlight it.\n\u2022 *Homebase Boost SKU kick-off \u2192 Chris McIntosh* \u2014 Billing window is closing. Today\u2019s session surfaced all the pricing context you need.\n\u2022 *Nelson: metro_area + bucketed_role + matching_roles columns* \u2014 Overdue since Apr 8.\n\u2022 *TLWA careers page QA w/ Fadi* \u2014 50k QR codes cannot go out with broken pages."
        }
    },
    {"type": "divider"},

    # Momentum note
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcaa Quick Win to Celebrate*\nYou locked a clean, phased Boost strategy in under an hour. Phase 1 is simple, ships fast, and sets up the attribution story. Phase 2 (intelligent threshold) has a real owner and a real timeline (May). That\u2019s exactly the kind of decision-making that keeps Launch Week on track. Proud of you, Manan \u2014 now go write that TLWA brief! \ud83d\ude04"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Your Chief of Staff \u2022 Apr 16, 2026 \u2022 Based on: Cindy/Manan 1:1 (Apr 15)_"
            }
        ]
    }
]


def send_slack(token, channel, blocks):
    payload = json.dumps({
        "channel": channel,
        "blocks": blocks,
        "text": "Your Daily Decision Summary - April 16, 2026"
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def preview(blocks):
    import sys
    out = sys.stdout.buffer
    def w(s):
        out.write((s + "\n").encode("utf-8", errors="replace"))
    w("=" * 70)
    w("DAILY DECISION SUMMARY PREVIEW (no SLACK_TOKEN set)")
    w("=" * 70)
    for block in blocks:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            w(text)
            w("")
        elif block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            w(f"### {text} ###")
            w("")
        elif block.get("type") == "divider":
            w("-" * 50)
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                w(el.get("text", ""))
            w("")


if __name__ == "__main__":
    if not SLACK_TOKEN:
        preview(BLOCKS)
        import sys
        sys.stdout.buffer.write(b"\nNOTE: Set SLACK_TOKEN secret in Cursor Dashboard to send this to Slack.\n")
    else:
        result = send_slack(SLACK_TOKEN, CHANNEL, BLOCKS)
        if result.get("ok"):
            print(f"Message sent successfully! ts={result.get('ts')}")
        else:
            print(f"Slack error: {result.get('error')}")
            raise SystemExit(1)
