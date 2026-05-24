#!/usr/bin/env python3
"""
Chief of Staff Daily Summary — Sunday May 25, 2026
Covers: Friday May 22 decisions + Sunday battle plan for the week ahead.
"""
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
            "text": "Sunday Night Debrief — May 24 | Your Week Starts Tomorrow 🎯",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Hope your Sunday is treating you well. No meetings today (as it should be!), but Friday was *packed* — 5 meetings, a ton of decisions locked, and some things I want to make sure are top of mind before the week kicks off. Let's break it all down."
        }
    },
    {"type": "divider"},

    # ── SECTION: Friday's Meetings ──────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Friday May 22 — 5 Meetings, 7 Major Decisions*"
        }
    },

    # Decision 1 — Boost Experiment
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1️⃣  Boost Experiment Design — LOCKED* _(Hiring Leads Standup, 8:30am)_\n\n*Decision:* Target *only companies already syndicated at company level* for the boost-post-job-creation experiment. Purchase allowed for jobs still *'in review'* (not just approved). Two outcome paths: auto-approve → boost fires automatically; job flagged → Michael's team reaches out for corrections or refund.\n\n*Why:* Only 8% of new companies qualify as low/no-risk for auto-syndication — the existing syndicated pool is much larger and gives you a real experiment cohort without changing the full product flow.\n\n*Fraud check timing fix:* Move fraud checks to *during screener fill* (background) to close the timing mismatch where fraud checks only happen after job creation.\n\n*Action — Manan (CRITICAL):* Loop Michael's team in on boost-for-pending-jobs logic *before* engineering starts. Two paths need alignment."
        }
    },
    {"type": "divider"},

    # Decision 2 — Indeed $3/call risk
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2️⃣  Indeed $3/API Call Billing Risk — SURFACED* _(Indeed Boost Spike Sync, 1:00pm)_\n\n*Decision:* Adopt Iszael's *async local polling* + local campaign data storage as the mitigation strategy to minimize API calls.\n\n*Why this matters:* After a customer's monthly ad spend limit, Indeed charges *$3 per API call* — and those charges hit the *customer's credit card directly* (not Homebase). A coding error could result in hundreds of dollars in surprise charges. Example: $100 ad spend + 195 calls = $585 in API costs, $435 out-of-pocket for the customer. This is real liability.\n\n*Still open — Manan (URGENT):* Follow up with your Indeed contact on the *ATS JavaScript plugin exemption* — if plugin users bypass the $3 fee structure entirely, this changes the architecture discussion significantly. Also confirm: (1) analytics requirement — link-out vs pull-in? (2) predictions API — mandatory or optional? (3) sprint planning proceeds Monday with Carlo/Bob/Iszael."
        }
    },
    {"type": "divider"},

    # Decision 3 — Indeed integration placement
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3️⃣  Indeed Integration → Settings > Integrations Page — LOCKED* _(Manan/Cindy, 10:00am)_\n\n*Decision:* Create a dedicated *Settings > Integrations page* for all Indeed functionality (+ Google Calendar integration). Account setup flow: Create employer account → billing disclaimer ('won't run until billing configured') → link to Indeed billing → account settings access.\n\n*Why:* Keeps the UI clean, avoids scattering Indeed features across the product, and gives you a natural home for Google Calendar integration too.\n\n*Status:* Cindy should have prototype EOD Friday — Manan adds Indeed screenshots — walkthrough scheduled for *next week*. Fatih covers design Monday (Cindy OOO May 25+).\n\n*Reference model:* Workable integration (good account creation + auth flow + billing setup upfront)."
        }
    },
    {"type": "divider"},

    # Decision 4 — Deck language
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4️⃣  Deck Language: 'Marketplace' → 'Talent Pool' — LOCKED* _(Manan/Dana 1:1, 9:30am)_\n\n*Decision:* Replace 'marketplace' with *'talent pool'* throughout the strategy deck. Move referral fee specifics out of the main deck body (appendix or cut entirely — too tactical for a high-level doc). Also cut views-to-applicants forecasting from the plan-of-attack slide — it's unrealistic without owning the platform.\n\n*Why:* John's direction. 'Marketplace' is a loaded term internally. 'Talent pool' is the agreed language. The referral fee section came from a brainstorming session, not core strategy — keep the broader referral economy concept (side-hustle recruiters, $50/referral) but lose the specifics.\n\n*Action — Manan:* Update the deck this weekend if you can — it'll be in better shape for any Monday conversations."
        }
    },
    {"type": "divider"},

    # Decision 5 — Engineering lead gap
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5️⃣  Engineering Lead Gap — FLAGGED (Needs Escalation)* _(Manan/Dana 1:1, 9:30am)_\n\n*Situation:* No dedicated tech lead available for your squad. Bob moved to distribution oversight. Andrew is gone. Malcolm is unreliable (still running time clock team despite hiring priority). Sprint execution is failing consistently — clear definitions set but nothing completing. Dana flagged that engineering is not being held to the same standard as product.\n\n*Also flagged:* Jatin is forgetting critical technical requirements despite multiple conversations — Dana raised this directly.\n\n*Unresolved:* Who builds the applicant-to-interview flow? Core team vs applicant flow team — ownership undefined.\n\n*Action — Manan (HIGH):* Escalate engineering lead gap with Ray or Martin this week. This is a structural problem, not a people problem, and it's blocking sprint delivery."
        }
    },
    {"type": "divider"},

    # Decision 6 — Rami experiment
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6️⃣  Rami Marketplace Experiment — Architecture Locked* _(Rami/Manan, 2:00pm)_\n\n*Decision:* Geo matching uses *lat/lng with configurable radius tiers* (5, 10, 25, 50 miles) — NOT commute time (nice-to-have for later). Role normalization uses LLM + *caching for repeated base/bucket roles* to avoid repeated processing at scale. Target: *300 candidates per job posting* across 3 cohorts: 1yr inactive, 2yr inactive, 3yr inactive. Success = *5-10 clicks/applies from 100 contacted* for a given time segment.\n\n*Why:* Tests whether Homebase can reanimate its latent talent pool before building net-new infrastructure. Quick validation signal.\n\n*Gap identified:* V1 companies may only have zip codes (no addresses) — need a location fallback strategy before running the experiment on them.\n\n*Timeline:*\n• Rami delivers tech: *Wednesday May 27*\n• Co-design session: *Thursday May 29, 11am–1pm PT* (target demographics, radius params, success metrics)\n\n*Action — Manan:* Prepare experiment parameter questions for Thursday's co-design."
        }
    },
    {"type": "divider"},

    # Decision 7 — TLWA
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7️⃣  TLWA Campaign — Exceeding Expectations ✅* _(Hiring Leads Standup, 8:30am)_\n\n*Decision/Status:* John Wallman would run the campaign *exactly the same way again*. Focus shifting to documenting reusable components (career pages, zero-state applications, new signup flow) for future campaigns.\n\n*Outstanding:* Matan's comprehensive one-pager was due at 2pm Friday — confirm you received it (or follow up Monday)."
        }
    },
    {"type": "divider"},

    # ── SECTION: Next Week ─────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📆 Your Week Ahead — May 25–31*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Mon May 25 (Memorial Day)*\n• US holiday — teams mostly OOO\n• Sprint planning: Carlo/Bob/Iszael proceeding\n• Boost sales motion: *KICKS OFF TODAY*\n• Cindy: OOO starts"
            },
            {
                "type": "mrkdwn",
                "text": "*Tue May 26*\n• Sprint 2611 begins\n• Fatih: design handoff from Cindy\n• Send consolidated Indeed questions to contact"
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Wed May 27*\n• Rami delivers geo matching + role normalization tech\n• Validate V1 location fallback strategy"
            },
            {
                "type": "mrkdwn",
                "text": "*Thu May 29*\n• *11am–1pm PT:* Co-design session w/ Rami\n• Dana + Fatih in SF (Ted joining)\n• Indeed integration walkthrough — have prototype ready"
            }
        ]
    },
    {"type": "divider"},

    # ── SECTION: Action Items ────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Your Action Items — Priority Order*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*[URGENT — before Monday EOD]*\n• Send consolidated question list to Indeed contact: (1) ATS plugin exemption from $3/call fee? (2) Analytics — link-out or pull-in required? (3) Predictions API — mandatory or optional? (4) Ad spend threshold calculation method\n• Loop Michael's team in on boost-for-pending-jobs logic before engineering starts\n• Confirm Matan delivered TLWA one-pager (was due 2pm Friday)\n• Verify Boost sales motion collateral ready for Monday launch (Matan one-pager + Usman)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*[HIGH — this week]*\n• Build Indeed integration prototype (add Indeed screenshots to Cindy's designs; walkthrough next week)\n• Escalate engineering lead gap with Ray or Martin — structural issue blocking delivery\n• Address Jatin accountability issue (forgetting critical tech requirements)\n• Define applicant-to-interview flow ownership: core team vs applicant flow team\n• Update strategy deck: 'marketplace' → 'talent pool', referral fees section to appendix"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*[PENDING — don't lose track]*\n• Confirm all Cindy design feedback closed before she returns (OOO May 25+)\n• Offsite Jun 6 attendance decision — recommended sessions: talent pool + applicant profiles\n• V1 location data fallback strategy — zip-code-only companies need a geo solution before Rami's experiment runs on them\n• Prepare experiment parameters for Thu May 29 co-design with Rami (target demographics, radius tiers, time-back windows, success metrics)"
        }
    },
    {"type": "divider"},

    # ── FOOTER ───────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💡 The One Thing*\n\nBefore anything else this week: *get those Indeed questions out the door.* The $3/API call risk is live, the ATS plugin exemption question changes your entire architecture calculus, and the sprint planning is already kicking off Monday. Every day without clarity on this is engineering time potentially going in the wrong direction.\n\nYou had a great Friday — lots locked, good strategic clarity. Now it's about execution. You've got this, Manan. 💪"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot | Based on 5 Granola meetings from Fri May 22 | Ran Sun May 24 at midnight UTC"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Sunday Night Debrief — May 24 | Chief of Staff Summary",
    "blocks": blocks
}


def preview():
    print("=" * 70)
    print("CHIEF OF STAFF SUMMARY — PREVIEW (no SLACK_TOKEN in environment)")
    print("=" * 70)
    for blk in blocks:
        if blk["type"] == "header":
            msg = blk["text"]["text"]
        elif blk["type"] == "section":
            msg = blk.get("text", {}).get("text", "")
            if not msg and "fields" in blk:
                msg = " | ".join(f["text"] for f in blk["fields"])
        elif blk["type"] == "context":
            msg = blk["elements"][0]["text"]
        elif blk["type"] == "divider":
            msg = "---"
        else:
            continue
        sys.stdout.buffer.write((msg + "\n").encode("utf-8", errors="replace"))
    print("=" * 70)
    print("To send for real: set SLACK_TOKEN env var and re-run.")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read())
            if body.get("ok"):
                print(f"✅ Message sent successfully to {CHANNEL}!")
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")


if TOKEN:
    send()
else:
    preview()
