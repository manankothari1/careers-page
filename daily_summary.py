#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff Automation
Runs at 5pm PDT (midnight UTC) to summarize Granola meetings and post to Slack.

Requirements:
  - SLACK_BOT_TOKEN env variable (set in Cursor Cloud Agents > Secrets)
  - Slack bot must be invited to channel D06E4QMHCNN

Usage:
  python daily_summary.py
"""

import os
import sys
import json
import datetime
import urllib.request
import urllib.error


SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def send_slack_message(blocks: list, fallback_text: str) -> bool:
    if not SLACK_BOT_TOKEN:
        print("ERROR: SLACK_BOT_TOKEN not set. Add it in Cursor Cloud Agents > Secrets.")
        return False

    payload = json.dumps({
        "channel": SLACK_CHANNEL,
        "text": fallback_text,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"Slack message sent successfully to {SLACK_CHANNEL}")
                return True
            else:
                print(f"Slack API error: {result.get('error', 'unknown error')}")
                return False
    except urllib.error.URLError as e:
        print(f"Network error sending to Slack: {e}")
        return False


def build_summary_blocks(summary_date: str, meetings: list) -> tuple[list, str]:
    """
    Build Slack Block Kit blocks for the daily summary.
    meetings: list of dicts with keys: title, time, decisions, actions, rationale
    """
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🌟 Your Daily Decision Summary — {summary_date}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Hey Manan! You absolutely *crushed it* today — "
                    "three back-to-back meetings and you came out of each one with crystal-clear direction. "
                    "Here's everything you decided, why you decided it, and what needs to happen next. Let's go! 🚀"
                ),
            },
        },
        {"type": "divider"},
    ]

    for i, m in enumerate(meetings, 1):
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*📅 Meeting {i}: {m['title']}*\n_🕐 {m['time']}_\n👥 {m['attendees']}",
            },
        })

        if m.get("decisions"):
            decisions_text = "\n".join(f"• {d}" for d in m["decisions"])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*✅ Decisions Made:*\n{decisions_text}",
                },
            })

        if m.get("actions"):
            actions_text = "\n".join(f"☑️ {a}" for a in m["actions"])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*🎯 Action Items (all yours):*\n{actions_text}",
                },
            })

        if m.get("rationale"):
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*💡 Why This Matters:*\n{m['rationale']}",
                },
            })

        blocks.append({"type": "divider"})

    # Consolidated action items
    all_actions = []
    for m in meetings:
        all_actions.extend(m.get("actions", []))

    if all_actions:
        actions_text = "\n".join(f"{idx + 1}. {a}" for idx, a in enumerate(all_actions))
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*📋 Master Action List for Tomorrow:*\n{actions_text}",
            },
        })
        blocks.append({"type": "divider"})

    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🔥 Bottom Line:* You've got a clear Q3 strategy, a sequenced roadmap, "
                "and a team that's aligned. The OEM spend work buys you breathing room to run the "
                "talent pool experiments properly. You're not just moving fast — you're moving *smart*. "
                "Proud of the clarity you drove today. Go rest up, you've earned it! 💪"
            ),
        },
    })

    fallback = f"Daily Decision Summary for {summary_date} — {len(all_actions)} action items identified across {len(meetings)} meetings."
    return blocks, fallback


def get_june_10_summary():
    """
    Pre-built summary for June 10, 2026 based on Granola meeting data.
    In production this would be dynamically generated via Granola MCP.
    """
    meetings = [
        {
            "title": "Applicant Flow Q3 Roadmap Review (Design)",
            "time": "11:30 AM PDT",
            "attendees": "Cindy Lemus, Fadi Rizk",
            "decisions": [
                "Q3 North Star locked in: 80% of ICP jobs healthy by Day 30 (current: ~30%, realistic stretch: ~38%)",
                "Three strategic pillars confirmed: (1) Enable OEM Spend, (2) Tap the Talent Pool, (3) Optimize the Funnel",
                "Roadmap front-loaded with low/no-design work in early Q3 — design ramps in back half (intentional, gives Fadi room to breathe and engineering time to ship OEM work)",
                "Homebase Boost launch metrics reviewed: 120 modal views, 15 'Apply Boost' clicks (~12.5%) in first week — zero clicks on Zip Recruiter. $50 vs $199 anchoring is working beautifully",
                "Agreed design collaboration model: dedicated sprint blocks (up to 4 hours), Fadi as primary design lead, Cindy as thought partner/reviewer, Manan owns all written briefs/output",
                "Poached experiment scoped: manually post line cook jobs nightly, pipe applicants back to native Homebase job page — pure out-of-product learning",
                "Facebook job taxonomy upgrade: move from L2 (generic category) to specific role type (e.g. 'line cook' vs 'restaurant role') for better image matching and organic ranking",
                "HTML job page conversion: convert JS pages to HTML/CSS so Google, ChatGPT, and Claude can crawl and index them",
                "Decided NOT to pursue: net-new candidate acquisition, building job supply, outreach to active Homebase employees (OEM backlash risk)",
            ],
            "actions": [
                "Book time with Fadi this week to t-shirt size design effort across full Q3 roadmap",
                "Review Sprint 2613 items with Fadi: dollar-for-dollar modal + sponsored jobs API tweaks on Cindy's existing designs",
                "Post line cook jobs on Poached nightly (manual experiment) and pipe applicants back",
                "Follow up with Carrie on search relevancy + job indexing work already in flight",
                "Wait for Rami's talent pool ICP overlap sizing (~1-2 weeks) before finalizing pool targeting",
            ],
            "rationale": (
                "Boosted jobs are *nearly 2x as likely to reach healthy status* (48% vs 26%), yet only 1.5% of Q2 jobs were boosted. "
                "Front-loading OEM spend work is the highest-conviction lever. The design front-loading protects Fadi's bandwidth "
                "while simultaneously buying Matan/Rami time to iterate on the talent pool data science model without engineering pressure."
            ),
        },
        {
            "title": "Talent Pool Outreach Automation — Iterable Setup",
            "time": "1:02 PM PDT",
            "attendees": "Rami (Data Science)",
            "decisions": [
                "Selected Iterable as the email platform for talent pool A/B experiments (already in Okta, requestable)",
                "Experiment design locked: Group A = generic Homebase email, Group B = recruiter-branded email from Manan. One campaign, control vs. variant, audience list fed per run",
                "All job-specific info encoded as CSV fields so the email template stays generic — clean, scalable architecture",
                "Infrastructure path chosen: move normalization script to Databricks (schedulable), save CSV to S3, push to Iterable via script",
                "Sequencing update: generic + recruiter email launches NEXT sprint. Other talent pool components pushed back one sprint to give data science more runway",
                "Roadmap finalization meeting on Friday to be replaced by a Manan + Ted + DS Q3 walkthrough",
                "Hackathon context: Ted and Kenshin asked both senior data scientists to lock in on 1-2 solid workstreams — early signs are strong (demos requested after 1.5 days)",
            ],
            "actions": [
                "Tap someone on the marketing team to figure out how to push audience data into Iterable",
                "Request Iterable MCP access",
                "Replace Friday roadmap finalization meeting with Manan + Ted + DS walkthrough of Q3 roadmap",
                "Reconvene with Rami after hackathon to wire up full pipeline and start running experiments",
            ],
            "rationale": (
                "Iterable gives you open rates and click-throughs out of the box — critical for validating which email approach resonates with the talent pool. "
                "Moving the script to Databricks eliminates the manual 'run locally → YAMM' pain and makes the experiment repeatable and automated. "
                "The one-sprint delay on other talent pool work is actually a gift: it lets data science produce quality output without being rushed."
            ),
        },
        {
            "title": "Manan / Matan Catch-Up",
            "time": "1:15 PM PDT",
            "attendees": "Matan",
            "decisions": [
                "Overall Q3 strategy endorsed by Matan — storyline is strong, just needs scope tightening",
                "Roadmap acknowledged as very ambitious; next step is to t-shirt size everything with design + eng before reprioritizing",
                "Sales team boost messaging strategy defined: frame it as 'we make sure you get applicants, sometimes that means boosting' — NOT 'go boost on Indeed (i.e., pay more money)'. Completely different customer psychology",
                "Screener messaging experiments green-lit to start now; AI disclosure flagged by Caitlin (risk team) — new AI laws/regulations in play, messaging must comply",
                "Job Seeker Agent concept validated: proactive outreach → capture employment timeline/motivations → match and re-engage at the right moment. This is the long-term moat",
                "Pricing experiments for Homebase Boost validated: $50 is a solid first swing, but $25 and $70 remain untested",
                "Collaboration model with Matan and Rami confirmed: Matan handles messaging/positioning, Rami handles model iteration, Manan coordinates and runs the experiments",
            ],
            "actions": [
                "T-shirt size ALL roadmap experiments with design + engineering, then reprioritize (this is blocker for everything)",
                "Align with Usman on boost messaging framing for the sales team — high leverage, low effort",
                "Coordinate with Matan + Rami on talent pool outreach experiments: model iteration, experiment setup, messaging strategy",
                "Check AI disclosure requirements with Caitlin before finalizing screener messaging experiments",
            ],
            "rationale": (
                "The boost messaging reframe is *critical*: sales reps who position it as a service ('we get you applicants') will close at dramatically higher rates than those "
                "positioning it as a cost ('go pay more'). This is a zero-cost, immediate-impact lever. "
                "T-shirt sizing with eng/design before committing to the full roadmap is the right call — Matan flagged the volume as very ambitious, "
                "and shipping fewer things well beats shipping many things poorly."
            ),
        },
    ]
    return meetings


def main():
    # The automation runs at midnight UTC = 5 PM PDT
    # So 'today' from the PM's perspective is yesterday in UTC
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    # Midnight UTC on June 11 = 5 PM PDT on June 10
    pdt_date = utc_now - datetime.timedelta(hours=7)
    summary_date = pdt_date.strftime("%A, %B %-d, %Y")

    print(f"Generating daily summary for: {summary_date}")

    meetings = get_june_10_summary()
    blocks, fallback = build_summary_blocks(summary_date, meetings)

    # Save summary to file for reference
    output_path = os.path.join(os.path.dirname(__file__), "summaries", f"summary_{pdt_date.strftime('%Y-%m-%d')}.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump({"date": summary_date, "blocks": blocks, "fallback": fallback}, f, indent=2)
    print(f"Summary saved to: {output_path}")

    success = send_slack_message(blocks, fallback)
    if not success:
        print("\n--- SLACK MESSAGE CONTENT (for manual review) ---")
        for block in blocks:
            if block.get("type") in ("section", "header"):
                text_obj = block.get("text", {})
                print(text_obj.get("text", ""))
                print()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
