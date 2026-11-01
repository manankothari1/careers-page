#!/usr/bin/env python3
"""
Chief of Staff Weekend Digest -- Saturday, October 31, 2026 (PDT)
Sends to Manan Kothari's DM channel D06E4QMHCNN
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
            "text": "\U0001f31f Weekend Chief of Staff Digest \u2014 Saturday, October 31",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan \U0001f44b You're back in SF, the jet lag is real, and this weekend has a LOT riding on it. No meetings today \u2014 that's a gift. Here's how your week landed and what you need to crush before Monday morning."
        }
    },
    {"type": "divider"},

    # --- WEEK GRADE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4ca Week Grade: B+ (sprint delivered, personal deliverables slipping)*\n\nStrong sprint execution \u2014 first formal Friday close worked beautifully, company vision landed well at kickoff, Malcolm's scheduling verdict gave the team a clear direction, and entitlements events went live. But your overdue personal items (2029 one-pager, JD rules, Scheduling Ideal State doc, BDD spec) are compounding. This weekend is your window to clear the log."
        }
    },
    {"type": "divider"},

    # --- WEEK WINS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3c6 This Week\u2019s Wins (Oct 26\u201330)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Sprint Ceremony Works.* First formal Friday close (Oct 30) completed. Outcome-oriented goals, board pre-filled, demo\u2019d against sprint goal. New standard is locked.\n\u2022 *Vision Presented.* Company kickoff vision landed \u2014 hiring capture rate as north star, 3-stage roadmap (standalone \u2192 talent network \u2192 marketplace). Crowd received it well.\n\u2022 *Malcolm\u2019s Verdict Delivered.* PATCHES NOT REBUILD. Each flow mapped, color-coded. Skye endorsed. You now own the ideal state design.\n\u2022 *Entitlements Events LIVE.* JJ confirmed customer entitlement events emitting Oct 30. Adam\u2019s workers consuming in PR. Pipeline working.\n\u2022 *Nihilus Screener Nudge SHIPPED.* Malcolm\u2019s final gift \u2014 built and ready to release.\n\u2022 *Indeed RECOVERED.* Day 68. Back to pre-outage volume. Huge.\n\u2022 *Hiring Intent Capture Scoped.* Soheil assigned for count & speed. Sina to start this sprint (status TBD).\n\u2022 *Match Quality Up.* 85% \u2192 33-35% applicant match rate \u2014 quality improvement is working."
        }
    },
    {"type": "divider"},

    # --- BIG DECISIONS THIS WEEK ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4dd Decisions Made This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1\ufe0f\u20e3 *Scheduling = Patches, Not Rebuild* \u2014 Malcolm\u2019s final verdict Oct 30. Incremental fixes to Nihilus-based system. No vendor switch in Q4/Q1. _Rationale:_ Skye clarified Manan designs ideal state; gap closed incrementally.\n\n2\ufe0f\u20e3 *Malcolm Out as of Oct 30* \u2014 Gone through last week of December. All scheduling context now on you + Skye. No more rubber duck sessions. _Rationale:_ Planned leave, not unexpected. His spike docs are your starting point.\n\n3\ufe0f\u20e3 *Sprint Ceremony Structure Locked* \u2014 Skye\u2019s proposal confirmed and executed. Friday closes, outcome goals, 80/20 split, multi-sprint = Linear initiative. _Rationale:_ First close proved the model works.\n\n4\ufe0f\u20e3 *Comms Agent Spike Scoped* \u2014 Jatin + Bob own interview confirmation spike (BDD format). Malcolm\u2019s screener nudge ready to release. _Rationale:_ Malcolm handoff completed before departure.\n\n5\ufe0f\u20e3 *Soheil Assigned to Hiring Count & Speed + Prompt Chips* \u2014 Confirmed in Oct 30 standup. _Rationale:_ Jatin realigned resources to cover Malcolm gap.\n\n6\ufe0f\u20e3 *Entitlements Rollout Gating on Facebook API Fix* \u2014 Rate limiting resurfaced Oct 20+ (no Homebase code change). Iszael + Bob investigating. Page token exemption expected but no response yet from Meta. _Rationale:_ Can\u2019t fully roll out while a channel is broken.\n\n7\ufe0f\u20e3 *Matan Going ~40% to Core PMM (CONFIDENTIAL)* \u2014 Susie fired, only Linda + Matan left as PMMs. Skye pulling Matan to cover. _Rationale:_ Company-level resource constraint. Manan must quietly reset expectations with Matan Monday."
        }
    },
    {"type": "divider"},

    # --- WEEKEND DELIVERABLES ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f525 Weekend Deliverables \u2014 Must Ship Before Monday 9am*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f6a8 *#1 \u2014 Scheduling Ideal State Doc* \u2014 CRITICAL. Malcolm is gone. Bob has open questions. This is the single most important unblocked thing you can do. Start with Malcolm\u2019s spike docs. Write your product POV. Define what the ideal end state looks like (not patches \u2014 the vision). Share with Skye + Bob.\n\n\U0001f6a8 *#2 \u2014 Interview Confirmation BDD Spec* \u2014 Jatin + Bob can\u2019t start their spike without this. You know the design cold (24hr confirm, YES variants, 4hr follow-up, 2hr cancel). Write it in BDD format. This is a 60-90 min task.\n\n\U0001f6a8 *#3 \u2014 2029 Vision One-Pager* \u2014 15+ DAYS OVERDUE. John and board are waiting. Fadi submitted his. You have NOT. This is a reputational risk. Write it. Tonight.\n\n\u26a0\ufe0f *#4 \u2014 JD Rules for Divij* \u2014 Day 6 overdue. Divij is idle. Rules are clear in your head: 1 hire ~30d = vanilla; 2+ hires = 'multiple positions available'; urgency <=2wk = 'urgently hiring'. Just write them down and send."
        }
    },
    {"type": "divider"},

    # --- MONDAY BATTLE PLAN ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2694\ufe0f Monday Nov 2 Battle Plan (by priority)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1\ufe0f\u20e3 *NIHILUS DECISION \u2014 DEADLINE IS TUESDAY NOV 3.* Skye is deciding. You need to be in the room. If you haven\u2019t already \u2014 ping Skye first thing Monday morning. This is do-or-die.\n\n2\ufe0f\u20e3 *Escalate Indeed FSA to Ashley Lutz.* Jessica\u2019s response was due Oct 27. It\u2019s now Nov 2. Three days past due. Don\u2019t wait. Email Ashley Lutz directly first thing Monday.\n\n3\ufe0f\u20e3 *Quiet 1:1 with Matan.* Confidential. He\u2019s now 40% PMM. Reset his expectations on intent propensity model, onboarding wizard, and pricing/packaging workload. Be warm \u2014 this is hard for him too.\n\n4\ufe0f\u20e3 *Push Jatin on Magic Link identity blocker.* Mary Turpin is on vacation. Jatin needs to pressure the identity EM to assign a replacement. The allow-list is blocking IBK from rolling out at 10-20%.\n\n5\ufe0f\u20e3 *Send Tallroo dates.* November meeting. Include Skye. Quick email \u2014 10 minutes.\n\n6\ufe0f\u20e3 *Tag Fatty for Verify CTA designs.* Magic link success screen. You\u2019ve been sitting on this. Do it Monday morning.\n\n7\ufe0f\u20e3 *Draft Indeed company field bug reply.* You\u2019ve owed Indeed support a reply for 8+ days. Bob\u2019s PR merged, company field paused. Write and send the reply.\n\n8\ufe0f\u20e3 *Matan local testing env walkthrough.* After your 1:1 \u2014 set up Claude-assisted job state + Iterable/SendGrid sandbox with him. Be mindful of his reduced capacity.\n\n9\ufe0f\u20e3 *Prompt chips MD file.* Write it and ping Justin (he\u2019s back Nov 3 \u2014 have it ready for him).\n\n10\ufe0f\u20e3 *Check on Sina.* Should have started hiring intent capture this sprint. Jatin was following up. Confirm status."
        }
    },
    {"type": "divider"},

    # --- WATCH LIST ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f440 Watch List \u2014 Critical Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f534 *NIHILUS \u2014 NOV 3 DEADLINE (TOMORROW after Monday).* $8K/mo now, $100K+/yr at scale. Decision: renew or scope rebuild. Skye owns the call.\n\U0001f534 *2029 VISION ONE-PAGER \u2014 15+ DAYS OVERDUE.* Board waiting. Write it.\n\U0001f534 *SCHEDULING IDEAL STATE DOC \u2014 MALCOLM IS GONE.* Your job now.\n\U0001f534 *INDEED FSA \u2014 ESCALATE MON.* Jessica 3 days past due. Escalate to Ashley Lutz.\n\U0001f534 *FACEBOOK API RATE LIMITING \u2014 DAY 35+.* Iszael investigating new errors from Oct 20. Escalate if no Meta Slack response by Tuesday.\n\U0001f7e1 *MAGIC LINK \u2014 IDENTITY TEAM BLOCKER.* Mary Turpin on vacation. IBK stuck at 0%. Jatin to fix.\n\U0001f7e1 *JD RULES FOR DIVIJ \u2014 DAY 6 OVERDUE.* Divij is idle. Send the rules.\n\U0001f7e1 *INDEED COMPANY FIELD BUG REPLY \u2014 8 DAYS.* Write and send to Indeed support.\n\U0001f7e1 *MATAN 40% PMM SPLIT \u2014 CONFIDENTIAL.* 1:1 Monday. Scope impact.\n\U0001f7e1 *CARLO KT \u2014 NOT CONFIRMED.* Paternity through mid-Feb. Knowledge at risk.\n\U0001f7e1 *BILLING DATA GAP.* Secure trial end events not emitting 1+ year. David Lin investigating. Revenue discrepancy risk to entitlements rollout.\n\U0001f7e1 *INDEED ID TEAM TECH REVIEW CALL.* Rachel to coordinate with Ashley. Bring engineer + posting flow diagram.\n\U0001f7e1 *DEPARTURES SIGNAL DOCS \u2014 30+ DAYS OVERDUE.* Zane, Sean, Jon W, Bobby. This is costing you institutional knowledge.\n\U0001f7e1 *46 OLD EXPERIMENTS.* Jatin surfaced. Quick review with Fadi this week."
        }
    },
    {"type": "divider"},

    # --- CLOSER ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4aa You\u2019ve Got This*\n\nManan \u2014 you just closed your first sprint under the new ceremony, launched your company vision, and held down the fort through Paris + Malcolm\u2019s departure. That\u2019s legitimately hard and you did it well. This weekend is purely about clearing the log of things only you can unblock. Three docs + one email. You\u2019ll feel 10x lighter Monday morning.\n\n_Chief of Staff Digest \u2014 auto-generated \u00b7 Saturday, October 31, 2026 \u00b7 5:02 PM PDT_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Weekend Chief of Staff Digest - Saturday Oct 31"
}


def preview():
    print("=" * 72)
    print("CHIEF OF STAFF WEEKEND DIGEST -- Saturday, October 31, 2026 (PDT)")
    print("=" * 72)
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n=== " + block["text"]["text"] + " ===\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
    print("=" * 72)
    print("CHANNEL: D06E4QMHCNN")
    print("STATUS: PREVIEW (no SLACK_TOKEN found)")


def send_slack(token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + token,
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print("SUCCESS: Message sent to", CHANNEL)
                print("ts:", result.get("ts"))
            else:
                print("SLACK ERROR:", result.get("error"))
                print(json.dumps(result, indent=2))
    except urllib.error.URLError as e:
        print("REQUEST ERROR:", e)


if __name__ == "__main__":
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN") or
        ""
    )
    if not token:
        preview()
        sys.exit(0)
    send_slack(token)
