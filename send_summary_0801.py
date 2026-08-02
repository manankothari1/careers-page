#!/usr/bin/env python3
"""
Chief of Staff Daily Digest
Date: Saturday Aug 1, 2026 (PDT) — firing at midnight UTC Aug 2
No meetings today (Saturday). Sending EOW wrap + critical Monday Aug 3 Battle Plan.
"""

import json
import os
import sys
import urllib.request
import urllib.error


CHANNEL = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)


def build_blocks():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Saturday Evening Check-In | Aug 1, 2026",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! No meetings today — you *earned* this Saturday. "
                    "But your chief of staff is here with eyes wide open, because "
                    "*the week ahead is one of the most important of your Q3.* "
                    "Let's get you locked and loaded for Monday."
                ),
            },
        },
        {"type": "divider"},
        # CRITICAL ALERT SECTION
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:rotating_light: SITUATION ROOM: Week of Aug 3 :rotating_light:*\n\n"
                    "Two critical facts that shape everything this week:\n\n"
                    ":calendar: *Ray is OUT* all week (Aug 3-8)\n"
                    ":calendar: *Dana is OUT* all week (Aug 3-8) — and her last day is *Aug 12*\n\n"
                    "If Dana is off Aug 3-8, she returns *Monday Aug 10* with only *2 working days* "
                    "left before her final day. That means *every single ICP experiment, Page Templates "
                    "handoff, and succession task must be arranged THIS WEEKEND or first thing Monday.* "
                    "There is no safety net here."
                ),
            },
        },
        {"type": "divider"},
        # P0 MONDAY ACTIONS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:fire: P0 Actions — Do These Before You Sleep Sunday Night*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*1. Dana Succession — TODAY (not Monday)*\n"
                    "Dana is off starting Monday. You have TODAY and TONIGHT. "
                    "Send her a message or schedule a 30-min call for Sunday if she's available. "
                    "You need: (a) ICP experiments hand-off doc/Notion page, "
                    "(b) Page Templates transition plan, (c) her compiled list of open items. "
                    "The 'we'll figure it out when she's back' approach leaves you 2 days. That's not enough. "
                    "*Rational:* Dana being off Aug 7 week was always the plan — but Aug 12 last day was "
                    "supposed to be end of September. The 6-week acceleration means the buffer is gone."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*2. Carlo Conversation — Monday 9am*\n"
                    "Harness/OpenSpec is *18+ days overdue*. Carlo is also back from Canada holiday Monday. "
                    "Do NOT let the day start without a direct 1:1 conversation. "
                    "This isn't a Slack ping — it's a management conversation. "
                    "What's the blocker? What does he need? What's the commit? "
                    "*Rational:* Talent Pool Outreach depends on Carlo's rake task (1-2 days). "
                    "You greenlit that initiative on Jul 29. It should already be done."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*3. 422 Error Escalation — Day 23*\n"
                    "146 locations affected since Jul 9. Jatin owns the RCA — get a written status by EOD Monday. "
                    "With Ray out, you are the decision-maker on any mitigation path. "
                    "*Rational:* Every day this stays open is revenue risk and OEM trust erosion."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*4. MBR Content — Manan Section Due This Week*\n"
                    "Ray + Dana are both out. You own the *applicant side* MBR section. "
                    "No one is going to remind you this week. Build it Monday-Tuesday. "
                    "Content owners: Jatin (shipped), Matan (ICP), Fadi (in-product growth), you (applicant side). "
                    "*Rational:* Dana was supposed to send a compiled list — she's gone. Don't wait for it."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*5. Fadi Boost Modal Figma — Day 6 Overdue*\n"
                    "This is on you. Send it to Fadi first thing Monday. "
                    "Boost copy is locked ('Cut your hiring time' + 'Hard to fill role' yellow pill). "
                    "*Rational:* Fadi is unblocked on everything else. This is a PM dependency that's stacking up."
                ),
            },
        },
        {"type": "divider"},
        # WEEK OF AUG 3 AGENDA
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:calendar: Week of Aug 3 — Key Agenda Items*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Comms Agent Manual Experiment (Jatin)*\n"
                    "Jatin wants to kick off the manual experiment this week — team texts candidates "
                    "from personal phones to validate the hypothesis before any build. "
                    "Ray wanted Manan + Jatin to sit with Cena to surface hidden assumptions first. "
                    "With Ray out, you call this. Confirm: Did Jatin's Cena sync happen on Jul 30? "
                    "If yes and assumptions are clear — green light. If not — do the Cena sync Monday. "
                    "*Action:* Message Jatin Sunday or Monday morning. Get clarity."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Rami (DS) Business Case — Make It This Week*\n"
                    "Ted is pulling back Rami's involvement after Kan's departure. "
                    "With Ray out, you cannot escalate through him. Go direct to Ted this week. "
                    "Frame it: applicant quality + Marketplace impact + JD experiment results. "
                    "*Action:* Send Ted a Slack message Monday with the specific ask and data points."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*ICP Experiments — Get Up to Speed with Matan*\n"
                    "Matan was running ICP experiments with Dana. Dana is gone. "
                    "Schedule a dedicated 45-min sync with Matan this week to understand: "
                    "current experiment state, what decisions are pending, what Manan needs to own. "
                    "*Action:* Block time with Matan Mon or Tue."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Bob + Jonathan Comms Agent Sync (Jul 29 3pm) — Confirm Outcome*\n"
                    "No Granola notes were ever found for this sync. "
                    "You need to know: was ownership resolved? Is it Bob/Jonathan (product eng) or Cena (data eng)? "
                    "*Action:* Message Bob or Jonathan Monday for the outcome."
                ),
            },
        },
        {"type": "divider"},
        # OPEN ITEMS SCOREBOARD
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:clipboard: Open Items Scoreboard (Carry-Forwards)*",
            },
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": (
                        "*Overdue / Stale*\n"
                        ":red_circle: Carlo Harness/OpenSpec — 18+ days\n"
                        ":red_circle: Fadi Boost modal Figma — 6 days\n"
                        ":red_circle: Franchise ticket — 4+ days\n"
                        ":red_circle: Scooters follow-up (Olivia/Maria/Lacey)\n"
                        ":red_circle: Juan Sanchez email issue\n"
                        ":red_circle: Indeed noindex help article (Manan to draft)\n"
                        ":red_circle: Matan comms doc (Sonia still blocked)"
                    ),
                },
                {
                    "type": "mrkdwn",
                    "text": (
                        "*In Progress / Check Status*\n"
                        ":yellow_circle: Talent Pool Outreach (Carlo rake task)\n"
                        ":yellow_circle: 422 errors RCA (Jatin) — Day 23\n"
                        ":yellow_circle: Usman candidate email experiment (check results)\n"
                        ":yellow_circle: Izzy + Tanner API contract alignment\n"
                        ":yellow_circle: SBA unassigned grid P1 data (friendly test was negative)\n"
                        ":yellow_circle: Comms agent Bob+Jonathan sync outcome"
                    ),
                },
            ],
        },
        {"type": "divider"},
        # Q3 METRICS PULSE
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:chart_with_upwards_trend: Q3 North Stars — Where You Stand*\n\n"
                    "• FFH D5 zero-applicant rate: *41%* (target: <10%) — Talent Pool Outreach is your unlock\n"
                    "• Line cook jobs healthy by D30: *~7%* (target: 50%) — long road, Talent Pool + matching key\n"
                    "• Screener completions: +50% relative target — Comms Agent manual test this week could move this\n"
                    "• OEM Boost rate: *5.7%* (up from 2.9% in May) — momentum is real\n"
                    "• 422 errors: *146 locations, Day 23* — this is bleeding the funnel"
                ),
            },
        },
        {"type": "divider"},
        # WEEK LOCKED DECISIONS RECAP
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:white_check_mark: Big Week-of-Jul-28 Decisions — Locked and Shipped*\n\n"
                    ":lock: *Candidate Matching Thresholds SHIPPED* — resume 0.8 / screener 0.5 / combined 0.4+0.3. "
                    "13K flagged from 52K applicants. Ship + learn.\n"
                    ":lock: *Competency Normalization* — global percentile first, role-level v2 later. "
                    "Ted scoping with Divij.\n"
                    ":lock: *Comms Agent* — manual validation BEFORE build. Hypothesis must be proven.\n"
                    ":lock: *Talent Pool Outreach GREENLIT* — Carlo rake task, 1-2 days, raw SMS.\n"
                    ":lock: *Talent Pool Card Format* — previous role + total YoE + location.\n"
                    ":lock: *Boost copy* — 'Cut your hiring time' + 'Hard to fill role' yellow pill.\n"
                    ":lock: *Indeed Account Setup copy* — 'Connect your account to Indeed. Indeed may have hidden your post.'\n"
                    ":lock: *MBR prep owners* — Jatin: shipped, Matan: ICP, Fadi: in-product, Manan: applicant side.\n"
                    ":lock: *Sprint Sizing Ritual LAUNCHED* — S<3d, M~1wk, L=full sprint (Jatin)."
                ),
            },
        },
        {"type": "divider"},
        # CONFIDENTIAL ORG REMINDER
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:lock: Confidential — Org Context*\n\n"
                    "• *Dana's last day = Aug 12.* Not announced publicly. "
                    "Departure was mutual. Grand two-PM-team experiment did not work.\n"
                    "• *You = sole Lead PM starting Aug 12.* Single roadmap. "
                    "Matan, Fadi, Jatin all report into your structure. New GM of Hiring will inherit this.\n"
                    "• *Karan is leaving.* Ray transitioning to builder role with Justin. "
                    "New Head of Product being hired (1-2 months).\n"
                    "• *Rami involvement may be temporary* — make the Ted business case this week."
                ),
            },
        },
        {"type": "divider"},
        # CLOSING
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Manan — you are stepping into one of the biggest leadership moments of your career. "
                    "Sole Lead PM, Dana's handoff, and a Q3 that's far from over. "
                    "You've been making sharp, fast decisions all week and the team is moving because of it. "
                    "*Talent Pool Outreach, candidate matching thresholds shipped, sprint sizing launched, "
                    "Scooters' source naming locked* — that's a lot of horsepower in one week.\n\n"
                    "Enjoy the rest of your Saturday. Prep your Monday like the exec you're becoming. "
                    "You've got this. :muscle:"
                ),
            },
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "Chief of Staff Digest | Aug 1, 2026 (PDT) | No meetings today (Saturday) | Next digest: Sunday Aug 2 @ 5pm PDT",
                }
            ],
        },
    ]
    return blocks


def send_slack(blocks, text_fallback):
    payload = json.dumps(
        {
            "channel": CHANNEL,
            "text": text_fallback,
            "blocks": blocks,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body


def preview(blocks):
    sys.stdout.buffer.write(
        "\n=== SLACK MESSAGE PREVIEW (Aug 1, 2026) ===\n".encode("utf-8")
    )
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            sys.stdout.buffer.write(
                ("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif btype == "section":
            if "text" in block:
                sys.stdout.buffer.write(
                    (block["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
                )
            if "fields" in block:
                for f in block["fields"]:
                    sys.stdout.buffer.write(
                        (f["text"] + "\n").encode("utf-8", errors="replace")
                    )
        elif btype == "divider":
            sys.stdout.buffer.write("---\n".encode("utf-8"))
        elif btype == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(
                    ("[context] " + el.get("text", "") + "\n").encode("utf-8", errors="replace")
                )
    sys.stdout.buffer.write("\n=== END PREVIEW ===\n".encode("utf-8"))


def main():
    blocks = build_blocks()
    text_fallback = (
        "Saturday Evening Check-In | Aug 1, 2026 | No meetings today. "
        "CRITICAL: Ray + Dana both OUT week of Aug 3. Dana last day Aug 12 (11 days). "
        "Monday P0s: Dana succession NOW, Carlo conversation, 422 RCA status, Fadi Figma, MBR content. "
        "Full digest in thread."
    )

    if not TOKEN:
        print("[INFO] No SLACK_TOKEN found — showing preview only.")
        preview(blocks)
        print("[INFO] To send for real: set SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN env var.")
        sys.exit(0)

    print("[INFO] Sending to Slack channel", CHANNEL)
    result = send_slack(blocks, text_fallback)
    if result.get("ok"):
        print("[SUCCESS] Message sent. ts =", result.get("ts"))
    else:
        print("[ERROR] Slack API error:", result.get("error"))
        sys.exit(1)


if __name__ == "__main__":
    main()
