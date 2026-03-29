#!/usr/bin/env python3
"""
Sunday Mar 29 evening chief-of-staff message.
No meetings today (Sunday) — hackathon kicks off TOMORROW (Mon Mar 30).
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Sunday Evening Brief — Mar 29 🏁",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! No meetings today (you deserve the rest 💪). "
                "But *tomorrow is Hackathon Day 1* — here's everything you need "
                "to walk in ready to go."
            ),
        },
    },
    {"type": "divider"},
    # --- HACKATHON TOMORROW ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 TOMORROW: Hackathon Kick-Off — Mon Mar 30*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "2-week full-team sprint. Your job today/tonight is to make sure "
                "all 4 project briefs are locked so the team can hit the ground running.\n\n"
                "*4 Projects (briefs need to be DONE before standup):*\n"
                "1. *Indeed OAuth (3LO)* — highest priority. Andrew owns the spike. "
                "Two entry points: _View Live Job Posts_ + _Boost with Indeed_. "
                "You still need to review spike + email Kenneth + add Ray.\n"
                "2. *Applicant Flow* — full team redesign. Brief + prototype was due EOD Wed Mar 25 — confirm status.\n"
                "3. *Deal Breakers + Match* — roadmap item #3.\n"
                "4. *(4th project)* — confirm with Jeff.\n\n"
                "*Your action before 9am:* Drop all 4 brief docs in the hackathon channel so nobody's blocked at standup."
            ),
        },
    },
    {"type": "divider"},
    # --- DECISIONS FROM LAST WEEK ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Key Decisions from Last Week (Mar 23–25)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*TLWA Hiring Activation (Mar 25)*\n"
                "✅ *Decision:* Option C confirmed — 4-step QR flow (scan → reveal → activate → next steps)\n"
                "✅ *Decision:* SMS/phone auth (not email) to prevent QR hijacking\n"
                "✅ *Decision:* Generic Team Member job post as default, 2032 expiry, auto-scheduling off\n"
                "✅ *Decision:* Build outside HB1 for speed; 50k unique QR codes\n"
                "✅ *Decision:* URL format: `app.jhb.com/tlwa/[unique-string]`\n"
                "✅ *Decision:* Top Local Workplace badge = DB flag for 2026 winners (Kvan PM)\n\n"
                "_Why it matters:_ Printer specs + QR URLs were due Friday. Confirm Ray/Jatin locked this before hackathon starts."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Smart PreSets — Careers Page (Mar 25)*\n"
                "✅ *Decision:* 4-tier preset framework (zero → category → specific → full scrape)\n"
                "✅ *Decision:* Logo as highest-ROI MVP element — middle ground between accuracy + wow factor\n"
                "✅ *Decision:* Smart placeholder UX (dotted-line, Dropbox pattern)\n\n"
                "_Why it matters:_ Manan + Jeff still need to finalize tier specs. Logo scraping tool needs Supabase connection (currently local only)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Indeed OAuth Strategy (Mar 24)*\n"
                "✅ *Decision:* 3LO (three-legged OAuth) required for sponsored jobs API\n"
                "✅ *Decision:* Two entry points — _View Live Job Posts_ + _Boost with Indeed_\n"
                "✅ *Decision:* Up to 5 redirect URIs to distinguish features\n"
                "⚠️ *Risk:* Indeed cutting organic reach aggressively (3rd partner this week to feel it)\n\n"
                "*JobGet (Mar 24):* Organic XML feed ready in ~30 min. Billy to send docs for standard + easy apply. Low-hanging fruit — don't let this slip."
            ),
        },
    },
    {"type": "divider"},
    # --- ACTION ITEMS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Your Personal Action Items (Carry-Forwards)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "🔴 *URGENT — Manan Boost SKU:* Email Chris (billing) to kick off SKU creation. "
                "Early May launch = billing needs 3-wk lead. You needed to start this last week.\n"
                "🔴 *Manual Mode green light:* Cindy's QA is done. This is on you to approve.\n"
                "🔴 *Andrew 3LO spike:* Review spike results + email Kenneth + add Ray to the thread.\n"
                "🟡 *Applicant flow brief + prototype:* Was due EOD Wed Mar 25. Is it done?\n"
                "🟡 *Hackathon brief docs (all 4 projects):* Must be ready before Mon standup.\n"
                "🟡 *Indeed integration email response:* Confirm you replied.\n"
                "🟢 *Smart PreSets logo scraping:* Integrate with Supabase (currently local only)."
            ),
        },
    },
    {"type": "divider"},
    # --- TEAM STATUS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👥 Team Owners Entering the Week*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Ray* — Friday deck, target segment, lifecycle/Salesforce\n"
                "• *Jatin* — URL routing, QR structure (TLWA)\n"
                "• *Fadi* — TLWA QR pres, post-QR UX flow, marketing insert content\n"
                "• *Cindy* — trial flow pres (waiting on your green light for Manual Mode)\n"
                "• *Matan* — zero-state/screener pres, lifecycle/Salesforce\n"
                "• *Dana* — ICP research, field testing\n"
                "• *Kvan* — Top Local Workplace PM\n"
                "• *Andrew* — Indeed 3LO spike"
            ),
        },
    },
    {"type": "divider"},
    # --- NORTH STARS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 North Stars (last known)*",
        },
    },
    {
        "type": "section",
        "fields": [
            {"type": "mrkdwn", "text": "*Paying Companies*\n~600 (target: 2,600 H1)"},
            {"type": "mrkdwn", "text": "*Weekly Trials*\n112 (target: ~1,000)"},
            {"type": "mrkdwn", "text": "*Monthly Retention*\n87% (target: 95%)"},
            {"type": "mrkdwn", "text": "*Segment*\nFood & Bev / Hospitality, 26+ emp, <5 locations"},
        ],
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_You've had a great week — TLWA alignment locked, hackathon scoped, "
                "JobGet partnership moving, and Smart PreSets strategy set. "
                "Now go crush the hackathon. You've got this. 💪_\n\n"
                "_— Your Chief of Staff_"
            ),
        },
    },
]

fallback = "Sunday Evening Brief — Mar 29 | Hackathon kicks off TOMORROW"


def send_slack_message(blocks: list, text: str) -> None:
    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("⚠️  SLACK_TOKEN not set — printing preview only.\n")
        print("=" * 70)
        print(text)
        print("=" * 70)
        for block in blocks:
            if block.get("type") == "section":
                t = block.get("text") or {}
                if t:
                    print(t.get("text", ""))
                fields = block.get("fields", [])
                for f in fields:
                    print(f.get("text", ""))
            elif block.get("type") == "header":
                print("\n### " + block["text"]["text"])
            elif block.get("type") == "divider":
                print("-" * 60)
        return

    payload = json.dumps({
        "channel": CHANNEL,
        "text": text,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✅  Message sent to {CHANNEL}")
            else:
                print(f"❌  Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌  Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    send_slack_message(blocks, fallback)
