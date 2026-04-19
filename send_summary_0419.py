#!/usr/bin/env python3
"""
Chief of Staff Daily Summary - Sunday Apr 19, 2026
No meetings today (Sunday). Sending week-ahead battle plan.
"""
import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Report - Sunday Apr 19, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Good evening, Manan! No meetings today (Sunday), which means it's the *perfect moment to get ahead of the week*. You're crushing it — ARR at *$650K (+44%* since January), Launch Week on the horizon, and a ton of big bets in flight. Here's everything you need to walk into Monday locked and loaded. Let's go. :muscle:"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CODE RED — These Cannot Wait Until Monday Morning*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. TLWA Launch Week Brief — 16+ Days Overdue to Ted*\n> You made this decision weeks ago. The brief has not landed with Ted. This is your #1 unblocking moment for Launch Week. Every day this slips is a day the team loses alignment on the QR mailer, careers page rollout, and award winner migration.\n> :white_check_mark: *Action:* Send the full TLWA/LW brief to Ted today or first thing Monday. If it's not written, timebox 30 min and get it out."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. URGENT: Audit Talroo Feed for Manual Mode Customers*\n> You flagged this on the Ray/Manan call Apr 17 — Manual Mode customer jobs may be flowing into the Talroo feed. You are currently spending *$35/job* on customers paying *$30/month*. This is negative-margin spend happening right now.\n> :white_check_mark: *Action:* Audit the feed ASAP. Confirm with Nelson/Ray that Manual Mode jobs are excluded. If not excluded, halt or filter immediately.\n> :white_check_mark: *Action:* Confirm Saja (Talroo) has received the CPA category recommendations and has configured the campaign switch from CPC."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Greenlight Manual Mode — Cindy QA Done, Ball is in Your Court*\n> Cindy finished QA. You're the only blocker on shipping Manual Mode. This has been sitting.\n> :white_check_mark: *Action:* Greenlight it Monday morning. Zero reason to hold."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Homebase Boost SKU Kick-off with Chris McIntosh — Billing Window Closing*\n> The billing window for Boost SKU is closing. You need the kick-off with Chris to lock pricing + packaging before Launch Week.\n> :white_check_mark: *Action:* Reach out to Chris McIntosh today/Monday. Get this scheduled this week, no exceptions."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: Key Decisions Still Pending — Need Your Call This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. V1 Migration for TLWA Award Winners — Decision Was Due EOD Apr 17*\n> ~50% of V1 users are award winners. ~75% of users with live jobs are winners. Three options on the table:\n> (A) Exclude from mailer — lose the most engaged users\n> (B) Optional V2 migration — highest risk, complex UX\n> (C) Build generic role plumbing so past-applicants + quick-repost exist in V2\n> Risks: past-applicant visibility and quick-repost not yet in V2.\n> :white_check_mark: *Action:* Make this call Monday morning. Loop in Fadi + Jeff on implications."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Predictive Role Timeline — Was Time-Boxed to EOD Apr 17*\n> Divij's predictive role matching: is it a yes or no for Launch Week? You time-boxed the answer to EOD Apr 17. The answer is still open.\n> :white_check_mark: *Action:* Confirm yes/no with Divij Monday. If yes, unlock him with cloud code acceleration. If no, move to fast-follow queue."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. QR Code Mailer — ~3,000 Unmailable Addresses*\n> Cassy (printer) flagged ~3,000 unmailable addresses. 50,000 QR codes are queued for print. You need to confirm the final count before the run starts.\n> :white_check_mark: *Action:* Ping Cassy + Fadi Monday to confirm mailable address count. Also confirm Iszael resolved the ~8,000 missing company addresses."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:memo: Homework You Owe People — Clear the Queue*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":small_blue_diamond: *Ray's Homework Doc:* Create Google Doc with Talroo CPA spec + XML feed segmentation (entry-level vs managerial) + incomplete applicant ingestion pipeline design. You committed to this on the Apr 17 call.\n\n:small_blue_diamond: *Bob (endpoint structure):* Share application endpoint structure with Ray for the incomplete applicant ingestion V2 job experiment reference.\n\n:small_blue_diamond: *Jatin (warm lead framing):* Convince Jatin on incomplete applicant ingestion value. Frame it as a warm lead (clicked but didn't apply), not spam. The 30%+ Talroo applicant lift depends on his buy-in.\n\n:small_blue_diamond: *Jeff (TLWA desktop designs):* Jeff needs to ship desktop designs for the TLWA V2 badge to engineers. This is blocking. Tag him if not done.\n\n:small_blue_diamond: *Nelson (job description quality thresholds):* Nelson still needs to define char/line minimums for Talroo job quality. Also still pending: metro_area + bucketed_role + matching_roles columns (overdue since Apr 8).\n\n:small_blue_diamond: *Matan (#leads post):* Matan needs to post the Boost Phase 1 vs Phase 2 rationale to #leads for Ray. Still pending.\n\n:small_blue_diamond: *Justin (Supabase RLS audit):* Full audit should be active. Confirm Justin is running it — your conflict (LW) doesn't mean it can stall."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rocket: Launch Week Readiness Checklist*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Boost:* 3 entry points locked (job creation + jobs section + email/push). Phase 1 = every trial user auto-boosted. 'Boost' renamed to 'Sponsored Job'.\n:hourglass: *TLWA V2 badge:* Desktop designs from Jeff blocking engineers. Unblock this Monday.\n:hourglass: *Careers page TLWA QA:* Full QA with Fadi before 50k QR codes print.\n:hourglass: *Walk-in poster / custom QR builder:* Jeff's mockup. Confirm status.\n:hourglass: *3LO (Indeed OAuth):* Phase 1 ships with 3 entry points. Confirm engineers are unblocked and on track.\n:hourglass: *Company descriptions:* Batches 93-100 re-running with real website content. Justin to QA sample.\n:hourglass: *CTA hierarchy mapping:* Manan + Cindy + Matan need to map full CTA hierarchy in job creation flow before LW to prevent noise overload (Boost + one-time post + 3LO simultaneously)."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bar_chart: State of the Metrics — Where You Stand*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":star: *ARR:* $650K (+44% from $450K in January) — you are on a rocket ship\n:star: *GTM OS ML:* 70% of top 250 companies converted in 7 days\n:star: *Lifecycle:* 46% team app upgrades influenced\n:star: *Taru feed:* ~300 → ~1,100 jobs (3.7x growth)\n:star: *Applicant pool:* 90k in past 30 days — 10% re-engagement = 9k warm applicants untapped\n:star: *3LO:* V1 must-have (live job post status) + stretch (sponsored redirect) on track\n:star: *Talroo CPA:* $2.01/lead avg via pixel. Switching from CPC to CPA bidding — major efficiency unlock incoming."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Monday Morning Priority Stack (in order)*\n\n1. :fire: TLWA brief → Ted (overdue 16+ days)\n2. :fire: Greenlight Manual Mode (Cindy QA done)\n3. :fire: Talroo feed audit — confirm Manual Mode jobs excluded\n4. :fire: Boost SKU kick-off — ping Chris McIntosh\n5. V1 migration decision for award winners (50% of user base)\n6. Predictive role yes/no with Divij\n7. QR code mailer count — ping Cassy + Fadi\n8. Create Ray's Homework Google Doc (CPA + segmentation + incomplete ingestion)\n9. Jeff → ship desktop TLWA designs (unblock engineers)\n10. Matan → confirm #leads Boost post is live"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan — you've built something genuinely special in the past few months. The ARR trajectory, the product bets landing, the team pulling together for Launch Week — this is real. Monday is a big day. You've got this. :trophy:\n\n_Your Chief of Staff, signing off for Sunday evening. See you at the 5pm briefing tomorrow._"
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "blocks": blocks,
    "text": "Chief of Staff Report - Sunday Apr 19, 2026 - Week-Ahead Battle Plan"
}


def preview():
    print("=" * 70)
    print("CHIEF OF STAFF REPORT - SUNDAY APR 19, 2026")
    print("=" * 70)
    for block in blocks:
        if block.get("type") == "section":
            text_obj = block.get("text", {})
            if text_obj.get("type") == "mrkdwn":
                sys.stdout.buffer.write((text_obj["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            text_obj = block.get("text", {})
            sys.stdout.buffer.write(("### " + text_obj.get("text", "") + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
    print("=" * 70)


def send_slack():
    if not SLACK_TOKEN:
        print("SLACK_TOKEN not set — printing preview only.")
        preview()
        return 0

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_TOKEN}"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"Slack message sent successfully! ts={result.get('ts')}")
                return 0
            else:
                print(f"Slack API error: {result.get('error')}")
                preview()
                return 1
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        preview()
        return 1


if __name__ == "__main__":
    sys.exit(send_slack())
