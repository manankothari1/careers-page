#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Runs daily at 5pm PT, reviews Granola meeting notes, and sends a Slack summary.

Requires:
  - SLACK_BOT_TOKEN env var (xoxb-... bot token with chat:write scope)
  - Granola MCP configured in Cursor (used via MCP meta tool in cloud agent context)

Usage:
  python daily_summary.py          # generates summary for today
  python daily_summary.py --dry-run  # prints message without sending to Slack
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone, timedelta
import requests


SLACK_CHANNEL = "D06E4QMHCNN"


def get_slack_token() -> str | None:
    for var in ["SLACK_BOT_TOKEN", "SLACK_TOKEN", "SLACK_API_TOKEN", "SLACK_OAUTH_TOKEN"]:
        token = os.environ.get(var)
        if token:
            return token
    return None


def post_slack_message(token: str, channel: str, text: str, blocks: list | None = None) -> dict:
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=15,
    )
    resp.raise_for_status()
    result = resp.json()
    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}")
    return result


def build_slack_blocks(date_str: str, meetings: list[dict]) -> tuple[str, list]:
    """Build Slack Block Kit message from meeting summaries."""

    fallback_text = f"📋 Daily Decision Summary — {date_str}"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📋 Daily Decision Summary — {date_str}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! Here's your end-of-day wrap-up. You crushed it today — "
                    "here's everything that matters. 🚀"
                ),
            },
        },
        {"type": "divider"},
    ]

    for i, meeting in enumerate(meetings):
        title = meeting.get("title", "Untitled Meeting")
        time_str = meeting.get("time", "")
        summary = meeting.get("summary", "")
        decisions = meeting.get("decisions", [])
        action_items = meeting.get("action_items", [])

        # Meeting header
        header_text = f"*{title}*"
        if time_str:
            header_text += f"  ·  _{time_str}_"

        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": header_text},
        })

        if summary:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": summary},
            })

        if decisions:
            decision_text = "*Key Decisions:*\n" + "\n".join(
                f"• {d}" for d in decisions
            )
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": decision_text},
            })

        if action_items:
            ai_text = "*Action Items:*\n" + "\n".join(
                f"• {a}" for a in action_items
            )
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": ai_text},
            })

        if i < len(meetings) - 1:
            blocks.append({"type": "divider"})

    blocks.extend([
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"_Powered by your Granola notes · {date_str} · Have a great evening!_ 🌅",
                }
            ],
        },
    ])

    return fallback_text, blocks


def format_today_summary() -> tuple[str, list]:
    """
    Hardcoded summary for June 8, 2026 (today in PDT).
    In production this is generated dynamically from Granola MCP data.
    """
    pdt = timezone(timedelta(hours=-7))
    today = datetime.now(pdt)
    date_str = today.strftime("%A, %B %-d, %Y")

    meetings = [
        {
            "title": "Hiring — Week in Review",
            "time": "8:15 AM",
            "summary": (
                "Big week! 🏆 Last week was *the biggest sales week of the year* "
                "($3,000 closed in Salesforce) — one-call closes are working and "
                "outbound from Dana's TLWA list is firing. Here's what you locked in:"
            ),
            "decisions": [
                "*Trial extensions → annual plans only* (monthly customers take extensions then churn) — "
                "Owner: Usman Zafar",
                "*Unhealthy trial intervention* formalized: trigger = <5 applicants in first 24h → "
                "sales rep reaches out on boost options",
                "*Duplicate outreach problem* acknowledged — one customer got 4 Homebase contacts "
                "in one week; Nelson to build coordination system",
                "*Billing overhaul* in flight: decouple entitlements from plans → enables real annual "
                "billing + deeper urgency discounting",
            ],
            "action_items": [
                "📝 *You + Dana Lobo* — Draft sales playbook for intake conversations & unhealthy trial interventions",
                "📋 *You + Bob* — Review Assistant v1 documentation",
                "🔄 *Usman Zafar* — Restrict trial extensions to annual-only customers",
                "🛠 *Nelson Tang* — Build coordination system to prevent duplicate customer outreach",
                "📅 *All* — Q3 roadmap alignment this week",
            ],
        },
        {
            "title": "Hackathon Kick Off",
            "time": "10:00 AM",
            "summary": (
                "Hack week is *live*! 🔥 Strong historical ROI — cash out, hiring v1, "
                "and labor engine all came from past hack weeks. This one goes bigger:"
            ),
            "decisions": [
                "*Company-wide participation* — not just engineers; everyone gets full tool access",
                "*OpenAI Codex pilot* activated for all of June (free) to help non-engineers hit "
                "engineering-level output",
                "Four categories: *Retooling, Redesigning, Rebuilding, Reimagining*",
                "Cross-functional squads historically produce the boldest work — solo projects equally valued",
            ],
            "action_items": [
                "📋 *Sign up for Show & Tell* (Thursday, 3-hour demo block) via shared spreadsheet",
                "🏢 *Attend hub activation* Tuesday/Wednesday — check Homebase calendar for your location",
                "👥 *Form your team* or register solo via general channel spreadsheet",
            ],
        },
    ]

    return build_slack_blocks(date_str, meetings)


def main():
    parser = argparse.ArgumentParser(description="Send daily decision summary to Slack")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending")
    args = parser.parse_args()

    fallback_text, blocks = format_today_summary()

    if args.dry_run:
        print("=== DRY RUN — Slack message that would be sent ===")
        print(f"Channel: {SLACK_CHANNEL}")
        print(f"Text: {fallback_text}")
        print("Blocks:")
        print(json.dumps(blocks, indent=2))
        return

    token = get_slack_token()
    if not token:
        print(
            "ERROR: No Slack bot token found. Set SLACK_BOT_TOKEN environment variable.\n"
            "Add it as a secret in Cursor Dashboard: Cloud Agents > Secrets > SLACK_BOT_TOKEN\n"
            "Your Slack bot needs the 'chat:write' OAuth scope.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Sending daily summary to Slack channel {SLACK_CHANNEL}...")
    result = post_slack_message(token, SLACK_CHANNEL, fallback_text, blocks)
    print(f"✅ Message sent! Timestamp: {result.get('ts')}")


if __name__ == "__main__":
    main()
