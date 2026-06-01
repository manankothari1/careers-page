#!/usr/bin/env python3
"""
Send today's daily decision summary to Slack.
This script is executed by the Cloud Agent after gathering Granola meeting data.
"""
import os
import sys
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

SLACK_CHANNEL_ID = "D06E4QMHCNN"

def send_blocks(token: str, channel: str, text: str, blocks: list) -> bool:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    client = WebClient(token=token)
    try:
        resp = client.chat_postMessage(channel=channel, text=text, blocks=blocks)
        print(f"SUCCESS ts={resp['ts']}")
        return True
    except SlackApiError as e:
        print(f"ERROR {e.response['error']}", file=sys.stderr)
        return False

# ─── Message content ─────────────────────────────────────────────────────────
DATE_STR = "Monday, June 1, 2026"

# Today (Sunday May 31 PDT / June 1 UTC) had no recorded meetings.
# The most recent workweek's key decisions are surfaced below as an EOW lookback.
SUMMARY = """\
*No meetings today* — it's a Sunday, so you get a pass! Here's your end-of-week decision \
lookback and everything you need to hit the ground running Monday morning. 🚀

─────────────────────────────────

*🔴 BIG CALL: Killing Indeed 3LO & Sponsored Jobs API*
*Meeting:* Hiring Leads Standup — May 28
*Decision:* Cancel the automated Indeed 3LO integration and sponsored jobs API work entirely.
*Rationale:* 2–3 month timeline, unclear customer demand, Indeed team causing scope creep and draining eng cycles.
*Path forward:* Add a manual "Sponsor on Indeed" button in the boost modal → link directly to Indeed job portal + help article. Prove demand first, automate later.
*Impact:* Frees up Jatin/Tanner for other experiments immediately.

─────────────────────────────────

*⚡ Decisions Made This Week*

1. *Zero state page removal experiment → GO* (May 28)
   Jatin implementing without disrupting sprint. Tanner may be pulled for 1-day removal work. Fadi's team confident in the lightweight dashboard redesign as the right path.

2. *Talent pool experiments → UNLOCKED* (May 28)
   With 3LO work paused, engineering capacity freed up. Show top 10 candidates to employers after job creation. Sprint 2612 (June 8) is the launch target.

3. *Manual sponsoring approach approved* (May 28)
   Button in boost modal → Indeed portal. Manan leads customer validation (3 customers this week). No automation until demand proven.

4. *Boost modal for "in-review" jobs → approved in principle* (May 22)
   Two paths: job auto-approves → boost auto-applies; job flagged → Michael's team handles outreach/refund. Manan to sync with Michael's team on implementation.

5. *Homebase Boost work target: complete by end of May 28 week* (May 20)
   Modal upgrade is NOT a blocker for Boost release. Modal update punted to next sprint.

─────────────────────────────────

*✅ YOUR Open Action Items (Don't Drop These!)*

• *[THIS WEEK]* Get 3 customers to sponsor jobs on Indeed manually — validate demand before re-investing eng
• *[THIS WEEK]* Coordinate with Usman on outreach strategy for those 3 customers
• *[JUNE 3 — WBR]* Prep key questions + analysis for WBR Wednesday. Every lead should come sharp.
• *[ONGOING]* Align with Rami on talent pool A/B test design — June 8 launch for Sprint 2612
• *[ONGOING]* Confirm ATS JS plugin exception eligibility with Indeed (avoids $3/API call charge)
• *[ONGOING]* Dana → define ICP: single location, 11–50 employees, frequent hirers, existing Homebase customers

─────────────────────────────────

*📅 Heads Up for This Week*

| Day | Event |
|-----|-------|
| Mon June 1 | Talent pool A/B test target launch (check in with Rami!) |
| Wed June 3 | *WBR* — come prepared |
| Fri June 6 | Manan flying in for offsite (Due West Fest was June 5–6) |

─────────────────────────────────

*💡 Ongoing Strategic Threads to Keep Momentum On*
• *Agentic Hiring Assistant* — Dana leading architecture; foundational tools (scheduling, status, messaging) with Applied AI. SF team meeting to define use cases.
• *Talent Pool* — North Star: 80% of jobs with healthy applicant flow (20+ applicants, 5+ top matches). Rami building the matching tech.
• *ICP Focus* — single location, frequent hirers, Homebase payroll/plus customers showing highest conversion.

You're making great calls, Manan. The 3LO pivot was bold and right — prove demand before you build. Monday's going to be a great day. 💪"""

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"📋 Daily Decision Summary — {DATE_STR}",
            "emoji": True,
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": SUMMARY},
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Automatically generated from your Granola meeting notes by your Chief of Staff AI_ 🤝",
            }
        ],
    },
]

token = os.environ.get("SLACK_BOT_TOKEN")
if not token:
    print("=" * 60)
    print("SLACK_BOT_TOKEN not found in environment.")
    print("To enable Slack sending, add SLACK_BOT_TOKEN as a Cursor Secret:")
    print("  Cursor Dashboard → Cloud Agents → Secrets → Add SLACK_BOT_TOKEN")
    print()
    print("Message that would be sent to", SLACK_CHANNEL_ID)
    print("=" * 60)
    print(SUMMARY)
    sys.exit(0)

success = send_blocks(token, SLACK_CHANNEL_ID, f"Daily Decision Summary — {DATE_STR}", blocks)
sys.exit(0 if success else 1)
