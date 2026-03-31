#!/usr/bin/env python3
"""Daily Decision Summary - March 30, 2026"""

import json
import os
import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")


def send_slack(blocks, fallback_text):
    if not SLACK_TOKEN:
        print("=== PREVIEW (no SLACK_TOKEN) ===")
        print(fallback_text)
        print("\n=== BLOCKS JSON ===")
        print(json.dumps(blocks, indent=2))
        return

    payload = json.dumps({
        "channel": SLACK_CHANNEL,
        "text": fallback_text,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": "Bearer " + SLACK_TOKEN,
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Message sent! ts=" + str(body.get("ts")))
            else:
                print("Slack error: " + str(body.get("error")))
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print("HTTP error: " + str(e))


D = "\n"  # newline alias to keep lines readable

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Debrief - Monday, March 30",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Manan -- you crushed it today. Five meetings, a full-team all-hands, a sprint kick-off, "
                "and a deep product sync -- and you walked out of all of them with clear direction. "
                "Here is everything you decided, why it matters, and what needs to happen next. Let's go."
            ),
        },
    },
    {"type": "divider"},

    # ── 1: Hiring Leads Standup ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Hiring Leads Standup  |  8:30 AM*\n_With: Fadi, Dana, Matan, Cindy, Bob, Jatin, Ray, Nelson_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made*\n"
                "- *Kickoff deck = #1 priority today* -- all slides must land before the 2pm all-hands\n"
                "- *Replace 25% figure with 44% healthy-trial conversion stat* -- flips narrative from bad to great\n"
                "- *Core message locked:* problem is applicant flow + GTM, NOT the product\n"
                "- *MBR slide skeleton to be sent today,* full content due Wednesday AM\n"
                "- *Jatin to address AI/agentic coding gap* on slide 17 + 'team of builders' section\n\n"
                "*Why it matters:* This deck set the tone for the entire 5-week sprint. "
                "The 44% stat is your momentum builder -- it gives leadership confidence and gets the team fired up."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Action Items*\n"
                ":white_check_mark: Send MBR slide skeleton today\n"
                ":white_check_mark: Sync with Jatin on auto-syndication security incident status\n"
                ":white_check_mark: Confirm Dana's slide edits (she'll Slack when done)"
            ),
        },
    },
    {"type": "divider"},

    # ── 2: Sprint Kickoff ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Sprint Kick Off  |  10:00 AM*\n_Company-wide sprint kickoff (Ankit hosting)_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made*\n"
                "- *AI Assistant is the company strategic priority* -- targeting 24k MAU, Small Business Week is the tent-pole launch\n"
                "- *First release = Q&A in messaging,* subset rollout with feedback loop; success criteria must be defined before expanding\n"
                "- *New operating principles live company-wide:* 'Bring solutions,' 'Decide and commit,' 'AI native by default'\n"
                "- Engineering hit *100% AI utilization* (up from 37% in January)\n\n"
                "*Why it matters:* The AI assistant anchors Small Business Week (May 3-9). "
                "Your team's 5-week sprint directly feeds this. 35 days on the clock."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Action Items*\n"
                ":white_check_mark: Align on success criteria for AI assistant Q&A subset rollout\n"
                ":white_check_mark: Make sure hiring sprint plan maps publicly to Small Business Week deadline"
            ),
        },
    },
    {"type": "divider"},

    # ── 3: Applicant Flow Grooming ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Applicant Flow Grooming  |  12:45 PM*\n_Engineering grooming: Andrew, Tanner, Salvandi, Jeff_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made*\n"
                "- *Toru: remove 14-day age limit* -- that single change eliminates 50% of current job dropoff. Salvandi owns. Tickets due Tue EOD\n"
                "- *Lift industry restrictions temporarily* + fix null business_type mappings -- both blocking full Toru coverage\n"
                "- *10-applicant cap stays* but needs override mechanism built for Homebase Boost (flag now, build later)\n"
                "- *Indeed 3LO: Andrew leads.* Already approved by Indeed, credentials live, redirect URI limits need confirmation\n"
                "- *Careers page starts immediately* after 'Show the Work' ships today -- Andrew + Tanner sequenced\n"
                "- *JobGet integration:* email intro + Slack channel setup (Salvandi, post-Toru tickets)\n"
                "- *Thursday = next grooming session*\n\n"
                "*Why it matters:* Toru at $2.15/applicant vs ZipRecruiter's $15-16 is a *7x cost advantage.* "
                "Getting to full coverage before Small Business Week = flood the funnel at near-zero marginal cost."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Action Items*\n"
                ":white_check_mark: Confirm redirect URI limits with Indeed rep (Andrew is blocked without this)\n"
                ":white_check_mark: Confirm smart presets docs coming from Jeff (careers page is blocked on this)\n"
                ":white_check_mark: Verify Salvandi's Toru ticket breakdown by Tuesday EOD"
            ),
        },
    },
    {"type": "divider"},

    # ── 4: The Path Ahead All-Hands ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Hiring: The Path Ahead (All-Hands)  |  2:00 PM*\n_Full hiring team + stakeholders, 25+ people_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made*\n"
                "- *5-week sprint with hackathon mentality officially launched.* Two prongs: flood funnel + improve conversion\n"
                "- *TLWA campaign confirmed and locked:* printer deadline is *TOMORROW 5PM PST.* "
                "50k custom QR codes to Top Local Workplace award winners. "
                "Flow: scan -> phone/email verify -> instant career page -> AI screener demo -> sticker placement\n"
                "- *Homebase Boost pricing locked:* $50 = ~20 applicants via Tellru (vs ZipRecruiter $199 = 13 applicants). Eat cost per new customer\n"
                "- *Team allocation locked:* Izzy + IBK on TLWA, Malcolm + Carlo on trial funnel, rest on applicant flow\n"
                "- *New sprint cadence live immediately:* Mon/Tue = planning + grooming | Wed/Thu = heads-down | Fri = optional unblock + show and tell\n"
                "- *Culture reset:* 'Fast-moving, high-risk, high-autonomy.' Option to transfer explicitly offered to team\n\n"
                "*Why it matters:* Today was a pivot. You set the vision, rallied the full team, and gave everyone enough clarity to sprint. "
                "The 44% conversion vs 30% benchmark is proof the product works -- you just need more people in the funnel."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Action Items -- TIME SENSITIVE*\n"
                ":red_circle: *TOMORROW 5PM PST HARD DEADLINE:* QR code URLs + printer specs -- confirm with Jatin + Ray tonight or first thing AM\n"
                ":white_check_mark: Verify Fadi has TLWA UX flow locked (phone/email -> career page -> AI screener)\n"
                ":white_check_mark: Confirm 'concierge service' contact info is on the one-pager insert\n"
                ":white_check_mark: Validate Homebase Boost $50 pricing with Chris/Finance before public commitment"
            ),
        },
    },
    {"type": "divider"},

    # ── 5: Jeff / Manan ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Jeff / Manan  |  8:57 PM*\n_Product deep-dive: Indeed integration + Smart PreSets + Business Categorization_",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made*\n"
                "- *Indeed pending status:* add 'Pending on Indeed' intermediate status + email notification when live. "
                "Set expectation: 'Jobs typically take 1-2 hours. We'll email you when it's live.'\n"
                "- *3LO auth is a go:* no additional reviews needed. Credentials live, redirect URL configurable. Build starts now\n"
                "- *4-layer business categorization system locked:*\n"
                "  L1: Default (navy, basic) | L2: Business type known | L3: Category + AI images | L4: Full scrape (logos, colors, real photos)\n"
                "- *Initials-based default logo selected* (e.g., 'TB' for Taco Bell) over emoji -- cleaner, more professional\n"
                "- *Backfill null business_type fields* -- many nulls in DB blocking Layers 2-4\n"
                "- *AI-generated images = minimum bar* for all businesses at career page launch\n"
                "- *Amplitude walkthrough: Thursday*\n\n"
                "*Why it matters:* Smart PreSets and instant career page personalization are the conversion lever for TLWA. "
                "When someone scans a QR and lands on a beautiful branded page in seconds -- that's the wow moment. "
                "This is what makes the May campaign convert."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Your Action Items*\n"
                ":white_check_mark: Finalize business categorization % breakdown (was on your list today)\n"
                ":white_check_mark: Build proof of concept for business data scraping (logos, colors, descriptions)\n"
                ":white_check_mark: Email Indeed team about job status handling (pending state UX)\n"
                ":white_check_mark: Prepare MBR deck (content due Wednesday)\n"
                ":white_check_mark: Jeff continues presets dev -- check in tomorrow\n"
                ":white_check_mark: Block Thursday for Amplitude walkthrough"
            ),
        },
    },
    {"type": "divider"},

    # ── Master Action List ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Master Action List -- What Needs to Happen*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:red_circle: CRITICAL -- Do Tonight or First Thing Tomorrow*\n"
                "1. QR code URLs + printer specs -> confirm with Jatin + Ray (HARD deadline: Tue 5PM PST for printer)\n"
                "2. Fadi TLWA UX flow -> verify locked and ready for activation at scale\n"
                "3. Redirect URI limits -> get answer from Indeed rep to unblock Andrew\n\n"
                "*:large_yellow_circle: Due Wednesday (MBR)*\n"
                "4. MBR deck -- slide skeleton out today, full content by Wed AM\n"
                "5. Business categorization % breakdown + scraping PoC\n"
                "6. Email Indeed team about pending job status handling\n\n"
                "*:large_green_circle: This Week*\n"
                "7. Validate Homebase Boost $50 pricing with Chris/Finance\n"
                "8. Verify Salvandi Toru tickets done by Tue EOD\n"
                "9. JobGet -- confirm Salvandi sets up email intro + Slack channel\n"
                "10. Smart PreSets docs from Jeff -- unblocks careers page build\n"
                "11. Block Thursday for Amplitude walkthrough\n"
                "12. Sync with Jatin on auto-syndication security incident status\n\n"
                "*:large_orange_circle: Overdue -- Still on Your Plate*\n"
                "- *Manan Boost SKU kick-off* with Chris -- billing needs 3-wk lead for Early May. PAST DUE. Do Wednesday.\n"
                "- *Manual Mode green light* -- Cindy QA done, ball is in your court\n"
                "- *3LO spike review + email Kenneth + add Ray* -- Andrew has designs ready\n"
                "- *Applicant flow brief + prototype* -- was due EOD Mar 25"
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
                "*Quick Pulse*\n"
                "Five meetings. One company all-hands. A new operating model launched. "
                "A 50,000-QR-code campaign locked with a hard printer deadline tomorrow. "
                "The 44% conversion stat is gold -- use it everywhere.\n\n"
                "The TLWA printer deadline tomorrow is the single most time-sensitive thing on your plate -- "
                "it's irreversible once it ships. Everything else is important, but that one's a one-way door.\n\n"
                "Sleep well. Tomorrow's a big day. You've got this."
            ),
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Summary generated by your Chief of Staff automation -- Monday March 30, 2026_",
            }
        ],
    },
]

fallback = (
    "Daily Decision Debrief -- Monday March 30, 2026 | "
    "5 meetings: Hiring Standup, Sprint Kickoff, Applicant Flow Grooming, "
    "Path Ahead All-Hands, Jeff/Manan sync. "
    "CRITICAL: QR printer deadline TOMORROW 5PM PST."
)

send_slack(blocks, fallback)
