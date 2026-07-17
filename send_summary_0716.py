#!/usr/bin/env python3
"""Daily Decision Digest — Thu Jul 16, 2026 (Manan Kothari, PM @ Homebase)"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN") or ""

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "🌆 Chief of Staff Daily Digest — Thu Jul 16, 2026", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Huge day — you crushed *3 key meetings* and made some really important decisions around match quality, sprint planning, and the team's process. Here's everything you need to know, crisp and clear. Let's go! 💪"
        }
    },
    {"type": "divider"},

    # ── MILESTONE CALLOUT ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🏆 *BIG MILESTONE: Homebase just broke 800K accounts!* From 700K→800K in only ~5 weeks (vs 14 weeks for the prior 100K). That acceleration is real and you should feel great about it."
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 — Hiring Leads Standup* | 8:45 AM PDT\n_with Ray, Dana, Matan, Jatin, Fadi, Nelson, Jeff, Usman_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*1. New Engineering PR Directive — Ray escalating*\nAndrea/Andrew issued new guidelines (not consulted with EMs): all PRs now require staff+ engineer review; backend restricted to admin/delete-only. Ray believes the team is being interpreted too literally — nothing you do is high-risk. He's pushing Andre to raise this with Martin + Jatin from curiosity, not confrontation. His advice: keep all work in flight, don't uninstall tools.\n_Rationale: Blocking this kind of gatekeeping before it slows the sprint is the right call._\n\n*2. Expired Job Link Fix — Scoped for Next Sprint*\nCustomer QR codes hitting expired jobs show a sign-in error page. Two paths identified: (a) redirect to careers page, or (b) 'job closed' screen with general application link. Complication: not all V2 locations have general application enabled. Ray wants you to define a graceful experience for every scenario (expired job, no open roles).\n_Rationale: Broken applicant experience is a trust killer — fixing this is the right default._\n\n*3. 800K Accounts Milestone* ✅\nTeam crossed 800K active accounts. Acceleration is real (not just V1→V2 migration). $30 plan removal + organic trial growth is working."
        }
    },
    {"type": "divider"},

    # ── MEETING 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 2 — Hiring Applicants: EPD Leads Sync & Prep* | 9:00 AM PDT\n_with Jatin, Fadi_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*4. Next Sprint Locked — 6 Projects*\nSmaller sprint by design: Indeed account setup, salary recommendations, closed job improvements, renewed jobs (no design needed), closed job fallback (needs Fadi design), + one more. Good scope — lean and executable.\n\n*5. EPD Leads Meeting → Moves to Thursday Afternoon*\nCurrent Monday/Tuesday timing means capacity clarity comes too late for Jatin to prep properly. New format: Thursday afternoon, back-to-back with Dana's session. Manan joins start, Dana joins end, ~75 min total. Trial next week.\n_Rationale: Front-loading the capacity read means you can go into look-ahead with real answers, not guesses._\n\n*6. Renewed Jobs: Email Copy Update Needed (No Design)*\nWhen a job is renewed, expiry updates +30 days + triggers email warning. Current email warns 3 days before expiry but has no renewal CTA. Quick copy fix only — Jatin flagged, no design needed.\n\n*7. Closed Job Fallback — Fadi to Design*\nApplicant landing on a closed job currently hits an error page. Likely fix: 'job closed' screen with 'view careers page' button. Fadi needs a task tagged to him with 'design required.'\n\n*8. Definition of Ready Template — Updated Roles*\nFadi stops writing product briefs. Product and design are now separate, distinct inputs on the handoff template. Dana now owns the brief that Fadi was historically writing (escalated to Jen + Cindy, resolved).\n_Rationale: Clean role boundaries = better handoffs, less friction, happier Fadi._\n\n*9. Weekly Priorities Sync — Ray + Dana + Manan*\nPriority alignment for the core/applicant flow side is still missing. A standing sync needs to be set up so you have a shared ranked list before each EPD leads meeting.\n\n*10. Zero State Page — John's Direction: No Product Screenshots*\nJohn explicitly prefers the version of the zero state page without product screenshots ('leave them in the product'). That's the direction.\n\n*11. Landing Page Animation — Prompt Box Concept Locked*\nUser types 'I hire a line cook' → converts to a chip → fills in next field automatically. Wants to pull neighborhood from Google Places (hyper-local: 'line cooks in Kensington Market'). Two CTAs are visually cluttered — one needs to become secondary. Dana asked to explore address scraping."
        }
    },
    {"type": "divider"},

    # ── MEETING 3 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 3 — Applied AI Jamming: Hiring Core* | 11:30 AM PDT\n_with Fadi, Divij, Dana, Ted, Jatin_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*12. North Star Metric Locked — 'Move Forward Rate'*\nYou are optimizing for OEM intent-to-interview (OEM sends booking link OR accepts a candidate-requested interview), NOT raw interview attendance. This is a cleaner signal of actual hiring intent.\n_Rationale: Raw attendance is noisy. Move forward = OEM has made a real decision. Much better signal._\n\n*13. Two-Metric Funnel Agreed*\n(1) % of top matches moved to interview → (2) % of those hired. Guardrail: % of non-matches who also get moved forward (should shrink as match quality improves). Clean, measurable, actionable.\n\n*14. Roster Addition as Hiring Proxy*\nIf a top match appears on the employer's team roster within X days → treat it as a hire. Clever workaround for the absence of formal 'hired' signals in the product.\n\n*15. Divij's Combined-Score Chart Dropped*\nThe simulation chart using simple averaging of resume + screener scores is NOT representative of actual AND-gate logic in the product. Dropped to avoid misleading the team. Divij will re-pull with real data and the agreed funnel.\n_Rationale: Bad data visualizations drive wrong product decisions. Good call catching this early._\n\n*16. Near-Term Approach: Update Thresholds + Learn*\nUpdate match definition thresholds to properly incorporate both resume AND screener scores (not simple averaging, actual gating). Learn from OEM behavior. Iterate. Screener redesign (dynamic, resume-pulling) is deferred — Pandora's box for now.\n\n*17. Smarter Score Combination Worth Exploring*\nBefore combining signals, proper gating logic (not addition) should be explored. Flagged as a near-term investigation before the next model update."
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Your Action Items — Prioritized*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 P0 — Do These Today / First Thing Tomorrow:*\n\n• *Sync with Dana on 'move forward' edge cases* — nail down: hired-without-interview-record scenario, booking link flow vs. candidate-requested flow. This unblocks Divij's data re-pull. _(Applied AI Jamming)_\n• *Create Fadi design task for closed job fallback* — tag with 'design required', include the two options (redirect vs. closed screen + CTA). _(EPD Leads Sync)_\n• *Reschedule EPD leads sync → Thursday afternoon* (back-to-back with Dana's session). Trial next week. _(EPD Leads Sync)_\n• *Message Paul directly on role rec DP progress* — different voice = different urgency. Still P0. _(Carried from Jul 15)_\n• *Assess WTP for $100/interview Instawork pricing* — 2-3 line cook hirers. Momentum is hot. _(Carried from Jul 15)_\n• *Approve Ugu's backend PR* — unblocks OEM setup call prompts. Still pending. _(Carried from Jul 15)_\n• *Carlo Harness/OpenSpec — NOW 6 DAYS OVERDUE* from Jul 10 deadline. Escalate. Now. _(Carried from Jul 15)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟡 P1 — This Week:*\n\n• *Update roadmap to cover sprint-after-next* — needs to be ready before the rescheduled Thursday EPD leads session. _(EPD Leads Sync)_\n• *Set up weekly priorities sync with Ray + Dana* — needed before each EPD leads meeting. Put it on the calendar. _(EPD Leads Sync)_\n• *Define graceful expired job experience* — all scenarios: expired job, no open roles, no general application enabled. Scope for next sprint. _(Hiring Leads Standup)_\n• *Monitor Ray's escalation on new eng directive* — make sure it doesn't bottleneck your sprint. Keep an eye out for resolution. _(Hiring Leads Standup)_\n• *Friday pairing session with Rami* — bring JD evaluation criteria, Rami brings sample JD outputs. Don't miss this. _(Carried from Jul 15)_\n• *Confirm Culinary Agents pricing outcome* from Ray's noon call Jul 15. _(Carried from Jul 15)_\n• *Reconnect with Ashwin (Instawork)* once WTP read is done. _(Carried from Jul 15)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟢 P2 — On the Radar:*\n\n• Talent pool sprint (2-4 weeks after salary+role recs ship)\n• Abby ownership area — needs clarity ASAP (Week 2)\n• Dana succession planning (~10 weeks remain, not started)\n• Boost purchase bug — still no owner, revenue-impacting\n• Chase job page opt-ins assignment with Carlo (Jatin flagged)"
        }
    },
    {"type": "divider"},

    # ── WATCH LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👀 Watch List*\n\n• *V1→V2 Cutover (Jul 20 — 4 days out):* Dana investigating 200+ unexpected trial spike. Monitor screener gap + star/fav gap post-cutover.\n• *Carlo Harness/OpenSpec:* 6 DAYS OVERDUE — status unconfirmed. NEEDS IMMEDIATE ACTION.\n• *Salary Recs:* Izzy starting, Rami handing off context. Friday pairing session = your next touchpoint.\n• *Match Quality / AI Jamming:* Divij re-pulling data with agreed funnel + real AND logic. Next step after Dana sync.\n• *Instawork:* Fresh $100/interview opportunity. WTP research = unlock.\n• *SEO:* 66K pages live, 15.5K indexed — big organic gap. Carlo + Google Search Console data in hand.\n• *Abby (Week 2):* Still needs a clear ownership area. Don't let this slip into Week 3.\n• *Dana leaving end of September:* Succession planning clock is ticking (~10 weeks)."
        }
    },
    {"type": "divider"},

    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Summary:* Today was a thoughtful, high-signal day. You locked in the match quality metric that will anchor the AI hiring features for the next sprint cycle — that 'move forward rate' decision alone saves weeks of future debate. The process improvements (EPD leads timing, Definition of Ready) are exactly the kind of operating system upgrades that compound over time. And the 800K milestone? That's a testament to the platform momentum you've been building. 🚀\n\n_Your chief of staff, signing off at 5pm PDT. See you tomorrow._"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest — Thu Jul 16, 2026 | 17 Decisions | Action Items Inside",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("=" * 70 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("CHIEF OF STAFF DIGEST — Thu Jul 16, 2026\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("=" * 70 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"Channel: {CHANNEL}\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"Meetings covered: 3 (Hiring Leads Standup, EPD Leads Sync, Applied AI Jamming)\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"Decisions documented: 17\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(f"P0 action items: 7\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("=" * 70 + "\n\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("─" * 70 + "\n").encode("utf-8", errors="replace"))

if not TOKEN:
    print("⚠️  No Slack token found. Set SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN.")
    print("   Add it in Cursor Dashboard → Cloud Agents → Secrets")
    print()
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"✅ Digest sent to {CHANNEL} — ts={result.get('ts')}")
    else:
        print(f"❌ Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"❌ Network error: {e}")
    sys.exit(1)
