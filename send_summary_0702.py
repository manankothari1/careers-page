#!/usr/bin/env python3
"""Daily decision digest for Manan — July 2, 2026 (Applicant Flow Sprint Lookahead)."""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Digest — Thursday Jul 2",
            "emoji": True,
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff wrap-up | 1 meeting today | End-of-day summary",
            }
        ],
    },
    {"type": "divider"},
    # Intro
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! Great day today. You ran a seriously tight *Applicant Flow Sprint Lookahead* "
                "and made a bunch of crisp, well-reasoned calls that are going to unblock the team right "
                "as you head into a long holiday weekend. Here is everything you decided, why it matters, "
                "and exactly what needs to happen next. You are crushing it."
            ),
        },
    },
    {"type": "divider"},
    # Meeting summary header
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Meeting Today*\n>*Applicant Flow Sprint Lookahead* — 10:00 AM PDT\n>Sprint carryover review, Indeed policy learnings, upcoming work: reactivate jobs + job post recommendation system",
        },
    },
    {"type": "divider"},
    # Decisions header
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decisions Made Today*",
        },
    },
    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Copy jobs removal + reactivate jobs must ship simultaneously*\n"
                "Rationale: Removing copy jobs without reactivate leaves customers with zero way to repost — "
                "catastrophic UX. Both must go live in the same deploy.\n"
                ":pushpin: Carlo to mark copy job removal as a *blocker* on reactivate in Linear."
            ),
        },
    },
    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Reactivate logic: auto-approve with no edits; back in review if edited*\n"
                "Rationale: Job already passed fraud check on first post — no need to re-run unless "
                "content changes. If OEM edits after reactivation, fraud check kicks in again for safety."
            ),
        },
    },
    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Reactivation must syndicate across ALL job boards — not just Indeed*\n"
                "Rationale: You confirmed no duplicate flags on Facebook Jobs, Talroo, or ZipRecruiter for reactivations. "
                "Whoever builds this must ensure the syndication worker re-adds the job across every board, not just Indeed."
            ),
        },
    },
    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Transactional email trigger changed: '0 by D1 / under 15 by D5' → 'under 5 by D3'*\n"
                "Rationale: Earlier, tighter signal = faster intervention for unhealthy jobs before they fall too far behind. "
                "Charmaine is out 2 months so Tanner is picking this up — it's a SendGrid config change, low lift."
            ),
        },
    },
    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Three job post recommendation areas confirmed: role titles, salary, job description*\n"
                "Rationale: ~1/3 of 800 Q2 ICP jobs had non-ideal titles (promo language, pay in title, "
                "'coffee ninja'-type names). Flagging these proactively before submit stops self-sabotage before it starts."
            ),
        },
    },
    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Recommendation modal: blocking, dark overlay, no X — fires after OEM clicks Next on job description page*\n"
                "Rationale: Three reasons — (a) don't interrupt mid-edit, (b) need full job data to send to HPLM agent, "
                "(c) positions us to do fraud check upfront in a future sprint. Modal shows 'reviewing your job post' "
                "with 2-4s wait. Must add copy: *'this may take a couple of seconds'* so users don't think it's frozen."
            ),
        },
    },
    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Roll out recommendation feature as an experiment with traffic throttle — not just a kill switch*\n"
                "Rationale: Critical to monitor job creation drop-off. A/B throttle between default and updated flow "
                "gives you real signal on whether the modal creates churn. Carlo adding this to the acceptance criteria."
            ),
        },
    },
    # Decision 8
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Data science dependency timeline set: role rec agent by Jul 3; salary rec agent end of next week (known risk)*\n"
                "Rationale: DS was slammed with incidents. Role recs are committed for tomorrow. "
                "Salary recs are a known spill risk — whoever implements should coordinate directly with DS on the handoff interface."
            ),
        },
    },
    # Decision 9
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9. Carlo's priority order locked: fraudulent job applications first → SEO wrap-up → SLO coverage*\n"
                "Rationale: SEO findings need a 1-day sanity check before close. SLO items can slip to next sprint. "
                "Fraud work unblocks further planning for job + career page SEO."
            ),
        },
    },
    # Decision 10
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10. Design gaps go to the project channel with a recommendation — not blocked waiting on Cindy*\n"
                "Rationale: Cindy is split across two teams. Rather than blocking on missing design specs, "
                "team posts in channel with a proposed interaction pattern, you align fast, and they build."
            ),
        },
    },
    # Decision 11
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*11. Team self-assigns upcoming work items rather than top-down assignment*\n"
                "Rationale: Martin's recommendation — cleaner, faster, respects eng context. "
                "You're delegating sprint self-assignment for items like job page opt-in v1 re-implementation."
            ),
        },
    },
    {"type": "divider"},
    # Action items header
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:zap: Action Items — By Owner*",
        },
    },
    # Manan actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*You (Manan):*\n"
                ":fire: *URGENT* — Investigate boost purchase bug. Two reporters in two days could not buy boosts. "
                "Matan tagged you in the boost thread. This is a revenue-impacting bug, check it NOW before EOD.\n"
                ":memo: Confirm with Ugu if he has any questions about account setup to-do — you are *OFF tomorrow* (US holiday Jul 3), so today is the last window.\n"
                ":memo: Add 'this may take a couple of seconds' copy to acceptance criteria for the recommendation modal (flagged in meeting)."
            ),
        },
    },
    # Carlo actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Carlo:*\n"
                "- Mark copy job removal as a *blocker* on reactivate jobs in Linear\n"
                "- Add experiment setup (traffic throttle) to role recommendations acceptance criteria\n"
                "- Priority sequence: fraud app work first → SEO sanity check wrap-up → SLO coverage"
            ),
        },
    },
    # Tanner actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Tanner:*\n"
                "- Pick up transactional email trigger change in SendGrid (Charmaine is out 2 months)\n"
                "  - New trigger: under 5 applicants by day 3 (was: 0 by D1 / under 15 by D5)\n"
                "- Share spike work context on reactivate jobs with whoever picks up implementation"
            ),
        },
    },
    # Usman actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Usman:*\n"
                "- Post Aventa sync update to the project after 2:30 PM sync today\n"
                "  - Team needs the Salesforce timeline ASAP for sprint planning visibility"
            ),
        },
    },
    # Ugu actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Ugu:*\n"
                "- Account setup / value prop to-do: back end nearly done, targeting review-ready by *tomorrow Jul 3*\n"
                "- Slack any questions to Manan *today* — Manan is off tomorrow"
            ),
        },
    },
    # Eng team actions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Eng team (self-assign):*\n"
                "- Re-implement job page opt-in features from v1 (quick, needed for talent pool outreach)\n"
                "- Coordinate directly with data science on role/salary recommendation agent handoff interface\n"
                "  - Role rec agent: committed by *Jul 3*\n"
                "  - Salary rec agent: end of next week (known spill risk)"
            ),
        },
    },
    {"type": "divider"},
    # Carry-forward / overdue
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: Overdue & Carry-Forward Items (from previous days)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":red_circle: *VERY OVERDUE* — Confirm Rami's email blast status (was due EOD Jun 25 — that's 7 days ago)\n"
                ":red_circle: *OVERDUE* — Analyze reactivation applicant discount (V1 jobs, CDC table in Databricks)\n"
                ":red_circle: *OVERDUE* — Run Claude Code on Indeed Oct 1 policy — clarify sponsorship scenarios (agreed Jul 1)\n"
                ":red_circle: *OVERDUE* — Follow up with Ivana on Ashby reactivation test result\n"
                ":yellow_circle: ZipRecruiter: find job-level caps or pause spend ($2K burned in 1.5 days, no caps)\n"
                ":yellow_circle: Send call script to Sean (source claiming playbook)\n"
                ":yellow_circle: Confirm Ugu ETA on 'Finish Account Setup' to-do (just added as sprint work)\n"
                ":yellow_circle: Draft v3 Q3 goals doc (3-bucket structure) — share with Ray before John\n"
                ":yellow_circle: Poached: add baristas/cashiers for broader line cook sample\n"
                ":yellow_circle: Follow up: did Matan share Calendly link + source claiming doc with Sean?"
            ),
        },
    },
    {"type": "divider"},
    # Holiday note
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:us: Reminder: You are OFF tomorrow, July 3 (US observes Jul 4 on Jul 3)*\n"
                "Make sure Ugu, the team, and any blockers are unblocked *today* before you sign off. "
                "Tanner's reactivate spike work + Ugu's account setup are the two things most likely to need you."
            ),
        },
    },
    {"type": "divider"},
    # Closing
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Seriously Manan — the way you handled the Indeed policy explainer today was *excellent*. "
                "You gave the entire engineering team the 'why' behind copy jobs vs. reactivate in a way that was clear, "
                "grounded in data (50% zero applicants!), and forward-looking. The team is bought in. "
                "The recommendation system you are building is genuinely differentiated for small businesses who do not "
                "know they are hurting themselves with bad job titles. Big week. Enjoy the long weekend — you earned it. :rocket:"
            ),
        },
    },
]


def build_payload():
    return {"channel": CHANNEL, "blocks": blocks, "unfurl_links": False}


def send_slack(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def preview():
    sys.stdout.buffer.write(
        "\n=== SLACK DIGEST PREVIEW (Jul 2, 2026) ===\n".encode("utf-8", errors="replace")
    )
    for block in blocks:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("### " + text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("---\n".encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("=== END PREVIEW ===\n".encode("utf-8", errors="replace"))


if __name__ == "__main__":
    if not TOKEN:
        print("No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN).")
        print("Add the secret in Cursor Dashboard → Cloud Agents → Secrets.")
        preview()
        sys.exit(0)

    result = send_slack(build_payload())
    if result.get("ok"):
        print(f"Digest sent successfully! ts={result.get('ts')}")
    else:
        print(f"Slack error: {result.get('error')}")
        print(f"Full response: {result}")
        preview()
        sys.exit(1)
