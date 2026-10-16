#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Oct 15 CEST (Day Off + Competition Day)
Cron fired: midnight UTC Oct 16 → reviewing Oct 15 Spain workday.
0 meetings captured or workspace-visible (Manan out Thu+Fri).
"""

import sys
import json
import os
import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f3c6 Chief of Staff — Thu Oct 15 Digest",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day Off \u2014 You Earned It!* \U0001f3cb\ufe0f\n"
                "No meetings today (you blocked Thu+Fri). Zero Granola notes, zero workspace calls. "
                "Go absolutely *destroy* that competition. You've had an A-grade week \u2014 "
                "this is your victory lap. \U0001f947"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f525 *MONDAY OCT 19 BATTLE PLAN \u2014 26/23 Look-Ahead Day*\n"
                "_This is the most important day of the sprint cycle. Here's what you need to walk in ready for:_"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\u26a0\ufe0f CRITICAL \u2014 First 30 Minutes Monday Morning:*\n"
                "1\ufe0f\u20e3  *Indeed Feed \u2014 Day 54 Suspended.* "
                "Ping Ashley first thing: did she give Bob the green light to merge the source name rollback PR? "
                "Bob should NOT merge until she confirms T&S approval. "
                "If merged \u2714, circle back with Jessica Kanaskie on multi-location source claiming.\n"
                "2\ufe0f\u20e3  *Indeed Partner Console \u2014 Tiger.* "
                "Follow-up was sent to Marketplace Support Oct 14. Tiger CC'd. "
                "If no response by now \u2192 escalate.\n"
                "3\ufe0f\u20e3  *3-Year Vision One-Pager.* "
                "Board meeting opened Oct 15. This was NOT mentioned in any meeting all week. "
                "Do you have a draft? If not, block 90 min Monday AM before Look-Ahead."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4cb 26/23 Look-Ahead Prep Checklist:*\n"
                "\u2022 Spec steps 1-8 ready for review\n"
                "\u2022 Fadi low-fi ready\n"
                "\u2022 Divij sync on Q4 TS priorities (he's been waiting)\n"
                "\u2022 Carlo KT gap \u2014 have you done async Slack/doc? "
                "Risk items: AE65 source name change, Iterable 6 emails fix, 'do not syndicate' bug, continuation sizing.\n"
                "\u2022 Pending syndication data split \u2014 initial thinking ready?\n"
                "\u2022 Syndication timing requirements + viz draft for Jatin"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f4ca *This Week's Wins (Oct 13-15 CEST):*\n"
                "\u2705 *21-Day Job Post Matrix LOCKED* \u2014 Tiger implementing. "
                "Extend=same ID, <21 days=reopen, >21 days=new Indeed post. Clean.\n"
                "\u2705 *Indeed Source Name Root Cause CONFIRMED + Rollback PR RAISED* \u2014 Bob's PR is up. Ashley met T&S Oct 14. One confirm away from fixing Day 53+ suspension.\n"
                "\u2705 *Source of Hire Attribution SCOPED* \u2014 fuzzy/LLM out, exact 2-of-3 field match in. Right call.\n"
                "\u2705 *Q4 Scope FINALIZED* \u2014 cuts made, swarm model locked, N+2 cadence live.\n"
                "\u2705 *Discovery Format LOCKED* \u2014 Wednesday weekly, product owns agenda, Matan optional.\n"
                "\u2705 *Match Explanation Workshop PLANNED* \u2014 FigJam, next Discovery slot, Skye+Bob+Matan.\n"
                "\u2705 *Intent Capture = Design Exploration* \u2014 Skye's call, scope right-sized."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u23f0 *Overdue Items That Need You Monday:*\n"
                "\u2022 *Rachel Q4/Q1/Q2 UX view* \u2014 due Oct 7. Did it go out? Confirm.\n"
                "\u2022 *Prompt chips min wage* \u2014 write the MD file + ping Justin this sprint.\n"
                "\u2022 *Discovery block for Match Explanation Workshop* \u2014 book it. Invite Skye, Bob, Matan.\n"
                "\u2022 *Indeed release blocker* \u2014 identify right Indeed contact for arch review. Tiger to join. Must resolve before job posting ships.\n"
                "\u2022 *Facebook API \u2014 Day 21.* Bob + IBK. Last update Oct 9. Ping.\n"
                "\u2022 *Comms Assistant production decision* \u2014 Malcolm leaving Nov-Dec. Clock is ticking.\n"
                "\u2022 *Omni access* \u2014 Looker went dark Oct 2. Ping IT.\n"
                "\u2022 *Gift cards owed:* Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50)."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f4c5 *Week Ahead Snapshot:*\n"
                "*Mon Oct 19* \u2014 26/23 Look-Ahead (first thing!)\n"
                "*Wed Oct 23* \u2014 Discovery (block for Match Explanation Workshop)\n"
                "*Fri Oct 23-ish* \u2014 Town Hall (submit Q&A questions by Mon)\n"
                "*Board Meeting* \u2014 team traveling to SF next week (3-year one-pager MUST be ready)"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f916 *Your Chief of Staff Says:*\n"
                "You locked a massive amount of scope and process this week from Spain. "
                "The Indeed rollback is one Slack message from Ashley away from resolving a 54-day suspension. "
                "The 21-day matrix is clean. Q4 is tight. The team knows what to build.\n\n"
                "Now go WIN. \U0001f947\n"
                "_See you Monday, Senior PM. Let's go._"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff digest \u2022 Oct 15 CEST \u2022 0 meetings (day off) \u2022 Indeed Day 54 \u2022 Facebook API Day 21"
            }
        ]
    }
]

payload = {
    "channel": SLACK_CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Digest \u2014 Thu Oct 15 (Day Off + Competition Day)"
}


def preview():
    sys.stdout.buffer.write(
        ("\n=== SLACK PREVIEW ===\n" + json.dumps(payload, indent=2, ensure_ascii=False) + "\n=== END PREVIEW ===\n").encode("utf-8", errors="replace")
    )


def send(token: str):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"[OK] Message sent to {SLACK_CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {result.get('error')}")
                preview()
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        preview()


token = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

if token:
    send(token)
else:
    print("[PREVIEW] No SLACK_TOKEN found \u2014 printing preview only.")
    preview()
