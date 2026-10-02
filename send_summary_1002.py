#!/usr/bin/env python3
"""Chief of Staff daily digest — Oct 1, 2026 (PDT). Fires at midnight UTC = 5pm PDT."""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN") or ""

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Brief — Thu Oct 1, 2026 ✈️",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Day Grade: A-* | 2 meetings captured | LAST DAY BEFORE SPAIN (3pm flight)\n*Theme: JD VALIDATION LOCKED · FRAUD PRIORITY SHIFTED · OT→HIRING MODAL SET · PRE-SPAIN SPRINT*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🚨 *PRE-SPAIN CRITICAL ALERTS — BEFORE YOUR 3PM FLIGHT*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• 🔴 *OMNI ACCESS* — Looker goes DARK today (Oct 2). File IT help desk ticket *RIGHT NOW* if you haven't. This is the last window.\n• 🔴 *EarnIn email to John* — NDA + docs + positioning. Committed Sep 30. Still unsent? 5 minutes. Do it.\n• 🟡 *3-Year Vision One-Pager* — Due before board meeting (~Oct 15). First draft was supposed to be before Spain. Can you get 30 min on the plane?\n• 🟡 *OKR Draft* — Was due EOD Sep 29. Did it reach Fadi? Confirm before you board.\n• 🟡 *Carlo KT* — He's on paternity leave Oct–Feb. What has been handed off? The clock is ticking.\n• 🟡 *Skye's OKR MD file* — She committed to sending you SQL context. Follow up if it hasn't landed."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "📅 *MEETING 1 of 2: Skye / Manan 1:1 — 9:15 AM PDT*\n_<https://notes.granola.ai/d/597ee6cd-5a6f-49fd-9025-5ce2f066a1c3|View Granola Notes>_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏆 DECISION 1: FRAUD PRIORITY SHIFT — Job-level checks FIRST*\n*What:* Company-level fraud checks are performing better than assumed. Shift engineering focus to job-level (JD content) checks.\n*Why:* 62% of company-flagged posts get syndicated after review — they're mostly legit. Only 1.3% of flagged posts are actually fraud. The biggest *actual* problem is contact info in job descriptions, affecting paying HB customers 91% of the time. Job-level checks have fewer data science / data platform dependencies and ship faster.\n*Action → Manan:* Confirm with Jatin what JD-level checks are possible without DS/data platform. If green, tell Ted to move Divij to company-level checks and proceed down the priority list."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 DECISION 2: 8 FRAUD ACCOUNTS WITH LIVE POSTS — BUG CONFIRMED*\n*What:* 8 suspected-fraud accounts had 72 posts go live, collecting ~2,500 applications. 3 are *still active right now*. 91% of applications came *after* the fraud decision was made.\n*Why it matters:* These accounts are skewing your hiring success metrics. Posts going live on or after the fraud decision date = clear bug in the review enforcement logic.\n*Action → Skye:* Share full writeup (company IDs, Salesforce cases) with Manan + Jatin.\n*Action → Manan:* Investigate + manually close the 3 still-active accounts ASAP."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🐛 DECISION 3: FIX THE JOB EDIT BLOCK DURING REVIEW*\n*What:* Customers whose jobs are flagged for contact info in the description cannot edit while under review. They're trapped.\n*Why:* We email them to fix it, but the edit flow is blocked. They can't comply even if they want to. This is a conversion killer and a trust destroyer for paying customers.\n*Action:* Assign owner + ship fix. This unblocks legitimate paying customers caught in the review trap."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⭐ DECISION 4: TOP MATCH VISIBILITY = HIGH PRIORITY*\n*What:* Elevate Top Match visibility near the top of the Q4 stack rank.\n*Why:* Two compounding benefits — satisfies OEM curiosity about *why* someone is a top match, AND reduces dependency on high applicant volume by building per-candidate confidence. This is a retention and quality win.\n*Open question:* How to represent match reasoning — score, badges, or composite signals (resume fit, screener performance, HB track record)?\n*Action → Design:* Session with Vaddy to map the universe of signals.\n*Important nuance on screener audio:* Manan spoke with Caitlin about compliance — retention requirements, disclosure of audio use, ADA accommodations for users who can't speak. Safe harbor options: screener not required to be a top match, OR text fallback alternative."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🛑 DECISION 5: TALENT POOL Q4 STANCE CONFIRMED — STAY DEPRIORITIZED*\n*What:* No change from last week. Talent pool remains off the Q4 roadmap as a core investment.\n*Why:* Product experience leakage means adding more top-of-funnel supply won't move outcomes. 1-2 extra applications per role from the talent pool is not yet differentiating. Q4 holiday seasonality = natural dip = ideal time for controlled side-of-desk experiments, not a push.\n*Key open design questions still unresolved:* What data to collect from talent pool members, how to surface them distinctly to OEMs (not just more undifferentiated volume), when to re-engage across employers.\n*Action:* Continue side-of-desk experiments only. No DS commitment until Q1.\n*Also flagged:* Divij re-ping on talent pool notebook (job request ID input needed) remains outstanding."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔍 WATCH ITEM: Sep 7 Anomaly — High-Risk Rate Dropped ~⅔*\n*What:* Something changed around September 7 — high-risk flag rate fell dramatically, posts started going live faster.\n*Action:* Investigate what was pushed or changed on that date. Could be a fix that worked too well, or a regression that widened a fraud gap."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "📅 *MEETING 2 of 2: Intent Signals — Manan + Fadi — 1:00 PM PDT*\n_<https://notes.granola.ai/d/372809ad-5cea-45fd-ac04-4308b5bf0455|View Granola Notes>_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 DECISION 6: JD FRONT-END VALIDATION DESIGN LOCKED*\n*What:* Inline highlight + hover card is the chosen UX pattern. Sticky banner shows 'Fix 3 errors' with count. 'Remove' button animates up from highlight on hover. Triangle hit area prevents accidental dismiss. Save-and-exit allowed while errors present. Re-validation triggers on next 'Continue.' Success state shown after all resolved.\n*Root cause confirmed:* Contact info (email, phone, website) in JD body = why jobs get stuck in review. NOT a company-level syndication problem. Confirmed to affect paying HB customers.\n*Editor:* Lexical (not React Quill — that's legacy compat code only). Lexical natively supports custom text node highlighting. Red highlight styling = new but straightforward.\n*Copy:* 'Partner job boards reject jobs that have an email, phone number, or website in their job description.'\n*Scope:* Job creation AND edit flows. Manually added jobs too (not just AI-generated).\n*Ship velocity:* Jatin said shippable in a few hours. Orca already building the PR.\n*Actions:*\n  → Iszael: Add rollout flag to PR before merging. Share Loom of test. Release to APDD channel.\n  → Manan: Finalize inline validation spec in Linear (confirm edit-job + manually-added jobs in scope; remove auto-snap / silent-remove notes from MD)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 DECISION 7: OT→HIRING MODAL DIRECTION LOCKED*\n*What:* Cost comparison modal bridges the overtime alert to a job post CTA. Right-side layout selected (table retained). H1: 'Save $218 every pay period.' Chart/table below for specificity. Disclaimer required: 'figures are illustrative estimates.'\n*Why the modal:* Direct CTA to job post felt too abrupt. The modal gives the OEM a concrete cost-comparison (OT cost = hours × wage × 1.5 vs. new hire cost = hours × base wage) to justify the decision.\n*Surfaces in scope:* (1) Payroll details page — alert/CTA below OT cost line item, (2) Payroll dashboard — two cards with blue gradient, (3) Earnings tab — inline info-style alert below the table (not row insertion).\n*Generated via Claude/Orca* from FigJam sketch. Two variants were reviewed; right variant won for table parsability.\n*Action → Fadi:* Finalize designs across all three surfaces."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📦 DECISION 8: 'NO INDEED APPLICANTS BY DAY 3' FRAUD SIGNAL — READY TO SHIP*\n*What:* Signal is built, tested by Iszael, excludes the scooters CSV list.\n*Why it matters:* Proactive fraud detection signal embedded in job posting flow.\n*Actions:*\n  → Iszael: Share Loom walkthrough, add rollout flag, post to APDD hiring channel.\n  → Manan: No action needed — just approve when you see it."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 STRATEGIC INSIGHT: The Bottleneck Has Shifted*\n*What:* With Orca, engineering effort is now cheap. The scarce resource is now *PM/design thinking* — taste, intuition, and problem framing.\n*Implication:* The old model of de-risking before building (because building was expensive) is obsolete. Manan is now explicitly pushing engineers to own approach decisions. PM role = priorities + quality bar, not work breakdown.\n*Why this matters for Spain:* You're the constraint now. Every hour in transit is an hour of PM bandwidth offline. The team needs clear priorities set before you board."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🗺️ DECISION 9: FTUE — HOLD THE LINE*\n*What:* No change to FTUE stance. Dashboard outperformed all FTUE variants tested (empty state, screenshot, video, split screen). Need new data before revisiting.\n*Context:* Fadi is skeptical of Skye's FTUE initiative based on prior experiment results.\n*Action → Manan:* Bridge Fadi and Skye. Share any new data with both before any FTUE work is scoped."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "📋 *CONSOLIDATED ACTION ITEMS — OCT 1*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 URGENT (before 3pm flight today):*\n• File IT ticket for *Omni access* — Looker goes dark Oct 2 (TODAY)\n• Send *EarnIn email to John* — NDA + docs + positioning (committed Sep 30, still open)\n• Confirm *OKR draft* reached Fadi (was due Sep 29)\n• Confirm *Carlo KT* is in progress — what has been handed off?\n\n*🟡 MANAN — due this sprint:*\n• Confirm with Jatin what JD-level checks are possible without DS/data platform → decide Divij's assignment\n• Investigate 3 still-active fraud accounts (once Skye sends writeup)\n• Finalize inline validation spec in Linear (scope confirmation + cleanup)\n• Design session with Vaddy on Top Match signal universe\n• Build Q4 roadmap visual (sequencing + sprint-fit check — not a commitment doc)\n• Bridge Fadi + Skye on FTUE (share new data first)\n• Introduce yourself to Matt McAllister (CMO — Day 5 today)\n• Have Divij fact-check Skye's fraud data analysis (2-3 hour sanity check)\n\n*👥 OWNED BY OTHERS (Manan to track):*\n• Iszael: Rollout flag + Loom + APDD post for both (1) JD validation PR and (2) Day-3 fraud signal\n• Fadi: Finalize OT→Hiring modal designs (3 surfaces)\n• Skye: Send fraud writeup (8 accounts) to Manan + Jatin; send OKR SQL context as MD file\n• Jatin: Confirm JD-level check capability scoping"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🔴 *WATCH LIST ITEMS STILL OPEN (carry-forward)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Indeed Feed Suspended* — Day 39. Fraud evidence package with Jessica Kanaskie. Awaiting 2-3 week review window.\n• *Facebook API down* — Day 8. Meta developer checkup expired. Bob + IBK leading. No ETA.\n• *Indeed Easy Apply PDF* — Was due Sep 30. Status UNKNOWN. Confirm before boarding.\n• *3-Year Vision One-Pager* — Due ~Oct 15 (board). First draft by Spain?\n• *Reply to John Waldman on EarnBetter* — Propose paid CPC test (~100 jobs, $0.07-0.10 CPC, $2K budget).\n• *Ryan Reilly $50 gift card* — Was due Mon Sep 28. ryan.reilly@liveyourheritage.com\n• *Lola Erickson $50 gift card* — Promised on Sep 28 call. lola.e.erickson@gmail.com\n• *Matan job title/salary data* — Texted Sep 24. Still not sent. mzion@joinhomebase.com\n• *Marina / Mundo Academy* — 19+ days late. marina@mundoacademy.com. Under 5 minutes.\n• *IBK JD A/B signal* — 3+ weeks overdue. Pull before V2 widens.\n• *DEPARTURES SIGNAL DOCS* — 30+ days overdue. Conflict docs → Zane, Sean, Jon W, Bobby."
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "🤖 Chief of Staff digest auto-generated from Granola notes | Oct 1, 2026 | You've got this, Manan — have a great trip to Spain. Just knock out that Omni ticket first. ✈️🇪🇸"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Brief — Thu Oct 1, 2026 | Day Grade A- | JD VALIDATION LOCKED · FRAUD PRIORITY SHIFTED · LAST DAY BEFORE SPAIN",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK DIGEST PREVIEW (no token) ===\nChannel: " + CHANNEL + "\n\n").encode("utf-8", errors="replace"))
    for b in blocks:
        if b.get("type") == "section" and "text" in b:
            sys.stdout.buffer.write((b["text"].get("text", "") + "\n\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "header":
            sys.stdout.buffer.write(("### " + b["text"].get("text", "") + "\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif b.get("type") == "context":
            for el in b.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")

if not TOKEN:
    preview()
    print("\nINFO: No Slack token found. Add SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN secret in Cursor Dashboard (Cloud Agents > Secrets) to enable live delivery.")
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + TOKEN},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print("Slack message sent successfully! ts=" + str(result.get("ts")))
    else:
        print("Slack API error: " + str(result.get("error")))
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print("Network error: " + str(e))
    preview()
    sys.exit(1)
