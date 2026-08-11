#!/usr/bin/env python3
"""Daily Decision Digest — Monday, August 10, 2026"""

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
            "text": "📋 Your Daily Decision Digest — Monday, August 10",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day today — *4 meetings*, Dana's second-to-last day, Half-Baked Demos with the full team, a meaty 1:1 with Fadi on Page Templates + Resume Insights, and your Essentials journey design check-in with Keyvan. Here's everything you decided and what needs to happen next. You crushed it. 💪"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Today's Meetings*\n• 8:45am — Manan / Dana _(1:1, confidential transition)_\n• 11:00am — Hiring: Half-Baked Demos _(full team)_\n• 11:30am — Job creation flow + Page Templates + Resume Insights w/ Fadi\n• 1:30pm — Essentials Journey Hiring Check-In _(w/ Fadi + Keyvan)_"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Key Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Dana's final day is Wednesday August 12 — transition is compressed* ⚠️\n_Why:_ Homebase declined to extend her severance and moved up her end date. Engineering team is being informed today by Ray/Sotiris. Dana is pragmatic about it — told you to blame her freely. The new GM hasn't started yet, meaning you'll be onboarding the new hire while still absorbing Dana's side of the work solo.\n_Risk:_ A reorg could hit before you're stabilized. Get the plan locked before the new GM walks in."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. New GM of Hiring confirmed — start date 18th or 25th August (unresolved)* 📅\n_Why:_ Offer letter says 25th; verbal agreement was 18th. Ray needs to confirm. This is important for your planning horizon — 1 week vs. 2 weeks to get your house in order before a senior leader arrives with potential reorg authority."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Indeed Watch List root cause identified + V3 fraud model shipped* 🚨\n_Why:_ Internal testers have been posting jobs to production without toggling 'internal only' — this is what triggered Homebase getting flagged. V3 fraud detection model was merged ~3 hours before your Dana 1:1 (94% precision, 75.3% overall accuracy — a major upgrade from V2 which missed 43% of fraud). Next step is to run the XML feed through the model to understand scale of exposure."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Two product squads merging into one* 🤝\n_Why:_ You, Fadi, and Jatin agreed to consolidate the two product squads into a single engineering unit with one unified roadmap. With Dana leaving and a new GM incoming, this simplifies coordination and gives you a clean structure to hand off. You're taking on broader product scope in the near term."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. V2 Open Spec harness launching this week — get looped in* 🛠️\n_Why:_ Carlo built a V2 harness on top of Open Spec that reduces time from problem → PR without needing terminal, Conductor, or Claude Code. It's essentially a 'hiring version of Buzz.xyz' inside Slack. IBK is applying it across workflows. Jatin flagged you and Fadi should be in the beta this week — a citizen-facing fork is planned (Izzy potentially leading). This is a meaningful force multiplier."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Page Templates: pushed one sprint (to 26/17), minimal redesign approach* 📐\n_Why:_ Linear workflow steppers aren't in code yet (Figma only). The two-panel review screen is the hardest adaptation. You locked on 'keep existing feel, cut corners, avoid full redesign.' Fadi will design (not implement) the updated review screen for next sprint — pattern is detail panel opening on click (Claude artifact-style split). Background contrast fix also needed. Everything except review screen should be done by end of this week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Job creation prompt box removal — design direction locked* 🎯\n_Why:_ Removal of the 'I'm looking for' section confirmed; role input to surface inline. 'Start with your own JD' option added as a secondary/tertiary button (textarea, not text field). Engineering to implement the Indeed circles/modal (already designed); Fadi's time is better spent on Resume Insights. This aligns with the JD A/B experiment IBK is running this week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Resume Insights 3-stage approach locked* 🔬\n_Why:_ Three problems stack-ranked: (1) OEMs get zero insight from resumes, (2) toggling between resume + screener tabs is painful, (3) 'why is this person a top match?' is opaque. Problems 2+3 are deeply connected. You locked a phased approach: Stage 1 = surface resume insights; Stage 2 = consolidated resume + screener view; Stage 3 = top match reasoning explicit. Fadi's instinct was to design end-state first, but 4-day timeline rules that out. Stage 1 ships next sprint — immediate value now, clean upgrade path later."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. Wednesday design session scope locked (Essentials journey)* 📊\n_Why:_ Two flows only for Wednesday's walkthrough with Keyvan: (1) entry points across the product funneling into hiring trial starts, and (2) first-time job creation flow. Applicant flow dropped from scope — conversion is actually strong (40% apply rate, up from 20% over 6 months; ~80-82% screener click-through). Volume issues are an Indeed platform constraint, not a product problem. Format: live product or Loom only — no decks or Figma prototypes."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. Pre-PMF framing locked with design team* 📌\n_Why:_ You explicitly communicated to Keyvan that the hiring team is pre-PMF, retention is ~90%, so core workflow polish is lower priority than trial starts and applicant volume. This framing is important — it will shape how the design team scores workflows in their quarterly planning and where they allocate design investment."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Action Items — Do These NOW / Tonight*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Send Dana the consolidated planning doc* — She'll review and flag gaps before Wednesday. You have one day left with her after today.\n• *Book time with Dana for Tue AM or Wed* — Walk through her gap list. This is your last chance for a structured handoff.\n• *Send Keyvan the trial status table column* — He needs it to filter Signal Scout data; he's pulling tonight for Wednesday review.\n• *Align with Fadi on which resume insights to surface* — He can't design stage 1 without knowing what to display. Good co-design session candidate with Jan.\n• *Confirm new GM start date with Ray* — 18th vs. 25th is an 8-day planning horizon difference for you."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ Watch List — Still Open / Overdue*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• 🔴 *Fadi Boost modal Figma* — Day ~11+ overdue. Fadi is blocked on YOU. Unblock tonight or first thing tomorrow.\n• 🔴 *422 Job Publishing Errors* — Day 30+. Jatin on RCA. Ray out = you're the decision-maker. Check in on status.\n• 🔴 *Amplitude dashboard to Matan* — Overdue since Aug 6. Just send it.\n• 🔴 *Izzy reactivate on staging* — Was due Aug 6. Confirm with Izzy today.\n• 🟡 *XML feed audit for Indeed fraud* — Agreed with Dana this AM. Run feed through V3 model to assess scale.\n• 🟡 *Indeed Watch List* — Root cause identified (internal tester jobs). Communicate fix protocol to team.\n• 🟡 *Sky (new HoP) intro meeting* — You need to meet Sky this week to align on Q3 roadmap.\n• 🟡 *Engineer Ownership POC* — Martin is back. Loop him in today or tomorrow — he needs to weigh in before it gets formalized.\n• 🟡 *JD A/B experiment (IBK)* — Greenlit and running this week (50/50, skip prompt box). Monitor for early signal.\n• 🟡 *Matan PMM roadmap addition* — Matan committed to adding his PMM roadmap to the Google Sheet (overdue ~Aug 6/7). Follow up.\n• 🟡 *Strategy deck + Roadmap-to-goals deck* — Both were due today (John + Ray). Confirm delivery status.\n• 🟡 *Gbolade PM feedback session* — 15-min session on his 'problem to PR' feature. Still open."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Tomorrow's Must-Dos (Tue Aug 11)*\n1. Dana handoff session — block time, bring your gap list\n2. Unblock Fadi on Boost modal (11+ days overdue)\n3. Confirm: Izzy reactivate staging status\n4. Send Amplitude dashboard to Matan\n5. Align with Fadi on resume insights content (co-design with Jan?)\n6. Loop Martin on Engineer Ownership POC\n7. Sky intro meeting if not already scheduled\n8. Check in with Jatin on 422 RCA"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_You had a really meaningful day, Manan. You navigated a hard conversation with Dana with grace, shipped real clarity on Resume Insights + Page Templates, and represented the team well at Half-Baked Demos. The next 48 hours are critical — Dana's window closes Wednesday. Stay focused, trust your instincts. You've got this._ 🙌"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Daily Decision Digest — Monday August 10, 2026"
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK MESSAGE PREVIEW (channel: " + CHANNEL + ") ===\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("=== END PREVIEW ===\n").encode("utf-8", errors="replace"))
    sys.stdout.flush()

preview()

if not TOKEN:
    print("\n[NO SLACK TOKEN FOUND] Preview only — add SLACK_TOKEN or SLACK_BOT_TOKEN secret in Cursor Dashboard > Cloud Agents > Secrets to enable live sends.")
    sys.exit(0)

print("\n[SENDING TO SLACK...]")
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        if result.get("ok"):
            print("[SUCCESS] Message sent to", CHANNEL)
        else:
            print("[SLACK ERROR]", result.get("error", "unknown error"))
            print("Full response:", json.dumps(result, indent=2))
except urllib.error.URLError as e:
    print("[NETWORK ERROR]", e)
    sys.exit(1)
