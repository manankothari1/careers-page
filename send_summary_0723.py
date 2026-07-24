#!/usr/bin/env python3
"""Daily Decision Digest - Thursday, Jul 23, 2026"""

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
            "text": "Chief of Staff Daily Digest — Thursday, Jul 23, 2026",
            "emoji": True,
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! :wave: Big day — you made a *crystal-clear product call* this morning"
                " that will save your team weeks of debugging, and then got *direct customer intel*"
                " from a real Homebase hiring user. You are moving fast and with conviction."
                " Here is everything you decided today, why, and exactly what needs to happen next. :rocket:"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:trophy: DECISIONS MADE TODAY*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 1: Email route LOCKED for hiring outreach (over click-to-callback / Calendly)*\n"
                ":white_check_mark: *Status:* LOCKED — communicated to Matan, Carla, and Fadi\n"
                ":thought_balloon: *Why:* Callback required Manan + Matan + Sean available within 10 minutes of"
                " any inbound request — basically impossible given schedules. The 3-way call experience was"
                " clunky for users, and there was significant testing overhead to validate the callback setup."
                " Email leapfrogs all of that friction and is the better long-term solution.\n"
                ":dart: *Impact:* Unblocks the entire hiring outreach feature — no more coordination dependencies,"
                " no clunky multi-party calls, ships faster."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 2: Email UX direction — buttons OUT of dropdown, headed toward single-screen experience*\n"
                ":hammer_and_wrench: *Status:* In progress (Manan + Fadi working through post-standup)\n"
                ":thought_balloon: *Why:* Dropdown-inside-modal creates a bad interaction pattern — options"
                " hover off-screen, less content visible, confusing UX. Moving to a dedicated screen when"
                " 'email them' is clicked gives users full context on what is being sent. Fadi also floated"
                " simplifying to a *single email option* (no call alternative at all) — worth considering to"
                " reduce cognitive load. :bulb:\n"
                ":dart: *Next:* Confirm final UX pattern with Fadi and move to implementation."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 3: Source claiming — new approach is 'sending a letter' (briefed Carla this morning)*\n"
                ":white_check_mark: *Status:* Communicated — Carla, Fadi, and Matan are all looped in\n"
                ":thought_balloon: *Why:* This is the cleaner, lower-friction path to source claiming."
                " Ray endorsed it. No additional detail captured in the meeting but the decision is logged"
                " and the team is aligned.\n"
                ":dart: *Next:* Confirm implementation timeline with Fadi."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 4: Rails 8 upgrade — acknowledge, no action from you*\n"
                ":white_check_mark: *Status:* Noted — Izzy doing smoke testing this Friday\n"
                ":thought_balloon: *Why:* Rails 7 is end-of-life (no more security patches). Another team"
                " is driving the upgrade. No breaking changes expected for the hiring team.\n"
                ":dart: *Next:* When ready to cut over, instructions posted in #engineering — pull main"
                " and run listed commands. You do not need to do anything today."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: CUSTOMER INTEL — Alchemy Springs (2pm Customer Council)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Chelsea Supawit, Director of Ops at *Alchemy Springs* (SF urban bathhouse, ~10 employees,"
                " 20 contractors, targeting full opening September). Used Homebase Hiring Assistant for"
                " two real roles. Here is what matters for YOUR product:\n\n"
                ":microphone: *AI Screener feedback:* One candidate explicitly said the screener felt *'clunky.'*"
                " This is signal. Matan is connecting with that candidate directly for applicant-view feedback.\n"
                " :arrow_right: *You should know this.* When that feedback comes in, loop in and decide if"
                " it warrants a screener UX sprint.\n\n"
                ":link: *Career site embed:* Chelsea wants to embed the Homebase career site directly on"
                " Alchemy's website. Matan noted deep link may already work today and will follow up with"
                " PMs (that is you).\n"
                " :arrow_right: *Confirm whether deep link works today and reply to Matan.*\n\n"
                ":calendar: *Multi-interviewer scheduling gap:* Homebase only supports one calendar integration"
                " per account. Chelsea needs multiple interviewers at different stages of the hiring process."
                " This is a real gap — flag for roadmap consideration.\n\n"
                ":bar_chart: *Reporting ask:* She wants automated weekly reports pushed (shifts by role,"
                " hours tracking, payroll cost by role, headcount cost modeling). Not your team, but good"
                " customer intelligence."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:zap: YOUR ACTION ITEMS — P0 (Do Today / Tonight)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":red_circle: *1. Carlo — 13+ DAYS OVERDUE on Harness/OpenSpec*\n"
                "This is now a management issue. Every day this drags is a day of compounding delay."
                " If you have not already sent the 'this is not okay' message — send it tonight.\n\n"
                ":red_circle: *2. 422 Job Publishing Errors — Day 14, 146 locations*\n"
                "Jatin is on RCA. Check in today for an update. This has been silent for 2 weeks"
                " and is actively hurting employers. What is the ETA to fix?\n\n"
                ":orange_circle: *3. Send PR for multiple ad team bug fix*\n"
                "Share with Fadi and Jatin once done (committed in standup this morning).\n\n"
                ":orange_circle: *4. Confirm final email UX pattern with Fadi*\n"
                "You stayed on post-standup — document the agreed pattern and get it to the team.\n\n"
                ":orange_circle: *5. Confirm Rami pairing happened today (JD experiment + talent pool emails)*\n"
                "This was scheduled for Thu AM — did it happen? If not, reschedule ASAP."
                " Tanner is waiting on the finalized prompt to start the JD 50/50 experiment.\n\n"
                ":orange_circle: *6. Usman candidate email experiment — Day 2, check results*\n"
                "Greenlit Jul 22. Should have early signal by now or tomorrow. Ping Usman."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:soon: YOUR ACTION ITEMS — P1 (This Week)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":yellow_circle: *Dana succession — 8 weeks and counting, no plan*\n"
                "Dana is off Aug 7 week. Page Templates deadline Aug 14. You need a handoff owner NOW.\n\n"
                ":yellow_circle: *Confirm Gurkiran Amplitude call is scheduled*\n"
                "SBA exit survey trigger fix pending this call.\n\n"
                ":yellow_circle: *Niko — Confluence SBA flow update*\n"
                "Confirm this was completed or is in progress.\n\n"
                ":yellow_circle: *Career site deep link — reply to Matan re Alchemy Springs request*\n"
                "Chelsea wants to embed the career site on her own website. Quick confirm if it works today."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: WATCH LIST (Unresolved from Prior Days)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "| Item | Status | Days Open |\n"
                "|------|--------|-----------|\n"
                "| Carlo Harness/OpenSpec | :red_circle: OVERDUE | 13+ days |\n"
                "| 422 Job Publishing Errors | :red_circle: CRITICAL | Day 14 |\n"
                "| Dana Succession Plan | :red_circle: NO PLAN | 8 wks left |\n"
                "| JD Experiment (Tanner) | :yellow_circle: Awaiting prompt | Rami pairing TBD |\n"
                "| SBA Onboarding (Gurkiran Amplitude) | :yellow_circle: Pending | TBD |\n"
                "| Usman Candidate Email Experiment | :green_circle: Running | Day 2 |\n"
                "| Izzy Replica Identity (Justin sign-off) | :yellow_circle: Blocked | Ongoing |\n"
                "| SEO Gap (66K live / 15.5K indexed) | :yellow_circle: Scoped next sprint | Ongoing |"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":trophy: *Today in numbers:* 2 meetings. 3 locked decisions. 1 key customer insight."
                " Strong, clean, purposeful day.\n\n"
                "You are building something real, Manan. The email call this morning was *exactly* the kind"
                " of decisive, reasoned product thinking that separates good PMs from great ones. You saw"
                " the constraints, weighed the options, and cut through the noise. That is the job.\n\n"
                "Tomorrow: get that Carlo message sent, check in with Jatin on 422s, and confirm Rami."
                " The line cook goal is 7% -> 50% and you are the person who is going to get it there. :muscle:"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff digest — auto-generated from Granola meeting notes — Jul 23, 2026_",
            }
        ],
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Daily Decision Digest — Thursday, Jul 23, 2026",
    "blocks": blocks,
}


def preview():
    sys.stdout.buffer.write(
        "\n=== PREVIEW (no SLACK_TOKEN set) ===\n".encode("utf-8", errors="replace")
    )
    for b in blocks:
        if b["type"] == "section" and "text" in b:
            sys.stdout.buffer.write(
                (b["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
            )
        elif b["type"] == "header":
            sys.stdout.buffer.write(
                ("# " + b["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
            )
        elif b["type"] == "divider":
            sys.stdout.buffer.write(
                "---\n".encode("utf-8", errors="replace")
            )
    sys.stdout.buffer.write(
        "\n=== END PREVIEW ===\n".encode("utf-8", errors="replace")
    )


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"Message sent successfully to {CHANNEL}")
            else:
                print(f"Slack API error: {result.get('error', 'unknown')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        sys.exit(1)


if not TOKEN:
    preview()
    print(
        "\nNOTE: No SLACK_TOKEN found. Add SLACK_TOKEN (or SLACK_BOT_TOKEN) as a secret"
        " in the Cursor Dashboard (Cloud Agents > Secrets) to enable live Slack delivery."
    )
else:
    send()
