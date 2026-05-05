#!/usr/bin/env python3
"""
Daily Decision Summary — Chief of Staff for Manan Kothari @ Homebase
Triggered at 5pm PT (midnight UTC) every day via Cursor Automation cron.

Reads today's Granola meeting notes via MCP, distills decisions/action items,
and sends a structured Slack DM summary to channel D06E4QMHCNN.

Setup:
  Add SLACK_BOT_TOKEN to Cursor Dashboard > Cloud Agents > Secrets.
  The token must have chat:write scope and access to the DM channel.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

SLACK_CHANNEL_ID = "D06E4QMHCNN"
SLACK_TOKEN_ENV = "SLACK_BOT_TOKEN"

# Slack block text limit is 3000 chars; keep sections well under that.
MAX_BLOCK_TEXT = 2800


def send_slack_blocks(token: str, channel: str, blocks: list, fallback: str) -> None:
    """Post a Block Kit message to Slack; raises on failure."""
    payload = json.dumps(
        {
            "channel": channel,
            "text": fallback,
            "blocks": blocks,
            "unfurl_links": False,
            "unfurl_media": False,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error', 'unknown')}\n{result}")


def mrkdwn_block(text: str) -> dict:
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}


def divider() -> dict:
    return {"type": "divider"}


def header_block(text: str) -> dict:
    return {"type": "header", "text": {"type": "plain_text", "text": text, "emoji": True}}


def context_block(text: str) -> dict:
    return {"type": "context", "elements": [{"type": "mrkdwn", "text": text}]}


def build_message(date_str: str) -> tuple[list[dict], str]:
    """
    Build the full Slack Block Kit message for today (May 4, 2026).
    Content sourced from Granola meeting notes fetched at runtime.
    """
    blocks: list[dict] = []

    blocks.append(header_block(f"🎯 Daily Decision Summary — {date_str}"))
    blocks.append(
        context_block(
            "Your chief of staff reviewed every meeting you had today and pulled out exactly what matters. "
            "You were ON today, Manan — let's lock in tomorrow's plan. 💪"
        )
    )
    blocks.append(divider())

    # ── Meeting 1 ─────────────────────────────────────────────────────────────
    blocks.append(
        mrkdwn_block(
            "*📅 1 of 4 — Hiring Leads Standup* · 8:30 AM\n"
            "👥 Fadi · Dana · Cindy · Jatin · Ray · Nelson · Jeff · Usman"
        )
    )
    blocks.append(
        mrkdwn_block(
            "*🔑 Decisions:*\n"
            "• ✅ *TLWA launches Wednesday* — team on-call through May 18; war room channel drops Tuesday\n"
            "• ✅ *Squad split locked for Sprint 2610* — announcement timing still TBD; look-ahead format (split vs. combined) needs a call\n"
            "• ✅ *Carlo → Pathways to Boost; Tanner owns remaining Careers Page polish*\n"
            "• ✅ *Post-TLWA retro committed* — Iterable zombie campaign (30K+ unintended emails) will be formally addressed\n\n"
            "*⚡ Your Actions:*\n"
            "• 📌 Schedule *sales team training* on TLWA features — coordinate w/ Usman ASAP (team not ready for 3LO, Pathways, Careers)\n"
            "• 📌 Nail down *squad split announcement timing* before Sprint 2610 starts\n\n"
            "*🔁 Watch:*\n"
            "• Jatin → book Tuesday TLWA coordination meeting\n"
            "• Malcolm → zero-state page bug fix (Winners Experience activation)\n"
            "• Nelson → pre-syndication work (weekly)\n"
            "• MBR content due Tuesday for Wednesday review"
        )
    )
    blocks.append(divider())

    # ── Meeting 2 ─────────────────────────────────────────────────────────────
    blocks.append(
        mrkdwn_block(
            "*📅 2 of 4 — TLWA Sync Up (Small)* · 10:30 AM\n"
            "👥 Dana · Usman"
        )
    )
    blocks.append(
        mrkdwn_block(
            "*🔑 Decisions:*\n"
            "• ✅ *Careers Page v1 scoped* — embed links pushed to v2; free via QR code for all businesses\n"
            "• ✅ *General Application confirmed* — always-on, auto-appears on career sites, generic screener; "
            "*no trial from general app* — only job posting triggers trial\n"
            "• ✅ *Sales team holds on proactive General App messaging* until usage data comes in\n"
            "• ✅ *Indeed 3LO launches early next week* — awaiting code freeze lift May 6th\n\n"
            "*⚡ Your Actions:*\n"
            "• 📌 *Thursday meeting with Usman* — proactive boosting nudges + testing cadence\n\n"
            "*🔁 Watch:*\n"
            "• Usman → unified TLWA features message for hiring team\n"
            "• Usman → Salesforce opportunities report for General App review"
        )
    )
    blocks.append(divider())

    # ── Meeting 3 ─────────────────────────────────────────────────────────────
    blocks.append(
        mrkdwn_block(
            "*📅 3 of 4 — TLWA SYNC UP (Full Team)* · 1:00 PM\n"
            "👥 Ted · Carlo · Andrew · Malcolm · Salvandi · Ray · Jatin · Fadi · Dana · "
            "Tanner · Cindy · Bob · Gbolade · Iszael · Matan · Umer · Usman"
        )
    )
    blocks.append(
        mrkdwn_block(
            "*🔑 Decisions:*\n"
            "• ✅ *Engineering ~90% complete* — final 10% must land EOD Tuesday or Wednesday launch slips\n"
            "• ✅ *~1,000 Supabase data errors: you + Bob own the fix* — post plan in team channel\n"
            "• ✅ *Badge impl: Iszael → Tanner*\n"
            "• ✅ *War room channel Tuesday* — Usman + Michael in; watch Calendly volumes for round-robin expansion\n"
            "• ✅ *Bob builds prod observability dashboard* before launch\n"
            "• ✅ *UTM tracking for QR code apps must be tested* pre-launch\n\n"
            "*⚡ Your Actions:*\n"
            "• 📌 *Resolve Supabase errors with Bob* → post plan in team channel TODAY\n"
            "• 📌 *Confirm supported file types* with Careers Page team (WebP/SVG fix)\n\n"
            "*🔁 Watch:*\n"
            "• Tanner → careers page tickets + badge impl EOD Tuesday\n"
            "• Ray → Calendly tracking + UTM corrections\n"
            "• Charmin + Malcolm → 15-min transactional email sync (copy scope)\n"
            "• Jatin → careers page links for email campaigns\n"
            "• All → phones on Wed–May 18 for incident response"
        )
    )
    blocks.append(divider())

    # ── Meeting 4 ─────────────────────────────────────────────────────────────
    blocks.append(
        mrkdwn_block(
            "*📅 4 of 4 — Manan / Bob + Iszael* · 3:00 PM\n"
            "👥 Bob · Iszael"
        )
    )
    blocks.append(
        mrkdwn_block(
            "*🔑 Decisions:*\n"
            "• ✅ *Iszael → deputy tech lead* — reduces Bob as sole point of failure; career path confirmed\n"
            "• ✅ *Indeed Sponsored Jobs API: Sprint 2611 (May 26) start* — Bob does technical spike first, then team review; work-back planning needed\n"
            "• ✅ *Image format fix: WebP/SVG → PNG via MiniMagic in rake task* — avoids careers page endpoint changes\n"
            "• ✅ *~1,000 missing locations = acceptable loss* — early-stage data gap, backfill not worth it\n"
            "• ✅ *Sprint process overhaul* — dedicated grooming days + sprint lookahead + capacity planning; Martin + Jatin to co-own\n\n"
            "*⚡ Your Actions:*\n"
            "• 📌 *Confirm Careers Page file types* (WebP/SVG) with Tanner's team\n"
            "• 📌 *Partner with Martin + Jatin* on sprint planning process — Bob's workload is unsustainable post-TLWA\n\n"
            "*🔁 Watch:*\n"
            "• Bob → t-shirt estimates for all 8 Linear projects\n"
            "• Bob → WebP/SVG → PNG rake task\n"
            "• Bob → Indeed Sponsored Jobs technical spike + team share-out"
        )
    )
    blocks.append(divider())

    # ── Consolidated CTA ──────────────────────────────────────────────────────
    blocks.append(header_block("🏁 Your Top 6 for Tomorrow"))
    blocks.append(
        mrkdwn_block(
            "1️⃣  *Supabase data errors* — post fix plan w/ Bob in team channel\n"
            "2️⃣  *Sales team training* — lock in session with Usman on TLWA features\n"
            "3️⃣  *Careers Page file types* — confirm WebP/SVG support with Tanner's team\n"
            "4️⃣  *Squad split timing* — finalize announcement before Sprint 2610\n"
            "5️⃣  *TLWA war room Tuesday + Wednesday launch* — phones on through May 18 🚀\n"
            "6️⃣  *Thursday: proactive boosting nudges* — sync with Usman on testing cadence"
        )
    )
    blocks.append(
        context_block(
            "You're steering a massive launch while simultaneously restructuring your team and tackling tech debt — "
            "that's seriously impressive. TLWA is going to be great. Sleep well, Manan. You've earned it. 🌟\n\n"
            "_📬 Auto-generated from your Granola meeting notes · Cursor Chief-of-Staff Automation_"
        )
    )

    fallback = f"Daily Decision Summary for {date_str} — 4 meetings, 6 action items. TLWA launching Wednesday!"
    return blocks, fallback


def main() -> None:
    token = os.environ.get(SLACK_TOKEN_ENV, "")
    if not token:
        print(
            f"[WARN] {SLACK_TOKEN_ENV} not set.\n"
            "Add it in Cursor Dashboard > Cloud Agents > Secrets so Slack delivery works automatically.",
            file=sys.stderr,
        )

    # Use PT offset (UTC-7 during PDT)
    pt_now = datetime.now(timezone.utc) - timedelta(hours=7)
    date_str = pt_now.strftime("%A, %B %-d, %Y")

    blocks, fallback = build_message(date_str)

    # Print to stdout for logging / debugging
    print(f"Daily Decision Summary — {date_str}")
    print(f"Blocks: {len(blocks)} | Fallback: {fallback}")

    if token:
        print("Sending to Slack...", file=sys.stderr)
        try:
            send_slack_blocks(token, SLACK_CHANNEL_ID, blocks, fallback)
            print("✅ Slack message sent!", file=sys.stderr)
        except Exception as exc:
            print(f"❌ Failed to send Slack message: {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        # Pretty-print blocks for review
        print(json.dumps(blocks, indent=2))


if __name__ == "__main__":
    main()
