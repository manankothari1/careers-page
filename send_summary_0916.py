#!/usr/bin/env python3
"""Chief of Staff daily digest for Manan Kothari — Sep 16, 2026"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Your Daily Debrief — Wed, Sep 16, 2026", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3 meetings | Day 23 of Indeed suspension | OKR lock in 2 days | Yosemite in 2 days*\n"
                "_Cron fired at midnight UTC = your 5pm debrief. Day grade: *A+* — read on for why._"
            )
        }
    },
    {"type": "divider"},

    # BIG NEWS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":tada: *MANAN — YOU GOT PROMOTED.* :tada:\n\n"
                "You are now a *Senior Product Manager* at Homebase.\n\n"
                "Ray initiated it. Skye confirmed it. Jatin advocated directly with Martin (director-level) during his 1:1 on your behalf. "
                "Ray's quote on the call: _'Sky, you now have 4 months of reprieve.'_ Well deserved. Own it."
            )
        }
    },
    {"type": "divider"},

    # MEETINGS OVERVIEW
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:calendar: Today's Meetings (3)*\n\n"
                "*8:30am* — `Fadi / Manan` — Indeed job lifecycle design deep-dive\n"
                "*9:30am* — `Building Hiring Comms: Enabling LCM` — Matan, Soumya, Jatin, Skye, Nelson, Darin\n"
                "*2:00pm* — `Hiring EPD Leads Sync & Prep` — Jatin, Fadi (+ org chatter + Q4 shape)"
            )
        }
    },
    {"type": "divider"},

    # DECISIONS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Indeed Job Lifecycle — Architecture Locked*\n"
                "• Default expiry extended from 30 → *120 days* (Indeed max before requiring a fresh post)\n"
                "• Two job-close paths: (A) customer signals a hire, (B) customer goes silent → 30-day prompt → 7-day warning → auto-close\n"
                "• Deduplication: same role within 21 days = reopen existing post ID; after 21 days = new post ID, same requisition ID\n"
                "• *Why:* Indeed compliance is mission-critical. 'Indeed jail' risk is real. No shortcuts.\n\n"

                "*2. Job-Close Modal — Direction Set (with a delta)*\n"
                "• You prefer *Option C: morphing modal with a stepper* (one question at a time, conditionally shown)\n"
                "• Skye prefers Option A — *resolve this with Fadi tomorrow before he prototypes*\n"
                "• Fadi is prototyping only (not building) to feel the interaction first. Smart.\n\n"

                "*3. OEM Candidate Messaging on Job Close — Added*\n"
                "• If interviews are live when a job closes, affected candidates get notified\n"
                "• OEM sees a pre-filled template they can edit *before* it sends — customers hate surprises\n"
                "• Adds complexity to the messaging pipeline but agreed it's solvable and worth it\n\n"

                "*4. LCM Data into Iterable — Short-Term Path Chosen*\n"
                "• *Short-term:* High Touch (queries Databricks, daily sync, no eng lift) for Indeed comms\n"
                "• *Long-term:* Custom events (near-real-time triggers) once Nelson + Paul's playbook is ready (1-2 months)\n"
                "• *Why:* Indeed comms don't need real-time today. High Touch is the right call. Don't over-engineer.\n\n"

                "*5. Steps 2-4 Iterable Emails — Jatin Owns the Fix*\n"
                "• Hiring email steps 2-4 stopped firing after V1→V2 migration in July\n"
                "• Root cause: Ripple was never instrumented (not a metadata issue)\n"
                "• Jatin re-instruments + confirms job request ID is included. This unblocks Soumya's personalization work.\n\n"

                "*6. SendGrid Migration — NOT Now*\n"
                "• Consolidation into Iterable is the right long-term direction (Darin has buy-in)\n"
                "• But migration = heavy lift (IP warming, spam placement, months of effort) with a strained LCM team\n"
                "• Decision: map everything in SendGrid first, then pilot *one email migration* to baseline the effort\n\n"

                "*7. Quality Bar — You and Fadi Aligned*\n"
                "• Pattern identified: product has accepted low-quality decisions due to perceived eng constraints\n"
                "• New norm: *define what 'good' looks like first, then scope down if needed* — but maintain the bar\n"
                "• This was a healthy reset. Keep enforcing it.\n\n"

                "*8. Culinary Agents — 3rd Boost Option Added to Sprint*\n"
                "• Add Culinary Agents at $69/post as a 3rd boost option (between Homebase and ZipRecruiter)\n"
                "• Show only for BOH/FOH roles at restaurant-type accounts\n"
                "• 'Recommended' pill shifts to Culinary Agents when applicable; UI hierarchy updated\n"
                "• Fadi estimates it's a *very small lift* — targeting completion tomorrow\n\n"

                "*9. Q4 Shape — 3 Focus Areas Emerging*\n"
                "• (1) Trial journey — strong OEM engagement, messaging a candidate drives conversion (15% → 30%)\n"
                "• (2) Quality improvements — screener opt-out, AI toggle complaints, deal-breaker pre-population\n"
                "• (3) Talent pool — employee-first matching, push notifications experiment\n"
                "• Skye writing Q4 narrative POV by EOW. You compile product problem spaces list → stack-rank with Fadi + Jatin\n\n"

                "*10. Talent Pool Messaging — Matan Owns End-to-End*\n"
                "• Timing, copy, and channel all on Matan. You're PM, he's the implementer.\n\n"

                "*11. Intent Signals — NOT in Next Sprint (Yet)*\n"
                "• You and Fadi review Matan's Vercel doc *together tomorrow* before deciding\n"
                "• Risk of rushing: some of Matan's suggestions (data viz, overtime signals) may not belong in Hiring\n"
                "• Wednesday is lookahead. Fadi has Fri/Mon/Tue to build if you align tomorrow. *Tight window.*"
            )
        }
    },
    {"type": "divider"},

    # ACTION ITEMS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rocket: Your Action Items — Sorted by Urgency*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:rotating_light: TONIGHT / BEFORE EOD:*\n"
                "• :slack: *Slack Skye about EarnIn* — need a response from the CEO to unblock the partnership; Ernan has gone dark 8+ days. Escalate to Skye or John NOW.\n"
                "• :speech_balloon: *Message Soumya* re: talent pool activity recency — this is blocking in-progress talent pool work\n"
                "• :mag: *QA:* salary recommendations, comms agent, talent pool (all in QA now)"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:fire: TOMORROW — HARD DEADLINE:*\n"
                "• :brain: *Q4 thoughts → Skye* — DUE THURSDAY SEP 17. OKR lock Fri Sep 18. Exec review Mon Sep 22. This is #1 priority.\n"
                "• :pencil: *Review Matan's intent signals doc with Fadi* (morning) — decide together before Wed lookahead. Fadi needs Fri/Mon/Tue to build.\n"
                "• :art: *Clean up + finalize FigJam flow* — both job-close paths, silent-customer cadence, candidate comms branch\n"
                "• :handshake: *Align Q4 big boulders + KR thresholds with Skye* — before Friday OKR lock. Don't let this slip."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:memo: THIS WEEK:*\n"
                "• :clipboard: *Compile Q4 product problem spaces list* — Fadi + Jatin involved in stack-ranking\n"
                "• :busts_in_silhouette: *Performance Pulse check-in conversations* — due this week (all-hands callout Sep 14)\n"
                "• :ping_pong: *Ping Rohit* — Databricks tables for Indeed lifecycle comms → Hightouch → Iterable\n"
                "• :bar_chart: *Measure time-to-apply after email send* — determines real-time vs. batch for talent pool"
            )
        }
    },
    {"type": "divider"},

    # OVERDUE
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:warning: Overdue — These Need to Stop Slipping*\n\n"
                ":red_circle: *Departures Signal Docs* — 13+ DAYS OVERDUE (was due Sep 4). "
                "Conflict docs + data → Zane, Sean, Jon W, Bobby. "
                "Not mentioned in ANY meeting for 8 consecutive days. *Do it today or tomorrow.*\n\n"

                ":red_circle: *EarnIn sample feed → Jon Salzburg* — 15+ days overdue. "
                "jon.salzberg@earnin.com. Blocked, but send what you have.\n\n"

                ":red_circle: *Marina / Mundo Academy* — 7 days late. "
                "marina@mundoacademy.com. Quick email. Under 5 minutes.\n\n"

                ":large_yellow_circle: *IBK JD A/B signal* — 3+ weeks overdue. "
                "Pull the signal before V2 widens and the comparison gets muddier.\n\n"

                ":large_yellow_circle: *422 publishing errors* — 146 locations since Jul 9. "
                "Jatin's RCA still outstanding. Flag in next sync."
            )
        }
    },
    {"type": "divider"},

    # WATCH LIST
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:eyes: Watch List*\n\n"
                "• *Indeed suspension:* Day 23. Fraud evidence package → Jessica Kanaskie still outstanding. "
                "David (Indeed Product) intro window = Day 3 of 7 (closes Sep 21). Be ready with a crisp pitch.\n"
                "• *Yosemite:* Sep 18-21, Diamond O Campground. Departure = *Friday in 2 days.* Pack early.\n"
                "• *Skye back from Toronto* — she's in. Q4 narrative POV coming by EOW.\n"
                "• *Jatin's read on org:* Ankit flattening — EMs potentially phased out, tech leads reporting to directors, ~4-person teams. "
                "All senior female eng leaders have exited or are being pushed out (Ronnie, Palomilu, Kanchana, Andrea). "
                "Andrea told Fadi directly: 'Ankit doesn't like it when I disagree with him.' Watch this closely.\n"
                "• *Gbolade:* OTP fixes (3) + resume iframe height still outstanding. Ping for status.\n"
                "• *Carlo:* knowledge risk on Talent Pool + Indeed 3LO. Tiger pairing but Carlo taking time off soon. "
                "Make sure Tiger is fully unblocked.\n"
                "• *Darren (lifecycle):* Iterable pipeline params still need alignment.\n"
                "• *Skye signaling daily in-person eng standups* — Jatin setting up monthly sync with Skye. New cadence forming."
            )
        }
    },
    {"type": "divider"},

    # FOOTER
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day Grade: A+* :star:\n"
                "You got promoted. You made 11 real architectural decisions across 3 meaty meetings. "
                "You aligned on quality standards, Q4 shape, and the Iterable data strategy. "
                "The only thing keeping this from perfect is the overdue items that keep rolling. "
                "Tomorrow is a sprint — Q4 deadline, intent signals review, FigJam cleanup. You've got this.\n\n"
                "_Compiled by your Chief of Staff. See you at 5pm tomorrow. :wave:_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Your Daily Debrief — Wed Sep 16, 2026 | Day Grade: A+ | 3 meetings | Promoted to Senior PM!",
    "blocks": blocks
}

def preview():
    print("=" * 70)
    print("SLACK PREVIEW — no token available")
    print("=" * 70)
    for block in blocks:
        if block["type"] == "header":
            print(f"\n### {block['text']['text']} ###\n")
        elif block["type"] == "section":
            txt = block["text"]["text"]
            # strip mrkdwn markers for terminal readability
            for ch in ["*", "`", "_", ":"]:
                txt = txt.replace(ch, "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            print("-" * 70)
    print("=" * 70)

def send_to_slack(token):
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
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                preview()
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        preview()

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

if token:
    send_to_slack(token)
else:
    print("[INFO] No SLACK_TOKEN found — printing preview.")
    preview()
