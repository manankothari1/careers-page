#!/usr/bin/env python3
"""Daily chief-of-staff digest for Manan Kothari — Sep 21, 2026 (Return from Yosemite + Exec Review Day)."""

import json
import os
import sys
import urllib.request
import urllib.error

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
            "text": "Chief of Staff Daily Digest — Monday, Sep 21 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":tada: *WELCOME BACK FROM YOSEMITE, MANAN!* :mountain_snow:\n"
                "Grade: *A* | Theme: *GROUND RUNNING — ZIPRECRUITER ROOT CAUSE CRACKED · Q4 OKR FRAMEWORK CRYSTALIZED · TALENT POOL PATH CLARIFIED · OPERATING MODEL REBUILT · ORCA GOES WIDE*\n\n"
                "You hit the ground HARD today. 4 meetings, massive strategic clarity across talent pool legals, Q4 framework, a 5x ZipRecruiter surge demystified, and a brand new AI-native engineering motion opening to the whole org. First full day back as Senior PM — and you absolutely earned that title today."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Today's Meetings (4)*\n"
                    "9:00 AM — Hiring Week in Review _(Jatin, Ankit, Martin, Jan, Jon W, Skye)_\n"
                    "10:45 AM — Tiger / Manan _(1:1 on Claude + Amplitude workflow)_\n"
                    "11:00 AM — :briefcase: Hiring Half-Baked Demos _(Full team + Skye)_\n"
                    "3:52 PM — Skye / Manan _(1:1: Q4 OKRs, Talent Pool, ZipRecruiter deep dive)_"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:white_check_mark: KEY DECISIONS MADE TODAY*\n\n"
                "*1. Monday WIR is DEAD — New operating cadence incoming*\n"
                "Low attendance, low value. Replacing with bi-weekly sprint kickoff (every other Monday). New sprint-end show-and-tell for hiring team specifically (Jon W, Bobby, Sean, support). Jatin drafts new cadence by *Thu Sep 24* with launch *Mon Sep 28*. Skye also reducing standup frequency.\n"
                "_Why it matters: the current format was a relic of chaos-mode. You're in a different era now._\n\n"
                "*2. ZipRecruiter 5x Surge — ROOT CAUSE FOUND*\n"
                "ZipRecruiter applicants went from ~1,945/week (Jul 13) to ~11,500/week — share jumped from 10% to ~40% of total applicants. Root cause: a `job_id_zip_code` payload bug (invalid for ZR) causing silent submission failures — fixed Jul 30. Likely an AI-generated PR with zero monitoring.\n"
                "_Why it matters: this is a GOOD problem. More applicant volume. But you need to understand feed quality now — reach out to your ZR contact._\n\n"
                "*3. Talent Pool Data Strategy — Legal Path Clarified*\n"
                "Three segments with different risk profiles: (a) Past HB employees = cleanest path — rich data, defensible ToS; (b) Job board applicants (Indeed/ZR) = need explicit opt-in due to ATS partner agreements; (c) HB app users = covered under HB ToS, which supersedes job board restrictions. Opt-in UX framed as 'we found 3 jobs in your area' beats generic consent ask. Job closure timing matters — don't redirect candidates until employer is done.\n"
                "_Why it matters: this unblocks the talent pool roadmap. Start with ex-employees, get the legal framework right, then expand._\n\n"
                "*4. Q4 OKR Framework Crystallized (with Skye)*\n"
                "Top-line metric: *paying locations* (currently 857). Two core levers: trial conversion (declining 3-4 months!) + retention/churn. Updated job health threshold: *20 applicants + 2 touches by Day 14* (beats the old 20+5 by Day 5 on fill rate AND conversion). Full metric stack: paying locations → trial conversion → retention/churn → role fill rate → Signal Scout → job health. Sales comp should incentivize retention, not just paid conversion.\n"
                "_Why it matters: you're finally naming the real enemy — declining trial conversion. Now build to solve it._\n\n"
                "*5. Delivery vs. Capability Gap — Framed Correctly*\n"
                "Can't know if a capability gap exists until delivery issues are resolved first. Signal Scout complaints are partly delivery failures. Job-go-live SLA flagged as the metric to instrument — but only for approved/legitimate companies (fraud detection creates invisible false positives). First step: separate 'pending syndication' from 'flagged/fraudulent' in the roadmap.\n"
                "_Why it matters: this is the right philosophical frame. Fix delivery, then see what's left._\n\n"
                "*6. OTP Early Results Reviewed — Paying Customer Exemption Raised*\n"
                "53 companies enrolled; 98% sailed through (already had 2-step). Only 8 hit the OTP modal: 4 completed, 4 didn't. Of non-completers: 1 confirmed fraud, 1 paying TMAP customer being blocked (!), 2 ambiguous. Open question: should paying customers be exempt from OTP friction? Validate with Laura.\n"
                "_Why it matters: blocking a paying customer with fraud friction is a churn risk. Answer this fast._\n\n"
                "*7. Comms Assistant — Production Decision Needed THIS WEEK*\n"
                "Malcolm's LLM-generated screener SMS, nudges, reminders, and Q&A replies are live on staging. Handles out-of-scope questions gracefully. Jatin wants a go/no-go decision this week. Future Q4 prioritization still TBD.\n"
                "_Why it matters: it's ready. Decide._\n\n"
                "*8. Orca (fka Orchestrate) — Opening to Full EPDD*\n"
                "Orchestrator (Carlo, OpenSpec-based) now has 5 invocation sources via Orca (Gbolade): Slack form, Granola transcript → Linear, Paper (Fadi), Linear comment @straight tag, Slack modal. Target: 70-100 tickets pushed through before claiming confidence. Exploring Jev for deterministic layer. Demo format changing next few weeks.\n"
                "_Why it matters: this could be the most leverage-multiplying thing your team builds in Q4._\n\n"
                "*9. AI Hiring Compliance — Q4 Priority*\n"
                "5 states in scope: California, NYC, Illinois, Connecticut, Colorado (+ Canada likely). Requirements: 4-year data retention + candidate disclosure when AI used. Homebase relatively protected (no auto-disqualification), but ranking/recommendations still create exposure. Jatin to add Skye to compliance thread. Employment Counsel review before building anything.\n"
                "_Why it matters: getting caught later = PR disaster + legal exposure. Do this right._\n\n"
                "*10. Linear 'Done' ≠ 'Shipped' — Hygiene Fix Incoming*\n"
                "Talent pool auto-poster announced the feature as live when Malcolm accidentally set status to 'Done' — feature is NOT in production. Fix: add a separate 'Released' stage in Linear so the auto-poster only fires on actual production deploys."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:zap: YOUR ACTION ITEMS (Manan-owned, due ASAP)*\n\n"
                ":red_circle: *Add roadmap line item: separate 'pending syndication' from 'flagged/fraudulent' jobs*\n"
                "  → Enables clean job-go-live SLA metric. Do this before the next sprint planning.\n\n"
                ":red_circle: *Reach out to ZipRecruiter contact*\n"
                "  → Understand what's driving the 5x surge: feed quality scoring, traffic shifts from Indeed, or both.\n\n"
                ":red_circle: *Cross-reference OTP paying customer exemption with Laura*\n"
                "  → Validate the logic: should TMAP paying customers bypass 2FA entirely?\n\n"
                ":red_circle: *Re-ping Divij — unblock talent pool notebook*\n"
                "  → Needs job request ID input added. Blocking manual outreach emails.\n\n"
                ":red_circle: *Decide on Comms Assistant production release*\n"
                "  → Jatin needs a decision this week. It's on staging. What's the hold-up?\n\n"
                ":yellow_circle: *Try Amplitude MCP workflow on OTP project*\n"
                "  → Replicate Tiger's approach: feed ticket, dupe dashboard, let Claude verify.\n\n"
                ":yellow_circle: *Kick off talent pool consent thread (employee segment first)*\n"
                "  → You said you'd do this Sep 18 — now Day 3 overdue. Loop in Matan.\n\n"
                ":yellow_circle: *Intent signals proposal review*\n"
                "  → Fadi is drafting for Gabe (Payroll PM) + Alexis. You said you'd review today and prep the deck. Do it tonight or first thing tomorrow."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:rotating_light: OVERDUE / CRITICAL WATCH LIST*\n\n"
                ":sos: *DAVID (Indeed Product) INTRO — WINDOW CLOSES TODAY*\n"
                "  The intro window you were warned about for 3 days closes Sep 21 PDT — *TODAY*. If you haven't sent this yet, DO IT NOW. Even if it's 11pm. This is your best shot at clearing the Indeed feed suspension.\n\n"
                ":sos: *INDEED FEED SUSPENDED — Day 29*\n"
                "  Fraud evidence package (Manan + Divij) → Jessica Kanaskie → 2-3 week review. Where does this stand? It's been a month.\n\n"
                ":large_orange_circle: *DEPARTURES SIGNAL DOCS — 24+ DAYS OVERDUE*\n"
                "  Conflict docs + data → Zane, Sean, Jon W, Bobby. This hasn't been mentioned in 2 weeks. Block 30 mins tomorrow.\n\n"
                ":large_orange_circle: *INDEED EASY APPLY PDF — DUE SEP 30*\n"
                "  9 days away. Auto-enablement explanation, no disable feature. Submit within 2 days = by Sep 23.\n\n"
                ":large_orange_circle: *MARINA / MUNDO ACADEMY — 12+ DAYS OVERDUE*\n"
                "  marina@mundoacademy.com. Under 5 minutes. Just do it.\n\n"
                ":large_yellow_circle: *EARNBETTER (Jon Salzberg)* — 18+ days overdue. jon.salzberg@earnin.com\n"
                ":large_yellow_circle: *EARNJOBCASE (Ernan)* — 13+ days, Iszael blocked.\n"
                ":large_yellow_circle: *Q4 OKRs* — Lock was Sep 18. Skye writing Q4 narrative. Confirm status with Skye.\n"
                ":large_yellow_circle: *IBK JD A/B signal* — 3+ weeks overdue. Pull before V2 widens.\n"
                ":large_yellow_circle: *422 publishing errors* — 146 locations since Jul 9. Jatin RCA still outstanding."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:trophy: TEAM ACTION ITEMS TO TRACK*\n"
                "• *Jatin* — New sprint cadence draft by Thu Sep 24; add Skye to AI compliance thread\n"
                "• *Iszael* — Fix talent pool copy bug (city not neighborhood)\n"
                "• *Fadi* — Design QA on talent pool flow (after staging restored)\n"
                "• *Gbolade* — Demo videos for all 5 Orca input sources\n"
                "• *Tiger* — Resume job description formatting after Salesforce real-time work for Jon W\n"
                "• *Skye* — Share company-level verification data with Manan; transition ownership\n"
                "• *Malcolm* — Comms assistant production release pending your decision"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:star2: CLOSING THOUGHT FROM YOUR CHIEF OF STAFF*\n\n"
                "Manan — you came back from Yosemite and didn't miss a beat. Four meetings, Q4 framing locked with Skye, a 5x ZipRecruiter mystery solved, talent pool legal path scoped, and you watched your team demo AI-native tooling that could 10x their output. That's a Senior PM day.\n\n"
                "But here's the honest flag: *the David intro window closes tonight.* Everything else on the watch list is manageable. That one is not. It's the difference between clearing the Indeed suspension in October or never. Send the email. Right now.\n\n"
                "_You've got this. One week from now, Indeed will be back, Q4 OKRs will be locked, and Orca will be running hot. Keep going._ :muscle:"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest — Sep 21, 2026 (Return from Yosemite)",
    "blocks": blocks
}

def preview():
    print("\n" + "=" * 80)
    sys.stdout.buffer.write("CHIEF OF STAFF DIGEST PREVIEW — Sep 21, 2026\n".encode("utf-8", errors="replace"))
    print("=" * 80)
    for block in blocks:
        if block.get("type") == "header":
            txt = block["text"]["text"]
            sys.stdout.buffer.write(f"\n### {txt} ###\n".encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            txt = block["text"]["text"]
            sys.stdout.buffer.write(f"\n{txt}\n".encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            print("-" * 80)
    print("=" * 80)

if not TOKEN:
    print("[PREVIEW MODE] No SLACK_TOKEN found — printing digest and exiting.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"[SUCCESS] Digest sent to Slack channel {CHANNEL}")
        print(f"  Timestamp: {result.get('ts')}")
    else:
        print(f"[ERROR] Slack API returned error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error sending to Slack: {e}")
    preview()
    sys.exit(1)
