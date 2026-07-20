#!/usr/bin/env python3
"""
Daily Chief-of-Staff Digest — Sunday Jul 19, 2026 (PDT)
Week-in-Review + Monday Jul 20 Battle Plan
Slack DM channel: D06E4QMHCNN
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
            "text": "Sunday Wrap + Monday Battle Plan — Jul 19 EOD",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Happy Sunday evening, Manan! No meetings today (as expected), so let's use this moment to celebrate a genuinely big week and set you up to *crush* Monday. Week of Jul 13-17 was a landmark — you made more structural decisions in five days than most PMs make in a month. Here's what matters."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*BIG WINS THIS WEEK* :trophy:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *800K accounts milestone* — 700K to 800K in ~5 weeks. Accelerating. That's a company-level win and your team is a core driver.\n• *Reactivation architecture locked* — stable Indeed ID, association table model, copy-job officially dead. No more duplicate-content 41% D5 zero-applicant rate dragging your Q3 goal. Tanner + Bob scoping ~7 tasks.\n• *Match quality north star aligned* — 'move forward rate' (OEM sends booking link or accepts interview). Two-metric funnel. Clean, measurable, tied to real employer intent.\n• *Salary recs unblocked* — Antoine approach approved, Izzy starts this week without DP dependency. LCM email: 5.8x enrollment lift, $379K at 10% conversion.\n• *Instawork $100/interview* — potential line cook unlock. $200-300 for niche. Real path to 50% healthy line cook target.\n• *JD prompt: ship small first* — right call. Standard headers, salary near top. Proven over perfect."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*DECISIONS LOCKED THIS WEEK* :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1. *Copy job is dead. Reactivation only.* Stable Indeed ID + association table = the path. Indeed-only scope vs universal is your open Q.\n2. *Move forward rate = match quality north star.* Divij re-pulling with real AND logic (not averaged score).\n3. *EPD Leads sync moved to Thursday afternoon* — back-to-back with Dana. Trial starts next week.\n4. *Single prioritized product list → Fadi.* Wednesday cadence locked: you + Ray + Dana.\n5. *Definition of Ready updated* — Fadi stops writing product briefs. Right.\n6. *JD prompt: ship small first* — standard headers, salary near top, eval before deeper overhaul.\n7. *V1→V2 cutover target: Jul 20* — that's *tomorrow*. No V1 companies after today.\n8. *'Drive off the lot' revival* — target Indeed users with in-product messaging. In Ugu's next sprint scope.\n9. *New eng PR directive flagged as too restrictive* — Ray escalating with Martin to clarify intent.\n10. *SEO: plain-English recs + Ahrefs crawl* — Tatiana owning. 66K pages live, 15.5K indexed = massive gap.\n11. *Parallel strategy confirmed* — net-new acquisition + message testing run simultaneously.\n12. *SBA H2 locked into 3 phases* — Jul-Sep V1, Oct-Nov memory scope, Nov-Dec agentic spec."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MONDAY JUL 20 — YOUR BATTLE PLAN* :rocket:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*P0 — MUST HAPPEN TODAY:*\n\n:red_circle: *V1→V2 Cutover* — This is THE target date. First thing Monday: ping Ugu. Is it done? Are there stragglers? Dana was investigating 200+ unexpected trial spikes. Confirm completion or triage any blockers. This is not optional.\n\n:red_circle: *Carlo Harness/OpenSpec* — Now 9+ DAYS OVERDUE (deadline was Jul 10). This is becoming a management issue. You need a conversation today — either he delivers by EOD or you escalate to Dana/Ray. Do not let this slip another day.\n\n:red_circle: *Rami → Antoine* — Rami was supposed to message Antoine *this morning* about the salary data-pull script. Confirm it happened. Izzy starts salary recs this week — she needs the data script to move.\n\n:red_circle: *Ugu PR approval* — Backend PR enabling in-product OEM setup prompts. You need to approve or unblock it. Every day this sits is a day the 'drive off the lot' flow is blocked."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*P1 — HIGH PRIORITY TODAY:*\n\n:large_yellow_circle: *Message Paul directly* on role recommendation DP status. You've been carrying this for multiple weeks. Get a yes/no by EOD.\n\n:large_yellow_circle: *Answer the Indeed-only vs universal Q* for reactivation scope. Tanner + Bob are blocked on full estimation until you decide. What's your instinct? Start with Indeed-only (smaller, faster) or go universal from day 1?\n\n:large_yellow_circle: *Confirm Rami→Antoine→Izzy handoff chain* — Salary recs: Izzy starts this week. Make sure the Monday Rami/Manan meeting has Izzy added and the handoff is actually happening.\n\n:large_yellow_circle: *Dana handoff — start the conversation.* ~10 weeks until September end. Page Templates ship Aug 14. Dana is off Aug 7 week. You have ~3 weeks to get a real plan. Ask her today: what does she want to hand off, and in what order?"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*P2 — ON YOUR RADAR THIS WEEK:*\n\n:white_circle: *Instawork $100/interview* — Reconnect with Ashwin if there's customer appetite for line cook pricing. High-leverage unlock for Q3.\n\n:white_circle: *Divij's match data re-pull* — Should be ready this week with real AND logic. Review when it lands — confirms or challenges your match quality direction.\n\n:white_circle: *Abby (Week 4+)* — She needs a clear ownership area. What's the right scope for her? Don't let this drift another week.\n\n:white_circle: *Ray 'I don't want to be the leader anymore'* — You heard this Jul 17. Stay close. His headspace matters a lot for team stability.\n\n:white_circle: *Boost purchase bug* — Revenue-impacting, no owner. Who owns this?"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*OPEN QUESTIONS YOU NEED TO ANSWER* :thinking_face:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1. *Indeed-only vs universal* for reactivation stable ID? (Blocks Tanner+Bob scope estimate)\n2. *Boost purchase bug* — who owns it? Revenue-impacting.\n3. *Abby ownership area* — what's her lane?\n4. *Dana succession* — what's the actual plan for her accounts when she leaves?\n5. *Ray directive intent* — staff+ review required on all PRs. Marketing or real? (Ray escalating with Martin)\n6. *Instawork $100/interview* — worth pursuing for line cook unlock?"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Q3 SCORECARD* :bar_chart:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• FFH D5 zero-applicant rate: *41%* → target <10% :red_circle: (reactivation is THE unlock)\n• Line cook jobs healthy by D30: *~7%* → target 50% :red_circle: (Instawork + source claiming = path)\n• Screener completions: +50% relative target :yellow_circle:\n• Healthy job rate (ICP): *30%* → target 80% :yellow_circle:\n• OEM boost rate: *5.7%* (up from 2.9% in May) :green_circle: trending right\n• ARR: *$650K+* (from $450K Jan) :green_circle: strong trajectory\n• Accounts: *800K* milestone hit :green_circle:"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*QUIET RISKS* :eyes:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Dana leaving Sep 30* — ~10 weeks. No succession plan. This is the single biggest quiet risk in your world right now. Page Templates (Aug 14), Usman+Matan day-to-day, her whole knowledge base. Start planning *this week*.\n• *Carlo overdue 9+ days* — If he's blocked, find out why. If not, this is a delivery risk that reflects on you.\n• *SEO indexing gap* — 66K pages live, 15.5K indexed. Big opportunity, no clear owner driving it urgently.\n• *Boost purchase bug* — Revenue-impacting, still floating without an owner."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You had a *massive* week, Manan. Architecture decisions locked, org friction reduced, Q3 levers identified. Monday is about execution and clearing the backlog of overdue items. You've got this. :fist:\n\n_— Your Chief of Staff_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Sunday Wrap + Monday Battle Plan — Jul 19, 2026",
    "blocks": blocks
}


def preview():
    print("=" * 70)
    print("SLACK MESSAGE PREVIEW (no token — would send to D06E4QMHCNN)")
    print("=" * 70)
    for block in blocks:
        if block["type"] == "header":
            print("\n### " + block["text"]["text"])
        elif block["type"] == "section":
            txt = block["text"]["text"]
            print("\n" + txt)
        elif block["type"] == "divider":
            print("\n" + "-" * 60)
    print("\n" + "=" * 70)


def send(token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print("Message sent successfully to D06E4QMHCNN")
            else:
                print("Slack API error:", result.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error:", e)
        sys.exit(1)


if __name__ == "__main__":
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN")
    )
    if token:
        send(token)
    else:
        preview()
        print("\nNOTE: Set SLACK_TOKEN in Cursor Dashboard (Cloud Agents > Secrets) to auto-send.")
