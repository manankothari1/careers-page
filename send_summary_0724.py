#!/usr/bin/env python3
"""Daily EOD digest for Manan Kothari — Friday July 24, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Your EOD Wrap \u2014 Friday, July 24, 2026", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Manan \u2014 big day. You shipped clarity on two gnarly problems, made a key comms call,"
                " and closed the week strong. Here\u2019s everything you decided and what comes next."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\uddd3 Today\u2019s Meetings (5)*\n"
                    "\u2022 8:30am \u2014 Hiring Leads Standup\n"
                    "\u2022 9:15am \u2014 SBA: Testing Update _(Gurkiran\u2019s)_\n"
                    "\u2022 9:30am \u2014 SBA: Go/No-Go _(Gurkiran\u2019s)_\n"
                    "\u2022 2:00pm \u2014 Ashlee / Manan: CX Hiring Pains"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 1 \u2014 Archived Job Redirect: Fix Locked*\n"
                    "*What you decided:* Short-term \u2014 all archived job links redirect to the careers page. "
                    "If the company has no active jobs, they land on a custom 'this role is no longer open' page (design scoped to *next sprint*). "
                    "Catch-all redirect + logging added so you always know where traffic is coming from.\n"
                    "*Why it matters:* Ray flagged the principle \u2014 a sign-in page is never the right fallback for a job link. "
                    "Jatin\u2019s logging layer means you\u2019ll catch every failure path, not just archived jobs.\n"
                    "*Your action:* \u2757 PR up for the short-term redirect. Scope the landing page design into next sprint."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 2 \u2014 CX Hiring Pain: Inline Compliance Check Locked*\n"
                    "*Context:* 117 CX chats in the last 30 days tied to 'job in review' status \u2014 69% contained by Sierra, "
                    "but customers still had to reach out. Sierra tells customers 24-72 hrs; product says 24 hrs. "
                    "That mismatch burns trust before a human even sees the ticket.\n"
                    "*Root cause you mapped:* Three layers \u2014 (1) company syndication lives in Salesforce (one-time, fraud risk check), "
                    "(2) job-level syndication checks content against partner board guidelines (e.g., contact info in the description), "
                    "(3) partner board propagation lag (30 min sends, but boards can lag 4-12 hrs). "
                    "Also: no event log on the backend \u2014 job status is a single mutable row, so you can\u2019t measure average time in review.\n"
                    "*What you decided:* Extend the in-progress 'reviewing your job post' feature to run the same LLM "
                    "compliance check *during job creation* \u2014 surface issues (like contact info in description) *before* "
                    "the user hits Post Job. Job arrives at Michael/Juan\u2019s queue clean \u2192 auto-approved \u2192 syndicates immediately. "
                    "Kills the majority of the 117-chat volume.\n"
                    "*Why this path:* You already have the feature in flight for below-market pay. Extending it is incremental, not net-new. "
                    "Company syndication (medium/high risk new cos) still needs human review short-term, but that volume is low.\n"
                    "*Your actions:*\n"
                    "\u2022 Dig into Sierra hiring transcripts using intent tags (fraud / syndication / applicant / misc) \u2014 map the issue categories\n"
                    "\u2022 Investigate pipeline delay: Michael/Juan approve in under an hour, but jobs still sit in review \u2014 likely a worker/sync bug\n"
                    "\u2022 Scope inline compliance check into the job creation flow (extend existing feature)\n"
                    "\u2022 Longer-term: explore giving Sierra access to actual job/company status for accurate real-time answers"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 3 \u2014 Owner vs. Manager Comms: Managers In*\n"
                    "*What you decided:* Include managers in email cohorts for hiring engagement. "
                    "Filter out low-usage owners. Focus messaging on active managers.\n"
                    "*Why it matters:* Managers feel the hiring pain but aren\u2019t getting comms. "
                    "Owners don\u2019t feel the pain \u2014 so when the owner asks the manager 'how\u2019s hiring going?' "
                    "the manager says 'it\u2019s okay' and nothing changes. "
                    "Usman flagged a wrinkle: in Salesforce, many accounts have managers *listed as owners* \u2014 so the data is inconsistent.\n"
                    "*Your action:* \u2757 *Review Matan\u2019s comms doc this weekend.* "
                    "Flag missing/redundant triggers before Sonia starts building. Matan is waiting on this."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 4 \u2014 Juan Sanchez Email Issue: Your Follow-Up*\n"
                    "*What you decided:* Juan is sending his own emails outside the proper flow. You own following up.\n"
                    "*Your action:* \u2757 Message Juan directly. You got buried today \u2014 don\u2019t let this slip to next week."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe1 SBA FYI \u2014 Ships Monday (Gurkiran\u2019s call, but you should know)*\n"
                    "\u2022 Target: *Monday July 27, 12pm* (Gurkiran checking peak activity time \u2014 may shift earlier)\n"
                    "\u2022 *Risk to watch:* Unassigned grid is getting *overwhelmingly negative* feedback from friendly testing. "
                    "If P1 amplifies this, cohort expansion stops. Watch for this signal next week.\n"
                    "\u2022 QA: ~99% done. Model performing well. CS training video and knowledge base going out EOD today."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd34 Watch List \u2014 Standing Issues*\n"
                    "\u2022 \u26a0\ufe0f *CARLO* \u2014 *14+ DAYS OVERDUE* on Harness/OpenSpec. This is a management issue. Address Monday, no excuses.\n"
                    "\u2022 \u26a0\ufe0f *422 Errors* \u2014 Day 15. Jatin owns RCA. Check status first thing Monday.\n"
                    "\u2022 *Rami pairing (Thu AM)* \u2014 JD quality analysis + talent pool emails. Did it happen? Confirm.\n"
                    "\u2022 *Izzy Rails 8 smoke test* \u2014 scheduled for today (Fri Jul 25). Confirm it\u2019s done.\n"
                    "\u2022 *Usman candidate email experiment* \u2014 Day 2 as of Thursday. Check results.\n"
                    "\u2022 *Fadi \u2014 email UX + source claiming* \u2014 'sending a letter' approach locked Thu. Confirm final state.\n"
                    "\u2022 *Dana succession* \u2014 ~7 weeks. Still no plan. Page from book: start this conversation now. "
                    "Page Templates hand-off must begin before Aug 7.\n"
                    "\u2022 *Career site embed* \u2014 Matan following up with PMs. Did the deep link work? Confirm.\n"
                    "\u2022 *Franchise CX* \u2014 You called it a 'shit show' in your Ashlee call. You\u2019re working on a proposal. "
                    "Keep this moving \u2014 don\u2019t let it get buried again."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\ude80 Your Weekend / Monday P0s*\n"
                    "1. *Tonight or tomorrow:* Review Matan\u2019s comms doc \u2014 he\u2019s waiting so Sonia can start building\n"
                    "2. *Monday:* Archived job redirect PR (if not already merged)\n"
                    "3. *Monday:* Address Carlo \u2014 14+ days is a management issue, not just a ticket\n"
                    "4. *Monday:* Check 422 error RCA with Jatin\n"
                    "5. *Monday:* Check Usman experiment results\n"
                    "6. *Monday:* Juan Sanchez follow-up (if not done today)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "You crushed a tough Friday, Manan. You walked into a 117-chat CX crisis and left with a "
                "clear path to fix it. You locked the archived job approach, aligned the team on manager comms, "
                "and still made time to understand a problem most PMs would\u2019ve waved off. "
                "Go enjoy that boat tonight \u2014 you earned it. \ud83d\udea2"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Your EOD Wrap - Friday July 24, 2026"
}

def preview():
    sys.stdout.buffer.write(b"\n=== SLACK MESSAGE PREVIEW (no token) ===\n")
    for b in blocks:
        t = b.get("type", "")
        if t == "header":
            sys.stdout.buffer.write(("** " + b["text"]["text"] + " **\n\n").encode("utf-8", errors="replace"))
        elif t == "section":
            txt = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif t == "divider":
            sys.stdout.buffer.write(b"---\n")
    sys.stdout.buffer.write(b"=========================================\n\n")

if not TOKEN:
    print("No SLACK token found. Set SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"Message sent successfully to {CHANNEL}.")
    else:
        print(f"Slack API error: {result.get('error', 'unknown')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
