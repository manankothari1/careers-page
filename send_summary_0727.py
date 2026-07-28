#!/usr/bin/env python3
"""Daily Chief-of-Staff Digest — Monday July 27, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Monday Jul 27 — End-of-Day Debrief",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day — SBA shipped, Role Rec architecture got locked, FFH candidate preview got real detail, and you showed Ray the prototype. Three packed meetings. Here's everything that matters. You crushed it today. :rocket:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: DECISIONS MADE TODAY*"
        }
    },

    # ---- MEETING 1: ROLE REC HANDOFF ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Role Recommendation Handoff (10am | Sina, Rami, Tanner, Izzy)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":lock: *Use Hiring Package (not self-serve HPLM) for role recommendation*\n"
                "_Why:_ Rami can update the prompt independently — no data platform roundtrip. Better input/output logging for prompt eval. Keeps the team autonomous.\n\n"

                ":lock: *Ship current prompt as-is — no pre-launch optimization*\n"
                "_Why:_ Deb's multi-step suggestion is valid but not on the critical path. Get it in users' hands first, iterate from real signal. Deb's suggestion deferred to v2.\n\n"

                ":lock: *One combined gRPC endpoint: role recommendation + role normalization*\n"
                "_Why:_ Two sequential endpoints = 4-6s total latency. Combined prompt = ~3-4s. Role rec and salary rec MUST surface simultaneously in the UI — sequential calls break the experience. Role normalization split can happen later when other teams need to reuse it.\n\n"

                ":lock: *Role normalization added as top-ranked bucket output in role rec prompt*\n"
                "_Why:_ Open text field (e.g. 'sushi chef') can't map to Antoine's salary table directly. The LLM normalizes to a standard role bucket. Only the #1 rec gets the bucket — clean, low-overhead. Tanner maps bucket → metro salary table."
            )
        }
    },

    # ---- MEETING 2: FADI FFH SYNC ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Manan / Fadi — Hard to Fill Candidate Preview (1pm)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":lock: *Fake candidate data (not live users), real neighborhood names*\n"
                "_Why:_ Real neighborhoods (Mission, SoMa) make it feel credible without privacy risk. Distance field dropped — neighborhood alone gives enough signal.\n\n"

                ":lock: *List view over map view*\n"
                "_Why:_ Map raises unanswerable questions (home address vs. work address, pin placement). List is cleaner and unambiguous.\n\n"

                ":lock: *3 candidate cards (not 6-7)*\n"
                "_Why:_ More breathing room, feels premium. Overcrowding undercuts quality perception.\n\n"

                ":lock: *Minimum 10 candidates per MSA; use specific counts ('14 people' not '300+')*\n"
                "_Why:_ Specific small numbers feel more real and trustworthy than inflated round ones. LA tops 336 line cook; New Orleans surprisingly strong — good supply signal.\n\n"

                ":lock: *Auto-expand accordion animation on page load (~2 second delay)*\n"
                "_Why:_ Feels premium and intentional. Timing needs a small tweak — Fadi owns it.\n\n"

                ":lock: *Owner message pre-filled with template; Homebase wrapper hidden from owner*\n"
                "_Why:_ Job seekers may not remember opting in — Homebase needs to introduce itself first. Owners shouldn't see the boilerplate; their message stays theirs.\n\n"

                ":lock: *Boost CTA added AFTER invites are sent ('Invites are on the way — boost your job')*\n"
                "_Why:_ This is exactly the moment hard-to-fill context motivates action. The 'Hard to Fill' label belongs here, not on the preview screen.\n\n"

                ":lock: *WhatsApp-style photos, pool of ~100 randomized — no headshots*\n"
                "_Why:_ Casual photos make candidates feel human and real. Needs enough variety to avoid same faces appearing across different roles."
            )
        }
    },

    # ---- MEETING 3: RAY PROTOTYPE ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Manan / Ray — Show You the Prototype (3pm)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":bulb: *'Bring Your Own Indeed' concept worth exploring*\n"
                "_Frame:_ Owners keep posting on Indeed (where they trust volume), Homebase handles all downstream screening/ATS/logistics. Reframes product from applicant sourcing → candidate management layer. Persistent candidate pool per business is the long-term prize.\n"
                "_Why it matters:_ The Indeed perception problem is real — owners blame Homebase when volume drops even when Homebase isn't at fault. This model sidesteps that entirely.\n"
                "_Blocker identified:_ Indeed doesn't email applicant contact info. No clean webhook/API. Scraping is undesirable. Ray's bar: real-time contact capture. This is an open architecture question.\n\n"

                ":lock: *Align JD prompt exactly to Indeed's requirements*\n"
                "_Why:_ If Homebase posts perform differently from direct Indeed posts, owners notice. Closing the format gap removes the 'perceived fewer applicants' objection before it becomes a churn risk.\n\n"

                ":lock: *Update scraper to write each row incrementally*\n"
                "_Why:_ Script crashed mid-run at ~400 of 440 jobs — data likely lost. Incremental writes prevent total loss on future crashes. Recovery attempt in progress."
            )
        }
    },

    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:point_right: YOUR ACTION ITEMS (owned by you)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":fire: *TODAY / TONIGHT*\n"
                "• Send Fadi the Boost modal Figma designs _(he needs them if the existing code is hard to pull)_\n"
                "• Recover ~400 scraped jobs + update scraper script for incremental writes\n"
                "• Align JD description prompt to Indeed's exact format requirements\n\n"

                ":rotating_light: *STILL OPEN FROM LAST WEEK (don't let these slip)*\n"
                "• Carlo Ferrer — 14+ DAYS overdue on Harness/OpenSpec. This is a management issue now. Have the direct conversation.\n"
                "• 422 job publishing errors — Day 17. Jatin is on RCA. Get a status update.\n"
                "• Matan comms doc review — Sonia has been blocked waiting. If you haven't reviewed it yet, do it tonight.\n"
                "• Juan Sanchez email issue — he's sending outside the proper flow. Follow up directly.\n"
                "• Usman candidate email experiment — should have results by now. Check in.\n"
                "• Franchise customer CX proposal — you flagged this as in progress. Where does it stand?\n"
                "• Kristin (TalkDesk) — check engineering effort on TalkDesk trigger ID\n"
                "• Abby — week 7+. She needs a clear ownership area. When are you making that call?"
            )
        }
    },

    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:busts_in_silhouette: TEAM COMMITMENTS (they're on it)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Rami* — Review hiring package repo + sync with Sina TODAY (this afternoon)\n"
                "• *Sina* — Create gRPC contract + HPLM endpoint (1-2 days)\n"
                "• *Izzy* — Adjust backend to consume Sina's gRPC contract once it's defined\n"
                "• *Tanner* — Consume normalized role bucket → Antoine's metro salary table for market comparison\n"
                "• *Fadi* — Finalize candidate preview (3-card layout, photos, animation, Boost CTA, updated copy) → wrapping tomorrow to free rest of week for page templates\n"
                "• *Fadi (maybe)* — Prototype chips (role tags) tonight pending eng effort estimate; you're not blocking it\n"
                "• *Gurkiran* — SBA launched today :tada: — watch P1 signal on unassigned grid hard\n"
                "• *Jatin* — 422 error RCA in progress"
            )
        }
    },

    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: WATCH LIST / OPEN QUESTIONS*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *SBA launched today* — unassigned grid was negative in friendly testing. Watch P1 data aggressively. Be ready to act fast.\n"
                "• *'Bring Your Own Indeed' architecture* — Ray is intrigued but the Indeed contact info blocker is real. No webhook, no clean API. Keep this as a strategic concept while the scraper research runs.\n"
                "• *Prototype candidate (Ray's meeting)* — Ray mentioned they'd be a solid hire even if not the top candidate. Keep them warm if hiring opens up.\n"
                "• *Dana succession* — ~7 weeks. Still no plan. Off Aug 7 week. Page Templates hand-off must start NOW. This is the biggest quiet risk on the team.\n"
                "• *Backend resourcing* — Ray is escalating. FE→BE swap still in discussion. ~2 months to hire. Keep visibility here.\n"
                "• *Archived job redirect PR* — in progress from Jul 24. Where does this stand with Jatin?"
            )
        }
    },

    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:trophy: THE BIG PICTURE*\n"
                "Today you locked Role Rec architecture cleanly — one endpoint, combined prompt, ships fast, iterates from signal. The FFH candidate preview got real design clarity (3 cards, neighborhoods, Boost CTA in the right place). And you've opened a genuinely interesting strategic question with Ray about whether Homebase should reframe around candidate management vs. applicant sourcing. That's a meaningful conversation to be having at the right level.\n\n"
                "The open items are real but manageable. Carlo is the one that needs direct action — not another nudge. Take care of yourself tonight. Tomorrow's going to be another good one. :muscle:"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Manan — Monday Jul 27 End-of-Day Debrief (3 meetings, 14 decisions, your action items)",
    "blocks": blocks
}


def preview():
    sys.stdout.buffer.write(
        "\n=== SLACK PREVIEW (no token) ===\n".encode("utf-8", errors="replace")
    )
    for b in blocks:
        if b.get("type") == "section" and "text" in b:
            sys.stdout.buffer.write(
                (b["text"].get("text", "") + "\n").encode("utf-8", errors="replace")
            )
        elif b.get("type") == "header":
            sys.stdout.buffer.write(
                ("[HEADER] " + b["text"].get("text", "") + "\n").encode("utf-8", errors="replace")
            )
        elif b.get("type") == "divider":
            sys.stdout.buffer.write(
                "---\n".encode("utf-8", errors="replace")
            )


if not TOKEN:
    print("No SLACK_TOKEN found — printing preview and exiting.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"Sent! ts={body.get('ts')} channel={body.get('channel')}")
    else:
        print(f"Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
