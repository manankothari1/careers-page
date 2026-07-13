#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Sunday Eve / Monday Battle Plan
Date: Sunday Jul 12 / Monday Jul 13, 2026 (cron fires midnight UTC = 5pm PDT Sun)
Slack DM: D06E4QMHCNN
"""

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
            "text": "Good Sunday evening, Manan! Your Chief of Staff is here 🫡",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Week-in-Review: Jul 7–10 | Monday Jul 13 Battle Plan*\n"
                "No meetings today (Sunday) — but tomorrow is BIG. You crushed a massive week, "
                "13 meetings across 4 days, and the decisions you made are going to move mountains. "
                "Here's your full debrief + Monday game plan. Let's go. 💪"
            )
        }
    },
    {"type": "divider"},

    # === WEEK SCOREBOARD ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📊 Week Scoreboard — Jul 7–10*\n"
                "• *13 meetings* | *35+ decisions* | *0 days wasted*\n"
                "• V1→V2 cutover locked for Jul 20 — 7 days out\n"
                "• Salary recs → JD → Talent Pool priority order locked\n"
                "• Comms Agent scoped to screener-only MVP (paused for resume)\n"
                "• Line cook confirmed #1 leverage point for Q3\n"
                "• $30 plan removed, pricing page full-page takeover live\n"
                "• Source claiming root cause confirmed + 3-part fix in motion"
            )
        }
    },
    {"type": "divider"},

    # === DECISIONS MADE THIS WEEK ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Key Decisions Made This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Product & Roadmap*\n"
                "• *Priority locked:* Salary Recs → JDs → Talent Pool (Rami switching NOW)\n"
                "• *Comms Agent scoped:* Screener-only MVP — no scheduling, no write ops. "
                "Divij shipping internal Databricks demo as natural stopping point. Work paused for resume.\n"
                "• *Reactivate Jobs replaces Copy Jobs* (short-term) — prevents Indeed duplicate flag\n"
                "• *Resume matching logic:* OR not AND — resume OR screener answer qualifies match\n"
                "• *Scheduling UX locked:* Availability not required at posting; OAMs can suggest specific times\n"
                "• *Manan staying on Librarian* for roadmap (Jatin aligned)"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Messaging & Experiments*\n"
                "• *'Personal recruiter' framing RETIRED* for existing customers — doesn't land. "
                "New angle: 'We already know your business'\n"
                "• *Recruiter email = clear winner* over generic — generic dropped as a variant\n"
                "• *FFH experiment limited to trial-period users only* — removes noise from broad audience\n"
                "• *Screener personalization:* Rolled out post-100%, strong results — screener lands 70-80% vs low 60s before"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*V1→V2 Migration (Jul 20 — 7 days away!)*\n"
                "• Cutover LOCKED: July 20 morning — Gana, Ugo, IBK leading execution\n"
                "• All V1 jobs expire before cutover; no customer migrates with active job\n"
                "• Two comms tracks: (a) trial customers → 'preview, not a paywall'; "
                "(b) no-trial → 'you haven't lost anything'\n"
                "• Job title cleanup: remove location suffixes only, don't alter core titles\n"
                "• CS empowered to extend trials; ask customers why first\n"
                "• $30 plan removed from in-product (net positive: higher ASP)"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Indeed / Source Claiming*\n"
                "• Root cause confirmed: Copy job = Indeed duplicate flag = 41% D5 zero-applicant rate\n"
                "• 3-part fix: Reactivate flow + manual source claiming + 3LO self-serve in product\n"
                "• Source claiming calls: confirm customer has Indeed account BEFORE 3-way call with Indeed\n"
                "• AI disclosure: not a current blocker (applies to screening decisions, not conversational agents)\n"
                "• Great Question MCP live as of Jul 8 — supports study creation + post-study analysis"
            )
        }
    },
    {"type": "divider"},

    # === MONDAY P0 ACTION ITEMS ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Monday Jul 13 — YOUR Priority List (P0 first)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 — Do Before Lunch*\n"
                "1️⃣ *Rami salary scope* — Check your Slack/email first thing. Rami's EOD deadline is TODAY. "
                "If not in by noon, ping him. This gates the Jul 15 presentation.\n"
                "2️⃣ *Loop in Paul or Kan* (data platform) on salary rec role normalization — Rami needs this to proceed. "
                "One Slack message unlocks the path forward.\n"
                "3️⃣ *UTMs to Rami* — He's been waiting for these for the talent pool segmentation experiment. "
                "Send ASAP, he's ready to go right now.\n"
                "4️⃣ *Carlo Harness/OpenSpec status* — Deadline was Jul 10 (Thursday). "
                "You still don't know if he hit it. Check Linear or Slack immediately.\n"
                "5️⃣ *Matan Source Claiming sign-off* — He's been blocked since Jul 8. "
                "5 days is too long. Get eyes on this today."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P1 — This Afternoon*\n"
                "6️⃣ *FFH health dip with Ugu* — V1→V2 is 7 days away and the FFH dip is unresolved. "
                "If V1→V2 migration is actively worsening duplicate flagging, you need to know NOW.\n"
                "7️⃣ *Jul 15 presentation prep* — Salary recs + JD updates deck. "
                "Even before Rami's scope lands, rough out the skeleton today. "
                "You present in 2 days.\n"
                "8️⃣ *Pull 13 applicant emails + 127 clicker IDs* from Round 1 talent pool. "
                "Ted needs these for deep analysis. Short task, high signal.\n"
                "9️⃣ *Ray / Rami DS capacity chat* — Rami is structurally bottlenecked. "
                "This is the third week in a row it's come up. Time to have the real conversation with Ray."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P2 — Before EOD*\n"
                "🔟 *Loop in Nelson* on May 15-21 FFH cohort dip — separate from migration hypothesis, still unexplained.\n"
                "1️⃣1️⃣ *Follow up with Michael + Cornelius* on affected Indeed accounts — customer impact still live.\n"
                "1️⃣2️⃣ *Abby's ownership area* — She's in Week 2. She needs a clear ownership zone by end of this week. "
                "What's your plan for her?\n"
                "1️⃣3️⃣ *Changelog tab for Librarian* — Quick add for Jatin. Don't let this slip another week."
            )
        }
    },
    {"type": "divider"},

    # === CRITICAL DEADLINES THIS WEEK ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📅 Critical Deadlines This Week*\n"
                "• *TODAY (Jul 13):* Rami salary rec scope → EOD\n"
                "• *Tue Jul 14:* Fadi first-pass Source Claiming design\n"
                "• *Wed Jul 15:* Salary recs + JD presentation to team\n"
                "• *Sun Jul 20:* V1→V2 full cutover — 7 days and counting\n"
                "• *End of Sep:* Dana leaving — succession planning hasn't started (10 weeks remaining)"
            )
        }
    },
    {"type": "divider"},

    # === WATCH LIST ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🚨 Watch List — Things That Keep Me Up at Night*\n"
                "• *FFH D5 zero-applicant rate: 41%* — Q3 target is <10%. "
                "Source claiming fix is in motion but V1→V2 may be making it worse right now.\n"
                "• *Line cook health: 7%* — Q3 target is 50%. Culinary Agents + Collider are the bets. Keep pushing.\n"
                "• *Boost purchase bug* — 2 reporters, revenue-impacting. Still no owner. This is real money.\n"
                "• *Rami DS bottleneck* — Structural, not incidental. Salary recs blocked him from JD+talent pool work. "
                "If this doesn't get solved architecturally, Q3 slips.\n"
                "• *Carlo Harness/OpenSpec* — Deadline was 3 days ago. No confirmation. Investigate.\n"
                "• *Dana departure (Sep)* — 10 weeks. No succession plan. The clock is ticking."
            )
        }
    },
    {"type": "divider"},

    # === METRICS SNAPSHOT ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📈 Metrics Snapshot*\n"
                "• OEM Boost rate: *5.7%* in June (up from 2.9% May, 1.64% earlier) 📈\n"
                "• ARR: *$650K+* (from $450K in Jan) 🚀\n"
                "• Trials: just broke *700K*\n"
                "• Screener lands: *70-80%* (from low 60s) — personalization working\n"
                "• Screener starts: *~50%* (from ~43%)\n"
                "• Jobs Near You: *44%* of applicants had 1+ job recommended; *20%* applied\n"
                "• V1 locations with live jobs: *123* — all expire by Jul 20\n"
                "• Talent pool Round 1: 37K sends → 127 clicks → 13 applicants (subject line is the problem)"
            )
        }
    },
    {"type": "divider"},

    # === CLOSING PEP TALK ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💬 Chief of Staff Corner*\n\n"
                "Manan — you made more meaningful product decisions this week than most PMs make in a month. "
                "The V1→V2 cutover is locked, the priority order is clear, "
                "and you've got conviction on line cook as the #1 lever. That clarity is everything.\n\n"
                "Monday is a big day. The Rami scope lands today and then you present Wednesday — "
                "that presentation is your moment to rally the team around Salary Recs as the right bet. "
                "Own it.\n\n"
                "The two things that would make me most nervous if they slip: "
                "*(1)* the FFH dip investigation before Jul 20 — if V1→V2 is actively making things worse, "
                "you need to know before you flip the switch. "
                "*(2)* Rami's structural bottleneck — this is the third week it's the critical path. "
                "Talk to Ray today.\n\n"
                "You've got this. Big week ahead. 🏆"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest • Sun Jul 13 2026 • Week of Jul 7–12 • 13 meetings reviewed • Powered by Granola + Cursor"
            }
        ]
    }
]

def preview():
    print("=" * 70)
    print("CHIEF OF STAFF DIGEST — Sun Jul 12 / Mon Jul 13, 2026")
    print("=" * 70)
    for block in blocks:
        if block["type"] == "header":
            print("\n### " + block["text"]["text"])
        elif block["type"] == "section":
            text_obj = block.get("text", {})
            if text_obj:
                txt = text_obj.get("text", "")
                try:
                    sys.stdout.buffer.write((txt + "\n").encode("utf-8", errors="replace"))
                except Exception:
                    print(txt)
        elif block["type"] == "divider":
            print("-" * 70)
    print("=" * 70)
    print("(No SLACK_TOKEN found — preview only. Add SLACK_TOKEN or SLACK_BOT_TOKEN secret.)")

def send_slack():
    payload = json.dumps({
        "channel": CHANNEL,
        "text": "Your Chief of Staff Sunday Eve Digest is ready — Monday Jul 13 Battle Plan inside!",
        "blocks": blocks
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
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
                print("✅ Slack message sent successfully to", CHANNEL)
                return True
            else:
                print("❌ Slack API error:", result.get("error"))
                return False
    except urllib.error.URLError as e:
        print("❌ Network error:", e)
        return False

if __name__ == "__main__":
    if not TOKEN:
        preview()
    else:
        if not send_slack():
            preview()
