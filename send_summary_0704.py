#!/usr/bin/env python3
"""Daily decision digest — July 4, 2026 (Holiday Edition).

Cron: midnight UTC Jul 5 = 5pm PDT Jul 4 (July 4th holiday).
No meetings today (Manan is off). Week-in-review of Jun 29-Jul 2 +
Monday battle plan for Abby's first day (Jul 7).
"""

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
            "text": "Happy 4th of July, Manan! :fireworks: Your Weekly Debrief",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "You crushed it this week. No meetings today — you earned a real day off :sunglasses:\n"
                "Here's everything that mattered from *Jun 29 – Jul 2* "
                "and your battle plan for Monday (Abby's first day!)."
            ),
        },
    },
    {"type": "divider"},

    # ── BIG STORY ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:rotating_light: The Big Story of the Week*\n"
                "Copy Jobs is *dead*. Reactivate is now the *only* path forward — and you made that call "
                "decisively after Ray alignment. Indeed flags reposted jobs as duplicates requiring sponsorship; "
                "reactivation keeps the same job ID and sidesteps the flag entirely.\n\n"
                "This was the right call. ~50% of copied jobs were getting 0 applicants by D5/D30 anyway."
            ),
        },
    },
    {"type": "divider"},

    # ── 22 DECISIONS ───────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:brain: 22 Decisions Made This Week (across 8 meetings)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:knife: Copy Jobs & Reactivation (Jul 1-2)*\n"
                "1. *Copy Job KILLED* — Indeed duplicate-flags copies; no workaround exists\n"
                "2. *Reactivate = only path* — same job ID, no duplicate flag, works across boards\n"
                "3. *Logic:* auto-approve if no edits; back in review if edited post-reactivation\n"
                "4. *Syndication:* reactivation must push to ALL boards — FB Jobs, Talroo, ZipRecruiter\n"
                "5. *Simultaneous ship:* copy removal + reactivate must go live together (Carlo: blocker in Linear)\n"
                "   _Rationale: removing copy jobs without reactivation leaves OEMs stranded_"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:building_construction: Product Architecture (Jul 1-2)*\n"
                "6. *Job Requisition concept* — group hiring rounds under one role WITHOUT new job IDs\n"
                "   _Solves the applicant-bucket problem; no LinkedIn Easy Apply regression_\n"
                "7. *Auto-reactivation at Day 29* — Tanner confirmed buildable; auto-reactivates OEM's behalf\n"
                "8. *Facebook Jobs:* skip backfill, net-new only — Tanner to turn on\n"
                "   _Rationale: backfill creates noise and potential duplicate risk_"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:bar_chart: Job Post Recommendations (Jul 2)*\n"
                "9. *3 recommendation areas:* role titles, salary, job description optimization\n"
                "10. *Modal UX:* blocking, dark overlay, no X, after 'Next' on job desc page, 2-4s wait\n"
                "    _Copy: 'this may take a couple of seconds' — sets expectations_\n"
                "11. *Launch as experiment* with traffic throttle — not just a kill switch (Carlo adding to AC)\n"
                "12. *DS timeline:* role rec agent committed Jul 3; salary rec end of next week (known spill risk)\n"
                "    _Action: confirm role rec agent actually shipped before standing down_"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:email: Transactional Email & Sourcing (Jul 2)*\n"
                "13. *Email trigger* changed to 'under 5 by D3' (was: 0 by D1 / under 15 by D5) — Tanner owns\n"
                "    _Charmaine is out 2 months; Tanner absorbed her SendGrid work_\n"
                "14. *Team self-assigns sprint work* — not top-down (Martin's recommendation, adopted)\n"
                "15. *Design gaps:* go to project channel directly, don't wait on Cindy"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:handshake: Source Claiming & OEM Onboarding (Jun 29-30)*\n"
                "16. *3LO excluded* from current test — keep experiment clean, single variable\n"
                "17. *Source claiming = priority #1* in OEM success calls (above calendar + job desc)\n"
                "18. *Call script locked:* 'personal recruiter / success framing' — not 'do you have an Indeed account?'\n"
                "19. *Two-phase OEM onboarding:* SMS/email outreach first, then in-product to-do\n"
                "20. *Calendly:* in-product modal embed (dismisses on confirmed booking, not on close)\n"
                "21. *Resume-inclusive matching* rolling out — 100%+ higher accept/advance rate — no more A/B needed\n"
                "22. *'Personal Recruiter' retired* → go all-in on *'Homebase Advantage'* framing\n"
                "    _Also: Command AI officially dead_"
            ),
        },
    },
    {"type": "divider"},

    # ── URGENT ITEMS ───────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:rotating_light: Do Not Ignore These Over the Weekend*\n\n"
                ":fire: *Boost Purchase Bug* — 2 reporters in 2 days can't buy boosts. "
                "Matan tagged you. This is revenue-impacting. If Matan hasn't resolved, "
                "it's your first Slack message Monday morning.\n\n"
                ":fire: *ZipRecruiter Spend* — Burned $2K in 1.5 days with zero job-level caps. "
                "If no one paused this, they may have burned another ~$2-3K over the 4-day holiday weekend. "
                "Check the account first thing Monday — if it's still running uncapped, pause immediately.\n\n"
                ":fire: *Rami's Email Blast* — Due EOD Jun 25. Now ~10 days overdue. "
                "Needs a firm answer Monday: shipped or scrapped?"
            ),
        },
    },
    {"type": "divider"},

    # ── MONDAY BATTLE PLAN ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:calendar: Monday Jul 7 Battle Plan — Abby's First Day!*\n\n"
                "Welcome Abby to the team :tada: — PM with an engineering background. "
                "Monday is about setting her up for success while clearing your own backlog."
            ),
        },
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*:one: Triage First*\n"
                    "• Boost bug — resolved by Matan?\n"
                    "• ZipRecruiter — pause or cap spend NOW\n"
                    "• Rami email blast — ship or kill decision\n"
                    "• Role rec agent — confirm DS shipped Jul 3"
                ),
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*:two: Abby Onboarding*\n"
                    "• Context doc: Q3 goals, Reactivate pivot, OEM motion\n"
                    "• Walk through: what Copy Jobs was, why killed, what Reactivate does\n"
                    "• Intro to Matan, Tanner, Ugu, Carlo\n"
                    "• Share the 'Homebase Advantage' framing doc"
                ),
            },
        ],
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*:three: Your Action Items*\n"
                    "• Analyze reactivation applicant discount (CDC table, Databricks + Claude Code)\n"
                    "• Run Claude Code on Indeed Oct 1 policy page\n"
                    "• Follow up Ivana on Ashby reactivation test\n"
                    "• ZipRecruiter: find job-level caps or pause\n"
                    "• Send final call script to Sean + Calendly link"
                ),
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*:four: Specs to Draft*\n"
                    "• Reactivation UX (applicant expectation-setting)\n"
                    "• Job Requisition concept (owner: Tanner?)\n"
                    "• Auto-reactivation Day 29 opt-out UX\n"
                    "• Gaming-detection: close → reactivate time windows\n"
                    "• Q3 goals doc v3 (3-bucket; share with Ray before John)"
                ),
            },
        ],
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": (
                    "*:five: Team Check-Ins*\n"
                    "• Tanner: FB Jobs net-new live? SendGrid trigger done?\n"
                    "• Carlo: experiment AC for role recs? Linear blocker logged?\n"
                    "• Ugu: account setup UI review-ready (was targeting Jul 3)\n"
                    "• Ivana: Ashby reactivation test started?\n"
                    "• Izzy: unblocked when Culinary Agents respond"
                ),
            },
            {
                "type": "mrkdwn",
                "text": (
                    "*:six: Comms & Misc*\n"
                    "• Modal copy → Ted (hiring onboarding)\n"
                    "• Follow up Jenna on SEO indexing guidance\n"
                    "• Decide comms agent ownership (take or leave with Dana/Fadi/Davi)\n"
                    "• Confirm Rami blast status (very overdue)\n"
                    "• Note: Dana leaving end of September — Ray knows"
                ),
            },
        ],
    },
    {"type": "divider"},

    # ── METRICS SNAPSHOT ───────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:chart_with_upwards_trend: Key Metrics Snapshot*\n"
                "• Healthy job rate: *30%* of ICP jobs (target: 80%) — this is the number\n"
                "• OEM boost rate: *1.64%* of jobs (boosted jobs: ~50% healthy vs 26% unboosted)\n"
                "• FFH jobs w/ zero Indeed applicants on D5: *41%* (target: <10%)\n"
                "• ARR: *$650K+* (up from $450K in Jan 2026) :fire:\n"
                "• Resume matching variant: *100%+ higher* accept/advance rate — ship it\n"
                "• Trial volume: just broke *700K* :tada:\n"
                "• Boost click-to-purchase: *23%* | Post-job modal conversion: *15%*"
            ),
        },
    },
    {"type": "divider"},

    # ── CLOSER ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*The Bottom Line*\n\n"
                "You made a hard call killing Copy Jobs, you aligned with Ray fast, "
                "and you locked the Reactivate path before going on holiday. That's the move. "
                "The team has clear direction heading into Monday.\n\n"
                "Abby joining on Monday is a real asset — engineering PM on a team "
                "that's shipping hard technical infra right now. Set her up well and she'll multiply your output.\n\n"
                "Enjoy the fireworks tonight. You've earned it. :sparkler:\n\n"
                "_— Your Chief of Staff_"
            ),
        },
    },
]

payload = {"channel": CHANNEL, "blocks": blocks, "unfurl_links": False}


def preview():
    print("=" * 72)
    print("DAILY DIGEST PREVIEW — Jul 4, 2026 (Holiday Edition)")
    print("=" * 72)
    for b in blocks:
        t = b.get("type", "")
        if t == "header":
            sys.stdout.buffer.write(
                ("\n### " + b["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif t == "section":
            txt = b.get("text", {}).get("text", "")
            if txt:
                sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
            for f in b.get("fields", []):
                sys.stdout.buffer.write(
                    (f.get("text", "") + "\n").encode("utf-8", errors="replace")
                )
        elif t == "divider":
            sys.stdout.buffer.write(("-" * 60 + "\n").encode("utf-8", errors="replace"))
    print("=" * 72)


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
            if body.get("ok"):
                print(f"Slack message sent! ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if not TOKEN:
        print("No Slack token found — printing preview instead.\n")
        preview()
        print(
            "\nTo send for real: set SLACK_TOKEN (or SLACK_BOT_TOKEN / SLACK_API_TOKEN) "
            "in Cursor Dashboard > Cloud Agents > Secrets."
        )
        sys.exit(0)
    send()
