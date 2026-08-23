#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Saturday Aug 22, 2026 (PDT) / EOW Wrap + Monday Battle Plan
Cron fires midnight UTC = 5pm PDT Saturday
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Saturday EOW Wrap + Monday Battle Plan - Aug 22",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Happy Saturday - no calls today (as expected), so I'm using this slot to give you your *End-of-Week Wrap + Monday Morning Battle Plan*. This is one of the most important weekends in a while - *Sky starts Monday*. Here's everything you need to walk in sharp."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THE BIGGEST THING HAPPENING MONDAY*\n\n:star2: *Sky starts as Head of Product - Monday Aug 25*\nYou've been prepping the talent pool strategy doc for his onboarding. Here's your pre-Monday checklist:\n• *Talent Pool doc:* Is the framing updated? Key reframe: talent pool = *bridge* between applicant flow AND core product value (not just an applicant flow fix). Make sure this is clear before he reads it.\n• *Two PM/sales syncs consolidation:* Matan is resending the invite for the bi-weekly Tuesday. First one lands ~Sep 1 - confirm it's on the cal by Monday.\n• *In-domain emails brainstorm:* Was earmarked for 'next week with Sky.' Put this on his first-week agenda.\n• *Talent Pool all-in conversation:* Fadi wants to pull 1-2 engineers and go all-in. This is a real conversation to have with Sky in week 1 - prepare your POV on timing and tradeoffs.\n\n:question: *New GM of Hiring:* If they started Aug 25 (today), you'll have two new leaders on your team from day one. Connect ASAP if you haven't already."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*CRITICAL / OVERDUE - Things That Should Have Happened Already*\n\n:rotating_light: *422 Job Publishing Errors* - Day 44+ as of Friday. 146 locations still impacted. Jatin owns the RCA. This is your most embarrassing open bug. Push for a status update first thing Monday morning.\n\n:rotating_light: *Fadi - Resume Insights Designs* - Overdue since Aug 17 (now 5+ days). This is blocking you and the sprint. Get clarity on ETA Monday.\n\n:rotating_light: *Fadi - Talent Pool Designs* - Still not in Linear. Izzy (front end) is blocked waiting. This needs to be Fadi's immediate priority after Resume Insights.\n\n:rotating_light: *Culinary Agents First Data Signal* - 27 line cook jobs went live Aug 12. It's been 10 days. You should have conversion data by now. Chase Gray this week.\n\n:rotating_light: *Carlo Ferrer* - Was out 'this week' (week of Aug 18). Should be back Monday. He owns Talent Pool backend + Indeed 3LO. If he's still out, Jatin needs a contingency plan NOW."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THIS WEEK'S ACTION ITEMS (Aug 25-29)*\n\n:calendar: *Monday Aug 25 - Sky's Day 1*\n• Prep your 30-min welcome conversation with Sky. Lead with: what's in flight, what's locked, and where you need his judgment (Talent Pool all-in, in-domain emails, fraud recovery path).\n• Confirm Q3 strategy doc comments are resolved (deadline was noon Aug 21).\n• Check if Jatin created #hiring-epdd channel (greenlit Aug 20).\n• Pull your own early signal on JD A/B experiment (IBK's prompt box test) - don't wait for IBK to surface it.\n• Get 422 error RCA status from Jatin.\n\n:calendar: *Tuesday Aug 26*\n• Resume Insights designs check - if Fadi still hasn't delivered, escalate or unblock.\n• Push Myan to share ICP nudge experiment results (still opaque).\n• Abandonment survey rework: Change question to 'what stopped you STARTING?' - Assign ownership and timeline.\n\n:calendar: *Wednesday Aug 27*\n• *Mike Mohrhardt follow-up (Loco Boys Brewing)* - 46 views, 4 applicants on their bartender role. This was your scheduled follow-up date. Prep talking points on boost recommendation (<5-10 early applicants = proactively recommend boost).\n• BarTaco: Rushi was supposed to email Brooke + get intro to Scott Rodney (back from Chicago after this week). Confirm this happened.\n\n:calendar: *This week overall*\n• Tatiana (SEO) scoping session - zero content right now, huge gap, don't let this slip.\n• Tanner Hartwig: Still behind on Indeed account setup. Check status.\n• Charmina's scheduling spike docs in Linear - still unreviewed. Block 20 mins to look.\n• Push for ICP nudge experiment results from Myan.\n• Send Amplitude dashboard to Matan (overdue since Aug 6 - seriously, send this!)."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THINGS LOCKED & SHIPPING (celebrate these!)*\n\n:white_check_mark: *OTQ Email Verification Flow LOCKED* (Aug 21) - email > phone, job stays DRAFT until verified, 98.5% of users have email. Targeting sprint after next. This is your Indeed jail exit path.\n:white_check_mark: *Internal Job Posting added to roadmap* (Aug 21) - auto-publish externally after X days. Brooke at BarTaco will love this.\n:white_check_mark: *Q3 Strategy Doc shared* (Aug 20) - human-written, in Leads Slack, comments due Aug 21.\n:white_check_mark: *Jon Wanczyk officially day-to-day Hiring Sales lead* - high trust, strong start.\n:white_check_mark: *Page Templates: SHIPPED* - rolling out. Done.\n:white_check_mark: *Somia - 3 email drip initiatives in flight* - payroll users, non-payroll team app, hiring clickers.\n:white_check_mark: *15% hiring chip click rate at signup* - consistent 3-month signal. Strong foundation for Somia's drips."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WATCH LIST - Keep on Radar*\n\n• *Indeed OTP/fraud flow:* Sprint after next. Designs finishing (Laura Hulse). Juan tracking repeat fraud attempts (Inspire Brands + Wells Fargo changed method, didn't stop). Monitor.\n• *Dashboard 'views' label:* Customer confusion risk - only shows Homebase career page views, not Indeed/ZR. Consider a PM ticket.\n• *Sales framing:* NEVER say 'AI.' Screener = 'a screener that does the job for you.' Jon should reinforce with the sales team.\n• *Homebase boost messaging:* Talroo (not ZR), say Jobget externally. Check product copy is consistent - Zane may not know this.\n• *Gbolade feedback session:* 15-min still open. Schedule this week.\n• *Abby (new PM hire):* Needs a clear ownership area. Define this with Sky in week 1.\n• *BarTaco:* ~8 weeks until Paylocity/Grayscale pilot ends. That's your close window. Rushi needs the Scott Rodney intro moving.\n• *Jobcase (Matan):* Follow-up still open post Aug 18 meeting.\n• *PJ's Coffee Indeed escalation:* Still open (Christofer owns).\n• *Scooters follow-up:* Still open (Olivia/Maria/Lacey)."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Q3 SCOREBOARD (heading into week 5 of Q3)*\n\n| Metric | Current | Target |\n|--------|---------|--------|\n| FFH D5 zero-applicant rate | 41% | <10% |\n| Line cook jobs healthy | ~7% | 50% |\n| Healthy job rate (ICP) | 30% | 80% |\n\nYou're not going to hit these with 5 weeks left in Q3 on the metrics alone - but you know that. The story to tell is: *what's locked and shipping* (OTQ fraud fix, email drips, Indeed applicants D3) and *what the structural answer is* (Talent Pool). Frame it that way with Sky."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MANAN - A WORD FROM YOUR CHIEF OF STAFF*\n\nYou had a genuinely strong week. Three big decisions in one Friday (OTQ email flow locked, internal job posting added to roadmap, abandonment survey rework scoped, BarTaco strategy clarified, PM/sales sync consolidated). You're building the John+Matan+Manan trio which is the right move.\n\nMonday is a big day. Sky is smart, experienced, and has built things like this before. Your job isn't to have all the answers - it's to frame the right questions and show him where you need his judgment. Lead with: *what's working* (applicant flow conversion, OEM, Jon leading sales), *what's the core problem* (jobs not reaching Indeed, not conversion), and *what's the answer* (Talent Pool as strategic bridge + fraud removal). You've got this.\n\nEnjoy the rest of your Saturday. See you Monday. :rocket:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff digest | Saturday Aug 22, 2026 | 5pm PDT | No Granola meetings today | Next digest: Monday Aug 25"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Saturday EOW Wrap + Monday Battle Plan (Aug 22) - Sky starts Monday!"
}


def preview():
    sys.stdout.buffer.write(b"\n=== SLACK MESSAGE PREVIEW ===\n")
    for block in blocks:
        if block.get("type") == "section":
            text_obj = block.get("text", {})
            sys.stdout.buffer.write((text_obj.get("text", "") + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            sys.stdout.buffer.write(("### " + block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")


if not TOKEN:
    print("No SLACK_TOKEN/SLACK_BOT_TOKEN/SLACK_API_TOKEN found - printing preview only.")
    preview()
    sys.exit(0)

body = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=body,
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
        print("SUCCESS: Message sent to Slack channel", CHANNEL)
        print("Timestamp:", result.get("ts"))
    else:
        print("SLACK API ERROR:", result.get("error"))
        print("Full response:", json.dumps(result, indent=2))
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print("NETWORK ERROR:", e)
    preview()
    sys.exit(1)
