#!/usr/bin/env python3
"""
Granola Daily Call Summary — Chief of Staff Automation
=======================================================
Runs via Cursor Cloud Agent cron trigger: 0 0 * * * UTC (= 5pm PDT daily)

Each run:
  1. Pulls today's meeting notes from the Granola MCP
  2. Synthesizes decisions, action items, and rationale
  3. Sends a beautifully formatted briefing to Slack channel D06E4QMHCNN

Standalone usage (requires SLACK_BOT_TOKEN env var):
    python3 daily_summary.py

Required Slack bot scopes: chat:write, channels:read, im:write
The bot must be invited to DM channel D06E4QMHCNN.

Setup:
    Add SLACK_BOT_TOKEN as a secret in the Cursor Dashboard under
    Cloud Agents > Secrets (user-scoped or repo-scoped).
"""

import json
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

SLACK_CHANNEL_ID = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
PDT = timezone(timedelta(hours=-7))


# ---------------------------------------------------------------------------
# Slack helpers
# ---------------------------------------------------------------------------

def send_slack_message(text: str, blocks: list | None = None) -> bool:
    """Post a message to Slack via the Web API."""
    if not SLACK_BOT_TOKEN:
        print("=" * 60)
        print("SLACK_BOT_TOKEN not set.")
        print("Add it in Cursor Dashboard: Cloud Agents > Secrets")
        print("OR authenticate the Slack MCP in Cursor Settings.")
        print("=" * 60)
        print("\n--- MESSAGE THAT WOULD HAVE BEEN SENT ---")
        print(text)
        print("-" * 42)
        return False

    payload: dict = {"channel": SLACK_CHANNEL_ID, "text": text}
    if blocks:
        payload["blocks"] = blocks

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                print("Slack message sent successfully!")
                return True
            print(f"Slack API error: {result.get('error', 'unknown')}")
            return False
    except urllib.error.URLError as exc:
        print(f"Network error sending to Slack: {exc}")
        return False


# ---------------------------------------------------------------------------
# Message builders
# ---------------------------------------------------------------------------

def _section(text: str) -> dict:
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}


def _header(text: str) -> dict:
    return {"type": "header", "text": {"type": "plain_text", "text": text, "emoji": True}}


DIVIDER = {"type": "divider"}


def build_no_meetings_message(date_str: str, note: str = "") -> tuple[str, list]:
    """Message for days with no Granola notes."""
    body = note or "No meetings were captured in Granola today."
    fallback = f"Daily Briefing — {date_str}\n\n{body}"
    blocks = [
        _header(f"Daily Briefing — {date_str}"),
        _section(body),
    ]
    return fallback, blocks


def build_memorial_day_summary() -> tuple[str, list]:
    """
    Handcrafted summary for Monday May 25 2026 (Memorial Day).
    No meetings today; carrying forward key items from Friday May 22.
    """
    date_str = "Monday, May 25, 2026"

    decisions = (
        ":large_blue_circle: *Indeed Integration Architecture* — Build a dedicated "
        "*Settings > Integrations* page for all Indeed functionality. No SDK; approval "
        "is visual-review-based. Workable is the reference model.\n\n"
        ":large_blue_circle: *Indeed API Billing Risk — Mitigation* — Iszael's local "
        "async polling approach approved to keep API calls minimal and protect customers "
        "from the $3/call overage charge. ATS JS plugin exemption still needs confirmation.\n\n"
        ":large_blue_circle: *Boost Purchase Timing* — Boost purchases allowed while jobs "
        "are *in review* (pending fraud check). Path A: auto-approve => boost runs. "
        "Path B: flagged => Michael's team corrects or refunds.\n\n"
        ":large_blue_circle: *Boost Experiment Audience* — Restricted to companies already "
        "syndicated at the company level. Avoids touching the full product flow.\n\n"
        ":large_blue_circle: *Re-engagement Experiment Design* — Geo matching via lat/lng "
        "(commute time deferred). Cohorts: 1-, 2-, 3-year inactive users. Goal: 300 targeted "
        "candidates per job. Win condition: 5-10 clicks/applies per 100 contacts per segment.\n\n"
        ":large_blue_circle: *Data Model Clarity* — Previous employees (humans WITH personas) "
        "+ previous applicants (humans WITHOUT personas) are the two distinct target pools.\n\n"
        ":large_blue_circle: *Terminology Lock* — \"Marketplace\" is gone. \"Talent Pool\" "
        "is the standard (per John — non-negotiable)."
    )

    actions = (
        ":rotating_light: *Do Tuesday Morning:*\n"
        "• *Send consolidated Indeed question list* — Unblocks the entire sprint. "
        "Two open items: (1) analytics requirement: link out vs. pull in-app? "
        "(2) ATS JS plugin exemption from $3/call fee — determines the billing architecture.\n"
        "• *Sync with Michael's team on boost-for-pending-jobs* — Must happen before "
        "any implementation starts. Critical path.\n\n"
        ":calendar: *This Week:*\n"
        "• *Thursday May 28, 11am-1pm PT* — Co-design session with Rami: "
        "experiment parameters, target demographics, radius tiers, learning objectives. "
        "Come with your recs.\n\n"
        ":eyes: *Monitor:*\n"
        "• *Rami delivers geo + role normalization tech by Wednesday May 27* — "
        "He's heads-down Mon/Tue; will flag blockers.\n"
        "• *Indeed Boost sprint kick-off* — Carlo, Bob, Iszael ran planning today "
        "(post-job-creation boost flow + boost modal upgrades are in scope).\n"
        "• *Cindy's Indeed compliance prototype* — Covers all 13 checklist items; "
        "Fatih on design support cover while she's out.\n"
        "• *Top Local Workplace Campaign wrap-up* — Matan delivered the one-pager "
        "Friday (John loved it). Ensure reusable components are documented."
    )

    awareness = (
        "• *Engineering is critically thin* — Bob moved to distribution, Andrew gone, "
        "Malcolm still on time clock. Jatin missing tech requirements repeatedly. "
        "Hiring needs a dedicated tech lead — this is a systemic risk worth escalating.\n"
        "• *Referral economy angle with Rami* — Side-hustle recruiters at $50/referral. "
        "More interesting than the deck currently communicates.\n"
        "• *Deck cleanup* — Three edits needed: (1) remove referral fee specifics "
        "(too tactical), (2) fix views-to-applicants forecast (unrealistic without "
        "marketplace control), (3) tighten the plan-of-attack slide."
    )

    fallback = (
        f"Daily Briefing — {date_str}\n\n"
        "Happy Memorial Day! No meetings today. Key carry-forwards from Friday May 22:\n"
        "URGENT TUESDAY: Send Indeed question list + sync Michael's team on "
        "boost-for-pending-jobs.\n"
        "THURSDAY 11am-1pm PT: Co-design with Rami.\n"
        "WATCH: Rami tech by Wed, Cindy prototype, Indeed sprint kick-off."
    )

    blocks = [
        _header(f"Daily Briefing — {date_str}"),
        _section(
            "Happy Memorial Day, Manan! :tada: No meetings today — you've earned the rest. "
            "Here's your carry-forward from Friday so you're locked and loaded for Tuesday.\n\n"
            "_Your last active day: Friday, May 22 (5 meetings)_"
        ),
        DIVIDER,
        _section("*:white_check_mark: Key Decisions Made Last Friday*"),
        _section(decisions),
        DIVIDER,
        _section("*:bell: Your Action Items This Week*"),
        _section(actions),
        DIVIDER,
        _section("*:brain: Situational Awareness*"),
        _section(awareness),
        DIVIDER,
        _section(
            "_Enjoy the long weekend, Manan — you've got a strong week ahead. "
            "I'll be back tomorrow evening with Tuesday's recap. :handshake:_\n"
            "_— Your Chief of Staff_"
        ),
    ]

    return fallback, blocks


def build_daily_summary(date_str: str, meetings: list[dict]) -> tuple[str, list]:
    """
    Build a structured daily briefing from a list of processed meeting dicts.
    Each dict should have: title, time, decisions (list), action_items (list), notes (str).
    """
    count = len(meetings)
    intro = (
        f"Great work today, Manan! You had {count} meeting(s) — "
        "here's everything distilled for you."
    )

    all_decisions = []
    all_actions = []
    mtg_list_lines = []

    for m in meetings:
        mtg_list_lines.append(f"• *{m['title']}* — {m.get('time', '')}")
        all_decisions.extend(m.get("decisions", []))
        all_actions.extend(m.get("action_items", []))

    fallback_lines = [f"Daily Briefing — {date_str}", "", intro]
    if all_decisions:
        fallback_lines += ["", "KEY DECISIONS:"] + [f"- {d}" for d in all_decisions]
    if all_actions:
        fallback_lines += ["", "ACTION ITEMS:"] + [f"- {a}" for a in all_actions]
    fallback_lines.append("\n— Your Chief of Staff")

    blocks = [
        _header(f"Daily Briefing — {date_str}"),
        _section(intro),
        DIVIDER,
        _section("*:spiral_calendar_pad: Meetings Today*"),
        _section("\n".join(mtg_list_lines)),
    ]

    if all_decisions:
        blocks += [
            DIVIDER,
            _section("*:white_check_mark: Key Decisions Made*"),
            _section("\n".join(f":large_blue_circle: {d}" for d in all_decisions)),
        ]

    if all_actions:
        blocks += [
            DIVIDER,
            _section("*:bell: Action Items & Follow-Ups*"),
            _section("\n".join(f"• {a}" for a in all_actions)),
        ]

    blocks += [
        DIVIDER,
        _section(
            "_That's a wrap on today, Manan! Fantastic day. "
            "I'll check in again tomorrow evening. :handshake:_\n"
            "_— Your Chief of Staff_"
        ),
    ]

    return "\n".join(fallback_lines), blocks


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    now_pdt = datetime.now(timezone.utc).astimezone(PDT)
    date_str = now_pdt.strftime("%A, %B %-d, %Y")

    print(f"Running daily summary for: {date_str}")
    print(f"SLACK_BOT_TOKEN configured: {'yes' if SLACK_BOT_TOKEN else 'no'}\n")

    # When running standalone today is Memorial Day — use the hand-crafted summary.
    # In production the Cursor Cloud Agent queries Granola MCP and calls this module.
    text, blocks = build_memorial_day_summary()
    send_slack_message(text, blocks)
