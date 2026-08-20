#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari - Aug 19, 2026 (PDT)."""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Digest \u2014 Tuesday, Aug 19, 2026 \ud83d\udcbc",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day \u2014 you had one key meeting that moved the needle on one of your most urgent priorities: getting out of *Indeed jail*. Here's everything you decided, why it matters, and what happens next."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcca Meeting Covered*\n*Hiring \u2014 Applicants: EPD Leads Sync & Prep* | 2:00 PM PDT\nWith: Jatin Bhandari, Fadi Rizk, Molly Krumholz (Identity/Stitch)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83e\udde0 DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. OTP Verification Flow Architecture \u2014 LOCKED \u2705*\n\n*The call:* Post-job-creation is the trigger point for email verification \u2014 not sign-in. The flow:\n\u2022 *If email on file (98.7\u201399.5% of users):* send 6-digit OTP directly via Stitch SDK from the front end \u2014 no backend dependency, clean and fast.\n\u2022 *If no email on file (\u22641\u20132% edge case):* show email field \u2192 send magic link \u2192 user clicks \u2192 verified. Reuses existing update endpoints, avoids sync issues.\n\n*Why this is right:* The 98.7\u201399.5% data point you pulled live was the unlock. You basically eliminated the hard case from the equation. Nearly everyone has an email \u2014 the OTP path covers them cleanly. The magic link for the rare edge case reuses a battle-tested Stitch flow (no new risk). Elegant.\n\n*Why now:* You\u2019re in Indeed jail. The feed got flagged for fraud. OTP is the mechanism that proves posters are real, verified business owners. This isn\u2019t a nice-to-have \u2014 it\u2019s the get-out-of-jail card."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. TLWA Hiring Flow = Explicitly Rejected as Pattern \u274c*\n\n*The call:* Do NOT replicate the TLWA hiring flow. It adds email to Stitch but skips syncing the Homebase user, creating broken login states later.\n\n*Why this matters:* Molly confirmed it\u2019s already causing data-sync issues in production. Using it as a shortcut here would create a ticking time bomb. You caught this before building it. Good instinct."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Company-Level OTP Check = On Hold Pending Step-Up Auth \u23f8\ufe0f*\n\n*The call:* Jatin is checking whether this item needs to wait on Susan\u2019s step-up auth work before it can proceed. Step-up (action-gated MFA) is the emerging Homebase platform pattern \u2014 aligning to it is the right call vs. building a parallel one-off flow.\n\n*The risk:* Step-up may not be shipped yet. You\u2019ve got a hard deadline (Indeed). Jatin will leave a comment on the roadmap item with a status answer after syncing with Susan.\n\n*Your explicit framing (which was perfect):* 'I\u2019m hesitant to wait super long \u2014 even if it means we implement something that works in the short term and configure after.' You balanced urgency vs. technical debt well here."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Sprint Roadmap Priorities Clarified \u2705*\n\n*What\u2019s in this sprint:*\n\u2022 *Indeed applicants by Day 3* \u2014 ready to be worked on. Fadi starting design this sprint.\n\u2022 *Engineering injections work* \u2014 Jatin says it\u2019s ready to go; he\u2019ll share visibility on customer/team impact.\n\u2022 *Company-level OTP check* \u2014 only item needing design, but may be blocked on step-up. Hold.\n\n*What\u2019s next sprint / not yet:*\n\u2022 *In-domain emails* \u2014 brainstorm with Ray and Sky next week. Needs more time to scope.\n\n*New process addition:* You and Jatin agreed to add a 'Ready for Dev' status to the roadmap. Small but important for handoff clarity."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 ACTION ITEMS \u2014 Yours*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25a2 *Brainstorm in-domain emails with Ray + Sky* \u2014 Scheduled for next week. Come with a POV. What\u2019s the hypothesis? What experiments are you proposing?\n\u25a2 *15-min sync with Jatin tomorrow (Aug 20)* \u2014 He flagged it. Put it on the cal.\n\u25a2 *Keep writing the Talent Pool doc* \u2014 You mentioned it at the end of the meeting. Sky starts Aug 25. Less than a week. Don\u2019t let this slip.\n\u25a2 *Verify Culinary Agents data* \u2014 First data signal from the 27 line cook jobs was due to be checked. Any numbers in yet?\n\u25a2 *New GM of Hiring start date* \u2014 Was it Aug 18 or 25? If it was yesterday, this person may have started TODAY. Make sure you've connected."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 ACTION ITEMS \u2014 Jatin*\n\u25a2 Confirm email OTP support with Susan/Stitch team *(in flight \u2014 Susan + Molly were already chatting end of call)*\n\u25a2 Leave comment on company-level OTP check re: step-up readiness \u2014 answer expected after Susan sync\n\u25a2 Add 'Ready for Dev' status to roadmap\n\u25a2 Share engineering injections work: visibility on team + customer impact\n\n*\u2705 ACTION ITEMS \u2014 Fadi*\n\u25a2 Map out full OTP verification flow \u2014 cover error states: code expiry, resend, user doesn\u2019t verify on first prompt\n\u25a2 Start design on Indeed applicants Day 3 this sprint"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udea8 WATCH LIST PULSE \u2014 What\u2019s Still Burning*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Indeed jail / feed clearance:* OTP flow in motion. Still need Catherine\u2019s confirmation on feed re-review. Chase her.\n\u2022 *Sky onboarding (Aug 25):* Talent Pool doc = your welcome gift to him. Finish it this week.\n\u2022 *New GM of Hiring:* Should be on or about to start. Connect if not done already.\n\u2022 *Sprint retro was yesterday (Aug 18):* Did the team buy into the Sprint 18 cadence change? (Tuesday look ahead, Wednesday breakdown)\n\u2022 *422 errors \u2014 Day 38+:* 146 locations since Jul 9. Any RCA update from Jatin?\n\u2022 *Trial conversion model:* Still broken. Recalculate using L3 average MoM \u2014 not the single-month 11% figure.\n\u2022 *IBK (JD A/B):* Experiment running since week of Aug 10. Pull early signal. You flagged IBK as too passive \u2014 is that changing?\n\u2022 *Fadi\u2019s Talent Pool designs:* Not in Linear yet. Engineers (Izzy) are blocked.\n\u2022 *Amplitude dashboard to Matan:* Overdue. Send it."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udca1 Manan, One Thing*\n\nYou did something great in this meeting: you pulled the data yourself in real-time ('I just checked \u2014 it\u2019s 99.5%') and it changed the entire conversation. That\u2019s the best kind of PM move. Keep leading with data like that and the team will keep trusting your calls."
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Sent by your Chief of Staff \u2022 Powered by Granola \u2022 Aug 19, 2026 EOD"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Daily Decision Summary \u2014 Aug 19, 2026"
}

token = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

def preview():
    sys.stdout.buffer.write(("\n" + "="*70 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("PREVIEW (no Slack token) \u2014 Aug 19 Daily Summary\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("="*70 + "\n\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("## " + block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("\n" + "="*70 + "\n").encode("utf-8", errors="replace"))

if not token:
    preview()
    print("\nNOTE: No Slack token found. Add SLACK_TOKEN (or SLACK_BOT_TOKEN) in Cursor Dashboard > Cloud Agents > Secrets.")
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        if result.get("ok"):
            print(f"SUCCESS: message posted to {CHANNEL} (ts={result.get('ts')})")
        else:
            print(f"SLACK ERROR: {result.get('error')}")
            preview()
            sys.exit(1)
except urllib.error.URLError as e:
    print(f"NETWORK ERROR: {e}")
    preview()
    sys.exit(1)
