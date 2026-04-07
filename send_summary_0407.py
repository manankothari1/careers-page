#!/usr/bin/env python3
"""
Daily Decision Summary - End of Day Monday, April 6 / Tuesday Apr 7 kickoff
Slack channel: D06E4QMHCNN
"""

import os
import json
import urllib.request
import urllib.error
import sys

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📋 Your End-of-Day Briefing — Monday, April 6",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! No recorded meetings today — which means you've got a clean slate and some catching up to do. Here's your full situational briefing heading into *Tuesday*. You're in a strong position overall, but a few things are at risk of slipping. Let's lock them down. 💪"
        }
    },
    {"type": "divider"},

    # ── SECTION 1: FIRE DRILLS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 CRITICAL — Act First Thing Tuesday*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Homebase Boost SKU kick-off with Chris McIntosh* ← this is the big one\n"
                ">📌 *Decision locked:* $50 price point, ~20 applicants via Tellroo at $0.50 CPC, Indeed Sponsored Jobs in sidebar\n"
                ">⚠️ *Why it's critical:* Billing needs a *3-week lead time* to build the one-time-purchase SKU. Early May launch = billing work must start *this week or you miss the window*\n"
                ">✅ *Action:* Ping Chris McIntosh today. Confirm the SKU is in Bishop's (or billing team's) queue. If not, escalate immediately.\n\n"
                "*2. TLWA / Launch Week Brief → Ted* ← overdue since Wed Apr 2\n"
                ">📌 *Decision locked:* TLWA standalone component, QR bifold (winner page + evergreen door tool), 47,584 company scope, smart default copy, Google Places API for descriptions\n"
                ">⚠️ *Why it's critical:* Small Business Week is May 3–9. Ted is blocked without this brief — he can't allocate time or give feedback if he doesn't have the doc.\n"
                ">✅ *Action:* Send the brief today. Even a draft is better than silence. Don't let perfect block done.\n"
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 2: DECISIONS MADE THIS SPRINT ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decisions Locked This Sprint (Week of Mar 30 – Apr 3)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Here's the full record of what's been decided — these are locked, no need to revisit:\n\n"
                "• *CommandAI → Amplitude Journeys migration* — No new nudges will be built in CommandAI. All future nudge work goes through Amplitude Journeys. _(Apr 3 Hiring Leads Standup)_\n"
                "• *Resume parsing WON'T ship this sprint* — No API contract yet; Jatin owns delivery visibility; Ted gets more runway. _(Apr 2 DS check-in)_\n"
                "• *Divij mentorship* — Schedule a session w/ Ted + Dana. Manan owns scheduling. _(Apr 2 DS check-in)_\n"
                "• *Careers Page → Supabase normalized tables* — base table + lookup tables (not denormalized). Location ranking = hours worked > Google Places ID > website. _(Apr 2 Nelson/Manan)_\n"
                "• *Generic Roles tiering: T0/T1/T2* — job-request-per-location + `is_generic_role` flag + single UX entry point. _(Apr 2 Nelson/Manan)_\n"
                "• *Indeed 3LO UX* — \"View on Indeed\" = secondary (disabled + 1-2hr subtext), email notification when live, graceful fallback if 6+ hours no status, boost panel CTA. _(Apr 2 Jeff/Manan)_\n"
                "• *QR bifold structure* — immediate scan (TLWA winner page) + evergreen on-door talent tool. _(Mar 31 Zeeshan/Manan)_\n"
                "• *LW scraping ownership* — Manan: desc/color/logo/photos | Zee: badge/name/addr | Nelson: roles. _(Mar 31)_\n"
                "• *Logo confidence threshold* — smart preset (initials) below threshold; don't show a bad logo. _(Mar 31)_\n"
                "• *47,584 distinct company scope* — full count, not smaller. _(Mar 31)_\n"
                "• *TLWA Standalone Component* — locked, TLWA badge in hero, apply button animates. _(Apr 1 TLWA sync)_\n"
                "• *Supabase → HB1 migration* — ~2-3 weeks; Google Places API for descriptions; smart default copy. _(Apr 1 TLWA sync)_\n"
                "• *Homebase Boost pricing* — $50 / ~20 applicants locked. Tellroo $0.50 CPC. _(Mar 30)_\n"
                "• *Indeed 3LO* — Andrew leads, approved, build starts. _(Mar 30)_\n"
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 3: YOUR ACTION ITEM LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📝 Your Full Action Item List — Prioritized*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 — Today (before EOD Tuesday):*\n"
                "☐ Ping Chris McIntosh → confirm Boost SKU is in billing queue\n"
                "☐ Send TLWA/LW brief to Ted (overdue 5 days)\n"
                "☐ Green-light Manual Mode (Cindy's QA is done — it's on you)\n\n"
                "*P1 — Tuesday in your 1:1s / standup:*\n"
                "☐ Sync with Fadi on sprint concerns (Ray + Dana flagged issues — Fadi should know before standup)\n"
                "☐ Review Jeff's Indeed 3LO prototype → send to team + add acceptance criteria\n"
                "☐ Review Matan's 3 prototypes + topical workplace prototype\n"
                "☐ Andrew: review 3LO spike → email Kenneth → add Ray to thread\n\n"
                "*P2 — This week:*\n"
                "☐ Write generic roles proposal doc (2 options + recommendation: location-mapping approach)\n"
                "☐ Build Supabase tables + run 60k upsert; Nelson to validate\n"
                "☐ Schedule Ted + Dana Divij mentorship session\n"
                "☐ Confirm Iszael has resolved ~8,000 missing TLWA addresses\n"
                "☐ Confirm Fadi's 4 TLWA badge design variations shared with Jeff\n"
                "☐ Decide scraping approach for photos/logos (Claude scraper vs Google Places vs 3rd party) — *currently blocking eng*\n"
                "☐ Applicant flow brief + prototype — overdue since Mar 25 — needs a date or descope decision\n"
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 4: SPRINT HEALTH ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Sprint Health Check*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *TLWA / LW Campaign* — On track architecturally; brief + scraping approach = the two open blockers\n"
                "• *Homebase Boost* — Pricing locked, Jeff's UI not started yet (⚠️ blocker for Early May)\n"
                "• *Indeed 3LO* — Andrew leads, approved; redirect URI limits from Indeed still needed\n"
                "• *Resume Parsing* — Intentionally delayed. Jatin owns visibility. ✅ intentional decision\n"
                "• *Manual Mode* — QA done. One click to ship. Don't let this stall.\n"
                "• *Careers Page / Supabase* — Architecture decided (normalized), migration 2-3 weeks out\n"
                "• *Applicant Flow* — No brief, no prototype. Oldest overdue item (Mar 25). Needs attention or explicit descope.\n\n"
                "_North stars: 600 paying cos → 2,600 H1 | 112 weekly trials → 1k | Retention 87% → 95%_"
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
                "_You're running a tight ship, Manan. The decisions this sprint have been sharp — "
                "you've de-risked the DS timeline, locked the Boost price, and gotten 3LO approved. "
                "The main thing standing between you and a great week is getting the Boost SKU into billing's queue and sending that TLWA brief. "
                "Do those two things first tomorrow and everything else flows. You've got this. 🚀_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "📋 End-of-Day Monday, April 6 — Decisions, Actions & Sprint Health",
    "blocks": blocks
}

def send_slack_message(token, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    return result

if not SLACK_TOKEN:
    print("=" * 70)
    print("SLACK_TOKEN not set — PREVIEW MODE (message not sent)")
    print("=" * 70)
    print()
    print("To: D06E4QMHCNN")
    print()
    # Print a readable version of the blocks
    for block in blocks:
        if block.get("type") == "header":
            print(f"\n{'=' * 60}")
            print(block["text"]["text"])
            print('=' * 60)
        elif block.get("type") == "section" and "text" in block:
            print()
            print(block["text"]["text"])
        elif block.get("type") == "divider":
            print("-" * 60)
    print()
    print("Add SLACK_TOKEN to Cursor Secrets to enable live delivery.")
    sys.exit(0)

result = send_slack_message(SLACK_TOKEN, payload)

if result.get("ok"):
    print(f"✅ Message sent successfully to {CHANNEL_ID}")
    print(f"   Timestamp: {result.get('ts')}")
else:
    print(f"❌ Slack API error: {result.get('error')}")
    print(f"   Full response: {json.dumps(result, indent=2)}")
    sys.exit(1)
