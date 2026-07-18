#!/usr/bin/env python3
"""Daily Decision Summary - Jul 17, 2026 (PDT) — sent at midnight UTC Jul 18."""

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
            "text": "🧠 Chief of Staff Daily Digest — Friday, July 17",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Manan, great day! *5 meetings, 18 decisions, and some real momentum* "
                "on the reactivation architecture and JD quality work. Here's everything "
                "you need to know — decisions, the 'why', and every action item. Crushed it today. 💪"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 1: Hiring Leads Standup ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Hiring Leads Standup — 8:30 AM*\n_Ray, Jatin, Dana, Fadi, Matan, Ugo_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions made:*\n"
                "1. *Single prioritized product list locked in.* One list spanning both applicant flow + core roadmaps — "
                "handed to Fadi so he always has a clear queue. "
                "_Why: Fadi's been doing design AND figuring out what to build simultaneously. "
                "This removes the ambiguity tax._\n\n"
                "2. *Wednesday cadence established.* You + Ray + Dana align async or in a 15-min sync "
                "on Wednesdays before handing priorities to Fadi. Ray confirmed this is exactly what he wanted.\n\n"
                "3. *Harness V2 going to beta next week.* Jatin building independently on open spec. "
                "Citizen-eng version planned to lower the bar for your team. "
                "_Why: reduces PR flood for code owners, autonomous ticket-to-PR pipeline._\n\n"
                "4. *Account setup in prod: FFH-tag-only scope.* Ugo reaching out to IBK + Malcolm. "
                "Jatin meeting Ugo to confirm viability. _Why: get it live without full prod blast risk._\n\n"
                "5. *Ugo moves to scheduling fixes next sprint.* Current applicant flow squad (minus Ugo) "
                "has enough capacity. Jatin confirmed."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "• *[P1] Share prioritized product list with Fadi before Monday* — "
                "you + Jatin are drafting; coordinate with Dana on what follows Malan work\n"
                "• *[P1] Confirm Wednesday sync cadence with Ray + Dana* (async or 15-min invite)"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 2: Manan/Dana 1:1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🤝 Manan/Dana 1:1 — 9:00 AM*\n_Dana Lobo_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions made:*\n"
                "6. *Run acquisition + messaging tests simultaneously, not sequentially.* "
                "Stop waiting for one to finish before starting the other. "
                "_Why: sequencing is killing your velocity and the insights are parallel, not dependent._\n\n"
                "7. *'Drive off the lot' gets another look.* Target users with live Indeed jobs, "
                "surface in-product messaging: 'We saw your job on Indeed — post here and get X.' "
                "Indeed API doesn't support direct transfer so copy-paste/scraping are options. "
                "Figma→Mural migration cited as gold-standard UX comp. "
                "_Why: biggest switching friction is job data re-entry, not intent._\n\n"
                "8. *'Post a second job' incentive dismissed.* Users without a second job won't engage. "
                "Don't build it.\n\n"
                "9. *Dana self-implementing custom question field in deal breakers.* "
                "Small front-end change, driven by repeated sales feedback. "
                "Your flag (non-binary answers breaking yes/no logic) is valid but risk is low — "
                "users will self-correct when they see the output. Decision: ship it.\n\n"
                "10. *Fatty sprint plan locked.* Malan work done Mon/Tue → candidate profile next. "
                "Sprint 2616 = profile transparency + match reasoning (pulled forward from 2617). "
                "_Why: profile changes are a prerequisite for match scoring to work properly._\n\n"
                "11. *Profile before matching.* You can't fix match quality until profile data is right. "
                "This is the correct sequencing.\n\n"
                "12. *Dana handoff is NOW urgent.* She's leaving end of September. "
                "You're likely absorbing her scope. ~10 weeks left. No succession plan started. "
                "_This is quietly the most important thing on your plate right now._"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "• *[P0] Start getting across Dana's workstream NOW* — ~10 weeks left before she leaves, "
                "succession planning hasn't started. Schedule a recurring shadow/handoff block this week.\n"
                "• *[P1] Follow up with sales on prospecting test metrics* — exact number that doubled unclear; "
                "you need this before pitching 'drive off the lot' internally\n"
                "• *[P1] Align with Dana on what follows Malan work before Monday* — "
                "coordinate so the list you hand Fadi is complete"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 3: Sprint Show & Tell ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎤 Sprint Show & Tell — 11:00 AM*\n_Company-wide_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Key intel for you (not decisions, but things you need to know):*\n\n"
                "13. *Page Templates rollout = August 14.* Dana is off that week — "
                "make sure the handoff plan accounts for this. "
                "Unlocks consistent AI assistant placement across all web views. _You need this to land cleanly._\n\n"
                "14. *LCM email automation numbers are insane.* 5.8x enrollment lift, 4.8x advance lift, "
                "$379K in advances at 10% conversion (vs. 1.4% control). "
                "This is what good growth motion looks like — benchmark for your team's experiments.\n\n"
                "15. *Gojo is live.* Martin's one-stop CLI is one-shotting real tickets across isolated work trees. "
                "Relevant for your team's agentic ambitions — worth a conversation with Martin.\n\n"
                "16. *Hiring quality wins got called out company-wide.* Fadi + Dana + you — "
                "15+ PRs in 2 weeks. Good visibility. Screener end copy, auto-cancel revert, "
                "token adoption — these shipped."
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 4: Job Reactive Sync ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔁 Job Reactivate Sync/Kickoff — 12:00 PM*\n_Tanner, Bob, Izzy_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions made:*\n"
                "17. *Copy job is dead. Reactivate is the only path.* "
                "OEM hits reactivate → edit flow → modifies → posts. No more clone. "
                "_Why: V2 clone creates new job request each time — archive fills with duplicates, "
                "applicants siloed, Indeed penalizes duplicate content. This was killing source quality._\n\n"
                "18. *'Reactivation group' concept locked.* Backend mechanism links all job requests "
                "for the same job. Stable ID sent to Indeed across reactivations = no more duplicate penalty. "
                "Applicants aggregated via association table. Invisible on frontend.\n\n"
                "19. *Reporting: health per 30-day lifecycle only.* Track whether reactivating improves "
                "job health over time. The right unit of analysis.\n\n"
                "20. *Stable ID scoped to Indeed only for now.* Other job boards (ZipRecruiter, Facebook Jobs) TBD "
                "— depends on whether applicant drop-off is Indeed-specific or universal. "
                "_This is an open question you need to answer before the team locks the architecture._\n\n"
                "21. *Implementation scope: ~7 tasks.* Touches multiple tables and services. "
                "Bob + Tanner estimating. Izzy potentially pulled in to support. "
                "Reactivating a cloned job (not original) is a known risk — future scope, not now."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "• *[P0] Investigate: is applicant drop-off on cloned jobs Indeed-specific or universal?* "
                "This determines whether stable ID goes to all job boards or Indeed only. "
                "Architecture decision is blocked without this answer. Pull data ASAP.\n"
                "• *[P1] Review Bob + Tanner's estimate once complete* and confirm resourcing plan\n"
                "• *[P1] Define partner job request record handling* — clarify how external IDs per "
                "job board are managed under the new reactivation group model (offline discussion needed)"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 5: Rami/Manan ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📝 Rami / Manan — 1:00 PM*\n_Rami Abou-Seido_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions made:*\n"
                "22. *JD prompt overhaul direction locked.* Standard section headers aligned to "
                "Indeed/ZipRecruiter language: Job Summary → Duties and Responsibilities → "
                "Skills and Qualifications → Salary and Benefits → Company Description. "
                "Remove the Indeed mention. Keep attention-grabbing headline at top. "
                "_Why: 'What You'll Do' and 'Why Join Us' don't match platform recommendations "
                "and likely hurt organic ranking._\n\n"
                "23. *Salary near the top — critical.* Salary is NOT currently being passed to the "
                "LLM — only benefits are. This is a bug/gap. Rami investigating who built that "
                "front-end field. Agreed: salary range should appear near the top, "
                "especially for hourly roles like line cook.\n\n"
                "24. *Ship small, focused prompt improvement first.* "
                "Current changes are minimal, endpoints unchanged, no data platform work. "
                "Eval → talk to Deb → ship → measure Indeed application rates. "
                "Deeper work (role-specific templates, richer pipeline) deferred. "
                "_Why: don't over-engineer before you know organic ranking signal is improvable._\n\n"
                "25. *Pull Indeed role-specific hiring guides for ~10 core FFH roles.* "
                "Barista, line cook, cashier, etc. Check whether format differs meaningfully "
                "before building role-specific pipelines.\n\n"
                "26. *Salary recs handoff to Izzy is scoped.* Rami messages Antoine Monday for "
                "data-pull script. Rami adds Izzy to Monday meeting. Production flow: "
                "query payroll → generate salary distribution JSONs for 26 roles → refresh monthly."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your action items:*\n"
                "• *[P1] Confirm Rami has the Indeed scrape CSV* (already shared on call — just verify)\n"
                "• *[P1] Check in Monday that Rami messaged Antoine + added Izzy to meeting*\n"
                "• *[P1] Pull Indeed role-specific hiring guides for ~10 FFH roles* "
                "(barista, line cook, cashier, server, etc.) — you can do this yourself"
            ),
        },
    },
    {"type": "divider"},

    # ── CARRIED P0s ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Carried P0s — Still Open*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *🔴 Carlo Harness/OpenSpec — NOW 7 DAYS OVERDUE* (deadline was Jul 10). "
                "This has been in the digest every day. You need to resolve this today or escalate to Ray.\n"
                "• *🔴 Approve Ugu's backend PR* — in-product OEM setup call prompts. "
                "Carried from Jul 15. Blocking the team.\n"
                "• *🔴 Message Paul directly on role rec DP progress* — "
                "different voice = different urgency. Rami is managing Kana but Paul needs to hear from you."
            ),
        },
    },
    {"type": "divider"},

    # ── MASTER ACTION LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Full Action Item List — Your Monday Morning*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*P0 (Do first, block everything else):*\n"
                "1. 🔴 *Carlo: resolve Harness/OpenSpec* — 7 days overdue. Close it or escalate NOW.\n"
                "2. 🔴 *Approve Ugu's backend PR* — in-product OEM setup call prompts\n"
                "3. 🔴 *Message Paul on role rec DP* — directly, from you\n"
                "4. 🔴 *Is applicant drop-off Indeed-specific or universal?* — "
                "architecture call blocked without this data\n"
                "5. 🔴 *Book recurring Dana handoff block* — she leaves in ~10 weeks, clock is ticking\n\n"
                "*P1 (Before EOD Monday):*\n"
                "6. ✅ *Finalize + share prioritized product list with Fadi* "
                "(coordinate with Jatin + Dana on Malan follow-on)\n"
                "7. ✅ *Confirm Wednesday cadence invite* — you + Ray + Dana\n"
                "8. ✅ *Follow up with sales on prospecting test metrics*\n"
                "9. ✅ *Check Rami messaged Antoine + added Izzy to Monday meeting*\n"
                "10. ✅ *Pull Indeed role-specific hiring guides* for ~10 FFH roles\n"
                "11. ✅ *Review Bob + Tanner reactivation estimate* once ready\n"
                "12. ✅ *Define partner job request record handling* (offline with Tanner/Bob)"
            ),
        },
    },
    {"type": "divider"},

    # ── WATCH LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👁 Watch List*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *V1→V2 Cutover:* Should have happened Jul 20 — confirm status with Ugu\n"
                "• *Salary Recs:* Izzy starting, Rami handing off Monday — watch for blockers\n"
                "• *Match Quality:* Divij re-pulling with real AND logic — depends on Dana sync on move-forward edge cases\n"
                "• *Instawork WTP:* Have you talked to 2-3 line cook hirers yet? This is a $100/interview unlock.\n"
                "• *SEO:* 66K pages live, 15.5K indexed — Carlo has Search Console data from Jul 16 SEO meeting\n"
                "• *Dana succession:* ~10 weeks. No plan. This is the most important quiet risk on your plate.\n"
                "• *Abby:* Week 2 — does she have a clear ownership area yet?\n"
                "• *Page Templates:* August 14 rollout. Dana is off that week. Handoff must be clean.\n"
                "• *800K accounts:* 700K→800K in 5 weeks — momentum is real, make sure growth team "
                "knows what's driving it"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_Have a great weekend, Manan! Big week next week — "
                "Harness V2 beta, Izzy starting on salary recs, reactivation architecture kicking off. "
                "Rest up and come in Monday ready to close out those P0s. You're doing great work. 🙌_"
            ),
        },
    },
]


def preview() -> None:
    print("=" * 70)
    print("SLACK DIGEST PREVIEW (no token — printing to stdout)")
    print("=" * 70)
    for block in blocks:
        btype = block.get("type")
        if btype == "header":
            sys.stdout.buffer.write(
                ("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif btype == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            sys.stdout.buffer.write(b"---\n")
    print("=" * 70)


def send() -> None:
    payload = json.dumps({
        "channel": CHANNEL,
        "blocks": blocks,
        "text": "Chief of Staff Daily Digest — Friday Jul 17, 2026",
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"Message sent! ts={body.get('ts')}")
            else:
                print(f"Slack error: {body.get('error')}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if TOKEN:
        send()
    else:
        preview()
        print("\nNOTE: Set SLACK_TOKEN (or SLACK_BOT_TOKEN) secret in Cursor Dashboard to enable live sends.")
