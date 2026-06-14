#!/usr/bin/env python3
"""
Sends the pre-built daily summary for Friday June 12, 2026 to Slack.
This script uses Granola data already retrieved via MCP.
"""

import os
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = "D06E4QMHCNN"

MESSAGE = """:star2: *Daily Decision Summary — Friday, June 12, 2026*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hey Manan! :wave: It's 5pm — time to debrief. You had a genuinely *stacked day* (4 real meetings before noon!), and you made some *really sharp strategic moves*. Here's your complete breakdown so nothing slips through the cracks tonight. You should feel great about the clarity you drove today. :dart:

━━ *1. Q3 North Star Locked: 80% of ICP Jobs Healthy by Day 30* ━━
:calendar: 11:30am · Q3 Applicant Flow Strategy · with Ted Naseri & Rami Abou-Seido

*Decision:* Set the Q3 north star at 80% of ICP jobs reaching health by Day 30 (up from ~30% today). Three-pillar strategy finalized:
• Enable OEM spend (boosting) — front-loaded to Sprint 1 so eng is free later
• Tap the 20M-person talent pool — you + Rami run experiments *concurrently*
• Optimize the job board funnel

*Rationale:* Day-30 healthy jobs drive ~3x trial-to-paid conversion. The sequencing is smart — OEM spend work first frees engineering to productionize talent pool outputs once experiments are proven. New designer joining early July aligns with design-heavy work starting then.

*Action Items:*
:white_check_mark: Clean up Q3 roadmap — add sprint dates, surface talent pool timeline, add salary recs as a line item _(you)_
:white_check_mark: Share finalized roadmap with Ted so he can flag Rami capacity conflicts vs. Cashout model deployment _(you)_
:white_check_mark: Rami finishes outreach script by Mon/Tue — ping him for 15-min sync if needed _(Rami)_
:white_check_mark: Set up weekly Tue/Wed sync: Manan + Ted + Rami + designer (when onboarded) _(you)_
:white_check_mark: Set up biweekly Fri afternoon brainstorm: you + Rami, for open-ended hiring DS opps _(you)_
:white_check_mark: Share Antoine's hackathon handoff file with Rami _(you)_

━━ *2. Indeed Browser Agent: POC Promising, ToS Check Required* ━━
:calendar: 10:00am · Hiring Team Check-in · Full team

*Decision:* Don't green-light production on the Indeed browser agent yet. The POC handles login + OTP — but two gates remain before moving forward: (1) legal review of Indeed's ToS for browser automation, and (2) completing the boost step with a real paid employer account.

*Rationale:* Boosted jobs reach "healthy" at 50% vs. 26% unboosted — the leverage is massive. But ToS risk and production architecture questions (latency, concurrency, Rails vs. Python, security) need answers first. Smart to spike before investing eng time.

*Action Items:*
:white_check_mark: Get Zane a paid Indeed employer account to finish proving out the browser agent POC _(you)_
:white_check_mark: Review Indeed ToS for browser automation before any production work _(you)_
:white_check_mark: Ray to set up a call with Anon (headless browser experts) next week _(Ray)_
:white_check_mark: Find time with Zane to map Rescue Job into the boosting flow + LCM motion _(you)_
:white_check_mark: Share full deck + Librarian link in hiring team channel _(you + Nelson)_

━━ *3. Indeed Agent Architecture Spike This Sprint* ━━
:calendar: 10:48am · Izzy / Manan

*Decision:* Treat Indeed agent production readiness as a spike next sprint. Don't build for production yet.

*Key unknowns to investigate:*
• Latency per agent run + max concurrency (e.g. 100 OEMs simultaneously)
• Communication architecture between HB1 and the Python agent
• Security: safe credential handling, preventing leaks
• Reference: Anon (payroll headless browser — no longer does headless but knows best practices)

*Action Items:*
:white_check_mark: Update Indeed sponsored job prompt: custom budget instructions + 1-week end date logic _(you)_
:white_check_mark: Investigate credit card prerequisite via Indeed account setup endpoint _(you)_
:white_check_mark: Spike on production agent architecture (latency, concurrency, HB1 comms, security) _(eng)_
:white_check_mark: Get Homebase credit card approved for running experiments independently _(you)_

━━ *4. Salesforce Reporting Gap: Per-Job Data Required* ━━
:calendar: 9:30am · Usman / Manan Sales Support · with Usman Zafar

*Decision:* Current Salesforce fields (cumulative applicants/screeners/top matches) are *not sufficient*. Need per-job V2-only data to power an unhealthy-trial outreach workflow.

*Rationale:* Back-of-napkin: ~450-500 jobs/week, ~40% ICP, ~70% unhealthy by Day 5 = ~140 businesses/week to reach out to. This is the rep motion that converts unhealthy trials. Without per-job Salesforce data, reps can't target systematically.

*Action Items:*
:white_check_mark: Write a Salesforce data requirements brief → share with Usman + Jotin _(you)_
:white_check_mark: Schedule early next week sync: Usman + Jotin + Rich → align on what eng delivers by end of next sprint _(you)_

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:muscle: *Manan, you drove serious strategic clarity today.* You sequenced Q3 correctly, you protected the team from premature production investment on the browser agent, and you identified the exact Salesforce gap blocking the sales motion. The Monday/Tuesday priorities are: (1) share the roadmap with Ted, (2) write the Salesforce brief, and (3) ping Rami on the outreach script. Everything else flows from those three.

Go enjoy your Friday evening — you earned it. :fire:"""


def main():
    if not SLACK_BOT_TOKEN:
        print(
            "⚠️  SLACK_BOT_TOKEN is not set.\n"
            "To enable automatic Slack delivery, add SLACK_BOT_TOKEN to your\n"
            "Cursor Dashboard → Cloud Agents → Secrets.\n\n"
            "Prepared Slack message:\n"
            + "=" * 60 + "\n"
            + MESSAGE
        )
        sys.exit(1)

    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=MESSAGE,
            mrkdwn=True,
            unfurl_links=False,
            unfurl_media=False,
        )
        print(f"✅ Daily summary sent to Slack! ts={response['ts']}")
        sys.exit(0)
    except SlackApiError as e:
        print(f"❌ Slack API error: {e.response['error']}")
        print(f"Full response: {e.response}")
        sys.exit(1)


if __name__ == "__main__":
    main()
