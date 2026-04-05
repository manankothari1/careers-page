#!/usr/bin/env python3
"""Sunday Apr 5 — Weekly recap + Monday kickoff summary for Manan."""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "☀️ Good evening, Manan — your Chief of Staff here!",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Sunday wrap-up + Monday battle plan. No meetings today (you earned the rest!) "
                "so I reviewed everything from this week and built you a clean picture of "
                "*what you decided, why, and exactly what needs to happen Monday morning.* "
                "It was a big week — you made a lot of great calls. Let's make sure they all land. 🚀"
            ),
        },
    },
    {"type": "divider"},
    # ── SECTION 1: LOCKED DECISIONS ──────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔒 DECISIONS LOCKED THIS WEEK*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. CommandAI → Amplitude (Journeys) — No new nudges in CommandAI effective immediately*\n"
                "> *Why:* CommandAI sunsets end of April. Amplitude Journeys is the replacement — easier engagement tracking, better nudge tooling.\n"
                "> *Owners:* Matan Chen Zion owns migration; new release nudges go into Amplitude starting next week.\n"
                "> *Watch out:* Amplitude needs to be pressure-tested before end of April cutoff. Matan is pressure-testing with next release nudges."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Indeed 3LO UX — \"View on Indeed\" = secondary, disabled for 1-2 hrs post-posting*\n"
                "> *Why:* Surfacing it as a primary action implies Indeed matters more than other boards — it doesn't. "
                "\"Live\" is the signal. Indeed is a curiosity.\n"
                "> *Three states designed:* (1) Posted, not yet live → disabled + \"typically 1-2 hrs\" subtext; "
                "(2) Live → email sent, link enabled; (3) Stuck >6 hrs → graceful \"we're on it\" message.\n"
                "> *Extras:* Two new to-dos (\"View on Indeed\" first, then \"Boost on Indeed\") + Indeed option in boost panel.\n"
                "> *Jeff's ask:* Share alternative design directions (he only saw one leading option at crit)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Careers Page: Supabase normalized tables + location ranking locked*\n"
                "> *Why:* Normalized structure prevents data loss on upserts (individual lookup tables per mutable field). "
                "Ranking primary location by hours worked beats \"first created\" since older locations have missing onboarding data.\n"
                "> *Schema:* Base table (location ID, company ID, owner email) + lookup tables for address, biz category, Google Places ID.\n"
                "> *Ranking order:* Most hours worked → Google Places ID present → company website URL."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Generic Roles v2 Architecture — job-request-per-location + is_generic_role flag*\n"
                "> *Why:* v2 requires every job to have a job request ID — you can't attach applications directly to a location. "
                "Creating one job request per location with a flag is the cleanest path.\n"
                "> *System rules:* generic roles → syndication off, expiry = 2099.\n"
                "> *UX:* Single \"General Application\" entry on careers page; job seeker selects their location on the job page. "
                "Avoids a cluttered multi-location view.\n"
                "> *Next:* Write up both options with recommendation (location-mapping approach above)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Generic Roles tiering for companies without open positions (Nelson sync)*\n"
                "> *Why:* TLWA companies mostly haven't posted jobs — need sensible fallback content for their careers pages.\n"
                "> • *T0:* No data → \"Team Member\" only\n"
                "> • *T1:* \"Team Member\" + Nelson's predicted role (12-month hiring pattern model)\n"
                "> • *T2:* \"Team Member\" + role from existing active jobs in system"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. TLWA Career Pages — standalone component, TLWA badge as hero, animated apply button*\n"
                "> *Why:* Reusing the existing careers page component would have been a liability. Custom gives full control.\n"
                "> *Apply button:* Animate on tap (wiggle or \"Applied ✓\") — removing it entirely risks users thinking the page can't accept applicants.\n"
                "> *Font styles:* Classic/Modern/Friendly change typography only (not persisted) — demonstrating customization potential, not shipping config.\n"
                "> *Description fallback:* Smart default copy from business name + industry if Google Places returns nothing."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Homebase Boost — $50 locked, Tellroo at $0.50 CPC, ~15-20 applicants per boost*\n"
                "> *Why:* Not a revenue play — this is subsidizing applicant flow. Only ~10% of jobs get healthy flow today. "
                "At $2.50-3.50/applicant, this smokes ZipRecruiter ($16/applicant) and Craigslist ($20/applicant).\n"
                "> *Indeed Sponsored Jobs API:* Future workstream — sidebar with Chris McIntosh only for now. "
                "Don't surface in the billing channel yet to avoid confusion with the one-time purchase work.\n"
                "> *Billing handoff:* You're taking over coordination from Dana on the hiring/applicant flow side."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Data Science team structure — Jatin owns delivery visibility across ALL of eng*\n"
                "> *Why:* Resume parsing WON'T ship this sprint (no API contract between Divij and eng). "
                "Root cause: sprint planning happened before requirements were defined. This is a coordination failure, not a Divij failure.\n"
                "> *Resolution:* Jatin drives the API contract conversation AND owns delivery visibility across data science, front-end, and back-end — no more discipline silos.\n"
                "> *Ted's expanded role:* Brought in for thought partnership + roadmap input. Needs >1 hr/week.\n"
                "> *Divij gap named:* Executes well when directed; needs mentorship on surfacing blockers proactively (example: 1.5 weeks reformatting markdown instead of fixing the prompt)."
            ),
        },
    },
    {"type": "divider"},
    # ── SECTION 2: MONDAY MUST-DO ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 MONDAY MUST-DO — Your Top Priorities (in order)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":red_circle: *1. Send TLWA/Launch Week brief to Ted — OVERDUE since Apr 2 EOD*\n"
                "Ted can't do anything on the data science side without this. Resume parsing, "
                "Divij mentorship alignment, and predicted roles all flow downstream from this brief. "
                "Send it first thing Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":red_circle: *2. Homebase Boost SKU kick-off with Chris McIntosh — CRITICAL*\n"
                "Billing needs a 3-week lead for Early May launch. Every day you wait shrinks the runway. "
                "This should be a quick sync — $50, Tellroo integration, one-time purchase SKU. Get it on the calendar."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":large_yellow_circle: *3. Sync with Fadi before Monday squad standup — sprint concerns from Ray + Dana*\n"
                "Ray and Dana said the new sprint doesn't feel different. Fadi needs to know before the all-hands standup "
                "so you're not caught flat-footed. 5-minute alignment, high leverage."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":large_yellow_circle: *4. Green-light Manual Mode — Cindy QA is done, it's on you*\n"
                "Cindy finished QA. You're the blocker. Give it the green light today or first thing Monday — "
                "this is sitting idle waiting for you."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":large_yellow_circle: *5. Review Jeff's Indeed 3LO prototype + send to team*\n"
                "Jeff was asked to share alternative design directions. Review those and share the prototype to the broader team. "
                "Also: add acceptance criteria (Indeed to-do lives at top of to-do list)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":large_yellow_circle: *6. Write generic roles proposal doc (both options + recommendation)*\n"
                "You landed on location-mapping approach (job-request-per-location + is_generic_role flag). "
                "Write up both options and recommend this one — you noted people may have strong opinions worth surfacing early."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":large_yellow_circle: *7. Build Supabase tables + 60k upsert (TLWA)*\n"
                "Nelson is waiting to validate once your tables are live. "
                "Base table + lookup tables for address, biz category, Google Places ID. "
                "Nelson also needs the full list of 8 scraping criteria from you."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_circle: *8. Schedule Ted + Dana Divij mentorship session*\n"
                "Ted is open to mentoring Divij more explicitly now that the gaps are named. "
                "Set this up this week — the gaps were clearly articulated Thursday, momentum is fresh."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_circle: *9. Review Matan's 3 prototypes + topical workplace prototype*\n"
                "Matan shared these out Friday. He got your detailed feedback (thank you for that). "
                "Close the loop with reactions/direction so he doesn't sit idle Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_circle: *10. Andrew 3LO spike review + email Kenneth + add Ray*\n"
                "Still open from last week. Unblocks the Indeed 3LO path — don't let this drift another week."
            ),
        },
    },
    {"type": "divider"},
    # ── SECTION 3: WATCH LIST ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👀 THINGS TO WATCH CLOSELY*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Resume parsing:* Won't ship this sprint. Jatin owns the API contract convo. "
                "Check in Monday — has Jatin connected Divij with eng?\n"
                "• *~8,000 missing TLWA addresses:* Iszael is resolving. Needed for the physical bifold. Confirm status.\n"
                "• *Fadi's 4 design variations (TLWA badge):* Should be shared with Jeff already. Confirm it happened.\n"
                "• *Billing team (Bishop?):* Confirm one-time purchase SKU for Homebase Boost is actively in progress.\n"
                "• *Applicant flow brief + prototype:* Overdue since Mar 25. Needs a date committed or a formal descope decision — "
                "it's been floating too long."
            ),
        },
    },
    {"type": "divider"},
    # ── CLOSING ───────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*You had a genuinely great week, Manan.* "
                "You locked the v2 generic roles architecture, the Supabase schema, the Indeed UX flow, "
                "the Boost pricing, and the TLWA career page design — all in 3 days. "
                "The sprint concerns from Ray and Dana are a gift: you now have the data to make Monday's standup count. "
                "\n\nGo enjoy the rest of your Sunday. Monday's going to be a big one. 💪"
            ),
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Your Chief of Staff | Sunday Apr 5, 2026 | Based on meetings Apr 1–3_",
            }
        ],
    },
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Your Sunday recap + Monday battle plan is ready, Manan!",
    "unfurl_links": False,
    "unfurl_media": False,
}

if not SLACK_TOKEN:
    print("=" * 60)
    print("SLACK_TOKEN not set — printing preview instead")
    print("=" * 60)
    for block in blocks:
        if block["type"] == "section":
            print(block["text"]["text"])
            print()
        elif block["type"] == "header":
            print(f"### {block['text']['text']}")
            print()
        elif block["type"] == "divider":
            print("-" * 40)
    print("=" * 60)
    print("Add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets")
else:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SLACK_TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"✅ Message sent successfully! ts={result.get('ts')}")
            else:
                print(f"❌ Slack API error: {result.get('error')}")
                print(json.dumps(result, indent=2))
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
