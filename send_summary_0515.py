#!/usr/bin/env python3
"""
Chief of Staff Daily Briefing — Friday, May 15, 2026
Manan Kothari | Homebase | Slack DM: D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

# ---------------------------------------------------------------------------
# Message content
# ---------------------------------------------------------------------------

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Briefing — Friday, May 15 \U0001f31f",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! No meetings on the calendar today \u2014 Friday is your *execution day*. "
                "Thursday was a heavy-lifting day with two back-to-back strategic sessions. Here\u2019s "
                "your full debrief with everything you need going into the weekend."
            )
        }
    },
    {"type": "divider"},

    # ------- BIG DECISION -------
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f534  THE BIG DECISION (This Weekend)*\n"
                "*Sponsored Jobs API: Descope or POC?*\n\n"
                "Thursday surfaced a real tension between two smart people:\n\n"
                "\u2022 *Cindy sync:* Homebase earns *$0* from the Indeed partnership. "
                "3+ months of engineering for zero revenue \u2192 strong case to *descope entirely*. "
                "Freed bandwidth goes to boost modal upgrades, smart suggestions, built-in careers page, and talent pool.\n\n"
                "\u2022 *Ray sync:* Embedded API = *10x engagement uplift* vs. redirect-only. "
                "Enables agentic \u2018sprinkle $50\u2019 flows via HB Assistant. "
                "Homebase Payroll succeeded *because it\u2019s embedded*. "
                "Ray\u2019s position: \u201cI don\u2019t believe in a universe where we don\u2019t have this.\u201d\n\n"
                "*Ray\u2019s proposed path (you aligned with it):* Build proof-of-concept *outside HB1* (Vercel / vibe coding). "
                "De-risk Indeed\u2019s coordination overhead without burning Tanner\u2019s throughput inside HB1. "
                "Once you have proof of life on the API calls, *then* bring it in.\n\n"
                "> \u26a1 *You need to talk to Jatine before Wednesday\u2019s look-ahead and make the call.*"
            )
        }
    },
    {"type": "divider"},

    # ------- KEY DECISIONS -------
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af  Key Decisions Made Thursday, May 14*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Sponsored Jobs API \u2014 if it proceeds, build outside HB1 first*\n"
                "_Why:_ Tanner doing POC inside HB1 means PRs, context switching, and "
                "\u201cmost of his life is on Indeed email.\u201d Vercel POC = pure API validation, fast feedback.\n"
                "_Rationale:_ You actually built the 3LO prototype this way before handing it to engineering. Same playbook."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Boost Modal Design Direction \u2014 locked*\n"
                "_Why:_ First-time user should get their free HB boost at peak intent \u2014 after "
                "job approval, when they land back on the dashboard. Avoids conflict with trial modal.\n"
                "_Decision:_ Three-option modal: *Homebase (recommended)* | ZipRecruiter | Indeed. "
                "Copy workshop with Matan needed: \u201cbest value\u201d + \u201cup to 4x more applicants.\u201d"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Smart Suggestions = Easiest Win \u2014 prioritized*\n"
                "_Why:_ Leverages existing scheduling team patterns. No new infra. "
                "Title + salary suggestions in-flow. Character count + grammar = next complexity layer.\n"
                "_Rationale:_ Rami starting today can anchor applicant flow work while Cindy designs boost."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. 3LO 12-Hour Architecture Bug \u2014 fix scoped*\n"
                "_Why:_ Jobs posted before authentication window don\u2019t sync. "
                "Users are stuck with no status updates.\n"
                "_Fix:_ Check company 3LO status first \u2192 run worker based on auth timing, not job posting timing. "
                "Tanner monitoring DataDog + Sentry for Thursday\u2019s test results."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Notion over Google Docs for Team Documents \u2014 directional decision*\n"
                "_Why:_ Google Docs MCP can\u2019t read comments. Notion API can. "
                "Team-accessible by default. No permission chaos for Librarian agents.\n"
                "_Ray\u2019s ask:_ Join his Notion group. Manan aligned in Thursday\u2019s 1:1."
            )
        }
    },
    {"type": "divider"},

    # ------- ACTION ITEMS -------
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705  Action Items \u2014 Your Plate*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f534 OVERDUE*\n"
                "\u2022 Complete Indeed documentation analysis (was due EOD Thursday)\n"
                "\u2022 Send Dana: Predicted Roles Figma links + spec doc\n\n"
                "*\U0001f7e0 THIS WEEKEND*\n"
                "\u2022 *Decide: Sponsored Jobs API descope vs. POC path* \u2014 answer needed before Wed look-ahead\n\n"
                "*\U0001f7e1 BY TUESDAY*\n"
                "\u2022 Talk to Jatine: Sponsored Jobs API POC outside HB1? What\u2019s his read on the work?\n"
                "\u2022 Research competitor UI: Greenhouse + Ashby Indeed sponsored flows\n"
                "\u2022 Clarify UI flexibility requirements with Gustavo (can we pre-package budget?)\n"
                "\u2022 Review Cindy\u2019s Boost designs (her deadline is Tue morning for Wed look-ahead)\n"
                "\u2022 Tag Matan for copy workshop on Boost modal messaging\n"
                "\u2022 Confirm Rami onboard \u2014 he started today (applicant flow + job matching)"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Others to Check Monday:*\n"
                "\u2022 *Tanner:* Recruiter display fix (was due Thu) + 3LO test results via DataDog/Sentry\n"
                "\u2022 *Cindy:* Boost modal designs due Tue morning for Wed look-ahead\n"
                "\u2022 *Gustavo (Indeed):* Response to Tanner\u2019s email re: employer.hosted_job scope \u2014 "
                "determines if 3LO is truly unblocked"
            )
        }
    },
    {"type": "divider"},

    # ------- WEEK AHEAD -------
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4c5  Big Week Ahead*\n"
                "\u2022 *Mon May 18:* Cindy/Manan follow-up \u2014 Sponsored Jobs flow + Gustavo answers\n"
                "\u2022 *Tue May 19:* Exec presentation (6-week plan) \u2014 align with Ray on content this weekend\n"
                "\u2022 *Wed May 19:* 2611 look-ahead \u2014 designs must be in Tue morning\n"
                "\u2022 *Fri May 22:* QA complete (Boost) + Customer Connection Challenge Show & Tell\n"
                "\u2022 *May 25\u201326:* Boost sales motion kicks off + Cindy PTO starts (all design feedback must close before)"
            )
        }
    },
    {"type": "divider"},

    # ------- CLOSING -------
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "You\u2019re doing great work, Manan. Thursday was a genuinely hard day \u2014 two back-to-back "
                "sessions on a thorny problem, and you walked out with *clarity*. "
                "The Cindy-Ray tension is actually healthy: Cindy\u2019s protecting engineering ROI, "
                "Ray\u2019s playing the long platform game. Your job this weekend is to mediate and decide. "
                "You\u2019ve got this. Happy early birthday \U0001f382"
            )
        }
    }
]

fallback_text = (
    "Chief of Staff Daily Briefing - Fri May 15: No meetings today. "
    "Key Thursday decisions: (1) Sponsored Jobs API - Descope vs. Vercel POC - decide before Wed look-ahead; "
    "(2) Boost modal direction locked - 3-option, free HB boost post-job-approval; "
    "(3) Smart Suggestions = priority #1; "
    "(4) 3LO 12-hr window bug fix scoped. "
    "Overdue: Indeed docs analysis + Dana Figma links."
)

payload = {
    "channel": CHANNEL,
    "text": fallback_text,
    "blocks": blocks
}

# ---------------------------------------------------------------------------
# Preview
# ---------------------------------------------------------------------------

def preview():
    lines = [
        "",
        "=" * 70,
        "  CHIEF OF STAFF DAILY BRIEFING  --  Friday, May 15, 2026",
        "=" * 70,
        "",
    ]
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            lines.append("  " + block["text"]["text"])
            lines.append("")
        elif btype == "divider":
            lines.append("  " + "-" * 60)
        elif btype == "section":
            text_obj = block.get("text", {})
            if text_obj:
                lines.append("  " + text_obj.get("text", "").replace("\n", "\n  "))
                lines.append("")
    lines.append("=" * 70)
    lines.append("")
    sys.stdout.buffer.write("\n".join(lines).encode("utf-8", errors="replace") + b"\n")

# ---------------------------------------------------------------------------
# Send
# ---------------------------------------------------------------------------

def send(token: str):
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
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Slack message delivered to {CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error', 'unknown')}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"[ERROR] Network error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    preview()

    token = (
        os.environ.get("SLACK_TOKEN")
        or os.environ.get("SLACK_BOT_TOKEN")
        or os.environ.get("SLACK_API_TOKEN")
    )

    if not token:
        print(
            "[PREVIEW ONLY] No SLACK_TOKEN found in environment.\n"
            "To enable live delivery, add SLACK_TOKEN (or SLACK_BOT_TOKEN / SLACK_API_TOKEN)\n"
            "as a secret in the Cursor Dashboard under Cloud Agents > Secrets.",
            file=sys.stderr
        )
        sys.exit(0)

    send(token)
