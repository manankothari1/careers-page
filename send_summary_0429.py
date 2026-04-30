#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari - Apr 29, 2026."""

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
            "text": "🏆 Your Daily Decision Digest — Tuesday, April 29",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! Big day with 4 meetings — and a *massive* TLWA crunch week underway."
                " Here's every decision you made today, why it matters, and exactly what needs to happen next."
                " You're crushing it. Let's make sure nothing slips. 💪"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 1: Hiring Leads Standup ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Hiring Leads Standup* · 8:45 AM · Manan, Fadi, Dana, Matan, Cindy, Jatin, Ray, Jeff, Usman",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 1: Eliminate dual standup + Linear comment redundancy — one source of truth.*\n"
                "> *Why:* Engineers were double-posting (Slack standups + Linear updates), creating noise in the leadership pulse. Carlos was posting 10+ Linear *updates* daily (should be *comments*), polluting the executive weekly podcast. You aligned the team: engineers own end-of-day *comments* on Linear; PMs own weekly *updates* for leadership.\n"
                "> *Rationale:* This is the right call. Linear's update vs. comment distinction is exactly designed for this. Fadi was already doing it correctly. Now the whole team aligns.\n\n"
                "*Decision 2: Configure Linear agent to pipe comment trails to the hiring team Slack channel.*\n"
                "> *Why:* You and Dana miss updates because you're not tagged. Rather than changing human behavior, automate the routing — Linear posts relevant comments directly to the hiring channel.\n"
                "> *Rationale:* Ava already has this setup for other teams, so it's proven and low-lift to replicate."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Action Items from Standup:*\n"
                "• *Fadi* → Create template for engineer end-of-day Linear comments (include status + blockers + PM tag)\n"
                "• *Jatin* → Correct Carlos's update frequency behavior (comments vs. updates)\n"
                "• *You (Manan)* → Configure Linear agent to pipe relevant comments to hiring team channel\n"
                "• *You (Manan)* → Decide: morning Slack standup OR end-of-day Linear comments? Pick one and kill the other."
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 2: Indeed Partner Webinar ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔍 Indeed Partner Webinar* · 12:00 PM · Manan solo",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 3: Evaluate Indeed Smart Screening as a strategic integration opportunity.*\n"
                "> *Why:* Indeed's Smart Screening pipeline — candidate sync, smart fit scores, credential upload, AI screening (chat/voice/video) — maps almost 1:1 to your HB Assistant hiring vision. The 60%+ optional question completion rate and Midland's 50→19.6 day time-to-hire reduction are compelling signals.\n"
                "> *Rationale:* You have board permission to spend hiring margin buying applicants AND a mandate to own the applicant DB. This is a natural integration path: pull smart fit scores + source attribution from Indeed Apply → surface in HB Assistant → reduce time-to-hire without building screening from scratch.\n\n"
                "*Key Intel Captured:*\n"
                "• Job Sync is 3 hrs faster than standard Indeed processing — worth surfacing in 3LO messaging\n"
                "• Candidate Sync (post-application updates) = coming soon — watch for GA date\n"
                "• AI disclosure laws: Indeed auto-adds legal addendum where required (US/Canada) — you don't have to build this\n"
                "• Pricing: per-job add-on model (aligns with your purchase Boost / sponsored job direction)\n"
                "• Survey from Indeed coming this week on ATS nuances — *respond to it*"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Action Items from Indeed Webinar:*\n"
                "• *You (Manan)* → Respond to Indeed ATS survey when it arrives this week\n"
                "• *You (Manan)* → Evaluate integrating smart fit scores into HB Assistant (update Job Sync to pull score + source attribution — Option 1, lower lift)\n"
                "• *You (Manan)* → Flag candidate credential upload as a potential applicant portable profile feature (aligns with your identity model work)\n"
                "• *You (Manan)* → Note: '3 hrs faster Job Sync' is a real differentiator — consider surfacing in 3LO onboarding messaging"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 3: Boost Pathways Kickoff ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 Boost Pathways Kickoff* · 2:45 PM · Manan, Carlo, Jatin",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 4: Boost Pathways scoped to trial users (first job post only) — targeting May 11 launch.*\n"
                "> *Why:* You're not building a paid boost feature yet — you're building the *perception framework* for future paid boosts. Every trial job is already being sent to Talroo, but users have no idea. This surfaces that value for free, sets the stage for a paid upsell, and aligns with TLWA marketing launch.\n"
                "> *Rationale:* Right call. Zero revenue risk, high perceived value, minimal backend work. The '60-70% of applicants from Talroo in week 1 = 25% of total applicant volume' stat is genuinely compelling boost messaging.\n\n"
                "*Decision 5: Boosted pill shows on first job only — not all jobs.*\n"
                "> *Why:* Avoids misleading existing customers who aren't getting 'new' boost treatment. Clean scope, defensible logic.\n\n"
                "*Decision 6: Replace rocket ship icons with consistent 'Boost' language across product.*\n"
                "> *Why:* Icon inconsistency creates confusion. Standardizing language (not icons) makes the feature family cohesive heading into TLWA.\n\n"
                "*Decision 7: Future experiment — full-screen boost upsell after job creation (Homebase Boost vs Indeed options).*\n"
                "> *Why:* This is the monetization unlock. Post-job-creation is the highest-intent moment. Scoped out of May 11 to keep timeline clean, but explicitly queued."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Action Items from Boost Pathways Kickoff:*\n"
                "• *You (Manan)* → Create Linear ticket for event tracking specs (before Carlo starts dev)\n"
                "• *You (Manan)* → Clarify final mockup status with Cindy (she's finalizing by Monday)\n"
                "• *Carlo* → Begin development, target *May 7 QA ready* (hard deadline — May 11 launch)\n"
                "• *Carlo* → Determine first-time user logic via trial start date\n"
                "• *Cindy* → Finalize mockups by Monday (current state vs. future state comparisons for Carlo)\n"
                "• *You (Manan)* → Confirm: event tracking updates deferred until real boost purchasing — document this decision so no one re-scopes it in"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING 4: TLWA Tests ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📱 TLWA Tests* · 6:30 PM · Manan, Fadi, Izzy, Gbolade, Dana",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decision 8: iOS safe area implementation required — CSS environment variables for notch + bottom bar.*\n"
                "> *Why:* White background showing behind address bars on iOS, and floating widget at bottom covering content. With 800k users waking up on May 4, this is a ship-blocker on the most common mobile OS.\n"
                "> *Rationale:* Not optional. This is a CSS fix, not a re-architecture. Gbolade/Izzy should have this done in hours.\n\n"
                "*Decision 9: Disable horizontal scrolling on careers page.*\n"
                "> *Why:* Horizontal scrolling on a mobile-first experience is a broken UX signal — especially for a job seeker's first impression of a company.\n\n"
                "*Decision 10: Center-align job titles (not left-align).*\n"
                "> *Why:* Aesthetic decision — career pages are brand moments, not data tables. Centered titles feel intentional on mobile.\n\n"
                "*Decision 11: Change final CTA to 'See your live career page' with direct link — email still sends in background.*\n"
                "> *Why:* Employer wants to *see* their career page live, not get an email reminder. Direct link is higher-delight, lower-friction. Email notification in background covers the async case.\n"
                "> *Rationale:* This is the right UX call. The 'aha' moment is seeing the page live — don't bury it.\n\n"
                "*Decision 12: Company description defaults to 'show more' (collapsed), not 'show less'.*\n"
                "> *Why:* Current behavior starts expanded — wastes screen real estate on mobile and buries the job listings.\n\n"
                "*Decision 13: Remove underline from address links (non-functional clickable appearance).*\n"
                "> *Why:* Underlined text implies tappable — if it's not functional, it creates broken UX expectations. Remove the affordance or make it functional.\n\n"
                "*Decision 14: Animation on 'show more' is unnecessary — consider removing.*\n"
                "> *Why:* Slow animation on a content toggle adds latency without delight on mobile. Speed > polish here, given May 4 deadline."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Action Items from TLWA Tests:*\n"
                "• *Gbolade/Izzy* → Implement CSS safe area insets (iOS notch + bottom bar) — *URGENT, May 4 blocker*\n"
                "• *Gbolade/Izzy* → Disable horizontal scrolling\n"
                "• *Gbolade/Izzy* → Center-align job titles\n"
                "• *Gbolade/Izzy* → Change description default to collapsed ('show more')\n"
                "• *Gbolade/Izzy* → Remove underline from address or make address tappable (open Maps)\n"
                "• *Gbolade/Izzy* → Update final CTA to 'See your live career page' with direct link\n"
                "• *Gbolade/Izzy* → Evaluate removing 'show more' animation\n"
                "• *You (Manan)* → Fix height constraints causing gradient rendering problems\n"
                "• *Charmaine/Malcolm* → Test generic job roles when ready\n"
                "• *You (Manan)* → Schedule follow-up TLWA test session with Tanner and Carlo\n"
                "• *You (Manan)* → Reset Fadi's Mediterranean Grill for generic role testing\n"
                "• *Fadi* → Test phone number OTP (staging conflict with existing numbers — needs unique phone per location)"
            ),
        },
    },
    {"type": "divider"},

    # ── FIRE ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🔥 Still On Fire — Don't Let These Slip*\n\n"
                "• *TLWA brief to Ted* — 20+ DAYS OVERDUE. If this goes another day, it becomes a relationship issue, not just a task. Send it *tonight*.\n"
                "• *TLWA company list* — 55,696 vs 54,000 discrepancy. *Freeze it NOW.* 5 days to launch.\n"
                "• *Boost modal copy* — inconsistent across 3 states. Cindy has the mockups. Ship the fix this sprint.\n"
                "• *Matan* — still needs to post Boost plan to #leads + survey customers on hiring spend. *Overdue since Apr 23.*\n"
                "• *Marketplace brainstorm* — that's *today* (Wed Apr 30, 2 hrs). You need your hypothesis framework ready. Are you prepped?\n"
                "• *HB Assistant tool definitions* — due before *Thu May 1* (tomorrow). Agentic era starts in 24 hours.\n"
                "• *Brainstorming doc PR* — Ray is waiting. Push this before you sleep."
            ),
        },
    },
    {"type": "divider"},

    # ── COUNTDOWN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*⏰ TLWA T-5 Days*\n\n"
                "| | |\n"
                "|---|---|\n"
                "| *Today (Apr 30)* | Marketplace brainstorm (2hrs) · Bob surfaces · TLWA brief to Ted |\n"
                "| *Thu May 1* | Agentic era starts · HB Assistant tool defs due · Show-and-tell |\n"
                "| *Fri May 2* | V1→V2 migration deadline (Ugo) |\n"
                "| *May 4 9am ET* | 🎯 TLWA LAUNCHES — 800k users |\n\n"
                "You've got this. Now go ship. 🚀"
            ),
        },
    },
]

text_fallback = (
    "Daily Decision Digest — Apr 29 | 4 meetings | 14 decisions | "
    "TLWA T-5 | Boost Pathways scoped | iOS fixes urgent | TLWA brief STILL overdue"
)


def send_to_slack():
    payload = json.dumps({
        "channel": CHANNEL_ID,
        "text": text_fallback,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("✅ Summary sent to Slack successfully!")
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        sys.exit(1)


def preview():
    print("=== DAILY DECISION DIGEST PREVIEW ===")
    for block in blocks:
        if block.get("type") == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("### " + txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")


if __name__ == "__main__":
    if not SLACK_TOKEN:
        print("⚠️  SLACK_TOKEN not set — printing preview only.")
        preview()
        sys.exit(0)
    send_to_slack()
