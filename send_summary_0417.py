#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari - Apr 17, 2026 (covering Apr 16 meetings)"""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌟 Your Daily Debrief — Friday, April 17",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day yesterday — 5 meetings covering Talroo/CPA strategy, predefined roles, TLWA V2 badge launch, and V1 migration risk. Here's every decision you made, why it matters, and exactly what needs to happen next. Let's go! 🚀"
        }
    },
    {"type": "divider"},

    # DECISION 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #1: Switch Talroo Feed from Flat CPC → CPA Bidding*\n\n*What you decided:* Move the Talroo XML feed from flat CPC to CPA bidding, with a $35/job budget cap and a 4-category structure: (1) Entry Level $3–5, (2) Managerial, (3) Specialized (cooks/chefs/bartenders), (4) 'Desperation' high-CPA for hard-to-fill roles.\n\n*Why it's the right call:* CPA gives you dynamic bid optimization — jobs stay alive longer, bids auto-adjust to competition, and you only pay for actual lead submissions (name, email, phone). Your current $2.01/lead is solid; CPA lets you protect that while scaling. The $35 cap prevents runaway spend on any single job.\n\n*Risks to watch:* 3–5% of jobs have short/low-quality descriptions that get buried — Nelson needs to define the threshold so bad jobs don't eat budget."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• 📋 *Saja (Talroo)* — Send recommended categories + CPA ranges per tier by *today (Apr 17)* — then configure campaign before CPA switch goes live\n• 🛠️ *Manan (you)* — Add `category` and `CPA` nodes to XML feed, remove `CPC` node\n• 📏 *Nelson* — Define job description quality thresholds (character/line count minimums for posting requirements)\n• 💰 *Chris (Talroo)* — Research spend threshold benefits for scaling accounts"
        }
    },
    {"type": "divider"},

    # DECISION 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #2: Predefined Roles — 'Entry Point to Job Creation Flow' Approach*\n\n*What you decided:* For the CSV of predefined roles (tens of thousands already exist), use Approach 2: the predefined role is an *entry point into the job creation flow* (not a pre-created live job). User clicks 'activate' → drops into Step 2 of job creation → completes wage, schedule, params → full syndication kicks in.\n\n*Why it's the right call:* Approach 1 (pre-created hidden job) risks orphaned jobs and cluttered dashboards. Approach 2 keeps the user in control, preserves the full creation UX, and syndication only fires when the job is actually ready. Engineering delta is only 1–2 days.\n\n*Dependency:* Malcolm owns the Rake task / S3 upload mechanism and one-click post plumbing — he needs to be looped in immediately."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• 🔗 *Jatin* — Sync with Malcolm to understand current one-click post implementation and confirm the job creation flow integration point\n• 🤖 *Manan (you)* — Accelerate Divij's role-matching using cloud code (match business types to predicted roles for companies without existing rules)\n• 🗄️ *Manan (you)* — Ensure Supabase career page import respects existing customizations: check existing value first, only write Supabase data if field is empty (conditional fork per field)"
        }
    },
    {"type": "divider"},

    # DECISION 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #3: TLWA Careers Page V2 — Badge Under Address, Desktop Designs Urgent*\n\n*What you decided:* Top Local Workplace badge goes *underneath the address* on career pages. Jeff built the V2 tab with updated designs. QR code prototype designs will include the badge. Walk-in poster concept validated — custom QR code poster builder (like Cindy's branding tool), free premium printed version as part of the Week 1 welcome packet.\n\n*Why it's the right call:* 50k QR codes are going out — the badge needs to be there at launch. The walk-in poster solves the 'internal hiring' gap that front-door stickers don't cover. Free shipping removes friction for a high-value acquisition touchpoint.\n\n*Risk:* Desktop designs are *urgently needed* by engineers right now — any delay here is on the critical path to launch."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• 🎨 *Jeff* — Ship desktop designs for TLWA badge to engineers *ASAP* (this is blocking)\n• 🖨️ *Manan (you)* — Confirm timeline with Cassy (printer) for QR code production — ~3,000 unmailable addresses flagged, get count finalized before print run\n• 📐 *Jeff* — Finalize walk-in poster / custom QR code poster builder mockup for Week 1 welcome packet pitch\n• 🔄 *Manan (you)* — Preset data migration from Supabase to Homebase: sync with Jatin to confirm approach"
        }
    },
    {"type": "divider"},

    # DECISION 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #4: V1 Migration for Award Winners — Decision Needed TODAY*\n\n*What you decided (partially):* You flagged a critical risk — 50% of V1 users are TLWA award winners, and 75% of users with *live jobs* are award winners. This is your highest-sensitivity cohort. Three options are on the table but not yet resolved:\n1. Exclude award winners from the mailer entirely\n2. Optional V2 migration with better careers page as the carrot\n3. Solve by shipping generic role functionality (most complete but requires more piping)\n\n*Why this is urgent:* 50k QR codes are heading to print. If award winners get migrated to V2 before past-applicant visibility and quick-repost are ready, you'll break their experience and torch the relationship. This is a go/no-go decision.\n\n*Required piping for Option 3:* Generic role → job request mapping, non-expiring role functionality, multi-location company handling on careers page."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• 🚨 *Manan (you)* — Make the call TODAY: exclude winners from mailer, optional migration, or build generic role plumbing. Time-box is now.\n• 📊 *Fadi* — Finalize company winner list vs. location winner list — this feeds the mailer and the classifier\n• 🏗️ *Engineering* — If Option 3: scope generic role job request mapping + non-expiring role + multi-location careers page handling\n• 🤖 *Fadi* — Two-pass Haiku/Sonnet classifier for TLWA award winners is approved and running — confirm taxonomy alignment with Cindy's categories"
        }
    },
    {"type": "divider"},

    # DECISION 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #5: Predictive Role Timeline — Time-Boxed to Today*\n\n*What you decided:* You're time-boxing the predictive role timeline decision to today. If no conclusion is reached, you leave it as-is for the launch week QR code mailing (mail delivery delays from ~3k unmailable addresses may give a small buffer).\n\n*Why it's the right call:* Shipping without predicted roles is better than delaying the QR code mailer. The migration complexity is lower for users without live jobs — and most award winners (by definition) are active, so this is a calculated risk."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• ⏰ *Manan (you)* — Decide predictive role scope for launch mailer by end of day. Yes or no.\n• 📬 *Manan (you)* — Get final mailable address count from Cassy before committing to print volume"
        }
    },
    {"type": "divider"},

    # DECISION 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Decision #6: Boost CTA Noise — Flag Raised, Monitor*\n\n*What you decided:* Product noise concern surfaced — users are now seeing Indeed Boost CTA + one-time job post options + 3LO login prompts simultaneously. No hard decision made yet, but this is a real risk going into launch week.\n\n*Why it matters:* Too many competing CTAs will dilute conversion on all of them. The Boost Phase 1 plan (every trial user gets a free boost) needs to be *the* primary CTA, not one of five.\n\n*Recommendation:* Before launch week, align on a CTA hierarchy: 3LO OAuth first, then Boost, then other job board options. Don't let the modal become a buffet."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• 🗺️ *Manan + Cindy + Matan* — Map full CTA hierarchy in job creation flow before LW. What fires when, in what order, for which user segment\n• 📝 *Matan* — Post Boost plan update to #leads (Phase 1 vs Phase 2 rationale for Ray) — *still pending from Apr 16*"
        }
    },
    {"type": "divider"},

    # Overdue items
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Still Overdue / Carry-Forward (Don't Let These Slip)*\n\n• 📄 *TLWA/Launch Week brief* — NOW 15 DAYS OVERDUE — send to Ted *right now*\n• 💳 *Homebase Boost SKU kick-off with Chris McIntosh* — billing window is closing, schedule immediately\n• ✅ *Manual Mode green light* — Cindy QA done, on you — greenlight it today\n• 📊 *Nelson* — metro_area + bucketed_role + matching_roles columns — overdue since Apr 8\n• 🔗 *Manan* — intro Divij ↔ Nelson; send predicted role docs to Divij\n• 📋 *Manan* — send 3LO spec doc to team as pre-read\n• 🎯 *TLWA careers page QA* with Fadi before 50k QR codes go out\n• 📱 *IBK/Izzy mobile TLWA version* — send Jeff's designs\n• 🔍 *Justin* — full Supabase RLS audit — confirm handoff is active"
        }
    },
    {"type": "divider"},

    # Summary
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Today's Scorecard*\n\n6 decisions locked in across 5 meetings. The big 3 you need to close *today*:\n1️⃣ V1 migration call for TLWA award winners (50% of your user base)\n2️⃣ Predictive role scope for launch mailer (yes/no by EOD)\n3️⃣ TLWA brief to Ted (15 days overdue — just send it)\n\nYou're in great shape strategically. Talroo CPA switch is smart, predefined roles approach is clean, and the badge + poster direction is solid. Now it's about closing the open loops before launch week locks everything in. You've got this, Manan! 💪"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot • Apr 17, 2026 • Covering 5 meetings from Apr 16 | Hiring Leads Standup · Jatin/Manan · Jeff/Manan · Talroo Connect · Fadi/Manan"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Debrief — Friday April 17 (6 decisions, 20+ action items)",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK PREVIEW ===\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("Channel: " + CHANNEL_ID + "\n\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            text = block["text"]["text"]
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el["text"] + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("\n=== END PREVIEW ===\n").encode("utf-8", errors="replace"))

def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + SLACK_TOKEN
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("SUCCESS: Message sent to", CHANNEL_ID)
            else:
                print("SLACK ERROR:", body.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("NETWORK ERROR:", e)
        sys.exit(1)

if not SLACK_TOKEN:
    print("SLACK_TOKEN not set — printing preview instead.")
    preview()
    sys.exit(0)

send()
