#!/usr/bin/env python3
"""Daily Decision Summary — Apr 14, 2026 (covering Apr 13 meetings)"""

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
            "text": "🌟 Daily Decision Debrief — Monday, Apr 14",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan — you had a *strong* day Monday. Four meetings, multiple locked decisions, and real progress on TLWA. Here's everything you decided, why it matters, and what needs to happen next."
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 of 4 — Hiring Leads Standup* (8:30 AM)\n_Fadi, Dana, Matan, Jatin, Ray, Nelson, Jeff_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 1: TLWA fallback banner = brand-color-to-white gradient*\n> *Why:* Avoids generic \"techy AI\" vibe that alienates small businesses. Cohesive with each company's brand. Softer/neutral look fits the audience.\n> *Action:* Jeff + design team deliver 3 illustrative examples this week. _(Owner: Jeff/Matan, Due: this week)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 2: Generic Role = high priority, ships BEFORE predicted role*\n> *Why:* Predicted role is nice-to-have for LW; generic role is the foundation. Screener questions + static JD approach approved.\n> *Action (critical):* Jatin gives Malcolm timeline estimate for careers page completion *by EOD today*. You then set up the generic role planning meeting immediately after. _(Owner: Jatin → you, Due: Today)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 3: Predicted role = fast-follow (3 days post-launch), not a blocker*\n> *Why:* Data is ready (Nelson + David, minor tweaks needed). FE is ahead of schedule with 3 weeks of polish time. Pushing to post-LW avoids scope creep.\n> *Carry-forward:* Monitor closely — if FE stays ahead, you may be able to pull it in."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ Open Item: OEM Award Email Campaign*\n> Kayla + Matan are building the email flow for OEMs who win awards → direct to careers page.\n> *Action:* Follow up on Kayla's message from last week. This touches lifecycle + TLWA — don't let it slip. _(Owner: You, Due: Today)_"
        }
    },
    {"type": "divider"},

    # ── MEETING 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 2 of 4 — Justin / Manan 1:1* (9:30 AM)\n_Justin Nazari_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 4: Scrap hallucinated company descriptions — re-run with real website context*\n> *Why:* Previous batch made up descriptions from company names/URLs only. No actual site content was used. Results looked real but were 100% fabricated — shipping fake descriptions to 50k QR recipients is a major trust/brand risk.\n> *What's happening:* New pipeline retrieved missing websites for ~39k of 40k+ companies. Re-running batches 93-100 (~8k companies) with homepage/about/careers content as context.\n> *Action:* Justin downloads remaining batch results when complete. You validate a sample before this goes to Supabase. _(Owner: Justin → you for QA, Due: ASAP — this is a LW blocker)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 5: Gradient banner fallback for companies without logos*\n> Stripe-style gradient (less bold/solid) with company colors. Will complete the full dataset: descriptions + logos + images + hex colors.\n> *Why:* Ensures every one of the 50k QR recipients lands on a polished page, even for companies with no brand assets."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 Bonus Unlock: Signal Scout / Data Genie Agent*\n> Justin built a new analyst agent connected to Databricks (Claude-managed, MCP, cloud code execution, returns downloadable files).\n> *Opportunity:* Replace your current manual Databricks query loop with natural-language analysis. This could 10x your data velocity for Boost targeting, applicant health, etc.\n> *Action:* Explore integrating Homebase schema/analytics glossary into the agent. Schedule a follow-up with Justin when LW pressure eases. _(Owner: You + Justin, Due: Post-LW)_"
        }
    },
    {"type": "divider"},

    # ── MEETING 3 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 3 of 4 — Manan / Liza: Learning Activities Demo* (3:00 PM)\n_Liza Fontana, Justin Nazari, Cassidy Edwards_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 6: Liza's Lovable + Supabase learning toolkit = worth investing in*\n> *Why:* She's built a full modular training system (flip cards, drag-drop sequencing, trivia, persona matching, chat-with-customer scenarios) inside Rippling as a free LMS — avoiding an $80k dedicated LMS cost. Justin helped with the Supabase backend. Real impact on sales + CS enablement.\n> *Your direction:* Build an admin dashboard (user-level + training-level analytics/scores). Move actual training into Lovable environment; use Rippling only as launch pad + certification layer.\n> *Action:* Liza will explore dashboard implementation. You offered to brainstorm further — optional but high-leverage. _(Owner: Liza, you as advisor)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎤 Opportunity: Present at Master Your Craft session*\n> Liza invited you to present on AI/vibe coding at a future session. Next 3 are booked (Claude skills, Vibe coding, Systems thinking).\n> *Rationale:* High visibility, aligns with your builder culture push. Consider it once LW is behind you."
        }
    },
    {"type": "divider"},

    # ── MEETING 4 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 4 of 4 — TLWA Design Review* (6:47 PM)\n_Manan solo / design decisions_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 7: Dynamic QR landing page — logo fallback = hide placeholder entirely*\n> *Why:* Initial placeholder approach (company initials on colored background) looked too generic and incomplete. Better UX to show nothing than a fake logo.\n> *System:* 4-layer dynamic page — Photos (scraped or gradient), Logo (real or hidden), Description (scraped or default), Colors (scraped hex or #0B3F7E default)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 8: Gradient = bottom-up (not left-right)*\n> *Why:* Left-right gradient looked like a progress bar. Bottom-up creates better visual flow and draws the eye upward toward the CTA."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decision 9: Jeff builds mobile version showing dynamic business example*\n> *Action:* Jeff → mobile designs → tags you in final file → meets IBK + Izzy tomorrow morning for implementation alignment.\n> *Action (yours):* Send IBK/Izzy the mobile version of TLWA demonstrating dynamic functionality. _(Owner: Jeff for designs → you for distribution, Due: Tomorrow morning before Jeff's IBK/Izzy meeting)_"
        }
    },
    {"type": "divider"},

    # ── MASTER ACTION CHECKLIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 YOUR MASTER ACTION LIST — Apr 14*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 P0 — Do These First*\n• *TLWA brief to Ted* — NOW 12 DAYS OVERDUE. Send it. This is your #1 blocker.\n• *Homebase Boost SKU kick-off with Chris McIntosh* — Billing window is closing. Do not let another day pass.\n• *Manual Mode green light* — Cindy's QA is done. This is on you. Greenlight it today.\n• *Andrew: company-level vs location-level Indeed answer* — Grooming is this week. You need this resolved NOW."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟠 P1 — Today*\n• *Jatin → Malcolm timeline estimate (careers page)* — By EOD today, then you schedule generic role planning meeting.\n• *Follow up on Kayla's LCM/OEM award email message* — Don't let this fall through the cracks.\n• *Jeff: confirm mobile TLWA designs + tag you in file* — You need to send to IBK/Izzy before their morning meeting.\n• *Validate a sample of Justin's re-run company descriptions* — Before anything goes to Supabase or QR recipients."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟡 P2 — This Week*\n• *Nelson: metro_area + bucketed_role + matching_roles columns* — Overdue since Apr 8. Chase this.\n• *Supabase tables + 60k upsert* — Build it; send Nelson UI branch screenshot.\n• *Jeff Indeed 3LO prototype* — Review + send to team + add ACs before grooming.\n• *TLWA pipeline QA with Fadi* — Before 50k QR codes go out.\n• *Minh + Manan: Supabase remediation sync* — From INC-372 retro.\n• *Justin: full Supabase RLS audit* — Confirm handoff is active."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Scoreboard*\n> ARR: *$650K* (+44% since January) 🔥\n> GTM OS ML: *70%* of top 250 converted in 7 days\n> Lifecycle: *46%* team app upgrades influenced\n> Taru feed: *~300 → ~1,100 jobs* (CPC caps + biz-type filter removed)\n> TLWA: *50,000 QR recipients* — LW is close"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You're shipping meaningful product at an incredible clip. The dynamic TLWA page is going to blow people away. Keep the TLWA brief to Ted and the Boost SKU as your north stars tomorrow — everything else follows. Let's go! 💪"
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Daily Decision Debrief — Apr 14: 4 meetings, 9 decisions locked (TLWA QR design, generic role priority, company descriptions re-run, Liza LMS, Signal Scout agent). P0: TLWA brief (12 days overdue!), Boost SKU, Manual Mode greenlight.",
    "blocks": blocks
}

if not SLACK_TOKEN:
    print("=" * 70)
    print("PREVIEW MODE (no SLACK_TOKEN found)")
    print("=" * 70)
    print(json.dumps(payload, indent=2))
    print("\nTo send for real: set SLACK_TOKEN environment variable")
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
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"✅ Slack message sent successfully! ts={result.get('ts')}")
    else:
        print(f"❌ Slack API error: {result.get('error')}")
        print(json.dumps(result, indent=2))
        raise SystemExit(1)
except urllib.error.URLError as e:
    print(f"❌ Network error: {e}")
    raise SystemExit(1)
