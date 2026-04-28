#!/usr/bin/env python3
"""Daily Chief of Staff Summary - Apr 28, 2026 (meetings from Apr 27)"""
import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Debrief - Monday Apr 28 :rocket:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big Monday ahead. You had 3 meetings yesterday (Apr 27) across your Hiring Leads Standup, Sprint Kickoff, and EPDD Cycle Kick Off. Here's every decision you made, why it matters, and exactly what needs to happen next. Let's go get it. :muscle:"
        }
    },
    {"type": "divider"},

    # ─── MEETING 1 ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:busts_in_silhouette: Meeting 1 of 3 | Hiring Leads Standup — 8:30 AM*\n_Manan, Fadi, Dana, Cindy, Jatin, Ray, Nelson, Jeff, Usman_"
        }
    },

    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 1: Jatin will represent Ted/Divij in the standup going forward (starting today)*\n*Why:* There was a visibility gap on Ted's competing priorities from last week. Rather than adding Ted as a required attendee, Jatin will maintain a dedicated 1-on-1 with Ted daily and relay context to the team.\n*Actions:*\n• :point_right: *Jatin* — 1-on-1 with Ted & Divij starts today; relay priorities to standup\n• :point_right: *Manan* — confirm comms channel with Jatin is working; if Ted's priorities ever feel opaque again, flag it immediately"
        }
    },
    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 2: Launch 1Password vault for all sensitive credentials/API keys*\n*Why:* Credential hygiene issue — team members have keys scattered across DMs, Slacks, personal notes. Jatin is centralizing everything in a vault with limited access.\n*Actions:*\n• :point_right: *Jatin* — launch vault; share access protocol with hiring team\n• :point_right: *Manan* — push your tap account API key + any other creds to Jatin once vault is live\n• :point_right: *All hiring team* — audit your local passwords/keys and hand them to Jatin by EOW"
        }
    },
    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 3: TLWA cohort tracking — upload amplitude cohort from TLWA UIDs*\n*Why:* You want to isolate TLWA users in Amplitude to understand their behavior separately (trial starts, entry points, post-trial conversion, job posting activity). Dana can upload the cohort using UIDs from the TLWA list.\n*Actions:*\n• :point_right: *Dana* — upload TLWA winner cohort to Amplitude; confirm Manan has access to the cohort and relevant funnels\n• :point_right: *Manan* — define the specific funnels you want to track (entry point → trial → activation → job post → boost). Do this before May 4 launch\n• :note: Nelson leaves May 9 — ensure cohort is set up before he's out"
        }
    },
    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 4: V1V2 migration — Ugo must be complete by Friday; overtime authorized if needed*\n*Why:* Ugo is confident on a Friday ship. You've pre-agreed on paid overtime over the weekend as a backstop. No slip is acceptable here — TLWA launch week depends on it.\n*Actions:*\n• :point_right: *Jatin* — confirm with Ugo by Wed midday on trajectory; activate weekend plan if there's any doubt\n• :point_right: *Manan* — no action needed unless Jatin flags a risk; stay unblocked for TLWA testing with Tanner"
        }
    },
    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 5: Career page preset + launch-week award flag — Izzy runs Rake task on return; flag must not get lost*\n*Why:* Preset data transfer is code-complete. Izzy returns from vacation today (Apr 28) and will run the Rake task. You explicitly called out that the launch-week award display flag on the careers page is in scope and must not be dropped just because it's bundled with Izzy's preset work.\n*Actions:*\n• :fire: *Manan* — remind Izzy today that the careers page award flag is in scope, not just the preset data transfer. Don't let this fall through\n• :point_right: *Jatin* — confirm Izzy's Rake task is queued and the flag work gets scheduled with Fadi/IBK before EOW"
        }
    },
    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 6: Boost pathways developer assignment — Jatin to confirm by EOD today*\n*Why:* Dana asked; you asked. Neither of you got an answer. Jatin acknowledged and committed to a response before end of day. This is a blocker for Sprint 2610 grooming.\n*Actions:*\n• :fire: *Jatin* — developer assignment for Boost pathways, EOD today (Monday Apr 28)\n• :point_right: *Manan* — follow up with Jatin at 3pm if you haven't heard; grooming is Tuesday and you need this locked"
        }
    },
    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 7: Bob is heads-down on TLWA observability until Wednesday — all engineering questions route through Jatin*\n*Why:* Observability infrastructure (DataDog/Sentry monitoring) for TLWA is critical for launch week. You made this a hard rule — no pings to Bob, no CCs.\n*Actions:*\n• :point_right: *Manan* — enforce this with yourself too. Any engineering questions → Jatin\n• :point_right: *Jatin* — triage everything; Bob surfaces Wednesday"
        }
    },
    # Decision 8
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 8: Indeed 3LO goes into staging + prod testing today — Tanner to book time with Manan*\n*Why:* Indeed has no sandbox, so prod testing is required. Tanner is scheduling a session with you. You haven't seen the calendar invite yet.\n*Actions:*\n• :fire: *Manan* — if Tanner hasn't sent a calendar invite by 10am today, reach out proactively. Testing must happen today\n• :point_right: *Jatin* — prompt Tanner if Manan doesn't have a confirmed time by morning"
        }
    },
    # Decision 9
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 9: Sprint 2610 prototype bucket locked in Linear — grooming kicks off Tuesday*\n*Why:* Linear now has the prototype bucket as the source of truth for Sprint 2610 priority order. Two items (V1V2 migration remainder + resume matching) still need brief details filled in — you flagged this but the priority order itself is locked.\n*Actions:*\n• :fire: *Manan* — fill in the V1V2 + resume matching briefs in Linear prototype bucket TODAY before grooming tomorrow\n• :point_right: *Manan* — make sure Homebase Boost + Predicted Roles briefs are ironclad for Tuesday grooming\n• :point_right: *Jatin* — OTP prep should start being scoped this week for next sprint"
        }
    },
    {"type": "divider"},

    # ─── MEETING 2 ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:trophy: Meeting 2 of 3 | Sprint Kick Off — 10:00 AM*\n_Manan + cross-functional TLWA / brand team_"
        }
    },
    # Decision 10
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 10: TLWA launches May 4 at 9am ET — 800k users, no scope changes*\n*Why:* Third annual campaign. 55k winning locations, 600k employees, 180 location owners getting full in-product Spotify-Wrapped-style experience + persona assignment. Launch is locked. This is the company's Super Bowl moment.\n*Actions:*\n• :point_right: *Manan* — ensure careers page presets are production-ready before May 4. QR code career page in winner kit must work end-to-end\n• :point_right: *Manan* — confirm with Izzy that preset Rake task runs and all 55k career pages are personalized before Monday May 4\n• :point_right: *Manan* — add launch-week award flag to careers page (already flagged in standup — make sure it's tracked)"
        }
    },
    # Decision 11
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 11: QR code hiring card included in winner kit — custom careers page activates on first scan*\n*Why:* Net new this year. First scan activates the custom careers page for the business. Subsequent scans by job seekers go directly to live job listings. This was a deliberate decision to make TLWA a hiring acquisition moment, not just a brand moment.\n*Actions:*\n• :point_right: *Manan* — verify with Fadi/IBK that the QR code → careers page activation flow works end-to-end before May 4\n• :point_right: *Manan* — confirm the careers page that activates looks properly personalized (preset data visible on first visit)"
        }
    },
    # Decision 12
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 12: Customer Connection Challenge runs through May 22 show and tell — prizes for top 3 Homies*\n*Why:* Christina/People team running internal engagement campaign tied to TLWA. Points for visiting customer locations, posting on social, getting product feedback. Announced publicly at Sprint Kickoff.\n*Actions:*\n• :point_right: *Manan* — this is an internal culture moment; consider personally visiting 1-2 TLWA winner locations this week to set an example\n• :note: Winner announced May 22 show and tell"
        }
    },
    {"type": "divider"},

    # ─── MEETING 3 ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:brain: Meeting 3 of 3 | EPDD Cycle Kickoff — 11:00 AM*\n_Full Engineering, Product, Design, Data all-hands — Ankit, Andrea, Ray, Jan, Rachel, cross-functional teams_"
        }
    },
    # Decision 13
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 13: Half-day of learning/experimentation explicitly allocated per sprint for all of Engineering*\n*Why:* Ankit + Andrea added a 5th OKR for Engineering — AI SDLC re-envision. The explicit half-day is locked. Teams can use it individually or by craft. The only requirement is sharing back what worked and what didn't. This is your company making a real bet on velocity differentiation.\n*Actions:*\n• :point_right: *Manan (for hiring team)* — block a half-day in Sprint 2610 for your eng team's experimentation. Make sure Jatin/Fadi schedule it, not leave it vague\n• :point_right: *Manan* — think about what experiment YOU want to propose for the hiring team's half-day. Agentic scheduling? Dynamic UX for job health? Bring a hypothesis"
        }
    },
    # Decision 14
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 14: HB Assistant V0 mobile build is live for internal testing today*\n*Why:* Multi-agent architecture (orchestrator + tool-calling agents + response agent). V0 is the 'ask any question' demo UI. Jatin's agentic experimentation start date (May 1) is right around the corner.\n*Actions:*\n• :fire: *Manan* — test HB Assistant V0 TODAY. You need hands-on time before May 1 agentic era starts and before your show-and-tell scheduling commitment\n• :point_right: *Manan* — define tool calls + structured outputs for the hiring team before Thursday May 1. This is already overdue\n• :point_right: *Manan* — schedule HB Assistant show-and-tell for hiring team before May 1 (you committed to EOD today on this — do it now)"
        }
    },
    # Decision 15
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 15: Indeed API integration is complete — XML feed dependency eliminated*\n*Why:* You presented this publicly at the EPDD kickoff. This is a major risk removal — Indeed was deprecating XML and that was your primary applicant source. Now you're on their API. This is done. Good.\n*Actions:*\n• :point_right: *Manan* — confirm with Andrew (before he leaves) that the Indeed status endpoint is live and returning correct states in prod\n• :point_right: *Manan* — Bob owns prod monitoring for 3LO post-Tanner testing today"
        }
    },
    # Decision 16
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 16: New job page showing 20%+ lift in job seeker → applicant conversion — keep momentum*\n*Why:* You announced this publicly. 20%+ increase in less than a week. The direction on applicant flow work must continue.\n*Actions:*\n• :point_right: *Manan* — make sure this gets into your metrics dashboard / weekly review. Establish a baseline so you can track whether it holds or improves\n• :point_right: *Manan* — surface this to Ray as a proof point for continued investment in applicant flow"
        }
    },
    # Decision 17
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 17: Hiring team pivoting back to core product innovation post-TLWA — agentic scheduling + HB Assistant integration next*\n*Why:* You and Fadi publicly announced this shift at the EPDD kickoff. TLWA + applicant flow were deprioritizing core innovation. That changes now.\n*Actions:*\n• :point_right: *Manan* — begin scoping agentic scheduling and HB Assistant tool integration for Sprint 2611+ planning (start the doc this week)\n• :point_right: *Manan* — the marketplace brainstorm (this week, 2hrs) is also part of this pivot. Don't let it get bumped"
        }
    },
    # Decision 18
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision 18: End-of-trial recommendation experiment showed 26.6% uplift for forced upgrade — validate + scale*\n*Why:* Huge result from Growth team. Personalized plan recommendation at trial end = 26.6% lift for employee-cap forced upgrade. Still running for voluntary upgrades.\n*Actions:*\n• :point_right: *Manan* — follow this closely. When voluntary upgrade results are in, flag to Ray whether to ship to 100%. This directly impacts H1 trial goal (21k target, currently way behind at ~100/week)"
        }
    },
    {"type": "divider"},

    # ─── FIRE ITEMS ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:fire: FIRE ITEMS — Do These First Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1. :rotating_light: *TLWA brief to Ted* — 20+ DAYS OVERDUE. Send it this morning. Stop. Do this first.\n2. :rotating_light: *HB Assistant show-and-tell* — Schedule by EOD today (you committed to this)\n3. :rotating_light: *Tanner 3LO testing* — Confirm time block if not already on your calendar\n4. :rotating_light: *Izzy preset + award flag* — He's back from vacation. Brief him on BOTH tasks today\n5. :rotating_light: *Linear briefs* — Fill in V1V2 + resume matching briefs before tomorrow's grooming\n6. :rotating_light: *Jatin: Boost pathways dev* — Follow up at 3pm if no answer\n7. :rotating_light: *Matan + #leads post* — Boost plan post + survey OVERDUE since Apr 23\n8. :rotating_light: *Nelson: metro_area + matching_roles* — OVERDUE since Apr 8. Today."
        }
    },
    {"type": "divider"},

    # ─── THIS WEEK ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: This Week's Critical Path*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Mon Apr 28* — 3LO frontend deploys behind feature gate (Tanner). TLWA brief to Ted. HB Assistant show-and-tell scheduled. Izzy Rake task queued.\n• *Tue Apr 29* — Sprint 2610 grooming. Predicted Roles placement decision. Have briefs ready.\n• *Wed Apr 30* — Marketplace brainstorm (2hrs). Bob surfaces from observability. Hypothesis framework ready.\n• *Thu May 1* — Agentic era experimentation starts. HB Assistant tool definitions due. Show-and-tell with hiring team.\n• *Mon May 4* — *TLWA LAUNCHES.* 800k users wake up to a win. 9am ET. Everything must be green by EOD Friday Apr 30."
        }
    },
    {"type": "divider"},

    # ─── FOOTER ──────────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You're in a massive week, Manan. TLWA launches in 6 days. You've built something incredible — careers pages personalized to 55k businesses, QR codes in physical winner kits, 800k people waking up to a win. That's real. The fire items above are the only things standing between you and a clean launch. Knock them out this morning and the rest of the week is yours to build on. :muscle: :star2:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Summary | 3 meetings (Apr 27) | 18 decisions | Generated Apr 28, 2026 at midnight UTC"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Decision Debrief - Monday Apr 28 | 3 meetings | 18 decisions",
    "blocks": blocks
}


def send_slack(payload):
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
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body


def preview():
    import sys
    lines = [
        "=== DAILY CHIEF OF STAFF SUMMARY (PREVIEW) ===",
        "Date: Monday Apr 28, 2026",
        "Meetings: 3 (Apr 27)",
        "Channel: D06E4QMHCNN",
        "",
        "MEETING 1: Hiring Leads Standup (8:30 AM)",
        "  Decision 1: Jatin represents Ted/Divij going forward",
        "  Decision 2: 1Password vault launched for all creds",
        "  Decision 3: TLWA amplitude cohort upload via UIDs",
        "  Decision 4: V1V2 done by Friday; overtime authorized",
        "  Decision 5: Preset Rake task + launch-week award flag on careers page",
        "  Decision 6: Boost pathways dev assignment by EOD today",
        "  Decision 7: Bob heads-down until Wed; all eng -> Jatin",
        "  Decision 8: Indeed 3LO prod testing today with Tanner",
        "  Decision 9: Sprint 2610 linear prototype bucket locked; grooming Tue",
        "",
        "MEETING 2: Sprint Kickoff (10:00 AM)",
        "  Decision 10: TLWA launches May 4, 9am ET, 800k users — no scope changes",
        "  Decision 11: QR code hiring card activates custom careers page on first scan",
        "  Decision 12: Customer Connection Challenge through May 22 show and tell",
        "",
        "MEETING 3: EPDD Cycle Kickoff (11:00 AM)",
        "  Decision 13: Half-day learning/experimentation per sprint locked for Eng",
        "  Decision 14: HB Assistant V0 mobile build live — test TODAY",
        "  Decision 15: Indeed API complete — XML dependency eliminated",
        "  Decision 16: New job page: 20%+ lift in job seeker -> applicant conversion",
        "  Decision 17: Hiring team pivots to core innovation post-TLWA",
        "  Decision 18: End-of-trial experiment: 26.6% uplift for forced upgrade",
        "",
        "FIRE ITEMS: TLWA brief to Ted (20+ days overdue), HB show-and-tell scheduling,",
        "  Tanner 3LO testing, Izzy presets + award flag, Linear briefs, Boost pathways dev,",
        "  Matan #leads post, Nelson metro_area/matching_roles",
        "",
        "=== END PREVIEW (SLACK_TOKEN not set) ===",
    ]
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("utf-8", errors="replace"))


if not SLACK_TOKEN:
    print("SLACK_TOKEN not set — printing preview instead.")
    preview()
    sys.exit(0)

try:
    result = send_slack(payload)
    if result.get("ok"):
        print(f"Sent successfully. ts={result.get('ts')}")
    else:
        print(f"Slack error: {result.get('error')}")
        preview()
        sys.exit(1)
except Exception as e:
    print(f"Exception sending to Slack: {e}")
    preview()
    sys.exit(1)
