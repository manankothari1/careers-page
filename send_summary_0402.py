#!/usr/bin/env python3
"""Daily decision summary for Manan - April 2, 2026 (covering April 1 meetings)."""
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
            "text": "🌟 Your Daily Decision Briefing — April 1, 2026",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! You had a productive day with *2 key meetings*. Here's everything you decided, why it matters, and what needs to happen next. You're moving fast — let's make sure nothing slips through the cracks. 💪",
        },
    },
    {"type": "divider"},
    # ── MEETING 1 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 of 2: TLWA <> Career Pages Sync* (2:00 PM)\n_With: Fadi, Iszael (IBK), Jeff, Gbolade_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*1. Standalone custom component (not reusing existing careers page)*\n> *Why:* The TLWA use case is unique enough that bolt-on reuse would create tech debt and constrain the design. Clean slate = faster iteration for the hackathon.\n\n*2. TLWA award badge as default hero image (replacing business photo)*\n> *Why:* Celebrates the award recipients and differentiates the page. Fadi has 4 design variations ready to share with Jeff.\n\n*3. Apply button stays — but animates instead of opening a real form*\n> *Why:* Removing the apply button would raise red flags with businesses wondering if the page can actually receive applicants. Animation keeps the UX believable without requiring a real pipeline yet.\n\n*4. Font style selector (Classic/Modern/Friendly) = demo only, does not persist*\n> *Why:* Shows customization capability for the demo without needing to actually configure/store it. Smart scope decision.\n\n*5. Google Places API (NOT geocode API) for company descriptions*\n> *Why:* Homebase has historically conflated these two — Places is the right one for business descriptions. You're scraping + storing in Supabase, then migrating to Homebase One in ~2–3 weeks.\n\n*6. Smart default copy when no description available*\n> *Why:* ~8K companies missing addresses, unknown % missing descriptions. Default: \"[Name] is a [industry] business\" keeps the page looking polished for every recipient.\n\n*7. Jobs display logic: General Application as default, custom role as stretch*\n> *Why:* Keeps it simple for the base case while leaving room to delight with contextually relevant roles (e.g. \"Barista\" for a café). Implementation: check for existence of custom role value — no explicit flag needed.",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Your Action Items (Manan):*\n• `IN PROGRESS` Scrape company descriptions via *Google Places API* → load into Supabase\n• `COORDINATE` Pin down *Supabase → Homebase One* migration timeline (~2–3 weeks) with Iszael & Andrew\n• `DEFINE` Write smart default copy template for missing company descriptions\n• `WATCH` Track % of TLWA companies with custom roles available — determines viability of the stretch goal (Nelson's role normalization work feeds into this)",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔁 Delegated Actions (track these):*\n• *Fadi* → Share 4 design variations (with/without photo, with/without TLWA badge) with Jeff + prototype apply button animation + source font files\n• *Iszael (IBK)* → Build career page as standalone component + sync with Andrew on data endpoint structure + resolve ~8,000 missing addresses\n• *Jeff* → Confirm font format needed from Fadi",
        },
    },
    {"type": "divider"},
    # ── MEETING 2 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 2 of 2: Manan/Dana 1:1* (4:00 PM)\n_With: Dana Lobo_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*1. Homebase Boost pricing locked at $50*\n> *Why:* Expected CPA of $2.50–$3.50 = 15–20 applicants per boost. This isn't a revenue play — it subsidizes applicant flow where only ~10% of jobs currently get healthy applicants. ZipRecruiter ($199 for 13 applicants = $16/applicant) and Craigslist ($79 for ~4 applicants) comparisons make $50 look like outstanding value.\n\n*2. Boost mechanism: adds job to Tellroo feed at $0.50 CPC, runs until budget depletes*\n> *Why:* Clean, simple mechanism. OEMs don't need to understand the plumbing — they just see more applicants.\n\n*3. Sponsored Jobs API (Indeed) = future workstream — NOT surfaced to billing yet*\n> *Why:* Keeping it out of the billing channel avoids confusion with the current one-time purchase work. You'll handle this as a sidebar with Chris McIntosh instead. Smart sequencing.\n\n*4. You're taking over billing coordination on the hiring/applicant flow side*\n> *Why:* Dana remains billing's single POC for their build, but once that's done, you own the handoff. Clean separation of concerns.\n\n*5. Jeff hasn't designed the boost flow yet — copy needs a full rework*\n> *Why:* \"Get up to 8x more quality candidates\" flagged as weak. This needs to be crisp before launch.",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Your Action Items (Manan):*\n• `OWN` Brief billing team on *Homebase Boost requirements* — take over applicant flow coordination once Dana's handoff is done\n• `SIDEBAR` Schedule chat with *Chris McIntosh* to flag Sponsored Jobs API (Indeed) as a future workstream — keep it OUT of the billing channel for now\n• `COLLAB` Work with *Jeff* on redesigning the boost flow UI and copy (\"8x more quality candidates\" is weak — needs a rewrite)\n• `CONFIRM` Check with billing (Bishop?) that the *one-time purchase SKU for Homebase Boost* is actively in progress",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔁 Delegated Actions (track these):*\n• *Dana* → Remain POC with billing team for their build + send outstanding gift cards to interviewees\n• *Jeff* → Design the boost flow UI (hasn't started yet — this is a blocker for launch)",
        },
    },
    {"type": "divider"},
    # ── SUMMARY SNAPSHOT ──────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Day-at-a-Glance*\n\n| | |\n|---|---|\n| Total meetings | 2 |\n| Decisions made | 12 |\n| Your action items | 8 |\n| Items you delegated | 7 |\n| Blockers identified | 2 (Jeff's boost UI design; missing address/description data) |",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Top 3 Things to Do Tomorrow:*\n1. *Sidebar with Chris McIntosh* — flag Indeed Sponsored Jobs API so it doesn't get buried\n2. *Check Jeff's boost UI design status* — this is on the critical path for Homebase Boost launch\n3. *Confirm billing (Bishop) has the one-time purchase SKU in flight* — don't let this stall quietly",
        },
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Generated by your Chief of Staff automation | April 2, 2026 | Based on Granola notes from April 1 | _You're crushing it, Manan_ 🚀",
            }
        ],
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Your Daily Decision Briefing — April 1, 2026",
    "blocks": blocks,
}

if not SLACK_TOKEN:
    print("⚠️  SLACK_TOKEN not set — printing preview instead:\n")
    print(json.dumps(payload, indent=2))
    print("\n--- PREVIEW COMPLETE (message NOT sent) ---")
else:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
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
