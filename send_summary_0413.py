#!/usr/bin/env python3
"""
Daily Chief of Staff Summary - Monday April 13, 2026
No meetings today (it's 5pm / start of week), so sending a comprehensive
Monday battle plan covering all critical items from last week.
"""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🗓️ Monday Battle Plan — April 13, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! No meetings in Granola today (yet) — but you've got a *massive* week ahead with TLWA Launch Week, Indeed 3LO grooming, and Homebase Boost all converging. Here's your full battle plan, synthesized from last week's meetings. Let's make this week count 💪"
        }
    },
    {"type": "divider"},

    # === FIRE FIRST ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 FIRE FIRST — Do These Before Anything Else*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Send TLWA Launch Week Brief to Ted* ⚠️ 10+ DAYS OVERDUE\n>You've been carrying this one since before Apr 2. Ted needs this brief — 50,000 QR code recipients are going out and the exec team needs to be aligned. First thing this morning, no exceptions.\n>→ *Action:* Draft and send the TLWA brief to Ted TODAY."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Homebase Boost SKU — Close the Billing Window with Chris McIntosh* 🚨 CRITICAL\n>You confirmed $50 pricing, Taru CPC is locked, and the team is aligned — but the billing SKU is still not finalized. The early-May billing window is closing *now*. This slips = Boost slips.\n>→ *Action:* Block 30 min with Chris McIntosh today. Finalize the one-time $50 SKU and confirm Bishop sign-off. Also flag Sponsored Jobs API as future workstream.\n>→ Bonus: Align with Zuara on migrating free Craigslist boosts → $50 Homebase Boost once live."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Green-Light Manual Mode* ✅ WAITING ON YOU\n>Cindy finished QA. This is done. You're the only thing blocking it from shipping. Greenlight it.\n>→ *Action:* Send the go-ahead to Cindy/team."
        }
    },
    {"type": "divider"},

    # === TODAY'S GROOMING PREP ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Indeed 3LO Grooming Today/Tomorrow — Pre-work Needed*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Get Andrew's Answer: Company-Level vs. Location-Level Indeed Connection*\n>This is the last unresolved architectural question before grooming. Andrew was supposed to get an answer from Indeed over the weekend. If you don't have it, ping him first thing.\n>→ *Action:* Confirm with Andrew before grooming. No grooming without this answer.\n\n*5. Review Jeff's Indeed 3LO Prototype + Send to Team*\n>Jeff built the prototype — you haven't reviewed it yet. Review it, write acceptance criteria, and share with the team before or at grooming.\n>→ *Action:* Review Jeff's prototype + send ACs to team before grooming.\n\n*Key 3LO decisions already locked (bring into grooming as context):*\n> • Phase 1 must-have: View live job post status on Indeed\n> • Phase 1 stretch: Sponsored jobs redirect (open Indeed Boost tab)\n> • Failure handling: 2hr delay / 12hr internal escalation / never surface to OEM\n> • Token: 1hr access / 60-day refresh (Andrew owns)\n> • Auth entry points: to-do, boost, job page\n> • Plaid-style in-app modal (vs redirect)"
        }
    },
    {"type": "divider"},

    # === NELSON / DATA ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Nelson's Data Work — Check Status*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Nelson: 3 Supabase Columns Due Since Apr 8*\n>Nelson was supposed to deliver `metro_area`, `bucketed_role`, and `matching_roles` columns plus the absolute applicant-delta analysis by Apr 8. That's 5 days overdue. You also need to send him the UI branch screenshot.\n>→ *Action:* Ping Nelson — did the columns land? Share your UI branch screenshot.\n>→ *Action:* Once columns land: wire up the job recommendation carousel UI.\n\n*7. Build Supabase Tables + 60K Upsert (Careers Page)*\n>Normalized tables architecture was locked (base + lookup structure). You committed to building these and Nelson will validate.\n>→ *Action:* Block time this week to build tables + upsert 60K location rows."
        }
    },
    {"type": "divider"},

    # === TLWA LAUNCH WEEK ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 TLWA Launch Week — Unblocked Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. QA the Careers Page Pipeline with Fadi*\n>50,000 QR codes go out soon. You need to QA the full end-to-end pipeline with Fadi before they're sent. Iszael is resolving ~8K companies with missing addresses.\n>→ *Action:* Schedule QA session with Fadi this week.\n\n*9. Scrape Company Descriptions via Google Places API → Load to Supabase*\n>Locked decision from the data strategy meeting: you're scraping company descriptions, colors, logos, and photos. Iszael has addresses/badges. Nelson has roles. Your piece is blocking completeness.\n>→ *Action:* Run the scraper, load results to Supabase.\n\n*10. Job Get Integration — Confirm It Shipped*\n>This was scheduled to launch this week per the Apr 10 Hiring Team Check-in. Confirm with the team it's live.\n>→ *Action:* Follow up with Debaditya/team to confirm Job Get went live."
        }
    },
    {"type": "divider"},

    # === PEOPLE / RECURRING ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👥 People & Recurring Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Divij mentorship session:* Schedule with Ted + Dana. Still outstanding.\n• *Matan's prototypes:* Review his 3 prototypes + topical workplace prototype — give him feedback.\n• *Michael Heistand / Indeed search visibility:* Share specific job ID with the Indeed rep. Escalate.\n• *Jatin — resume scoring:* Tue sync with Fadi + Aman. Resume parsing won't ship this sprint but the discussion should clarify the next step.\n• *Minh — Supabase remediation sync:* Still open from INC-372 retro. Quick 30-min sync needed.\n• *Justin Nazari — Supabase audit:* Confirm he's leading the full RLS audit. Handoff should be clean since you're heads-down on LW.\n• *Show & Tell format:* You flagged restructuring it from summarization → discussion format. If you want to make that call, do it before the next S&T.\n• *Applicant flow brief + prototype:* Overdue since Mar 25. Either date it or descope it — it's been hanging for 3 weeks."
        }
    },
    {"type": "divider"},

    # === WEEK SCORECARD ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📈 Where Things Stand (Week of Apr 13)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *ARR:* $650K (up 44% from $450K in January 🔥)\n• *Taru feed:* 300 → 1,100 active jobs/week (CPC caps + biz-type filter removed)\n• *Homebase Boost pricing:* $50 locked ($0.50 CPC on Taru)\n• *Manual V2:* Free for everyone — confirmed publicly to CS; just needs green-light to ship\n• *TLWA careers pages:* Auto-customized (logo, photos, colors, description) for 50K companies\n• *GTM OS ML model:* 70% of top 250 companies converted within 7 days of scoring\n• *Lifecycle:* 46% of team app upgrades influenced by lifecycle campaigns\n• *Security (INC-372):* Architecture upgraded to private Vercel env vars; Semgrep auto-enrolled; Severity = Medium"
        }
    },
    {"type": "divider"},

    # === P0/P1 CHECKLIST ===
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Today's P0/P1 Checklist*\n\n*P0 — Do today, no exceptions:*\n☐ Send TLWA brief to Ted\n☐ Book Chris McIntosh — finalize Boost billing SKU\n☐ Green-light Manual Mode (Cindy is waiting)\n☐ Confirm Andrew has company vs. location answer for 3LO grooming\n\n*P1 — Do today or first thing tomorrow:*\n☐ Review Jeff's 3LO prototype + write ACs + share with team\n☐ Ping Nelson on Supabase columns (overdue since Apr 8)\n☐ Send Nelson your UI branch screenshot\n☐ Schedule QA session with Fadi (TLWA careers page)\n☐ Confirm Job Get integration shipped\n☐ Minh sync — Supabase remediation\n☐ Justin — confirm Supabase audit handoff"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_You've got an absolutely stacked week ahead, but the momentum is real — $650K ARR, Taru scaling 4x, TLWA going to 50K people, and Homebase Boost about to launch. Clear the Ted brief first, get the billing window closed with Chris, ship Manual Mode, and you'll have rocket fuel for the rest of the week. Let's go! 🚀_"
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Monday Battle Plan — April 13, 2026 | Chief of Staff Summary",
    "blocks": blocks
}

def send_slack_message(token, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

if not SLACK_TOKEN:
    print("=" * 70)
    print("SLACK_TOKEN not set — printing preview of message that WOULD be sent")
    print("=" * 70)
    print(f"\nChannel: {CHANNEL_ID}")
    print("\n--- SLACK BLOCKS PAYLOAD ---")
    for block in blocks:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            print(f"\n{text}")
        elif block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            print(f"\n{'='*60}")
            print(f"  {text}")
            print(f"{'='*60}")
        elif block.get("type") == "divider":
            print("-" * 60)
    print("\n" + "=" * 70)
    print("To enable: add SLACK_TOKEN secret in Cursor Dashboard (Cloud Agents > Secrets)")
    print("=" * 70)
    exit(0)

print("Sending Slack message...")
result = send_slack_message(SLACK_TOKEN, payload)

if result.get("ok"):
    print(f"✅ Message sent successfully! ts={result.get('ts')}")
else:
    print(f"❌ Slack API error: {result.get('error')}")
    print(f"Full response: {json.dumps(result, indent=2)}")
    exit(1)
