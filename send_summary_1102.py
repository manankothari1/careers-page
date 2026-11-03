#!/usr/bin/env python3
"""Daily chief-of-staff digest for Manan Kothari -- Mon Nov 2, 2026 PST"""
import json, os, sys, urllib.request, urllib.error

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
            "text": "\U0001f4cb Chief of Staff Digest \u2014 Monday, Nov 2, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day Grade: B+* \u2014 Productive Lookahead with full team, 3 bodies of sprint work scoped and debated. "
                "The one shadow: Nihilus subscription deadline was TODAY and no meeting was captured about it. That needs your attention NOW.\n\n"
                "*\U0001f3af Theme:* SCHEDULING RELIABILITY = SPRINT 26.24 GOAL \u2014 NO-SHOW CRISIS ADDRESSED \u2014 NIHILUS CLOCK STILL TICKING"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4c5 Meetings Today (3)*\n"
                "\u2022 8:45am \u2014 HB Assistant Standup _(workspace intel)_\n"
                "\u2022 10:00am \u2014 Palmetto Superfoods customer interview w/ Keyvan _(workspace intel)_\n"
                "\u2022 11:00am \u2014 *\U0001f4bc Hiring Lookahead (N+2)* \u2014 full team w/ Skye, Jatin, Fadi, Matan, IBK, Divij, Tiger, Bob, Iszael, Jon, Martin, Malcolm, Carlo, Michael H."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. No auto-cancellation in Interview Confirmation v1*\n"
                "_Source: Hiring Lookahead_\n"
                "Research (doctors offices, appointment systems) shows many candidates who don\'t confirm via SMS still show up. "
                "Auto-cancel risks losing good candidates who are simply non-responsive to texts. "
                "Decision: notify OEM 2hrs before if no confirmation, but KEEP the interview on the books. "
                "Bob pushed for A/B test; Manan overruled citing existing research.\n"
                "_Why it matters: This shapes the entire comms agent v2 build. No rollback complexity, cleaner first launch._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. No 'Cancel' option in Interview Confirmation v1*\n"
                "_Source: Hiring Lookahead_\n"
                "Michael suggested adding a Cancel option to the SMS flow. Manan\'s call: ship with Confirm + Reschedule only. "
                "Learn from reschedule-to-no-follow-up data first, then add Cancel in v2 if the data supports it.\n"
                "_Why it matters: Keeps scope tight. Cancel creates OEM-side rescheduling complexity we don\'t need on day 1._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Pre-existing jobs GRANDFATHERED from count/speed required fields*\n"
                "_Source: Hiring Lookahead_\n"
                "Gbolade raised the backfill concern: making count/speed required fields forces a DB migration for all existing jobs. "
                "Resolution: net-new jobs only are required to fill these fields; pre-existing jobs are grandfathered. Exact cutoff date TBD.\n"
                "_Why it matters: Unblocks IBK from a major backfill scope that would have pushed the timeline weeks._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Hiring urgency field design: DEFERRED (30-day default is Manan\'s lean, not yet locked)*\n"
                "_Source: Hiring Lookahead_\n"
                "Martin suggested defaulting to 'immediate' to reduce friction. Bob pushed back \u2014 a default of ASAP removes the signal value. "
                "Jatin suggested qualitative labels instead of a date picker. Fadi noted pre-select chips already exist. "
                "Manan\'s lean: default to 30 days (current norm). Not finalized \u2014 Fadi to prototype and team to review.\n"
                "_Why it matters: This is a 2-way door \u2014 we can adjust post-launch. Don\'t let the debate block IBK from building._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Sprint 26.24 goal = scheduling reliability for OEMs, THREE bodies of work*\n"
                "_Source: Hiring Lookahead_\n"
                "Officially locked: (a) Candidate profile context-aware CTAs, (b) Hiring count + speed capture, (c) Interview confirmation. "
                "Scheduling deep-dive scoped for *Wednesday* \u2014 full squad discovery session, invite going out from Jatin.\n"
                "_Why it matters: This is the sprint north star. Everything else is noise until these 3 ship._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Candidate profile CTAs: Move Forward KILLED, context-aware states LOCKED*\n"
                "_Source: Hiring Lookahead_\n"
                "'Move Forward' is ambiguous and means different things depending on stage. Replacing with: "
                "No interview yet \u2192 'Schedule Interview' + 'Decline'. Pre-booked slot \u2192 'Confirm Interview' + 'Pick Another Time'. "
                "Booking link sent, no reply \u2192 'Pick a Time' + 'Resend Link' + 'Decline'. "
                "Fadi owns prototype link in Linear. Scout TBD \u2014 Jatin to assign.\n"
                "_Why it matters: Signal Scout feedback \u2014 this is one of the top OEM pain points. No logic changes, just clarity._"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af Your Action Items \u2014 Do These*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f534 *NIHILUS SUBSCRIPTION \u2014 WAS DUE TODAY* \u2014 No meeting captured. Skye was supposed to be in discussions. "
                "Ping Skye RIGHT NOW to confirm the decision. This is $8K/month and a hard deadline.\n\n"
                "\U0001f534 *2029 ONE-PAGER \u2014 DAY 18+ OVERDUE* \u2014 John is waiting. Board meeting opened Oct 15. Fadi submitted his. Write and send today.\n\n"
                "\U0001f534 *JD RULES FOR DIVIJ \u2014 DAY 9 OVERDUE* \u2014 Divij is IDLE. Rules: 1 hire ~30d=vanilla; 2+ hires='multiple positions available'; "
                "urgency <=2wk='urgently hiring'. TBD: ASAP definition + posted vs activated date. Send this TODAY.\n\n"
                "\U0001f534 *INTERVIEW CONFIRMATION BDD SPEC \u2014 OVERDUE* \u2014 Jatin + Bob cannot start the comms agent spike without this. "
                "You decided the shape today in the Lookahead. Write the BDD spec now while it\'s fresh.\n\n"
                "\U0001f7e1 *Justin Mason is BACK TODAY* \u2014 Ping him about Prompt Chips min wage MD file. He\'s your eng partner for this sprint.\n\n"
                "\U0001f7e1 *Tag Fatty for Verify CTA designs* \u2014 Magic link success screen designs are still pending. Still on your list.\n\n"
                "\U0001f7e1 *Indeed FSA \u2014 Escalate to Ashley Lutz* \u2014 Jessica has been MIA 7 days. Go over her head to Ashley now.\n\n"
                "\U0001f7e1 *Send Tallroo meeting dates* \u2014 November meeting. Include Skye. Still outstanding.\n\n"
                "\U0001f7e1 *Write Scheduling Ideal State doc* \u2014 Malcolm is gone. This is now critical. His spike docs are the starting point. "
                "Add to Linear. Schedule time with Skye to review.\n\n"
                "\U0001f7e1 *Align with Matan on interview confirmation copy/comms strategy* \u2014 Due next 1-2 weeks.\n\n"
                "\u26aa *Indeed company field bug \u2014 draft + send support reply* \u2014 10+ days outstanding.\n\n"
                "\u26aa *Doreen/Welcome Tech \u2014 decline Q4, suggest Q1 reconnect.*"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f465 Team Follow-ups (from Lookahead)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *Jatin* \u2014 Follow up with Sina on capacity TODAY (he said 'let me do that right now' in the meeting). "
                "HEADS UP: Sina is actively working on HB Assistant shift fill workflow handlers \u2014 capacity conflict likely.\n"
                "\u2022 *Jatin* \u2014 Assign scout for candidate profile CTAs (engineering TBD)\n"
                "\u2022 *Jatin* \u2014 Send Wednesday scheduling deep-dive invite to full squad\n"
                "\u2022 *Fadi* \u2014 Add full candidate state prototype link to Linear project for scouts\n"
                "\u2022 *Divij* \u2014 Generate JD body placement samples for count/speed; run by Manan\n"
                "\u2022 *Divij* \u2014 Wrap first version of count/speed prompt parsing by EOW\n"
                "\u2022 *IBK (Gbolade)* \u2014 Builder confirmed for hiring count + speed"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 Watch List \u2014 Critical Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f534 *NIHILUS \u2014 DEADLINE WAS TODAY*. Skye talking to Nihilus. Decision needed NOW. Ping Skye.\n"
                "\U0001f534 *2029 ONE-PAGER \u2014 18+ DAYS*. Critical board item. Not submitted.\n"
                "\U0001f534 *JD RULES FOR DIVIJ \u2014 DAY 9*. Divij is idle. You have the answer. Just send it.\n"
                "\U0001f534 *INTERVIEW CONFIRMATION BDD SPEC \u2014 OVERDUE*. Write it.\n"
                "\U0001f7e1 *Magic Link Identity Blocker* \u2014 Mary Turpin still on vacation. Has Jatin pushed EM for replacement?\n"
                "\U0001f7e1 *Indeed FSA Review \u2014 7 days overdue*. Jessica still MIA. Escalate to Ashley Lutz.\n"
                "\U0001f7e1 *Facebook API Rate Limiting \u2014 Day 13+*. No Meta response. Iszael investigating. Escalate if no response today.\n"
                "\U0001f7e1 *Scheduling Ideal State Doc \u2014 Malcolm is gone*. Manan owns. Critical.\n"
                "\u26aa *Sina capacity conflict* \u2014 Shift fill (HBA team) vs. hiring count/speed (Jatin to resolve).\n"
                "\u26aa *Entitlements rollout* \u2014 Adam\'s workers in PR midweek. Billing data gap (David Lin) still a risk.\n"
                "\u26aa *Change payment method flag* \u2014 Edwin out Mon-Tue. Check Wednesday.\n"
                "\u26aa *Comms assistant production decision \u2014 OVERDUE*. Malcolm gone. Decide urgently with Jatin.\n"
                "\u26aa *Spec Swarm \u2014 status still unknown*. Was supposed to happen Oct 27. Confirm with Jatin.\n"
                "\u26aa *MATAN 40% PMM split \u2014 CONFIDENTIAL*. Have the quiet 1:1 with Matan about workload."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f50d Workspace Intel (adjacent meetings you should know about)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*HB Assistant Standup (8:45am)* \u2014 Sina is actively building shift fill workflow handlers for the HBA team. "
                "State handlers done last week; now on task execution + internal event triggers. "
                "This directly competes with Jatin\'s promise to confirm Sina\'s capacity for hiring count/speed. "
                "Watch this carefully \u2014 it may delay the AI science layer for count/speed.\n\n"
                "*Palmetto Superfoods Customer Interview (10am, Keyvan + Jan + Chris Wallace)* \u2014 "
                "Customer uses HBA primarily to ask scheduling questions via the help center AI. "
                "Didn\'t know the lightning bolt assistant existed. Square auth error prevented POS integration. "
                "ADP tip integration gap = manual re-entry pain. Break waivers enabled live in session. "
                "Customer insight: overstaffs intentionally in year 1, trimming to ~15 hrs/week per person as winter begins. "
                "Product signal: ADP integration gap keeps coming up \u2014 HB Payroll conversion opportunity."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4ca By the Numbers*\n"
                "\u2022 FFH paying customers: ~210 (Q4 goal: 500)\n"
                "\u2022 Capture rate: ~7-8% | Healthy job rate: 30% (target: 80%)\n"
                "\u2022 Indeed: RECOVERED (Day 69+) | ZipRecruiter: ~11,500 applicants/week\n"
                "\u2022 Match rate: ~33-35% (improved from 85% \u2014 quality win)\n"
                "\u2022 OTP send success: ~64% \u2014 Magic Link will fix this to ~100%"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_You\'re running hard and making sharp calls, Manan. The Lookahead was tight \u2014 you kept the team focused, "
                "made the no-auto-cancel call with conviction, and unblocked IBK on the grandfathering decision. "
                "Now close out the overdue items \u2014 Nihilus first, JD rules second, BDD spec third. "
                "You\'ve got this. \U0001f4aa_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Digest \u2014 Monday, Nov 2, 2026",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(
        ("\n=== SLACK DIGEST PREVIEW (no token) ===\n" +
         json.dumps(payload, indent=2, ensure_ascii=False) +
         "\n=== END PREVIEW ===\n").encode("utf-8", errors="replace")
    )

def send():
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
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"Digest sent successfully to {CHANNEL}. ts={result.get('ts')}")
            else:
                print(f"Slack API error: {result.get('error')} | {result.get('warning')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"HTTP error sending to Slack: {e}")
        sys.exit(1)

if TOKEN:
    send()
else:
    print("No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN). Printing preview.")
    preview()
