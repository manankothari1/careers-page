#!/usr/bin/env python3
"""Daily EOD Chief of Staff digest — Friday Aug 21, 2026."""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Friday Aug 21 — Your EOD + EOW Digest",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Wrapping up a big Friday for you — *3 meetings*, a bunch of crisp decisions, and some real momentum heading into the week Sky starts. Here's everything you locked in today, with your action items front and center. You're operating with serious clarity right now — let's keep that going. :fire:"
        }
    },
    {"type": "divider"},

    # ── MEETING 1: BarTaco ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:taco: Meeting 1 — Homebase <> BarTaco* | 11:00 AM\n_Manan + Rushi Patel | Brooke (btoole) + Lisa Bassilios Mosby (bartaco)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Context:* BarTaco has 31 locations, 25 salaried openings at any given time, and a lean recruiting team of 2 (Brooke + Sheri). They're paying ~$50K/yr for Paylocity + Grayscale integration, and piloting Grayscale for scheduling/texting in ~8 weeks. The real decision-maker is *Scott Rodney* (ops/tech lead) — returning from Chicago after this week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision: Add internal job posting to the roadmap*\n> Auto-publish externally after X days if unfilled. Brooke said this was a *'big deal'* — she used it at Dick's Sporting Goods, sees it as a cultural signal AND an efficiency win. Their current workaround is manual comms through Opus/Seven Shifts/email to regional directors. This is a legitimate product gap.\n\n*Rationale:* This is a pattern across enterprise-adjacent customers. Internal-first posting signals respect for current employees before going external. Easy to spec, defensible on roadmap.\n\n:pushpin: *Why the deal isn't closed yet:* Financial commitment to Paylocity/Grayscale is the real blocker — not product quality. Homebase could deliver the same at ~$20K/yr (vs. their current $50K). Once the Grayscale pilot plays out in 8 weeks, that's the window."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your action items from this meeting:*\n• :white_medium_square: *[Manan]* Add internal job posting (auto-publish after X days) to roadmap — Brooke called it a 'big deal'\n• :white_medium_square: *[Rushi]* Email Brooke to stay top of inbox + get intro to Scott Rodney (ops/tech, real decision-maker)\n• :white_medium_square: *[Rushi]* Follow up with BarTaco after Scott returns from Chicago"
        }
    },
    {"type": "divider"},

    # ── MEETING 2: Fraud Check In ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:lock: Meeting 2 — Hiring Fraud Check In* | 12:15 PM\n_Manan + Juan Sanchez Jr + Laura Hulse_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision: OTQ email verification flow is LOCKED — targeting sprint after next*\nDesigns are finishing up. Trigger = first job posting (not account creation). Job stays in *draft* until email is verified. Company-level + job-level syndication only kick off post-verification.\n\n*How it works:*\n• 98.5% of users have email on file → 6-digit OTP sent, no extra friction\n• 1.5% without email → prompted to add at posting time\n• Deep link in verification email returns user directly to job posting flow\n• Existing fraud checks still run after verification\n\n:white_check_mark: *Decision: Email > Phone for fraud prevention*\nPhones are trivially faked in bulk — no affiliation signal. Email enables domain-level checks (temp domains out, @mcdonalds.com in). Only the legitimate owner receives the OTP, even if a fraudster lifts the address from a public listing.\n\n:rotating_light: *Current fraud context:* Juan shared a CSV of repeat fraud attempts (Inspire Brands + Wells Fargo impersonation). Attempts paused in the last 2 days — *likely changed method, not stopped.* Keep the heat on this one.\n\n*Your action items from this meeting:*\n• :white_medium_square: *[Manan]* Bring OTQ email verification into the upcoming sprint (sprint after next week's)"
        }
    },
    {"type": "divider"},

    # ── MEETING 3: Matan / Manan ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:brain: Meeting 3 — Matan / Manan (Strategy Doc Review)* | 12:30 PM\n_Manan + Matan Chen Zion_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Decision: Strategy doc needs rebalancing — talent pool is the bridge, not just applicant flow*\nMatan's honest read: the doc leans applicant flow. That's accurate to your prior focus, but talent pool solves *both* applicant flow AND core product value simultaneously — that framing needs to be front and center before Sky reads it Monday.\n\n*Rationale:* Screener toggle + scheduling reliability = known core gaps. Talent pool is the rare investment that strengthens multiple weak spots at once. With Sky arriving Monday, this is the exact narrative to anchor on.\n\n:white_check_mark: *Decision: Consolidate two PM/sales syncs → one bi-weekly (Matan's Tuesday session)*\nKeep next Tuesday's session as-is, then merge from the week after. Matan to resend invite with your availability, 30 mins.\n\n:white_check_mark: *Decision: Abandonment survey questions need a full rework*\nThe real insight: users are exiting on *screen 1* — so asking 'what stopped you from finishing?' is the wrong question. Change it to *'what stopped you from starting?'* and redesign answer options to surface actionable signal, not confusion.\n\n*Rationale:* 25 responses all saying 'just browsing' or 'no immediate need' = the question is wrong, not the product. You need to understand why people who showed enough intent to open the flow immediately bounced.\n\n:white_check_mark: *Decision: Build a tighter trio — Manan + Matan + John*\nSales team is already reacting positively to intent signals work (easier conversations, more trial starts per John's feedback). Formalizing this trio = faster alignment on top-of-funnel messaging and acquisition strategy.\n\n*Signals worth tracking:*\n• Hiring chip at signup: *15% consistent click rate over 3 months* — strong signal, use it for targeting\n• Somia implementing 3 email drip initiatives (payroll-interested, non-payroll/team app, hiring-clickers)\n• SEO = essentially zero content today; 'where to post my job' >> 'AI hiring assistant' in search volume — big gap to fill\n• Ray told Matan to ship the AI product video rough (not polished); feedback: *skip 'hire with confidence' opener → cut straight to ATS demo at :13*\n\n*Your action items from this meeting:*\n• :white_medium_square: *[Manan]* Update strategy doc framing — talent pool as the bridge, not just applicant flow lever\n• :white_medium_square: *[Manan]* Rework abandonment survey: 'what stopped you *starting*?' + redesign answer options\n• :white_medium_square: *[Manan]* Define what to build from signup hiring intent data (who clicks hiring chip + what they do next)\n• :white_medium_square: *[Manan]* Build tighter trio with Matan + John (align on top-of-funnel influence + messaging)\n• :white_medium_square: *[Matan]* Resend PM/sales sync invite with Manan's availability (30 min, bi-weekly Tuesday)\n• :white_medium_square: *[Matan]* Ship product video rough — cut opener, start at ATS demo (:13)"
        }
    },
    {"type": "divider"},

    # ── CONSOLIDATED ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:clipboard: Your Master Action List — Aug 21*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Manan owns:*\n:one: Update strategy doc — talent pool as the bridge (before Sky reads it Monday)\n:two: Rework abandonment survey ('what stopped you *starting*?' + answer options)\n:three: Define product changes from signup hiring intent (hiring chip clickers)\n:four: Build trio: Manan + Matan + John (align on top-of-funnel)\n:five: Add internal job posting to roadmap (auto-publish after X days)\n:six: OTQ email verification → confirm sprint targeting (sprint after next)\n\n*Others own:*\n• Rushi: Email Brooke (BarTaco) + get intro to Scott Rodney\n• Matan: Resend PM/sales sync invite; ship AI product video rough"
        }
    },
    {"type": "divider"},

    # ── EOW WATCH LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: Friday EOW Watch — Things Hot Heading into Next Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *Sky starts Monday Aug 25* — 3 days. Strategy doc should be in great shape before he reads it. You're writing the Talent Pool doc for his onboarding. This is your moment to set the narrative.\n\n:rotating_light: *Q3 Strategy Doc* — Comments were due by noon today from the Leads team. Hopefully in! Ray reviews after — but Ray is gone, so this is Manan's doc now.\n\n:rotating_light: *422 Job Publishing Errors* — Day 40+. 146 locations. Jatin is on RCA but this has been open too long. Get a status update Monday.\n\n:rotating_light: *#hiring-epdd channel* — Jatin greenlighted to create (Aug 20). Did it happen? Check Monday.\n\n:rotating_light: *Fadi Resume Insights designs* — Overdue since Aug 17. Blocking you. Follow up first thing Monday.\n\n:rotating_light: *OTQ fraud attempts* — Paused last 2 days = changed method, not stopped. Juan has the CSV. Stay vigilant.\n\n:rotating_light: *New GM of Hiring* — Start was Aug 18 or 25. If Aug 18, they're already a week in and you haven't connected. Reach out Monday."
        }
    },
    {"type": "divider"},

    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:tada: You had a sharp Friday, Manan.*\n\nThree meetings, each with clear decisions and clean next steps. The BarTaco call surfaces a real product gap worth owning. The fraud check-in got OTQ locked and scoped. And the strategy doc conversation with Matan gave you the framing upgrade you need right before Sky walks in the door Monday.\n\nSky starts in 3 days. You're walking in with a tight strategy narrative, a locked OTQ path back to Indeed health, and momentum on trial conversion. Go enjoy the weekend — you've earned it. :raised_hands:"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Friday Aug 21 EOD Digest — 3 meetings, key decisions + action items",
    "blocks": blocks
}

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

if token:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        if result.get("ok"):
            print(f"[OK] Slack message sent to {CHANNEL}")
        else:
            print(f"[ERROR] Slack API error: {result.get('error', 'unknown')}", file=sys.stderr)
            sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}", file=sys.stderr)
        sys.exit(1)
else:
    print("[PREVIEW — no SLACK_TOKEN found] Message that would be sent:\n")
    sys.stdout.buffer.write(
        json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8", errors="replace")
    )
    sys.stdout.buffer.write(b"\n")
