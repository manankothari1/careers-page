#!/usr/bin/env python3
"""
Daily Chief of Staff Summary — April 9, 2026
Slack channel: D06E4QMHCNN
"""
import json
import os
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🗂️ Chief of Staff Daily Brief — Thursday, April 9",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Here's your end-of-day wrap. One meeting today, and it moved the ball meaningfully on Indeed 3LO. Let's lock in the open items before Monday grooming. 💪"
        }
    },
    {"type": "divider"},

    # ─── TODAY'S MEETING ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Today's Meeting: Indeed 3LO Design Review*\n_11:00 AM · Manan, Andrew, Bob, Jeff Gombos, Tanner_"
        }
    },
    {"type": "divider"},

    # ─── DECISIONS LOCKED ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Decisions Locked Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. View Live Job Post = MUST-HAVE for TLWA Launch Week*\n"
                "> The ability for an OEM to view their live Indeed post is non-negotiable before Launch Week. "
                "This is the core value prop of 3LO Phase 1 — confidence that their job is actually live.\n\n"

                "*2. Sponsored Jobs Redirect = Nice-to-Have (not a showstopper)*\n"
                "> Redirecting to Indeed to boost a job is extremely valuable and you heard it directly from users "
                "(\"if I can't boost on Indeed through Homebase it's a nonstarter\"). But if it slips, "
                "Launch Week won't be blocked. Treat it as a strong stretch goal.\n\n"

                "*3. Failure Handling: Internalize, Don't Surface Errors*\n"
                "> 1-in-4 job posts to Indeed fail. Decision locked: OEMs are NEVER shown an error in-app. "
                "Homebase owns the fix. Protocol:\n"
                ">   • 2-hour delay before \"view live\" is shown (standard queue time)\n"
                ">   • If live after 2 hrs → email OEM with link to view on Indeed\n"
                ">   • If still not live after 12 hrs → internal escalation + email OEM: \"We're working on it, hang tight\"\n"
                ">   • Job's live badge stays ON (reflects other boards, not just Indeed)\n"
                "> Rationale: failure rate is too high to communicate to users; we use 3LO failure reasons from Indeed "
                "to debug and eventually build a feedback loop preventing bad submissions.\n\n"

                "*4. Three UX Entry Points for Auth Flow*\n"
                "> Auth can be triggered from: (1) To-Do section on dashboard, (2) Boost section (next to Craigslist/Indeed boost), "
                "(3) Individual job page \"sync to Indeed\" button. Happy path fully designed — Jeff to finalize in Figma.\n\n"

                "*5. Token Lifecycle: Refresh, Don't Re-Auth*\n"
                "> Access token = 1 hour. Refresh token = 60 days. The team aligned that OEMs should NEVER have to re-auth "
                "within that window. Andrew owns the token refresh mechanism to keep this seamless.\n\n"

                "*6. Auth is a Plaid-Style Modal (No New Tab)*\n"
                "> OAuth flow stays in-app as an overlay — no redirect to an external page. "
                "Exception: opening a new tab only for (a) boosting on Indeed and (b) viewing the live post link."
            )
        }
    },
    {"type": "divider"},

    # ─── OPEN QUESTION (HIGH PRIORITY) ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔶 Open Question — Needs Your Call Before Monday Grooming*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Company-Level vs. Location-Level Indeed Connection*\n"
                "> Bob raised a critical architecture question: do we connect the _company_ to an Indeed account "
                "or each _location_ independently?\n"
                "> • *Company-level:* All locations share one Indeed account. Simpler, better UX, but breaks "
                "if a multi-location business has location-specific Indeed accounts.\n"
                "> • *Location-level:* Each location connects separately. More precise, but OEMs with 5+ locations "
                "have to auth 5+ times — a significant friction spike.\n"
                "> Tanner surfaced an important nuance: once one person auths, does it sync across all managers/owners at that level?\n"
                "> *Andrew is asking the Indeed team about user-to-company association rules.* "
                "His hypothesis: Indeed may handle the mapping themselves, which could inform the right level to connect at. "
                "> ⚡ You need this answer before Monday grooming to unblock the full technical spec."
            )
        }
    },
    {"type": "divider"},

    # ─── ACTION ITEMS FROM TODAY ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 Action Items from Today's Meeting*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Andrew* → Ask Indeed team: how are user accounts mapped to companies/locations? Can multiple owners share one auth? _(asap — blocks Monday grooming)_\n"
                "• *Andrew* → Implement token refresh mechanism (1-hr access / 60-day refresh) so OEMs never re-auth\n"
                "• *Andrew* → Confirm: is Bob's concern about job-to-location mapping on Indeed handled by existing job ID routing? _(quick check)_\n"
                "• *You* → ✅ *DONE:* Added Andrew to the Indeed sponsored jobs conversation\n"
                "• *You* → Confirm with Jeff: \"sync to Indeed\" check-mark wording shouldn't imply the job isn't live on other boards — Jeff said he'll refine the copy\n"
                "• *Team* → Full grooming Mon/Tue — 3LO is in good shape architecturally, just needs the company-vs-location call\n"
                "• *You* → Monitor 3LO failure reasons once live; build OEM feedback loop if failure patterns are consistent"
            )
        }
    },
    {"type": "divider"},

    # ─── CARRY-FORWARD CRITICAL ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Carry-Forward Critical Items (Pre-Existing)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "These are the items that keep following you around. Let's kill them this week:\n\n"
                "🔴 *TLWA / Launch Week Brief to Ted* — NOW 7 DAYS OVERDUE. "
                "This was due April 2nd EOD. Every day this slips creates downstream risk for the launch. "
                "Send it today. Literally nothing is blocking this except bandwidth.\n\n"
                "🔴 *Homebase Boost SKU kick-off with Chris McIntosh* — CRITICAL. "
                "Billing needs a 3-week lead time for an Early May launch. You are now inside that window. "
                "If you don't kick this off today or tomorrow, Early May Boost is off the table.\n\n"
                "🟠 *Nelson deliverables* — metro_area + bucketed_role + matching_roles columns in Supabase were due YESTERDAY (Apr 8). "
                "Check in with Nelson. Also: absolute applicant-delta analysis (needed for applicant health reframe story).\n\n"
                "🟠 *Manual Mode green light* — Cindy's QA is done. This is entirely on you. Just say go.\n\n"
                "🟠 *Fadi sync on sprint concerns* — Ray and Dana both flagged concerns. "
                "You said you'd sync with Fadi before Monday. Today is Thursday — do it tomorrow morning.\n\n"
                "🟡 *Jeff's 3LO prototype* — Review it, send to team, add acceptance criteria. "
                "3LO grooming is Monday/Tuesday — you need this done before then.\n\n"
                "🟡 *Generic roles proposal doc* — Write both options, recommend location-mapping approach. "
                "Grooming depends on this.\n\n"
                "🟡 *Supabase tables + 60k upsert* — You're building this, Nelson validates. Due soon.\n\n"
                "🟡 *Matan's 3 prototypes + topical workplace prototype* — Review pending.\n\n"
                "🟡 *Applicant flow brief + prototype* — Overdue since Mar 25. Needs a date or an explicit descope decision."
            )
        }
    },
    {"type": "divider"},

    # ─── INSIGHT OF THE DAY ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💡 Insight to Keep Top of Mind*\n"
                "> First-day app velocity is the #1 predictor of job health. "
                "Healthy jobs average 13 apps on Day 1 (median: 9). "
                "Jobs with 1-2 apps on Day 1 almost never recover. "
                "Boost on Day 1 — not Day 3. This is the core narrative for the applicant health reframe. "
                "Make sure Nelson's absolute delta analysis (needed: ~4k apps target) lands before you write the TLWA brief."
            )
        }
    },
    {"type": "divider"},

    # ─── TOMORROW'S PRIORITIES ───
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Tomorrow (Friday Apr 10) — Top 5 Priorities*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "1. 🔴 *Send TLWA brief to Ted* — no more delays, this is #1\n"
                "2. 🔴 *Homebase Boost SKU kick-off with Chris* — before you lose the billing window\n"
                "3. 🟠 *Fadi sync on sprint concerns* — before weekend, before Monday grooming\n"
                "4. 🟠 *Chase Nelson on deliverables* (Supabase columns + delta analysis)\n"
                "5. 🟡 *Review Jeff's 3LO prototype + add ACs* — grooming is Monday"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Auto-Brief · April 9, 2026 · Have a great evening, Manan! You're crushing it. 🙌"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Brief — Thursday, April 9, 2026"
}

def send_slack(payload, token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


if SLACK_TOKEN:
    print("Sending to Slack...")
    result = send_slack(payload, SLACK_TOKEN)
    if result.get("ok"):
        print(f"✅ Message sent! ts={result.get('ts')}")
    else:
        print(f"❌ Slack error: {result.get('error')}")
        print(json.dumps(result, indent=2))
else:
    print("=" * 70)
    print("PREVIEW MODE (no SLACK_TOKEN found)")
    print("=" * 70)
    print("\nSLACK CHANNEL: D06E4QMHCNN")
    print("\nMessage blocks summary:")
    for block in blocks:
        if block.get("type") == "section" and "text" in block:
            text = block["text"].get("text", "")
            print("\n" + "-" * 40)
            print(text[:300] + ("..." if len(text) > 300 else ""))
    print("\n" + "=" * 70)
    print("Add SLACK_TOKEN secret in Cursor Dashboard to enable live sends.")
    print("=" * 70)
