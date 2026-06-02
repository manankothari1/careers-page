#!/usr/bin/env python3
"""
Daily Decision Summary - Slack Sender
Chief of Staff automation for Manan Kothari @ Homebase
Runs daily at 5pm PT (midnight UTC) via Cursor Cloud Agent cron.

Usage:
    SLACK_BOT_TOKEN=xoxb-... python3 send_daily_summary.py --message "..."
    SLACK_BOT_TOKEN=xoxb-... python3 send_daily_summary.py --file summary.txt

Requires:
    pip install slack_sdk
    SLACK_BOT_TOKEN env variable with a bot token that has chat:write scope
    SLACK_CHANNEL_ID env variable (default: D06E4QMHCNN)
"""

import os
import sys
import argparse
from datetime import datetime

CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")


def send_slack_message(message: str) -> bool:
    """Send a message to the configured Slack channel. Returns True on success."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN environment variable not set.")
        print("Add it via Cursor Dashboard > Cloud Agents > Secrets")
        return False

    try:
        from slack_sdk import WebClient
        from slack_sdk.errors import SlackApiError

        client = WebClient(token=token)
        response = client.chat_postMessage(
            channel=CHANNEL_ID,
            text=message,
            mrkdwn=True,
        )
        if response["ok"]:
            print(f"Message sent successfully to {CHANNEL_ID}")
            return True
        else:
            print(f"Slack API returned error: {response}")
            return False
    except ImportError:
        print("ERROR: slack_sdk not installed. Run: pip install slack_sdk")
        return False
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        return False


def build_no_meetings_message(date_str: str) -> str:
    """Generate the message when no meetings were recorded today."""
    return f"""*📋 Daily Decision Summary — {date_str}*

Hey Manan! Checking in as your chief of staff. 🤝

*No meetings were captured in Granola today.* This could mean you had a lighter day, were heads-down, or Granola wasn't running during your calls. Either way — here's where things stand based on your most recent meetings:

---

*🔴 HOT: WBR is TOMORROW (June 3)*
Make sure you're prepped with key questions and your analysis. This is the moment to sharpen thinking on next month's priorities.

---

*🎯 Your Open Action Items (from last week)*

1. *Indeed Manual Sponsoring Validation* — Get 3 customers to sponsor jobs on Indeed manually this week. This is the key demand-proof gate before any engineering investment. Coordinate with Usman on outreach strategy.

2. *Linear Project Cleanup* — Extract Indeed entry point tickets from the Sponsored Jobs API project → move to Indeed 3LO UX project. Also connect #project-indeed-3lo Slack channel to the new structure.

3. *Indeed API Questions* — You committed to following up with Indeed on:
   • ATS plugin exemption from $3/call fee structure
   • Campaign analytics: requirement vs. option?
   • Separate redirect URL for account setup vs. token exchange

---

*📊 Project Status Snapshot*

• *Indeed Integration (3LO UX)* — Entry points 1, 2, 4 unblocked and can start now. Copy updates needed for EP 1 & 2.
• *Indeed Sponsored Jobs API* — Paused. Waiting on Indeed to confirm billing ($3/call) and analytics requirements.
• *Boost Modal* — "Sponsor on Indeed" manual button in progress. Purchase Homebase Boost XML fixes ongoing.
• *Careers Page 2.1* — Bug resolution in progress.
• *Talent Pool Experiments* — Show top 10 candidates post-job creation; freed up by 3LO pause.
• *Applicant Flow DS* — KO complete with Ted & Rami. Experiment targeting 300 candidates/job, test groups by 1/2/3yr inactivity.

---

*You're doing great, Manan — big week ahead with the WBR! Let's nail it. 💪*"""


def build_meetings_summary_message(date_str: str, meetings_summary: str) -> str:
    """Generate the message when meetings were recorded today."""
    return f"""*📋 Daily Decision Summary — {date_str}*

Hey Manan! Here's your end-of-day brief from your chief of staff. Here's what you decided, committed to, and need to follow up on today 👇

{meetings_summary}

---
_This summary was auto-generated from your Granola meeting notes._"""


def main():
    parser = argparse.ArgumentParser(description="Send daily Slack summary")
    parser.add_argument("--message", type=str, help="Message text to send")
    parser.add_argument("--file", type=str, help="File containing message to send")
    parser.add_argument("--no-meetings", action="store_true",
                        help="Send 'no meetings today' summary")
    args = parser.parse_args()

    today = datetime.now().strftime("%A, %B %-d, %Y")

    if args.no_meetings:
        message = build_no_meetings_message(today)
    elif args.file:
        with open(args.file, "r") as f:
            message = f.read()
    elif args.message:
        message = args.message
    else:
        print("ERROR: Provide --message, --file, or --no-meetings")
        sys.exit(1)

    success = send_slack_message(message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
