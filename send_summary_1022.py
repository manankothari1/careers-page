#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Thursday, Oct 22, 2026
Meetings reviewed: Iszael/Manan (8am), Hiring EPD Standup (8:45am), Indeed Bug Call (2:30pm)
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
            "text": "\U0001f306 Thursday, Oct 22 — Chief of Staff Digest",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Day 61 Indeed RECOVERED  \u00b7  Day 29 Facebook API  \u00b7  3 meetings today  \u00b7  Town Hall + Match Workshop *TOMORROW*"
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af THEME OF THE DAY*\n*INDEED BUG CONTAINED \u00b7 JD VERDICT DUE NEXT WEEK \u00b7 CRITICAL NIGHT AHEAD*\n\nYou fought two real fires today and came out ahead. The Indeed company-name routing bug is mitigated, the zombie profile link in applicant emails is gone, and Divij is unblocked and moving. The cost: everything that matters for Friday is still sitting in your queue. Let\u2019s fix that tonight."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2696\ufe0f DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. \U0001f6a8 Indeed Company Field Bug \u2014 Mitigated*\n*What:* Multiple unrelated businesses sharing the same company name triggered a routing/dedup conflict on Indeed. Bob\u2019s PR merged mid-call \u2014 company field is now *temporarily paused* from being sent.\n*Rationale:* Net new jobs will have the identifier removed. Existing jobs left as-is \u2014 reposting would cascade across all syndication partners, not worth it.\n*Next:* Reply via the existing Indeed support ticket (cover: what changed, real customer impact examples, request their recommended solution for multi-business same-name scenarios). Share draft in team chat before firing. Bob updates Michael directly."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": '*2. \U0001f4e7 Applicant Email \u2014 \u201cYour Profile\u201d Link Permanently Removed*\n*What:* The post-application email had a \u201cYour profile\u201d nav link redirecting to nothing \u2014 candidate profile (V1) is sunset and *not coming back.*\n*Decision:* Strip both the job role link and profile hyperlink. Short-term copy: plain text \u201cYou applied to [role] on [date].\u201d Longer-term: proper email redesign.\n*Rationale:* Clean > broken. Profile product direction is confirmed closed.'
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. \U0001f517 Jobcase Integration \u2014 Effectively Parked*\n*What:* No reply from Jamie/Jane in 3+ weeks. Earnin also deprioritized (blocked by partnership).\n*Decision:* Iszael to formally close out with Jobcase rather than let it drift.\n*Rationale:* Don\u2019t let partner threads go cold for weeks \u2014 set a clean status and move on."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. \U0001f9e0 JD Content + Thresholds \u2014 Verdict Due w/c Oct 26*\n*What:* Divij has kicked off hiring count + frequency work in the job creation flow. Job parsing is good. He is *blocked on your product verdict* \u2014 specifically: what hiring info to include in the JD and exact threshold values.\n*Decision:* Confirm verdict by the week of Oct 26th.\n*Rationale:* Divij is unblocked on everything else. This is the only input he needs from product to move."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f525 YOUR ACTION ITEMS*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f534 TONIGHT \u2014 Non-Negotiable*\n\n\u25a2 *Submit Town Hall Q&A questions* \u2014 overdue since Monday. Town Hall is *tomorrow morning.* Do this first.\n\n\u25a2 *Match Explanation pre-work* \u2014 audit raw match data, identify gaps. FigJam workshop with Fadi is *tomorrow.* No prep = wasted session.\n\n\u25a2 *Draft + share Indeed support reply* \u2014 share in team chat for review before sending. Cover: (a) what changed + why, (b) real customer impact examples, (c) company field temporarily paused, (d) request Indeed\u2019s recommended solution for multi-business same-name.\n\n\u25a2 *Write JD rules doc for Divij* \u2014 rules for when to include count (1 hire = vanilla; 2+ = \u2018multiple positions\u2019) and urgency (\u22642wk = \u2018urgently hiring\u2019). Define reference date (posted vs activated) and ASAP definition. This is BLOCKING DS work."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f7e1 BEFORE NEXT TUESDAY*\n\n\u25a2 *Spec Swarm N+1 decision (with Fadi)* \u2014 bring hiring count+speed into next Tue\u2019s swarm, or wait for N+2? No verdict spike = carryover risk. Decide this weekend.\n\n\u25a2 *Pre-align with Matan + Skye on GTM Lookahead N+1* \u2014 Matan is bringing work into next Tuesday\u2019s meeting. Get ahead of it."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb WATCH LIST \u2014 KEY UPDATES*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u26a0\ufe0f *NIHILUS \u2014 11 DAYS TO NOV 3 DEADLINE.* Izzy still scoping build cost. Decision needed before renewal. Leaning: stay Q4, remove Q1. This has been on the list too long.\n\n\U0001f6a8 *SMS SLO Failures \u2014 FLAGGED TODAY.* SMS send failures spotted in standup. Iszael investigating after Facebook Jobs fix wraps. Keep an eye on this.\n\n\U0001f4dd *2029 Vision One-Pager \u2014 CRITICALLY OVERDUE.* Fadi submitted his (with design deck). You have not. Board meeting opened Oct 15. Block 90 min this week.\n\n\U0001f4f1 *Facebook API \u2014 Day 29. Still dark.* Bob + IBK. No update since Oct 9. Escalate?\n\n\U0001f9e0 *Carlo KT \u2014 Not Confirmed.* On paternity through mid-Feb. Knowledge risk is real and growing.\n\n\U0001f4bb *Malcolm Out Halloween Onward.* Comms assistant production decision still OVERDUE. Clock is ticking.\n\n\U0001f4e6 *INDEED XML Feed \u2014 Make Private.* Jatin waiting on Ashley. Jatin is OOO today/tomorrow (Austin). Follow up Monday.\n\n\u26a0\ufe0f *Sohail Missing from Standup Invite.* Jatin owns the fix but is OOO. Consider adding him manually \u2014 don\u2019t let this slide another week."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4c5 TOMORROW \u2014 FRIDAY OCT 23*\n\n\U0001f3a4 *Town Hall* \u2014 Q&A questions needed TONIGHT (overdue since Monday)\n\U0001f9e9 *Match Explanation FigJam Workshop* (with Fadi) \u2014 raw data audit pre-work needed TONIGHT\n\U0001f6ab *Jatin OOO* through tomorrow (Austin). Back Monday.\n\U0001f44b *Matt McAllister* \u2014 new CMO, Week 2 starts Monday. Good time to connect."
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "*Day Grade: A-* \u2014 Good fires fought and contained (Indeed bug, email zombie link). Divij is unblocked. But tonight is loaded \u2014 Town Hall Q&A + match pre-work + Indeed draft + JD doc. You\u2019ve got this. \U0001f4aa"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest \u2014 Thursday Oct 22",
    "blocks": blocks
}

def preview():
    msg = "\n===== SLACK PREVIEW (no token) =====\n"
    msg += "TO: " + CHANNEL + "\n"
    msg += "---\n"
    for b in blocks:
        if b["type"] == "header":
            msg += "\n### " + b["text"]["text"] + "\n"
        elif b["type"] == "section" and "text" in b:
            msg += b["text"]["text"] + "\n\n"
        elif b["type"] == "context":
            for el in b.get("elements", []):
                msg += "[ctx] " + el.get("text", "") + "\n"
        elif b["type"] == "divider":
            msg += "---\n"
    msg += "\n===== END PREVIEW =====\n"
    sys.stdout.buffer.write(msg.encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()

def send(token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + token
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print("SUCCESS: message sent to " + CHANNEL)
            else:
                print("SLACK ERROR: " + result.get("error", "unknown"))
                preview()
    except Exception as e:
        print("REQUEST ERROR: " + str(e))
        preview()

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

if token:
    send(token)
else:
    print("No Slack token found. Printing preview.")
    preview()
