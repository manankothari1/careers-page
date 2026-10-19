#!/usr/bin/env python3
"""
Chief of Staff daily digest — Monday Oct 19, 2026 (UTC)
Sunday 5pm PDT / First night back in SF — Eve of Day 1 back
No Manan meetings today; new workspace intel from Fri Oct 16 + Monday battle plan
"""
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
        "text": {
            "type": "plain_text",
            "text": "Welcome Home, Manan! Your Eve-of-Day-1 Battle Brief",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Mon Oct 19 (UTC) | Sun 5pm PDT | Your first day back is TOMORROW*\n\nSpain is officially in the rearview. You crushed a ton from abroad — now it's time to run. No meetings today (Sunday), so this is your intel drop + battle plan for Monday morning. Let's get you locked and loaded."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:satellite: WORKSPACE INTEL — What You Missed Friday Oct 16*\n_Three workspace sessions you weren't in. All relevant to your world._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. HBA Architecture: Evolve vs Rebuild — Daniel Chao Raised the Question*\n\n:rotating_light: This is strategic signal you need to have on your radar.\n\n• Only *183 HBA users ever sent a message*. Active in last 4 weeks: *~28 people (~2% of active pop)*\n• Industry precedent: Copilot, Agent Force, Facebook M — all abandoned because they answer but can't *finish the job*. HBA owns the data, so completion is the differentiator.\n• Daniel convened an 'evolve vs rebuild' review. Not all-clear on past decisions — structured pause.\n• 5 target pillars defined: *Knows the Business | Works in Background | Earns Right to Act | Shows Up Fast | Built to Scale*\n• *Next step:* Side-by-side architecture comparison (evolve vs rebuild) with POC work proving each path.\n• *Janneke leaving soon* — only a couple days left to capture her institutional HBA knowledge. This is being flagged as urgent.\n\n:bulb: *Why this matters to you:* SBA×HBA integration is on your roadmap. The 'one front door' vision (single assistant for support + task completion) directly touches your hiring product experience. Stay close to this."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. SBA v2 Technical Alignment — Q4 Commitment Being Set by Tuesday Oct 20*\n\n• *Stephen leaving* — full client platform moving under core engineering\n• *'Jeesh' offer extended* for Schedule Builder EM role (originally interviewed for HPA; had to be convinced to take SB). If accepted, he'll lead SBA.\n• *Swaib being extracted* from client platform to join SBA next week\n• Q4 SBA scope is currently disorganized (Gurkiran's words). Target: clear realistic Q4 commitment by *Tuesday Oct 20*\n• *Forecasting (labor + demand)* confirmed as Q4 SBA deliverable — foundational work that feeds into the scheduling agent\n• Hard cutoff: *nothing beyond late November ships in Q4*\n• Idowu to lead SBA codebase walkthrough with Swaib + Zain before SBA V2 session\n\n:bulb: *Why this matters to you:* SBA×HBA edge case decisions you made Oct 15 may need re-validation against the new EM + Q4 scope. Confirm with Gurkiran that the callout edge cases are still on track to ship."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Billing & Businesses — Friday Ticket Refinement Decisions*\n\n• *787 archived companies* with active Stripe subscriptions found — Hilary running cleanup scripts (Datadog cohorts Oct 28 → Oct 7-12)\n• *JJ:* Fixed Clover BSI sync timing bug + admin user note creation bug causing stuck downgrades. Opened async tech leadership review for entitlements event.\n• *Edwin:* Change payment method frontend nearly done. Next: extend to TeamUp + Payroll, then 3DS tickets for grooming.\n• *Adam:* Raycast backfill categories merged to prod. Data migration needed before `category` becomes non-nullable.\n• *Billing address bug:* Invoice service hardcodes 'US' — Canadian zip codes broken → backlog for now.\n• *Check × Stripe dunning:* Void invoice + cancel past_due event decision confirmed (also aligns with what Dipesh reported last week)."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: MONDAY BATTLE PLAN — Sequenced for Day 1 Back*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*BEFORE ANYTHING ELSE:*\n:one: *3-Year Vision One-Pager* — Block 90 min before your first meeting. This was due Oct 15 for the Board. URGENT. Do not let this slip to Tuesday.\n:two: *Town Hall Q&A Questions* — Due TODAY (Oct 19). Submit before EOD Monday."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MORNING SEQUENCE:*\n:three: *Indeed Merge — Ping Ashley + Bob FIRST THING.* Did Ashley give Bob the green light after T&S met Oct 14? Do NOT merge until confirmed. This is Day 56 of suspension.\n:four: *Indeed Partner Console — Escalate if no response.* Tiger's been CC'd on the Marketplace Support request. Push if still no response.\n:five: *Facebook API — Ping Bob + IBK.* Day 24 of all-calls-failing. No update since Oct 9.\n:six: *26/23 Look-Ahead* — Your first big meeting. Spec steps 1-8 + Fadi low-fi must be ready.\n:seven: *Matt McAllister intro* — New CMO, from Yelp. Today is Day 1 for him being on your radar."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*AFTERNOON / FOLLOW-UPS:*\n:eight: *Divij Gupta — Q4 TS priorities sync.* He's been waiting two weeks. Unblock him today.\n:nine: *Carlo KT (async).* Paternity started Oct 14. Knowledge not confirmed captured. Ping him on: AE65 source name change, Iterable 6 emails fix, 'do not syndicate' bug, continuation sizing. Slack or doc.\n:keycap_ten: *Dunning bug — Ping Dipesh.* Revenue leak. He was in B&B standup Oct 16. Skye + Dipesh own this.\n:one::one: *Discovery slot → Match Explanation Workshop.* Block next Wednesday. Invite Skye, Bob, Matan. FigJam format.\n:one::two: *Syndication timing — Draft requirements + viz for Jatin.* Even a rough mockup unblocks him."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CRITICAL WATCH — Still Burning*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Indeed Feed: Day 56 SUSPENDED.* Root cause: AE65 suffix. Rollback PR raised by Bob. Awaiting T&S green light from Ashley. Every day this stays down = applicants lost.\n• *3-Year One-Pager:* Board meeting opened Oct 15. Still unwritten (as of last check).\n• *Carlo KT:* Not confirmed. Paternity started. AE65 + 6 Iterable emails + 'do not syndicate' bug all live in his head.\n• *Facebook API: Day 24* — All calls still failing.\n• *OMNI Access:* Looker went dark Oct 2. Day *17*. IT ticket still pending.\n• *Emails unsent:* John Waldman (EarnBetter NDA), Marina/Mundo Academy (26+ days). Clear these today.\n• *Rachel Q4/Q1/Q2 UX view:* Was due Oct 7. Still outstanding — did it go out?\n• *Trial source claiming → 100%:* Decision made Oct 9. Still not flipped.\n• *Gift cards owed:* Lola E. Erickson, Michele Landry, Ryan Reilly ($50 each). Don't let these age more.\n• *HBA Evolve vs Rebuild:* New signal — keep an eye on how this affects SBA×HBA integration scope."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bar_chart: QUICK SCOREBOARD*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Indeed:* :red_circle: Day 56 suspended"
            },
            {
                "type": "mrkdwn",
                "text": "*Facebook API:* :red_circle: Day 24 all-calls-failing"
            },
            {
                "type": "mrkdwn",
                "text": "*FFH Paying Customers:* ~210 (goal: 500)"
            },
            {
                "type": "mrkdwn",
                "text": "*Capture Rate:* ~7-8%"
            },
            {
                "type": "mrkdwn",
                "text": "*D5 Zero-Applicant Rate:* 41%"
            },
            {
                "type": "mrkdwn",
                "text": "*Monthly Churn:* ~12%"
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:airplane: Welcome Home, Manan.*\n\nYou've been shipping decisions from a 9-hour time difference for 3 weeks. You kept the team moving, scoped Q4 properly, locked the 21-day job post matrix, decided the SBA callout edge cases, and ran 4 F&B research interviews — all from Spain. That's exceptional.\n\nMonday is your reset. Come in fresh, trust the groundwork you've laid, and stay calm on Indeed — the rollback is in motion. You've got this. :muscle:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest | Mon Oct 19 UTC (Sun 5pm PDT) | 0 Manan meetings | 3 workspace meetings analyzed | Day 1 back tomorrow"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Digest — Welcome Home! Eve of Day 1 Back in SF | Mon Oct 19 UTC"
}

def preview():
    sys.stdout.buffer.write(("=== SLACK PREVIEW (no token) ===\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + " ###\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            if "text" in block:
                sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
            if "fields" in block:
                for f in block["fields"]:
                    sys.stdout.buffer.write(("  " + f["text"] + "\n").encode("utf-8", errors="replace"))
                sys.stdout.buffer.write(b"\n")
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(("[ctx] " + el["text"] + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")

if not TOKEN:
    print("No SLACK_TOKEN found — printing preview only.")
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
        result = json.loads(resp.read())
    if result.get("ok"):
        print(f"Slack message sent OK! ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        preview()
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
