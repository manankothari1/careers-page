#!/usr/bin/env python3
"""
Sunday Apr 26 — Week-Ahead Battle Plan for Manan Kothari, PM @ Homebase
Sends to Slack DM channel D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Good Sunday, Manan! Your Week-Ahead Battle Plan — Apr 28–May 2",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "No meetings today — perfect time to recharge and get ahead. Here's everything you need to *own this week*. It's a big one. TLWA is live imminently, 3LO deploys Monday, and the agentic era officially begins Thursday. You've got this."
        }
    },
    {"type": "divider"},

    # ── MONDAY APR 28 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Monday, Apr 28 — 3LO Deployment Day*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *3LO frontend deploys behind feature gate* — Tanner owns the deploy. Bob owns prod smoke tests + DataDog/Sentry monitoring. This is Indeed sandbox-less so prod is the only test env — be close to Bob.\n• *Confirm with Tanner* that the Boost modal 3LO entry point is confirmed descoped.\n• *Check in with Andrew* before he departs — confirm Indeed status endpoint is live and documented for handoff.\n• *Greenlight Manual Mode* — Cindy's QA is done. This is on *you*. Ship it or explicitly defer it."
        }
    },

    # ── TUESDAY APR 29 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Tuesday, Apr 29 — Sprint Grooming + Predicted Roles Decision*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Sprint grooming* — Sprint 2610 priority order is locked: Purchase Boost → V1→V2 migration → OTP → JobGet Easy Apply. Hold the line.\n• *Predicted Roles placement decision* — Dashboard vs Careers page. Divij released, chips cover 65% for TLWA. Make the call in grooming. You still need a Linear project + Slack channel for this.\n• *Nelson OVERDUE (since Apr 8!)* — metro_area, bucketed_role, matching_roles. Chase him down before grooming. No more slipping.\n• *Matan OVERDUE (since Apr 23)* — Post Boost plan to #leads AND survey customers on hiring spend. Follow up directly."
        }
    },

    # ── WEDNESDAY APR 30 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Wednesday, Apr 30 — Marketplace Brainstorm + Email Audit*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Marketplace 2-hour brainstorm* — Ray moved this to this week. Come prepared with:\n  - Hypothesis 1: Can we own the applicant DB? (prev applicants/employees as untapped source)\n  - Hypothesis 2: Owners willing to spend on applicants through HB vs Indeed?\n  - Josh Leverton spreadsheet framework as your structure\n  Ray wants you to have done independent research first — do it Sunday/Monday.\n• *Email journey audit* (Matan + Kayla) — This is blocking ALL future email launches. Get Matan + Kayla calendared this week.\n• *Indeed discoverability audit* — Run as an applicant on a sample of live jobs. Flag the link-to-dashboard-not-job-post issue."
        }
    },

    # ── THURSDAY MAY 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Thursday, May 1 — Agentic Era Starts*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *HB Assistant show-and-tell* — Schedule this NOW (before EOD Monday). All hiring team tool definitions must be submitted before this meeting.\n• *Agentic era experimentation officially begins* — Jatin's Codex/Claude good-cop/bad-cop demo is May 4, but experimentation starts today.\n• *Hiring team tool definitions due* — Before this meeting, each team member should have defined their tools + structured outputs for the assistant orchestrator.\n• *Saja (Talroo)* — Send CPA categories + configure campaign. This has been sitting too long.\n• *IBK* — Send logo max width/height specs. Quick task, high signal."
        }
    },

    # ── FRIDAY MAY 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Friday, May 2 — Wrap + Look Ahead*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *TLWA brief to Ted* — This is *20+ days overdue*. I'm flagging this every single day until it's sent. Review the brief this weekend, send it Monday morning, and unblock Ted's team permanently.\n• *Cassy (printer)* — Confirm mailable address count (~3k flagged unmailable QR recipients). Quick ask.\n• *Justin* — Re-run description batches 93–100 + confirm Supabase RLS audit is complete (INC-372 follow-through).\n• *Weekly retro* — How did 3LO deploy go? Is TLWA live? What's blocking the Predicted Roles 35%?"
        }
    },

    {"type": "divider"},

    # ── FIRE LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Things That Are Actually on Fire Right Now*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*TLWA Brief → Ted*\n20+ days overdue. Send Monday AM."
            },
            {
                "type": "mrkdwn",
                "text": "*Nelson: metro_area + roles*\nOverdue since Apr 8. Chase before grooming Tue."
            },
            {
                "type": "mrkdwn",
                "text": "*Matan: Boost plan + survey*\nOverdue since Apr 23. DM him today."
            },
            {
                "type": "mrkdwn",
                "text": "*Boost Modal Copy*\nInconsistent across 3 states. Assign + fix this sprint."
            },
            {
                "type": "mrkdwn",
                "text": "*Greenlight Manual Mode*\nCindy done. Ball in your court — decide Mon."
            },
            {
                "type": "mrkdwn",
                "text": "*TLWA Company List Freeze*\n55,696 vs 54,000 — needs a freeze decision NOW."
            }
        ]
    },

    {"type": "divider"},

    # ── KEY MILESTONES ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚀 Key Milestones This Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Mon Apr 28* — 3LO behind feature gate (Tanner + Bob)\n• *Mon Apr 28* — Andrew's last day window — get 3LO handoff docs\n• *Tue Apr 29* — Sprint 2610 grooming (Predicted Roles decision)\n• *Thu May 1* — HB Assistant show-and-tell; agentic experimentation begins\n• *Mon May 4* — Jatin agentic demo (Codex/Claude); Fadi candidate profile redesign starts\n• *~May 5* — Juan risk logic review; auto-syndication watch-and-wait closes\n• *~May 5* — Ugo's V1→V2 migration should be well underway"
        }
    },

    {"type": "divider"},

    # ── CONTEXT + STRATEGIC FRAME ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Strategic Frame for the Week*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Last week was huge — Town Hall confirmed Homebase's trajectory: NRR >100%, ARR per FTE improving, $48M cash, breakeven by December. The new website positioning drops *this week*. \n\nYou're at an inflection point on three vectors simultaneously:\n1. *TLWA* — your rebirth moment. It's the narrative anchor for the board, the team, and the market.\n2. *Marketplace innovation* — Ray gave you the greenlight to spend hiring margin on buying applicants. You have a 4-month window before competitors catch up. Don't waste it.\n3. *HB Assistant / Agentic* — the architecture is right (tools → orchestrator → structured UI). The team alignment is there. Now you just need to execute the show-and-tell and get tool definitions locked before May 1.\n\nYou're building the best version of Homebase's hiring product. The momentum is real. Have a great week."
        }
    },

    {"type": "divider"},

    # ── HEALTH CHECK ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 Numbers to Watch*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*H1 Trial Goal*\n21k needed / ~100/wk actual → need 800/wk"
            },
            {
                "type": "mrkdwn",
                "text": "*Healthy Job Rate*\n8% — critically low despite 2x applicant volume"
            },
            {
                "type": "mrkdwn",
                "text": "*ARR*\n$650K (+44% from $450K in Jan)"
            },
            {
                "type": "mrkdwn",
                "text": "*Auto Syndication*\n52% (16/31 cos) — watch & wait until ~May 5"
            }
        ]
    },

    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Your Chief of Staff • Sunday Apr 26, 2026 • Based on all Granola calls from the week of Apr 20–25"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Week-Ahead Battle Plan — Apr 28–May 2, 2026",
    "blocks": blocks
}


def preview():
    sys.stdout.buffer.write(
        "\n=== SLACK MESSAGE PREVIEW ===\n".encode("utf-8", errors="replace")
    )
    sys.stdout.buffer.write(
        "Channel: {}\n".format(CHANNEL_ID).encode("utf-8", errors="replace")
    )
    sys.stdout.buffer.write(
        "Blocks: {} block(s)\n".format(len(blocks)).encode("utf-8", errors="replace")
    )
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(
                "\n[HEADER] {}\n".format(
                    block.get("text", {}).get("text", "")
                ).encode("utf-8", errors="replace")
            )
        elif block.get("type") == "section":
            text_obj = block.get("text", {})
            if text_obj:
                sys.stdout.buffer.write(
                    "[SECTION] {}\n".format(
                        text_obj.get("text", "")[:200]
                    ).encode("utf-8", errors="replace")
                )
            fields = block.get("fields", [])
            for f in fields:
                sys.stdout.buffer.write(
                    "  [FIELD] {}\n".format(
                        f.get("text", "")[:120]
                    ).encode("utf-8", errors="replace")
                )
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(
                "---\n".encode("utf-8", errors="replace")
            )
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(
                    "[CONTEXT] {}\n".format(
                        el.get("text", "")
                    ).encode("utf-8", errors="replace")
                )
    sys.stdout.buffer.write(
        "=== END PREVIEW ===\n\n".encode("utf-8", errors="replace")
    )


def send_slack():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer {}".format(SLACK_TOKEN),
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully! ts={}".format(body.get("ts")))
                return True
            else:
                print("Slack API error: {}".format(body.get("error")))
                return False
    except urllib.error.URLError as e:
        print("Network error sending to Slack: {}".format(e))
        return False


if __name__ == "__main__":
    preview()
    if not SLACK_TOKEN:
        print("SLACK_TOKEN not set — preview only. Add it via Cursor Dashboard > Cloud Agents > Secrets.")
        sys.exit(0)
    success = send_slack()
    sys.exit(0 if success else 1)
