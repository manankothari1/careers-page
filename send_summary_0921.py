#!/usr/bin/env python3
"""
Daily Chief of Staff Digest — Sunday Sep 20, 2026 (PDT) / Sep 21 UTC
No meetings today (Yosemite Day 3). Sending Monday Battle Plan.
Channel: D06E4QMHCNN
"""

import os
import sys
import json
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🏔️ Welcome Back, Manan! Your Monday Battle Plan",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "*Sunday Sep 20 · Yosemite Night 3 · Daily Digest @ 5PM PDT* | No meetings today — you were exactly where you needed to be."
            }
        ]
    },
    {"type": "divider"},

    # Exec Review hype
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎖️ TOMORROW: YOUR FIRST EXEC REVIEW AS SENIOR PM*\n\nYou earned that title. Now you walk into the room owning it. Here's your narrative:"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*📈 What you've shipped (Q3)*\n• OTP live (company-level verification)\n• V1 backend fully deprecated\n• Match definition updated (resume OR screener)\n• Intent signals placement LOCKED (payroll surface)\n• Fraud taxonomy separated (true fraud vs ToS)\n• Indeed Easy Apply compliance (PDF, Sep 30 deadline)\n• 4-year AI screener data retention policy\n• Morphing modal direction LOCKED (Option C)\n• EarnBetter mutual test green-lit\n• Q4 growth strategy aligned (net new, education-first)"
            },
            {
                "type": "mrkdwn",
                "text": "*🎯 Q4 Strategy (your 3 pillars)*\n1. Trial Journey — 40% of trials never message. Messaging 1-2 = 2x conversion.\n2. Quality Improvements — job health 30% → 80%. AI screener, deal-breakers.\n3. Talent Pool — 231K active, consent framework, comms journey.\n\n*📊 Key Metrics to know cold*\n• Indeed: SUSPENDED Day 28. Feed = 0. David window = Sep 21.\n• ARR: $650K+ (from $450K Jan)\n• Paid retention: 90% (1mo), high-80s (2mo)\n• Trial conversion: 6.1% FFH vs 8.2% non-FFH\n• Healthy job rate: 30% (target: 80%)"
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💬 Exec Review talking points:*\n• The ICP insight: FFH week-to-hire is NOT a moat. Semi-skilled industries need AI screening + candidate profiling. Our play = core foundation first, then expand.\n• The Indeed crisis: feed suspended Day 28. Fraud model at 94% precision. Evidence package sent to Jessica. David (Product) intro window = tomorrow.\n• The talent pool opportunity: 231K contacts, low-hanging fruit for reactivation.\n• PMF framing: share of wallet = 50%+ of hires through product. ~15-month horizon. That's the north star."
        }
    },
    {"type": "divider"},

    # CRITICAL
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 CRITICAL — DO THIS FIRST THING MONDAY MORNING*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1️⃣  *David (Indeed Product) — Window Closes TODAY Sep 21*\n→ This is Day 28 of Indeed feed suspension. David's intro window expires TODAY.\n→ Send the intro request the moment you're back. Do not wait until after exec review.\n→ Contact: through Jessica Kanaskie (jkanaskie@indeed.com) or whoever has the intro.\n→ Even a 3-sentence Slack/email before 9am buys you the window.\n\n2️⃣  *Indeed Easy Apply PDF — Due Sep 30 (10 days away)*\n→ Auto-enablement explanation. No disable feature. Submit within 2 days of return (Sep 24 latest).\n→ You said Sep 24. Monday is your window.\n\n3️⃣  *Intent Signals Review + Deck Prep*\n→ Fadi drafted the proposal for Gabe (Payroll PM) + Alexis while you were gone.\n→ Review Fadi's FigJam first thing and prep your deck before meeting Gabe this week."
        }
    },
    {"type": "divider"},

    # Week priorities
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 WEEK OF SEP 21 PRIORITIES (ordered)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 — This week or it's a crisis:*\n"
                "• David/Indeed intro (TODAY)\n"
                "• Exec Review (today)\n"
                "• Indeed Easy Apply PDF → submit by Sep 24\n"
                "• Intent signals deck → Gabe + Alexis meeting this week\n"
                "• EarnBetter follow-up (Jon Salzberg jon.salzberg@earnin.com) — 16+ days overdue\n"
                "• Marina reply (marina@mundoacademy.com) — 10+ days, under 5 min\n\n"
                "*P1 — This week, meaningful progress:*\n"
                "• Talent pool consent thread (you said you'd kick it off Sep 18)\n"
                "• Reactivate + Copy task list → walk Bob or Madhav through it\n"
                "• Sprint show-and-tell scheduling (tentative Sep 25, include sales + support)\n"
                "• Jon Blackwell: confirm Boolean wage access field (unblocks Iterable)\n"
                "• Khrystyna: draft hiring incident response workflow\n"
                "• Khrystyna: raise EIN verification with Laura before October Toronto\n\n"
                "*P2 — Keep moving:*\n"
                "• Fadi: Linear project for Copy + Reactivate\n"
                "• Matan + Meg: hiring LP cleanup (pricing module, benefit-led copy, demo embed)\n"
                "• Chy → Superline creator ad test\n"
                "• T&S: historical applicant consent ruling\n"
                "• OTP retest (Gbolade fixing 3 issues)\n"
                "• 422 publishing errors RCA (Jatin, 146 locations since Jul 9)"
            )
        }
    },
    {"type": "divider"},

    # Overdue
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*⏰ OVERDUE — These Cannot Slip Another Week*\n\n"
                "• *Departures Signal Docs* — 22+ DAYS. Conflict docs + data → Zane, Sean, Jon W, Bobby. "
                "Not mentioned Sep 8–19. Will be Day 23 Monday. Pick a 30-min slot.\n"
                "• *EarnIn/Jobcase (Ernan reply)* — Iszael is blocked 11+ days. "
                "Escalate to Skye if no reply by EOD Monday.\n"
                "• *IBK JD A/B experiment signal* — 3+ weeks overdue. Pull before V2 widens.\n"
                "• *Performance Pulse check-ins* — Due Sep 14-18. You've been OOO. First week back, schedule them."
            )
        }
    },
    {"type": "divider"},

    # Watch list
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*👁️ TOP WATCH LIST ITEMS — Week of Sep 21*\n\n"
                "• *Indeed feed* — Day 28 of suspension. Every day costs you organic traffic. "
                "David intro = the unlock. Jessica = the contact. Move fast.\n"
                "• *Exec Review* — Your first as Senior PM. You walked in knowing the data cold. "
                "Use the PMF / share-of-wallet frame. Show you think at the business level.\n"
                "• *Carlo Ferrer (Talent Pool + 3LO lead)* — KNOWLEDGE RISK flag. "
                "Make sure you have a knowledge transfer plan if he moves on.\n"
                "• *Culinary Agents $69 boost* — Fadi delivered design feedback Sep 18. Confirm shipped.\n"
                "• *Verify deal-breaker data model* — null = no deal breakers? Confirm it captures correctly "
                "before talent pool consent work builds on bad data.\n"
                "• *Pending syndication black box* — 3 states conflated (queue / fraud rejected / ToS flagged). "
                "Needs a product spec this week.\n"
                "• *Q4 OKR lock* — Was Sep 18 EOD. You were at Yosemite. Confirm with Skye first thing Monday.\n"
                "• *Source Claim tracking table* — Manan to build. Don't let this keep slipping."
            )
        }
    },
    {"type": "divider"},

    # Big picture reminder
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🗺️ YOUR NORTH STAR REMINDER*\n\n"
                "You're building toward *50% share of wallet* — half of every SMB hire going through Homebase. "
                "That's a 15-month project. The ingredients: a healthy job post (30% → 80%), "
                "a trial that converts (1-2 messages = 2x), and a talent pool that actually activates "
                "the 231K contacts sitting there. Every decision this week should ladder up to one of those three.\n\n"
                "Indeed is a blocker and a distraction. Resolve it, but don't let it become the whole story."
            )
        }
    },
    {"type": "divider"},

    # Closer
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💪 YOU'VE GOT THIS, SENIOR PM*\n\n"
                "4 days in the mountains. Probably thought about work anyway (you know you did 😄). "
                "But seriously — you come back to a team that believed in you enough to promote you, "
                "to a product that has real momentum, and to an exec review where you get to show "
                "exactly why they made the right call.\n\n"
                "The indeed situation is stressful. The overdue list is real. But your Q3 track record "
                "is undeniable and your Q4 vision is sharp. Go get 'em.\n\n"
                "_Your Chief of Staff — always in your corner_ 🤝"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Digest for Sunday Sep 20, 2026 · 0 meetings (Yosemite Day 3) · Built from week-of-Sep-14 + Sep 18 session notes"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "🏔️ Welcome Back! Your Monday Battle Plan is ready — exec review, Indeed critical, full week priorities.",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("\n" + "="*70 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("SLACK PREVIEW (no token — would send to D06E4QMHCNN)\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("="*70 + "\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            txt = block.get("text", {}).get("text", "")
            if txt:
                sys.stdout.buffer.write((txt + "\n").encode("utf-8", errors="replace"))
            for field in block.get("fields", []):
                sys.stdout.buffer.write((field.get("text", "") + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(("[ctx] " + el.get("text", "") + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("-"*60 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("="*70 + "\n\n").encode("utf-8", errors="replace"))

token = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

if not token:
    preview()
    print("⚠️  No SLACK_TOKEN found — add it in Cursor Dashboard > Cloud Agents > Secrets")
    print("   Message preview printed above. Exiting 0.")
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print("✅ Slack message sent successfully to D06E4QMHCNN")
        print("   ts:", result.get("ts"))
    else:
        print("❌ Slack API error:", result.get("error"))
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print("❌ Network error:", e)
    preview()
    sys.exit(1)
