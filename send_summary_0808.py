#!/usr/bin/env python3
"""
Saturday Aug 8 EOW + Monday Aug 10 Battle Plan
Chief of Staff Daily Digest for Manan Kothari
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

def get_token():
    for k in ("SLACK_TOKEN", "SLACK_BOT_TOKEN", "SLACK_API_TOKEN"):
        v = os.environ.get(k, "")
        if v:
            return v
    return ""

def send_blocks(token, blocks, fallback_text):
    payload = json.dumps({
        "channel": CHANNEL,
        "text": fallback_text,
        "blocks": blocks
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    return body

def preview(blocks, fallback_text):
    sys.stdout.buffer.write(b"\n=== PREVIEW (no Slack token) ===\n")
    sys.stdout.buffer.write(fallback_text.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")
    for b in blocks:
        t = b.get("text", {})
        if isinstance(t, dict):
            sys.stdout.buffer.write(t.get("text", "").encode("utf-8", errors="replace"))
            sys.stdout.buffer.write(b"\n")
    sys.stdout.buffer.write(b"================================\n")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Saturday Evening Check-In + Monday Aug 10 Battle Plan",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Hey Manan!* Saturday evening here. No meetings today (as expected), but Monday is one of the most loaded days you have had in months. I have pulled everything together so you can walk in completely locked and loaded. Let's make it a great week!"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *ACTIVE FIRE: Indeed Watch List*\n>Homebase is still flagged for fraudulent jobs (flagged Aug 5). ~60% of your applicant volume flows through Indeed. If strict review mode kicks in, new client jobs simply will not appear. You were supposed to email your Indeed contact *this weekend.* If you have not done this yet, send that email right now before bed tonight. This is your single highest-urgency item."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *ACTIVE FIRE: 422 Job Publishing Errors*\n>Day *29* as of today. Jatin is on the RCA. Ray is out, which means *you are the decision-maker.* Get a status update from Jatin first thing Monday. If there is a fix path, unblock it. This cannot drag into week 5."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":mega: *MONDAY DELIVERABLES (Due Before EOD)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Strategy Deck for John + Ray* :large_green_circle:\n>Full roadmap-to-goals deck, framed around the two core FFH metrics: 500 FFH paying customers + 70% FFH with healthy jobs. Include the Engineer Ownership POC as a concept (Martin is back Monday and needs to weigh in before you finalize). Have Fadi + Jatin review it first. Make sure the four focus areas are crisp: (1) trial starts, (2) unblocking applicant flow, (3) core light touches, (4) retention at 85-90%.\n>*Action:* Send deck to Fadi + Jatin for review first thing Monday AM, incorporate feedback, present to John + Ray."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Sprint Retro* :spiral_notepad:\n>Jatin is setting it up for Monday. This is a team ritual you own. Show up prepared with your retrospective notes from last sprint.\n>*Action:* Come with your own retro points written down. Make it a great session."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *MONDAY MORNING FIRST HOUR: Unblock These People*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":busts_in_silhouette: *Dana Lobo - Page Templates Handoff (CONFIDENTIAL)*\n>Dana returns Monday Aug 10. She has *2 working days left* (last day Aug 12). Page Templates ownership is still unresolved. Fadi has been getting conflicting info from two different people about who owns it. This hand-off is critical. Resolve this Monday AM first thing so Dana can do a clean knowledge transfer in her final 2 days.\n>*Action:* DM Dana + Fadi immediately Monday AM. Lock in ownership. Block 30 min with Dana for handoff sync."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":busts_in_silhouette: *Fadi Rizk - Boost Modal Figma (~10+ days overdue)*\n>Fadi is blocked on YOU for the Boost modal Figma review. This has been sitting for over 10 days. Unblock him Monday.\n>*Action:* Review and give Fadi your feedback on the Boost modal Figma by 10am Monday."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":busts_in_silhouette: *Izzy (Iszael Gonzalez) - Reactivate Feature*\n>Reactivate was due on staging as of Aug 6. You wanted to confirm this Monday.\n>*Action:* Ping Izzy Monday AM. Is it on staging? If not, what is the blocker?"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":busts_in_silhouette: *Martin (Eng Lead) - Engineer Ownership POC*\n>Martin was out last week. He needs to weigh in on the Engineer Ownership POC before it goes into the Monday deck. Loop him in ASAP Monday.\n>*Action:* Slack Martin first thing. Share the concept. Get his gut check."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *KEY THIS WEEK (Aug 10-14)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":star: *Meet with Sky (New Head of Product)*\n>Sky was introduced Aug 5 with 15-20 years of B2B marketplace experience, already built a voice agent prototype for job posting. She is your new skip (replacing Ray who is transitioning to a builder role). Align early this week on Q3 roadmap direction.\n>*Action:* Get on Sky's calendar for a 1:1 this week. Come with your Q3 priorities pre-articulated."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":test_tube: *JD Prompt Box A/B Experiment (IBK, week of Aug 10)*\n>Greenlit Aug 6. IBK is running it as a 50/50 test, skipping the prompt box page and dropping users directly on the details page. Based on your data: 60% of users currently drop off on the JD page, so this experiment could be a big unlock.\n>*Action:* Confirm with IBK that the experiment is live or being launched this week. Set up a check-in for results."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":chart_with_upwards_trend: *Amplitude Dashboard - Share with Matan (OVERDUE)*\n>This has been sitting since Aug 6. Matan needs this.\n>*Action:* Share the Amplitude dashboard with Matan Monday. 2-minute task. Do not let this drag into another week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":survey: *Applicant-Count Survey (Great Question)*\n>You are building a survey to distinguish desperation vs satisfaction at ~15 applicants. Team needs to review it.\n>*Action:* Send the draft survey to the team for review this week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":dna: *Rami Business Case to Ted*\n>Ted (DS lead) is pulling back from hiring after Karan's departure. Rami's involvement is likely temporary. You need to make the business case directly to Ted to retain Rami for the hiring team.\n>*Action:* Schedule time with Ted this week. Come with a clear case for why DS resources are critical to Q3 goals."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":art: *Meta Ads Timing-Targeting Feasibility*\n>Needs validation with Jenna before you commit to this direction.\n>*Action:* Ping Jenna this week. Validate feasibility before it goes on any roadmap."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":seedling: *ONGOING THREADS TO NOT LOSE*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Domain Events*: Malcolm completing FINAL PR (Bob reviewing); Kafka topics live. Nearly done. Check in Monday.\n• *Comms Agent*: Malcolm back on it Aug 5; spike on incoming SMS handling first. Jatin is pushing for experiment. You own the decision with Ray out.\n• *Soheil dynamic threshold*: configurable for experimentation, in progress.\n• *Culinary Agents*: STILL blocked on Gray (vendor legal). No action needed from you right now.\n• *Matan PMM roadmap*: Matan committed to adding to the Google Sheet by EOD Aug 6 or within a week. Follow up if not done.\n• *Scooters follow-up*: Olivia / Lacey email still open. Do not let this slip.\n• *PJ's Coffee (Yvonne) Indeed escalation*: Christofer owns the fallback. Check status this week.\n• *Abby (new PM)*: Week 9+. She needs a clear ownership area. Think about what that looks like this sprint.\n• *Gbolade*: Has a 'reduce time from problem to PR' feature ready. Needs a 15-min PM feedback session with you."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":bar_chart: *Q3 SCORECARD SNAPSHOT*\n>• FFH D5 zero-applicant rate: 41% (target: <10%)\n>• Line cook jobs healthy by D30: 7% (target: 50%)\n>• Healthy job rate: 30% of ICP jobs (target: 80%)\n>• ARR: $650K+ | Total accounts: 800K\n>• MBR July: 178 (Jun) → 199 (Jul) = +11.8% MoM :arrow_up: | Quality softened: 19% → 26.5% low-match :arrow_down:"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":brain: *MANAN'S MONDAY PRIORITY ORDER*\n>1. Email Indeed contact (if not done tonight)\n>2. Resolve Dana Page Templates handoff — first 30 min of day\n>3. Unblock Fadi Boost modal Figma review\n>4. Loop Martin in on Engineer Ownership POC\n>5. Get 422 error status from Jatin\n>6. Ping Izzy on reactivate staging status\n>7. Sprint retro\n>8. Strategy deck final review + present to John + Ray\n>9. Get on Sky's calendar for 1:1 this week\n>10. Share Amplitude dashboard with Matan (literally 2 mins)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You have got this, Manan. This is a huge week but you are set up to deliver. Monday is your moment. Go crush it! :muscle:"
        }
    }
]

fallback = "Saturday Aug 8 EOW + Monday Aug 10 Battle Plan - Chief of Staff Daily Digest"

token = get_token()
if not token:
    preview(blocks, fallback)
    print("No Slack token found. Printed preview above.")
    sys.exit(0)

try:
    result = send_blocks(token, blocks, fallback)
    if result.get("ok"):
        print("Message sent successfully!")
    else:
        print(f"Slack API error: {result.get('error', 'unknown')}")
        preview(blocks, fallback)
        sys.exit(1)
except Exception as e:
    print(f"Error sending message: {e}")
    preview(blocks, fallback)
    sys.exit(1)
