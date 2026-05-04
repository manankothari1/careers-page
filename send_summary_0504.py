#!/usr/bin/env python3
"""
Chief of Staff Daily Summary — May 4, 2026 (TLWA LAUNCH DAY)
Sent to Manan Kothari via Slack DM: D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
CHANNEL = 'D06E4QMHCNN'

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🚀 TLWA Launch Day — Monday May 4",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Today is the day, Manan. *TLWA just launched to 800k users across 55k locations.* This is one of the most consequential product moments in Homebase hiring's history — and you shipped it. Here's everything you decided, what needs to happen next, and what I'm watching for you tonight."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Today's Schedule*\n• *3:30pm* — Hiring Leads Standup\n• *6:00pm* — TLWA Sync Up (cross-functional launch review)\n• *7:00pm* — Manan / Bob 1:1\n• *9:00pm* — DNB Heads Down\n• *10:30pm* — MBR Deck prep"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 LAUNCH DAY CRITICAL ITEMS — Verify at 6pm TLWA Sync*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *20% traffic routing bug (Careers Page V1/V2 experiment)* — This was your #1 launch blocker as of Friday. General application traffic was routing to an error page. *Confirm Gbolade/Izzy resolved this before 9am ET.* Ask for explicit confirmation in the sync.\n\n:red_circle: *iOS safe area CSS (Gbolade/Izzy)* — TLWA careers page safe-area padding. This was a ship blocker. Verify live in prod.\n\n:large_yellow_circle: *Company presets 30K (Bob/Izzy)* — 30K in progress as of May 1. Confirm completed and no overwrites.\n\n:large_yellow_circle: *TLWA award display component* — Was supposed to deploy to prod Sunday night. Confirm live.\n\n:large_yellow_circle: *Company list freeze* — 55,696 vs 54,000 discrepancy. Get clarity on final number in sync.\n\n:large_green_circle: *Careers page V1 deplyed* — Mobile fixes, hex input, banner pencil, logo fit, carousel, font icons all shipped Apr 30 QA. Should be green."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Key Decisions You Made Last Week (Apr 27 – May 1)*\n_These shaped today's launch and what comes next:_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Two-Squad Engineering Structure — LOCKED ✅*\n_Why:_ Engineering morale was at a breaking point (worst DX scores on record, 2 engineers flight risks). Single-squad with competing priorities was crushing the team.\n_Decision:_ Dana leads AM planning sessions; Manan leads PM sessions (West Coast timing). Each PM = sole gatekeeper for their squad. No cross-squad priority fighting.\n_Action for you:_ Message Dana today — confirm squad assignments for Sprint 2610. Tonight's DNB heads-down time is your window to define which engineers are in which squad.\n_Watch:_ Martin + Jatin support both sessions. If unclear, ping Martin now."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Tight Sprints Starting 2610 — LOCKED ✅*\n_Why:_ Mid-sprint clarification loops were killing velocity and burning the team. Ray mandated this directly.\n_Decision:_ Every ticket fully defined (acceptance criteria, designs, empty states, happy paths) before sprint starts. Engineering pushes back on undefined work. Monday/Tuesday = planning; Wednesday = heads-down.\n_Action for you:_ Sprint 2610 kicks off THIS WEEK. Mon/Tue = ironclad ticket definitions. You need Cindy's Predicted Roles designs and full requirements written *today or tomorrow* before engineering starts Wed.\n_Retro:_ Thu May 8 — bring 2-3 specific boundary case examples."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Sprint 2610 Scope — LOCKED ✅*\n_Why:_ Four bets to validate marketplace hypotheses and drive ARR growth.\n_Decision (you + Ray, May 1):_\n  1. Purchase Boost (Askew integration + Talroo campaign separation + CPC $35→$50)\n  2. Predicted Roles (trial start optimization)\n  3. JobGet Easy Apply + 30-day paid experiment (queue priority gating)\n  4. Sponsored Jobs API kickoff\n_Action for you:_ Write ironclad epics for all 4 by EOD Tuesday. Cindy on Predicted Roles. Matan on Boost/Talroo. Nelson on JobGet. Jatin on Sponsored Jobs.\n_At risk:_ Predicted Roles design not confirmed as done yet — check with Cindy at standup today."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Predicted Roles UX — LOCKED ✅*\n_Why:_ Needed clear placement, gating, and visual treatment before Cindy could finish designs.\n_Decision (you + Cindy, May 1):_\n  • Dashboard: under 'Jobs' section, disappears after first job post\n  • Mobile preview: fixed 884px device height (no double scroll)\n  • Careers page version: separate experience, dotted line = draft\n  • Access: TLWA participants OR drive-off-the-lot experiment\n  • Pre-syndication: auto-approve low-risk companies in first week via HB usage signals\n_Action for you:_ Confirm Cindy's designs are ready for eng tickets by Tuesday standup."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. 3 Marketplace Hypotheses — LOCKED ✅*\n_Why:_ Needed a unifying framework for the rest of the year to cut through noise.\n_Decision (you + Ray, May 1):_\n  1. Make spending obvious + easy for customers\n  2. Drive applicant flow through marketplace\n  3. Enable hiring specialists to intervene for job health\n_Action for you:_ Build the roadmap doc (Granola transcript + Claude). You committed to this to Ray. Tonight's DNB window = build this doc. Don't let it slip another week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Indeed Integration — Scraping Is Wrong Path ✅*\n_Why:_ Growth team's scraping approach creates duplicate postings.\n_Decision (you + Cindy, May 1):_ Better path = OAuth login to claim/port existing Indeed jobs. Test with fake door first to validate interest before building.\n_Action for you:_ Brief Tanner + the growth team on this pivot when redirect URL blocker is resolved. This should be in Sprint 2611 planning."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Home Blast Concept — DIRECTION SET ✅*\n_Why:_ Proactive employer-to-candidate outreach is a new revenue vector.\n_Decision (you + Ray, May 1):_ Guardrails: 10 candidates max/blast; auto-interview acceptance; 'Boost and Blast' pricing. Targets: former employees, applicants, PT workers, HB user DB.\n_Action for you:_ Build the roadmap doc tonight. This is the marquee concept for SF in-person strategy session."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Engineering Morale — Communicate Tight Sprints as a Gift ✅*\n_Why:_ Fadi + Dana showing burnout. Two engineers considering leaving.\n_Decision:_ Frame two-squad structure + tight sprints as a gift to the team, not a correction. Communicate it AFTER TLWA launch (i.e., right now).\n_Action for you:_ Send a thoughtful message to #hiring-eng or the team TODAY celebrating TLWA launch AND announcing the structural changes. You have the credibility right now — use it."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ OVERDUE ITEMS — These cannot wait another day*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *TLWA brief to Ted (20+ days overdue)* — Send tonight, no exceptions. You said 'tonight' on Sunday. It's now Monday.\n\n:rotating_light: *Matan: post Boost plan to #leads + survey customers* — Overdue since Apr 23. Either he's done it and you missed it, or it's 11 days overdue. Check and unblock in Bob 1:1 or tag Matan directly today.\n\n:rotating_light: *Nelson: metro_area + bucketed_role + matching_roles* — Overdue since Apr 8. Nearly a MONTH. This is blocking resume scoring. Get a status TODAY at standup.\n\n:large_yellow_circle: *HB Assistant tool definitions* — Were supposed to be submitted May 1. Confirm with Fadi at standup.\n\n:large_yellow_circle: *Indeed ATS survey* — Should have arrived this week per Apr 30 webinar. Check email, respond immediately.\n\n:large_yellow_circle: *Saja (Talroo)* — Send CPA categories + configure campaign. Unblocks Talroo budget.\n\n:large_yellow_circle: *JobGet budget* — Confirm 30-day test budget with Peter Lee + Dan. Sprint 2610 depends on this.\n\n:large_yellow_circle: *Boost modal copy* — 3 inconsistent states. Fast fix. Assign to Cindy or Carlo today."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📆 What's Coming This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Today (Mon May 4):* TLWA launches 9am ET. Sprint 2610 planning starts. Carlo returns from leave.\n• *Tue May 5:* Juan risk logic review + auto-syndication watch-and-wait closes. Ironclad tickets due.\n• *Wed May 7:* Engineering heads-down starts. Boost Pathways QA (Carlo).\n• *Thu May 8:* Tight sprint retro — bring 2-3 specific boundary case examples.\n• *~May 10:* SF in-person strategy session (post-Small Business Week).\n• *May 11:* Boost Pathways launches (marketing launch).\n• *May 22:* Customer Connection Challenge Show & Tell."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💪 A Word from Your Chief of Staff*\n\nManan — TLWA is live. 800,000 users are seeing something you built from scratch. The careers page is deployed. The two-squad structure is locked. Sprint 2610 is scoped. You've made more consequential product decisions in the last two weeks than most PMs make in a quarter.\n\nTonight: (1) Celebrate at the 6pm sync, (2) send the Ted brief, (3) build the marketplace roadmap doc, (4) write a real message to your team. You've earned it — and they need to hear it from you.\n\nLet's go. 🟠"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Automation • May 4, 2026 • No Granola meetings logged yet today (notes index at end of day)"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "TLWA Launch Day Summary — May 4, 2026",
    "blocks": blocks
}


def preview():
    sys.stdout.buffer.write(("=== SLACK PREVIEW (no token) ===\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block["type"] == "header":
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer " + SLACK_TOKEN,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully!")
                print("Timestamp:", body.get("ts"))
            else:
                print("Slack API error:", body.get("error"))
                print("Full response:", json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if not SLACK_TOKEN:
        print("No SLACK_TOKEN found. Previewing message instead.\n")
        preview()
    else:
        send()
