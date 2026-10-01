#!/usr/bin/env python3
"""Daily Chief of Staff digest - Sep 30, 2026 PDT"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest  |  Wednesday, Sep 30"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "*Day Grade: B+*  |  4 meetings  |  2 direct  |  :airplane: Leaving for Spain in 2 days  |  Pre-Spain checklist CRITICAL"
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: THEME OF THE DAY*\n*EARNIN POSITIONED \u00b7 ROLE NORMALIZATION MVP LOCKED \u00b7 PRE-SPAIN CHECKLIST NOW URGENT*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: TODAY\u2019S MEETINGS*\n9:30 AM \u2014 HRM Essential Journey _(company-wide review; you weren\u2019t in this)_\n10:32 AM \u2014 :key: Partnership Value Exchange & NDA with Skye _(1:1 with Skye)_\n11:00 AM \u2014 :key: Role Normalization Context Sync _(you + Divij + Sina + Bob + Tiger + Jatin)_\n12:45 PM \u2014 Growth Brain Daily Standup _(company-wide; you weren\u2019t in this)_"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mega: DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":one:  *[EarnIn] NO DATA-SHARING DEAL \u2014 NOT NOW*\n:white_check_mark: *Decision:* Proceed with organic + paid feed only. Deeper data-exchange arrangement is 1\u20132 quarters out.\n:thought_balloon: *Why:* The value exchange is asymmetric \u2014 HB gets distribution, EarnIn gets users *and* the customer relationship, which compounds against HB over time. You and Skye landed on the cleanest, most honest framing: 'We\u2019re actively working on the same segment.' It protects HB\u2019s long-term position without burning the relationship. Smart call.\n:dart: *Manan to send:* One consolidated email to John at EarnIn \u2014 NDA + documentation request + follow-up positioning."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":two:  *[EarnIn] NDA SIGNED :white_check_mark:*\n:white_check_mark: *Decision:* Skye signed the mutual NDA via Apple account. She\u2019ll send the PDF to you.\n:thought_balloon: *Why:* The NDA has been blocking any formal data exchange for weeks. Getting it signed and packaged in a single email to John closes the loop cleanly and unblocks the relationship.\n:dart: *Skye to send:* Signed NDA PDF to Manan. Manan packages into outbound email."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":three:  *[Role Normalization] gRPC MVP CONTRACT LOCKED :lock:*\n:white_check_mark: *Decision:* Single-call gRPC contract. Inputs: job title + business type + business category + business name. Output: normalized role table (bucket role + base role + seniority). Versioned. Null/failure returns a 1\u20132 line reason string.\n:thought_balloon: *Why:* This is foundational infrastructure for salary recs, matching, and job board targeting. Locking the contract now \u2014 with versioning baked in \u2014 means the taxonomy can evolve without breaking downstream consumers. The reason string on failure makes the system auditable and improvable from day one.\n:no_entry_sign: Sibling roles DEFERRED from MVP. Backfill scope deferred until data volume is known (18-month window = reasonable hypothesis)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":four:  *[Role Normalization] ABSTRACT BEHIND MarketplaceMatching \u2014 DESIGN PRINCIPLE ADOPTED :building_construction:*\n:white_check_mark: *Decision:* Design toward the ideal end-state architecture NOW, not just MVP. Abstract behind a MarketplaceMatching class so the implementation can swap underneath. Single vs. multiple gRPC calls to be decided in a dedicated future session.\n:thought_balloon: *Why:* Jatin\u2019s push here was exactly right \u2014 stakes are low while scope is small. The cost of short-term thinking is a multi-sprint rewrite in Q2/Q3. This is the kind of call that separates good senior PMs from great ones: investing 30 minutes of design thinking now to save 3 sprints later."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":five:  *[Background Checks] HYPOTHESIS SET FOR Q4 REVENUE ESTIMATE*\n:white_check_mark: *Decision:* Your hypothesis is background checks are primarily used by *non-hiring* customers (not just Hiring plan users). Skye to run the data to confirm for Finance\u2019s Q4 estimate.\n:thought_balloon: *Why:* Background checks have been the 'redheaded child' of the product \u2014 useful but under-examined. Trending up YoY but with Nov\u2013Dec seasonality (roles involving kids/vulnerable groups). Spikes expected late winter and summer. Getting clarity on the customer breakdown finally gives Finance a real number to work with."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: ACTION ITEMS FROM TODAY\u2019S CALLS*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Yours (committed in calls):*\n:red_circle: Send consolidated email to John at EarnIn \u2014 NDA + docs request + partnership positioning _(partnership call)_\n:red_circle: Post normalized role use cases to talent pool Slack channel \u2014 salary, matching, JD board targeting, etc. so team can build toward right architecture _(role normalization call)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Others\u2019 actions:*\n:large_blue_circle: *Skye* \u2014 Sign and send NDA PDF to Manan\n:large_blue_circle: *Skye* \u2014 Run BG check usage data by customer type (Hiring vs. non-Hiring) for Finance Q4 estimate\n:large_blue_circle: *Team* \u2014 Each person to add their future use cases to the talent pool Slack channel\n:large_blue_circle: *Team* \u2014 Schedule focused end-state MarketplaceMatching architecture session (timebox it)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: PRE-SPAIN CRITICAL CHECKLIST (You leave Oct 2 \u2014 2 DAYS)*\nThings that must happen before your flight:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *HIGHEST URGENCY \u2014 TODAY OR TOMORROW MORNING*\n:black_small_square: *Indeed Easy Apply PDF* \u2014 WAS DUE TODAY (Sep 30). Did you submit?! This is CRITICAL.\n:black_small_square: *Omni access request* \u2014 DUE BEFORE OCT 2. Looker goes dark Oct 2 \u2014 the same day you fly. File an IT help desk ticket TONIGHT.\n:black_small_square: *OKR draft* \u2014 Was due EOD yesterday (Sep 29). Was it submitted? Confirm sent to Fadi.\n:black_small_square: *Q4 planning session w/ Skye* \u2014 Was supposed to happen today. No meeting note captured. Did it happen async? If not, it must happen tomorrow."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *IMPORTANT \u2014 BEFORE SPAIN*\n:black_small_square: *3-year vision one-pager* \u2014 At least a rough draft before Spain. Board meeting ~Oct 15\u201322.\n:black_small_square: *Introduce yourself to Matt McAllister* \u2014 New CMO, Day 4. Yelp SMB background = directly relevant to GTM Excellence. Don\u2019t let the week go by.\n:black_small_square: *Carlo KT (knowledge transfer)* \u2014 He goes on paternity Oct\u2013Feb. BIGGEST knowledge risk. Block time tomorrow.\n:black_small_square: *Lola Erickson $50 gift card* \u2014 Promised on Sep 28 call. lola.e.erickson@gmail.com. Under 5 minutes.\n:black_small_square: *Matan job title/salary data* \u2014 He texted Sep 24. Just send it.\n:black_small_square: *Reply to John Waldman on EarnBetter* \u2014 Acknowledge clarification, propose paid CPC test (~100 jobs, $0.07\u20130.10 CPC, $2K budget)."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:telescope: INTEL FROM TODAY (meetings you weren\u2019t in)*\n*HRM Essential Journey* \u2014 Homebase-wide UX audit of core HR flows (invite, send docs, terminate). Key signal: multi-location termination is a recognized pain point; moving toward company-level 'inactive' status. Several UX issues flagged in invite flow that could affect your Hiring product thinking.\n*Growth Brain Standup* \u2014 Data ingestion pipeline on track to complete end of this week. Guardrail rules agreed: 1-year window for engagement, 2D30 for upsell. Paying customer = any TMAP or payroll (OR logic). Stack-rank framework in progress. Watch this one \u2014 it\u2019ll touch hiring surfaces as it matures."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:brain: MANAN, A NOTE FROM YOUR CHIEF OF STAFF*\n\nToday was a strategically clean day. Both of your direct calls landed on the right answers \u2014 you avoided the EarnIn trap (asymmetric data exchange that builds their moat, not yours), and you and Jatin locked a role normalization architecture that won\u2019t embarrass you in 6 months. That\u2019s good PM work.\n\nBut the scoreboard still shows: *Indeed Easy Apply PDF* (due today), *Omni access* (due in 2 days), and *Q4 planning* (no note). These are the things that could come back to bite you while you\u2019re in a museum in Barcelona with no cell service.\n\nCrank through tonight. You leave in 2 days. You\u2019ve got this. :es:"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest \u2014 Sep 30 | EarnIn positioned \u00b7 Role normalization MVP locked \u00b7 Pre-Spain checklist URGENT",
    "blocks": blocks,
    "unfurl_links": False
}

def preview():
    sys.stdout.buffer.write(("\n" + "="*70 + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("SLACK DIGEST PREVIEW (no token \u2014 would send to D06E4QMHCNN)\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("="*70 + "\n\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("[HEADER] " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("\n" + "="*70 + "\n").encode("utf-8", errors="replace"))

if not TOKEN:
    print("No Slack token found. Printing preview.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"SUCCESS: Message sent to {CHANNEL}")
    else:
        print(f"Slack API error: {result.get('error')}")
        print(json.dumps(result, indent=2))
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    sys.exit(1)
