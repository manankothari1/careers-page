#!/usr/bin/env python3
"""Daily Chief-of-Staff Slack digest — Tuesday Aug 4, 2026 (PDT)"""

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
            "text": "Chief of Staff Digest — Tuesday Aug 4 \U0001f4c8",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! \U0001f44b You crushed it today — 3 meetings, a locked sprint, "
                "and real strategic alignment with Matan. Here\u2019s your full rundown. \U0001f680"
            ),
        },
    },
    {"type": "divider"},
    # ── MEETINGS ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4c5 Today\u2019s Meetings (3)*\n"
                "• *9:30 AM* — Hiring Sprint Planning (Applicants) — Ugo, Tanner, Izzy, Jatin, Carlo\n"
                "• *12:00 PM* — Christofer / Manan — PJ\u2019s Coffee Indeed customer escalation\n"
                "• *3:30 PM* — Matan / Manan — Applicant funnel deep-dive + roadmap alignment"
            ),
        },
    },
    {"type": "divider"},
    # ── DECISIONS ─────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af Decisions Made Today — Your Calls*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Tap the Talent Pool scope \u2705 LOCKED*\n"
                "_What:_ Post-job-creation flow shows fake candidate profiles \u2192 invite-to-apply \u2192 Boost CTA. "
                "Chips removed; plain text only. Carlo leads starting *Monday*.\n"
                "_Why:_ Lowest-effort unlock for line cook D5 zero-applicant rate. Carlo is back from Canada \u2014 kick this off immediately."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Renew Jobs approach \u2705 CONFIRMED*\n"
                "_What:_ Timestamp-push approach (not close/repost). Tanner leads. Capacity opens end of week.\n"
                "_Why:_ Validated by Indeed Jul 29 \u2014 reposting triggers job-copy flag; timestamp push preserves ranking and avoids penalties."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Matching logic near-term fix \u2705 DECIDED*\n"
                "_What:_ If only one signal (screener OR resume), lower the threshold and apply ~0.6 weight instead of requiring both. Ships soon.\n"
                "_Why:_ Strong-resume candidates with no screener are being excluded from matches today \u2014 this fixes the false-negative problem without a full rebuild."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Matching philosophy \u2705 LOCKED \u2014 Absolute (population-level) scoring*\n"
                "_What:_ Score each competency against the full screener population, not just the current applicant pool. "
                "Present as % score (not binary match/no-match). Threshold = top 20% of population per competency.\n"
                "_Why:_ Relative scoring recommends the least-bad in a weak pool \u2014 not credible. "
                "Absolute scores are stable, don\u2019t shift with new applicants, and match how every major competitor presents ranking. "
                "This is the right north star."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Applicant-side priority order \u2705 LOCKED with Matan*\n"
                "1\ufe0f\u20e3 Trigger-based drip (terminations, role recs)\n"
                "2\ufe0f\u20e3 Matching score improvements (per-competency, population-level)\n"
                "3\ufe0f\u20e3 Comms experiments (timing-focused, FFH users only)\n"
                "4\ufe0f\u20e3 Talent pool outreach strategy\n"
                "5\ufe0f\u20e3 SEO / domain authority content\n"
                "_Why:_ Matan aligned on this stack ranking. Trigger-based drip is the highest-leverage unlock for "
                "D5 zero-applicant rate; everything else is sequenced behind it."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. PJ\u2019s Coffee (Yvonne) Indeed escalation \u2014 Christofer owns fallback*\n"
                "_What:_ Wait for hiring team response on admin repost flow. "
                "If no path confirmed \u2192 Christofer creates a new company entity on Indeed to restore job visibility.\n"
                "_Why:_ Expired 75-applicant job is admin-blocked (\u2018cannot activate from current state\u2019). "
                "New company entity is a known workaround that tricks Indeed into treating it as fresh inventory."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Multi-contributor project ownership \u2014 process reset*\n"
                "_What:_ One-project-one-owner pattern is reverting; Jatin is enforcing multi-contributor structure. "
                "Lead breaks work into tasks upfront; others contribute in parallel. "
                "Izzy gets a shared Linear board view for visibility.\n"
                "_Why:_ Solo ownership creates bottlenecks and hides progress. "
                "Consistent application unlocks velocity in a sprint where carryover is heavy."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Sprint process retro \u2014 set for Monday (Jatin)*\n"
                "_What:_ Full team retrospective on planning and multi-person execution.\n"
                "_Why:_ Pattern of solo ownership crept back in last sprint; retro is the mechanism to systematize the fix."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9. SEO content strategy \u2014 Tatiana scoping session to kick off*\n"
                "_What:_ Build domain authority around hiring topics (competitors: HireMe.com, TalentReef already doing this). "
                "Carrie recently left; Tatiana is the right person.\n"
                "_Why:_ SEO is a cost-effective top-of-funnel for applicant volume. "
                "66K pages live but only 15.5K indexed \u2014 indexing gap is a symptom; content authority is the cure."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10. Meta ads timing-targeting \u2014 validate before committing*\n"
                "_What:_ Hypothesis: Meta signals can surface when a user is actively hiring. "
                "Validate feasibility with Jenna before adding to experiments list.\n"
                "_Why:_ Users are desensitized to email/push/SMS. If Meta can target on hiring intent signals, "
                "it\u2019s a differentiated channel \u2014 but not worth planning around until feasibility is confirmed."
            ),
        },
    },
    {"type": "divider"},
    # ── ACTION ITEMS ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Your Action Items (Manan)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *[TODAY]* Forward Rami\u2019s blocked PR list to Jatin (Rami to DM you both)\n"
                "\u2022 *[TODAY]* Confirm admin repost path status for Yvonne/PJ\u2019s (check hiring team thread)\n"
                "\u2022 *[THIS WEEK]* Validate Meta ads timing-targeting feasibility with Jenna\n"
                "\u2022 *[THIS WEEK]* Set up scoping session with Tatiana on SEO content strategy\n"
                "\u2022 *[THIS WEEK]* Share combined product roadmap with Matan\n"
                "\u2022 *[THIS WEEK]* Align with Rushi on franchise work scope (sprint dependency?)\n"
                "\u2022 *[THIS WEEK]* Scope comms agent manual experiment (Jatin pushing; you\u2019re the decision-maker w/ Ray out)\n"
                "\u2022 *[THIS WEEK]* Make Rami business case to Ted directly (Ted pulling back after Kan departure)\n"
                "\u2022 *[URGENT: 8 days]* Dana succession \u2014 she returns Aug 10 with only 2 days left; Page Templates hand-off must start *now*"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u23f0 Team Action Items to Track*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *Carlo* \u2014 Break down Tap the Talent Pool issues into tasks (starts Monday)\n"
                "\u2022 *Jatin* \u2014 Set up Monday retro; help Izzy build shared Linear board view; message Ray directly on culinary agents legal\n"
                "\u2022 *Tanner* \u2014 Confirm salary recs endpoint w/ Rami; clarify JD optimization versioning today\n"
                "\u2022 *Izzy* \u2014 Message Tanner to test copy jobs rollout; reactivate jobs on staging by Thursday\n"
                "\u2022 *Ugu* \u2014 Sync with Carlo after sprint kickoff on Indeed account setup QA\n"
                "\u2022 *Christofer* \u2014 New company entity on Indeed for Yvonne if no admin repost path\n"
                "\u2022 *Matan* \u2014 Share experiments plan + spending proposals with Manan this week"
            ),
        },
    },
    {"type": "divider"},
    # ── WATCH LIST ────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 Watch List \u2014 Open Risks*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f525 *Dana succession: 8 days* \u2014 She\u2019s off this week, back Aug 10, last day Aug 12. "
                "Two working days to hand off. Page Templates ownership must be resolved THIS WEEK.\n"
                "\U0001f525 *422 errors: Day 26* \u2014 Jatin on RCA. Ray is out \u2014 you\u2019re the decision-maker.\n"
                "\U0001f525 *Fadi Boost modal Figma: ~8 days overdue* \u2014 Fadi is blocked on you. Needs to happen today.\n"
                "\u26a0\ufe0f *Culinary agents* \u2014 Still blocked on vendor legal agreement (Gray). Ray + CEO going back and forth. Can\u2019t unblock directly but monitor.\n"
                "\u26a0\ufe0f *Comms agent manual experiment* \u2014 Jatin is pushing hard. You own this call with Ray out. Sit with Jatin + Cena to surface assumptions first.\n"
                "\u26a0\ufe0f *Carlo + Talent Pool* \u2014 Good news: he\u2019s back and taking ownership Monday. Make sure kickoff happens.\n"
                "\u26a0\ufe0f *Rami (DS) involvement* \u2014 Ted pulling back. You need to make the business case directly this week. Don\u2019t let this slip.\n"
                "\u26a0\ufe0f *Scooters follow-up email* (Olivia/Maria/Lacey) \u2014 Still open\n"
                "\u26a0\ufe0f *Juan Sanchez* \u2014 Still sending outside proper flow. Follow up.\n"
                "\u26a0\ufe0f *Franchise ticket* \u2014 6+ days open. Align with Rushi this sprint."
            ),
        },
    },
    {"type": "divider"},
    # ── FUNNEL SNAPSHOT ───────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4ca Funnel Snapshot (from Matan sync)*\n"
                "Screener land: *~80%* \u2022 Screener start: *~56%* \u2022 Screener complete: *~80%*\n"
                "Real gaps: *match count* + *interview show-up/completion rate*\n"
                "Root cause of low applicants: *jobs not reaching Indeed* \u2014 not a conversion problem. "
                "Fix the pipe first, then optimize the funnel."
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
                "*\U0001f4aa Today in a word: Clarity.*\n\n"
                "You got alignment on matching philosophy, locked the sprint priorities, "
                "unblocked a customer escalation, and built a shared roadmap frame with Matan \u2014 "
                "all on the day Carlo got back from Canada. "
                "The team is more cohesive than it\u2019s been in weeks. "
                "Keep the Dana succession moving and you\u2019re set up beautifully. "
                "Get some rest \u2014 tomorrow\u2019s going to be a big one. \u2b50"
            ),
        },
    },
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Digest \u2014 Tue Aug 4, 2026",
    "unfurl_links": False,
    "unfurl_media": False,
}


def preview():
    sys.stdout.buffer.write(
        "\n=== PREVIEW (no SLACK_TOKEN found) ===\n".encode("utf-8", errors="replace")
    )
    for block in blocks:
        if block.get("type") == "header":
            txt = block["text"]["text"]
            sys.stdout.buffer.write(
                ("\n\n\u2588\u2588 " + txt + " \u2588\u2588\n").encode(
                    "utf-8", errors="replace"
                )
            )
        elif block.get("type") == "section":
            txt = block["text"].get("text", "")
            sys.stdout.buffer.write(
                (txt + "\n").encode("utf-8", errors="replace")
            )
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"\n" + b"-" * 60 + b"\n")
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")


if not TOKEN:
    preview()
    print("\nSLACK_TOKEN not set. Add it in Cursor Dashboard > Cloud Agents > Secrets.")
    sys.exit(0)

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
        body = json.loads(resp.read().decode("utf-8"))
        if body.get("ok"):
            print(f"Message sent successfully! ts={body.get('ts')}")
        else:
            print(f"Slack API error: {body.get('error')}")
            print(json.dumps(body, indent=2))
            sys.exit(1)
except urllib.error.URLError as exc:
    print(f"Network error: {exc}")
    sys.exit(1)
