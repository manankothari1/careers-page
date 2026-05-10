#!/usr/bin/env python3
"""
Chief of Staff Daily Summary — Sunday May 10, 2026
No recorded meetings today (weekend). Sending Sunday Night Battle Plan.
Slack channel: D06E4QMHCNN
"""

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
            "text": "🌙 Sunday Night Battle Plan — Week of May 11",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Happy Sunday, Manan! No meetings logged today — which means you get this space entirely to yourself to prep. Tomorrow is *one of the most consequential Mondays of the quarter.* Here's everything you need to walk in locked and loaded. Let's go. 💪"
        }
    },
    {
        "type": "divider"
    },
    # ─── MONDAY MAY 11 ────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Monday May 11 — What's On Deck*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *9:00 AM PT* — 🔑 *6-Week Planning Call w/ Martin* (+Jatin, +Ray). "
                "This is your first strategic alignment moment with your new EM. First impressions matter.\n"
                "• *Morning* — Sprint 2611 kickoff. Engineers are back (had Friday off). Set the tone.\n"
                "• *Today* — 🚀 *Boost Pathways Marketing Launch* goes live. Make sure Cindy's assets are ready.\n"
                "• *TBD* — TLWA demo: decide today whether it moves to the sprint kickoff or stays in May 22 Show & Tell."
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── 6-WEEK PLANNING CALL PREP ────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 9am PT Call Prep — Martin / Jatin / Ray*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Martin is a 30-year vet (ex-1Password, ex-Meta AI/ML). He wants *spec-driven development* "
                "leading to agentic workflows. He's been Toronto-based all week (Denver travel Mon–Thu). "
                "Come in with crisp priorities — he respects precision.\n\n"
                "*Recommended talking points:*\n"
                "• 2611 scope is locked: Sponsored Jobs API spike, Boost Modal upgrade, Full-page Boost post-creation, Smart Suggestions\n"
                "• 75/25 capacity split: 75% product priorities, 25% KTLO/quality (engineer self-select)\n"
                "• Team structure: two squads (Dana AM, Manan PM); each PM sole gatekeeper\n"
                "• Carlo → Manan's team (effective this sprint)\n"
                "• Bob newly promoted: oversees Hiring + Distribution engineering; delegates Malcolm (Dana) and Izzy (Manan)\n"
                "• EM hire: actively searching; SF candidates now approved\n"
                "• Engineering morale: two-squad structure + tight sprints is the fix — show confidence\n"
                "• Key 6-week arc: 2611 (Boost/Sponsored Jobs) → 2612 → 2613 look-ahead\n\n"
                "*What to ask Martin:*\n"
                "• His preferred sprint review cadence (weekly? bi-weekly?)\n"
                "• His take on spec-driven workflow rollout timeline\n"
                "• How he wants to be looped in on vendor decisions (Nihilist, Talroo, etc.)"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── SPRINT 2611 KICKOFF ──────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏃 Sprint 2611 Kickoff — Locked Scope*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Sponsored Jobs API* — Bob owns the engineering spike. "
                "Purchase UX design needs to be Indeed brand-aligned.\n"
                "*2. Boost Modal Upgrade* — Visual treatment to drive conversion (baseline: 0.5% of job posters boost). "
                "Matan owns plan; remind him to post to #leads + survey customers (OVERDUE since Apr 23).\n"
                "*3. Full-page Boost after job creation* — Test Day 1 timing. "
                "Sales-led test also queued: Day 2–3 after post with <5 applicants → Usman calls.\n"
                "*4. Smart Suggestions* — In-flow job title + wage rate recommendations.\n\n"
                "_Predicted Roles is handed to Dana — send her Figma links + spec doc TODAY if not already done._"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── THIS WEEK'S CALENDAR ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🗓 Week Ahead at a Glance*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Mon May 11* — 9am PT Martin call · Sprint 2611 kickoff · Boost Pathways launch 🚀\n"
                "• *Wed May 13* — 15-min 2611 planning touchpoints w/ leads (Fatty→Dana, Matan/Usman optional→Manan's squad) · "
                "Cindy sync (*data pulls must be ready — see below*)\n"
                "• *Thu May 14* — Boost Pathways review (Carlo flagged: ready for your eyes)\n"
                "• *Fri May 15* — Martin/Manan 1:1 follow-up\n"
                "• *May 22* — Customer Connection Challenge Show & Tell (TLWA + Deal Breakers + Calendar)\n"
                "• *May 25+* — Cindy PTO in BC — all design feedback must be *closed before this date*\n"
                "• *May 29–31* — Dana + Fatty in SF (Ted joining)"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── DATA PULLS — URGENT ──────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Data Pulls — Must Be Ready Before Wednesday Cindy Sync*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Nelson is OOO 2 weeks (analytics team critically short-staffed). "
                "Queue these with Vlad *first thing Monday:*\n"
                "• Boost funnel drop-off % (where are users bailing?)\n"
                "• Indeed purchase options data\n"
                "• Job title quality % (feeding Smart Suggestions design)\n"
                "• Wage vs. applicants correlation\n\n"
                "_Emergency contact for analytics: Vlad. Ray also providing markdown documentation support._"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── TOP ACTION ITEMS ─────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Top Action Items — Clear Before EOD Monday*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":red_circle: *Send Dana: Predicted Roles Figma links + spec doc* — promised this weekend\n"
                ":red_circle: *Review Boost Pathways* before Thu (Carlo flagged it's ready)\n"
                ":red_circle: *Queue data pulls with Vlad* — Boost funnel, Indeed, job title quality, wage/applicants\n"
                ":large_yellow_circle: *Confirm Carlo's 2611 ticket assignments* with Dana (he's now on Manan's team)\n"
                ":large_yellow_circle: *Confirm IBK assigned* to 3 UX bug fixes (Dana owns 'Core product 2610 UX fixes' project)\n"
                ":large_yellow_circle: *Brief Bob* on Sponsored Jobs API spike scope + Indeed design constraints\n"
                ":large_yellow_circle: *EM hire*: share JD + criteria with Jatin; confirm SF budget approved\n"
                ":large_yellow_circle: *Nihilist*: confirm Joseph resolves $6K billing dispute; redirect vendor alerts → hiring-support@joinhomebase.com\n"
                ":large_yellow_circle: *Confirm Malcolm's paternity leave dates* with Dana\n"
                ":large_yellow_circle: *Decide TLWA demo placement* — sprint kickoff vs. May 22 Show & Tell\n"
                ":white_circle: Bob 1:1: set expectations for his strategic technical leadership role\n"
                ":white_circle: Matan: post Boost plan to #leads + survey customers *(OVERDUE since Apr 23)*\n"
                ":white_circle: Saja (Talroo): confirm CPA categories + campaign configured\n"
                ":white_circle: Indeed ATS survey: check email, respond immediately\n"
                ":white_circle: TLWA brief to Ted: confirm if sent\n"
                ":white_circle: Vibe pilot: Fadi needs Slack app approval from Joseph (blocker)\n"
                ":white_circle: Engineering morale message: confirm sent post-TLWA"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── KEY DECISIONS RECAP FROM MAY 8 ──────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Last Week's Big Calls — Friday May 8 Recap*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Here's what got decided Friday so it's fresh walking into Monday:\n\n"
                "• *Carlo → Manan's team* — moves to applicant flow squad for 2611\n"
                "• *Jason Noble terminated; Bob promoted* — now oversees Hiring + Distribution engineering\n"
                "• *EM hire approved* — SF candidates in scope; share JD + criteria with Jatin\n"
                "• *Malcolm: 2-week paternity leave* (not full month; dates TBD)\n"
                "• *Predicted Roles → Dana* for Sprint 2611 (fully designed, Figma-ready)\n"
                "• *3 UX bug fixes* → 'Core product 2610 UX fixes' project (IBK assigned, Dana owns)\n"
                "• *Wednesday 2611 planning sessions confirmed* — 15-min touchpoints with leads\n"
                "• *Sponsored Jobs API spike → Bob* — kicks off 2611\n"
                "• *Nihilist billing crisis* — $6K dispute; Joseph handling; vendor inventory sheet created\n"
                "• *Show & Tell format locked* — TLWA + Deal Breakers + Calendar (no 'how we work' repeat)\n"
                "• *Nelson OOO 2 weeks* — analytics critically short; escalate to Vlad\n"
                "• *Monday 9am PT planning call with Martin* — you're already prepped above ☝️"
            )
        }
    },
    {
        "type": "divider"
    },
    # ─── MORALE PULSE ─────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💙 Team Pulse*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "The team just crushed TLWA (800K users, 55K locations launched). "
                "They got Friday off as a thank-you from Ray + Martin — they've *earned* this sprint start. "
                "Come in Monday with energy and gratitude. Name the wins. They're ready to build.\n\n"
                "Watch list: Fadi + Dana (burnout signals). Two-squad structure + tight sprints is the cure — "
                "but make sure they feel the new structure is relief, not more complexity."
            )
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*You've got this, Manan.* 🚀 TLWA is live, the team is energized, "
                "and Sprint 2611 is locked with a real thesis. Monday is yours — go lead."
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot · Sunday May 10, 2026 · No meetings today (weekend) · Based on May 8 decisions + open items"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Sunday Night Battle Plan — Week of May 11",
    "blocks": blocks
}


def preview():
    sys.stdout.buffer.write(b"\n=== SLACK MESSAGE PREVIEW ===\n")
    sys.stdout.buffer.write(b"Channel: D06E4QMHCNN\n")
    sys.stdout.buffer.write(b"Text: Sunday Night Battle Plan -- Week of May 11\n\n")
    for block in blocks:
        if block.get("type") == "header":
            line = "HEADER: " + block["text"]["text"] + "\n"
            sys.stdout.buffer.write(line.encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            text = block["text"]["text"]
            line = text + "\n\n"
            sys.stdout.buffer.write(line.encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                line = "[context] " + el.get("text", "") + "\n"
                sys.stdout.buffer.write(line.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n")


def send():
    token = (
        os.environ.get("SLACK_TOKEN")
        or os.environ.get("SLACK_BOT_TOKEN")
        or os.environ.get("SLACK_API_TOKEN")
    )
    if not token:
        print("No SLACK_TOKEN found. Running in preview mode.")
        preview()
        return

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"Message sent successfully! ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')}")
                print("Full response:", json.dumps(body, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")


if __name__ == "__main__":
    send()
