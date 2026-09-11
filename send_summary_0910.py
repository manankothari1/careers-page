#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Sep 10, 2026 (PDT)
4 meetings: Malcolm 1:1, Mitratech BG Screen, TalentReef/Indeed, Fadi/Manan Reactivate
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
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Digest — Thursday, Sep 10 :briefcase:",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Day Grade: A-* | 4 meetings, 3 external partnerships scoped, 1 major product decision locked.\n*Theme: REACTIVATE FLOW LOCKED · BG CHECK DEEP-DIVE · INDEED ARCHITECTURE CLARIFIED · FRAUD OWNERSHIP CRYSTALLIZED*",
        },
    },
    {"type": "divider"},
    # ─── MEETING 1 ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:alarm_clock: 8:30am — Manan / Malcolm (Observability Dashboard)*\n"
            + "Quick 1:1. Scoped a single dashboard split into *OEM flow* vs *Applicant flow*, following the user journey chronologically. Agreed on stacked bar charts per source (success vs. error), dotted baseline anomaly lines, and collapsible sections. Screener steps collapsed into one chart; latency tracked for direct Homebase submissions only.\n"
            + "_Malcolm_ to ping you once the draft is updated.",
        },
    },
    {"type": "divider"},
    # ─── MEETING 2 ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mag: 10:30am — Homebase x Mitratech BG Screen Process Review*\n"
            + "Deep-dive with Courtney, Jacqui, and Chris (Mitratech) on background check integration gaps.\n\n"
            + "*Key issues surfaced:*\n"
            + "• :money_with_wings: Billing/refund gap — Homebase charges upfront but gets no visibility if applicant never completes the check. Webhook requested from Chris (going to Sabrina).\n"
            + "• :inbox_tray: Bulk submission not yet supported via the integration. Chris checking with Sabrina.\n"
            + "• :office: KYB friction root cause FOUND — Homebase sends *DBA name*, not legal entity name. Mitratech matches against SoS records → mismatch = vetting failure. Likely hits non-payroll customers hardest. Same-day activation once correct legal name is on file.\n"
            + "• :red_circle: Failed vets tracked in a shared Google Sheet — no programmatic callback yet. You flagged interest in automation.\n"
            + "• :robot_face: Sierra (AI support) integration: not ready on Mitratech side. Target: EOY.\n"
            + "• :mailbox: BG screen support email ≠ Slack. Chris to send correct address.",
        },
    },
    {"type": "divider"},
    # ─── MEETING 3 ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:speech_balloon: 11:00am — TalentReef/Homebase Discussion on Indeed (w/ Ray)*\n"
            + "Explored routing Homebase's Indeed feed through TalentReef (Mitratech gold-tier ATS partner) to reduce friction.\n\n"
            + "*Decision: TalentReef routing NOT the path forward.* Still on XML feed (not Job Sync API), sponsorship still requires separate employer credit card through TalentReef's portal, and single-source rule complexity adds a third system for shared clients. Core pain points unresolved.\n\n"
            + "*Key Indeed rules learned (gold knowledge):*\n"
            + "• Single-source rule: all jobs must flow through ONE ATS; two ATSs requires employer to declare source of truth to Indeed directly\n"
            + "• :warning: Reposting without disposing candidates from prior posting = flagging trigger\n"
            + "• Making job inactive then reactivating without candidate action = flagging trigger\n"
            + "• Evergreen postings: organic for ~30 days, then must be sponsored\n"
            + "• Candidate disposition is critical: final state required before repost; recommend 7-day gap between same-role reposts\n"
            + "• Gold-tier = better roadmap visibility, NOT preferential rules treatment\n\n"
            + "_Josh_ to send Indeed best-practices co-authored article (Indeed signed off on it).",
        },
    },
    {"type": "divider"},
    # ─── MEETING 4 ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:arrows_counterclockwise: 12:30pm — Fadi/Manan: Reactivate Flow + Fraud*\n"
            + "Big one. Locked the reactivate decision tree, advanced fraud model strategy, and aligned on trust/safety ownership.\n\n"
            + "*:white_check_mark: REACTIVATE FLOW — LOCKED*\n"
            + "• Default expiry: *30 days* (not 120; 120 = hard max a job can stay open)\n"
            + "• 90-day threshold: reuse same Job Post ID + Reference ID if under 90 days\n"
            + "• 21-day rule: if reopening same role, must wait 21 days since prior posting (Indeed organic visibility)\n"
            + "• Decision tree: Made a hire + want same role?\n"
            + "  → Under 90 days: keep open, extend 30 days, same IDs\n"
            + "  → 21+ days: new Job Post ID, keep Reference ID\n"
            + "• UX: *Option A chosen* — opinionated modal ('you are hiring, here's what we suggest') over open-ended prompts\n"
            + "• Copy: 'Stay visible on partner job boards' / 'Maintain job visibility on partner boards'\n"
            + "• All ID logic handled silently on backend\n\n"
            + "*:brain: FRAUD LLM V4*\n"
            + "• V3 (Paria, August): evaluated ~1,200 labeled jobs, strong accuracy improvement. Miss: Paria made inclusion decisions without full cross-team input.\n"
            + "• V4: 22 new Indeed-guided categories + larger labeled dataset\n"
            + "• *You're reaching out to Indeed today for 'known bad' jobs list* — strongest training signal available\n\n"
            + "*:bar_chart: COMPANY-LEVEL RISK SCORE (Laura's team)*\n"
            + "• 0–1 scale, 1–2 month timeline\n"
            + "• Combines Salesforce signals, Databricks signals, external web scraping (not full KYB vendor)\n"
            + "• Future flow: Company risk score → Hiring-specific layer → Auto-approve or manual review queue → ECE executes\n\n"
            + "*:clipboard: OWNERSHIP ALIGNED (provisional):*\n"
            + "• LLM (job fraud): Product + DS owns; T&S consults\n"
            + "• Company risk score: T&S builds; Product sets eligibility thresholds\n"
            + "• Hiring signals: Product owns; T&S consults\n"
            + "• Manual review: ECE executes; T&S owns quality + training\n"
            + "• Skye = final decision-maker; Laura to loop Skye in after aligning with you first",
        },
    },
    {"type": "divider"},
    # ─── DECISIONS MADE ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: DECISIONS MADE TODAY*\n\n"
            + "1. *Reactivate flow logic LOCKED* — 30-day default, 90-day ID reuse threshold, 21-day gap rule, Option A UX modal. Ship it.\n"
            + "2. *TalentReef routing REJECTED* — Adds friction, doesn't solve core Job Sync API pain. Stay direct with Indeed.\n"
            + "3. *Observability dashboard architecture AGREED* — Single dashboard, two sections, chronological user journey, stacked bar charts.\n"
            + "4. *Fraud ownership model ALIGNED (provisional)* — Product owns LLM + hiring signals; T&S owns risk score build + manual review quality.\n"
            + "5. *Indeed 'known bad' list outreach — initiated* — You're reaching out today. Strongest V4 training signal.",
        },
    },
    {"type": "divider"},
    # ─── YOUR ACTION ITEMS ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rocket: YOUR ACTION ITEMS (Today's meetings)*\n\n"
            + ":one: *Send reactivate flow to Skye, then Jessica* — Share FigJam with updated logic. Loop Skye first before external send.\n"
            + ":two: *Confirm 120-day hard limit with Jessica* — Ask: can a job be extended past day 120, or is 90 days the true renewal cutoff?\n"
            + ":three: *Check how Indeed captures outside-pool hires* — Job Sync API or Disposition Sync API? Critical for the decision tree.\n"
            + ":four: *Reach out to Indeed for 'known bad' jobs list* — V4 fraud model training data. Best signal available.\n"
            + ":five: *Get on Juan's Databricks tool walkthrough* — Laura adding you to Skye's invite. Confirm you're on it.\n"
            + ":six: *Review Indeed best practices article* — Josh (Mitratech) sending via Slack. Read and share with team.\n"
            + ":seven: *Chase Mitratech for KYB fix path* — DBA vs. legal entity name is causing vetting failures. Get the employer setup guide from Chris (due tomorrow).",
        },
    },
    {"type": "divider"},
    # ─── OVERDUE / CRITICAL ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: OVERDUE / STILL CRITICAL — Don't Let These Slip*\n\n"
            + ":fire: *Indeed feed SUSPENDED — Day 17.* Fraud package (Manan + Divij: cleanup + score + OTP) → Jessica. Where are you on this?\n"
            + ":fire: *Departures signal docs — 7 DAYS OVERDUE* (was Sep 4). Conflict docs + data → Zane, Sean, Jon W, Bobby. NOT mentioned today. Needs to happen first thing tomorrow.\n"
            + ":fire: *Marina / Mundo Academy* — Follow-up target was TODAY. Not mentioned in any meeting. Send tonight or first thing tomorrow.\n"
            + ":fire: *Reshare Linear with Divij* — Recency + distance experiments. Target was Sep 9, hard deadline Sep 10 = TODAY. LCM email target Sep 10 is already past. Do this NOW.\n"
            + ":warning: *EarnIn/Ernan* — Promised follow-up yesterday AND today. Still unaddressed. Iszael's source attribution is blocked. 3rd day in a row.\n"
            + ":warning: *IBK JD A/B signal* — 3+ weeks overdue. Pull before V2 widens the data.\n"
            + ":warning: *OTP retest* — Gbolade should be pinging you post-fixes. Don't wait — check in proactively.\n"
            + ":warning: *Google careers page indexing* — Target was TODAY (~66K live, ~15.5K indexed). Did this happen?\n"
            + ":warning: *Top Match Databricks query update* — Manan to update (join hiring_applicant_summaries, match_score >= 0.5). Check Soheil backfill status.\n"
            + ":warning: *Skye's deck* — Received Sep 8. Still unreviewed. She's your Head of Product. Do it tomorrow.",
        },
    },
    {"type": "divider"},
    # ─── INBOUNDS TO WATCH ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: INBOUNDS EXPECTED — Watch For These*\n\n"
            + "• *Chris (Mitratech)*: Employer setup guide + happy-path SLA + correct support email (due tomorrow)\n"
            + "• *Josh (Mitratech)*: Indeed best practices co-authored article (Slack)\n"
            + "• *Laura*: Hiring-specific signals list + provisional ownership write-up\n"
            + "• *Gbolade*: OTP retest ping post-3 fixes\n"
            + "• *Malcolm*: Updated observability dashboard link",
        },
    },
    {"type": "divider"},
    # ─── CONTEXT & GRADE ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Context: Last day of Heads Down Week before normal cadence resumes next week.*\n"
            + "Tomorrow (Sep 11) heads down week ends. Dreamforce WFH optional next week (Sep 14-18). *Skye's Toronto trip ~Sep 14-17* — get alignment before she travels.\n\n"
            + ":trophy: *Day Grade: A-* — Hugely productive on partnerships and architecture. The reactivate flow decision is a real product unlock. The fraud ownership alignment sets you up for a clean Indeed conversation. The only drag: critical overdue items still unaddressed for the 2nd/3rd consecutive day. Tomorrow matters.\n\n"
            + "_You had a strong day, Manan. The reactivate flow decision alone will unblock a lot. Now chase those overdue items — you know what needs to happen. :muscle:_",
        },
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Digest — Sep 10, 2026",
    "blocks": blocks,
}


def preview():
    msg = "\n=== SLACK DIGEST PREVIEW (no token — would send to D06E4QMHCNN) ===\n"
    msg += "Day Grade: A-\n"
    msg += "Theme: REACTIVATE FLOW LOCKED · BG CHECK DEEP-DIVE · INDEED ARCHITECTURE CLARIFIED · FRAUD OWNERSHIP CRYSTALLIZED\n"
    msg += "4 meetings: Malcolm 1:1 (8:30am), Mitratech BG Screen (10:30am), TalentReef/Indeed (11am), Fadi/Manan Reactivate (12:30pm)\n"
    msg += "\nKEY DECISIONS:\n"
    msg += "  1. Reactivate flow LOCKED (30d default, 90d ID threshold, 21d gap, Option A modal)\n"
    msg += "  2. TalentReef routing REJECTED\n"
    msg += "  3. Observability dashboard architecture AGREED\n"
    msg += "  4. Fraud ownership aligned (provisional)\n"
    msg += "  5. Indeed known-bad list outreach initiated\n"
    msg += "\nYOUR ACTIONS (new):\n"
    msg += "  1. Send reactivate flow to Skye then Jessica (FigJam)\n"
    msg += "  2. Confirm 120-day hard limit with Jessica\n"
    msg += "  3. Clarify how Indeed captures outside-pool hires\n"
    msg += "  4. Reach out to Indeed for known-bad jobs list\n"
    msg += "  5. Get on Juan Databricks walkthrough invite\n"
    msg += "  6. Review Indeed best practices article (Josh)\n"
    msg += "  7. Chase Mitratech KYB fix / employer setup guide\n"
    msg += "\nOVERDUE CRITICAL:\n"
    msg += "  - Indeed feed suspended DAY 17\n"
    msg += "  - Departures signal docs 7 DAYS OVERDUE\n"
    msg += "  - Marina/Mundo Academy (was today)\n"
    msg += "  - Reshare Linear with Divij (was today)\n"
    msg += "  - EarnIn/Ernan (3rd day unaddressed)\n"
    msg += "  - IBK JD A/B signal (3+ weeks overdue)\n"
    msg += "\n=== END PREVIEW ===\n"
    sys.stdout.buffer.write(msg.encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
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
                print(f"Sent to Slack OK — ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')} — {body}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        sys.exit(1)


if not TOKEN:
    preview()
else:
    send()
