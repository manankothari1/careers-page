#!/usr/bin/env python3
"""Daily Chief of Staff summary - Monday Apr 28 battle plan (sent Sun Apr 27 5pm PT)."""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"


def build_payload():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Good evening! \U0001f31f Your Monday Battle Plan is ready",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! No meetings today (Sunday) which is totally fine "
                    "\u2014 you needed the recharge. Big week ahead: *3LO ships*, "
                    "*Sprint 2610 grooming*, *marketplace brainstorm*, and the "
                    "*agentic era kicks off Thursday*. Let\u2019s crush it. \U0001f4aa"
                ),
            },
        },
        {"type": "divider"},
        # ---- FIRE ITEMS ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f525 *FIRE ITEMS \u2014 Clear These First Thing Monday*\n\n"
                    "1. \u26a0\ufe0f *TLWA Brief \u2192 Ted* \u2014 This is *20+ days overdue*. "
                    "Re-review the careers page section tonight, fire it off first thing Monday AM. "
                    "This is the #1 thing blocking you.\n\n"
                    "2. \u26a0\ufe0f *Nelson follow-up* \u2014 Overdue since *Apr 8* (19 days!). "
                    "Need metro_area + bucketed_role + matching_roles. Ping him Monday AM.\n\n"
                    "3. \u26a0\ufe0f *Matan follow-up* \u2014 Overdue since *Apr 23*. "
                    "Post Boost plan to #leads + survey customers on hiring spend. "
                    "Unblock this today.\n\n"
                    "4. \u26a0\ufe0f *TLWA Company List \u2014 FREEZE NEEDED* \u2014 "
                    "55,696 vs 54,000 discrepancy. Confirm freeze status with Ugo ASAP."
                ),
            },
        },
        {"type": "divider"},
        # ---- MON APR 28 ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4c5 *Monday, Apr 28*\n\n"
                    "\u2022 *3LO Frontend Deploy* \u2014 Tanner ships behind feature gate. "
                    "Bob owns prod smoke tests + DataDog/Sentry monitoring. "
                    "Confirm with Andrew that Indeed status endpoint is live *before* he leaves.\n\n"
                    "\u2022 *HB Assistant Show-and-Tell* \u2014 Schedule by EOD today. "
                    "Hiring team needs to define tools + structured outputs before Thu May 1. "
                    "Don\u2019t let this slip.\n\n"
                    "\u2022 *Greenlight Manual Mode* \u2014 Cindy QA is done, ball is in your court. "
                    "Make the call today (yes/no).\n\n"
                    "\u2022 *New Website Launches* \u2014 'Your new assistant. Never calls out.' "
                    "goes live. Keep an eye on any fires.\n\n"
                    "\u2022 *Boost Modal Copy* \u2014 Still inconsistent across 3 states. "
                    "Fix it or assign it today \u2014 it\u2019s a quick win.\n\n"
                    "\u2022 *Saja (Talroo)* \u2014 Send CPA categories + configure campaign. "
                    "URGENT: Manual Mode jobs are in feed, spending $35 on $30/mo customers.\n\n"
                    "\u2022 *Andrew (Indeed status endpoint)* \u2014 "
                    "Confirm endpoint is live before he officially departs."
                ),
            },
        },
        {"type": "divider"},
        # ---- TUE APR 29 ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4c5 *Tuesday, Apr 29*\n\n"
                    "\u2022 *Sprint 2610 Grooming* \u2014 Priority order locked: "
                    "Purchase Boost \u2192 V1\u2192V2 \u2192 OTP \u2192 JobGet Easy Apply. "
                    "Predicted Roles placement decision (dashboard vs careers page) needs to happen here.\n\n"
                    "\u2022 *Predicted Roles / Chips* \u2014 Divij released; chips cover 65% for TLWA launch. "
                    "Create Linear project + channel. Decision on placement TBD at grooming.\n\n"
                    "\u2022 *Resume Matching endpoint* \u2014 "
                    "50/50 blend confirmed; Divij\u2019s ML is ready. "
                    "Endpoint creation is the blocker \u2014 confirm it\u2019s in Sprint 2610."
                ),
            },
        },
        {"type": "divider"},
        # ---- WED APR 30 ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4c5 *Wednesday, Apr 30*\n\n"
                    "\u2022 *Marketplace Brainstorm (2 hrs)* \u2014 "
                    "This is a big one. Come armed with research on the two core hypotheses:\n"
                    "  \u2460 Owners already spend on Indeed \u2014 can spend less through HB\n"
                    "  \u2461 Previous applicants/employees = untapped applicant CRM\n"
                    "  Use Josh Leverton\u2019s hypothesis framework. Ray wants you to bring independent thinking.\n\n"
                    "\u2022 *Competition window*: ~4 months before catchup. This brainstorm matters."
                ),
            },
        },
        {"type": "divider"},
        # ---- THU MAY 1 ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4c5 *Thursday, May 1 \u2014 Agentic Era Begins* \U0001f916\n\n"
                    "\u2022 *HB Assistant Show-and-Tell* \u2014 "
                    "Scheduled (you\u2019re locking this today, right?). "
                    "Hiring team must have tool definitions + structured outputs ready.\n\n"
                    "\u2022 *Agentic Era Experimentation Starts* \u2014 "
                    "Jatin\u2019s Codex/Claude good-cop/bad-cop demo is May 4. "
                    "Make sure the stage is set.\n\n"
                    "\u2022 *Auto Syndication Check* \u2014 "
                    "Watch & wait window closes ~May 5. "
                    "Juan\u2019s risk logic review ~May 5 as well. "
                    "TLWA award winner gap (stuck in medium-risk?) should be clearer by then."
                ),
            },
        },
        {"type": "divider"},
        # ---- ONGOING / BACKLOG ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4cb *Ongoing / Don\u2019t Let These Slip*\n\n"
                    "\u2022 *Justin* \u2014 Re-run description batches 93-100 + Supabase RLS audit\n"
                    "\u2022 *JobGet 30-day paid test* \u2014 Set budget, confirm with Peter Lee + Dan\n"
                    "\u2022 *Indeed discoverability audit* \u2014 Run as applicant on sample of live jobs\n"
                    "\u2022 *Cassy (printer)* \u2014 Confirm mailable address count (~3k flagged)\n"
                    "\u2022 *Matan + Kayla* \u2014 Full email journey map (unblocks ALL future email launches)\n"
                    "\u2022 *IBK* \u2014 Logo max width/height specs still needed\n"
                    "\u2022 *Add Cindy* to careers page QA\n"
                    "\u2022 *Bob* \u2014 Backlog cleanup (307 items, 200+ Sentry tickets)\n"
                    "\u2022 *Matan* \u2014 Salesforce access via Justin Stroud or rev ops\n"
                    "\u2022 *Flag usage-based pricing* conversation to Ray/leadership "
                    "(HB Assistant upsell breaks current package model)"
                ),
            },
        },
        {"type": "divider"},
        # ---- METRICS PULSE ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f4ca *Metrics Pulse*\n\n"
                    "\u2022 ARR: *$650K* (+44% from $450K in Jan) \U0001f525\n"
                    "\u2022 H1 trial goal: 21k | Current: ~100/wk | Need: *800/wk* \u2014 "
                    "this gap is the existential challenge\n"
                    "\u2022 Healthy job rate: *8%* \u2014 critically low despite doubled applicant volume\n"
                    "\u2022 GTM OS ML: 70% of top 250 converted in 7 days\n"
                    "\u2022 NRR >100% \u2014 rare in SMB, keep protecting it"
                ),
            },
        },
        {"type": "divider"},
        # ---- CLOSING ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f3af *The Big Picture This Week*\n\n"
                    "You\u2019ve got a ton of momentum right now. "
                    "TLWA is about to launch, 3LO ships Monday, and you\u2019re about to kick off "
                    "what could be a category-defining marketplace strategy. "
                    "The agentic era starting Thursday isn\u2019t a buzzword \u2014 it\u2019s a "
                    "real inflection point for Homebase hiring.\n\n"
                    "Clear the overdue items first (TLWA brief, Nelson, Matan), "
                    "execute the Monday checklist, and *trust the sprint*. "
                    "You\u2019re building something special. Let\u2019s go! \U0001f680"
                ),
            },
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "Chief of Staff \u2022 Daily summary for Manan Kothari \u2022 Mon Apr 28, 2026",
                }
            ],
        },
    ]

    return {
        "channel": CHANNEL,
        "text": "Your Monday Battle Plan is ready \U0001f4aa",
        "blocks": blocks,
    }


def send_to_slack(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body
    except urllib.error.URLError as e:
        return {"ok": False, "error": str(e)}


def preview(payload):
    sys.stdout.buffer.write(
        b"\n=== SLACK MESSAGE PREVIEW ===\n"
    )
    for block in payload["blocks"]:
        if block["type"] == "header":
            sys.stdout.buffer.write(
                ("\n# " + block["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif block["type"] == "section":
            sys.stdout.buffer.write(
                (block["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
            )
        elif block["type"] == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block["type"] == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(
                    ("\n[" + el.get("text", "") + "]\n").encode("utf-8", errors="replace")
                )
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n\n")


def main():
    payload = build_payload()
    preview(payload)

    if not SLACK_TOKEN:
        print("SLACK_TOKEN not set. Add it in Cursor Dashboard > Cloud Agents > Secrets.")
        print("Message preview shown above. Exiting without sending.")
        sys.exit(0)

    print("Sending to Slack...")
    result = send_to_slack(payload)
    if result.get("ok"):
        print(f"Message sent! ts={result.get('ts')} channel={result.get('channel')}")
    else:
        print(f"Slack error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
