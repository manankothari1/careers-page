#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari — Tuesday Aug 11, 2026."""

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
            "text": "Chief of Staff Daily Brief — Tuesday Aug 11, 2026 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! \U0001f44b You had a *BIG* day — two high-signal meetings that genuinely moved things forward. Here's everything you decided, why it matters, and what you need to do next. Let's go! \U0001f680"
        }
    },
    {"type": "divider"},
    # ---- MEETING 1: Indeed ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd Meeting 1: Indeed ATS Partner Management — 9:30 AM*\n*Status: URGENT \u26a0\ufe0f — Feed Flagged*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f7e1 What Happened:*\nIndeed's Trust & Safety team flagged Homebase's feed for elevated fraud. If the trend continues, every new company submitted to Indeed will require *manual review* (delays applicants, doesn't block them — but still bad). Catherine from ATS Partner Management led the call.\n\nThe core issue: ~1% of free trial accounts drive most fraudulent activity. Indeed's general policy *discourages* free trials — but Homebase's tiered model (existing paying customers trialing Hiring) *may* be exempt. Catherine is confirming."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f7e2 Key Decisions Made:*\n• Accepted that this is a real risk, not a false alarm — remediating proactively\n• Agreed to build a comprehensive fraud signal checklist from Indeed's shared resources\n• Agreed to update Homebase support articles + CS team guidance with Indeed's posting standards\n• Will follow up with Catherine specifically on free trial exemption before changing any feed logic"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f535 Why This Matters:*\nYou already shipped V3 of the fraud model (94% precision, 75.3% accuracy). The internal tester root cause is identified. *This call is the next chapter* — ensuring Indeed alignment so the feed stays clean and applicant volume isn't throttled."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Action Items (Indeed):*\n1. \U0001f4de *Follow up with Catherine* — confirm whether Homebase's tiered free trial model is exempt from Indeed's fraud free-trial guidance *(DUE: this week)*\n2. \U0001f4cb *Build fraud checklist* — compile exhaustive list of fraud signals from Catherine's shared doc + Indeed help center links → feed into fraud scoring model *(DUE: before next sprint)*\n3. \U0001f4dd *Update support articles + CS guidance* — incorporate Indeed's job posting best practices (titles, descriptions, location accuracy, duplicate rules) → share Indeed employer help center as reference *(DUE: this week)*"
        }
    },
    {"type": "divider"},
    # ---- MEETING 2: Ray Weekly ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f91d Meeting 2: Manan / Ray Weekly — 2:30 PM*\n*Status: PIVOTAL \U0001f525 — Team Operating Model Reset*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f7e1 What Happened:*\nRay named the pattern clearly: the team is being pulled in too many directions by cross-functional mandates — page templates, Essentials Journey, domain events — all scoped as 'quick' and all ballooning. Ray is using this as a reset moment. He wants Manan to step up as the *true leader* of the team: question timelines, push back on scope, and stop accepting sunk-cost logic."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f7e2 Key Decisions Made:*\n• *Team north star locked* — only two things matter: (1) getting customers to start a trial and convert to paid, (2) ensuring every job gets enough applicants. Everything else is a distraction.\n• *Stop accepting mandates at face value* — Manan will question scope + timelines, push back, and stop work when it exceeds scope\n• *Page templates + Essentials Journey* = flagged as distractions from core focus; Manan to define exit points\n• *IBK to be pulled into direct partnership* — IBK has been too passive; Manan needs to proactively lead him, not wait\n• *Sales team engagement gap acknowledged* — very little product <> sales interaction currently; Manan to engage sales reps directly\n• *Ray acts as megaphone* — Ray will back Manan with hiring leads when Manan flags what he needs"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f535 Why This Matters:*\nThis is a full mandate for you to own the team's direction. Ray is explicitly telling you to stop letting timelines and cross-functional asks drive the roadmap. You are the PM. Push back hard, protect the team's focus, and drive the agenda. This is the move to owning your leadership."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Action Items (Ray Weekly):*\n1. \U0001f6d1 *Draft 'work to stop' list* — use the list already sent to Ray as a starting point; add recommended exit points for each (Essentials Journey, page templates, etc.) → share with Ray *(DUE: ASAP, today or tomorrow)*\n2. \U0001f4e3 *Write hiring team operating model* — cover: team focus, decision-making norms, cross-functional boundaries → share with Ray to align with hiring leads *(DUE: this week)*\n3. \U0001f91d *Engage sales reps directly* — mirror Ray's approach with Claire: ask what the sales team needs, then drive a product point of view *(DUE: schedule this week)*\n4. \U0001f4ca *Flag IBK for direct partnership* — pull IBK into proactive collaboration vs. waiting to be directed *(DUE: immediate)*"
        }
    },
    {"type": "divider"},
    # ---- WATCH LIST ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 Watch List — Critical Reminders*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f534 *Dana Lobo — LAST DAY TOMORROW (Wed Aug 12)* — Transition is compressed. Page Templates ownership still not fully resolved. Tonight or first thing tomorrow: confirm handoff for anything still open with Dana before EOD Wednesday.\n\n\U0001f534 *Fadi Boost Modal Figma — 12+ days overdue* — Fadi is blocked on YOU. Unblock him before tomorrow's design session.\n\n\U0001f534 *422 Job Publishing Errors — Day 31+* — Jatin on RCA. Ray is OUT = you're decision-maker. Get a status update today.\n\n\U0001f7e1 *New GM of Hiring* — Start date unresolved (18th vs 25th Aug). Ray to confirm. Follow up with Ray directly.\n\n\U0001f7e1 *Sky (new Head of Product)* — You still need to schedule a 1:1 to align on Q3 roadmap. Don't let this slip another week.\n\n\U0001f7e1 *Amplitude dashboard → Matan* — Overdue since Aug 6. Send immediately.\n\n\U0001f7e1 *JD A/B experiment (IBK)* — Running this week (50/50). Monitor for early signal.\n\n\U0001f7e1 *Strategy deck + Roadmap-to-goals* — Were due Aug 10. Confirm delivered to John + Ray."
        }
    },
    {"type": "divider"},
    # ---- TOMORROW ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4c5 Tomorrow (Wednesday Aug 12) — Key Priorities*\n1. \U0001f44b *Dana's last day* — Make it a good one. Final handoffs, confirm Page Templates ownership, say thank you.\n2. \U0001f3a8 *Hiring Essentials Journey design session with Fadi + Keyvan* — Scope locked: 2 flows only, no Figma, FigJam entry points + Loom from Fadi.\n3. \U0001f6d1 *Send 'work to stop' list* to Ray — ideally before the design session.\n4. \U0001f4de *Catherine / Indeed follow-up* — Send the free trial clarification email first thing."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af Today's Summary:* 2 meetings | 10+ decisions | Ray gave you the full mandate. Lead from the front. \U0001f4aa\n\n_Your chief of staff always has your back — see you tomorrow at 5pm PDT. \u2764\ufe0f_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Brief — Tuesday Aug 11, 2026",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write("\n===== SLACK PREVIEW (no token) =====\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"Channel: {CHANNEL}\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("---\n".encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(f"\n[HEADER] {block['text']['text']}\n".encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write(f"\n{block['text']['text']}\n".encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("─" * 60 + "\n".encode("utf-8", errors="replace") if False else b"\n" + b"-" * 60 + b"\n")
    sys.stdout.buffer.write("\n===== END PREVIEW =====\n".encode("utf-8", errors="replace"))

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
        result = json.loads(resp.read().decode("utf-8"))
        if result.get("ok"):
            print(f"SUCCESS: Message sent to {CHANNEL}")
        else:
            print(f"SLACK ERROR: {result.get('error', 'unknown')}")
            preview()
            sys.exit(1)
except urllib.error.URLError as e:
    print(f"NETWORK ERROR: {e}")
    preview()
    sys.exit(1)
