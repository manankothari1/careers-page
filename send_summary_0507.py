#!/usr/bin/env python3
"""Daily chief-of-staff summary for Manan — May 7, 2026."""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN", "")

# ---------------------------------------------------------------------------
# Message payload — Block Kit
# ---------------------------------------------------------------------------

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Day in Review — Thursday, May 7 :sunrise_over_mountains:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! You had a *really productive day* — three back-to-back calls before noon, "
                "and you came out of them with a crisp sprint scope, some strong data-driven decisions, "
                "and a clear plan headed into next week. Here is everything that matters."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 1: BOB / MANAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9:30 AM — Bob / Manan*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_No transcript was captured for this session. If there were decisions or actions, ping Bob to confirm notes._"
        }
    },
    {"type": "divider"},

    # ── MEETING 2: CINDY / MANAN — 2611 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10:15 AM — Cindy / Manan: Sprint 2611 Planning*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 1 — Predicted Role split into two separate projects + handed to Dana*\n"
                ">*What:* Predicted roles on the careers page (company-level, driven by highest-turnover location) and on the dashboard (location-specific) will be tracked as two distinct Linear projects.\n"
                ">*Why:* The two surfaces behave differently, the combined spec confuses engineers, and the work does not directly move applicant flow metrics — your top priority. Dana's squad has engineering capacity to absorb it.\n"
                ">*Rationale:* Classic scope discipline. Ship one thing, learn one thing. You correctly applied the same logic you built with Cindy on predicted roles ('what are we trying to test?') to your own backlog."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 2 — Craigslist removed from Boost*\n"
                ">*What:* Craigslist will be cut from the Boost product entirely.\n"
                ">*Why:* Data shows <0.5% of people are boosting Craigslist jobs and the revenue impact is ~$1K/month — essentially rounding error against a $900K hiring ARR base.\n"
                ">*Rationale:* Clean, evidence-based call. Low revenue, no measurable applicant lift, zero downside to removing it. This frees design + PM mental space."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 3 — Sprint 2611 scope locked to four bets*\n"
                ">1. *Sponsored Jobs API* — engineering spike this sprint; purchase UX designs needed\n"
                ">2. *Boost Modal upgrade* — replace list with visual treatment to test if it drives conversion (baseline: 0.5%)\n"
                ">3. *Full-page Boost after job creation* — post-creation timing test (NOT inside the job creation flow)\n"
                ">4. *Smart suggestions (job title + wage rate)* — in-flow recommendations to improve organic listing quality\n"
                ">*Why:* These four together form a coherent marketplace monetisation thesis: make boost compelling, make boost timely, make the underlying job better, and wire up the next ad network. All four have defined hypotheses and measurable success criteria."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 4 — Full-page Boost lives AFTER job creation (not inside it)*\n"
                ">*What:* The boost offer surfaces on a dedicated full-page post-creation screen, not embedded in the creation flow.\n"
                ">*Why:* Day-1 boost timing is the hypothesis you are testing. Putting it inside creation conflates intent-to-post with intent-to-boost. A/B potential: before vs. after creation is also on the table.\n"
                ">*Note:* Cindy needs to redesign the post-creation page again — acknowledged tradeoff."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 5 — Validate boost timing with Sales BEFORE building it in-product*\n"
                ">*What:* You and Usman agreed: on Day 2-3 after a job post where applicants < 5, the sales team calls the employer to recommend a boost. Message, reasons, and offer will be refined through real calls.\n"
                ">*Why:* Classic lean principle — test the hypothesis with humans before writing a line of code. If sales can convert at meaningful rates with this pitch, that is strong signal the in-product trigger will work.\n"
                ">*Rationale:* Smart sequencing. You get the learning in days, not sprints."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 3: ANDREW / MANAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*11:00 AM — Andrew / Manan: URL Slug Change Request*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *DECISION 6 — Approve this slug change; tighten policy going forward*\n"
                ">*What:* This specific customer's company URL slug will be changed (Charmin handling). Future requests: push back unless there is real churn risk.\n"
                ">*Why:* Customer is on V1 (no screener links to break). Engineering cost is disproportionate to request frequency (1-2/month). QR codes auto-redirect; Indeed syndication resumes within 30 minutes.\n"
                ">*Policy:* Emphasise the careers page is a free product, part of the paid Homebase plan. Escalate only if the customer is threatening to leave. Case-by-case engineering intervention for genuine urgency is acceptable.\n"
                ">*Bonus:* You flagged to confirm V1 → V2 migration details with Dana for TLWA winners. Important data point for slug-change risk assessment going forward."
            )
        }
    },
    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:clipboard: Your Action Items*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":fire: *Today / Tomorrow (do not let these slip)*\n"
                "• *Hand off Predicted Role to Dana* — discuss in your 1:1, confirm she is absorbing it against her backlog\n"
                "• *Update Indeed API doc permissions* — Cindy requested access; she needs it to start designs\n"
                "• *Close chat thread on URL slug + loop in Charmin* — Andrew is waiting on Charmin; keep the thread clean\n"
                "• *Confirm V1 → V2 migration details with Dana* for TLWA winners (slug-change risk has downstream implications)\n"
                "\n"
                ":bar_chart: *Data pulls needed before Wednesday's Cindy sync*\n"
                "• Boost modal funnel: % who open modal → % who do NOT purchase (establish the drop-off baseline)\n"
                "• What sponsored job purchase options look like in Indeed's API (so Cindy can design the purchase UX)\n"
                "• Job title quality: % of active jobs with non-descriptive or unclear titles\n"
                "• Wage competitiveness: do higher-relative-wage jobs get more organic applicants? (supports smart suggestion ROI story)\n"
                "• Define 'success' for boost modal upgrade — even a rough target (e.g. 0.5% → 1.5%) before Cindy starts designing\n"
                "\n"
                ":calendar: *Wednesday sync with Cindy (1.5 hrs booked)*\n"
                "• Walk all four 2611 items: hypotheses, success metrics, scope\n"
                "• Cindy to have code prototype + Figma ready for: Boost Modal, Full-page Boost, Sponsored Jobs API UX, Smart Suggestions\n"
                "• Goal: Cindy locks everything by *Friday EOD* before her PTO (she will be OOO week of May 25+)"
            )
        }
    },
    {"type": "divider"},

    # ── THINGS TO WATCH ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: On Your Radar*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Sprint 2611 look ahead is ~May 19* — you have ~two weeks to get all four items fully spec'd and handed to engineering\n"
                "• *Boost baseline is dire (0.5%)*. The modal upgrade alone probably will not fix it. The sales-first timing test + full-page post-creation surface together are your best shot at a real lift before the sprint closes\n"
                "• *Cindy's PTO* starts week of May 25 — any design feedback loops need to close by May 23\n"
                "• *Bob's team has capacity* (the 1-time purchase work was cut). Consider siphoning engineers for applicant flow work if sprint 2611 scope needs it\n"
                "• *Ray / Fadi / Dana ad-hoc meeting culture* — you and Cindy both flagged this. The fix you proposed (roadmap review before work begins, PM as gatekeeper) is exactly right. Keep pushing it."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Great day, Manan.* You made clean, fast calls backed by data, and you did the hardest thing — you intentionally gave away work (predicted role → Dana) rather than letting your backlog bloat. "
                "The sprint is focused, the thesis is tight, and you have a clear Wednesday milestone. "
                "Now go get that data. :muscle:"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Your Day in Review — May 7, 2026",
    "blocks": blocks
}


def preview():
    print("\n" + "=" * 70)
    print("SLACK MESSAGE PREVIEW (channel: %s)" % CHANNEL)
    print("=" * 70)
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            print("-" * 60)
    print("=" * 70)


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + TOKEN,
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("✅  Message sent to %s (ts=%s)" % (CHANNEL, body.get("ts")))
            else:
                print("❌  Slack API error: %s" % body.get("error"))
                print("    Full response: %s" % json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.URLError as e:
        print("❌  Network error: %s" % e)
        sys.exit(1)


if __name__ == "__main__":
    preview()
    if not TOKEN:
        print("\n⚠️   SLACK_TOKEN is not set. Add it as a secret in the Cursor Dashboard")
        print("    (Cloud Agents > Secrets > SLACK_TOKEN = your Slack user/bot OAuth token).")
        print("    The message above is what would have been sent.")
    else:
        print("\nSending to Slack...")
        send()
