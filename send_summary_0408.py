#!/usr/bin/env python3
"""
Daily Decision Summary - April 8, 2026
Chief of Staff summary for Manan Kothari, PM @ Homebase
Slack channel: D06E4QMHCNN
"""
import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📋 Your Daily Decision Briefing — Wednesday, April 8",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Great day — you had one meeting today and it was a *productive one*. No decisions to second-guess here; you and Nelson locked in some smart bets. Here's your full rundown 👇"
        }
    },
    {"type": "divider"},

    # ── MEETING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🗓 Meeting Today: Nelson / Manan 1:1* (Apr 7, 10 AM)"
        }
    },

    # ── DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decisions Made*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Reframe the applicant health problem: absolute numbers, not percentages*\n"
                "> *Decision:* Stop optimizing for \"% of jobs with 20+ applicants\" — instead, calculate the *raw delta* of applications needed to make each unhealthy job healthy. Current answer: *~4,000 additional applications* needed platform-wide.\n"
                "> *Why:* The percentage staying flat (~14%) is actually expected as jobs on platform scale to 1.5k — you need applications to grow *faster* than jobs, not just proportionally. The delta number gives engineering & data science a concrete target to optimize against.\n"
                "> *Owner:* Nelson to deliver the absolute delta analysis."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Tellroo scaling: send (nearly) all jobs*\n"
                "> *Decision:* Expanded Tellroo job send from ~300 jobs → almost all active jobs. Exclusions: jobs that already have 10+ Tellroo applicants OR are already healthy.\n"
                "> *Why:* First-day application velocity is the single strongest predictor of job health (13 avg / 9 median apps on day 1 for eventually-healthy jobs). Tellroo is the lever we *can* control; cost is already paid per application.\n"
                "> *Status:* Already shipped. Watch for a noticeable health rate lift in the coming days."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Build job recommendation carousel on career pages*\n"
                "> *Decision:* Green-lit a \"similar jobs near you\" feature on the vibe-coded job page. Show even *1 matching job* — you explicitly pushed back on Nelson's instinct to require a higher threshold. Your logic: job seekers are primed to apply again immediately, especially with pre-filled resumes.\n"
                "> *Why:* ~200–300 applications/week flow through Homebase today. Even a 25% weekly lift (~50 extra applications) meaningfully dents the 4,000-application gap and is essentially free to test.\n"
                "> *You have a branch with UI already built.* This is ready to wire up the moment Nelson delivers data."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Job matching architecture: Supabase via Databricks pipeline*\n"
                "> *Decision:* Nelson will write job-matching data directly to Supabase (jobs table). Architecture: Databricks → Supabase (following pattern Ray already established), eventually migrating to HB1. No new infra resourcing needed now.\n"
                "> *Why:* Gets the experiment running quickly without a HB1 eng dependency. Clean path to productionize later.\n"
                "> *Schema locked:* Nelson adds (a) `metro_area` column, (b) `bucketed_role` column, (c) `matching_roles` column to the jobs table."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Role similarity: one-degree-of-separation bucketing (not exact match)*\n"
                "> *Decision:* Job recommendations will use bucketed roles + a distance threshold — e.g., a Barista should also see Counter Service / Cashier jobs, a Server should see Cashier jobs. Exact title matching explicitly rejected.\n"
                "> *Why:* Real job platforms don't do exact-match recommendations. One degree of separation maximizes relevant inventory, especially in smaller markets."
            )
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Action Items from Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Nelson (due TOMORROW, Apr 8):* Deliver to Supabase jobs table:\n"
                "  — `metro_area` column\n"
                "  — `bucketed_role` column (from existing role normalization mapping)\n"
                "  — `matching_roles` column (distance-based role similarity)\n"
                "• *Manan:* Send Nelson a screenshot of the job recommendation UI branch so he can align data schema to the front-end contract\n"
                "• *Manan:* Wire up job recommendation UI to Nelson's Supabase data feed once delivered\n"
                "• *Nelson:* Deliver absolute applicant-delta analysis (not %) — how many raw applications needed per job / in total to hit healthy threshold"
            )
        }
    },
    {"type": "divider"},

    # ── CARRYOVER CRITICAL ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Still Critical — Carry-Forward Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "These didn't come up today but they're not going away — you know the drill:\n\n"
                "🔴 *TLWA Launch Week brief → Ted* — 6 days overdue (was due Apr 2 EOD). This is your most overdue item.\n"
                "🔴 *Homebase Boost SKU kick-off w/ Chris McIntosh* — billing needs a 3-week lead for Early May. The window is closing this week.\n"
                "🟡 *Manual Mode green light* — Cindy's QA is done. It's on you. Just send the 'go'.\n"
                "🟡 *Jeff's Indeed 3LO prototype* — review it, send to team, write acceptance criteria\n"
                "🟡 *Generic roles proposal doc* — write both options, recommend location-mapping approach\n"
                "🟡 *Supabase tables + 60k upsert* — Manan to build, Nelson to validate\n"
                "🟡 *Fadi sync on sprint concerns* (Ray + Dana flags from Apr 3) — ideally today/tomorrow\n"
                "🟡 *Schedule Ted + Dana + Divij mentorship session*\n"
                "🟡 *Review Matan's 3 prototypes* + topical workplace prototype\n"
                "🟡 *Andrew 3LO spike review* + email Kenneth + add Ray"
            )
        }
    },
    {"type": "divider"},

    # ── KEY INSIGHT ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💡 Key Insight to Sleep On*\n\n"
                "First-day application velocity is your most important leading indicator for job health — "
                "and you now have a formula: jobs that eventually become healthy average *13 applications on day 1* (median: 9). "
                "Jobs with 1–2 on day 1 almost never recover. "
                "This is your north star for prioritizing *when* to boost (right away, not after day 3) "
                "and *which* jobs to boost (the ones that got < 5 on day 1)."
            )
        }
    },
    {"type": "divider"},

    # ── FOOTER ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "You're making great calls, Manan. The job recommendation feature is a smart, low-cost experiment "
                "that punches above its weight — go ship it. 🚀\n\n"
                "_Your Chief of Staff 🤝_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Daily Decision Summary — Apr 8, 2026",
    "blocks": blocks
}

def send_slack():
    if not SLACK_TOKEN:
        print("⚠️  No SLACK_TOKEN found — printing preview instead.\n")
        print(json.dumps(payload, indent=2))
        return

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✅ Slack message sent! ts={body.get('ts')}")
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")

if __name__ == "__main__":
    send_slack()
