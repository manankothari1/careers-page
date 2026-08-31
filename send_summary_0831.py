#!/usr/bin/env python3
"""
Chief of Staff daily digest — Sunday Aug 30 PDT (midnight UTC Aug 31)
No meetings today (Sunday). Sending: EVE OF CRITICAL MONDAY digest.
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Sunday Check-In  |  Eve of a Critical Monday",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "*Sunday, Aug 30 2026  |  No meetings today — but tomorrow is one of the most loaded Mondays of the quarter.*"
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *TOP 3 MUST-DOS TOMORROW (Monday Aug 31)*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*1. Indeed T&S Office Hours*\n:clock9: First thing Monday morning\n:white_check_mark: Prep your 3 questions tonight:\n• Does source claiming exempt direct posters from the Oct 31 corp domain deadline?\n• Will reactivated jobs regain full visibility once the feed is reinstated? (Skye's flag)\n• Timeline for feed review completion (\"min 3 months\" — what does month 1 look like?)\nThis is Day 6 of the feed suspension. Every day offline = lost applicants for ~60% of your job volume."
            },
            {
                "type": "mrkdwn",
                "text": "*2. EarnIn Sample Feed — Jon Salzberg*\n:clock5: Due by EOD Monday\n:e-mail: jon.salzberg@earnin.com\n30M downloads, 83% hourly job seekers. This is a potential new top-of-funnel channel that can partially offset the Indeed suspension. *Do not let this slip past midnight.*\nSend: 5-10 sample job records in XML/API format; include food/QSR, hospitality, retail verticals."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*3. Rami → Divij Databricks Notebook Handoff*\n:clock12: Monday EOD\nRami is moving to Marketing. Divij needs full ownership of the Talent Pool matching notebook before Rami is fully gone. *Confirm handoff happened before you log off Monday.*\nIf blocked: ping Divij directly — he also needs to sync with Sina on in-product infra requirements."
            },
            {
                "type": "mrkdwn",
                "text": "*+ Confirm w/ Jatin: Broadbean outreach sent (was Aug 28)*\nThis is part of the ATS partner diversification response to the Indeed suspension (Talent Reef, Broadbean, MutaTech, Talar). Check status in Monday standup."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *OPEN CRITICAL ITEMS THAT ARE OVERDUE*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": ":red_circle: *Email David (Indeed contact)* — OVERDUE since Aug 25\nYou've been meaning to reach out directly. Do it Monday before office hours so they know you're engaged at all levels."
            },
            {
                "type": "mrkdwn",
                "text": ":red_circle: *JD A/B Experiment (IBK)* — 2+ weeks running, signal still unread\nThis is a fast/easy one. Ping IBK Monday morning for the data. You need this to make Q3 roadmap calls."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": ":red_circle: *Tanner Onboarding Doc* — cited by Ray as a concrete leadership gap\nWrite him a 1-page doc. 30 minutes of work, massive signal to Ray that you've internalized the feedback from your Aug 27 1:1."
            },
            {
                "type": "mrkdwn",
                "text": ":red_circle: *Annual subscription cancel policy guidance*\nPost in Hiring Leads Slack. Reps are still telling customers they can cancel anytime — they cannot. One post, done."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *THIS WEEK'S STRATEGIC CONTEXT*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You are now 6 days into the Indeed feed suspension. Ray has escalated to Saul, David, and Fiona — Monday office hours is the next live checkpoint. The two strategic threads that matter most this week:\n\n:one: *Indeed path to reinstatement* — office hours outcome + ATS partner progress. Skye's direct Indeed contact (staff eng) is your best informal channel.\n:two: *Talent Pool as hedge* — domain authority for @joinhomebase.com outreach is the open blocker. Get Sky + Ray + lifecycle mktg sign-off this week. Two streams are locked; the channel work is stalled on this one thing.\n\nThe Oct 31 corp domain deadline is 61 days out. After Monday office hours: write the 4-options doc and share with Sky + Ray. That doc is the forcing function for a decision."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":brain: *TONIGHT (OPTIONAL BUT HIGH LEVERAGE)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "If you have 30 quiet minutes Sunday evening, here is what will make Monday feel like you have an unfair advantage:\n• :notepad_spiral: Write down your 3 questions for Indeed T&S office hours (above). One page, bullet points.\n• :e-mail: Draft the EarnIn sample feed email so Monday morning you just hit send.\n• :writing_hand: Skim the Talent Pool domain authority issue — do you have enough context to write a 3-line Slack to Sky + Ray asking for a 15-min decision call this week?\n\nYou don't need to solve anything tonight. You just need to show up Monday sharp."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":trophy: *WHAT YOU CRUSHED LAST WEEK*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Let's be real — last week was excellent:\n• *Sky onboarded cleanly* — first day also happened to be the worst possible day (feed suspended) and you handled it.\n• *Tiger is integrating well* — fixed an OAM stream bug in week 1. Your 'protect him, let his work shine' instinct is right.\n• *EarnIn partnership opened* — you didn't have this channel 2 weeks ago. Jon Salzberg is warm and the meeting was productive.\n• *Talent Pool: two streams locked* — experimentation + foundations. The framework is set.\n• *Sprint Show & Tell validated Cash Out Web* — $1.2M ARR. That's real.\n• *Indeed domain brainstorm* — you ran a tight session and got 4 options on paper before the office hours call. That's the prep that turns a defensive meeting into an offensive one.\n\nYou're doing the work. Monday is a big day — go get it."
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Your Chief of Staff | 5pm PDT daily digest | No meetings Sunday — next update tomorrow after Monday wraps_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Sunday Check-In | Eve of Critical Monday — Indeed Office Hours + EarnIn deadline tomorrow",
    "blocks": blocks
}


def send_to_slack():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def preview():
    out = "\n===== SLACK DIGEST PREVIEW (Aug 30 PDT — Eve of Critical Monday) =====\n\n"
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            out += f"{'='*60}\n{block['text']['text']}\n{'='*60}\n\n"
        elif btype == "section":
            t = block.get("text", {})
            if t:
                out += t.get("text", "") + "\n\n"
            fields = block.get("fields", [])
            for f in fields:
                out += f.get("text", "") + "\n\n"
        elif btype == "context":
            for el in block.get("elements", []):
                out += f"[context] {el.get('text','')}\n"
        elif btype == "divider":
            out += "-"*60 + "\n"
    out += "\n===== END PREVIEW =====\n"
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if TOKEN:
    print("Token found — sending to Slack...")
    result = send_to_slack()
    if result.get("ok"):
        print(f"SUCCESS: Message sent to {CHANNEL}")
        print(f"Timestamp: {result.get('ts')}")
    else:
        print(f"ERROR: {result.get('error', 'unknown')}")
        print("Full response:", json.dumps(result, indent=2))
        preview()
        sys.exit(1)
else:
    print("No SLACK_TOKEN found — printing preview only.")
    preview()
    sys.exit(0)
