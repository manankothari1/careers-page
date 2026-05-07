#!/usr/bin/env python3
"""
Daily Chief of Staff Summary — Thursday, May 7, 2026 (covering May 6 meetings)
Manan Kothari, PM @ Homebase — Applicant Flow Squad
"""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = (
    os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Debrief — Wednesday, May 6 🌟",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! Huge day — you ran the *Sprint 2610 Lookahead* with the full squad and "
                "laid out a crisp four-project sprint with a brand-new execution model. You were "
                "clear, you were decisive, and your team walked away knowing exactly what to build "
                "and how to build it faster. Here's your full debrief. :muscle:"
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
            "text": "*:calendar: Today's Meetings*\n• 12:15 PM — *Applicant Flow 2610 Lookahead* with Tanner, Cindy, Bob, Iszael, Jatin, Unneji"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. New Execution Model: Team Swarming — LOCKED* :fire:\n"
                "_Decision:_ Shifting from individual project ownership to swarming — multiple "
                "engineers on Manan's #1 stack-ranked priority, then move to the next. No more "
                "\"Tanner owns X, Iszael owns Y.\"\n"
                "_Rationale:_ Gets the highest-impact work out faster, spreads context across "
                "the team, and aligns execution speed to product feedback loops. This is a "
                "fundamental mindset shift for the squad."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Homebase Boost — Spec Locked* :white_check_mark:\n"
                "_Decision:_ OEMs can purchase a Homebase Boost through Toru with the following "
                "parameters:\n"
                "• Budget: *$50* (up from $35 organic)\n"
                "• CPC: *50¢* (up from 40¢ organic)\n"
                "• Stays live until budget consumed or job expires — no removal at 10 applicants "
                "or \"healthy\" status\n"
                "• Still pulled if job goes inactive\n"
                "• Source tagged as *\"Homebase Boost\"* (visible in data + candidate table)\n"
                "• Jobs move from generic XML feed campaign → boosted campaign node\n"
                "_Rationale:_ Platforms are deranking organic listings. This gives OEMs a "
                "self-serve, affordable lever to ensure their boosted jobs surface at the top "
                "of Toru placements and drive the applicant flow they need for healthy trial volume."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Craigslist Boost: Hide Now, Remove Later — LOCKED* :broom:\n"
                "_Decision:_ Hide the Craigslist boost option in the UI immediately. Clean up "
                "code in ~1 month.\n"
                "_Rationale:_ <0.5% of jobs ever boosted through Craigslist, it's a waste of "
                "real estate. Hiding first (vs. hard delete) protects any jobs that are "
                "currently boosted from being affected."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Homebase Boost Data Tagging: Engineering to Decide Approach — DECIDED* :bar_chart:\n"
                "_Decision:_ How to tag Homebase Boost data is up to Bob & Iszael — whether via "
                "source field (UTM parameter change) or a separate campaign type field. "
                "Requirements are non-negotiable: visible in internal data + candidate table for OEMs.\n"
                "_Rationale:_ You correctly called out that you shouldn't constrain reporting "
                "design to a future state you don't know yet. The engineering team is better "
                "positioned to make the right technical data model decision."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Zip Recruiter CPC XML Feed: Test Integration Approved — LOCKED* :zap:\n"
                "_Decision:_ Build a ZipRecruiter XML feed (similar to Toru/AppCast). Key "
                "differences: CPA target set at *campaign level* (not job level), centrally "
                "controlled budget. Start as a test; full automation if successful.\n"
                "_Rationale:_ Diversifies the paid job distribution network. Low-risk to test "
                "because the pattern is well-understood (you've done it before with Toru/AppCast)."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. MD Implementation Files Approved for Lookaheads — DECIDED* :page_facing_up:\n"
                "_Decision:_ Manan will drop AI-generated MD spec files during lookaheads as "
                "context for engineers. Jatin endorsed. Drop as MD in repo/PR going forward.\n"
                "_Rationale:_ If it cuts execution time, it's worth it. Engineers can validate "
                "against the MD rather than starting from scratch."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Sponsored Jobs API (Indeed): Spike in 2610, Full Build in 2611 — LOCKED* :rocket:\n"
                "_Decision:_ 2610 deliverable is a spike only — map risks, dependencies, "
                "implementation timeline, complete Indeed's pre-integration checklist, and have "
                "a launch-ready plan for 2611. Cindy + Manan to define UX flow in 2610.\n"
                "_Rationale:_ Indeed requires a full pre-integration checklist + video walkthrough "
                "demo before going live. Doing the spike now de-risks the 2611 sprint start date "
                "and gives Cindy time to incorporate Indeed's required UI elements."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Indeed Boost UX = Separate Option in Boost Modal — DIRECTION SET* :iphone:\n"
                "_Decision:_ The in-product Indeed boost will appear as a distinct option in the "
                "boost modal (alongside the Homebase Boost and eventually others). Not bundled "
                "under \"Homebase Boost.\" OEMs won't be redirected to Indeed — it'll all happen "
                "inside Homebase.\n"
                "_Rationale:_ Keeps the purchase experience clean and in-product. Each channel "
                "is its own distinct value prop."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9. Careers Page: Embed Codes (2 Types) — SCOPED* :link:\n"
                "_Decision:_ Two embed types:\n"
                "• *Open Positions Only:* Jobs + locations (no Homebase branding, assumes "
                "they have their own careers page)\n"
                "• *Full Page Embed:* Everything — powered by Homebase branding included\n"
                "_Rationale:_ Gives OEMs flexibility to either augment their existing careers "
                "page or replace it entirely."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10. Location Name Editing: Hiring Profile Only — LOCKED* :pencil:\n"
                "_Decision:_ Editing location name on careers page saves to the *hiring profile "
                "table only* — does NOT update the main Homebase team app location data.\n"
                "_Rationale:_ Respects data isolation between hiring and the core product. Clean "
                "separation of concerns."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*11. Job Page Branding: P1 Priority — CONFIRMED* :art:\n"
                "_Decision:_ Carry OEM primary colors to the job page itself. "
                "Handle button readability (if color is unreadable, adjust accordingly). "
                "Cindy to finalize designs today and add them to a dedicated Figma frame linked "
                "from the ticket.\n"
                "_Rationale:_ Brand consistency across the careers page → job page funnel. "
                "A careers page that goes purple when you click a job is a jarring experience."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*12. DOR Check Enforcement Starts Now — LOCKED* :clipboard:\n"
                "_Decision:_ Starting tomorrow, any item Manan moves into the sprint board must "
                "have all DORs (Definitions of Ready) checked off before it goes in. "
                "Bob & Tanner will audit.\n"
                "_Rationale:_ Prevents half-baked work from entering the sprint and slowing "
                "engineers down. This is hygiene."
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
            "text": "*:white_check_mark: Your Action Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *RIGHT NOW:* Check off all milestones on Careers Page 2.1 in the project view "
                "(they were done, just not marked)\n"
                "• *RIGHT NOW:* Check off Homebase Boost + Zip Recruiter milestone checkboxes in "
                "d3lo as well\n"
                "• *TODAY:* Cindy is finalizing the job page branding designs + UX cleanup items "
                "in Figma — confirm she's done and link the frame to the ticket\n"
                "• *BEFORE MONDAY:* Move all sprint items with DORs checked — no exceptions going "
                "forward\n"
                "• *THIS SPRINT (2610):* Work with Cindy to define the Sponsored Jobs API / "
                "Indeed boost UX flow (boost modal design, in-app flow)\n"
                "• *MONDAY STANDUP:* Follow up with Bob & Iszael on Homebase Boost data tagging "
                "approach decision\n"
                "• *ONGOING:* For future lookaheads — attach AI-generated MD spec files to tickets "
                "to give engineers implementation context"
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
            "text": "*:eyes: Watch List / Open Questions*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Homebase Boost + existing organic boost collision:* The team confirmed the "
                "logic (OEM purchase overrides organic, job moves from generic → boosted campaign) "
                "but this is worth a quick sanity-check with Iszael before coding starts\n"
                "• *Indeed pre-integration video walkthrough:* This is a hard dependency before "
                "Sponsored Jobs API goes live — make sure this is on Cindy's radar as a sprint "
                "deliverable even though the full build is 2611\n"
                "• *Zoom meeting agenda links:* Your calendar invites are generating Zoom "
                "doc links that don't work — minor friction for teammates, worth turning off "
                "in Zoom settings when you get a sec"
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
            "text": "*:calendar: Looking Ahead*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *This week:* Sprint 2610 kicks off — swarming model goes live, "
                "Homebase Boost + Zip Recruiter build begins\n"
                "• *Sprint 2610 spike:* Indeed Sponsored Jobs API pre-integration — "
                "risk assessment, dependency map, implementation timeline ready for 2611\n"
                "• *Sprint 2611 start:* Sponsored Jobs API full build begins — "
                "need spike results + UX flow finalized before then"
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
                "*:star2: Chief of Staff Take*\n"
                "Today was a great session, Manan. You walked in with four well-scoped projects "
                "and a clear stack rank, and you walked out with a team that understands *why* "
                "each project matters and exactly *how* it works. The swarming model is a big "
                "shift — keep reinforcing it in the first few standups because old habits die hard.\n\n"
                "The highest-risk item right now is the *Sponsored Jobs API spike* — Indeed's "
                "pre-integration checklist is longer than most people expect, and the video "
                "walkthrough requirement adds a hard external dependency. Get someone assigned "
                "to that spike on day one of the sprint.\n\n"
                "You're building something real here — a self-serve paid acquisition engine "
                "inside Homebase. The pieces are coming together. Let's ship. :rocket:"
            )
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Debrief — Wednesday May 6 (Sprint 2610 Lookahead: 12 Decisions + Action Items)",
    "blocks": blocks
}

if not SLACK_TOKEN:
    print("=" * 70)
    print("SLACK_TOKEN not set — running in PREVIEW mode")
    print("To enable live Slack delivery, add SLACK_BOT_TOKEN to your")
    print("Cursor Dashboard > Cloud Agents > Secrets")
    print("=" * 70)
    print()
    print("Preview of message that would be sent to", CHANNEL_ID)
    print()
    for block in blocks:
        if block["type"] == "header":
            print("=" * 70)
            print(block["text"]["text"])
            print("=" * 70)
        elif block["type"] == "section":
            print(block["text"]["text"])
            print()
        elif block["type"] == "divider":
            print("-" * 70)
    exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SLACK_TOKEN}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        if result.get("ok"):
            print("SUCCESS: Message sent to", CHANNEL_ID)
            print("Timestamp:", result.get("ts"))
        else:
            print("ERROR from Slack API:", result.get("error"))
            exit(1)
except urllib.error.URLError as e:
    print("Network error:", e)
    exit(1)
