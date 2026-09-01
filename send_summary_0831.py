#!/usr/bin/env python3
"""Daily Chief of Staff digest — Monday Aug 31, 2026 PDT"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN", "")

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Monday Aug 31 — End of Day Debrief", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Chief of Staff — Monday Aug 31, 2026*\n\n"
                "4 meetings today, and honestly — *really strong day.* The Indeed call alone "
                "was a major unlock. You went in with heat and came out with exactly what the team needed. "
                "Here's everything that happened and what needs to happen next."
            )
        }
    },
    {"type": "divider"},

    # BIG WINS BANNER
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*WINS OF THE DAY*\n"
                ":trophy: Corporate email domain requirement — *DROPPED ENTIRELY* (huge unblock for eng + customers)\n"
                ":trophy: Jessica Kanaskie (jkanaskie@indeed.com) = new direct T&S POC, replacing unfruitful David relationship\n"
                ":trophy: Homebase invited into Indeed's *source claiming automation pilot* (~2-3 weeks)\n"
                ":trophy: Fraud = confirmed root cause; reposting = NOT the structural problem (clearer path forward)\n"
                ":trophy: Talent Pool vision upgraded to *talent-first hiring* — big strategic shift locked with Fadi"
            )
        }
    },
    {"type": "divider"},

    # MTG 1: Indeed <> Homebase
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10:00 AM — Indeed <> Homebase* (w/ Jessica Kanaskie + Skye)\n\n"
                "*Decision 1: Corporate email domain enforcement — PAUSED INDEFINITELY*\n"
                "Why: Got significant pushback from ATS partners with SMB/franchise clients. "
                "Enforcement of 'all jobs must have an email' still moving forward. "
                "Official communication from Indeed expected mid-September.\n\n"
                "*Decision 2: Fraud is the only issue (not reposting)*\n"
                "FSA rule was triggered by fraud signals. Existing sources are unaffected — "
                "only net new sources require review. Review timeline: 2-3 weeks with proactive "
                "outreach, up to 3 months without it. Claimed sources get vetted faster.\n\n"
                "*Decision 3: New onboarding step locked — email Indeed CS within 5 days*\n"
                "Jessica will send a template. All new feed clients need to send it. "
                "Must be folded into the Homebase onboarding flow.\n\n"
                "*Decision 4: Job ID rules LOCKED*\n"
                "Reopen within 7 days of closing = reuse same job ID. "
                "After 7 days = new job ID is fine. "
                "Keep roles open up to 120 days. Updating expiration date is OK (don't change the job ID). "
                "Evergreen requisition IDs: not worth investing in now — Indeed says sponsor instead.\n\n"
                "*Decision 5: Source claiming automation pilot — Homebase IN*\n"
                "Jessica will connect you + Skye with David (Indeed Product) to test auto-claiming "
                "via source name / unique ID from the job sync API. Replaces the painful CS email process."
            )
        }
    },
    {"type": "divider"},

    # MTG 2: Skye / Manan 1:1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*11:00 AM — Skye / Manan 1:1 (Indeed + Data)*\n\n"
                "*Decision 6: Fraud mitigation comms strategy — send NOW, don't wait*\n"
                "Option 1 (send what's done now + follow-up in 2 weeks when OTP ships) vs. "
                "Option 2 (bundle everything). Leaning toward Option 1 to show Indeed continued momentum. "
                "Skye owns packaging it; you own sending the fraud notice email context to her.\n\n"
                "*Decision 7: OTP scope expansion under consideration*\n"
                "Current OTP only covers net new users. Proposed: retroactively verify existing free/trial "
                "accounts too. Paying customers are exempt (low fraud risk, high cost to add friction). "
                "Open issue: Stitch ties OTP to login email — may not match hiring profile email. "
                "This needs infra alignment before expanding scope.\n\n"
                "*Decision 8: Jessica (not David) is the go-forward relationship at Indeed*\n"
                "David has been largely unfruitful and no regular cadence exists. Jessica confirmed "
                "as direct POC for T&S and feed issues.\n\n"
                "*Data orientation wins for Skye:*\n"
                "- Hiring V2 Databricks dashboard = production data (ignore 'staging' label)\n"
                "- Key tables: hiring_job_requests, hiring_job_application, hiring_job_applicants\n"
                "- Genie (Databricks AI) for natural language queries\n"
                "- Claude Code setup: clone homebase-context repo + Databricks token"
            )
        }
    },
    {"type": "divider"},

    # MTG 3: Fadi / Manan Talent Pool
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1:00 PM — Fadi / Manan — Talent Pool*\n\n"
                "*Decision 9: Talent-first hiring model — ADOPTED as the vision*\n"
                "Flip the current model. Instead of OEM posting a job and waiting: "
                "surface pre-vetted candidates first, create job post as the vehicle to invite them. "
                "Goal: someone quits Tuesday, OEM is interviewing candidates the same day. "
                "You built a near-identical product at Suna (talent marketplace for photo shoot bookings). "
                "Key insight: applicant quality and volume is everything — OEM UI polish is secondary.\n\n"
                "*Decision 10: Experiment phases LOCKED*\n"
                "Phase 1 (validate job seeker willingness): reach out to ~1K existing talent pool users "
                "in a local MSA who completed a screener. Ask them to fill out a general profile. "
                "No payment needed yet — test organic willingness. Deliver relevant local jobs if they engage.\n"
                "Phase 2 (Fadi, by Sep 4): OEM attribute preference study — survey which candidate "
                "attributes (reliability, skills/work history, availability) drive interview outreach. "
                "Stack-rank + visual prototype reaction.\n"
                "Phase 3 (only after Phase 1 validates): referral mechanics + UGC/influencer test "
                "(~100 college students, $100 each to post about profile creation).\n\n"
                "*Decision 11: OTP re-verification scope revisited*\n"
                "Paying customers = auto-approved (no OTP). Free/trial accounts = trigger verification. "
                "Existing 2FA users = already verified, no action. Net new = already handled.\n\n"
                "*Decision 12: Fraud doc for Indeed — Manan owns drafting it*\n"
                "Cover: fraudulent business cleanup, fraud agent improvements, upcoming OTP work. "
                "This is the package Skye sends to Jessica for T&S review."
            )
        }
    },
    {"type": "divider"},

    # MTG 4: Jon / Matan / Manan
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3:00 PM — Jon / Matan / Manan (Roadmap + Intent Signals)*\n\n"
                "*Decision 13: Roadmap tooling — Matan's Vercel/Linear tool adopted*\n"
                "Responsive PNG with clickable Linear ticket links, auto-updates on date changes. "
                "You're updating the prompt: larger 'Now' section + color-coded by function. "
                "Target: ready by end of week for Matan to review.\n\n"
                "*Decision 14: Roy departed — Greg (VP Sales) absorbs his role*\n"
                "Roy's last day was Friday. No replacement planned. His Rev Ops remit had drifted "
                "toward Salesforce tooling and created exec friction. Matan meeting Greg next week "
                "to discuss how hiring sales fits the broader sales vision.\n\n"
                "*Decision 15: Intent signals — no productization yet, mockups first*\n"
                "Debate: Matan wants to productize sooner (scale learnings faster). "
                "Jon agrees in-product testing gets to stat-sig faster. "
                "Your counterpoint: need to establish what content/messaging works first before building. "
                "Settled on: Matan builds mockups (starting with overtime spend on dashboard) "
                "so there's something tangible to react to and scope. "
                "Jon to pull Personal Recruiter campaign data as the baseline comparison.\n\n"
                "*Decision 16: Productization trigger metrics DEFINED*\n"
                "Jon's proposal: connect rate, trial start rate, conversion to paid. "
                "Baseline = Dana's Personal Recruiter campaign (better apples-to-apples than TLWA).\n\n"
                "*Decision 17: Sales silos are a real gap — Matan to speak with Greg*\n"
                "Payroll, hiring, and other sales teams don't share learnings. "
                "Not about merging experimentation — monthly syncs and shared best practices. "
                "Analogy you made: Snowden/NSA newsboard — a central place for cross-functional learnings."
            )
        }
    },
    {"type": "divider"},

    # ACTION ITEMS — MANAN
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*YOUR ACTION ITEMS (Manan)*\n\n"
                ":red_circle: *[TODAY/OVERDUE] EarnIn sample feed* — Was due today (Aug 31 EOD). "
                "Send to jon.salzberg@earnin.com. XML/API format. 30M-download channel. Do not let this slip.\n\n"
                ":red_circle: *[1-2 days] Draft Indeed fraud remediation doc* — "
                "Cover: fraudulent biz cleanup, fraud agent improvements, upcoming OTP work. "
                "This goes to Skye who sends to Jessica for T&S progress check.\n\n"
                ":red_circle: *[ASAP] Send Skye the original Indeed fraud notice email* — "
                "She needs context on why OTP work started. Wasn't shared before today's call.\n\n"
                ":red_circle: *[ASAP] Send team recap of Indeed call* — "
                "Key points: no existing customers impacted, what's changing for new accounts, "
                "fraud mitigation plan, corporate email WIN.\n\n"
                ":large_yellow_circle: *[This week] Clarify OTP email display mechanics for existing users* — "
                "Does UI show which email OTP will be sent to? Login email vs. hiring profile email "
                "mismatch risk. Loop in infra.\n\n"
                ":large_yellow_circle: *[This week] Follow up with Jessica on whether review tickets can be Homebase-initiated* — "
                "Can Homebase automate the Indeed CS email on behalf of new customers, or must it come from them directly?\n\n"
                ":large_yellow_circle: *[This week] Research disposition sync API status* — "
                "Required for the 120-day job-open strategy (keep sending relevance signals to Indeed).\n\n"
                ":large_yellow_circle: *[End of week] Update roadmap prompt* — "
                "Larger 'Now' section + color-code by function. Give Matan something to review before Monday.\n\n"
                ":large_yellow_circle: *[This week] Send Skye git clone command for homebase-context repo* — "
                "Unblocks her Claude Code setup once GitHub access is approved.\n\n"
                ":large_yellow_circle: *[This week] Align with infra on OTP re-verification flow for existing trial users* — "
                "Fadi Talent Pool session surfaced this as a needed step before expanding scope.\n\n"
                ":large_yellow_circle: *[This week] Launch Phase 1 Talent Pool experiment* — "
                "Reach out to ~1K talent pool users in a local MSA who completed a screener. "
                "Test organic willingness to fill out a general profile.\n\n"
                ":white_circle: *[OVERDUE — still open] JD A/B experiment signal* — Pull from IBK. 2+ weeks running.\n"
                ":white_circle: *[OVERDUE — still open] Tanner onboarding doc* — Cited by Ray as a concrete leadership gap.\n"
                ":white_circle: *[OVERDUE — still open] Annual cancel policy post in Hiring Leads* — Reps still misaligned.\n"
                ":white_circle: *[OVERDUE — still open] Rami → Divij Databricks notebook handoff* — Was due today.\n"
                ":white_circle: *[Sep 10] Marina / Mundo Academy follow-up* — Warm prospect, not buying now (budget cuts)."
            )
        }
    },
    {"type": "divider"},

    # ACTION ITEMS — OTHERS
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*OTHERS' ACTION ITEMS (keep tabs on these)*\n\n"
                ":small_blue_diamond: *Skye* — Package + send fraud mitigation steps to Jessica (T&S progress check)\n"
                ":small_blue_diamond: *Skye* — Get GitHub access approved + Databricks token set up\n"
                ":small_blue_diamond: *Fadi* — OEM attribute preference study, by Sep 4 (which candidate attributes matter most)\n"
                ":small_blue_diamond: *Fadi* — Design low-lift job seeker profile experience prototype\n"
                ":small_blue_diamond: *Jon* — Draft ideal sales call POV + scorecard (Manan reviews once done)\n"
                ":small_blue_diamond: *Jon* — Pull Personal Recruiter campaign data as intent signal baseline; share prospecting lists with Usman\n"
                ":small_blue_diamond: *Matan* — Build mockups for intent signals in product (start: overtime spend on dashboard)\n"
                ":small_blue_diamond: *Matan* — Jon/Matan session tomorrow to review intent signal cadence + Usman's prospecting motions\n"
                ":small_blue_diamond: *Matan* — Meet with Greg (VP Sales) next week re: hiring sales vision\n"
                ":small_blue_diamond: *Jessica (Indeed)* — Send FSA CS email template + reposting best practices\n"
                ":small_blue_diamond: *Jessica (Indeed)* — Connect Manan + Skye with David (Indeed Product) for source claiming pilot"
            )
        }
    },
    {"type": "divider"},

    # CARRY-FORWARD WATCH LIST
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*WATCH LIST / CARRY-FORWARD*\n\n"
                ":rotating_light: *Indeed feed still suspended* — Day 7 tomorrow. "
                "FSA path forward is now clearer (fraud not reposting), but no guarantee on timeline. "
                "2-3 weeks minimum with proactive outreach to Jessica.\n"
                ":rotating_light: *Indeed corp domain deadline (Oct 31)* — "
                "Corporate email req paused but email address enforcement still moving. "
                "~55.5% of Hiring customers at risk. Doc the 4 options + share with Sky + Ray after today.\n"
                ":rotating_light: *422 Job Publishing Errors* — Day 51+, 146 locations. Jatin on RCA. Still open.\n"
                ":large_yellow_circle: *Android screener permissions bug* — Silent failures on mic/camera. File as bug.\n"
                ":large_yellow_circle: *Disposition sync API* — Required for 120-day job strategy. Check status this week.\n"
                ":large_yellow_circle: *Domain authority for @joinhomebase.com Talent Pool outreach* — Open blocker. "
                "Needs Sky + Ray + lifecycle marketing sign-off.\n"
                ":large_yellow_circle: *Talent Pool: Fadi designs (Resume Insights) + Izzy blocked* — "
                "Check in with Fadi on what he needs to feel supported."
            )
        }
    },
    {"type": "divider"},

    # CLOSING
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day grade: A-*\n\n"
                "Today was genuinely excellent. The Indeed call delivered more than expected — "
                "no corporate email req, a direct T&S contact, and a path into the source claiming pilot. "
                "Talent Pool vision got significantly sharper with Fadi. "
                "Deductions: EarnIn sample feed deadline (must confirm sent), "
                "three persistent overdue items still open (JD signal, Tanner doc, cancel policy). "
                "Tomorrow: confirm EarnIn delivery, send Indeed call recap to team, start fraud doc."
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Monday Aug 31 End-of-Day Debrief — 4 meetings, major Indeed unlocks, Talent Pool vision shift"
}

def preview():
    sys.stdout.buffer.write("\n=== SLACK MESSAGE PREVIEW ===\n".encode("utf-8", errors="replace"))
    for b in blocks:
        if b.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + b["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "section" and "text" in b:
            sys.stdout.buffer.write((b["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "divider":
            sys.stdout.buffer.write("---\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("=== END PREVIEW ===\n".encode("utf-8", errors="replace"))

if not TOKEN:
    print("No SLACK_TOKEN found — printing preview. Add SLACK_TOKEN/SLACK_BOT_TOKEN/SLACK_API_TOKEN to send.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"Sent! ts={result.get('ts')} channel={result.get('channel')}")
    else:
        print(f"Slack error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
