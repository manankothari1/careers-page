#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Sep 8, 2026
OOO Return Dispatch: Manan's first day back (Labor Day was Sep 7)
No Granola meetings captured today (Heads Down Week Sep 7-11).
"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🏠 Welcome Back, Manan! — Chief of Staff Digest · Tue Sep 8",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "You crushed the OOO. Labor Day weekend is done and you're back for *Heads Down Week (Sep 7-11)*. "
                "No Granola meetings were captured today — but that doesn't mean nothing happened. "
                "Here's your full situational briefing to hit the ground running. Let's go. 💪"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🚨 CRITICAL — INDEED FEED SUSPENDED · Day 14*\n"
                "The Indeed feed has been suspended since Aug 25. Today is Day 14. "
                "The unlock path: package the fraud evidence → send to *Jessica Kanaskie* (jkanaskie@indeed.com) → 2-3 week review. "
                "David (Indeed Product) intro window opens *Sep 14-21* — don't miss it.\n"
                "*Action:* Finalize fraud evidence package with Divij (cleanup + score + OTP) and ship it to Jessica TODAY."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 TODAY'S FIRE ORDER (Priority Sequence)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1️⃣ Departures Signal Docs → Sales* _(OVERDUE since Sep 4)_\n"
                "Send conflict docs + data to Zane Williams, Sean Gohman, Jon Wanczyk ('J-Dubs'), Bobby Sladek. "
                "This was committed for Sep 4 — it's now 4 days late. This unlocks the sales motion.\n"
                "_Owner: Manan → Zane/Sean/Jon W/Bobby_\n\n"
                "*2️⃣ Fraud Evidence Package → Jessica (Indeed)* _(Unblocks feed — Day 14)_\n"
                "Coordinate with Divij on cleanup + score + OTP package. Send to jkanaskie@indeed.com. "
                "Every day of delay = another day of suspended traffic.\n"
                "_Owner: Manan + Divij → Jessica_\n\n"
                "*3️⃣ Confirm/Send 120-Day Flow Proposal → Skye* _(Committed before OOO)_\n"
                "The 120-day open job flow is LOCKED (removes 30-day auto-close, OEM prompt on close, fixes Indeed duplicate ID issue). "
                "Was committed to send to Skye BEFORE OOO. Confirm sent or send today.\n"
                "_Owner: Manan → Skye Laudari_\n\n"
                "*4️⃣ EarnIn Sample Feed → Jon Salzberg* _(OVERDUE since Aug 31)_\n"
                "jon.salzberg@earnin.com. 30M downloads, 750K users, 83% hourly workers — this is a real pipeline. "
                "8 days overdue. Send today.\n"
                "_Owner: Manan → jon.salzberg@earnin.com_\n\n"
                "*5️⃣ Chase Fadi on Copy+Reactivate Designs*\n"
                "Fadi was targeting Monday (Labor Day slipped it to today). Get an ETA on the designs. "
                "He's also starting Talent Pool SMS opt-in — get an update on that too.\n"
                "_Owner: Manan → Fadi Rizk (frizk@joinhomebase.com)_\n\n"
                "*6️⃣ Chase Divij + Sina: Role Normalization PRD* _(DUE was Sep 3 — 5 days OVERDUE)_\n"
                "This was due Sep 3 EOD. Chase them today.\n"
                "_Owner: Manan → Divij Gupta + Sina Salimian_\n\n"
                "*7️⃣ Pull IBK JD A/B Experiment Signal* _(2+ weeks OVERDUE)_\n"
                "The experiment has been running 2+ weeks. Pull the signal before V2 rolls out wider. "
                "This is blocking the JD V2 50/50 decision.\n"
                "_Owner: Manan_\n\n"
                "*8️⃣ Linear Tickets: Recency + Distance Experiments*\n"
                "File the Linear tickets for recency + distance — Divij is blocked on experiment coding until this happens.\n"
                "_Owner: Manan → Divij_\n\n"
                "*9️⃣ Chase Jatin on 422 RCA* _(Day 14, 146 locations)_\n"
                "Publishing errors have been happening since Jul 9 — 146 locations affected. "
                "Get Jatin's root cause analysis status today.\n"
                "_Owner: Manan → Jatin Bhandari_\n\n"
                "*🔟 Verify In-Product Termination Trigger* _(OVERDUE)_\n"
                "This intent signal is unverified. Chase down status.\n"
                "_Owner: Manan_"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 OOO PERIOD — WHAT HAPPENED WHILE YOU WERE GONE*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Indeed feed:* Still suspended — Day 14. No change. Path is clear: fraud evidence → Jessica → review.\n"
                "• *Talent Pool SMS opt-in:* Fadi was starting this while you were OOO. Get a status update.\n"
                "• *Copy+reactivate designs:* Fadi targeting Labor Day delivery → slipped to today (Sep 8).\n"
                "• *JobTarget:* Tyler Calvey one-pager still pending. Intro to Michael Doenmire (partnerships) still open.\n"
                "• *Indeed David intro:* Window opens Sep 14-21. Be ready.\n"
                "• *Carlo knowledge risk:* Team swarming agreed. Check in with Carlo on progress.\n"
                "• *Roadmap prompt update:* Was due Sep 4 EOD — confirm Matan's Vercel/Linear prompt was updated."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📡 WATCH LIST — Active Threads*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Power User Analysis* — OVERDUE. 90%+ started w/ Indeed/in-person. Chase and deliver to sales.\n"
                "• *Annual subscription cancel policy* — OVERDUE. Post in Hiring Leads channel.\n"
                "• *IBK OTP thread sign-off* — Pending your sign-off. Unblock today.\n"
                "• *Divij CSV spec for Iterable* — Blocking experiment coding.\n"
                "• *Amplitude + Databricks dashboards* — Indeed account setup flow. Nelson to build.\n"
                "• *Source Claim tracking table* — Manan action item. Still open.\n"
                "• *Marina / Mundo Academy* — Follow up window is *Sep 10 (2 days)*. Don't let it slip.\n"
                "• *Matan → Greg meeting* — Week of Sep 1. Confirm it happened and get a debrief.\n"
                "• *#hiring-epdd channel* — Confirm Jatin created it.\n"
                "• *Careers page A/B test with Jon* — Not started. Get on calendar during Heads Down Week.\n"
                "• *OTP copy update (Iszael)* — Expand to free-tier; exempt paying customers.\n"
                "• *Google crawling careers pages* — Should be live ~Sep 10. Check indexing status."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 CALENDAR RADAR*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Sep 7-11* → Homie Heads Down Week (light meetings — use this time well)\n"
                "• *Sep 10* → Marina/Mundo Academy follow-up deadline\n"
                "• *Sep 14-18* → Dreamforce WFH optional (SF office)\n"
                "• *Sep 14-21* → Indeed David intro window (source claiming — don't miss)\n"
                "• *Sep 14-17ish* → Skye Toronto trip\n"
                "• *Sep 18-21* → 🏕️ *YOSEMITE* (Diamond O Campground) — block your calendar NOW if not done"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Q3 SCOREBOARD (as of Sep 4 EOD)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• FFH D5 zero-applicant rate: *41%* → target <10% _(long way to go, experiments unblocking)_\n"
                "• Line cook jobs healthy by D30: *~7%* → target 50%\n"
                "• Indeed account setup experiment: *LIVE* — 30% nothing / 50% standard / 20% Indeed setup\n"
                "• Source claiming pilot: *LIVE* at 20%\n"
                "• Talent Pool: 231K active\n"
                "• ARR: *$650K+* (from $450K Jan 2026 — great trajectory 💪)\n"
                "• 422 errors: 146 locations, Day 14+"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Chief of Staff Assessment:* Manan, you left on a strong note — "
                "the Indeed account setup experiment went live, 120-day flow got locked, Talent Pool SMS got greenlit. "
                "The OOO was earned. Now it's time to execute: the Indeed feed is the biggest fire "
                "and the fraud evidence package is the key. Ship that first. Everything else flows from there. "
                "You've got this. Week grade for last week: *A*. Let's make this week another one. 🚀"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest · Sep 8, 2026 · Homebase Product · No Granola meetings captured today (Heads Down Week) · OOO Return Edition"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Digest — Sep 8, 2026 (OOO Return Edition)",
    "blocks": blocks
}


def preview():
    out = []
    out.append("\n" + "=" * 70)
    out.append("CHIEF OF STAFF DIGEST — SEP 8, 2026 (OOO RETURN EDITION)")
    out.append("=" * 70)
    for block in blocks:
        if block["type"] == "header":
            out.append("\n### " + block["text"]["text"])
        elif block["type"] == "section":
            out.append("\n" + block["text"]["text"])
        elif block["type"] == "divider":
            out.append("-" * 60)
        elif block["type"] == "context":
            for el in block["elements"]:
                out.append("\n[context] " + el["text"])
    out.append("\n" + "=" * 70)
    sys.stdout.buffer.write(("\n".join(out)).encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


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
        print(f"✅ Slack message sent successfully to {CHANNEL}")
        print(f"   ts: {result.get('ts')}")
    else:
        print(f"❌ Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"❌ Network error: {e}")
    preview()
    sys.exit(1)
