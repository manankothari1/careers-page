#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Monday Aug 17, 2026
Granola meetings: Thu Aug 14 (Sprint Show & Tell + Fadi/Manan 1:1)
Cron: 0 0 * * * UTC = 5pm PDT Sunday evening -> Monday morning readout
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN") or ""

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Good morning Manan! Your Monday Briefing — Aug 17",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Big week ahead. You had two key meetings on Thursday that surfaced a genuinely important strategic signal "
                "about your conversion funnel — and Fadi is pushing hard on something you've been advocating since January. "
                "Let's make sure Monday sets the right momentum. Here's everything you need."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 1: SPRINT SHOW & TELL ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Thu Aug 14 — Sprint Show & Tell (11:00am PDT)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Insight: Trial Health → Paid Conversion is declining*\n"
                "You presented trial health-to-paid conversion data across 6 months. "
                "The headline: healthy trial conversion was *37–39% in Jan–Feb* but has dropped significantly since. "
                "The key ratio still holds (healthy trials convert ~2x vs medium trials), but the floor across all tiers is falling.\n\n"
                "*Decision:* Timing points squarely at the *$30 starter plan deprecation (removed May 29 via Sohil's Starter Plan Cleanup ticket)* "
                "as the primary driver — removing the low-cost entry point collapsed a segment that was converting. "
                "This is still being validated (not shared broadly yet). Manual mode timeline (Apr–May) is also in the frame.\n\n"
                "*Why this matters:* You now have two levers to investigate — the plan removal and the free tier generosity. "
                "Understanding which drove the drop shapes your entire monetization strategy for Q4."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Company highlights from Show & Tell:*\n"
                "• *SecOps Agent (Khrystyna)*: 99% of critical/high alerts auto-investigated, avg response <3 min, *60 eng hours saved/month*, 30% of alerts handled overnight/weekends with zero on-call pages. Architecture: Slack → orchestrator → MCP sub-agents (SIEM, Datadog). Roadmap: expand to payroll, hiring, CS.\n"
                "• *Time Card Assistant*: Live to 100+ customers on iOS + Android. Bulk action side panel replaces per-card resolution. Page templates rolling out this week.\n"
                "• *Gabriel's PM Assistant*: Slack-native side project (nights/weekends, zero budget) answering natural language questions against the codebase (30K files), Databricks, Linear, Confluence, and *Granola*. Live in Slack via Runlayer. Self-improving via thumbs-up/down. Rolling out carefully to CX managers.\n"
                "• *Marketing — Podcast/Streaming*: 7.9M impressions, 1,300 signups on CPA buy. Female voice outperforming (58%). Streaming 3x better than podcasts. Top category: politics/news + true crime."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 2: FADI / MANAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Thu Aug 14 — Fadi / Manan 1:1 (11:37am PDT)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*DECISION: Manual mode = conversion rate drop — hypothesis confirmed*\n"
                "Manual mode launched Apr 8–13 and was made permanent default May 20. "
                "The correlation with the conversion rate decline is direct and clear. "
                "You and Fadi aligned on this being the root mechanism.\n\n"
                "*DECISION: Both reads are simultaneously true*\n"
                "Fadi's read: paid features (screener, matching) aren't compelling enough to upgrade. "
                "Your read: too much value given away for free. "
                "These aren't competing — they're both correct at the same time, and that's the real problem."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*DECISION: Talent Pool = the strategic answer to both problems simultaneously*\n"
                "Talent pool adds applicants (solving the free-tier gap) AND creates exclusive paid value (solving differentiation). "
                "'All roads lead to the talent pool.' You've been advocating this since January.\n\n"
                "*Fadi floated going all-in:* Pull 1–2 engineers, stop everything else, try to crack it by year-end. "
                "This is a real conversation you need to have with Ray (and Sky once he starts Aug 25). "
                "You are in the best position to drive this — stake your position now before Sky arrives."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*DECISION: Trial flow model is broken — needs recalculation*\n"
                "The 11% MoM growth rate used in the trial flow model is a single-month data point (June→July). "
                "That's not a reliable baseline. You identified the flaw. Fix: use the L3 average MoM growth rate.\n\n"
                "*Free tier options under discussion (not yet decided):*\n"
                "• Limit job posts (e.g. one per month on free)\n"
                "• Remove AI JD generation from free tier\n"
                "• Cap applicant volume on free tier\n"
                "Core principle locked: either make paid features more compelling, or restrict free access."
            )
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Your Action Items — In Priority Order*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*TODAY (Mon Aug 17):*\n"
                "1. *Review Resume Insights designs from Fadi* — due today (multi-page scrolling is the main open issue; live jobs flow + states). Fadi blocked on you. Unblock this morning.\n"
                "2. *Recalculate trial flow model using L3 average MoM growth rate* — you flagged the flaw on Thursday, now fix it. This is fast.\n"
                "3. *Confirm New GM of Hiring start date* — 18th vs 25th. Ray to confirm. If it's today, you need to know ASAP.\n"
                "4. *Write/advance Sky onboarding doc (Talent Pool strategy)* — Sky targets Aug 25. Less than 2 weeks. The doc is your stake in the ground before he arrives.\n"
                "5. *Loop Ray into manual mode/conversion analysis* — you and Fadi agreed on this Thursday. Do it before the week fills up.\n\n"
                "*THIS WEEK:*\n"
                "• *Sprint 18 Retro — Tue Aug 18, 1–2pm ET* (Jatin scheduling). Team needs to buy in on the new Sprint cadence (Tue look-ahead, Wed breakdown, Thu heads-down, Fri locked) before it goes live.\n"
                "• *422 errors RCA — Day 37+* — where is Jatin on this? This is a 33-day-old critical issue with 146 affected locations. Push for an update.\n"
                "• *Talent Pool designs from Fadi* — ADD to Linear with prototype link. Engineers are blocked. Izzy is waiting for front-end spec.\n"
                "• *Amplitude dashboard to Matan* — overdue since Aug 6. Send it.\n"
                "• *ICP nudge experiment results from Myan* — push for sharing with the team (currently opaque).\n"
                "• *Fadi Boost modal Figma* — overdue, Fadi is blocked on you. Unblock ASAP.\n"
                "• *Sales reps time* — schedule direct time with reps (mirror Ray/Claire approach). Don't let this slip another week.\n"
                "• *Indeed follow-up (Catherine)* — feed was resubmitted Aug 12 for re-review. Chase for clearance status."
            )
        }
    },
    {"type": "divider"},

    # ── MONDAY BATTLE PLAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:crossed_swords: Monday Battle Plan*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "The big strategic narrative coming out of Thursday is this: *you now have a causal hypothesis for the conversion drop* "
                "(manual mode generosity + starter plan removal), *and* you have a strategic answer (Talent Pool) that Fadi is *also* now excited about. "
                "That alignment is rare and valuable — use it.\n\n"
                "Sky arrives in ~8 days. The talent pool doc you write this week isn't just an onboarding artifact — it's your product vision. "
                "Write it with conviction. Fadi wants to go all-in. Ray is transitioning out. You are the PM who has been pushing this since January. "
                "This is your moment to consolidate ownership.\n\n"
                "*Morning:* Fadi 1:1 → unblock Resume Insights + confirm Talent Pool designs in Linear\n"
                "*Midday:* L3 trial model recalculation + GM start date confirmation\n"
                "*Afternoon:* Sky doc (Talent Pool strategy) → stake your position before he arrives\n"
                "*EOD:* Loop Ray into conversion analysis; send Amplitude dashboard to Matan"
            )
        }
    },
    {"type": "divider"},

    # ── WATCH LIST PULSE ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: Watch List Pulse*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Culinary Agents*: GO-LIVE was Aug 12 (27 line cook jobs at $69/job). Check applicant flow numbers today — first real signal on whether this paid channel works.\n"
                "• *Indeed feed*: Resubmitted Aug 12 for re-review. Chase Catherine for clearance update.\n"
                "• *Carlo Ferrer*: Back from bereavement Aug 13 but out again next week. Indeed 3LO + Talent Pool are his. Make sure Jatin has a plan.\n"
                "• *Tanner Hartwig*: Behind on Indeed account setup. Unknown blocker. Chase today.\n"
                "• *JD A/B experiment (IBK)*: Running since week of Aug 10. You have ~5 days of data now. Check for early signal. IBK is flagged as too passive — this week is a good moment to pull him in directly.\n"
                "• *Careers page outreach*: 65% open / 12% CTR on 30-40 manually built pages. Decide: scale this into a formal experiment?\n"
                "• *Zero state page experiment*: Pause before killing — numbers (23 vs 15) look suspicious for 1 month of data. Re-check date range + compare vs OG baseline.\n"
                "• *Matan PMM roadmap*: ~1+ week overdue. Follow up.\n"
                "• *Abby (new PM, week 10)*: Needs clear ownership area. Don't let this drag into another week."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_You're in a great position, Manan. The hypothesis is coming together, your key designer is aligned, "
                "and you have a clear north star. Go make it happen. :muscle:_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Monday Aug 17 Chief of Staff Briefing — decisions, actions, and battle plan inside."
}


def preview():
    sys.stdout.buffer.write(b"\n=== SLACK PREVIEW (no token) ===\n")
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("## " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n")


def send_slack(token: str, payload: dict) -> bool:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
                return True
            else:
                print(f"[ERROR] Slack API: {result.get('error', 'unknown')}")
                return False
    except urllib.error.URLError as e:
        print(f"[ERROR] Network: {e}")
        return False


if not TOKEN:
    preview()
    print("[INFO] No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN).")
    print("[INFO] Add the token as a secret in Cursor Dashboard > Cloud Agents > Secrets.")
    sys.exit(0)

success = send_slack(TOKEN, payload)
sys.exit(0 if success else 1)
