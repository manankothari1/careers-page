#!/usr/bin/env python3
"""Daily Decision Summary - April 10, 2026"""

import os
import json
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📋 Your Daily Decision Summary — Friday, April 10",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Hope the in-office day was a good one — here's everything you decided and committed to today. You're moving fast and doing the right things. Let's close this week strong. 💪"
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔐 Incident Retro: #INC-372 — Exposed Supabase API Keys*\n_2:00 PM · With Minh Nghiem, Ali Firooz (Security)_"
        }
    },

    # CONTEXT
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*What happened:*\nA security researcher responsibly disclosed that a Supabase public API key (from Ray's first Supabase project) was committed to GitHub with misconfigured Row-Level Security (RLS). This allowed unauthenticated users to query ~25,000 job posting records for ~3 months. The data exposed was *already publicly available* (job descriptions, compensation, role details) — no PII, no sensitive data."
        }
    },

    # DECISIONS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decisions You Made / Locked:*\n\n*1. Architecture change: frontend public key → backend private key*\n_Rationale:_ Instead of just fixing the RLS and rotating the public key, you took the bigger, right call — moved to a private key stored securely in Vercel, serving data from the backend. The Supabase public key is no longer needed or exposed.\n\n*2. Supabase audit → Justin leads (not you)*\n_Rationale:_ You have launch week commitments you can't deprioritize. Justin Nazari is the right person with the context and availability. You explicitly advocated for this and removed your own name.\n\n*3. Incident severity → support downgrade to Medium (not High)*\n_Rationale:_ Ali proposed this, you aligned. No PII, no sensitive data, publicly available info — the \"High\" classification was driven by the 3-month detection gap, but the actual customer impact was near-zero. Medium is accurate and defensible.\n\n*4. No PR review requirement for non-technical builders*\n_Rationale:_ You pushed back on mandatory code review for non-eng builders, correctly noting that a reviewer won't know what they're looking at anyway. The real fix is education + tooling (Semgrep, env var guidelines), not process overhead."
        }
    },

    # WHAT'S ALREADY DONE
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Already Resolved (you or team acted on this):*\n• RLS policy fixed — unauthenticated requests now blocked ✓\n• Exposed API key revoked and rotated ✓\n• Private key stored in Vercel env vars (project-scoped, not global) ✓\n• All new Homebase repos now auto-enrolled in Semgrep secret scanning ✓\n• Vercel storage verified during call (you showed Ali) ✓"
        }
    },

    # ACTION ITEMS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Your Action Items from Today:*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Minh + Manan sync on remediation approach* — Ali flagged he wasn't fully up to speed on how you changed the architecture; Minh will follow up with you directly. *Get this scheduled early next week.*\n\n• *Investigate: Can RLS be enabled by default for all new Supabase projects?* — You started looking during the call, found only MFA system-wide. This is a follow-up you took on. Loop in Justin or Minh.\n\n• *Confirm Justin Nazari leads the full Supabase audit* — Minh is reaching out to Justin (and possibly Sammy). *Confirm handoff happened and that Justin has what he needs.*\n\n• *Minh to update retro doc* with private key storage details + your architectural changes — you don't need to do this, but verify it gets done so it can be shared with Andrea's team."
        }
    },

    # DELEGATION ITEMS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🤝 Delegated / Others Own:*\n• *Justin (or Sammy Nazari):* Full audit of all Supabase projects for RLS misconfigurations\n• *Security team (Andrea):* Build \"secure Supabase development\" guideline for non-technical/AI-assisted builders\n• *Minh:* Update retro doc, share with channel + Andrea's team\n• *Security team:* Explore whether default RLS enforcement is possible org-wide"
        }
    },

    {"type": "divider"},

    # CARRY-FORWARD CRITICAL
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Carry-Forward Critical Items (Pre-Weekend Check):*\n\n• *TLWA Launch Week brief to Ted* — NOW 8 DAYS OVERDUE. This is the most important thing you have not done. If it doesn't go out today, it needs to go out first thing Monday.\n• *Homebase Boost SKU with Chris McIntosh* — Billing lead time is closing. If you haven't kicked this off, the Early May window is at risk.\n• *Manual Mode green light* — Cindy QA is done. You just need to say go. Do it.\n• *Andrew's answer on company-level vs. location-level Indeed connection* — Needed before Monday grooming. Chase this before EOD.\n• *Nelson's deliverables* — `metro_area` + `bucketed_role` + `matching_roles` columns were due Apr 8. Where are they?\n• *Generic roles proposal doc* — Still unwritten. Two options, your recommendation. Blocking grooming.\n• *Jeff's 3LO prototype* — Review + send to team + write acceptance criteria before Monday."
        }
    },

    {"type": "divider"},

    # WEEK IN REVIEW
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Week in Review (Apr 7–10):*\n\nThis was a real execution week. You locked the Indeed 3LO architecture (phase 1 scoped, failure handling defined, auth entry points set, token refresh owned by Andrew). You handled a security incident quickly and correctly — moved the architecture in the right direction instead of just patching it. The Supabase audit is properly delegated. You've been in the office making things happen.\n\nThe one thing that keeps showing up: *the TLWA brief to Ted is overdue and it's the most visible deliverable you have right now.* Everything else is in motion. That one needs you to sit down and write it."
        }
    },

    {"type": "divider"},

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_Have a great weekend, Manan. You're building something real. Monday is going to be big — grooming, Boost, 3LO. Come back sharp._ 🚀"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Daily Summary · Apr 10, 2026 · 1 meeting reviewed (Incident Retro #INC-372)"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Daily Decision Summary — Friday, April 10 | Incident Retro #INC-372 + Week in Review",
    "blocks": blocks
}

if not SLACK_TOKEN:
    print("⚠️  SLACK_TOKEN not set — printing preview instead.\n")
    print(json.dumps(payload, indent=2))
    print("\n--- PREVIEW END ---")
    raise SystemExit(0)

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
        body = json.loads(resp.read().decode("utf-8"))
        if body.get("ok"):
            print(f"✅ Slack message sent successfully! ts={body.get('ts')}")
        else:
            print(f"❌ Slack API error: {body.get('error')}")
            print(json.dumps(body, indent=2))
            raise SystemExit(1)
except urllib.error.HTTPError as e:
    print(f"❌ HTTP error: {e.code} {e.reason}")
    raise SystemExit(1)
except urllib.error.URLError as e:
    print(f"❌ URL error: {e.reason}")
    raise SystemExit(1)
