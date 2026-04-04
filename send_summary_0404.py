#!/usr/bin/env python3
"""Daily decision summary for Manan — Apr 4, 2026 (reviewing Apr 3 meetings)."""
import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌅 Your Daily Wrap-Up — Friday, April 3, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! You crushed it today. Here's everything you decided, what it means, and exactly what needs to happen next. Let's get into it 👇"
        }
    },
    {"type": "divider"},

    # ── MEETING ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Meetings Today (1)*\nHiring Leads Standup — 8:30 AM  |  Fadi, Dana, Matan, Bob, Jatin, Nelson, Jeff"
        }
    },
    {"type": "divider"},

    # ── DECISIONS ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1️⃣  Kill CommandAI — Migrate to Amplitude Journeys*\n"
                ">*Decision:* No new nudges in CommandAI, effective immediately. Amplitude \"Journeys\" is the replacement. CommandAI sunsets end of April.\n"
                ">*Why:* Amplitude provides better engagement tracking and (reportedly) easier nudge creation via their native platform. The team bought CommandAI but Amplitude owns the full stack — consolidating makes sense.\n"
                ">*Risk to watch:* Nobody has actually shipped a nudge in Amplitude yet — this is pressure-testing next week. If Journeys turns out to be clunky, you'll need a fallback plan before the April 30 cutoff.\n"
                ">📎 <https://notes.granola.ai/d/0353db8f-fc0d-42aa-86e1-aa45f30ba1a3|Meeting notes>"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2️⃣  Sprint feedback from Ray & Dana flagged as a real problem*\n"
                ">*Decision:* You agreed this concern deserves a dedicated sync with Fadi — not a standup item.\n"
                ">*Why:* If the team is starting a new sprint and feels nothing has changed, that's a process/communication failure that'll compound. You identified it early, which is great.\n"
                ">*What it unlocks:* Addressing this proactively protects sprint momentum for launch week and prevents morale from sliding into the weekend."
            )
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Your Action Items (owned by you)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Sync with Fadi on sprint concerns* — Ray + Dana's feedback that \"nothing has changed\" needs a real conversation. Get on a call before Monday's squad sync so you can show up with a response.\n"
                "• *Review Matan's 3 prototypes + Topical Workplace prototype* — he's sharing today; you gave detailed feedback that he found valuable. Keep the momentum going with a quick reply.\n"
                "• *Watch the Amplitude Journeys intro deck* — familiarize yourself before next week's pressure test so you can unblock the team if they hit walls."
            )
        }
    },
    {"type": "divider"},

    # ── TEAM ACTIONS TRACKING ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👥 Team Actions to Track (they own it, you watch it)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Matan Chen Zion* — Share 3 prototypes + topical workplace prototype *today*. Create next week's nudges in Amplitude, not CommandAI.\n"
                "• *Team* — Pressure-test Amplitude Journeys with the new release nudges *next week*."
            )
        }
    },
    {"type": "divider"},

    # ── CARRY-FORWARD OVERDUE ITEMS ────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Overdue / Still Burning — Don't Let These Slide into Next Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *TLWA/Launch Week brief → Ted* — Was due end of Wed Apr 2. This is *blocking Ted*. Send ASAP.\n"
                "• *Jeff's Indeed 3LO prototype* — Jeff was to share before lunch Apr 3. Did you review? If not, review + send to team Monday AM.\n"
                "• *Generic Roles proposal doc* — Write both options (job-request-per-location + is_generic_role flag) and recommend. Needed for alignment.\n"
                "• *Homebase Boost SKU kick-off w/ Chris McIntosh* — CRITICAL. Billing needs 3-week lead for Early May launch. Every day this slips is a day off the runway.\n"
                "• *Manual Mode green light* — Cindy QA is done. This is on *you*. Greenlight it.\n"
                "• *Andrew 3LO spike review + email Kenneth + add Ray* — Still outstanding from earlier this week.\n"
                "• *Applicant flow brief + prototype* — Overdue since Mar 25. Either set a hard date or make a descope decision.\n"
                "• *Supabase tables + 60k upsert* — You're building, Nelson validates. Where does this stand?\n"
                "• *Divij mentorship* — Schedule Ted + Dana session; align with Ted Monday."
            )
        }
    },
    {"type": "divider"},

    # ── WEEKEND SETUP ─────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🎯 Set Yourself Up for a Strong Monday*\n\n"
                "Top 3 things to do *before* Monday's squad sync:\n"
                "1. Send the TLWA/Launch Week brief to Ted — unblock him going into the weekend.\n"
                "2. Sync with Fadi on sprint concerns — show up Monday with a plan, not a problem.\n"
                "3. Greenlight Manual Mode — Cindy's done her part, the ball is in your court.\n\n"
                "You've got a lot of threads in flight but you're navigating them well. Enjoy the weekend, Manan — you earned it. 💪"
            )
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Wrap-Up — Friday, April 3, 2026",
    "blocks": blocks
}

def send_slack_message(payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print("✅ Slack message sent successfully!")
            else:
                print(f"❌ Slack API error: {result.get('error')}")
                print(json.dumps(result, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")

if __name__ == "__main__":
    if not SLACK_TOKEN:
        print("⚠️  SLACK_TOKEN not set — printing preview instead:\n")
        print("=== SLACK MESSAGE PREVIEW ===")
        for block in blocks:
            if block.get("type") == "section":
                text_obj = block.get("text", {})
                print(text_obj.get("text", ""))
                print()
            elif block.get("type") == "header":
                print(f"# {block['text']['text']}")
                print()
            elif block.get("type") == "divider":
                print("---")
        print("=== END PREVIEW ===")
    else:
        send_slack_message(payload)
