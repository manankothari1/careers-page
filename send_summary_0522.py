#!/usr/bin/env python3
"""Daily Chief of Staff summary — Friday May 22, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Friday May 22 — Your Day in Review 🎯",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan — you had a *packed and productive Friday*. Five back-to-back calls, a major risk surfaced and immediately mitigated, a new marketplace experiment locked, and your Indeed integration strategy is crystallizing fast. Here's everything that matters."
        }
    },
    {"type": "divider"},

    # ── DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚡ DECISIONS LOCKED TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Boost Experiment Scope — Syndicated Companies Only*\n*Decision:* The post-job-creation boost experiment will target *only companies already syndicated at the company level* (not all new companies). Boost purchases allowed even for jobs still 'in review.' Two outcome paths: (a) job auto-approves → boost applies automatically; (b) job flagged → Michael's team contacts employer for corrections or issues refund.\n*Why:* Only 8% of new companies qualify as low/no-risk for auto-syndication — too narrow a funnel. Existing syndicated pool gives you a meaningful experiment cohort without product-wide risk.\n*Owner:* Manan + Michael's team"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Fraud Checks Moved Earlier in Job Posting Flow*\n*Decision:* Run background fraud checks *while the user is filling out screener questions* — before job submission — to eliminate the timing mismatch that would delay or block the boost offer.\n*Why:* Right now, fraud checks happen after job creation, which creates a window where you can't surface the boost modal reliably. Moving checks earlier closes that gap.\n*Owner:* Manan to align with Michael's team before engineering picks it up"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Indeed Sponsored Jobs API — MAJOR BILLING RISK IDENTIFIED & MITIGATED*\n*Decision:* API calls are *free only up to the customer's monthly ad spend amount* — every call beyond that costs *$3/call*, charged directly to the customer's credit card. A coding error could expose customers to unexpected charges.\n*Mitigation locked:* Use Iszael's local async polling system to minimize API calls + store campaign data locally to reduce external requests.\n*Open question (urgent):* ATS JavaScript plugin users *may be exempt* from the $3 fee structure. You need to confirm this with Indeed ASAP — it changes the entire cost model.\n*Owner:* Manan to follow up with Indeed"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Indeed Integration Lives in Settings > Integrations Page*\n*Decision:* All Indeed Sponsored Jobs functionality will live on a new dedicated *Settings > Integrations* page (alongside Google Calendar integration). No scattered UI placement.\n*Why:* Workable's model shows this is the clean, expected pattern. Keeps the flow coherent and gives you a natural home for account management, billing setup, and analytics links.\n*Owner:* Cindy (designs EOD today) + Fatih covering Monday"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Sprint Planning Shifts to Monday (Memorial Day adjusted)*\n*Decision:* US Memorial Day Monday — sprint planning rescheduled. Carlo, Bob, and Iszael will proceed with planning for the two defined tracks: (1) post-job-creation boost modal, (2) boost modal visual upgrades.\n*Owner:* Bob to run Monday planning session"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Deck Language: 'Marketplace' → 'Talent Pool'*\n*Decision:* Replace all 'marketplace' terminology in your deck with 'talent pool' per John's direction. Also, the referral fee section (side-hustle recruiters earning $50/referral) is too specific for the high-level deck — move it to a brainstorm appendix but keep exploring the broader referral economy angle with Rami.\n*Owner:* Manan to update deck"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Rami Marketplace Experiment — Locked Scope*\n*Decision:* First experiment targets *300 candidates per job posting*, segmented into three inactive cohorts (1yr, 2yr, 3yr). Geo matching uses lat/lng radius tiers (5, 10, 25, 50 miles). Role normalization uses LLM with caching to avoid repeated processing of identical roles. Target: tech ready by Wednesday, co-design session Thursday 11am-1pm PT.\n*Why:* Validates the core hypothesis before committing full engineering capacity. 5-10 people clicking from 100 contacted = green light for that time-segment.\n*Owner:* Rami (build) + Manan (co-design Thu)"
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ YOUR ACTION ITEMS — Don't Drop These*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🔴 *[URGENT — send today or Monday AM]* Compile and send consolidated question list to your Indeed contact:\n• Are ATS JavaScript plugin users exempt from the $3/call fee structure?\n• Campaign analytics: requirement to pull data in, or just link out to Indeed dashboard?\n• Predictions API: mandatory or optional for v1 compliance?\n• Confirm: monthly ad spend threshold calculation method\n\n🔴 *[Before engineering starts]* Loop in Michael's team on boost-for-pending-jobs logic — get alignment on the two outcome paths before it goes to sprint.\n\n🟡 *[By next week]* Build prototype using Cindy's EOD designs for Indeed walkthrough — add Indeed-side screenshots. This is your ticket to unblocking the integration approval.\n\n🟡 *[Update deck]* Swap 'marketplace' → 'talent pool' throughout. Pull referral fee specifics into an appendix.\n\n🟡 *[Thursday 11am-1pm PT]* Co-design session with Rami: define target demographics, radius + time-back parameters, and core learning objectives for the experiment.\n\n🟡 *[Ongoing]* Flag engineering accountability issue to Jatin or Bob: Jatine is repeatedly forgetting critical technical requirements despite multiple conversations (Dana flagged this as a pattern). Define who owns applicant-to-interview flow: core team or applicant flow team?"
        }
    },
    {"type": "divider"},

    # ── OPEN RISKS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ OPEN RISKS & WATCH ITEMS*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Indeed billing exposure:* $3/API call risk is REAL. Until you confirm the ATS plugin exemption, treat this as a customer-facing financial risk. Iszael's polling solution is good but not a complete fix if exemption doesn't apply.\n• *Engineering lead gap:* No dedicated tech lead for your team. Bob moved to distribution, Andrew gone, Malcolm unreliable (still running time clock team!). Sprint execution is failing. This needs an escalation conversation with Ray or Martin — you can't keep shipping on vibes.\n• *Cindy OOO May 25+:* She's out all next week in BC. All design feedback must close before EOD Friday. Fatih is covering Monday only.\n• *Indeed testing environment:* Production only, $200 credits (~65 API calls). Be deliberate — every test call costs real money.\n• *V1 location data gap:* Rami surfaced that V1 companies may only have zip codes (no real addresses) for geo matching. Need a fallback strategy before the experiment hits those records.\n• *Offsite decision (week of June 6):* Still pending. Talent pool / applicant profiles sessions are your most relevant — consider selective attendance if full week isn't feasible."
        }
    },
    {"type": "divider"},

    # ── CALENDAR ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 WHAT'S COMING*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Mon May 25 — MEMORIAL DAY:* US holiday. Carlo/Bob/Iszael running sprint planning. Boost sales motion kicks off. Cindy OOO starts.\n• *Tue May 26:* Sprint 2611 begins. Fatih design hand-off from Cindy.\n• *Thu May 29, 11am-1pm PT:* Co-design with Rami (experiment parameters)\n• *Thu May 29:* Dana + Fatty in SF (Ted joining)\n• *Next week:* Indeed integration walkthrough — have prototype ready\n• *Week of Jun 6:* Offsite (Due West Fest Jun 5, Manan flying in Jun 6) — attendance decision pending"
        }
    },
    {"type": "divider"},

    # ── HYPE ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏆 QUICK WINS TO CELEBRATE*\n• TLWA campaign is *exceeding expectations* vs QR code scans — John Wallman said he'd run it exactly the same way again. That's a W.\n• Rami is locked in and moving fast — geo matching + role normalization scripts already built. The marketplace experiment is real now.\n• You surfaced and scoped the Indeed $3/call billing risk *before* it shipped. That's the kind of thing that saves customers and the company. Well done."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Have a great weekend, Manan. 🙌 Monday is going to move fast — get that Indeed question list out the door first thing and you'll be set up perfectly for the week."
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Friday May 22 — Chief of Staff Daily Summary",
    "blocks": blocks
}

def preview():
    output = "\n=== SLACK MESSAGE PREVIEW ===\n"
    for b in blocks:
        if b.get("type") == "section":
            txt = b.get("text", {}).get("text", "")
            output += txt + "\n\n"
        elif b.get("type") == "header":
            txt = b.get("text", {}).get("text", "")
            output += f"### {txt} ###\n\n"
        elif b.get("type") == "divider":
            output += "---\n\n"
    output += "=== END PREVIEW ===\n"
    sys.stdout.buffer.write(output.encode("utf-8", errors="replace"))

if not TOKEN:
    print("No SLACK_TOKEN found — printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"Message sent successfully! ts={body.get('ts')}")
    else:
        print(f"Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
