#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari — Apr 3, 2026 (based on Apr 2 meetings)."""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌟 Your Daily Debrief — Thursday, April 3",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan — you had a *seriously productive* day. Four meetings, four distinct workstreams moved forward with real clarity. Here's everything you decided, why it matters, and what's next.",
        },
    },
    {"type": "divider"},

    # ── Meeting 1: Jeff / Manan ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 — Jeff / Manan · 9:00 AM*\n_Indeed 3LO UX Design Review_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "• *\"View on Indeed\" = secondary action, not primary.* Live means live everywhere — surfacing Indeed alone risks giving OAMs the wrong impression that Indeed is all that matters. Keep it discoverable, not prominent.\n"
                "• *Disabled button + \"typically viewable within 1–2 hours\" subtext* immediately after posting — removes anxiety without over-explaining the pipeline.\n"
                "• *Email notification when job goes live on Indeed.* OAMs train on this behavior fast — they post, they wait, the email lands, they click. Clean.\n"
                "• *Graceful fallback if 2+ hours pass with no live status:* show a \"we're working on it / contacting Indeed on your behalf\" message. Never leave them in silent limbo.\n"
                "• *Two to-do tasks to add to hiring dashboard:* (1) Connect with Indeed to view your live post, (2) Boost your job on Indeed.\n"
                "• *Indeed boost option in the rocket/boost panel* — a dedicated CTA to connect & boost via Indeed alongside other channels.\n"
                "• *Jeff to prototype the full updated flow* and share ASAP (ideally before lunch on Apr 3)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why it matters:* The 3LO connection is the unlock for Indeed Sponsored Jobs — this UX scaffolding needs to be airtight before the feature ships. Getting the state machine right now (pending → live → error → graceful fallback) prevents a wave of OAM confusion and support tickets at launch."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "◻ Review Jeff's prototype when he shares it — give feedback before it goes to the wider team\n"
                "◻ Add the pending-state, email-notification, and graceful-fallback requirements to the acceptance criteria doc"
            ),
        },
    },
    {"type": "divider"},

    # ── Meeting 2: Nelson / Manan ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Meeting 2 — Nelson / Manan · 9:30 AM*\n_Careers Page Data Architecture_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "• *Supabase = source of truth* for all careers page data. Clean separation from the main HB1 data layer.\n"
                "• *Normalized table structure locked:* base table (location ID, location name, company ID, company name, owner email) + separate lookup tables for each mutable field (address, business category/type, Google Places ID). Upsert by ID; truncate individual lookup tables rather than nuking everything on refresh.\n"
                "• *Primary location ranking logic (for multi-location companies):* (1) most hours worked / shift count — best proxy for the flagship location, (2) Google Places ID present, (3) company website URL present. \"First created\" is out — older locations have thinner data.\n"
                "• *Generic roles tiering system:* Tier 0 = no data → \"Team Member\"; Tier 1 = \"Team Member\" + Nelson's predicted role (hiring-pattern model); Tier 2 = \"Team Member\" + active job from existing roster. Requires a full brief before going deeper.\n"
                "• *~2–4k businesses missing Google Places IDs* — can query Google by business name to fill gaps."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why it matters:* This is the foundational data layer for the entire TLWA careers page launch. Getting the schema right now means ~60k location upserts won't corrupt data when source records change — and the tiering system is what makes blank careers pages actually look compelling to job seekers."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "◻ Build the normalized Supabase tables (base + lookup tables for address, biz type, Google Places ID)\n"
                "◻ Upsert all ~60k location rows into Supabase\n"
                "◻ Update location-ranking logic to prioritize hours worked / shift count\n"
                "◻ Write the generic roles epic brief and share with Nelson before syncing on it\n"
                "◻ Nelson is playing around with Supabase today — loop back with him to confirm upsert approach works"
            ),
        },
    },
    {"type": "divider"},

    # ── Meeting 3: Weekly Hiring Data Science Check-in ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔬 Meeting 3 — Weekly Hiring Data Science Check-in · 1:30 PM*\n_Team: Dana, Ted, Jatin, Ray, Martin_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "• *Resume parsing will NOT ship by end of sprint.* API contract between data science (Divij) and engineering hasn't been defined. Root cause: sprint was planned before requirements existed. No blame — process fix needed.\n"
                "• *Jatin owns delivery visibility across ALL engineering* — data science, front-end, back-end. No more siloing by discipline. He needs to drive the API contract conversation between Divij and eng to unblock resume parsing.\n"
                "• *This is a team-wide communication problem, not a Divij problem.* \"Show the work\" scope ballooned without the broader team knowing (including you — you learned it's still not done *today*). Dana's framing was right and the room agreed.\n"
                "• *Ted gets more than 1 hour/week.* He's here for thought partnership and roadmap direction — the kind of proactive \"what if we used an MCP server for scheduling?\" thinking that's currently missing. More involvement = more value.\n"
                "• *Divij mentorship plan (post-call, Manan + Ted):* Divij executes well once directed; the gap is proactive communication (e.g., spent 1.5 weeks reformatting markdown for Google Forms instead of flagging the prompt issue). Ted will mentor more explicitly now that the gaps are named.\n"
                "• *TLWA / Launch Week data science scope locked:* Pre-populate each of the ~50k careers pages with 1–3 ready-to-activate jobs — (1) General application (templated, lightly personalized), (2) Predicted role based on business type (e.g., barista for coffee shop). Divij generates JDs + screener questions for predicted roles. Brief was due from you end of day Apr 2."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why it matters:* The resume parsing slip is a symptom of a systemic issue — data science work living in a silo. Naming it clearly and moving accountability to Jatin is the right call. The TLWA brief is on the critical path for Launch Week and Small Business Week (May 3–9)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "◻ *Send the TLWA / Launch Week brief to Ted* (was due end of day Apr 2 — get this out first thing)\n"
                "◻ Schedule time with Ted + Dana to formally plan Divij's mentorship and expand Ted's involvement\n"
                "◻ *Monday: align with Ted* on Divij mentorship approach\n"
                "◻ Follow up with Jatin — confirm he feels equipped to own delivery visibility across full stack including data science\n"
                "◻ Ray checking with Jatin on the same — make sure there's no mixed message"
            ),
        },
    },
    {"type": "divider"},

    # ── Meeting 4: New note / HB1 Generic Roles v2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏗️ Meeting 4 — Solo Work Session / HB1 Notes · 7:33 PM*\n_Generic Roles v2 Architecture_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "• *v2 can't use location-level mapping* (every v2 job must have a unique job request ID — you can't have a location collecting applications without one).\n"
                "• *Agreed architecture:* Create a job request per location, add a `is_generic_role` flag column to hiring job requests. If flagged: turn off syndication settings + set expiry date to 2099.\n"
                "• *Front-end approach locked (Option 1 over Option 2):* Single generic application entry on the careers page. When a job seeker applies, they select their location — application maps to that location's generic role job request. One entry, not one-per-location (which gets cluttered fast with 6+ locations).\n"
                "• *Company case feature:* Back-end models are being built to support editability and asset uploads. Thursday + Friday off — targeting code-ready by end of next week.\n"
                "• *Proposal doc plan:* Write up both options but recommend the location-mapping approach. Flag that people may have strong opinions worth surfacing."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why it matters:* Generic roles are the fallback experience for the majority of TLWA career pages — companies that have never posted a job. Getting the v2 data model right before writing code saves an expensive re-architecture later."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "◻ Write up the generic roles proposal (both options, with recommendation for location-mapping)\n"
                "◻ Switch focus to generic roles work once company case back-end is unblocked (end of next week)\n"
                "◻ Revisit the \"three items\" mentioned in your notes (transcript was cut off — check your own notes)"
            ),
        },
    },
    {"type": "divider"},

    # ── Overdue / Carry-Forward ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🚨 Overdue / Still Needs You*\n"
                "These are still open from earlier this week — don't let them slip into the long weekend:\n"
                "• *Homebase Boost SKU kick-off with Chris* (billing needs 3-week lead for Early May) — CRITICAL, this is a blocker\n"
                "• *Manual Mode green light* — Cindy's QA is done, ball is in your court\n"
                "• *Andrew's 3LO spike review* + email Kenneth + add Ray to the thread\n"
                "• *Applicant flow brief + prototype* — overdue since Mar 25, needs a decision: do it or descope\n"
                "• *MBR content* — was due Wed Apr 1 AM"
            ),
        },
    },
    {"type": "divider"},

    # ── Closing ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Big picture:* You made real architectural decisions today — the kind that save your team weeks of rework. The Supabase schema, the generic roles v2 model, and the Indeed UX state machine are all cleaner because of today's conversations. The data science accountability conversation was hard but necessary — and you handled it well.\n\n"
                "Enjoy the long weekend. Monday is going to be a big one. 💪"
            ),
        },
    },
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Debrief — Thursday, April 3 (4 meetings, big decisions across Indeed UX, careers page architecture, data science accountability, and HB1 generic roles)",
    "blocks": blocks,
}

def send_slack(token, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=body,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


if not SLACK_TOKEN:
    print("⚠️  SLACK_TOKEN not set — printing preview instead.\n")
    print("CHANNEL:", CHANNEL_ID)
    print("TEXT:", payload["text"])
    print("\n--- BLOCKS (truncated) ---")
    for b in blocks:
        if b.get("type") == "section" and "text" in b:
            print(b["text"]["text"][:200])
            print()
    print("Set SLACK_TOKEN in Cursor Dashboard > Cloud Agents > Secrets to enable live delivery.")
else:
    result = send_slack(SLACK_TOKEN, payload)
    if result.get("ok"):
        print(f"✅ Message sent successfully! ts={result.get('ts')}")
    else:
        print(f"❌ Slack error: {result.get('error')}")
        raise SystemExit(1)
