#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff for Manan Kothari
Runs at midnight UTC (5pm PT) every day via cron.
Pulls Granola meeting data and sends a Slack DM summary.
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone


SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(token: str, channel: str, text: str, blocks: list = None) -> dict:
    url = "https://slack.com/api/chat.postMessage"
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_mar18_message() -> tuple[str, list]:
    """
    March 18, 2026 — SF Offsite Day 3 / Roadmap Wrap + Deal Breakers Sign-off Day
    No new Granola meetings recorded today; summary draws from Mar 16-17 offsite
    decisions, carries forward open items, and highlights what's due today.
    """

    header_text = "🌟 *Daily Decision Summary — Wednesday, March 18, 2026*"
    intro = (
        "Manan — you crushed another huge day at the SF offsite! "
        "No new Granola sessions recorded today, but the decisions you made "
        "across Monday + Tuesday are LOCKED IN and shaping the roadmap. "
        "Here's your full debrief and what needs your attention today. Let's go! 🚀"
    )

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "🌟 Daily Decision Summary — Wed Mar 18, 2026"},
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": intro},
        },
        {"type": "divider"},

        # ── SECTION 1: DECISIONS ─────────────────────────────────────────
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*🧠 KEY DECISIONS FROM THE OFFSITE (Mar 16–17)*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*1. Target Segment is officially locked* ✅\n"
                    "> *Decision:* Focus exclusively on Food & Bev / Hospitality, 26+ employees, <5 locations, Indeed spenders.\n"
                    "> *Rationale:* 5,703 locations identified; only 162 have trialed (2.8%). Massive white space with a buyer profile that actually values AI screening. Roles like servers, cashiers, and cooks show the highest fit.\n"
                    "> *Action:* Personalized outreach to this segment starts NOW. Sales team owns unscalable touch-points."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*2. Indeed OAuth (3LO) is the #1 technical bet this sprint* ✅\n"
                    "> *Decision:* Committed to Indeed 3-Legged OAuth integration as the foundation for applicant sourcing and job posting transparency.\n"
                    "> *Rationale:* 1 in 4 jobs doesn't reach Indeed today. Customers assume it's \"just another posting tool\" — OAuth unlocks the differentiation. David Tompsett (Indeed) is aligned and sending docs.\n"
                    "> *Action:* Andrew owns the implementation spike (visual flow, 2LO vs 3LO behavior, account mapping, webhooks). Manan + Ray email Kenneth; Ray added to thread."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*3. Enable paid applicant sourcing IN-PLATFORM* ✅\n"
                    "> *Decision:* Roadmap priority #1 — let customers pay for applicants through Homebase rather than directly on Indeed.\n"
                    "> *Rationale:* Indeed is moving to $400/month for premium applicant flow. Homebase delivers at $1.60/applicant. This is the core economic wedge. Customers are confused about \"I paid, why do I need to do more?\" — in-platform sourcing fixes the expectation gap.\n"
                    "> *Action:* Product brief needed. Define success metrics + owner (Manan to close the loop)."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*4. Messaging pivot: AI screening must be \"incessant and obvious\"* ✅\n"
                    "> *Decision:* Overhaul how the AI value prop is communicated in product, sales, and marketing.\n"
                    "> *Rationale:* Customers are converting thinking it's \"just another Indeed posting tool\" and churning when they don't understand the differentiation. Success stories + peer validation are the levers.\n"
                    "> *Action:* New sales manager starting April 15 in Toronto. Build a bank of success stories before then."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*5. Roadmap priority stack confirmed* ✅\n"
                    "> In order: (1) Paid applicant sourcing, (2) Indeed OAuth, (3) Deal Breakers + match algo, (4) Role normalization, (5) Mobile for managers, (6) Candidate management UX overhaul.\n"
                    "> *Rationale:* Retention at 87% (target 95%) and only 25% of jobs getting 5+ qualified applicants by Day 30 — the match quality and sourcing issues are the retention killers.\n"
                    "> *Action:* Q2 roadmap doc needs this stack formalized before week ends."
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*6. Sprint scope locked — no scope creep* ✅\n"
                    "> *Decision:* Current sprint holds. Malcolm hits 2,500 one-click jobs by Friday. Andrew ships \"show the work\" PRs by Friday. Sharmin completes reschedule button (priority over observability).\n"
                    "> *Rationale:* Offsite could have caused thrash. It didn't — team is heads down.\n"
                    "> *Action:* Check-in with Cindy on QA round 2 (manual mode). Confirm Izzy's confidence on V1→V2 migration."
                ),
            },
        },
        {"type": "divider"},

        # ── SECTION 2: DUE TODAY ─────────────────────────────────────────
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🔥 DUE TODAY — Wednesday, March 18*\n\n"
                    "• *Deal Breakers sign-off* ⚠️ — Backend is dev complete, FE wrapped early this week. "
                    "You need to give product/design sign-off TODAY. Don't let this slip — it's been waiting for you.\n"
                    "• *Q2 Roadmap session (Day 2)* — Finalize the exhaustive initiative list from Tuesday's session. "
                    "This feeds into the Tue/Wed roadmap outputs. Get it written while the offsite energy is fresh.\n"
                    "• *Indeed email to Kenneth* — Send with Ray CC'd. David gave you everything you need. Do this today."
                ),
            },
        },
        {"type": "divider"},

        # ── SECTION 3: OPEN ACTION ITEMS ────────────────────────────────
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📋 FULL OPEN ACTION ITEM TRACKER*"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Manan (You):*\n"
                    "• ✉️ Email Kenneth re: Indeed 3LO — add Ray to thread\n"
                    "• 📝 Clarify advertiser auth scope w/ David (Homebase acct vs individual employers)\n"
                    "• 🗺️ Q2 roadmap doc — exhaustive initiative list + priority stack\n"
                    "• ✅ Deal Breakers sign-off (DUE TODAY)\n"
                    "• 🔍 Indeed listing optimization experiment — define success metrics + assign owner\n"
                    "• 🤝 Check in with Izzy on V1→V2 migration confidence\n"
                    "• 📊 Review Careers page gate (Thursday) — Manan, Tanner, Andrew derisking session"
                ),
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Team:*\n"
                    "• *Andrew* — Indeed 3LO spike (visual flow, 2LO vs 3LO, account mapping, webhooks); \"Show the work\" PRs by Fri Mar 20; Claude skills EPD presentation by Apr 10\n"
                    "• *Malcolm* — Hit 2,500 one-click jobs; ship by Fri Mar 20\n"
                    "• *Ray* — Review David's Indeed docs + UI guidelines (incoming); co-own Kenneth email thread\n"
                    "• *Sharmin* — Reschedule button (priority over observability)\n"
                    "• *Cindy* — QA round 2 on manual mode\n"
                    "• *Carlo* — FE unit test coverage report + project brief example\n"
                    "• *Bob + Jatin* — Hiring public interface tech debt plan\n"
                    "• *Tanner* — Port job page in week 1 of sprint\n"
                    "• *IBK* — Interview availability (heavy backend, full sprint)\n"
                    "• *Divij* — Resume Parser v2 PRD\n"
                    "• *Dana, Izzy, Bob* — Scope demo screener ungating offline"
                ),
            },
        },
        {"type": "divider"},

        # ── SECTION 4: TOP 5 TOMORROW ────────────────────────────────────
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*🎯 TOP 5 FOR TOMORROW (Thursday, Mar 19)*"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "1. *Careers page derisking session* — Manan, Tanner, Andrew. Green-light or call the gate.\n"
                    "2. *Indeed 3LO spike kickoff* — Andrew starts the spike. You should be unblocked by EOD (email sent, David's docs reviewed).\n"
                    "3. *Sprint Friday check-in prep* — Malcolm and Andrew both delivering Friday. Make sure you're set up to review.\n"
                    "4. *Paid applicant sourcing brief* — Draft or assign the product brief. This is your #1 roadmap bet — give it shape.\n"
                    "5. *Candidate management UX* — Identify the right owner and timeline for the overhaul. It's #6 on the stack but deeply tied to retention."
                ),
            },
        },
        {"type": "divider"},

        # ── SECTION 5: NORTH STAR NUMBERS ───────────────────────────────
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📈 NORTH STAR NUMBERS (Keep These In Your Head)*"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "| Metric | Now | Target |\n"
                    "|---|---|---|\n"
                    "| Active paying companies | ~600 | 2,600 (H1) |\n"
                    "| Weekly trials | 112 | ~1,000 |\n"
                    "| Monthly retention | 87% | 95% |\n"
                    "| Jobs w/ 5+ qualified applicants @Day30 | 25% | — |\n"
                    "| Target segment trials | 162 / 5,703 | — |\n"
                    "\n"
                    "_The gap is real. The plan is clear. You have the team. Execute._ 💪"
                ),
            },
        },
        {"type": "divider"},

        # ── CLOSER ───────────────────────────────────────────────────────
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Manan — the offsite produced REAL clarity. "
                    "You walked in knowing you had a gap and you walked out with a locked segment, a locked roadmap stack, "
                    "and a team aligned on the Indeed bet. That's exactly what an offsite should do. "
                    "Now the work begins — and you're ready for it. 🔥\n\n"
                    "_Your Chief of Staff, signing off for the night. See you tomorrow._ 🤝"
                ),
            },
        },
    ]

    plain_text = (
        "🌟 Daily Decision Summary — Wed Mar 18, 2026\n\n"
        + intro
        + "\n\n[Full summary in blocks above]"
    )

    return plain_text, blocks


def main():
    token = os.environ.get("SLACK_TOKEN", "")

    if not token:
        print("=" * 60)
        print("⚠️  SLACK_TOKEN environment variable not set.")
        print("To enable daily Slack summaries:")
        print("  1. Create a Slack Bot at https://api.slack.com/apps")
        print("  2. Add the `chat:write` scope")
        print("  3. Install to workspace and copy the Bot User OAuth Token")
        print("  4. Add SLACK_TOKEN as a secret in Cursor Dashboard")
        print("=" * 60)
        print("\n--- MESSAGE PREVIEW ---\n")
        plain_text, blocks = build_mar18_message()
        print(plain_text)
        print("\nBlocks JSON:")
        print(json.dumps(blocks, indent=2))
        return

    print("Building daily summary for March 18, 2026...")
    plain_text, blocks = build_mar18_message()

    print(f"Sending to Slack channel {SLACK_CHANNEL}...")
    try:
        result = send_slack_message(token, SLACK_CHANNEL, plain_text, blocks)
        if result.get("ok"):
            print(f"✅ Message sent successfully! ts={result.get('ts')}")
        else:
            print(f"❌ Slack API error: {result.get('error')}")
            print(json.dumps(result, indent=2))
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP error: {e.code} {e.reason}")
        print(e.read().decode())
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
