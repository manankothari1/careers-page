#!/usr/bin/env python3
"""Daily decision summary - Sunday Apr 12, 2026 (No meetings today — Monday kickoff briefing)"""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌅 Sunday Wind-Down + Monday Battle Plan — Apr 12",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! No new meetings today — you earned that Sunday. But tomorrow is a BIG week with *Launch Week* on the horizon, so let's make sure you walk in Monday fully loaded. Here's your complete situation report. 💪"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 CRITICAL — Must Do Monday Morning (These Are On Fire)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. TLWA Launch Week Brief → Ted*\n*Status: 10 DAYS OVERDUE* 🔴\nThis is your single highest-leverage action. Ted needs context before the 50k QR codes go out. You know the brief cold — Taru expansion, auto-customized careers pages, Job Get integration, Boost pricing. Block 30 minutes, write it, send it. Monday. First thing.\n_→ Action: Draft & send brief to Ted before standup_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Homebase Boost SKU Kick-off with Chris McIntosh*\n*Status: CRITICAL — billing window closing* 🔴\nEarly May target requires the billing team to have ~3 weeks. You are now inside that window. The pricing is locked ($50 one-time via Taru), the CPC model is solid ($0.50 per applicant), and the old SKUs ($79 Craigslist, $199 ZipRecruiter) are being deprecated. Chris just needs the kick-off to start the billing config.\n_→ Action: Ping Chris today or first thing Monday — \"ready to kick off Boost SKU\"_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Green-Light Manual Mode*\n*Status: Waiting only on you* 🟡\nCindy finished QA. The feature is done. There is zero reason this is still pending — it's just sitting in your inbox waiting for a ✅. Free for everyone (confirmed publicly to CS already). Just say go.\n_→ Action: Send Cindy the green light before standup_"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Monday Grooming Prep — Unblock These Before the Session*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Andrew: Company-Level vs Location-Level Indeed Connection*\nThis is the last open question from the 3LO design review (Apr 9). Andrew was supposed to get an answer from the Indeed team before this grooming. If you haven't heard back, ping him *now* — this is a grooming blocker.\n_→ Action: Confirm Andrew got the answer; if not, escalate or make the call yourself (company-level is the safer default)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Jeff's Indeed 3LO Prototype*\nNeed to review, send to the team, and add acceptance criteria before Monday grooming. Don't let grooming start without this in hand.\n_→ Action: Review Jeff's prototype + add ACs today or first thing Monday_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Generic Roles Proposal Doc*\nTwo options need to be documented and a recommendation made (location-mapping approach is your lean). This feeds directly into grooming scope decisions.\n_→ Action: Write both options + rec in a doc; share before grooming_"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🗂️ Locked Decisions This Week — For the Record*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here's your full decision ledger from the week of Apr 7–11:\n\n*Monday Apr 7 (no meetings):* Carry-forward critical: TLWA brief, Boost SKU, Manual Mode, Jeff 3LO, generic roles doc, Fadi sync\n\n*Tue Apr 8 — Nelson/Manan 1:1:*\n• Applicant health reframed as *absolute delta* (~4k additional apps needed for \"healthy\")\n• Tellroo scaling to nearly all jobs ✅\n• Job recommendation carousel green-lit (even 1 job shown is fine) ✅\n• Architecture: Databricks → Supabase pipeline for job-match data ✅\n• Role bucketing: one-degree approach (not exact match) ✅\n\n*Wed Apr 9 — Indeed 3LO Design Review:*\n• View live job post status = *must-have* for TLWA LW ✅\n• Sponsored jobs redirect = nice-to-have stretch\n• Failure handling: internalize; 2hr delay, 12hr internal escalation, never surface to OEM ✅\n• 3 auth entry points (to-do / boost / job page) ✅\n• Token: 1hr access / 60-day refresh; Andrew owns refresh mechanism ✅\n• Plaid-style in-app modal confirmed ✅\n• *OPEN: company-level vs location-level connection*\n\n*Thu Apr 10 — Incident Retro #INC-372:*\n• Architecture upgraded: private key in Vercel (not just RLS fix) ✅\n• Justin Nazari leads Supabase audit (Manan delegated due to LW) ✅\n• Severity: downgraded to *Medium* (no PII, no sensitive data) ✅\n• No mandatory PR review for non-technical builders → education + tooling is the fix ✅\n\n*Fri Apr 11 — Sprint Show & Tell + Hiring Team Check-in:*\n• S&T format stays; optimize by asking audience if meeting is needed ✅\n• Meeting attendance = your call — skip if there's no value for you ✅\n• Taru feed expanded from *300 → 1,100 jobs* (CPC caps + biz-type filter removed) ✅\n• Homebase Boost at $50 via Taru *locked and confirmed to full team* ✅\n• Manual V2 = free for everyone — *confirmed publicly to CS* ✅\n• Job Get integration *shipping this week* ✅\n• TLWA careers pages auto-customized per business (logo/photos/colors/desc) ✅\n• Indeed job visibility issue → 3LO + escalate to Indeed rep via Michael H ✅\n• GTM OS ML model: 70% of top 250 converted within 7 days (use for Boost day-1 targeting) ✅\n• Lifecycle = 46% team app upgrades 📊\n• AI Context Repo for Analytics now live — get access ✅"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⏳ Outstanding / Overdue Items — Full Tracker*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "These are carried across multiple days and still need resolution:\n\n🔴 *TLWA brief → Ted* — 10 days overdue\n🔴 *Boost SKU kick-off → Chris* — billing window closing NOW\n🟡 *Manual Mode green light* — Cindy done, waiting on Manan\n🟡 *Andrew: company-level vs location-level Indeed answer* — needed before grooming\n🟡 *Jeff 3LO prototype review + ACs* — needed before grooming\n🟡 *Generic roles proposal doc* — write both options, recommend location-mapping\n🟡 *Supabase tables (base + lookup) + 60k upsert* — Manan to build, Nelson validates\n🟡 *Nelson: metro_area + bucketed_role + matching_roles columns* — overdue since Apr 8\n🟡 *Nelson: absolute applicant-delta analysis* — overdue since Apr 8\n🟡 *Nelson UI branch screenshot → send to Nelson; wire up carousel once data ready*\n🟡 *Schedule Ted + Dana: Divij mentorship session*\n🟡 *Review Matan's 3 prototypes + topical workplace prototype*\n🟡 *Applicant flow brief + prototype* — overdue since Mar 25; needs date or descope decision\n🟡 *Michael H: share specific job ID w/ Indeed search invisibility → escalate to Indeed rep*\n🟡 *Minh + Manan: Supabase remediation sync (INC-372)*\n🟡 *Justin Nazari: confirm Supabase RLS audit handoff*\n🟡 *Minh: update INC-372 retro doc with Vercel/private key storage details*\n🟡 *Security team: investigate default RLS for all new Supabase projects*\n🟡 *TLWA careers page pipeline: QA with Fadi before QR codes go out*\n🟡 *Taru spend: monitor CPC performance as volume goes 300 → 1,100*\n🟡 *Zuara/Sales: align on migrating free Craigslist boosts → $50 Homebase Boost once live*\n🟡 *Jatin: resume scoring discussion with Fadi + Aman (was Tue)*\n🟡 *Get access to AI context repository (GitHub)*\n🟡 *Kayla: align on TLWA-specific lifecycle sequences using dispatch email builder*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Key Insight to Keep Front of Mind*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "> *First-day app velocity = #1 predictor of job health.*\n> Healthy jobs average 13 apps on Day 1 (median 9). Jobs with 1–2 apps on Day 1 almost never recover.\n> *This is why Boost on Day 1 matters more than Day 3.* GTM OS ML data confirms 70% of top 250 convert within 7 days — use this to sharpen day-1 Boost targeting for the new SKU."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Your Monday Priority Stack (in order)*\n\n1️⃣ Send TLWA brief to Ted ← do this before anything else\n2️⃣ Green-light Manual Mode → ping Cindy\n3️⃣ Ping Chris McIntosh on Boost SKU kick-off\n4️⃣ Confirm Andrew's 3LO answer for grooming\n5️⃣ Review Jeff's prototype + add ACs\n6️⃣ Draft generic roles proposal doc\n7️⃣ Build Supabase tables + 60k upsert\n8️⃣ Chase Nelson on overdue columns + delta analysis"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You've had a massive week Manan — 12 decisions locked, Taru expanded 4x, Boost pricing confirmed to the whole team, INC-372 resolved cleanly, and Manual Mode is done. You're in great shape going into Launch Week. Now just clear those three 🔴 items Monday morning and you're set. Let's get it! 🚀"
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Sunday Wind-Down + Monday Battle Plan — Apr 12",
    "blocks": blocks
}

if not SLACK_TOKEN:
    print("=== PREVIEW (no SLACK_TOKEN found) ===")
    print(json.dumps(payload, indent=2))
    print("\nTo send for real, add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets")
else:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SLACK_TOKEN}"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"✅ Message sent successfully! ts={result.get('ts')}")
            else:
                print(f"❌ Slack API error: {result.get('error')}")
                print(json.dumps(result, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
