#!/usr/bin/env python3
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = []

# Header
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f319 Sunday Evening Check-In \u2014 Aug 2, 2026*\n"
            "No meetings today (Sunday) \u2014 and that\u2019s completely fine. "
            "This IS your daily summary. More importantly, it\u2019s your *Monday Morning Battle Plan* "
            "for the most consequential week of your Q3.\n\n"
            "*No Ray. No Dana. You are the captain this week.* \U0001f9ed"
        )
    }
})

blocks.append({"type": "divider"})

# Week at a glance
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f6a8 WEEK AT A GLANCE \u2014 Aug 3\u20137*\n\n"
            "\u2022 *Ray is OUT all week* \u2192 You are the sole decision-maker on everything\n"
            "\u2022 *Dana is OFF Mon\u2013Fri this week* \u2192 Returns Aug 10 \u2192 *2 working days* before her last day (Aug 12)\n"
            "\u2022 *Carlo back from Canada holiday \u2192 Monday Aug 4* \u2192 Have the direct conversation ready\n"
            "\u2022 *MBR:* Ray + Dana both out \u2192 you drive the applicant side section *solo*\n\n"
            "_9 days until Dana\u2019s last day. This week defines the transition._"
        )
    }
})

blocks.append({"type": "divider"})

# Dana succession
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\u23f0 P0: Dana Succession \u2014 The Clock Is Ticking*\n\n"
            "Dana goes dark *tomorrow (Monday)*. She returns Aug 10 for exactly *2 working days* before Aug 12. "
            "You need to reach her *before she fully goes offline* \u2014 ideally tonight or first thing tomorrow morning.\n\n"
            "*What needs to be locked before she\u2019s gone:*\n"
            "\u2022 *ICP experiments:* Matan is the bridge, but you need the full context directly from Dana\n"
            "\u2022 *Page Templates ownership:* who picks this up? No plan exists yet\n"
            "\u2022 *In-flight work only Dana holds:* any decisions, stakeholder relationships, or strategic context\n"
            "\u2022 *Her relationships with Ted, Ray, and the incoming GM of Hiring*\n\n"
            "_Remember: CONFIDENTIAL until the formal Slack announcement._"
        )
    }
})

blocks.append({"type": "divider"})

# P0 Hit List
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f3af P0 HIT LIST \u2014 Monday Aug 4*\n\n"
            "1\ufe0f\u20e3 *Send Fadi the Boost modal Figma* \u2014 7 days overdue. First 5 minutes of your Monday. Just do it.\n"
            "2\ufe0f\u20e3 *Carlo direct conversation* \u2014 He\u2019s back from Canada on Monday. 18+ days overdue on Harness/OpenSpec. "
            "This is a real management moment \u2014 be direct, be caring, get to a clear next step today.\n"
            "3\ufe0f\u20e3 *Reach Dana before she goes dark* \u2014 ICP context dump, Page Templates handoff, succession brief\n"
            "4\ufe0f\u20e3 *Ted: Rami business case* \u2014 Go direct. Ray is out. Make the case (applicant quality + Marketplace impact). "
            "Rami\u2019s involvement is at risk. Don\u2019t let another week pass.\n"
            "5\ufe0f\u20e3 *Confirm Bob + Jonathan comms agent sync outcome* \u2014 Jul 29 3pm sync had no Granola notes. "
            "What was resolved on data/DS vs. product eng ownership? You need this before calling the comms agent decision.\n"
            "6\ufe0f\u20e3 *Scooters follow-up email* \u2014 Olivia, Maria, Lacey: TalentReef migration + Lacey\u2019s written confirmation\n"
            "7\ufe0f\u20e3 *MBR applicant side section* \u2014 Solo mission this week. Get it started today."
        )
    }
})

blocks.append({"type": "divider"})

# Open decisions
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\u2696\ufe0f OPEN DECISIONS YOU\u2019RE CALLING THIS WEEK (Ray is OUT)*\n\n"
            "*1. Comms Agent Manual Experiment*\n"
            "Jatin wants to kick off the manual experiment this week (team texts candidates from personal phones). "
            "Cena: 1.5\u20132 sprints for data eng. Ray\u2019s ask: you + Jatin sit with Cena to surface hidden assumptions first. "
            "With Ray out, *this is your call*. Recommended: 30-min Manan + Jatin + Cena sync before committing.\n\n"
            "*2. 422 Errors \u2014 Day 24 on Monday*\n"
            "Jatin owns RCA. You own the decision: stakeholder comms, escalation path, or hold. "
            "What\u2019s the call this week? Get aligned with Jatin first thing Monday.\n\n"
            "*3. ICP Experiments Sync with Matan*\n"
            "Dana is out all week. Matan is your bridge. Get fully up to speed on ICP experiment status by EOD Monday.\n\n"
            "*4. Rami\u2019s Involvement (Data Science)*\n"
            "Ted is pulling back on DS resources after Kan\u2019s departure. Without Rami: JD quality analysis, "
            "talent pool experiments, and competency normalization all slow down significantly. "
            "Build the business case this week and take it to Ted directly."
        )
    }
})

blocks.append({"type": "divider"})

# Still open items
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f4cb STILL OPEN \u2014 Don\u2019t Let These Die*\n\n"
            "\u2022 *Franchise ticket* (5+ days) \u2014 unique source ID per franchise + company name field from Jul 29 Indeed call\n"
            "\u2022 *Indeed noindex help article* \u2014 copy locked Jul 30; the actual article still hasn\u2019t been written\n"
            "\u2022 *Matan comms doc review* \u2014 Sonia is blocked until you review; unblock her this week\n"
            "\u2022 *Talent Pool Outreach* \u2014 Carlo\u2019s rake task (1\u20132 days); he was out last week. Confirm status when he\u2019s back Monday\n"
            "\u2022 *Juan Sanchez email issue* \u2014 still unresolved\n"
            "\u2022 *Izzy + Tanner API contract alignment* \u2014 role rec + salary reco endpoint contract\n"
            "\u2022 *Usman candidate email experiment results* \u2014 check the data; still unchecked\n"
            "\u2022 *Jubs weekly cadence with Matan* \u2014 new strong sales partner; Denver trip in ~1 month"
        )
    }
})

blocks.append({"type": "divider"})

# Watch List
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f440 WATCH LIST*\n\n"
            "\u2022 *Dana last day: Aug 12 = 9 calendar days away.* Succession bridge must be built THIS WEEK.\n"
            "\u2022 *SBA:* launched Jul 27 \u2014 watching unassigned grid P1 data (friendly testing was negative)\n"
            "\u2022 *422 errors:* Day 24 Monday \u2014 Jatin on RCA \u2014 you\u2019re the decision-maker with Ray out\n"
            "\u2022 *Usman:* Ray had a direct performance conversation \u2014 passive behavior flagged; follow the signal\n"
            "\u2022 *Q3 targets:* FFH D5 zero-applicant <10% (currently 41%) | 50% line cook healthy (currently ~7%)\n"
            "\u2022 *\u2018Bring Your Own Indeed\u2019:* Ray\u2019s open concept from Jul 27 \u2014 don\u2019t let it lose momentum with Ray out"
        )
    }
})

blocks.append({"type": "divider"})

# Closing message
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "*\U0001f4aa You\u2019ve Got This, Manan.*\n\n"
            "You\u2019ve made 50+ decisions this month that have genuinely moved the needle \u2014 "
            "candidate matching shipped, Talent Pool greenlit, Boost copy locked, FFH architecture locked, "
            "role recs combined gRPC, SBA launched. This week is your moment to show the organization "
            "exactly what you\u2019re made of. Ray trusts you. Dana trusts you. *The team trusts you.*\n\n"
            "Go get it. \U0001f680 \U0001f3e0"
        )
    }
})

payload = {
    "channel": CHANNEL,
    "text": "Sunday Evening Check-In + Monday Battle Plan \u2014 Aug 3 Week (Ray + Dana OUT)",
    "blocks": blocks
}


def send_slack(token, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def preview(payload):
    sys.stdout.buffer.write("=== SLACK PREVIEW ===\n".encode("utf-8", errors="replace"))
    for block in payload.get("blocks", []):
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("---\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("=== END PREVIEW ===\n".encode("utf-8", errors="replace"))


token = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)

if not token:
    print("No SLACK_TOKEN found \u2014 printing preview instead.")
    preview(payload)
    sys.exit(0)

result = send_slack(token, payload)
if result.get("ok"):
    print(f"Message sent successfully! ts={result.get('ts')}")
else:
    print(f"Error sending message: {result.get('error')}")
    preview(payload)
    sys.exit(1)
