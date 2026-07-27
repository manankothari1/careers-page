#!/usr/bin/env python3
"""Sunday Evening / Monday Jul 27 Battle Plan — Chief of Staff Daily Digest"""
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
            "text": "Sunday Evening Dispatch — Monday Jul 27 Battle Plan",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff | Jul 26, 2026 @ 5 PM PDT | *0 new meetings today (Sunday)* — Weekly decisions recap + Monday priorities below"
            }
        ]
    },
    {"type": "divider"},

    # SBA LAUNCH BANNER
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*LAUNCH DAY — SBA Goes Live Monday Jul 27*\n"
                "Gurkiran's team ships the Schedule Builder Agent onboarding tomorrow. "
                "Early friendly-testing feedback on the *unassigned grid was negative* — watch that signal hard in the first 48 hours. "
                "Two flags: `modal_seen` + `sba_entered`. Pulsing icon V1 live. IBK + Malcolm handling prod enablement. "
                "This is the first real proof-point for the SBA arc."
            )
        }
    },
    {"type": "divider"},

    # P0 FIRES
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*P0 FIRES — Handle Before Anything Else Monday*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*CARLO — 14+ DAYS OVERDUE*\n"
                    "Harness/OpenSpec still not shipped. This is a management issue, not a technical one. "
                    "Have the direct conversation today. No more waiting."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*422 ERRORS — Day 17 (CRITICAL)*\n"
                    "146 locations still affected since Jul 9. Jatin on RCA. "
                    "Ask for a concrete status + fix ETA first thing Monday morning. "
                    "This has been silent for 2+ weeks — unacceptable."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*MATAN COMMS DOC — Sonia Is Blocked*\n"
                    "Sonia cannot build the new comms/triggers infrastructure until you review Matan's doc. "
                    "This review was supposed to happen over the weekend. Do it before standup."
                )
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*DANA SUCCESSION — 7 Weeks Left*\n"
                    "Dana is off Aug 7 week and leaves end of September. Page Templates hand-off has not started. "
                    "This is the biggest quiet risk in the portfolio. Draft a plan this sprint."
                )
            }
        ]
    },
    {"type": "divider"},

    # DECISIONS LOCKED THIS WEEK
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Locked This Week (Jul 21-25)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *Email Route LOCKED* (Jul 22-23) — Pre-populated mailto (Gmail/Outlook/Apple Mail) "
                "is the primary hiring outreach CTA. Beats callback (TalkDesk/Kio on vacation) and Calendly (3-person availability hell). "
                "Fadi finalized UX post-standup. _Why:_ one-step action, no one wants to call anymore, aligns with email-first strategy.\n\n"

                ":white_check_mark: *Source Claiming: 'Sending a Letter' LOCKED* (Jul 23) — "
                "Carla + Fadi + Matan looped in. Ray endorsed. "
                "_Why:_ old approach created copy jobs that inflated D5 zero-applicant rate to 41%.\n\n"

                ":white_check_mark: *FFH Experiment Option 1 LOCKED* (Jul 21) — "
                "Broad food/hospitality + in-trial, API activation trigger. "
                "Carlo + Ugo = ONE unified experiment (analytics clarity). "
                "_Why:_ proves proactive hiring nudge works before scaling.\n\n"

                ":white_check_mark: *JD Quality Experiment LOCKED* (Jul 21) — "
                "50/50 split, ratings = #1 signal (6K avg vs 300 bottom), formatting = #2. "
                "Tanner assigned. Rami on prompting. "
                "_Why:_ top line cook listings are 20x better rated — huge unlock.\n\n"

                ":white_check_mark: *SBA Onboarding Architecture LOCKED* (Jul 22) — "
                "Two-flag arch (modal_seen + sba_entered), no cooldown, pulsing border icon, "
                "tooltip auto-shows next session, jumpstart drawer suppressed when modal shown, roles usage = default in roster.\n\n"

                ":white_check_mark: *Archived Job Redirect LOCKED* (Jul 24) — "
                "Short-term: careers page redirect. Long-term: custom 'role no longer open' landing (next sprint). "
                "Jatin's catch-all + logging. Ray principle: never force sign-in.\n\n"

                ":white_check_mark: *Inline Compliance Check LOCKED* (Jul 24) — "
                "Extend 'reviewing your job post' in-progress feature to surface syndication flags DURING job creation. "
                "Kills most of 117 CX chats/30d. _Why:_ company syndication (fraud), job-level (content), propagation lag.\n\n"

                ":white_check_mark: *Manager Comms Inclusion LOCKED* (Jul 24) — "
                "Include managers in email cohorts, filter low-usage owners, focus active managers. "
                "Matan building cohorts. Dana looped in for FFH. Sonia building infra (blocked on doc)."
            )
        }
    },
    {"type": "divider"},

    # EXPERIMENTS / SIGNALS TO CHECK MONDAY
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Experiments & Signals to Check Monday*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":bar_chart: *Usman Candidate Email Experiment* — Running since Jul 23. Check results. "
                "This is the 'candidates in your area' email (Usman's signals model). "
                "Could validate proactive hiring outreach before FFH experiment launches.\n\n"

                ":bar_chart: *SBA Unassigned Grid* — First real data drops Monday. "
                "Friendly testing was overwhelmingly negative. Watch for P1 metric hard. "
                "Gurkiran has the pulse.\n\n"

                ":bar_chart: *JD Quality Experiment Kickoff* — "
                "Is Rami's prompt ready? Tanner should be set to go. Confirm experiment is live by EOD.\n\n"

                ":bar_chart: *Usman FFH Signals Model* — "
                "Carlo/Ugo FFH experiment should be getting its API trigger setup. "
                "Confirm Carlo is unblocked (or has the conversation after Harness gets resolved).\n\n"

                ":bar_chart: *Divij Match Data* — "
                "Re-pulling with real AND logic. Any update on where match quality numbers land?"
            )
        }
    },
    {"type": "divider"},

    # OPEN FOLLOW-UPS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Open Follow-Ups (Don't Let These Slip)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Juan Sanchez* — He's sending his own emails outside the proper flow. Follow up this week.\n"
                "• *Kristin* — Check TalkDesk trigger ID engineering effort (from Jul 22 EPD sync). Still relevant even though email won, need to know the delta.\n"
                "• *Rami/Reza* — Justin Lambert sign-off on replica identity / hard delete path for Izzy. Where does this stand?\n"
                "• *Tatiana* — Sitemap criteria + canonical work is next sprint. Make sure she has the MSA table access.\n"
                "• *Abby* — Week 7+. She needs a clear, real ownership area. This is overdue.\n"
                "• *Franchise proposal* — Multi-location customer closed without trial. High churn risk. Where's the proposal at?\n"
                "• *Rails 8* — Izzy smoke-tested Friday. No issues? Confirm status."
            )
        }
    },
    {"type": "divider"},

    # Q3 SCOREBOARD
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Q3 Scoreboard (Where You Stand)*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*FFH D5 Zero-Applicant Rate*\n41% :arrow_right: Target <10%\n:red_circle: Way off. Reactivation = THE unlock."
            },
            {
                "type": "mrkdwn",
                "text": "*Line Cook Jobs Healthy*\n~7% :arrow_right: Target 50%\n:red_circle: Critical. JD experiment + Instawork path."
            },
            {
                "type": "mrkdwn",
                "text": "*OEM Boost Rate*\n5.7% (up from 2.9% in May)\n:large_green_circle: Trending right."
            },
            {
                "type": "mrkdwn",
                "text": "*Total Accounts*\n800K hit week of Jul 14\n:large_green_circle: Milestone."
            }
        ]
    },
    {"type": "divider"},

    # WEEKLY KUDOS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*This Week's Wins — You Should Feel Good About These*\n\n"
                "You shipped an *insane* amount of decisions this week. Email route locked, source claiming locked, "
                "SBA architecture locked, inline compliance check scoped, manager comms locked — that's a team running at pace. "
                "The FFH frame shift (reactive product → proactive platform) is intellectually the most important unlock this quarter. "
                "Keep that thread alive. SBA launching Monday is a big moment — you've been running that arc for weeks. "
                "Proud of the week. Now go execute. :rocket:"
            )
        }
    },

    # Footer context
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff Daily Digest | Sunday Jul 26 5 PM PDT | Next run: Monday Jul 27 5 PM PDT_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Sunday Evening Dispatch — Monday Jul 27 Battle Plan"
}


def preview():
    sys.stdout.buffer.write(
        ("\n=== PREVIEW (no Slack token) ===\n" + json.dumps(payload, indent=2) + "\n").encode("utf-8", errors="replace")
    )


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"Slack message sent successfully. ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error sending to Slack: {e}", file=sys.stderr)
        sys.exit(1)


if TOKEN:
    send()
else:
    preview()
