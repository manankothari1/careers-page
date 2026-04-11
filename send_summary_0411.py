#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari — Sat Apr 12, 2026 (covering Fri Apr 10 meetings)."""
import json, os, urllib.request, urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌟 Your Friday Debrief — April 10, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Incredible Friday — 3 meetings, a bunch of real decisions locked in, and the team is *firing on all cylinders* heading into what's shaping up to be a massive launch week. Here's everything you decided today + what needs to happen next 👇"
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 of 3 — Hiring Leads Standup* (8:30 AM)\n_With: Fadi, Dana, Matan, Cindy, Jatin, Ray, Nelson, Jeff_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*1️⃣ Show & Tell format stays — but optimize it*\n> You pushed for transforming S&T from a \"summarization\" session into a *discussion forum.* The decision: keep the meeting (Ray's right that it's the only time engineering + sales see business metrics together), but today you'll directly ask the audience *what content is most valuable to them.* You also agreed to make more time for Q&A.\n> _Rationale: 30-person all-company forums are rare and valuable. The problem isn't the meeting — it's the format._\n\n*2️⃣ Meeting attendance = your call, not guilt*\n> You made a clear call: skip any meeting where you're not contributing or getting value — *with the exception of Dana* (who must attend). You also named the daily standup as a real source of meeting fatigue — it's been running over 15 min too often.\n> _Rationale: Agency over your calendar = more output. Meeting fatigue is a real tax on the team._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• [ ] *You @ Show & Tell today* — ask the audience: \"What's most valuable for us to share with you?\" Keep your own segment brief\n• [ ] *Daily standup fix* — enforce the 15-min cap starting Monday; agenda-based items only, no freeform overruns\n• [ ] *Dana* — you called her out as the exception who must attend; confirm she knows that's the expectation going forward"
        }
    },
    {"type": "divider"},

    # ── MEETING 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 2 of 3 — Hiring Team Check-in* (1:00 PM)\n_With: Full hiring squad (26 people) including new hire Matan Chen Zion_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Made:*\n\n*3️⃣ Taru XML feed — remove CPC caps + business-type filter → ~300 → ~1,100 active jobs*\n> You confirmed this change shipped this week. Jobs that were previously excluded (no business type OR high CPC) are now being sent to Taru. This is a direct lever on applicant flow for unhealthy jobs.\n> _Rationale: Taru = $2/applicant vs $15-20/applicant for ZipRecruiter/Craigslist. Removing artificial constraints unlocks the channel's full potential._\n\n*4️⃣ \"Homebase Boost\" = $50 via Taru CPC bump — locked*\n> You confirmed the Homebase Boost concept in front of the full team: OEMs pay $50 to bump their CPC on Taru, getting applicants faster (day 1, not day 3+). This replaces the $79 Craigslist boost and $199 ZipRecruiter boost, both of which you called out as \"extremely ineffective.\"\n> _Rationale: ZipRecruiter avg = 13 additional applicants ($15/app). Craigslist avg = 4 additional applicants. Taru = $2/app. The math is overwhelming._\n\n*5️⃣ Manual Mode V2 = FREE for everyone, regardless of plan — confirmed publicly*\n> You clarified for the team (and CS) that hiring V2 is free across all plans. The strategic intent: max job postings → seed the Homebase Marketplace. CS had been under the impression it required a Plus plan (because V1 was a ghost-packaged perk).\n> _Rationale: More jobs = more applicants = Marketplace flywheel. Short-term revenue sacrifice for long-term network effects._\n\n*6️⃣ Job Get integration — shipping this week*\n> You confirmed the Job Get (hourly work platform, like Indeed/ZipRecruiter) integration is finalizing between today and early next week.\n> _Rationale: Diversifying applicant sources reduces Indeed dependency and increases job health across the board._\n\n*7️⃣ TLWA Careers Page — customized per business, ready to go at QR scan*\n> You confirmed that for all 50,000 TLWA recipients, you've been building a pipeline to auto-populate: business logo, photos, primary colors, company description. When job seekers scan the QR, the page is ready.\n> _Rationale: Frictionless first impression for TLWA moment = max conversion from award recipient to active hiring customer._\n\n*8️⃣ Indeed job visibility issue → pursue via 3LO + Indeed rep*\n> Michael flagged that jobs are findable on the company page but *not* in general Indeed search results. You confirmed 3LO (three-legged OAuth) will give you job status retrieval from Indeed employer accounts. You also noted the issue may be geo-based search ranking. Follow-up committed: send Michael the job + ping Indeed rep.\n> _Rationale: If jobs aren't showing in search, Taru + 3LO visibility is your best backstop until Indeed resolves ranking._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• [ ] *You → Michael Heistand* — get the specific job ID he flagged for Indeed search invisibility; escalate to Indeed rep alongside 3LO status\n• [ ] *You* — finalize Job Get integration (today or early next week)\n• [ ] *You + Fadi* — confirm TLWA careers page pipeline is QA'd and ready before 50k QR codes go out\n• [ ] *You + Ray/Jon* — spend increase on Taru is approved; monitor CPC performance week-over-week as volume goes from 300→1,100\n• [ ] *Zuara + Sales* — brief the sales team that free Craigslist boosts should migrate to Homebase Boost ($50 Taru) once live; pipeline is being built\n• [ ] *Jatin* — resume scoring logic experiments to be discussed Tue with Fadi + Aman; bandwidth available for TLWA support if needed\n• [ ] *Nelson* — complete metro_area + bucketed_role + matching_roles Supabase columns (still overdue from Apr 8) and wire up job recommendation carousel"
        }
    },
    {"type": "divider"},

    # ── MEETING 3 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 3 of 3 — Sprint Show & Tell* (11:00 AM)\n_All-company, 30+ attendees_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Observations & Decisions (as PM/audience):*\n\n*9️⃣ GTM OS ML prioritization model — signal to watch*\n> Liz (Data Science) shared a model trained on pre-conversion behavior signals — 70% of top 250 companies converted within 7 days of being flagged. This is directly relevant to your Homebase Boost targeting strategy.\n> _Opportunity: Can you use this same signal logic to prioritize which jobs get a Homebase Boost nudge on day 1?_\n\n*🔟 Lifecycle Marketing = 46% of team app upgrades influenced*\n> Susie's team is crushing it — 432% increase in payroll milestone completions, 141% lift in free trial entries (Hiring Assistant), 30% conversion efficiency on newsletter. These are compounding flywheel effects that directly support hiring upsells.\n> _The dispatch email builder (70% faster build time) is now live — worth aligning with Kayla on TLWA-specific lifecycle sequences._\n\n*1️⃣1️⃣ CS Training Simulator (Lovable AI) — builder culture moment*\n> Liza + Elizabeth built a functional cash-out simulator in hours/days. This is proof of concept for your \"non-technical builders should build\" philosophy from the INC-372 retro.\n> _Decision-adjacent: This supports NOT mandating PR review for AI-assisted tools — education + tooling IS the right path._\n\n*1️⃣2️⃣ AI Context Repository for Analytics — now live*\n> Three-folder structure (Global / Domain / Data) to give AI sessions company context. Claude Code is the preferred workflow.\n> _Action for you: Get access to this repo — it'll make your Supabase + job recommendation work significantly faster._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Action Items:*\n• [ ] *You → Analytics/Data Science* — explore using GTM OS conversion signals to power Homebase Boost day-1 targeting\n• [ ] *You → Kayla* — align on TLWA-specific lifecycle sequences using the new dispatch email builder\n• [ ] *You* — get access to the AI context repository (GitHub); use it for Supabase + careers page work"
        }
    },
    {"type": "divider"},

    # ── CRITICAL CARRY-FORWARDS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 CRITICAL — Don't Let These Slip Into Next Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "| Priority | Item | Status |\n|---|---|---|\n| 🔴 P0 | *TLWA brief → Ted* | NOW 9 DAYS OVERDUE — send this weekend |\n| 🔴 P0 | *Homebase Boost SKU with Chris McIntosh* | Billing window closing — Early May is NOW |\n| 🔴 P0 | *Manual Mode green light* | Cindy QA done — it's on you. Just say go. |\n| 🟠 P1 | *Andrew: company-level vs location-level Indeed connection* | Needed for Mon grooming |\n| 🟠 P1 | *Jeff 3LO prototype* | Review + acceptance criteria before Mon grooming |\n| 🟠 P1 | *Nelson: Supabase columns + absolute delta* | Overdue since Apr 8 |\n| 🟡 P2 | *Generic roles proposal doc* | Write both options, recommend location-mapping |\n| 🟡 P2 | *Minh: INC-372 retro doc update* | Private key/Vercel storage details |\n| 🟡 P2 | *Schedule Divij mentorship session w/ Ted + Dana* | — |"
        }
    },
    {"type": "divider"},

    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Friday Scorecard*\n> ✅ Taru feed expanded (300→1,100 jobs) — ships this week\n> ✅ Homebase Boost $50 concept confirmed publicly to full team\n> ✅ Manual V2 = free, message aligned with CS\n> ✅ Job Get integration finalizing\n> ✅ TLWA careers page customization in flight\n> ⚠️ Nelson deliverables still outstanding\n> 🔴 TLWA brief to Ted is 9 days overdue — this is the one thing to fix this weekend"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You had a genuinely strong Friday, Manan. The Taru expansion + Homebase Boost framing in front of the full team was a power move — you've set the narrative and the team knows exactly where this is going. The only thing standing between you and a clean week is that TLWA brief to Ted. Write it tonight or first thing tomorrow morning — it will take 20 minutes and unlock everything else. You've got this. 💪\n\n_— Your Chief of Staff_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "🌟 Your Friday Debrief — April 10, 2026 | Decisions + Action Items",
    "blocks": blocks,
}

if not SLACK_TOKEN:
    print("=== PREVIEW MODE (no SLACK_TOKEN) ===")
    print(json.dumps(payload, indent=2))
    print("\n✅ Script completed — set SLACK_TOKEN env var to send to Slack.")
else:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
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
            print(f"✅ Slack message sent! ts={body.get('ts')}")
        else:
            print(f"❌ Slack API error: {body.get('error')}")
            print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
