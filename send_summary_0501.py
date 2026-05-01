#!/usr/bin/env python3
"""Daily decision summary for May 1, 2026 -- based on Apr 30 meetings."""

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
            "text": "Your Daily Decision Summary -- Thu Apr 30 \ud83d\ude80",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! What a day -- *TLWA launches in 4 days* and you crushed it in 3 meetings today. Here's everything you decided, why it matters, and exactly what to do next. Let's go! \u26a1"
        }
    },
    {"type": "divider"},

    # ── MEETING 1: HIRING LEADS STANDUP ──────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcca Hiring Leads Standup* | 8:45 AM | Manan, Fadi, Dana, Matan, Cindy, Jatin, Ray, Nelson, Jeff, Ugo"
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 1: Tight sprints starting Sprint 2610*\n> You + Martin agreed to move to structured 'tight sprints' where requirements are fully fleshed out *before* the sprint starts. No more mid-sprint pivots burning the team.\n\n*Why:* Engineering morale is suffering from TLWA crunch mode. Stable, well-defined work windows will reduce confusion, context-switching, and burnout -- and let engineers internalize trade-offs themselves.\n\n*\u2705 Actions:*\n\u2022 Martin + Jatin: finalize tight sprint standards + individual engineer needs eval by Sprint 2610\n\u2022 You: craft clear messaging to the eng team *after* TLWA ships -- frame it as a gift, not a correction\n\u2022 Reduce Sprint 2610 scope proactively to make tight execution actually possible"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 2: Team lane split -- Manan owns hiring lane, Dana owns her lane*\n> Moving away from a single prioritized backlog to parallel lanes so you and Dana each own your destiny.\n\n*Why:* Single backlog creates constant priority conflicts and makes it impossible for either PM to move fast. Lanes = speed + accountability.\n\n*\u2705 Actions:*\n\u2022 Define lane boundaries (which engineers sit in which lane) before Sprint 2610 kickoff\n\u2022 Loop in Martin + Jatin on final structure"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 3: V1 \u2192 V2 migration due EOD Friday (Ugo)*\n> Ugo is confident he hits end-of-day Friday. Overtime authorized if needed.\n\n*\u2705 Actions:*\n\u2022 Check in with Ugo tomorrow (Fri May 1) -- confirm he's on track or escalate immediately\n\u2022 This is a TLWA ship blocker. Do NOT let Friday pass without confirmation."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 4: Carlo moves to careers page bugs; Boost Pathways on hold until done*\n> Carlo is off Pathways temporarily and focused on careers page QA/fixes. He returns to Pathways after careers page is stable.\n\n*Why:* TLWA careers page ships May 4. Everything else is secondary.\n\n*\u2705 Actions:*\n\u2022 Confirm Carlo\u2019s exact return date to Pathways (should be Monday May 4 or Tuesday May 5)\n\u2022 Protect the May 11 Boost Pathways launch -- don\u2019t let this slip further"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 5: Malcolm starts OTP (one-time purchase) planning Mon/Tue -- primarily front-end*\n> Generic role Rake task completes today, freeing Malcolm for OTP planning starting tomorrow/Monday.\n\n*\u2705 Actions:*\n\u2022 Brief Malcolm on OTP scope before he starts -- make sure he has the full context on Boost modal states\n\u2022 Tag Charmaine too when generic role Rake task is confirmed complete"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 6: Indeed 3LO redirect URL blocking Tanner -- Ray escalating to Gustavo*\n> Tanner is paused on 3LO, redirected to careers page bugs. Ray owns the escalation to Indeed\u2019s Gustavo.\n\n*\u2705 Actions:*\n\u2022 Ping Ray today -- confirm he sent the nudge to Gustavo\n\u2022 If no response by Monday, escalate through your Indeed partnership contact"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 7: Company page presets -- 20K done, 30K in progress (Bob + Izzy); no data overwrite*\n> Bob and Izzy are processing remaining 30K presets. Confirmed: existing data will NOT be overwritten. TLWA award display component ready by EOW.\n\n*\u2705 Actions:*\n\u2022 Verify with Bob/Izzy that the remaining 30K completes before Monday morning (May 4 9am ET launch)\n\u2022 Double-check the TLWA award display component is deployed to prod before Sunday night"
        }
    },

    {"type": "divider"},

    # ── MEETING 2: CAREERS PAGE QA REVIEW ────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd0d Careers Page QA Review* | 11:15 AM | Manan, Carlo, Tanner"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 8: Hex code input field added to color picker*\n> Users will be able to manually type hex codes (with # + 3-6 char validation; defaults to last valid color on bad input).\n\n*Why:* Power users and brand-conscious SMBs need this. Without it, color customization feels half-baked for TLWA winners.\n\n*\u2705 Actions:*\n\u2022 Carlo/Tanner: ship this in current PR; test browser native color picker edge cases"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 9: Banner image replacement -- restore pencil icon (not delete+re-add)*\n> The current delete+add flow breaks with 2+ photos. Restoring the pencil icon for direct replacement mirrors the logo flow (which already has backend replacement logic).\n\n*\u2705 Actions:*\n\u2022 Carlo: port logo replacement backend logic to banner images -- confirm it\u2019s in this sprint\n\u2022 QA the 2+ photo edge case before Monday"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 10: Logo display switches from 'fill' to 'fit'*\n> Prevents logo cropping -- TLWA logos were getting clipped. Rectangular logos will appear smaller but uncropped. Acceptable for V1.\n\n*\u2705 Actions:*\n\u2022 Tanner: implement + QA across logo sizes; confirm with TLWA sample logos"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 11: Image carousel -- 3500ms auto-rotation with manual override*\n> Adds automatic rotation to the image carousel (3.5 second intervals) but lets users manually swipe/click to override.\n\n*\u2705 Actions:*\n\u2022 Carlo/Tanner: implement before Monday; make sure touch swipe works on mobile"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 12: Edit mode affordances stay purple (don't inherit brand color)*\n> Edit-mode UI elements (borders, handles, active states) should always be Homebase purple, not the company\u2019s brand color -- otherwise editor UI becomes invisible against similar brand colors.\n\n*\u2705 Actions:*\n\u2022 Tanner: apply globally across editor -- audit all interactive affordances"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 13: Mobile preview height -- confirm scroll behavior with Cindy*\n> Open question: is the 884px mobile preview a fixed frame (no scroll) or does it scroll? Needs Cindy alignment before Carlo/Tanner implement.\n\n*\u2705 Actions:*\n\u2022 *YOU*: Ping Cindy *today* (before EOD) and get the answer -- this is blocking Carlo/Tanner\n\u2022 If Cindy is unreachable, default to: scrollable inside fixed 884px container (matches real phone UX)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 14: Mobile multi-location fixes -- clickable address links + primary color text*\n> Address links were not tappable and not styled with primary color on mobile. Both fixed.\n\n*\u2705 Actions:*\n\u2022 Carlo: fix address tap targets and color; QA on real iPhone before Monday"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 15: Font preview icons replaced with actual font samples (from Cindy\u2019s assets)*\n> Abstract icons don't communicate font choices. Real font samples do.\n\n*\u2705 Actions:*\n\u2022 You: grab Cindy\u2019s font sample assets and hand off to Carlo/Tanner\n\u2022 Target: ship before Monday"
        }
    },

    {"type": "divider"},

    # ── MEETING 3: LUNCH & LEARN W/ RAY ──────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83e\udd16 Lunch & Learn w/ Ray -- Personal Assistants (Vibe)* | 12:30 PM | Manan, Ray, Fadi, Justin, Keyvan, Sammy, Kate, Phil"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 16: Vibe pilot -- 10 Homebase employees to use Vibe for personal assistant agents*\n> Ray shared his 'Sydney' agent built on Vibe (email triage 3x/day, family scheduling, daily Slack briefings). The Vibe team wants 10 HB employees for a pilot program.\n\n*Why:* Ray called it 'life-changing' after 2 weeks. This is real-world validation of the personal-assistant-agent concept you\u2019re building into HB Assistant. You\u2019ll learn what context accumulation, behavior patterns, and multi-user permission models actually look like in production -- invaluable input for the product.\n\n*\u2705 Actions:*\n\u2022 *Fadi*: get Slack app approval from Joseph -- this is the blocker for HB employees to connect to Vibe\n\u2022 You: nominate your 10 pilot users (suggest: Fadi, Justin, Keyvan, Sammy, Kate + 5 from hiring/product teams)\n\u2022 You: schedule a 30-min 'Sydney debrief' with Ray in ~2 weeks to capture learnings for HB Assistant roadmap"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 17: Agent context strategy -- incremental building beats big-bang upfront design*\n> Ray\u2019s key lesson: start with one real pain point, let the agent improve itself daily (his Sydney reviews an improvement list at 5pm and self-directs one enhancement). Don\u2019t try to design the whole context model upfront.\n\n*Why this matters for your roadmap:* This directly validates the 'agentic era starts May 1' framing. The right model for HB Assistant is iterative context accumulation, not a grand unified design session.\n\n*\u2705 Actions:*\n\u2022 In your HB Assistant tool definitions doc (due *today*): include a section on incremental context expansion -- what\u2019s Day 1, Day 7, Day 30\n\u2022 Use Ray\u2019s family hub schema as a reference architecture for the HB hiring context model"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 18: Managed agent platform (Vibe) vs build-from-scratch = Vibe wins for personal use*\n> Vibe\u2019s agent+app builder handles database creation, context management, and permissions automatically. For personal productivity use cases, this beats building from scratch by a wide margin.\n\n*Why:* This shapes the 'agentic era' experimentation framework starting tomorrow (May 1). Not everything needs to be built in-house.\n\n*\u2705 Actions:*\n\u2022 For the hiring team\u2019s agentic experiments (starting May 1 today!): evaluate Vibe as the platform vs LangChain/custom\n\u2022 Capture the Vibe platform limitations Ray mentioned (no calendar invite acceptance, no airline booking, SMS lacks threading) -- these are UX constraints to design around"
        }
    },

    {"type": "divider"},

    # ── FIRE ITEMS ────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd25 OVERDUE / FIRE ITEMS -- Do These Tonight or First Thing Tomorrow*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *HB Assistant tool definitions doc* -- DUE TODAY (agentic era starts tonight). If not done, send what you have to the hiring team with a 'WIP' label\n\u2022 *TLWA brief to Ted* -- 20+ DAYS overdue. Send. It. Tonight.\n\u2022 *iOS safe area CSS* (Gbolade/Izzy) -- SHIP BLOCKER for May 4. Confirm fix is merged and deployed to staging\n\u2022 *TLWA company list freeze* (55,696 vs 54,000 discrepancy) -- freeze tonight; 3 days to launch\n\u2022 *Brainstorming doc PR* -- Ray is waiting. Push tonight.\n\u2022 *Cindy: mobile preview scroll behavior* -- blocking Carlo/Tanner (see Decision 13 above)\n\u2022 *Matan: post Boost plan to #leads + customer survey on hiring spend* -- overdue since Apr 23\n\u2022 *Nelson: metro_area + bucketed_role + matching_roles* -- overdue since Apr 8 \ud83d\udea8"
        }
    },

    {"type": "divider"},

    # ── TLWA COUNTDOWN ────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83c\udf89 TLWA LAUNCH COUNTDOWN: T-4 Days (Mon May 4, 9am ET)*\n\n*Must-complete before Sunday night:*\n\u2022 \u2610 V1\u2192V2 migration (Ugo, Fri EOD)\n\u2022 \u2610 30K company presets complete (Bob/Izzy)\n\u2022 \u2610 TLWA award display component deployed to prod\n\u2022 \u2610 iOS safe area CSS merged (Gbolade/Izzy)\n\u2022 \u2610 Company list frozen (55,696 final count locked)\n\u2022 \u2610 Careers page: all Monday-ship items from QA review merged\n\u2022 \u2610 OTP sad path complete (email working, phone pending)\n\u2022 \u2610 Indeed redirect URL received from Gustavo (Ray\u2019s action)"
        }
    },

    {"type": "divider"},

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Summary: 18 decisions, 3 meetings, 4 days to TLWA.* You are *so close* to the finish line. The eng morale conversation shows real leadership -- taking care of the team while shipping something massive. Tomorrow is the agentic era Day 1 AND V1\u2192V2 deadline AND the last full working day before launch. Make it count. \ud83d\udcaa\n\n_Your Chief of Staff \ud83e\udd1d_"
        }
    }
]

def send_slack(blocks):
    payload = json.dumps({
        "channel": CHANNEL,
        "text": "Daily Decision Summary -- Thu Apr 30",
        "blocks": blocks
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": "Bearer " + SLACK_TOKEN,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully!")
            else:
                print("Slack API error:", body.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error:", e)
        sys.exit(1)

def preview():
    sys.stdout.buffer.write(
        json.dumps({"blocks": blocks}, indent=2, ensure_ascii=False).encode("utf-8", errors="replace")
    )
    sys.stdout.buffer.write(b"\n")
    print("\n--- PREVIEW MODE (no SLACK_TOKEN set) ---")

if SLACK_TOKEN:
    send_slack(blocks)
else:
    preview()
