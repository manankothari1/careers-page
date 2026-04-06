#!/usr/bin/env python3
"""Daily Chief of Staff Summary - Monday April 6, 2026"""

import json
import os
import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Good morning, Manan! ☀️ Monday Apr 6 — Chief of Staff Briefing",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "No new calls logged today yet — so I went back through *last week's sessions* to surface everything you decided, everything still open, and exactly what you need to attack today. You had a *seriously productive week* — here's what locked, what's overdue, and how to win this Monday.",
        },
    },
    {"type": "divider"},
    # ── LOCKED DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔒 LOCKED DECISIONS — Week of Mar 30 – Apr 3*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. CommandAI → Amplitude Journeys (Apr 3 — Hiring Leads Standup)*\n"
                "> No new nudges will be created in CommandAI. All future nudges go into Amplitude Journeys, which the team will pressure-test next week with new release nudges.\n"
                "> _Why:_ CommandAI sunsets end of April; Amplitude Journeys is easier for engagement tracking.\n"
                "> *Owner:* Matan Chen Zion — share prototypes + create nudges in Amplitude by end of this week."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Resume Parsing WON'T Ship This Sprint (Apr 2 — Data Science Check-In)*\n"
                "> No API contract between data science and engineering exists yet. Engineering can't build the endpoint this sprint.\n"
                "> _Why:_ Sprint planning happened before API requirements were defined — classic sequencing miss. Jatin now owns delivery visibility across all engineering workstreams (DS, FE, BE).\n"
                "> *Owner:* Jatin → drive the API contract convo between Divij + engineering. Ted → align on Divij mentorship Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Divij Mentorship Plan Activated (Apr 2 — Data Science Check-In)*\n"
                "> Gap identified: Divij executes well once directed but doesn't proactively surface blockers or contribute to direction. Classic example: spent 1.5 weeks manually reformatting markdown instead of flagging the prompt issue.\n"
                "> _Why:_ Ted is now explicitly on the hook to mentor Divij. Dana's framing (broadly agreed): this is a team-wide communication gap, not a Divij problem.\n"
                "> *Owner:* Manan → schedule Ted + Dana + Divij mentorship session this week."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Supabase Careers Page Architecture Locked (Apr 2 — Nelson / Manan)*\n"
                "> Normalized table structure confirmed: base table (location ID, company ID, owner email) + separate lookup tables for address, business category, Google Places ID. Upsert by location/company ID.\n"
                "> Location ranking locked: *hours worked > Google Places ID present > company website present.*\n"
                "> Generic roles tiering: T0 = 'Team Member' | T1 = 'Team Member' + Nelson's predicted role | T2 = 'Team Member' + active roster role.\n"
                "> _Why:_ Normalized structure prevents data loss on upstream updates; hours-worked proxy is the best signal for primary location.\n"
                "> *Owner:* Manan → build tables + upsert ~60k rows. Nelson → validate upsert approach."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Indeed 3LO Full UX Spec Locked (Apr 2 — Jeff / Manan)*\n"
                "> • 'View on Indeed' = *disabled immediately after posting* + subtext 'typically viewable within 1–2 hours'\n"
                "> • Once live: *email notification* sent with direct link (no manual checking)\n"
                "> • Stuck >6 hours: *graceful proactive comms* — 'we're contacting Indeed on your behalf'\n"
                "> • Indeed treated as *secondary* (not primary) action — 'Live' is the signal, Indeed is a curiosity check\n"
                "> • New to-dos: 'View job on Indeed' (top of list, before boost) + 'Boost on Indeed'\n"
                "> • Boost panel + subscription page: add Indeed connect option alongside Craigslist/Preparer\n"
                "> _Why:_ Avoids false anxiety, sets accurate expectations, doesn't over-elevate one job board.\n"
                "> *Owner:* Manan → prototype full flow (disabled, pending, email, error states) + add acceptance criteria. Jeff → divergent design directions."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. TLWA Launch Week Data Science Scope Defined (Apr 2 — Data Science Check-In)*\n"
                "> Pre-populate careers pages with 1–3 ready-to-activate jobs: (1) General application, (2) Predicted role from Nelson's model based on biz type.\n"
                "> Divij's involvement: generate JDs + screener questions for predicted roles.\n"
                "> _Why:_ Most TLWA winners (~50k) have never posted a job — need warm content to drive conversion.\n"
                "> *Owner:* Manan → send Launch Week brief to Ted (THIS IS OVERDUE — was due Apr 2 EOD)."
            ),
        },
    },
    {"type": "divider"},
    # ── TODAY'S PRIORITIES ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 YOUR PRIORITIES TODAY — MONDAY APR 6*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🔴 OVERDUE — Must Do First Thing*\n\n"
                "1. *Send TLWA / Launch Week brief → Ted Naseri*\n"
                "   Was due Apr 2 EOD. Ted is waiting to review over the long weekend — he's already behind. Send it now.\n\n"
                "2. *Kick off Homebase Boost SKU with Chris McIntosh*\n"
                "   Billing needs a 3-week lead for Early May launch. If you don't start today, you miss the window. Ping Chris NOW.\n\n"
                "3. *Applicant flow brief + prototype*\n"
                "   Overdue since Mar 25. Either commit to a date this week or make the explicit call to descope. Leaving it in limbo is the worst option."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🟡 HIGH PRIORITY — Today or Tomorrow*\n\n"
                "4. *Sync with Fadi on sprint concerns from Ray + Dana*\n"
                "   Do this before your squad standup. Ray and Dana feel nothing has changed — Fadi needs context so he can address this with the team credibly.\n\n"
                "5. *Green-light Manual Mode*\n"
                "   Cindy's QA is done. This is sitting on you. Unblock it.\n\n"
                "6. *Review Jeff's Indeed 3LO prototype + send to team*\n"
                "   Jeff shared designs. Review, add acceptance criteria (Indeed to-do = top of list), and ship it to the broader team today.\n\n"
                "7. *Schedule Ted + Dana + Divij mentorship session*\n"
                "   Ted is ready to lean in. Block 30-45 min this week."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🟢 THIS WEEK (No Procrastinating)*\n\n"
                "8. *Build Supabase tables + upsert ~60k rows*\n"
                "   Nelson is waiting to validate. Get the base + lookup tables live so he can test the sync.\n\n"
                "9. *Write Generic Roles proposal doc*\n"
                "   Two options, your recommendation = location-mapping approach. Nelson needs this before you sync on it.\n\n"
                "10. *Andrew 3LO spike → review + email Kenneth + add Ray*\n"
                "    Andrew's spike should be done or nearly done. Close the loop.\n\n"
                "11. *Review Matan's 3 prototypes + topical workplace prototype*\n"
                "    He shared them Friday. Give him feedback this week — he's been waiting on you.\n\n"
                "12. *Confirm ~8,000 missing TLWA addresses status with Iszael*\n"
                "    He said he was resolving it — confirm it's done."
            ),
        },
    },
    {"type": "divider"},
    # ── SPRINT HEALTH ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 SPRINT HEALTH CHECK*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Carrying over from last sprint:* Show the Work, Auto-scheduling, Manual Mode — nothing new has started on these\n"
                "• *Resume parsing:* Not shipping this sprint (no API contract)\n"
                "• *Ray + Dana morale signal:* 'Nothing feels like it changed' — Fadi sync is urgent\n"
                "• *CommandAI sunset:* End of April deadline — team has <4 weeks to fully migrate nudges to Amplitude\n"
                "• *Big May milestone:* Small Business Week (May 3-9) + TLWA live — Homebase Boost SKU must start billing setup THIS WEEK"
            ),
        },
    },
    {"type": "divider"},
    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*You made a ton of great calls last week, Manan* — the Indeed UX spec alone is the kind of crisp decision-making that unblocks teams for weeks. The architecture decisions with Nelson are solid. Now it's about *execution*: get that TLWA brief out the door, ping Chris on Boost, and let Fadi know what's coming in standup.\n\n"
                "This week has all the ingredients for a massive sprint. Let's go. 💪"
            ),
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot • Monday Apr 6, 2026 • Based on Apr 2–3 Granola sessions",
            }
        ],
    },
]

payload = {
    "channel": SLACK_CHANNEL,
    "blocks": blocks,
    "text": "Monday Apr 6 Chief of Staff Briefing — decisions, actions, and how to win this week.",
}

if not SLACK_TOKEN:
    print("=== PREVIEW MODE (no SLACK_TOKEN) ===")
    print(json.dumps(payload, indent=2))
    print("\n=== MESSAGE TEXT PREVIEW ===")
    for block in blocks:
        if block["type"] == "header":
            print(f"\n{'='*60}")
            print(f"HEADER: {block['text']['text']}")
            print('='*60)
        elif block["type"] == "section":
            text = block["text"]["text"]
            # strip mrkdwn markers for readability
            print(text.replace("*", "").replace(">", "  ").replace("_", ""))
            print()
        elif block["type"] == "divider":
            print("-" * 60)
    raise SystemExit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SLACK_TOKEN}",
    },
    method="POST",
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
