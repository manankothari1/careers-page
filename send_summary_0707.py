#!/usr/bin/env python3
"""
Daily Decision Digest — Jul 7, 2026 (Mon PDT)
Covers 2 meetings: Matan/Manan sync + Applicant Flow DS Weekly
Sends to Slack DM channel D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

def get_token():
    for key in ["SLACK_TOKEN", "SLACK_BOT_TOKEN", "SLACK_API_TOKEN"]:
        val = os.environ.get(key, "")
        if val:
            return val
    return None

def build_blocks():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Daily Decision Digest — Mon Jul 7",
                "emoji": True
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "2 meetings today  •  Applicant Flow  •  Your chief of staff has you covered"
                }
            ]
        },
        {"type": "divider"},

        # MEETING 1
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Meeting 1 of 2 — Matan / Manan*  |  11:30 AM PDT\n_Attendees: Matan Chen Zion_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":brain: *Decisions Made*\n\n"
                    "*1. PR subject line wins, but body copy is broken*\n"
                    "Personal Recruiter open rate edges generic (~10.7% vs 10.8%), but CTR nearly identical (1.72% vs 2.49%). The personal subject line promises intimacy — then delivers a generic body. Fix: rewrite the body to match the promise.\n\n"
                    "*2. Audience narrowing is the highest-leverage next move*\n"
                    "Current audience is too wide — unsubscribe rate above 1% benchmark. Next 1-2 experiments will concentrate on recently terminated employees + recent applicants. Ray and John both independently flagged this. This is the move.\n\n"
                    "*3. Multi-job surfacing in email*\n"
                    "Showing a single job caps relevance. Next experiments will test showing multiple roles to increase the odds of a match landing.\n\n"
                    "*4. CTA copy test: fear vs. curiosity*\n"
                    "'Apply to job' signals commitment and causes drop-off. Test 'View job details' as a lower-commitment CTA to get more clicks through the door.\n\n"
                    "*5. Don't run baseline experiments on line cook*\n"
                    "Line cook is inherently hard to fill and skews everything. Run clean baselines on a higher-volume job type first — then apply learnings back to line cook once the playbook is proven.\n\n"
                    "*6. Source claiming protocol locked*\n"
                    "Three-way merge button drops customers. Correct flow: keep Kelli on line, call Indeed separately, then merge. Always confirm customer has an Indeed account BEFORE initiating.\n\n"
                    "*7. SMS/text channel: post-JD work*\n"
                    "Explore SMS outreach channel once job description improvements are shipped with Rami. Don't front-load it."
                )
            }
        },
        {"type": "divider"},

        # MEETING 2
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Meeting 2 of 2 — Applicant Flow Data Science Weekly*  |  1:15 PM PDT\n_Attendees: Ted Naseri, Rami Abou-Seido_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":brain: *Decisions Made*\n\n"
                    "*8. Recruiter email is the clear winner — generic retired*\n"
                    "~4% conversion rate difference across 37K sends. Statistically meaningful. Generic is dropped as a variant. Recruiter is now the control going forward.\n\n"
                    "*9. Next experiment: hyper-personalized subject line*\n"
                    "New variant: 'It\'s James from Butter Baker...' — first-person, specific, human. Recruiter email stays as control. This tests whether named-person personalisation moves the needle.\n\n"
                    "*10. JD optimization before salary recommendations*\n"
                    "Priority order locked: job description optimization ships first, salary recommendation second. Rami to do a blocker/risk scan of salary files before switching tracks — surface risks early.\n\n"
                    "*11. Role recommendation model: Rami done, waiting on data platform*\n"
                    "Rami\'s side is complete. Blocking on data platform team capacity + Izzy (backend). Ted confirms capacity by tomorrow. Goal: Izzy starts Thursday.\n\n"
                    "*12. Friday jam session to prep Monday blast*\n"
                    "Manan + Ted sync Friday to finalize experiment variants, targeting parameters (30 vs 60-day recency, role bucket expansion to prep cook/chef), and email lists. Lists need to be ready for a Monday blast."
                )
            }
        },
        {"type": "divider"},

        # ACTION ITEMS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":white_check_mark: *Your Action Items*\n\n"
                    ":fire: *TODAY — Call Kelli back*\n"
                    "Complete the Indeed source claiming. Keep her on the line, call Indeed separately, then merge. Don't use the three-way button. She has a bad reviews problem on Indeed from a different 'Diamond in the Rough' location — flag that too.\n\n"
                    ":pushpin: *Pull 13 applicant + 127 clicker email/IDs → send to Ted*\n"
                    "Ted joins against his email send table. Key signals: recency, distance, role similarity, location clustering. UTM tags confirmed useful for attribution.\n\n"
                    ":memo: *Write up next email experiment proposal*\n"
                    "Cover: shorter time span, improved body copy, multi-job surfacing, CTA variant ('View job details'), audience narrowing (recently terminated + recent applicants). Run baseline on non-line-cook job type.\n\n"
                    ":bar_chart: *Ask Rami to rerun outreach script on a handful of non-line-cook jobs*\n"
                    "Broaden beyond line cook to get cleaner signal. This unblocks the baseline experiment narrative.\n\n"
                    ":calendar: *Friday jam session with Ted — lock experiment list + email lists*\n"
                    "Target: lists ready for a Monday blast. Align on recency window (30 vs 60 days), role expansion (prep cook, chef), variant specs."
                )
            }
        },
        {"type": "divider"},

        # DELEGATION / OTHERS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":people_holding_hands: *Watch Your Team*\n\n"
                    ":hourglass: *Ted → by tomorrow:* Confirm data platform team capacity for role recommendation this sprint. Izzy needs a green light to start Thursday.\n\n"
                    ":hourglass: *Rami → before JD work:* Scan salary recommendation files for blockers/risks. Surface anything before switching focus.\n\n"
                    ":hourglass: *Carlo → this week:* Harness Framework (OpenSpec) check-in. Deadline is *Thursday Jul 10*. Don\'t let this slip."
                )
            }
        },
        {"type": "divider"},

        # WATCH LIST
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":rotating_light: *Still Open From Last Week*\n\n"
                    ":red_circle: *Boost purchase bug* — 2 reporters, revenue-impacting. Status still unknown. Needs a check.\n"
                    ":red_circle: *ZipRecruiter holiday spend* — burned $2K in 1.5 days pre-Jul 4. Total Jul 3-6 spend still unconfirmed. No job-level caps in place.\n"
                    ":yellow_circle: *Dana\'s Homebase Advantage outreach script* — due last Friday. Confirm with Dana.\n"
                    ":yellow_circle: *Source Claiming Banner E2E* — Matan needs your signoff before ship. Still pending your review.\n"
                    ":yellow_circle: *OpenAI fallback model* — flagged P0 on Jul 6. Has this hit the eng backlog yet?"
                )
            }
        },
        {"type": "divider"},

        # BOTTOM LINE
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":dart: *The Big Picture*\n\n"
                    "Today was a focused execution day. The talent pool email strategy is sharpening fast — you\'ve moved from 'did it work?' to 'here\'s exactly what to tune and why.' The data is telling a clear story: open rates are a subject-line problem, CTR is a body-copy problem, and applicants are an audience-relevance problem. You know what to fix.\n\n"
                    "The role recommendation and JD optimization work is sequenced correctly. Keep Rami unblocked on the scan and get Ted\'s capacity answer tomorrow — that\'s the critical path.\n\n"
                    "You\'re building something real here. The signal is getting cleaner with every experiment. Keep pulling the thread."
                )
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Your chief of staff, reporting for duty every day at 5pm PT_"
                }
            ]
        }
    ]
    return blocks


def send_slack(token, blocks):
    payload = json.dumps({
        "channel": CHANNEL,
        "blocks": blocks,
        "text": "Daily Decision Digest — Mon Jul 7, 2026"
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body
    except urllib.error.URLError as e:
        return {"ok": False, "error": str(e)}


def preview(blocks):
    lines = []
    for b in blocks:
        btype = b.get("type", "")
        if btype == "header":
            lines.append("=" * 60)
            lines.append(b["text"]["text"])
            lines.append("=" * 60)
        elif btype == "section":
            text = b.get("text", {}).get("text", "")
            lines.append(text)
            lines.append("")
        elif btype == "context":
            for el in b.get("elements", []):
                lines.append(f"[{el.get('text','')}]")
            lines.append("")
        elif btype == "divider":
            lines.append("-" * 60)
    output = "\n".join(lines)
    sys.stdout.buffer.write(output.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


def main():
    blocks = build_blocks()
    token = get_token()

    if not token:
        print("No SLACK_TOKEN found — printing preview:\n")
        preview(blocks)
        print("\n[PREVIEW ONLY — add SLACK_TOKEN secret in Cursor Dashboard to send]")
        sys.exit(0)

    print(f"Sending to channel {CHANNEL}...")
    result = send_slack(token, blocks)
    if result.get("ok"):
        print(f"Sent! ts={result.get('ts')} channel={result.get('channel')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        preview(blocks)
        sys.exit(1)


if __name__ == "__main__":
    main()
