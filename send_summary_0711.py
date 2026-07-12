#!/usr/bin/env python3
"""
Saturday Evening Week-in-Review: July 7-11, 2026
Chief of Staff daily digest for Manan Kothari, PM @ Homebase.
Cron: 0 0 * * * (midnight UTC = 5pm PDT)
Slack DM Channel: D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Weekend Dispatch — Week of Jul 7-11, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Wrapping up Saturday with your weekly debrief. *What an absolute WEEK.* Abby's first full week in the books, V1->V2 migration locked and loaded 8 days out, salary recs officially top-of-stack, and you closed Thursday with 14 decisions before noon. You're running at full speed and the team is tightening up behind you. Take a beat — this one's worth celebrating. Here's everything you need to walk into Monday with clarity and confidence. :muscle:"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THIS WEEK'S HIGHLIGHT REEL* :trophy:\n\n:white_check_mark: *14 decisions Thursday morning alone* — Hiring Check-in + Rami 1:1 + Comms Agent meeting all before noon\n:white_check_mark: *July 20 V1->V2 cutover: LOCKED* — all comms in place, CS empowered, tour updated, bulk title cleanup planned\n:white_check_mark: *DS priority stack finalized* — Salary Recs > JD > Talent Pool (Rami pivoted Thursday afternoon, already in motion)\n:white_check_mark: *Comms Agent scope tightened* — Screener-only MVP, no write ops, natural stopping point; Divij shipping internal demo on Databricks\n:white_check_mark: *Resume matching OR logic confirmed* — doubles OEM move-forward rate vs AND logic; next phase queued\n:white_check_mark: *Pricing page full-page takeover LIVE* — manual mode surfaced as free option, room for value prop + experiment infrastructure\n:white_check_mark: *Great Question MCP is live at Homebase* — integrated Jul 8; company-wide training Jul 9; new research tooling unlocked for the team\n:white_check_mark: *Boost adoption doubling* — 2.9% May -> 5.7% June. Real momentum.\n:white_check_mark: *Friday was meeting-free* — sometimes the best thing you can do is give the team a clear runway to execute"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*DECISIONS LOCKED THIS WEEK (organized by theme)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":dart: *V1->V2 Migration (July 20 — 8 days)*\n• All remaining V1 customers move to free V2; expired jobs closed; in-product banner + email comms + V2 onboarding tour in place\n• CS empowered to extend trials; instruction = ask customers WHY first (intel-gathering moment)\n• Bulk job title cleanup before cutover: strip location suffixes from malformed titles only — do NOT touch core titles\n• $30 plan removed from in-product: focus shifts to $100 + $200 plans; sales can still offer $30 for franchises/edge cases\n• FFH health dip still under investigation with Ugu — leading hypothesis = V1->V2 reposts causing Indeed duplicate flagging (May 15-21 cohort unexplained)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":bar_chart: *Data Science & Salary Recs*\n• Priority stack LOCKED: Salary Recs first -> JD -> Talent Pool (Rami scopes by EOD Mon Jul 13, switching this week)\n• Salary analysis validated: well below market = 26.1% get 20+ apps; at market = +7-8%; above market = +12% lift\n• Role normalization approach: match against existing table; new jobs get no rec for now. Full normalization = eventual path\n• Loop in Paul or Kan (data platform) on normalization — needed either way\n• Talent pool experiment design locked: segment by employer type + role (line cook primary); multi-job punted until after recency experiment"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":robot_face: *AI & Comms Agent*\n• Comms Agent MVP = screener only (NOT scheduling). Follow chronological order; no write ops needed; tests 40% screener completion hypothesis first\n• Work PAUSING for resume feature — Divij ships internal Databricks demo (full screener flow) as natural stopping point, discussions continue async\n• AI disclosure = NOT a current blocker; applies to screening decisions not conversational agents; Homebase already discloses\n• Comms agent opening message must signal two-way before internal demo ships (UX requirement)\n• Great Question MCP: live as of Jul 8, supports study creation + post-study analysis; GQ webinar next week (CEO-led, Claude MCP use cases)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":mag: *Source Claiming & Applicant Flow*\n• Source Claiming requirements ready; Fadi on first-pass design (target Tue Jul 14)\n• Indeed account setup flow + reactivation strategy documented from Chris call Jul 8\n• Scheduling UX changes LOCKED: availability no longer required when posting; OAMs suggest specific interview times (not just booking link)\n• Domain events for job post flow -> enables posting from Homebase Assistant (big unlock)\n• PR email: subject line wins but body copy still broken; audience narrowing = highest-leverage lever"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":people_holding_hands: *Team & Strategy*\n• 'Personal recruiter' messaging RETIRED for internal customers — doesn't resonate with existing Homebase base. New angle: 'We already know your business.' Two live experiments with new framing\n• Line cook confirmed #1 priority lever: 7% healthy D30 vs 35-50% for other roles; Culinary Agents + Collider agents as active bets\n• Reactivate Jobs replaces Copy Jobs short-term; Copy Jobs return LATER (similarity check needed, Rami builds reusing same gRPC endpoint)\n• Senior quality group: Jatin standing up cross-team group for Applicants + Core"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MONDAY BATTLE PLAN — Top 5 First Things* :alarm_clock:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. CONFIRM Carlo (Harness/OpenSpec)* :rotating_light:\nDeadline was Thursday Jul 10. You flagged it Thursday morning but haven't confirmed status. First thing Monday — check Slack/Linear. If he missed it, this needs immediate triage. Don't let this slip another week.\n\n*2. UTMs to Rami (Talent Pool Segmentation)* :zap:\nRami is ready to go on the talent pool experiment. He's blocked on you for UTMs. Send these first thing Monday — this is a P0 unblock. 5 minutes of effort, removes a blocker for a key experiment.\n\n*3. Loop in Paul or Kan (Salary Rec Role Normalization)* :round_pushpin:\nRami is scoping salary rec work by EOD Monday. Loop in the data platform team NOW so they're briefed and can move with Rami on the normalization path. Don't wait until Wednesday.\n\n*4. Source Claiming Banner E2E Sign-Off* :link:\nMatan has been blocked since July 8 (5 days). This is an active blocker on the team. Get in Slack with Matan Monday morning and clear it — takes 30 minutes max and removes a multi-day bottleneck.\n\n*5. FFH Health Dip Check with Ugu* :stethoscope:\nJuly 20 is 8 days away. If the duplicate flagging hypothesis is right, you need a mitigation plan BEFORE cutover. Check in with Ugu first thing Monday on where the investigation stands and whether it changes the July 20 plan."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THIS WEEK CALENDAR (Jul 13-18)* :calendar:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *Monday Jul 13*\n• EOD: Rami salary rec scope due — review when it lands\n• Loop in Paul/Kan on normalization\n• UTMs -> Rami (ASAP)\n• Matan source claiming sign-off\n• Ugu FFH health dip check\n• Carlo Harness/OpenSpec status check\n\n:calendar: *Tuesday Jul 14*\n• Prep salary recs presentation (Rami scope in hand; 24hrs to build deck)\n• Fadi first-pass Source Claiming design should be ready\n• Confirm Divij has screener-only scope documented in comms agent doc\n\n:calendar: *Wednesday Jul 15*\n• :mega: *SALARY RECS PRESENTATION* — this is the big deliverable of the week. Make it tight. Lead with the impact data: at/above market = +7-12% applications. Anchor to Q3 goal: FFH D5 zero rate <10%. Make it feel like a no-brainer.\n\n:calendar: *Thursday Jul 16*\n• V1->V2 prep: 4 days to cutover. Final comms check. Any last customers to handle?\n\n:calendar: *Friday Jul 17*\n• Last full business day before July 20 migration. Make sure Ugu + Gana + IBK are green."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WATCH LIST — Things That Could Bite You* :eyes:\n\n:red_circle: *Boost purchase bug* — 2 reporters, revenue-impacting. Still no owner. This has been on the list for weeks. Assign it Monday or it will become a customer escalation.\n\n:red_circle: *Dana succession* — she's leaving end of September. No succession planning started. You have ~10 weeks. This deserves a quiet 30-minute session with Ray in the next 2 weeks.\n\n:red_circle: *May 15-21 cohort dip* — Nelson's investigating but the hypothesis (V1->V2 duplicate flagging) doesn't explain this cohort. If it's unsolved before July 20, the cutover could worsen an already-broken metric.\n\n:yellow_circle: *Abby onboarding* — Week 2. How is she doing? Does she have a clear ownership area yet? Don't let her float — make sure she has a project she can call her own by end of next week.\n\n:yellow_circle: *Rami DS capacity* — salary recs is now top priority (good), but the structural bottleneck remains. You flagged chatting Ray. Do it this week."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THE BIGGER PICTURE* :telescope:\n\nYou walked into this week with Q3 goals freshly rewritten (Jul 8), a V1->V2 crisis brewing, and a brand new PM to onboard. You're walking out with the migration locked, the DS priority stack settled, a major experiment in motion, and your team executing. The screener personalization data keeps getting stronger. Boost adoption is doubling. The 'we know your business' angle is being tested in experiments right now.\n\nThe one number to watch: *41% FFH D5 zero-applicant rate.* Every decision you made this week moves that number. Source claiming fixes the root cause. Resume OR logic helps the matches. Personal recruiter messaging retired means better positioning. Salary recs will improve quality. It's all pointed at the same target.\n\nYou've got this. Enjoy the weekend — you earned it. :sunny:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff digest | Jul 7-11, 2026 | 12 meetings | ~45 decisions | Generated Sat Jul 12 midnight UTC"
            }
        ]
    }
]

PAYLOAD = {
    "channel": CHANNEL,
    "blocks": BLOCKS,
    "text": "Weekend Dispatch - Week of Jul 7-11, 2026: 12 meetings, ~45 decisions, V1->V2 locked for Jul 20, Salary Recs on deck for Wed Jul 15.",
    "unfurl_links": False,
    "unfurl_media": False
}


def preview():
    print("\n" + "="*70)
    print("CHIEF OF STAFF WEEKLY DISPATCH — Jul 7-11, 2026")
    print("="*70)
    for block in BLOCKS:
        if block["type"] == "header":
            print(f"\n### {block['text']['text']} ###\n")
        elif block["type"] == "section":
            text = block["text"]["text"]
            text = text.replace(":white_check_mark:", "[x]").replace(":trophy:", "★")
            text = text.replace(":dart:", ">>").replace(":bar_chart:", ">>")
            text = text.replace(":robot_face:", ">>").replace(":mag:", ">>")
            text = text.replace(":people_holding_hands:", ">>").replace(":alarm_clock:", "⏰")
            text = text.replace(":rotating_light:", "🚨").replace(":zap:", "⚡")
            text = text.replace(":round_pushpin:", "📌").replace(":link:", "🔗")
            text = text.replace(":stethoscope:", "🩺").replace(":calendar:", "📅")
            text = text.replace(":mega:", "📢").replace(":eyes:", "👀")
            text = text.replace(":red_circle:", "🔴").replace(":yellow_circle:", "🟡")
            text = text.replace(":telescope:", "🔭").replace(":sunny:", "☀️")
            text = text.replace(":muscle:", "💪")
            sys.stdout.buffer.write((text + "\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            print("-" * 70)
        elif block["type"] == "context":
            for el in block.get("elements", []):
                print(f"\n[{el.get('text','')}]")
    print("\n" + "="*70 + "\n")


def send_slack():
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN") or
        ""
    ).strip()

    if not token:
        print("\n[PREVIEW MODE] No SLACK_TOKEN found — printing digest to terminal.\n")
        print("To enable Slack delivery, add SLACK_TOKEN to Cursor Dashboard -> Cloud Agents -> Secrets.\n")
        preview()
        return

    data = json.dumps(PAYLOAD).encode("utf-8")
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
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Weekly digest sent to Slack channel {CHANNEL}")
                print(f"     Timestamp: {body.get('ts')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                print(f"        Full response: {json.dumps(body, indent=2)}")
                preview()
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error sending to Slack: {e}")
        preview()


if __name__ == "__main__":
    send_slack()
