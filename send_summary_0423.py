#!/usr/bin/env python3
"""Daily decision summary for Apr 23, 2026 (covering Apr 22 meetings)."""
import json, os, sys, urllib.request, urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Debrief — Wednesday Apr 22 :briefcase:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day — 3 meetings, a lot moved forward. Here's every decision you made today, why it matters, and exactly what needs to happen next. You crushed it. :fire:"
        }
    },
    {"type": "divider"},

    # ── DECISION 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:one:  3LO — Simplified Job Status Display Strategy*\n*What you decided:* Show only Homebase + Indeed live links; all other job boards (Glassdoor, Google, XML partners like Talroo/Taurus) default to 'Live' status — no real-time status fetching.\n*Why it's smart:* Shipping a clean MVP without overengineering partner-specific API integrations you don't need on day one. Indeed is the only partner where real-time status actually matters to users right now.\n*Status states locked in:* Pending (<12 hrs) → Posted (live + URL) → Deleted (hide modal entirely)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :white_check_mark: *Andrew* — Build Indeed status controller/endpoint today; finish tomorrow morning _(due Thu Apr 23)_\n• :white_check_mark: *Tanner* — Implement frontend integration once Andrew shares the API interface\n• :white_check_mark: *Andrew* — Share example API interface for review before EOD"
        }
    },
    {"type": "divider"},

    # ── DECISION 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:two:  3LO Boost Modal — Descoped Entry Point*\n*What you decided:* Remove the 3LO entry point from the Boost modal entirely.\n*Why it's smart:* You previously flagged CTA noise risk (Boost + one-time posts + 3LO = hierarchy chaos). Descoping this keeps the flow clean and prevents confusion before TLWA launch week. The new Boost modal flow: hide if not authenticated → show 'waiting for live' if authenticated + job pending → show purchase if authenticated + job live.\n*Why it matters:* This directly unblocks Andrew's frontend work without adding complexity."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :white_check_mark: *Tanner* — Implement the 3-state Boost modal logic (hidden / waiting / purchasable) against Andrew's endpoint\n• :white_check_mark: *Manan* — Validate redirect URL routing logic (single URL → backend routes to dashboard or job page) once Andrew demos it"
        }
    },
    {"type": "divider"},

    # ── DECISION 3 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:three:  TLWA — Pre-Syndication Coverage for Award Winners*\n*What you decided:* Flag the coverage gap: 48k companies / 55k locations winning Top Local Workplace Awards likely aren't getting auto-syndicated despite being the highest-trust, most-established businesses in the system.\n*Why it's smart:* These are exactly the companies that should never hit a manual approval bottleneck. Getting them pre-syndicated before the campaign drops = faster time to 'live job' = better first-day app velocity = healthier jobs.\n*Context:* Auto syndication week 1 = 16/31 companies (52%). Better than zero but the risk cohort (TLWA winners) may be stuck in medium-risk classification incorrectly."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :rotating_light: *Manan (YOU)* — Create a thread to coordinate pre-syndication of TLWA award winners _(do this tomorrow)_\n• :rotating_light: *Manan (YOU)* — Message Nelson for backfill analysis on award winner risk classification _(do this tomorrow)_\n• :white_check_mark: *Juan* — Investigate risk logic strictness after current project: verify new companies aren't mislabeled as low-risk; check medium-risk signals"
        }
    },
    {"type": "divider"},

    # ── DECISION 4 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:four:  Auto Syndication — Watch & Wait (1-2 more weeks)*\n*What you decided:* Don't optimize the auto syndication risk logic yet. Wait 1-2 weeks for meaningful data before tweaking.\n*Why it's smart:* You just rolled out a new prompt + auto syndication together on Friday night. Pulling the thread too early = false signal. Let the data accumulate, then tune. Discipline here saves you from chasing noise.\n*Current stats:* 16/31 (52%) auto-syndicated in week 1. Low-risk is the dominant classification. Flagged cases dropped significantly = less team burden."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :calendar: *Juan* — Schedule risk logic review for ~May 5 (after 2 weeks of data)\n• :eyes: *Manan (YOU)* — Set a reminder to pull auto syndication metrics in 2 weeks"
        }
    },
    {"type": "divider"},

    # ── DECISION 5 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:five:  Linear Workflow — HIPAA Auto-Channel Creation (Don't Manual Create)*\n*What you decided:* Establish the norm: never manually create project channels — let Linear's HIPAA integration handle it automatically. Offer a training session for the team.\n*Why it's smart:* Manual channel creation = inconsistency + extra work. The HIPAA integration exists precisely for this. Getting everyone on the protocol now prevents the chaos that comes from half-and-half adoption.\n*Bonus:* HIPAA triage agent on the roadmap (2 weeks) will auto-analyze tickets, draft implementation plans, flag risks, and prioritize by Linear fields. Jatin's Codex/Claude good-cop/bad-cop system demos May 4th."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :rotating_light: *Manan (YOU)* — Schedule Linear training session for the team _(this week)_\n• :white_check_mark: *Jatin* — Continue agent dev; demo ready by May 4th\n• :white_check_mark: *IBK + Izzy* — IBK on frontend tickets, Izzy on backend tickets via agent"
        }
    },
    {"type": "divider"},

    # ── DECISION 6 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:six:  Priority Protocol — Engineers Must Confirm Trade-offs Before Switching Tasks*\n*What you decided:* When raising a problem, the team must state the priority level. Engineers confirm the trade-off before switching tasks (example: Malcolm's Manual Mode fix vs. TLWA work).\n*Why it's smart:* Context-switching kills sprint velocity. This protocol protects TLWA launch week and gives engineers permission to push back — which is exactly what you want from a high-performing team."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :white_check_mark: *Manan (YOU)* — Reinforce this norm in the next standup; make it a standing rule in the team handbook\n• :white_check_mark: *All engineers* — Surface trade-offs explicitly when issues arise; don't silently context-switch"
        }
    },
    {"type": "divider"},

    # ── DECISION 7 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:seven:  Board Meeting — Narrative Locked: Steady Improvement + AI-Native + TLWA*\n*What you decided:* Lock in 4 focus areas for the hiring board update:\n1. Steady improvement story with the GTM team in place\n2. Top Local Workplaces campaign launch\n3. Product innovation beyond current offerings\n4. AI-native company evolution showcase\n*Key message:* ICPs already spend on hiring — Homebase is positioned to capture more of that wallet share more efficiently."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• :rotating_light: *Manan (YOU)* — Build the board deck hiring section around these 4 pillars; pull Momentum Metrics (ARR $650K +44%, GTM OS ML 70% in 7 days, lifecycle 46% influenced)\n• :white_check_mark: *Matan* — Share TLWA draft communications in group chat (for review)\n• :white_check_mark: *Matan* — Coordinate with Nelson on priority scoring + V5 scope"
        }
    },
    {"type": "divider"},

    # ── OVERDUE TRACKER ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *OVERDUE — These Are On You, Manan*\n\n:fire: *TLWA brief to Ted* — 20+ days overdue. Send it. Today.\n:fire: *Predicted Roles decision with Cindy* — Was due Apr 22. Close it NOW. Create the Linear project + channel.\n:warning: *Nelson: metro_area + bucketed_role + matching_roles* — Overdue since Apr 8. Ping him.\n:warning: *Salesforce access for Matan* — Lee out sick; engage Justin Stroud or rev ops to unblock\n:warning: *Manual Mode Greenlight* — Cindy QA done. Ball is in your court."
        }
    },
    {"type": "divider"},

    # ── TOMORROW ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":dart: *Tomorrow (Thu Apr 23) — Your Hit List*\n\n1. Andrew delivers Indeed status endpoint — validate it\n2. Supabase DB integration into HB1 (scheduled milestone)\n3. Create TLWA award winner pre-syndication thread\n4. Message Nelson on backfill analysis\n5. Send TLWA brief to Ted (seriously, today)\n6. Close Predicted Roles decision with Cindy → Linear project + channel\n7. Schedule Linear training session\n8. Check in on Ugo's V1→V2 migration progress"
        }
    },
    {"type": "divider"},

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_Today's summary covers 3 meetings: Hiring Leads Standup, Bi-Weekly Hiring Ops Sync, Indeed 3LO Sync! — Have a great evening, Manan. You're building something incredible. :muscle:_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Daily Decision Summary — Wed Apr 22",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK MESSAGE PREVIEW ===\n" + json.dumps(payload, indent=2) + "\n").encode("utf-8", errors="replace"))

def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + SLACK_TOKEN
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully!")
            else:
                print("Slack API error:", body.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error:", e)
        sys.exit(1)

if not SLACK_TOKEN:
    print("SLACK_TOKEN not set — printing preview instead.")
    preview()
else:
    send()
