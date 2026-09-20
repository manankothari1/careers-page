#!/usr/bin/env python3
"""Chief of Staff daily digest — Sep 19, 2026 (Yosemite Day 2 → Monday Battle Plan)"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🏕️ Yosemite Day 2 — Sunday Evening Dispatch",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Hey Manan* — hope Yosemite is absolutely stunning right now. No meetings today, which means your brain got a genuine rest. That's not a gap in the record — that's fuel. You're going to need it, because *Monday September 22* is a big one: your *first Exec Review as Senior Product Manager.* Let's make sure you walk in locked and loaded. 🎯"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🚨 *CRITICAL — WINDOW CLOSES TOMORROW (Sep 21)*\n\n*David (Indeed Product) intro window closes Sep 21.* You're OOO through Tuesday, which means this deadline passes while you're off the grid. If you have any cell signal tomorrow, a quick DM to whoever has David's contact (likely Catherine or Jessica Kanaskie at Indeed T&S) could keep this door open. The feed has been suspended for *27 days* now — every week of delay is another week of zero Indeed traffic. Consider asking a teammate to ping David on your behalf today or tomorrow."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🏆 *MONDAY SEP 22 — EXEC REVIEW GAME PLAN*\n\nThis is your *debut exec review as Senior PM.* You've earned this seat. Here's how to own it:\n\n*What they're going to ask:*\n• What's the plan to fix the D5 zero-applicant rate (41% → <10%)?\n• Why is Indeed still suspended, and what's the mitigation?\n• What does Q4 look like with the new growth positioning?\n• How does hiring drive trial conversion?\n\n*Your narrative thread:*\nCore foundation first → trial conversion → talent pool. Education-first growth. Semi-skilled ICP. Proactive signals (payroll surface). $650K ARR on the way up.\n\n*Slides/prep to finalize:*\n• Intent signals proposal (Fadi should have the FigJam draft) — review before the meeting\n• Q4 OKR locked Friday Sep 18 — confirm final version\n• Fraud status update: model 94% precision, feed suspended Day 28, evidence package with Jessica Kanaskie"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🔥 *FIRES TO TACKLE MONDAY MORNING (before Exec Review)*\n\n*1. Departures Signal Docs — 22 DAYS OVERDUE*\nConflict docs + data → Zane, Sean, Jon W, Bobby. This has been overdue since Sep 4. Block 20 minutes Monday AM.\n\n*2. Marina / Mundo Academy — 10+ DAYS LATE*\nEmail marina@mundoacademy.com. Under 5 minutes. Do it first thing.\n\n*3. Jon Salzberg / EarnBetter — 16+ DAYS OVERDUE*\njon.salzberg@earnin.com — NDA thread with Ray + Skye needs to happen before any customer data flows. Escalate to Skye if no response.\n\n*4. EarnIn/Jobcase (Iszael blocked on Ernan reply)*\n10+ days unaddressed. Escalate to Skye. Iszael is fully blocked.\n\n*5. Indeed Easy Apply PDF — DUE SEP 30 (11 days)*\nNo disable feature. PDF approach locked. Submit within 2 days of return — this is Sep 24 latest."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "📋 *WEEK OF SEP 22 — ACTION QUEUE*\n\n*Intent Signals (High Priority)*\n• Review Fadi's FigJam draft (payroll-focused)\n• Prepare deck for Gabe (Payroll PM) + Alexis\n• Schedule sync with Gabe — payroll end-of-period summary + Payroll Journal + anchor + post-payroll email are the 4 placements\n\n*Talent Pool Consent*\n• Kick off the consent thread (you said you'd do this Sep 18 — it's still open)\n• T&S input needed on historical applicants (legally gray)\n• Matan mapping full comms journey (SMS Twilio + email SendGrid)\n\n*Reactivate + Copy*\n• Compile task list and walk Bob or Madhav through it\n• Fadi to create Linear project\n• Fadi to map 3-week reactivation window as separate flow\n\n*OTP & Engineering*\n• Gbolade: 3 OTP fixes + resume iframe height — confirm shipped\n• Jon Blackwell: confirm Boolean wage access field → unblocks Iterable trigger\n• Divij CSV spec for Iterable — blocking experiment coding\n\n*Sprint & QA*\n• Confirm sprint show-and-tell scheduling (tentative Sep 25 — include sales + support)\n• IBK JD A/B signal pull — overdue 3+ weeks\n\n*Hiring LP*\n• Matan + Meg: pricing module, benefit-led copy, updated screenshot, demo embed (Brian)\n• Hold on paid spend until all 4 done — 7shifts is your benchmark\n\n*Source Claim tracking table* — Manan to build\n*Performance Pulse check-ins* — due this week\n*Candidate exclusion rule* — active interviewees should not get new job recommendation emails"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "📊 *KEY METRICS SNAPSHOT (as of Sep 18)*\n\n• Indeed feed: 🔴 SUSPENDED — Day 27. Evidence package with Jessica Kanaskie. 2-3 week review window.\n• D5 zero-applicant rate: 41% (target <10%)\n• Line cook healthy by D30: 7% (target 50%)\n• ARR: $650K+ (up from $450K Jan 2026) — great trajectory 📈\n• Healthy job rate: 30% of ICP (target 80%)\n• Paid retention: 1-mo ~90%, 2-mo high 80s, 3-mo high 70s\n• Monthly churn: ~12%\n• Talent pool: 231K active\n• Trial messaging insight: 40% never message; 1-2 messages doubles conversion (15%→30%)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "💪 *REMINDER: WHO YOU ARE RIGHT NOW*\n\nYou are a *Senior Product Manager at Homebase*, freshly promoted (Sep 16). Ray initiated it. Jatin and Martin advocated. You earned this in a sprint. You've shipped OTP, locked the morphing card, defined PMF as share of wallet, set the Q4 growth strategy, separated the fraud taxonomy, and set intent signals on the most powerful surface in the product — payroll. That's a week's worth of work most PMs would stretch across a quarter.\n\nGo enjoy Yosemite. Sleep under the stars. You've got a big Monday ahead and you're more than ready for it. 🌟"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff digest — Sunday Sep 19, 2026 · No meetings today (Yosemite Day 2) · Next: Mon Sep 22 Exec Review · Indeed suspended Day 27 · EarnBetter NDA pending · SEP 30 deadline: Indeed Easy Apply PDF"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Sunday Sep 19 — Yosemite Day 2 dispatch + Monday battle plan"
}


def preview():
    sys.stdout.buffer.write(b"\n=== CHIEF OF STAFF DIGEST PREVIEW ===\n")
    sys.stdout.buffer.write(b"DATE: Sunday Sep 19, 2026 (Yosemite Day 2)\n")
    sys.stdout.buffer.write(b"CHANNEL: D06E4QMHCNN\n")
    sys.stdout.buffer.write(b"STATUS: NO SLACK TOKEN\n\n")
    for block in blocks:
        if block.get("type") == "header":
            line = ("=== " + block["text"]["text"] + " ===\n").encode("utf-8", errors="replace")
            sys.stdout.buffer.write(line)
        elif block.get("type") == "section":
            text = block["text"]["text"].replace("*", "").replace("_", "") + "\n\n"
            sys.stdout.buffer.write(text.encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                line = ("[ctx] " + el.get("text", "") + "\n").encode("utf-8", errors="replace")
                sys.stdout.buffer.write(line)
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + TOKEN,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully.")
            else:
                print("Slack API error:", body.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error:", e)
        sys.exit(1)


if not TOKEN:
    preview()
    print("\nAdd SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets to enable live delivery.")
    sys.exit(0)

send()
