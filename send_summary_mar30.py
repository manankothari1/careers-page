#!/usr/bin/env python3
"""
Mar 30 2026 — Monday Hackathon Kick-off Summary
No Granola calls recorded today; synthesizing from accumulated context.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from daily_summary import send_slack_message

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🚀 Monday Wrap-Up · March 30, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Happy Hackathon Kick-off Monday, Manan! 🎉 No meeting recordings captured today, so here's your full battle-briefing built from everything we know — decisions, ownership, and what *must* move this week."
        }
    },
    {"type": "divider"},

    # --- HACKATHON ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏕️ HACKATHON — Week 1 of 2 (Applicant Flow)*\n*Decision:* Full team locked in on applicant flow overhaul for the next 2 weeks, kicked off today.\n*Why:* Applicant flow is the biggest friction point between a job seeker applying and a manager acting — fixing it directly attacks your weekly-trials and retention north stars.\n*Owner:* Manan (PM lead), full squad\n\n*Action Items:*\n• ✅ Confirm all 4 project brief docs are complete and shared with the team *today*\n• Align on daily standups / demo cadence for the 2-week sprint\n• Keep an eye on scope creep — 2 weeks is short; ruthlessly cut anything not core to applicant UX"
        }
    },
    {"type": "divider"},

    # --- BOOST SKU (CRITICAL / OVERDUE) ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 CRITICAL: Manan Boost SKU Kick-off with Chris*\n*Decision (from last week):* Boost SKU launch targeting Early May.\n*Why it's urgent:* Billing needs a *3-week lead time* — that window is closing fast. Every day of delay risks the May launch date.\n*Owner:* Manan + Chris\n\n*Action Items:*\n• 🚨 Schedule kick-off with Chris *this week* if not already done\n• Confirm billing team is looped in and timeline is locked\n• Define pricing: Homebase Boost via Tellru at $30–$50 (eat cost for new customer acquisition)"
        }
    },
    {"type": "divider"},

    # --- INDEED OAUTH ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔗 Indeed OAuth (3LO)*\n*Decision:* Design → Build → Indeed Review → Launch. Two entry points: *View Live Job Posts* + *Boost with Indeed*.\n*Why:* Indeed is aggressively cutting organic reach (3rd partner lost last week) — owning the OAuth relationship protects distribution.\n*Owner:* Andrew (spike), Manan (review + Kenneth email)\n\n*Action Items:*\n• Review Andrew's 3LO spike\n• Email Kenneth at Indeed to maintain relationship\n• Add Ray to the Indeed thread\n• Confirm the 'View Live Job Posts' and 'Boost with Indeed' entry point designs are in motion"
        }
    },
    {"type": "divider"},

    # --- TLWA / QR ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📱 TLWA — Top Local Workplace Award QR Flow*\n*Decision (Mar 25):* Option C confirmed — 4-step QR flow (Scan → Reveal → Activate → Next Steps). Phone/SMS auth. Generic Team Member job post default. Build outside HB1 for speed. 50k unique QR codes at `app.jhb.com/tlwa/[unique-string]`.\n*Why:* Speed to market before the physical printer deadline; SMS prevents QR hijacking.\n*Owner:* Ray + Jatin (URL/QR), Fadi (UX + marketing insert), Kvan (Top Local Workplace PM)\n\n*Action Items (from Friday — check status):*\n• ✅ Confirm Jatin delivered URL routing + QR code structure (was due Fri)\n• ✅ Confirm Ray delivered Friday deck + target segment\n• Fadi: Marketing meeting for insert content — status?\n• Ray + Matan: Lifecycle marketing + Salesforce planning — in motion?"
        }
    },
    {"type": "divider"},

    # --- SMART PRESETS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚙️ Smart PreSets*\n*Decision (Mar 25):* 4-tier preset framework (zero → category → specific → full scrape). Logo identified as highest-ROI MVP element. Smart placeholder UX (dotted-line, Dropbox pattern).\n*Owner:* Manan + Jeff (preset specs Tiers 1–4), Fadi (post-QR scan UX), Manan (logo scraping → Supabase)\n\n*Action Items:*\n• Define preset specs for Tiers 1–4 with Jeff\n• Move logo scraping tool from local → Supabase (Claude ranking integration)\n• Debrief from Friday's in-person QR prototype user testing — what did Dana + Ray find?"
        }
    },
    {"type": "divider"},

    # --- MANUAL MODE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟡 Manual Mode — Waiting on You*\n*Decision:* Cindy's QA is complete. Green light is on Manan.\n*Why it matters:* This is blocking a shipped feature from reaching users.\n*Action Items:*\n• 🟡 Review QA results and give the green light (or flag issues) — ideally *today*"
        }
    },
    {"type": "divider"},

    # --- APPLICANT FLOW BRIEF ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Applicant Flow Brief + Prototype*\n*Status:* Was due EOD Wed Mar 25 — status unknown.\n*Action Items:*\n• Confirm this is done and shared; if not, unblock it *today* since the hackathon just started"
        }
    },
    {"type": "divider"},

    # --- JOBGET ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🤝 JobGet Partnership*\n*Decision (Mar 24):* Organic XML feed first, Easy Apply preferred, sponsored after.\n*Action Items:*\n• Confirm organic XML feed integration is in the backlog and owned"
        }
    },
    {"type": "divider"},

    # --- NORTH STARS SCOREBOARD ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 North Star Scoreboard (as of last known)*\n| Metric | Current | Target |\n|---|---|---|\n| Paying companies | ~600 | 2,600 (H1) |\n| Weekly trials | 112 | ~1,000 |\n| Monthly retention | 87% | 95% |\n\nThe hackathon applicant flow work directly attacks *weekly trials* and *retention* — keep that lens on everything you build."
        }
    },
    {"type": "divider"},

    # --- UPCOMING MILESTONES ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🗓️ Coming Up*\n• *Apr 15* — New Toronto sales manager starts (prep onboarding context)\n• *Early May* — Manan Boost SKU launch (billing clock is ticking 🕐)"
        }
    },
    {"type": "divider"},

    # --- BOTTOM LINE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚡ Bottom Line for Today*\nYou're juggling a lot and crushing it. The three things that *cannot slip* this week:\n1. 🚨 Boost SKU kick-off with Chris (billing lead time)\n2. 🟡 Manual Mode green light (Cindy is waiting on you)\n3. 🏕️ Hackathon briefs confirmed + team aligned\n\nYou've got this. Go make it happen! 💪"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff Summary · Mon Mar 30, 2026 · No new Granola recordings today — synthesized from accumulated context_"
            }
        ]
    }
]

fallback = "🚀 Monday Wrap-Up · Mar 30, 2026 — Hackathon Kick-off + Decision Summary"
send_slack_message(blocks, fallback)
