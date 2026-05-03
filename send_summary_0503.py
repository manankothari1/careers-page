#!/usr/bin/env python3
"""Daily chief-of-staff summary — Sunday May 3, 2026 (TLWA Launch Eve)"""
import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🚀 Chief of Staff — Sunday May 3 | TLWA LAUNCHES TOMORROW",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Happy Sunday, Manan! No meetings today — which is exactly right. You've been building toward this moment for months, and *tomorrow is the day*. 800,000 users wake up to a brand new careers page. Here's your launch-eve war room recap + everything you need to walk into Monday with total confidence. Let's GO. 🔥"
        }
    },
    {"type": "divider"},

    # ── SECTION 1: TLWA LAUNCH CHECKLIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 TLWA LAUNCH CHECKLIST — Mon May 4, 9am ET*\n_800k users. 55k locations. This is the moment._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Must be GREEN before 9am ET tomorrow:*\n"
                "• ✅ Careers page deployed (new image fixes, styling, logo, colors — live as of May 1)\n"
                "• ⚠️  *V1→V2 migration* (Ugo) — confirm it crossed the finish line by EOD Friday\n"
                "• ⚠️  *20% traffic error routing* — career page V1/V2 experiment logic bug found Fri; confirm fixed\n"
                "• ⚠️  *iOS safe area CSS* (Gbolade/Izzy) — white background on address bars = ship blocker\n"
                "• ⚠️  *Company presets 30K* (Bob/Izzy) — confirm completed before midnight Sunday\n"
                "• ⚠️  *TLWA award display component* — must be deployed to prod before midnight Sunday\n"
                "• ⚠️  *Company list freeze* — 55,696 vs 54,000 discrepancy; freeze must be confirmed\n"
                "• ✅ Email OTP working; phone OTP tested (Fadi staging conflict resolved?)\n"
                "• ✅ QR code stickers printed; ~3k unmailable (Cassy confirmed)\n"
                "• ⚠️  *Indeed redirect URL* (Tanner/3LO) — Ray escalating to Gustavo; confirm status\n"
                "• ⚠️  *Malcolm OTP sad path brief* — did you send this before he starts Monday?\n"
                "• ⚠️  *TLWA brief to Ted* — 20+ DAYS OVERDUE. If not sent Friday night, send NOW."
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 2: MAY 1 DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 DECISIONS FROM YOUR LAST MEETINGS (May 1)*"
        }
    },

    # Hiring Leads Standup
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1️⃣  Hiring Leads Standup — Tight Sprint Model Locked*\n"
                "• *Decision:* 'Tight sprints' begin Sprint 2610 — every ticket fully defined BEFORE the cycle starts. Engineering will push back on undefined work; if not ready by sprint start, it doesn't go in.\n"
                "• *Why:* Worst DX scores on record. Engineers burning out and at least one is planning to quit. This is the fix, not a nice-to-have.\n"
                "• *Decision:* Two-squad structure — Dana leads morning sessions, you lead afternoon (West Coast timing). Each PM is the sole gatekeeper for squad priorities. No more single-backlog fights.\n"
                "• *Decision:* Retro next week — everyone brings 2-3 specific examples of scope/process failures. Walk through together to build shared norms.\n"
                "• *Action → You:* Get prototypes + designs + empty states + happy states docs done for 2610 tickets by Monday/Tuesday. Engineering gets Mon/Tue for planning, Wed onward is heads-down.\n"
                "• *Action → Martin/Jatin:* Available for real-time escalation when engineers ask scope questions post-Tuesday."
            )
        }
    },

    # Manan/Dana 1:1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2️⃣  Manan / Dana 1:1 — Screener Data + Flight Risks*\n"
                "• *Decision:* Chat may outperform video for screener start rates. Current screener: 90% completion for those who start, but only 30-40% start (60% drop-off from landing page). Chat is the lever to pull.\n"
                "• *Decision:* Career page V1/V2 experiment logic is routing 20% of traffic to error page — this is a *launch blocker* that must be resolved before Monday 9am.\n"
                "• *Insight:* Dana assigned John Blackwell as mentor (initiated by Ankit/Martin over Ray management concerns). Blackwell's advice: focus on big vision, not Ray's tactical asks. Take note.\n"
                "• *Risk flagged:* Bob and Dividge are flight risks. Address both proactively in Sprint 2610 — give them meaningful, exciting work.\n"
                "• *Decision:* Dana needs a senior designer, not an entry-level mentoring relationship. Prioritize this hire.\n"
                "• *Action → You:* Push the brainstorming doc to Ray tonight (it was on your list). Confirm career page error routing bug is squashed."
            )
        }
    },

    # Cindy/Manan - Predicted Roles
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3️⃣  Cindy / Manan — Predicted Roles Design Locked*\n"
                "• *Decision:* Mobile preview = fixed device height (not responsive). Avoids double-scroll; empty states maintain height with blank space. ✅ Cindy question from last week is resolved.\n"
                "• *Decision:* Predicted Roles goes under 'Jobs' section on dashboard (not a to-do item). Disappears after first job post.\n"
                "• *Decision:* Access gated to TLWA participants OR drive-off-the-lot experiment participants only. Must bypass zero-state page.\n"
                "• *Decision:* Careers page version of Predicted Roles = separate experience; requires company syndication; dotted line treatment = draft status. NOT promotional — actual job listings.\n"
                "• *Decision:* Need pre-syndication automation — auto-approve low-risk companies in first week based on HB usage signals (scheduling/time clocks/payroll). Current manual process creates delays.\n"
                "• *Decision:* Growth team's Indeed scraping approach is wrong — creates duplicate postings. Better path = OAuth login to claim/port existing Indeed jobs. Test with fake door first.\n"
                "• *Decision:* Senior designer interviews this week were disappointing (candidates underprepared; interns had better portfolios). Technical assessment: design critique + AI project showcase + collaboration questions. Interviews start next week with Meg.\n"
                "• *Action → You:* Finalize predicted roles designs + ticket requirements by Monday/Tuesday."
            )
        }
    },

    # Manan/Ray 1:1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4️⃣  Manan / Ray — Sprint 2610 + Marketplace Vision*\n"
                "• *Decision:* Sprint 2610 scope LOCKED — 4 deliverables:\n"
                "  1. *Purchase Boost* — Askew integration + Talroo campaign separation + CPC $35→$50\n"
                "  2. *Predicted Roles* — trial start optimization\n"
                "  3. *JobGet Easy Apply + 30-day paid experiment* — queue priority gating\n"
                "  4. *Sponsored Jobs API kickoff* — high-impact marketplace capability\n"
                "• *Decision:* 3 marketplace hypotheses locked for rest of year: (1) make spending obvious + easy for customers, (2) drive applicant flow through marketplace, (3) enable hiring specialists to intervene for job health.\n"
                "• *Decision:* 'Home Blast' concept — proactive employer outreach to vetted candidate database. Guardrails: 10 candidates max/blast, auto-interview acceptance. Pricing: 'Boost and Blast.' Revenue model attached.\n"
                "• *Decision:* Roadmap doc to be built using Granola transcript + Claude (you + Ray agreed on this format).\n"
                "• *Decision:* In-person strategy session in SF office post-Small Business Week. Focus: growth campaign around careers page, top local workplaces learnings.\n"
                "• *Risk flagged (serious):* Engineering morale at crisis level — worst DX scores ever, Fadi and Dana showing burnout signs. Two-team structure is the immediate response but you need to watch this closely.\n"
                "• *Action → You:* Finalize 2610 sprint scope doc by Monday/Tuesday. Build roadmap via Granola + Claude. Schedule SF in-person.\n"
                "• *Action → Ray:* MBR presentation prep for executive team."
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 3: TONIGHT'S FIRE LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 TONIGHT'S TO-DO LIST (before you sleep)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "1. *Send TLWA brief to Ted* — 20+ days overdue. Do it right now if you haven't.\n"
                "2. *Confirm V1→V2 with Ugo* — did it ship Friday? Prod check.\n"
                "3. *Confirm 20% error routing bug is fixed* — critical launch blocker found in careers page.\n"
                "4. *Confirm 30K presets* with Bob/Izzy — needs to be done before midnight.\n"
                "5. *Confirm TLWA award display component* deployed to prod.\n"
                "6. *Push brainstorming doc PR* to Ray (he's been waiting).\n"
                "7. *Brief Malcolm on OTP sad path scope* if not done — he starts tomorrow.\n"
                "8. *Send Saja (Talroo) CPA categories* — this has been on the list for days.\n"
                "9. *Check Indeed redirect URL status* — was Ray able to reach Gustavo?\n"
                "10. *Confirm company list freeze* — 55,696 vs 54,000 discrepancy must be resolved."
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 4: MONDAY BATTLE PLAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚔️  MONDAY MAY 4 BATTLE PLAN*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9am ET — TLWA GOES LIVE.* 800k users. 55k locations. Be at your desk early.\n\n"
                "• *Monitor:* DataDog + Sentry for launch-day anomalies (Bob owns). Watch careers page error rates.\n"
                "• *Careers page:* Remaining polish ships Monday (mobile fixes: hex input, banner pencil icon, logo fit, carousel, purple affordances, address links).\n"
                "• *Boost Pathways:* Carlo returns from careers page → dev starts Monday/Tuesday. Protect May 11 launch.\n"
                "• *Agentic era:* Tool definitions DUE (were they submitted Friday?). Jatin's agentic demo.\n"
                "• *Hiring team:* HB Assistant tool definitions — confirm submitted.\n"
                "• *Sprint 2610 planning:* Mon/Tue — your ticket definitions need to be ironclad before engineers start Wednesday.\n"
                "• *Predicted roles:* Finalize designs + requirements with Cindy → ready for 2610.\n"
                "• *Vibe pilot:* Follow up with Fadi re: Slack app approval from Joseph (10 HB pilot users).\n"
                "• *Matan:* Post Boost plan to #leads + survey customers on hiring spend (overdue since Apr 23).\n"
                "• *Indeed ATS survey:* Should arrive this week — respond immediately.\n"
                "• *Tight sprint comms:* After TLWA stabilizes, communicate the new sprint model to the team as a *gift*, not a correction."
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 5: WEEK AHEAD ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 WEEK OF MAY 4 — KEY MILESTONES*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Mon May 4:* TLWA launches 9am ET | Sprint 2610 planning begins | Agentic era Day 1\n"
                "• *~Tue May 5:* Juan risk logic review | Auto-syndication watch-and-wait window closes\n"
                "• *Wed May 7:* Boost Pathways QA ready (Carlo)\n"
                "• *Thu May 8:* Tight sprints retro (bring 2-3 specific examples)\n"
                "• *~May 10:* In-person SF strategy session (post-Small Business Week)\n"
                "• *May 11:* Boost Pathways launches (TLWA marketing launch)\n"
                "• *May 22:* Customer Connection Challenge winner announced at Show & Tell"
            )
        }
    },
    {"type": "divider"},

    # ── OVERDUE ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*⏰ OVERDUE — CARRY INTO NEXT WEEK*\n"
                "• *Nelson:* metro_area + bucketed_role + matching_roles — overdue since *Apr 8* 🚨\n"
                "• *Matan:* Boost plan to #leads + customer hiring spend survey — overdue *Apr 23* 🚨\n"
                "• *Greenlight Manual Mode:* Cindy QA done, on you to decide\n"
                "• *Boost modal copy:* Inconsistent across 3 states — fix ASAP\n"
                "• *Linear agent:* Configure to pipe comments to hiring channel\n"
                "• *IBK:* Logo max width/height specs\n"
                "• *Matan + Kayla:* Full email journey map (unblocks all future email launches)\n"
                "• *JobGet:* Set budget, confirm 30-day test with Peter Lee + Dan\n"
                "• *Cassy (printer):* Confirm mailable address count (~3k flagged)"
            )
        }
    },
    {"type": "divider"},

    # ── CLOSER ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*You've got this, Manan.* 🙌\n\n"
                "You and the team have been grinding toward TLWA for months. The careers page is live and beautiful. "
                "The sprint model is being fixed. The marketplace vision is crystallizing. "
                "Tomorrow morning, 800,000 people wake up to something you built.\n\n"
                "_Now go knock out that Ted brief, check those blockers, and get some rest. "
                "Big day tomorrow. I'll be back at 5pm PT with your post-launch decision summary. 💪_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "🚀 Chief of Staff — Sunday May 3 | TLWA LAUNCHES TOMORROW — daily decision summary + launch-eve battle plan",
    "blocks": blocks,
    "unfurl_links": False,
    "unfurl_media": False
}


def preview():
    print("=" * 70)
    print("CHIEF OF STAFF SUMMARY — May 3, 2026 (TLWA LAUNCH EVE)")
    print("=" * 70)
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            print("-" * 70)
    print("=" * 70)


def send():
    if not SLACK_TOKEN:
        print("SLACK_TOKEN not set — printing preview only.")
        preview()
        return

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_TOKEN}"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✅ Slack message sent successfully! ts={body.get('ts')}")
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                preview()
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        preview()
        sys.exit(1)


if __name__ == "__main__":
    send()
