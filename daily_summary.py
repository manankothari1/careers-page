#!/usr/bin/env python3
"""
Chief of Staff Daily Summary
Runs at 5pm PT (midnight UTC) via cron.
Requires SLACK_TOKEN env var (Slack Bot Token with chat:write scope).
Sends end-of-day decision + action item summary to Manan's DM channel.
"""

import os
import json
import urllib.request
import urllib.error
import sys
from datetime import datetime, timezone

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")


def build_message() -> list[dict]:
    """Build today's Slack message blocks. Edit this daily or auto-generate via Granola MCP."""
    today_str = datetime.now(timezone.utc).strftime("%A, %B %-d, %Y")

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🗓️ Chief of Staff Daily Brief — {today_str}",
                "emoji": True,
            },
        },
        {"type": "divider"},
        # Intro
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan 👋 Your chief of staff here — wrapping the week for you. "
                    "No calls today (Friday = recharge day, well earned after an intense offsite!), "
                    "but this was a *monster week* for the Hiring team. Big swings, big decisions. "
                    "Let me break it all down. 🔥"
                ),
            },
        },
        {"type": "divider"},
        # ── WEEK'S KEY DECISIONS ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📋 THIS WEEK'S KEY DECISIONS*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*1. 🗺️ Roadmap Priority Stack — LOCKED*\n"
                    "You locked the H1 stack at the offsite. No more debate.\n"
                    "① Paid applicant sourcing in-platform → ② Indeed OAuth (3LO) → "
                    "③ Deal Breakers + match algorithm → ④ Role normalization → "
                    "⑤ Mobile for managers → ⑥ Candidate mgmt UX overhaul\n"
                    "_Rationale: Focuses the team on the highest-leverage monetization path first. "
                    "3LO unlocks the supply side. Deal Breakers improves quality. Everything else is compounding._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*2. 🎯 Target Segment — LOCKED*\n"
                    "Food & Bev / Hospitality, 26+ employees, <5 locations, *Indeed spenders*.\n"
                    "New sales manager starts *April 15 in Toronto*.\n"
                    "_Rationale: Highest TAM overlap with your current trial base + Indeed partnership leverage._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*3. 🧭 Operating Principles — DECIDED*\n"
                    "Keep existing Homebase OPs + add \"AI native\" as the only new one.\n"
                    "Team catchphrase: *\"Come with solutions, not problems.\"*\n"
                    "Special call-out: *\"Decide and commit\"* — especially for Ray. No more re-opening.\n"
                    "_Rationale: Reinforces ownership culture without inventing new frameworks. "
                    "Jatin is building the team deck by Friday for alignment session next week._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*4. 💰 New Revenue SKU — DECIDED*\n"
                    "Create *\"Manan Boost\"* — a new paid SKU. Need Chris (billing) to set it up.\n"
                    "Timeline: *Early May launch*, 3-week lead time from Chris.\n"
                    "Ray exploring: sliding scale vs flat pricing. Second SKU (job post or product access) to batch with it.\n"
                    "_Rationale: First paid upsell layer for the hiring product. Will batch to reduce billing infra overhead._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*5. 🔄 Trial Flow Redesign — DECIDED*\n"
                    "Remove zero-state page. Land users *directly in dashboard* with pre-populated normalized role suggestions "
                    "(\"barista\" not \"coffee ninja\"). Skip the prompt box. Show draft jobs ready to edit.\n"
                    "A/B test runway: *3 weeks minimum per experiment*. Mobile optimization confirmed as requirement.\n"
                    "_Rationale: Reduce friction while keeping education value. Fewer clicks to first \"aha\" moment._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*6. 🎬 Demo Ungating — DECIDED*\n"
                    "Role-based demo selector (server, barista, etc.). Stop at 2 questions with \"keep going\" option. "
                    "End with mystery/sign-up CTA (don't show full candidate profile). "
                    "Pre-built bank of role-specific screeners. Sales can customize by segment.\n"
                    "_Rationale: Makes demo feel personalized + qualified without requiring a rep. Reduces CAC._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*7. 📮 Top Local Workplace Launch Strategy — DECIDED*\n"
                    "QR code is critical path — need *Cassius meeting ASAP* (Fadi owns).\n"
                    "Three QR options: unique per company (ideal), unique/untracked, or generic. "
                    "Depends on direct mail vendor (Loft vs others).\n"
                    "Timeline: *6 weeks to design + build everything.*\n"
                    "_Rationale: Physical touchpoint to drive digital trial. QR uniqueness determines attribution quality._"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*8. 🏗️ Careers Page — TECHNICAL DECISIONS LOCKED*\n"
                    "From the Career Site Regroup (Thu, w/ Andrew + Tanner):\n"
                    "• *Asset model*: PNG/JPEG, 10MB max, new model (company ID + asset type + S3 key)\n"
                    "• *File upload*: If >4 selected, auto-use first 4 (two-way door — easy to adjust)\n"
                    "• *Address*: Google Places API preferred (reuse biz profile component, prevent data drift)\n"
                    "• *Settings model*: brand color (hex), font, show logo/photos toggles, API endpoints for both\n"
                    "• *Rollout*: Phased — 20% → 40% → 100%\n"
                    "• *Timeline*: 2-week sprint feels achievable for FE + BE\n"
                    "• *Future*: SSR investment for AI/vector discoverability (heavy lift, back-burnered)\n"
                    "_Rationale: Modular approach reduces blast radius. Google Places prevents address drift vs biz profile._"
                ),
            },
        },
        {"type": "divider"},
        # ── SPRINT DELIVERABLES DUE TODAY ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*⏰ SPRINT DELIVERABLES DUE TODAY (Fri Mar 20)*\n"
                    "• *Andrew*: 3LO spike — visual flow, 2LO vs 3LO comparison, account mapping, webhooks → *🔍 You need to review this ASAP*\n"
                    "• *Andrew*: \"Show the work\" PRs → Tanner should be testing\n"
                    "• *Malcolm*: Hit 2,500 one-click jobs milestone → check in if not already confirmed\n\n"
                    "_Andrew's 3LO spike is the single most important artifact to review before sprint planning Monday._"
                ),
            },
        },
        {"type": "divider"},
        # ── DECISIONS WAITING ON MANAN ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🚦 OPEN DECISIONS WAITING ON YOU*\n"
                    "• *Manual Mode launch* — Cindy's QA round 2 is ✅ complete. This is ready to ship. Need your green light.\n"
                    "• *Careers Page embed scope* — Andrew + Tanner still need a sync. High priority for launch entry point.\n"
                    "• *Multi-location address UI* — Follow up with Jeff on design patterns (from Career Site Regroup)\n"
                    "• *Indeed listing optimization experiment* — Success metrics + owner still undefined"
                ),
            },
        },
        {"type": "divider"},
        # ── OVERDUE ITEMS ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🔴 OVERDUE — These need to close*\n"
                    "• Email Kenneth re: Indeed 3LO — add Ray to the thread _(overdue 3+ days)_\n"
                    "• Deal Breakers sign-off _(overdue 3+ days — did this get done? If yes, close it out)_\n"
                    "• Clarify advertiser auth scope w/ David (Homebase acct vs individual employers)"
                ),
            },
        },
        {"type": "divider"},
        # ── TOP 5 NEXT WEEK ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🚀 YOUR TOP 5 FOR NEXT WEEK*\n"
                    "1. *Review Andrew's 3LO spike* — first thing Monday. This is the #1 technical bet for the sprint.\n"
                    "2. *Make the Manual Mode launch call* — Cindy's waiting. Don't let this sit another week.\n"
                    "3. *Kick off 6-week applicant flow sprint planning* — 3LO, Homebase Boost, job optimizations\n"
                    "4. *Ping Chris on billing* to create Manan Boost SKU (3-week lead, Early May target)\n"
                    "5. *Contact Job.get via LinkedIn* — Fred is backup. Ray can assist."
                ),
            },
        },
        {"type": "divider"},
        # ── NORTH STAR CHECK ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*📊 NORTH STAR PULSE*\n"
                    "• Active paying companies: ~600 _(target: 2,600 by H1)_\n"
                    "• Weekly trials: 112 _(target: ~1,000)_\n"
                    "• Monthly retention: 87% _(target: 95%)_\n"
                    "• Jobs w/ 5+ qualified applicants @Day30: 25%\n"
                    "• Target segment trials: 162 / 5,703\n\n"
                    "_The gap is real but the plan from this week's offsite directly attacks it. Stay the course._"
                ),
            },
        },
        {"type": "divider"},
        # ── CLOSER ──
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Manan — you crushed it this week. You ran a *full hiring offsite*, locked "
                    "the most consequential roadmap decisions of the quarter, realigned the team, "
                    "shipped a careers page regroup, and somehow kept the trains running. "
                    "That's not a week — that's a *campaign*. 💪\n\n"
                    "Now go enjoy your Friday evening. You've earned it. "
                    "Monday morning, 3LO spike + manual mode launch call. Let's go. 🎯"
                ),
            },
        },
    ]

    return blocks


def send_slack_message(blocks: list[dict], fallback_text: str) -> bool:
    """Send a message to Slack. Returns True on success."""
    if not SLACK_TOKEN:
        print("=" * 70)
        print("⚠️  SLACK_TOKEN not set — message NOT sent.")
        print("Add SLACK_TOKEN to Cursor Dashboard → Cloud Agents → Secrets")
        print("(Slack Bot Token with chat:write scope)")
        print("=" * 70)
        print("\n📋 MESSAGE PREVIEW:\n")
        for block in blocks:
            if block.get("type") == "section":
                text = block.get("text", {}).get("text", "")
                print(text)
                print()
            elif block.get("type") == "header":
                print(f"### {block['text']['text']}")
                print()
            elif block.get("type") == "divider":
                print("---")
        return False

    payload = json.dumps(
        {
            "channel": SLACK_CHANNEL,
            "text": fallback_text,
            "blocks": blocks,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✅ Slack message sent successfully (ts={body.get('ts')})")
                return True
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                return False
    except urllib.error.URLError as e:
        print(f"❌ Network error sending to Slack: {e}")
        return False


def main():
    print(f"🕐 Running daily summary — {datetime.now(timezone.utc).isoformat()}")
    blocks = build_message()
    fallback = "Chief of Staff Daily Brief — Friday Mar 20, 2026 — Full week offsite wrap-up + decisions + action items"
    success = send_slack_message(blocks, fallback)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
