#!/usr/bin/env python3
"""Daily chief-of-staff digest for Manan — Oct 14 CEST workday (Spain Day 13, Wednesday)."""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
DATE_LABEL = "Wednesday, October 14 \u2014 Spain Day 13"
THEME = "\U0001f4bc INTENT CAPTURE SCOPED \u00b7 JOB FLOW 21-DAY MATRIX LOCKED \u00b7 MATCH WORKSHOP PLANNED \u00b7 INDEED BLOCKER IDENTIFIED"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f9d0 Chief of Staff Digest \u2014 Oct 14",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*{DATE_LABEL}* | 4 meetings | \u2601\ufe0f Reviewing your day from sunny Spain\n_{THEME}_"
        }
    },
    {"type": "divider"},

    # Day grade + framing
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f3af Day Grade: A-* \u2014 Incredibly productive Wednesday. "
                "You shipped clean decisions across intent capture, job post flow architecture, and the match explanation workshop format. "
                "One red flag below that needs your attention before you crush that competition tomorrow. \U0001f4aa"
            )
        }
    },
    {"type": "divider"},

    # MEETING 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb Meeting 1 \u2014 Fadi / Manan: Hiring Intent Capture (4:30 PM)*\n_Sprint 26/21 readiness + intent capture problem framing_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Intent capture stays design-only for now*\n"
                    "Appetite is low given match explanation + trial experimentation priority. "
                    "Primary surface = job details screen (not job card). "
                    "Prompt chip changes flagged as the key lever \u2014 half of OEMs accept defaults as-is, "
                    "so a default of '1 hire' will skew fill rate data. "
                    "Proposal: highlight editable chip text to draw attention."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Match Explanation Workshop format locked*\n"
                    "FigJam workshop: participants arrange sticky notes inside a candidate profile frame. "
                    "Scope = resume screener, deal-breakers, match scores, Homebase Verified, HB history \u2014 "
                    "all 'Lego pieces' designed now so future adds slot in without a redesign. "
                    "Use next week's Discovery slot (extended block). Attendees: Skye, Bob, Matan."
                )
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items from this meeting:*\n"
                "\u25b6\ufe0f Prep pending syndication data split for *Monday's Discovery* \u2014 initial thinking ready to present\n"
                "\u25b6\ufe0f *Block next week's Discovery slot* for the match explanation workshop \u2014 invite Skye, Bob, Matan\n"
                "\u25b6\ufe0f Fadi wireframing prompt chip highlight changes to gut-check scope"
            )
        }
    },
    {"type": "divider"},

    # MEETING 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb Meeting 2 \u2014 Hiring EPD Standup (5:15 PM)*\n_Sprint 26/22 status \u00b7 Indeed release blocker \u00b7 OTP scope_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Indeed incident = RELEASE blocker, not implementation blocker*\n"
                    "Indeed recommended updating the source name; change caused a spike in fraudulent posts. "
                    "Before go-live, team must sit down with Indeed to walk through the architecture and get their sign-off. "
                    "Implementation continues. Tiger volunteered to join the Indeed review conversation."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: OTP Magic Link in scope for 26/21, deadline end of 26/22*\n"
                    "Gbolade can start this sprint or next depending on capacity. "
                    "Blocker: prototype has non-design elements to clean up first. "
                    "Design must give Gbolade a heads-up before he begins."
                )
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items from this meeting:*\n"
                "\u25b6\ufe0f *Identify the right Indeed contact* for pre-release architecture review (Tiger joining \u2014 coordinate)\n"
                "\u25b6\ufe0f *Sync with Divij* on Q4 roadmap + TS priorities \u2014 he needs this to POC after Indeed alerting wraps\n"
                "\u25b6\ufe0f *Note:* You are OUT Thursday + Friday \u2014 loop back on outstanding items Monday morning"
            )
        }
    },
    {"type": "divider"},

    # MEETING 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb Meeting 3 \u2014 Tiger / Manan (7:00 PM)*\n_Job post flow architecture \u00b7 Source of hire attribution \u00b7 Indeed Partner Console_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: 21-day reactivation matrix locked*\n"
                    "\u2022 Extend = same job ID, expiration date extended\n"
                    "\u2022 Reactivate <21 days = reopen same post (OEM + Indeed)\n"
                    "\u2022 Reactivate >21 days = reopen for OEM, *new post* to Indeed\n"
                    "\u2022 Net new job = follows same 21-day logic on Indeed side\n"
                    "PRs not yet merged \u2014 easy to update. Tiger adjusting implementation to include all 3 flows (create, reactivate, copy)."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Source of hire attribution scoped down*\n"
                    "Fuzzy/LLM matching scoped OUT for this iteration. "
                    "Exact or 2-of-3 field match (name, email, phone) is sufficient. "
                    "Suppress attribution prompt ONLY when system explicitly knows hire source via hiring product actions. "
                    "Manual roster additions deferred. "
                    "Databricks dashboard already exists with source tracking + scoring logic."
                )
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items from this meeting:*\n"
                "\u25b6\ufe0f *Indeed Partner Console access for Tiger* \u2014 follow-up sent to Marketplace Support, Tiger CC'd. "
                "Ping if no response by end of week."
            )
        }
    },
    {"type": "divider"},

    # MEETING 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb Meeting 4 \u2014 Hiring Discovery (7:30 PM)*\n_Intent signal capture deep-dive \u00b7 Syndication timing measurement \u00b7 Discovery format locked_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Intent signal capture = design exploration only (Skye's call)*\n"
                    "Problem: 48% of OEMs hire 1 person in 45-day window; 52% hire more. "
                    "No data on urgency or volume. Proposed: capture # hires + speed at job creation via prompt chips + job details page. "
                    "Predefined dropdowns preferred. "
                    "Risk: default bias (OEMs accept wage chip defaults). "
                    "Skye explicitly said NOT ready for engineering scoping \u2014 Manan + Fadi must align on experience first."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*\u2705 Decision: Discovery meeting format officially locked*\n"
                    "Weekly Wednesday 1-hour slot. Product owns agenda. "
                    "Jatin + Bob may use for technical design reviews (product/design optional). "
                    "Roadmap housekeeping moves to separate Manan/Fadi/Jatin sync. "
                    "Matan added as optional attendee going forward.\n\n"
                    "*\u2705 Decision: Syndication timing measurement = bring requirements to Jatin*\n"
                    "Jatin wants clear requirements + visualization (table, funnel, mockup). "
                    "'A picture worth a thousand words' \u2014 even a Claude-generated mockup works."
                )
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items from this meeting:*\n"
                "\u25b6\ufe0f *Define the intent signal capture UX with Fadi* before bringing to engineering\n"
                "\u25b6\ufe0f *Draft syndication timing requirements + visualization* for Jatin (mockup OK)"
            )
        }
    },
    {"type": "divider"},

    # MASTER ACTION ITEMS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4dd MASTER ACTION ITEMS \u2014 Your complete list from today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f525 *BEFORE YOU SLEEP TONIGHT:*\n"
                "1\ufe0f\u20e3 *3-YEAR ONE-PAGER* \u2014 Board meeting opens TODAY (Oct 15). This was due today and was NOT mentioned in any of your 4 meetings. Do you have a draft?! This is your most urgent deliverable right now.\n"
                "2\ufe0f\u20e3 *Indeed source name PR status* \u2014 Ashley met T&S today. Did Bob get the green light to merge? Loop back with Ashley and Bob tonight.\n\n"
                "\U0001f4c5 *THIS WEEK (before Thursday/Friday OOO):*\n"
                "3\ufe0f\u20e3 *Indeed Partner Console follow-up* for Tiger \u2014 ping Marketplace Support if no response (Tiger CC'd)\n"
                "4\ufe0f\u20e3 *Identify Indeed architecture review contact* \u2014 Tiger joining, must happen before job posting goes live\n"
                "5\ufe0f\u20e3 *Carlo KT async* \u2014 he started paternity today. AE65 source name, Iterable 6-email fix, 'do not syndicate' bug, continuation sizing. Slack/doc immediately.\n\n"
                "\U0001f4c5 *MONDAY (Oct 19) ON YOUR RETURN:*\n"
                "6\ufe0f\u20e3 *26/23 Look-Ahead presenting* \u2014 be ready\n"
                "7\ufe0f\u20e3 *Block Discovery slot* for match explanation FigJam workshop (invite Skye, Bob, Matan)\n"
                "8\ufe0f\u20e3 *Prep pending syndication data split* for Monday's Discovery\n"
                "9\ufe0f\u20e3 *Sync with Divij* on Q4 roadmap + TS priorities\n"
                "10\ufe0f\u20e3 *Define intent signal capture UX* with Fadi (align before engineering scoping)\n"
                "11\ufe0f\u20e3 *Draft syndication timing requirements + visualization* for Jatin"
            )
        }
    },
    {"type": "divider"},

    # WATCH LIST HIGHLIGHTS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 TOP WATCH LIST (critical overdue items)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u26a0\ufe0f *INDEED FEED \u2014 Day 53.* Bob's PR raised. T&S meeting happened today. GET MERGE CONFIRMATION from Ashley TONIGHT.\n"
                "\u26a0\ufe0f *FACEBOOK API \u2014 Day 21.* Still failing. Bob + IBK. No update since Oct 9. Ping this week.\n"
                "\u26a0\ufe0f *COMMS ASSISTANT production decision* \u2014 Malcolm leaving Nov. OVERDUE.\n"
                "\u26a0\ufe0f *RACHEL Q4/Q1/Q2 UX view* \u2014 was due Oct 7. Still not confirmed out.\n"
                "\u26a0\ufe0f *GIFT CARDS OWED:* Lola E. Erickson, Michele Landry, Ryan Reilly ($50 each).\n"
                "\u26a0\ufe0f *EMAILS UNSENT:* John Waldman (EarnBetter NDA) + Marina/Mundo Academy (26+ days late).\n"
                "\u26a0\ufe0f *OMNI ACCESS* \u2014 Looker went dark Oct 2. Past due. Ping IT."
            )
        }
    },
    {"type": "divider"},

    # Closing / personal note
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f1ea\U0001f1f8 *You're crushing it, Manan.* "
                "Four meetings, five major decisions, and a clean architecture decision on the job post flow \u2014 "
                "all while managing everything remote from Spain. "
                "Tomorrow is the competition \U0001f3c6 \u2014 go win it. "
                "Just handle the board one-pager and the Indeed merge confirmation tonight first. You've got this."
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "\U0001f916 Chief of Staff \u2022 Oct 14 CEST digest \u2022 4 meetings reviewed \u2022 Granola-powered"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Digest \u2014 Oct 14 | 4 meetings, 5 decisions, board one-pager DUE NOW"
}

def preview():
    sys.stdout.buffer.write("\n=== SLACK PREVIEW (no token) ===\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"TO: {CHANNEL}\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"FALLBACK: {payload['text']}\n\n".encode("utf-8", errors="replace"))
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            line = f"[HEADER] {block['text']['text']}\n"
        elif btype == "section":
            if "text" in block:
                line = f"[SECTION] {block['text']['text'][:200]}\n"
            elif "fields" in block:
                line = "[FIELDS]\n" + "\n".join(f"  - {f['text'][:120]}" for f in block["fields"]) + "\n"
            else:
                line = "[SECTION]\n"
        elif btype == "divider":
            line = "---\n"
        elif btype == "context":
            line = f"[CONTEXT] {block['elements'][0]['text']}\n"
        else:
            line = f"[{btype}]\n"
        sys.stdout.buffer.write(line.encode("utf-8", errors="replace"))

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
).strip()

if not token:
    preview()
    print("\n[INFO] No Slack token found. Add SLACK_TOKEN secret in Cursor Dashboard > Cloud Agents > Secrets.")
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"[OK] Digest sent to {CHANNEL} (ts={result.get('ts')})")
    else:
        print(f"[ERROR] Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error: {e}")
    preview()
    sys.exit(1)
