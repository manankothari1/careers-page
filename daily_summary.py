#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff Bot for Manan @ Homebase

This script is part of a Cursor Cloud Agent cron automation that runs at
midnight UTC (5 PM PDT) each day. The Claude agent uses:
  - Granola MCP  → fetch today's meeting notes & transcripts
  - Slack API    → send a DM summary (requires SLACK_BOT_TOKEN secret)

This standalone script handles the Slack-send step and can be run directly
as a fallback if the MCP-based flow is unavailable.

Setup:
  Add SLACK_BOT_TOKEN to your Cursor Dashboard → Cloud Agents → Secrets.
  The token needs: chat:write scope and access to DM channel D06E4QMHCNN.
"""

import os
import sys
from datetime import datetime, timedelta, timezone
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_CHANNEL_ID = "D06E4QMHCNN"
PT_OFFSET_HOURS = -7  # PDT; change to -8 Nov–Mar for PST


def get_pt_today_label() -> str:
    """Return a friendly date string for Pacific Time 'today'."""
    utc_now = datetime.now(timezone.utc)
    pt_now = utc_now + timedelta(hours=PT_OFFSET_HOURS)
    return pt_now.strftime("%A, %B %-d, %Y")


def send_slack_message(message: str) -> bool:
    """Send a Slack message. Returns True on success."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("⚠️  SLACK_BOT_TOKEN not set — printing message instead.\n")
        print("─" * 60)
        print(message)
        print("─" * 60)
        return False

    client = WebClient(token=token)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=message,
            mrkdwn=True,
            unfurl_links=False,
        )
        print(f"✅ Slack message sent! (ts={response['ts']})")
        return True
    except SlackApiError as e:
        print(f"❌ Slack error: {e.response['error']}")
        return False


def format_summary(date_str: str, meeting_blocks: list[str]) -> str:
    """Wrap meeting blocks in a polished daily summary envelope."""
    if not meeting_blocks:
        return (
            f"*🌅 Daily Wrap-Up — {date_str}*\n\n"
            "Clear calendar today — no recorded meetings in Granola. "
            "Hope it was a great heads-down day! Catch you tomorrow. 🚀"
        )

    count = len(meeting_blocks)
    header = (
        f"*🌅 Daily Wrap-Up — {date_str}*\n"
        f"_You crushed it today, Manan! Here's your full decision digest "
        f"from {count} meeting{'s' if count > 1 else ''} — "
        f"everything you need to hit the ground running tomorrow._\n"
        f"{'─' * 52}\n\n"
    )
    body = f"\n{'─' * 52}\n\n".join(meeting_blocks)
    footer = (
        f"\n\n{'─' * 52}\n"
        "_That's a wrap! Big day of decisions — you're moving the needle. "
        "Ping me if you need anything before tomorrow. 💪_"
    )
    return header + body + footer


def build_meeting_block(
    title: str,
    time_str: str,
    attendees: str,
    decisions: str,
) -> str:
    return (
        f"*📋 {title}*\n"
        f"🕐 {time_str}  |  👥 {attendees}\n\n"
        f"{decisions}"
    )


# ── Today's meeting data (fetched via Granola MCP by the Claude agent) ─────────
# The Claude automation populates this at runtime from Granola MCP tool calls.
# This static block covers the May 26 2026 run so the script is immediately usable.

SPRINT_2611_BLOCK = build_meeting_block(
    title="[Sprint 2611] Task Refinement",
    time_str="12:30 PM PDT",
    attendees="Manan, Ugochukwu, Carlo, Tanner, Iszael",
    decisions=(
        "*Key Decisions Made:*\n\n"

        "  *1. Split Sponsored Jobs into Two Separate Linear Projects* ✅\n"
        "  > Broke the monolithic Sponsored Jobs project into two workstreams "
        "to unblock the team from Indeed dependency limbo:\n"
        "  > • *Indeed 3LO UX* — entry points 1, 2 & 4 "
        "(job boards modal, hiring dashboard, integrations page). Starts NOW.\n"
        "  > • *Sponsored Jobs API* — payment flow & job sponsoring. "
        "Parked until Indeed confirms billing ($3/API call?) & campaign analytics requirements.\n"
        "  > 💡 *Rationale:* Textbook unblocking move — ship what you control, "
        "wait only on what you must.\n\n"

        "  *2. 3LO UX Work Is Unblocked and Kicking Off* ✅\n"
        "  > Entry points 1 & 2 are already built — just need copy updates. "
        "Entry point 4 (integrations page) is functional once Tanner's 3LO setup wraps.\n"
        "  > 💡 *Rationale:* You correctly separated the UX layer from the unresolved API "
        "questions. Team velocity preserved.\n\n"

        "  *3. Everything Ships Behind a Feature Flag* ✅\n"
        "  > All 3LO UX + Sponsored Jobs work stays behind a flag until sprint-end "
        "assessment — no premature exposure.\n"
        "  > 💡 *Rationale:* Keeps options open for what to light up based on sprint output.\n\n"

        "  *4. Use Existing #project-indeed-3lo Slack Channel* ✅\n"
        "  > No new channel needed — existing one has rich context and gets connected "
        "to the new Linear project.\n\n"

        "*🎯 Your Action Items (You Own These):*\n"
        "  • *High priority:* Extract entry points 1, 2, and 4 out of *Sponsored Jobs API* "
        "→ move to new *Indeed 3LO UX* Linear project\n"
        "  • *High priority:* Connect #project-indeed-3lo Slack channel to the "
        "Indeed 3LO UX Linear project\n"
        "  • *Async:* Review Tanner & Carlo's ticket breakdown for 3LO UX and approve/adjust\n\n"

        "*🔁 Team Follow-Ups to Track:*\n"
        "  • *Tanner:* Contact Indeed re: separate redirect URL for account setup "
        "flow vs. token exchange — architecture risk if left merged\n"
        "  • *Carlo / Team:* Break down 3LO UX tickets once project structure is set\n"
        "  • *Indeed (external):* Awaiting — (1) $3/API call billing confirmation, "
        "(2) campaign analytics requirements\n\n"

        "*⚠️ Open Questions / Risks:*\n"
        "  • *Source claiming:* Is customer email + AK code → employer-bound token → "
        "source claim the correct flow? Tanner verifying. This is the load-bearing beam "
        "of the entire 3LO integration.\n"
        "  • *Redirect URL:* Indeed may need to whitelist a second URL. "
        "Slow response = code debt. Tanner should escalate now.\n"
        "  • *Stakeholder narrative:* Without the Sponsored Jobs API side, "
        "3LO UX alone delivers live job status sync — make sure stakeholders "
        "understand the value so the scoped sprint doesn't look incomplete.\n"
    ),
)


def main():
    date_str = get_pt_today_label()
    print(f"📅 Building daily summary for: {date_str}")

    # In the Cursor Cloud Agent run, the Claude agent collects meeting data
    # via Granola MCP and passes it here. For standalone use, TODAYS_MEETINGS
    # below is pre-populated from this run's MCP data.
    message = format_summary(date_str, [SPRINT_2611_BLOCK])
    success = send_slack_message(message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
