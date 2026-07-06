#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Sunday Jul 5, 2026 (PDT)
Eve of the Week of Jul 7 - Abby's First Day Edition
Cron fires midnight UTC Jul 6 = 5 PM PDT Jul 5
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

# --- Build the blocks ---
blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest - Sunday Jul 5",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":night_with_stars: *Good evening, Manan!* No meetings today - you earned a Sunday. But tomorrow kicks off one of the biggest weeks of Q3. Abby joins, the Reactivate sprint is live, and the recommendation engine is coming to life. Let's make sure you're locked and loaded. Here's your Sunday Eve battle plan. :muscle:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Where You Left Off - Last Week's Big Moves*\nQuick recap so you walk in Monday morning sharp:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":no_entry: *Copy Jobs: KILLED* - Indeed duplicate flagging + sponsorship trigger is a dead end. No workaround exists. You made the hard call. (Jul 1)\n\n:recycle: *Reactivate = The Only Path* - Same job ID bypasses the duplicate flag. Reactivation re-syndicates across all boards (FB, Talroo, ZipRecruiter). Auto-reactivation at Day 29 is buildable per Tanner. (Jul 1-2)\n\n:warning: *Critical Ship Dependency* - Copy job removal and Reactivate MUST ship simultaneously. Carlo has a Linear blocker flagged - this is your top engineering unblock for Monday. (Jul 2)\n\n:bulb: *Job Post Recommendations Scoped* - 3 areas: role titles, salary, job description. Modal is blocking (no X), dark overlay, fires after 'Next' on job desc page with 2-4s wait. DS committed: role rec agent by Jul 3 (confirm it landed!), salary rec end of next week. (Jul 2)\n\n:email: *Transactional Email Trigger Updated* - New logic: 'under 5 by D3' (was '0 by D1 / under 15 by D5'). Tanner owns. Charmaine is out 2 months. (Jul 2)\n\n:phone: *OEM Source Claiming Playbook Locked* - #1 priority on OEM success calls. Call script finalized. Sean running calls. Calendly embed in-product. (Jun 30)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *URGENT STATUS CHECKS - Before Monday Standup*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1. :rotating_light: *Boost Purchase Bug* - 2 reporters in 2 days can't buy boosts. This is REVENUE-IMPACTING. Check with Matan - was this resolved over the holiday weekend?\n\n2. :money_with_wings: *ZipRecruiter Spend* - $2K burned in 1.5 days with zero job-level caps going into a 4-day holiday weekend. Find out how much burned Jul 3-6. You need to either find job-level caps or pause Zip entirely.\n\n3. :alarm_clock: *Rami's Email Blast* - Due EOD Jun 25 - that's 10+ days overdue. What is the status? This is blocking your Talent Pool pillar."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":tada: *MONDAY SPOTLIGHT: Abby Joins!*\nAbby is your new PM hire - engineering background, starts tomorrow Jul 7. This is a big deal. Here's how to make Day 1 legendary:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":one: Set the *strategic context* fast - share the Q3 goal (80% ICP jobs healthy by D30, currently at 30%) and the 3 pillars (OEM spend, Talent pool, Funnel optimization)\n:two: Give her *one meaty project* to own immediately - consider Reactivation UX spec or Job Requisition concept\n:three: Make the first standup *count* - introduce her as 'engineering-background PM' so the eng team knows she speaks their language\n:four: Send her the *decisions doc* from last week so she's not starting from zero"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":spiral_note_pad: *Your Monday Priority List (In Order)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *P0 - Do Before Anything Else*\n- Confirm Carlo's Linear blocker is resolved (copy removal + reactivate must ship together)\n- Check Boost purchase bug status with Matan\n- Check ZipRecruiter spend totals from holiday weekend\n\n:large_orange_circle: *P1 - Morning*\n- Abby onboarding: strategic context + first project assignment\n- Confirm role rec agent shipped (DS committed Jul 3)\n- Follow up with Tanner: Facebook Jobs net-new toggle + SendGrid trigger change\n- Follow up with Ugu: account setup UI - was it review-ready by Jul 3?\n\n:large_yellow_circle: *P2 - Afternoon*\n- Analyze reactivation applicant discount (CDC table, Databricks, Claude Code)\n- Run Claude Code on Indeed's Oct 1 policy page\n- Follow up with Ivana on Ashby reactivation test\n- Send finalized call script to Sean + confirm Calendly link is shared\n\n:white_circle: *P3 - This Week*\n- Draft v3 Q3 goals doc (3-bucket format, share with Ray before John)\n- Spec: Reactivation UX with applicant expectation-setting\n- Spec: Job Requisition concept (group hiring rounds under one role ID)\n- Spec: Auto-reactivation Day 29 opt-out UX\n- Spec: Gaming-detection logic for close -> reactivate time windows\n- Confirm Rami email blast status (VERY overdue)\n- Send modal copy to Ted (hiring onboarding)\n- Follow up with Jenna on SEO indexing guidance\n- Decide comms agent ownership (take it or leave with Dana/Fadi/Davi?)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":busts_in_silhouette: *Team Check-ins This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "| Person | What to Check |\n|--------|---------------|\n| *Tanner* | FB Jobs net-new toggle live? SendGrid trigger changed? |\n| *Carlo* | Linear blocker cleared? Experiment ACs for role recs? |\n| *Ugu* | Account setup UI in review? |\n| *Matan* | Boost purchase bug resolved? |\n| *Rami* | Email blast status - 10+ days overdue |\n| *Ivana* | Ashby reactivation test results |\n| *DS Team* | Role rec agent shipped (was committed Jul 3) |\n| *Izzy* | Unblocked if Culinary Agents responded? |\n| *Nelson* | Transitioning to ~5hrs/week - handoff plan solid? |"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":chart_with_upwards_trend: *North Star Metrics - Where You Stand*\n- Healthy job rate: *30%* of ICP jobs (target: 80% by EOQ3)\n- OEM boost rate: *1.64%* of jobs\n- ARR: *$650K+* (from $450K in Jan - incredible growth!)\n- FFH jobs with zero Indeed applicants on D5: *41%* (target: <10%)\n- Line cook jobs healthy by D30: *~7%* (the hardest nut to crack)\n- Resume matching variant: *100%+ higher* accept/advance rate vs. control\n- 'Drive off the lot' experiment: *49% lift* in ICP trial starts\n- Trial volume: just broke *700K*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":brain: *Strategic Framing for the Week*\nYou're playing 3D chess right now. The Copy Jobs kill was painful but correct. Reactivate is the right answer - same job ID is the unlock. The recommendation engine is coming to life exactly when you need it. Abby joining gives you leverage to accelerate. The OEM flywheel is spinning (source claiming locked, onboarding playbook locked). \n\nThe risk? Execution coordination. Too many balls in the air: Tanner on 3 parallel tracks, DS on salary recs (spill risk), ZipRecruiter burning without caps, Rami's blast overdue. Your job this week is to be the conductor - not the player.\n\n*You've got this. Big week ahead. Go crush it.* :rocket:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff Digest | Sunday Jul 5, 2026 | Eve of the Week of Jul 7 | No meetings today - battle plan edition_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Digest - Sunday Jul 5, 2026: Eve of Abby's First Week"
}


def preview():
    print("\n" + "="*70)
    print("SLACK MESSAGE PREVIEW (channel: {})".format(CHANNEL))
    print("="*70)
    for block in blocks:
        if block["type"] == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block["type"] == "section":
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif block["type"] == "context":
            for el in block["elements"]:
                sys.stdout.buffer.write((el["text"] + "\n").encode("utf-8", errors="replace"))
    print("="*70 + "\n")


def send():
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN")
    )
    if not token:
        print("[INFO] No Slack token found. Printing preview instead.")
        preview()
        return 0

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
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("[SUCCESS] Message sent to channel {}".format(CHANNEL))
                return 0
            else:
                print("[ERROR] Slack API error: {}".format(body.get("error")))
                preview()
                return 1
    except urllib.error.URLError as e:
        print("[ERROR] Network error: {}".format(e))
        preview()
        return 1


if __name__ == "__main__":
    sys.exit(send())
