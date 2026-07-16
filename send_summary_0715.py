#!/usr/bin/env python3
"""Chief of Staff Daily Digest — July 15, 2026"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Digest — Tuesday, July 15",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Big day, Manan.* Four back-to-back meetings and you absolutely crushed it. "
                "Salary recs are officially unblocked — Izzy can start *right now*. "
                "A brand-new partnership opportunity just landed on the table. "
                "Sprint execution is on track. "
                "Here is every decision you made today, exactly why it matters, and your clear path forward. "
                "Let us get into it."
            ),
        },
    },
    {"type": "divider"},
    # ── MEETING 1 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7:00 AM — Full Pod: Refine + Prototype (SBA / Scheduling team)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 1 — SBA H2 roadmap locked into three phases*\n"
                "> *Phase 1 (Jul–Sep):* Ship SBA V1, tackle multi-location quality backlog, run PTO collaboration pilot with payroll team.\n"
                "> *Phase 2 (Oct–Nov):* Scope memory and context — absorb learnings from Home Assistant launch before building.\n"
                "> *Phase 3 (Nov–Dec):* Agentic ideation + tech spec; implementation starts Q1.\n"
                "> *Why it matters:* Sequencing is intentional — V1 ships first, learnings inform memory architecture, agentic autonomy comes last. No rushing rungs 2 and 3 before rung 1 is solid.\n\n"
                "*Decision 2 — Collaboration with Home Assistant is limited until post-September*\n"
                "> They have unresolved technical constraints and no confirmed PMF. Smart to stay parallel rather than dependent.\n\n"
                "*Decision 3 — SBA strategic directive: deepen, not broaden*\n"
                "> Add depth to existing functionality (trust, memory, autonomy) rather than shipping net-new features. "
                "Every sticky on the Miro board is 'easier said than done' — technical constraints must be surfaced for each.\n\n"
                "*Decision 4 — Scheduler + Schedule Builder agent merge still on the table*\n"
                "> Legacy code and downstream effects are the core risk. No final call yet — needs more investigation.\n\n"
                "*Decision 5 — Prototyping session outputs to present to John if strong*\n"
                "> Group 1: multi-location optimization. Group 2: mobile SBA ('talk to the schedule'). "
                "Group 3: availability/onboarding concept with unavailability agent as agentic component."
            ),
        },
    },
    {"type": "divider"},
    # ── MEETING 2 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9:30 AM — Instawork x Homebase (Partnership Exploration)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 6 — Instawork partnership is worth exploring for hard-to-fill roles*\n"
                "> Instawork sells *guaranteed interview attendance*, not applications. "
                "~$100/completed interview, $200-300 for niche roles. "
                "They vet candidates before the interview — hiring manager just shows up.\n"
                "> *Why it matters for you:* Line cooks are only 7% healthy by D30. "
                "General job boards do not work for back-of-house roles. "
                "Instawork's 11M workers are high-intent with verified performance history from shift work. "
                "This could be the unlock for your hardest Q3 goal.\n"
                "> *The key unknown:* Will Homebase SMB customers pay $100/interview? "
                "Ashwin's pitch: factor in screening time + no-shows and the cost-per-hire math often wins vs. Indeed. "
                "Homebase fills ~30-40K roles/year — significant headroom.\n\n"
                "*What you need to do next:*\n"
                "> Talk to a handful of customers who hire line cooks regularly. "
                "Would they pay $100 for a guaranteed interview with a pre-vetted candidate who actually shows up? "
                "If yes, pilot with 1-2 businesses, then reconnect with Ashwin."
            ),
        },
    },
    {"type": "divider"},
    # ── MEETING 3 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10:00 AM — Rami / Manan (Salary Recs)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 7 — Antoine's salary rec approach is approved*\n"
                "> Economic model, no ML needed. Uses internal growth data month-over-month. "
                "Growth rate calculation needs one fix: calculate by *industry x metro*, not just industry "
                "(metro table likely already exists via MSA field in a hiring script).\n\n"
                "*Decision 8 — Engineering starts NOW, no data platform dependency*\n"
                "> Izzy can begin today. Nelson's DB of 50K role mappings covers the first 26-role iteration. "
                "Regex to strip numbers from role strings, then join to Nelson's table. "
                "Rami to meet Izzy and hand off the zip file + JSON structure context.\n"
                "> *Why this is huge:* You have been waiting on data platform capacity for weeks. "
                "The workaround is real — ship faster, validate the concept, then productionize properly.\n\n"
                "*Decision 9 — Role rec DP requirements are approved; DS/DP friction is being managed*\n"
                "> Shamir signed off. Rami is managing Kana on DP capacity. "
                "You nudging Paul directly is the right move — different voice, different urgency signal.\n\n"
                "*Decision 10 — Job description A/B experiment design finalized*\n"
                "> Control: current job description. Treatment: LLM-rewritten. "
                "Evaluated by a second LLM 'verifier' trained on what a strong Indeed post looks like. "
                "Primary metric: Indeed applications. Must retain original prompt alongside new one to run the A/B.\n"
                "> *Timeline:* Role and salary recs release next sprint, then ~2-4 weeks of data collection before talent pool sprint.\n\n"
                "*Decision 11 — Friday pairing session with Rami locked*\n"
                "> Rami brings sample JD outputs, you build evaluation criteria together. "
                "This is the session where the experiment design gets pressure-tested."
            ),
        },
    },
    {"type": "divider"},
    # ── MEETING 4 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*11:15 AM — Lookahead (Applicant Flow Sprint)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 12 — Culinary Agents feed is ready to enable*\n"
                "> Integration tested today. 15-second backend response time confirmed as backend-only — "
                "no impact to applicant experience. Ray is negotiating pricing with their CEO right now. "
                "Once pricing lands, flip the switch.\n\n"
                "*Decision 13 — SEO workstream split into two parallel tracks*\n"
                "> ~66K job pages live but only ~15.5K indexed. "
                "Two distinct problems: (a) job description metadata quality and (b) actual page indexing. "
                "Carlo pulled Google Search Console data and is being brought into the SEO team meeting this afternoon. "
                "These need to be owned and tracked separately.\n\n"
                "*Decision 14 — Reactivate + Copy jobs on track; JD optimization likely next sprint*\n"
                "> Reactivate: state machine transitions wrapping up, on track for end of sprint. "
                "Copy jobs: ~half a day of work remaining, on track. "
                "JD A/B test (Rami's DS work): pulled to next sprint — right call given salary recs is the priority.\n\n"
                "*Decision 15 — Indeed source claiming: short-term fix + long-term uniqueness approach locked*\n"
                "> *Root cause confirmed:* Franchise customers (e.g. Scooters Coffee) share identical source names "
                "— Indeed flags jobs as duplicates.\n"
                "> *Short-term:* Jatin updates Scooters Coffee source name to a unique variant to unblock their jobs.\n"
                "> *Long-term:* Append a unique identifier (location, number, or hash) to every source name company-wide. "
                "No more one-off carve-outs. Simpler code. Protects all franchises proactively. "
                "Jatin + Izzy to sync post-call on the scalable approach.\n\n"
                "*Decision 16 — FFH account setup flow: 50/50 split traffic*\n"
                "> Half of FFH customers get the full account setup (Ugo's work). "
                "Half see a 'Connect Indeed' to-do prompt. "
                "3LO token storage is already built. Goal: validate that FFH customers understand Indeed's value "
                "and will complete account setup. Reminder optimization is phase 2.\n\n"
                "*Decision 17 — Source claiming post-3LO: three paths available*\n"
                "> Self-serve (customer calls Indeed rep), click-to-call back (ring group API — trivial to build), "
                "or email template (Indeed accepts email; exploring auto-populating Gmail draft). "
                "Plus a nudge/reminder if 3LO connected but source not yet claimed.\n\n"
                "*Decision 18 — Closed jobs: read-only view + Reactivate as primary CTA + 30-day Renew*\n"
                "> OEMs can now see job content on closed jobs without having to copy the job. "
                "Reactivate replaces the buried three-dot menu flow. "
                "Renew extends expiry by 30 days — future: proactive email nudge before expiry with one-click renewal.\n\n"
                "*Decision 19 — Wage optimization experiment design confirmed*\n"
                "> Data: below market = 26% chance of 20+ apps; at market = 33.5%; above market = 38-39%. "
                "Rami finishing DS work, targeting customers with below-market wages. "
                "Surface wage intelligence inline in job post flow: 'increasing wage to $X raises your "
                "chance of 20+ applicants by Y%.' Same approach Antoine used on the marketing site."
            ),
        },
    },
    {"type": "divider"},
    # ── ACTION ITEMS ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items — Prioritized*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 — Do Today/Tomorrow*\n"
                ":red_circle: Message Paul directly about role recommendation DP progress "
                "(different voice = different urgency; Rami is managing Kana separately)\n"
                ":red_circle: Assess customer WTP for $100/interview Instawork pricing "
                "— talk to 2-3 line cook hirers before reconnecting with Ashwin\n"
                ":red_circle: *Approve Ugu's backend PR* for in-product OEM setup call prompts "
                "— this is still sitting unreviewed and unblocks a P0 feature\n"
                ":red_circle: *Carlo Harness/OpenSpec* — 5 days overdue from Jul 10 deadline. "
                "Get a status today. This cannot slip further.\n\n"
                "*P1 — This Week*\n"
                ":large_yellow_circle: Reconnect with Ashwin (Instawork) once you have the WTP read\n"
                ":large_yellow_circle: Friday pairing session with Rami — be ready to build JD evaluation criteria\n"
                ":large_yellow_circle: Confirm Carlo is looped into SEO team meeting (and aware of both workstreams)\n"
                ":large_yellow_circle: Review Fadi's close job / view details designs — "
                "confirm closed job empty state needs updating\n"
                ":large_yellow_circle: Confirm Culinary Agents pricing outcome from Ray's noon call — "
                "if locked, schedule feed enablement\n"
                ":large_yellow_circle: Message Jatin + Izzy to confirm sync on scalable source name uniqueness approach\n\n"
                "*P2 — Keep on Radar*\n"
                ":white_circle: Talent pool sprint: 2-4 weeks out once salary + role recs ship\n"
                ":white_circle: Abby ownership area — still needs to be clear by end of this week (Week 2)\n"
                ":white_circle: Dana succession planning — ~10 weeks remain before she leaves\n"
                ":white_circle: Boost purchase bug — still no owner; two reporters, revenue-impacting"
            ),
        },
    },
    {"type": "divider"},
    # ── WATCH LIST ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Watch List*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":fire: *V1 to V2 Cutover* — 5 days out (Jul 20). "
                "Dana investigating the 200+ unexpected trial spike. "
                "Monitor screener gap + star/fav gap post-cutover.\n"
                ":fire: *Carlo Harness/OpenSpec* — OVERDUE Jul 10. 5 days no confirmation. Escalate today.\n"
                ":warning: *Salary recs* — Izzy starts now; Rami hands off context. "
                "Data platform requirement doc due Thursday. Antoine source code location TBD.\n"
                ":warning: *Instawork* — Fresh opportunity. High upside for line cook problem. "
                "Do the WTP research fast while momentum is hot.\n"
                ":warning: *Ugu backend PR* — Still needs your approval. Unblocks OEM setup call prompts P0.\n"
                ":warning: *Culinary Agents* — Feed ready; waiting on Ray pricing call outcome.\n"
                ":warning: *SEO indexing gap* — 66K pages live, 15.5K indexed. "
                "Significant organic applicant volume sitting on the table.\n"
                ":white_check_mark: *Reactivate + Copy jobs* — On track for end of sprint. No action needed.\n"
                ":white_check_mark: *Indeed source claiming* — Scooters Coffee fix in Jatin's hands. "
                "Scalable approach: Jatin + Izzy syncing."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Bottom line:* Today was a momentum day. "
                "Salary recs went from 'blocked on data platform' to 'Izzy starts tomorrow' — "
                "that is a massive unlock. The Instawork partnership is the most interesting new bet "
                "you have seen in months for the line cook problem. "
                "Keep the Carlo pressure on, get Ugu's PR done, and you are set up for a strong Wednesday. "
                "You are doing great. :muscle:"
            ),
        },
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Digest — July 15, 2026",
    "blocks": blocks,
}


def preview():
    msg = "\n=== SLACK PREVIEW (no token) ===\n"
    for b in blocks:
        if b.get("type") == "header":
            msg += "\n## " + b["text"]["text"] + "\n"
        elif b.get("type") == "section" and "text" in b:
            msg += b["text"]["text"] + "\n"
        elif b.get("type") == "divider":
            msg += "\n---\n"
    sys.stdout.buffer.write(msg.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + TOKEN,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully.")
            else:
                print("Slack API error:", body.get("error"))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error sending to Slack:", e)
        sys.exit(1)


if TOKEN:
    send()
else:
    print("No SLACK_TOKEN found — printing preview.")
    preview()
