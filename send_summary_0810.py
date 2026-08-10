#!/usr/bin/env python3
"""Chief of Staff Daily Digest - Manan Kothari - Monday Aug 10, 2026"""
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
            "text": ":briefcase: Chief of Staff Digest - Monday Aug 10, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Happy Monday. No Granola meetings were captured today, so I'm pulling from everything I know to give you your end-of-day debrief. *This is one of the biggest days of your quarter* — here's where you stand."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CRITICAL: Dana's Final 2 Days*\n\nDana is back today and *Aug 12 is her last day* (confidential). You have 2 working days to sort Page Templates ownership. Fadi has been getting conflicting info from 2 different people — you must make the call on ownership and communicate it clearly before she walks out the door. This can't slip."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mega: TODAY'S DELIVERABLES*\n\n*Strategy Deck for John + Ray* — Did you get Fadi + Jatin to review before sending? The Engineer Ownership POC should be framed as a concept in this deck. Martin is back today — did you loop him in before sending? Make sure it went out.\n\n*Roadmap-to-Goals Deck* — This maps all your workstreams to the two core goals: *500 FFH paying customers* + *70% FFH with healthy jobs*. If it's not sent yet, block time tonight."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:busts_in_silhouette: KEY PEOPLE — STATUS CHECK*\n\n:star2: *Sky (new Head of Product)* — First full week. A quick alignment sync on your Q3 roadmap = very high leverage. Don't let the week get away before you connect.\n\n:wrench: *Fadi* — He has been blocked on you for *10+ days* on the Boost modal Figma. Also needs Page Templates clarity. Two conversations, big unblocks.\n\n:mag: *Izzy* — Confirm reactivate is on staging. This is THE unlock for FFH D5 zero-applicant rate (41% today, target <10%).\n\n:lady_beetle: *Jatin* — 422 errors are at *Day 30* today (146 locations since Jul 9). Ray is out. You're the decision-maker. Get the RCA status.\n\n:gear: *Martin* — Back today. Did he weigh in on the Engineer Ownership POC before the strategy deck went out?"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rocket: THIS WEEK'S BIG LAUNCHES*\n\n:test_tube: *JD Prompt Box A/B* (IBK) — Launching *this week*. 50/50 split, users drop directly on the details page (skipping the prompt box). This directly attacks the 60% drop-off on the JD page. Watch early signal closely.\n\n:incoming_envelope: *In-Product Abandonment Survey* — Should be live via Matan (Guides, pending LCM). Confirm it's running.\n\n:repeat: *Sprint Retro* (Jatin) — Was this done today? Keep the cadence strong."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:red_circle: OVERDUE — NEEDS ACTION*\n\n*Amplitude dashboard for Matan* — Overdue since Aug 6 (4 days). Please send this tonight.\n*Fadi Boost modal Figma* — 10+ days. He's blocked. Unblock him first thing tomorrow if not today.\n*Applicant-count survey* (Great Question) — Send to team for review.\n*Matan PMM roadmap* — He committed to adding to Google Sheet by EOD Aug 6. Did he? Follow up."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:warning: WATCH LIST — ACTIVE RISKS*\n\n:fire: *Indeed Watch List* — Still ACTIVE. Homebase is flagged for fraudulent jobs. ~60% of your applicant volume flows through Indeed. Strict review = new clients' jobs don't appear. Did you email your Indeed contact this weekend? If not, do it *right now*.\n\n:fire: *422 Job Publishing Errors* — Day 30 today. 146 locations affected since Jul 9. This is Jatin's RCA but you're the decision-maker with Ray out.\n\n:fire: *Dana succession* — 2 working days. No formal succession plan. Page Templates handoff = must happen before Aug 12."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: YOUR Q3 NORTH STAR*\n\nGoal 1: FFH D5 zero-applicant rate *41% → <10%*\nGoal 2: Line cook jobs healthy by D30 *7% → 50%*\nTwo FFH metrics: *500 FFH paying customers* + *70% FFH with healthy jobs*\n\nRoot cause: jobs *not reaching Indeed* (not a conversion problem).\nKey unlock: Reactivation (Izzy) + JD quality improvements."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:checkered_flag: MONDAY PRIORITY ORDER*\n\n1. :rotating_light: Dana handoff — Page Templates ownership convo (today or tomorrow at the latest)\n2. :mega: Strategy deck → confirm it reached John + Ray\n3. :bar_chart: Roadmap-to-goals deck → send if not done\n4. :wrench: Unblock Fadi (Boost modal + Page Templates clarity)\n5. :star2: Quick sync with Sky\n6. :lady_beetle: 422 RCA update from Jatin\n7. :mag: Izzy reactivate on staging — confirm\n8. :chart_with_upwards_trend: Send Amplitude dashboard to Matan (overdue!)\n9. :incoming_envelope: Check Indeed Watch List — email contact if not done"
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "You're doing great, Manan. The July MBR showed +11.8% MoM trial starts — the team is building real momentum. This week you've got A/B tests launching, a new HoP to align with, and two decks that will shape your Q3 execution. In 2 days you become the sole Lead PM — you've been set up for this. Execute cleanly today and set the tone. :muscle:"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": json.dumps(blocks),
    "text": "Chief of Staff Digest - Monday Aug 10, 2026 - Your EOD summary is ready!"
}


def preview():
    sys.stdout.buffer.write("\n=== SLACK MESSAGE PREVIEW (no token) ===\n".encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("=== " + txt + " ===\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                txt = el.get("text", "")
                sys.stdout.buffer.write(("[context] " + txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("────────────────────────────────────\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("=== END PREVIEW ===\n".encode("utf-8", errors="replace"))


if not TOKEN:
    print("No SLACK_TOKEN found in environment — printing preview only")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + TOKEN
    }
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print("SUCCESS: message sent to " + CHANNEL)
        print("ts=" + str(result.get("ts")))
    else:
        error = result.get("error", "unknown")
        print("SLACK ERROR: " + error)
        print(json.dumps(result, indent=2))
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print("NETWORK ERROR: " + str(e))
    preview()
    sys.exit(1)
