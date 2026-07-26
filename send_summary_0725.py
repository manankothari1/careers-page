#!/usr/bin/env python3
"""Saturday Jul 25 Week-in-Review + Monday Battle Plan for Manan Kothari."""
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
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🏊 Saturday Wrap + Monday Battle Plan — Week of Jul 21-25",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Happy Saturday, Manan! Hope the pool party was everything 🥂 "
                "No meetings today — you earned it. But Monday's coming in hot with SBA launching, "
                "so here's your full week-in-review and what you need to walk in ready for.\n\n"
                "*This was a big week. A LOT got locked. Let's recap.*"
            ),
        },
    },
    {"type": "divider"},
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
                "*1. Email Route — LOCKED* (Jul 22-23)\n"
                "> Callback/Calendly both dead. Pre-populated mailto is the primary CTA for hiring outreach. "
                "User clicks, email opens with Homebase CC'd and account details included. "
                "Gmail/Outlook/Apple Mail dropdown.\n"
                "> *Why:* Lower friction, no 3-way call logistics, no TalkDesk dependency (Kio on vacation anyway), "
                "aligns with long-term email-first direction.\n"
                "> *Owner:* Fadi on UX; Matan + Carla + Ray all aligned.\n"
                "> *Action:* Confirm Fadi finalized the UX post-standup Jul 23 — buttons outside dropdown, "
                "separate screen for 'email them'."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Source Claiming = 'Sending a Letter' — LOCKED* (Jul 23)\n"
                "> New framing: instead of 'we scraped your job,' it's 'we noticed you're hiring and sent a letter.' "
                "Warm, personal, not creepy.\n"
                "> *Why:* Removes perceived coldness of AI-driven outreach. Differentiates vs. every other tool.\n"
                "> *Owner:* Fadi building, Carla + Matan looped in, Ray endorsed.\n"
                "> *Action:* Make sure copy reflects this framing when reviewing Fadi's work."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. FFH Experiment: Option 1 — LOCKED* (Jul 21)\n"
                "> Broad demographic: food, drink, dining, hospitality + in trial. API activation trigger (not pre-signup). "
                "No backfilling. Carlo + Ugo = ONE unified experiment (analytics clarity).\n"
                "> *Why:* Avoid locking in a narrow FFH definition that'll change. Easier to filter down than invent retroactively.\n"
                "> *Owner:* Carlo (experiment), Ugo (account setup PR).\n"
                "> *Action:* Carlo 14+ days overdue — experiment setup should be 1-2 hours of work. Must address Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. JD Quality Experiment — LOCKED* (Jul 21)\n"
                "> 50/50 split on job description generator. Ratings = #1 signal (6K vs 300 avg for top vs bottom line cook listings). "
                "Formatting = #2 (Rami verifying manually). Logos = future (requires Indeed employer graph API). "
                "Sponsorship is NOT the lever — high-rated non-sponsored beats low-rated sponsored.\n"
                "> *Why:* Line cook at 7% healthy rate. D5 zero-applicant at 41% vs Q3 target of <10%. JD quality is the fastest unlock.\n"
                "> *Owner:* Tanner builds experiment; Rami to ping Manan when updated prompt is ready.\n"
                "> *Action:* Check if Rami sent the prompt this week. Loop Tanner to kick off immediately if so."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. SBA Onboarding Architecture — LOCKED → SHIPS MONDAY* (Jul 22-24)\n"
                "> Two-flag arch (modal_seen + sba_entered). No cooldown. No hard reset date. "
                "Pulsing icon V1 (border animation, stops on SBA entry). "
                "Tooltip auto-shows next session after modal dismissed. 'Don't show me again' option. "
                "Jumpstart drawer suppressed when modal shown. Subsequent SBA click goes straight to SBA. "
                "Roles usage = default in roster.\n"
                "> *Why:* Full team alignment; SBA Go/No-Go on Jul 24 was green.\n"
                "> *Owner:* Gurkiran leading. Ships Monday Jul 27.\n"
                "> *⚠️ WATCH:* Unassigned grid feedback was overwhelmingly negative in friendly user testing. "
                "Watch P1 data closely Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Archived Job Redirect — LOCKED* (Jul 24)\n"
                "> Short-term: all archived job links redirect to careers page. "
                "If company has active jobs → careers page. If no active jobs → custom 'this role is no longer open' landing page (next sprint). "
                "Catch-all redirect + logging (Jatin's idea, Ray endorsed). Ray's principle: NEVER land on sign-in page.\n"
                "> *Why:* Archived job links currently dump users on the sign-in page — dead end, trust-destroying.\n"
                "> *Owner:* Manan (PR), Jatin (logging).\n"
                "> *Action:* Is the PR up? Confirm status Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Inline Compliance Check During Job Creation — LOCKED* (Jul 24)\n"
                "> Extend the in-progress 'reviewing your job post' feature to surface syndication flags "
                "(contact info in description, etc.) BEFORE the user hits Post Job. "
                "Jobs arrive at Michael/Juan's queue clean → auto-approved quickly → syndicate immediately.\n"
                "> *Why:* Kills the root cause of 117 CX chats in 30 days. "
                "Michael/Juan approve in <1hr but jobs still sit — worker/pipeline pickup delay. "
                "Compliance catch during creation removes the human bottleneck.\n"
                "> *Owner:* Manan scoping, to investigate pipeline delay with Jatin.\n"
                "> *Action:* Review Sierra hiring transcripts to map issue categories (fraud/syndication/applicant/misc)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Manager Comms Inclusion — LOCKED* (Jul 24)\n"
                "> Include managers in email cohorts, filter low-usage owners. Focus messaging on active managers — they feel the hiring pain, "
                "owners don't. Usman flagged Salesforce inconsistency (managers listed as owners in some accounts).\n"
                "> *Why:* Current comms hit owners only; wrong audience for FFH pain.\n"
                "> *Owner:* Matan building cohorts; Dana looped in for FFH filter.\n"
                "> *Action:* Did you review Matan's comms doc this weekend? Sonia is blocked without it."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9. Data Platform Process — LOCKED* (Jul 21)\n"
                "> Named DP contact assigned to hiring team. That person joins team meetings when DP work is in scope. "
                "Tasks scoped into sprint planning. Manan goes direct with Paul + Kanchana (not through Ted/Rami).\n"
                "> *Why:* Role rec work stalled repeatedly on DP capacity. "
                "New process gives visibility and accountability.\n"
                "> *Action:* Check that DP assignee has been named. If not, ping Paul + Kanchana directly Monday."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10. FFH Frame Shift — Validated* (Jul 22)\n"
                "> Dana's 4 blockers validated: normalized pain, switching cost, wrong timing, trust gap. "
                "Product is currently reactive (triggered by pain) — opportunity to be always-on, proactive. "
                "3 test buckets for John: (1) Indeed job scrape + 1-click repost, (2) trigger-based outreach (Usman's signals model), "
                "(3) candidate-first experience.\n"
                "> *Owner:* Dana presenting to John. Usman running candidate email experiment.\n"
                "> *Action:* Check Usman experiment results — was running as of Jul 23."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 MONDAY BATTLE PLAN (Jul 27)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 — Non-negotiable before lunch:*\n\n"
                ":red_circle: *Carlo — 14+ DAYS OVERDUE.* Harness/OpenSpec is a management issue at this point. "
                "Have a direct conversation. This can't slip another week.\n\n"
                ":red_circle: *SBA launches today — watch closely.* "
                "Pull Gurkiran for a same-day check-in. Unassigned grid was negative in testing. "
                "If you see bad P1 signal, you want to know by EOD.\n\n"
                ":red_circle: *422 errors — Day 16.* Check in with Jatin on RCA status. "
                "146 locations affected since Jul 9. If still unresolved, escalate to Ray.\n\n"
                ":red_circle: *Matan comms doc.* If you haven't reviewed it, do it first thing. "
                "Sonia is blocked and every day of delay is a day of pipeline delay.\n\n"
                "*P1 — Get these done by EOD:*\n\n"
                ":large_yellow_circle: *Usman experiment results.* Check what the candidate email data is showing. "
                "This feeds directly into the John check-in narrative.\n\n"
                ":large_yellow_circle: *Juan Sanchez follow-up.* He's sending his own emails outside the proper flow. "
                "Small issue that snowballs if ignored.\n\n"
                ":large_yellow_circle: *Rami JD prompt check.* Confirm Rami sent the updated prompt from Thursday pairing. "
                "Loop Tanner to kick off the 50/50 experiment if ready.\n\n"
                ":large_yellow_circle: *DP named contact.* Confirm with Paul + Kanchana that a named assignee is set for hiring team DP work.\n\n"
                ":large_yellow_circle: *Sierra transcript review.* Map the 117 chat categories for the inline compliance check scope."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ WATCH LIST — Ongoing Risks*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":rotating_light: *Dana succession* — ~7 weeks until she's out. ZERO plan. "
                "Page Templates hand-off must start NOW. She's off Aug 7 week. This is your biggest quiet risk.\n\n"
                ":rotating_light: *422 Job Publishing Errors* — 146 locations, Day 16 on Monday. "
                "Jatin on RCA. If this isn't resolved this week, it becomes a customer-facing crisis.\n\n"
                ":warning: *SBA unassigned grid signal* — Friendly testing was overwhelmingly negative. "
                "Gurkiran launching anyway (good call), but watch P1 data hard.\n\n"
                ":warning: *JD Experiment kickoff* — Blocking on Rami's prompt + Tanner building infra. "
                "Don't let this stall another week.\n\n"
                ":warning: *Replica identity blocker (Izzy)* — Justin Lambert sign-off still needed. Push on this.\n\n"
                ":warning: *Backend resourcing* — Ray escalating FE→BE swap. ~2 months to hire. "
                "Don't block any critical Q3 path on this.\n\n"
                ":information_source: *Abby* — Week 7+. Still no clear ownership area. Needs to be resolved."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*📊 Q3 Scoreboard (as of Jul 24)*\n\n"
                "| Metric | Now | Target |\n"
                "|---|---|---|\n"
                "| FFH D5 zero-applicant rate | 41% | <10% |\n"
                "| Line cook jobs healthy (D30) | 7% | 50% |\n"
                "| Screener completions | baseline | +50% relative |\n"
                "| Healthy job rate (ICP) | 30% | 80% |\n\n"
                "_The gap is huge. JD experiment + reactivation + FFH outreach are the unlocks. "
                "Every week of delay on Carlo's experiment and the JD test is a week further behind._"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💬 Your Chief of Staff Says...*\n\n"
                "Manan, this was genuinely a great week of decision-making. You locked a TON — "
                "email route, source claiming, FFH experiment, JD experiment, SBA, archived jobs, inline compliance. "
                "These are real, meaningful product decisions that will move the needle.\n\n"
                "The thing I'd watch: *execution velocity on Monday*. "
                "SBA launching is a milestone, but the decisions mean nothing if Carlo's "
                "experiment is still sitting idle, the JD test hasn't kicked off, and Sonia can't build because Matan's doc wasn't reviewed. "
                "Monday is the unlock.\n\n"
                "You've got this. Enjoy the rest of the pool party 🌞"
            ),
        },
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Saturday Week-in-Review + Monday Battle Plan (Jul 25, 2026)",
    "blocks": blocks,
}


def preview():
    sys.stdout.buffer.write(
        "\n=== PREVIEW (no Slack token) ===\n".encode("utf-8", errors="replace")
    )
    for block in blocks:
        if block.get("type") == "section":
            text_obj = block.get("text", {})
            if text_obj:
                sys.stdout.buffer.write(
                    (text_obj.get("text", "") + "\n\n").encode("utf-8", errors="replace")
                )
        elif block.get("type") == "header":
            sys.stdout.buffer.write(
                ("## " + block["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
            )
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("---\n\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(
        "=== END PREVIEW ===\n".encode("utf-8", errors="replace")
    )


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print("Slack message sent successfully!")
            else:
                print(f"Slack API error: {result.get('error', 'unknown')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        sys.exit(1)


if not TOKEN:
    print("No Slack token found — printing preview.")
    preview()
else:
    send()
