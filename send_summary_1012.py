#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Oct 12, 2026 (Sunday Oct 11 CEST / Spain Day 10)
Manan Kothari - Senior PM, Homebase
Slack channel: D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f30d Sunday Night Spain Dispatch \u2014 Monday Oct 12 Battle Plan",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan \u2014 no meetings today (Sunday, rest well!), but tomorrow is one of the *most consequential Mondays of the quarter.* "
                "Carlo goes on paternity *Tuesday*. The board meeting window opens *this week*. "
                "Indeed is on *Day 50*. You have clear authority to act on all of it. Let's go.\n\n"
                "*Spain Day 10 \u2014 0 meetings \u2014 Monday blitz loading...*"
            )
        }
    },
    {"type": "divider"},

    # MONDAY ORDERS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f525 *MONDAY MORNING ORDERS (first 3 hours = 9am-12pm EDT / 3pm-6pm CEST)*\n"
                "Do these before anything else lands in your inbox:"
            )
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\u26a0\ufe0f #1 \u2014 Indeed: Email Jessica Kanaskie NOW*\n"
                    "jkanaskie@indeed.com \u2014 Day 50. Hypothesis confirmed via Kellie call: "
                    "AE65 unique identifier treating all customers as 'new' \u2192 manual review queue. "
                    "Send specific technical hypothesis + ask for manual expedite. "
                    "*This is the unlock.* Don't wait."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u26a0\ufe0f #2 \u2014 Give Skye your source name rollback recommendation*\n"
                    "She's expecting this Monday. Your call: rollback the AE65 source name change. "
                    "Frame it as: fastest path to restoring 50-day suspended feed. "
                    "Prepare for pushback on side effects \u2014 have your rationale tight."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u26a0\ufe0f #3 \u2014 SCHEDULE CARLO KT \u2014 TODAY*\n"
                    "Carlo\u2019s last day is TOMORROW (Tue Oct 14). "
                    "KT is critically unplanned. Block 2-3 hrs with Carlo *today*. "
                    "Focus: (1) AE65 source name change investigation, (2) Iterable 6 emails fix status, "
                    "(3) 'do not syndicate' bug, (4) continuation sizing handoff."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f4cb #4 \u2014 Verify Carlo fixed Iterable 6 emails*\n"
                    "He was on it EOW Oct 10. Check Slack/Linear for status. "
                    "If not done, surface it in your KT session TODAY before he's gone."
                )
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f4dd #5 \u2014 3-Year Vision One-Pager: ship a draft today*\n"
                    "Board meeting window opens Oct 15 (this week!). John assigned it. "
                    "It\u2019s overdue. Even a rough draft with your 3 bets is better than silence. "
                    "Think: 'Hire Smarter, Not Hire Faster' as the through-line."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 #6 \u2014 Confirm Rachel got Q4/Q1/Q2 UX view*\n"
                    "Was due Oct 7 \u2014 5 days overdue. Quick Slack ping: did it go out?"
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 #7 \u2014 Flip trial source claiming to 100%*\n"
                    "Decision made Oct 9. You own the experiment. Flip it. "
                    "Should take 15 minutes with eng. Do it."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 #8 \u2014 Standard Restaurant Supply SLC*\n"
                    "Follow up with Alexis (Indeed optimization team) \u2014 she was handling Mon/Tue. "
                    "Also check: equipment driver + merchandiser tickets status. "
                    "If no response by Wed Oct 14, escalate to Jessica Kanaskie thread."
                )
            }
        ]
    },
    {"type": "divider"},

    # CRITICAL WATCH LIST
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f6a8 *CRITICAL WATCH LIST (week of Oct 12)*"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *Indeed Day 50 \u2014 CRITICAL.* AE65 hypothesis confirmed. Rollback = fastest path. "
                "Second bug: fraud-flagged 'do not syndicate' jobs still syndicating (Bob/Carlo).\n"
                "\u2022 *Carlo leaves TUESDAY* \u2014 Q4 continuation sizing + all KT must happen TODAY.\n"
                "\u2022 *Board meeting Oct 15-22* \u2014 3-year one-pager is DUE. Draft now.\n"
                "\u2022 *Facebook API Day 28* \u2014 still failing. Bob + IBK. No update since Oct 9. Ping.\n"
                "\u2022 *Q4 Continuation Sizing* \u2014 needs Carlo present. Monday or bust.\n"
                "\u2022 *Orca Comms QA* \u2014 Matan built the skill, needs manual QA with IBK. Schedule.\n"
                "\u2022 *Ultraviolet data investigation* \u2014 API vs data lake. Rows 11, 35, 48 blocked on this.\n"
                "\u2022 *Row 38 Iterable workaround* \u2014 Share with Carlo in KT today.\n"
                "\u2022 *Omni/Looker access* \u2014 IT ticket, went dark Oct 2. 10 days overdue. Follow up.\n"
                "\u2022 *Indeed Duplicate Job Modal* \u2014 Get Fadi\u2019s design input before Tiger builds anything.\n"
                "\u2022 *Hire Smarter experiment* \u2014 Jon drafting 3-5 questions for sales. Review his draft.\n"
                "\u2022 *OTP Magic Link* \u2014 IBK starts implementation next sprint. Confirm with IBK today.\n"
                "\u2022 *Move Forward Label* \u2014 Fadi ships 'next week' (this week!). Check status."
            )
        }
    },
    {"type": "divider"},

    # OVERDUE / LINGERING
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u23f0 *OVERDUE \u2014 Cannot let these slide into week 2*\n"
                "\u2022 *Gift cards owed:* Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50) \u2014 just send them.\n"
                "\u2022 *John Waldman* \u2014 EarnBetter NDA + docs unsent.\n"
                "\u2022 *Marina \u2014 Mundo Academy* \u2014 26+ days late. One email.\n"
                "\u2022 *Departures Signal docs* \u2014 30+ days overdue. Zane, Sean, Jon W, Bobby. One session to close.\n"
                "\u2022 *IBK JD A/B signal* \u2014 3+ weeks overdue.\n"
                "\u2022 *Comms Assistant production decision* \u2014 Malcolm is out Nov\u2013Dec. Decide now."
            )
        }
    },
    {"type": "divider"},

    # WEEK AHEAD FRAMING
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f3af *WEEK OF OCT 12 \u2014 WHAT SUCCESS LOOKS LIKE*\n\n"
                "1\ufe0f\u20e3  Indeed source name rollback *decision locked* with Skye by EOD Monday\n"
                "2\ufe0f\u20e3  Carlo KT *complete* before he logs off Tuesday\n"
                "3\ufe0f\u20e3  Q4 continuation sizing *done* (Carlo\u2019s inputs captured)\n"
                "4\ufe0f\u20e3  3-year vision one-pager *draft shared* with John by Thursday\n"
                "5\ufe0f\u20e3  Trial source claiming experiment *at 100%*\n"
                "6\ufe0f\u20e3  Jessica Kanaskie email *sent by 10am EDT*\n"
                "7\ufe0f\u20e3  Competition Thursday Oct 15 \u2014 you\u2019ve earned it. Perform well. \U0001f4aa"
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
                "\U0001f1ea\U0001f1f8 *You\u2019re in Spain, drinking \u20ac2.30 wine, and still running one of the highest-impact PM workstreams at Homebase.* "
                "The team is counting on you for the Indeed recovery, the Carlo handoff, and the Q4 story. "
                "You know exactly what to do. Have a great espresso, cue up the battle playlist, and let\u2019s make this the week Indeed comes back online.\n\n"
                "_\u2014 Your Chief of Staff \U0001f91d_"
            )
        }
    }
]

FALLBACK = (
    "Spain Day 10 | Sunday Oct 11 | 0 meetings | Monday Oct 12 Battle Plan: "
    "(1) Email Jessica Kanaskie - Indeed Day 50 AE65 hypothesis; "
    "(2) Skye source name rollback recommendation; "
    "(3) Carlo KT ASAP - leaves Tuesday; "
    "(4) 3-Year One-Pager draft - board meeting this week; "
    "(5) Flip trial source claiming to 100%; "
    "(6) Verify Iterable 6 emails fixed."
)

payload = {
    "channel": CHANNEL,
    "text": FALLBACK,
    "blocks": BLOCKS
}


def preview():
    print("\n" + "=" * 70)
    print("SLACK MESSAGE PREVIEW (no token) \u2014 Oct 12 Chief of Staff Digest")
    print("=" * 70)
    print(f"Channel: {CHANNEL}")
    print(f"Fallback: {FALLBACK}")
    print("-" * 70)
    for block in BLOCKS:
        btype = block.get("type")
        if btype == "header":
            sys.stdout.buffer.write(("HEADER: " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            sys.stdout.buffer.write(("--- divider ---\n").encode("utf-8", errors="replace"))
        elif btype == "section":
            if "text" in block:
                sys.stdout.buffer.write(("SECTION: " + block["text"]["text"][:400] + "\n\n").encode("utf-8", errors="replace"))
            if "fields" in block:
                for f in block["fields"]:
                    sys.stdout.buffer.write(("  FIELD: " + f["text"][:300] + "\n").encode("utf-8", errors="replace"))
                sys.stdout.buffer.write(b"\n")
    print("=" * 70)
    print("PREVIEW ONLY \u2014 Slack token not set.")
    print("Add SLACK_TOKEN or SLACK_BOT_TOKEN to Cursor Dashboard > Cloud Agents > Secrets.")
    print("=" * 70 + "\n")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Slack message sent to {CHANNEL}. ts={body.get('ts')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if TOKEN:
        send()
    else:
        preview()
        sys.exit(0)
