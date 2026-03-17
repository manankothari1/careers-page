#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff for Manan Kothari, PM at Homebase
Runs at midnight UTC (5pm PT) via cron.
Sends a Slack DM summarizing decisions, action items, and follow-ups from the day's meetings.

Requires: SLACK_TOKEN env var (Slack Bot Token with chat:write scope)
Slack Channel: D06E4QMHCNN (Manan's DM)
"""

import os
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(token: str, channel: str, text: str, blocks: list = None) -> dict:
    url = "https://slack.com/api/chat.postMessage"
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_mar17_message() -> str:
    """Mar 17, 2026 — SF Offsite Day 2 — Meetings: Job+Careers Grooming, Hiring Standup,
    Indeed Job Sync + 3LO (Andrew), Ray/Manan 1:1, Talk Indeed <> Homebase."""

    msg = """Hey Manan! 👋 Big day — here's your *Daily Decision Brief* for *Monday, March 16, 2026* (SF Offsite Day 1). You crushed it today. Let's make sure nothing slips through the cracks. 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*📋 DECISIONS & ACTIONS — March 16, 2026*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*1. Careers Page Redesign — Greenlit with Thursday Derisk Gate*
*Meeting:* Job + Careers Page Grooming (4pm, with Andrew, Tanner, Cindy)
*Decision:* Move forward with a 2-week careers page redesign: multi-image banner (up to 4), logo upload, company info editing, brand color/font customization, hover-to-edit UX. *BUT* — treat Thursday's meeting as a formal go/no-go gate for embed functionality and mobile complexity.
*Why:* New data models required, embed patterns are uncharted in the platform, and mobile responsiveness could blow the timeline. Thursday is your safety valve.
*Action Items:*
• *Manan* → Send PRD docs to Andrew + Tanner before Thursday. Research image size limits (5MB?) + confirm SVG vs PNG requirement.
• *Andrew* → Derisk embed functionality + backend data model changes. Come to Thursday with a scope estimate.
• *Tanner* → Assess front-end scope + mobile editing complexity. Flag any descoping suggestions by Thursday.
• *All* → Thursday meeting = descoping conversation if risks materialize. Don't show up empty-handed.

*2. Indeed 3LO (Three-Legged OAuth) — Decided to Pursue Aggressively*
*Meetings:* Ray/Manan 1:1 (10pm), Indeed Job Sync + 3LO w/ Andrew (7:30pm), Talk Indeed <> Homebase (10:30pm)
*Decision:* Commit to building Three-Legged OAuth integration with Indeed. This unlocks: sponsored jobs API, source claiming, job visibility confirmation, and eliminates the 25% job posting failure rate. David (Indeed) confirmed the path forward.
*Why:* 25% of jobs are invisible on Indeed right now — that's a real customer pain point. 3LO is the key that unlocks sponsored jobs revenue, ATS partnership tier upgrades (targeting Platinum), and lets customers manage Indeed spend directly through Homebase.
*Action Items:*
• *Manan + Ray* → Email Kenneth + add Ray to Indeed email thread. Align on which customer segment to prioritize first (the 2×2 matrix: has Indeed acct / no Indeed acct).
• *Andrew* → Allocated sprint time for Indeed 3LO spike. Start with: (a) visual 3LO auth flow, (b) clarify 2LO vs 3LO posting behavior for authenticated users, (c) account-to-job mapping methodology, (d) webhook availability.
• *Ray* → Follow up with David (Indeed) post-call — he's sending docs + UI guidelines. Review and share with team.
• *Manan* → Clarify with David: Does advertiser authorization apply to Homebase account or individual employer accounts? This is the key open question.
• *Short-term:* Restart Indeed scraper as a band-aid while 3LO is being built.

*3. Indeed API — Acknowledged Current Documentation Gaps & Scoped the Investigation*
*Meeting:* Indeed Job Sync + 3LO Conversation w/ Andrew (7:32pm)
*Decision:* The Indeed API docs are wrong — actual capabilities differ from documentation. Decided to use the David call to get ground truth, and scope the technical investigation around: (a) does 3LO replace or supplement 2LO for job postings, (b) how Indeed maps jobs to employer accounts, (c) webhook availability for status updates.
*Why:* If jobs posted via 2LO don't link to the employer's Indeed account, that's a fundamental integration problem that 3LO doesn't automatically fix. Need to understand the mapping before building.
*Action Items:*
• *Andrew* → Draft the questions list for Indeed; make sure account-to-job mapping is Question #1.
• *Manan* → Flag sponsored jobs / organic ranking degradation risk to leadership — Indeed reducing organic visibility for non-sponsored jobs is a strategic threat worth tracking.

*4. Hiring Standup — Sprint Priorities Locked, Manual Mode Cleared for QA*
*Meeting:* Hiring Team Standup (6pm)
*Decision:* Reschedule button takes priority over observability work for Sharmin. Manual mode QA round 2 in progress (Cindy's feedback received, PR merged). One-click processing at ~2,000 jobs, targeting 2,500 EOD. Not going live today (team in transit / SF offsite).
*Why:* New sprint just kicked off. Reschedule button is higher customer impact than observability. One-click needs to hit the 2,500 threshold before go-live.
*Action Items:*
• *Sharmin* → Focus on reschedule button, deprioritize observability work until button ships.
• *Malcolm* → Hit 2,500 one-click processed jobs today. Report back.
• *Cindy* → Complete QA round 2 on manual mode. Go/no-go decision pending her sign-off.
• *Manan + Andrew* → Thursday careers page derisk meeting (already scheduled).
• *Malcolm + Andrew* → Update environment setup documentation this sprint.
• *Divij* → Continue PRD for Resume Parser v2 (beyond experience: skills, certifications, etc.).

*5. Indeed Listing Optimization as Sales Play — Greenlighted Experiment*
*Meeting:* Hiring Team Standup (6pm)
*Decision:* Test using Homebase's job description optimization to prospect new customers: show them optimized Indeed listings → book demo → convert to trial. Platform-specific descriptions (Indeed vs ZipRecruiter vs Facebook) as differentiator.
*Why:* Clever land-and-expand play. Use the product capability as the sales hook itself. Low cost, high signal.
*Action Items:*
• *Manan* → Define success metrics for the experiment. Who owns this — sales or product?
• *Z (Iszael?)* → Set up customer call to demonstrate the capability.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*🔥 OPEN ACTION ITEMS CARRIED FORWARD*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
These were open before today — don't let them fall off:
• *Malcolm* → One-click posting shipped by Fri Mar 20 ✅ (in progress, ~2k/2.5k)
• *Andrew* → "Show the work" feature PRs by Fri Mar 20
• *Carlo* → FE unit test coverage report + project brief example
• *Bob + Jatin* → Hiring public interface tech debt plan
• *Manan* → Q2 roadmap prep — exhaustive initiative list for Tue/Wed roadmap session THIS WEEK
• *Tanner* → Port job page in Week 1 of sprint
• *IBK* → Interview availability (heavy backend, full sprint)
• *Andrew* → Claude skills EPD presentation by Apr 10
• *Manan* → Check in with Izzy on V1→V2 migration confidence
• *Deal Breakers sign-off* → Wednesday Mar 18 ⚠️ (2 days away!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*🗓️ TOP 5 FOR TOMORROW (Tue Mar 17)*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. *Q2 Roadmap Session Day 1* — This is the big one. Make sure your exhaustive initiative list is prepped tonight.
2. *Deal Breakers Sign-off Prep* — Due Wednesday. Get alignment today.
3. *Indeed Email to Kenneth* — Loop in Ray, send before EOD.
4. *David's Indeed Docs* — Review and share with Andrew + Ray once received.
5. *Check in with Izzy* — V1→V2 migration confidence check.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Manan, seriously — you navigated a ton today. The Indeed 3LO path forward is *huge*, it's going to unlock real revenue and fix a painful customer experience. The careers page grooming was thorough, you've got the right risk gates in place. And keeping the sprint focused during the SF offsite week? That's leadership. 💪

Go enjoy the offsite tonight — you've earned it. Tomorrow's roadmap sessions are where the magic happens. Let's gooo. 🏆"""

    return msg


def build_no_meetings_message(is_weekend: bool = False) -> str:
    if is_weekend:
        return (
            "Hey Manan! 🌅 It's the weekend — no meetings to summarize today. "
            "Rest up, you've got a big week ahead. The roadmap sessions, the Indeed 3LO push, "
            "careers page sprint — all of it is going to need your best energy. "
            "Enjoy the downtime! 🎉"
        )
    return (
        "Hey Manan! 👋 No Granola meetings captured for today — either a light calendar day "
        "or recordings didn't sync. Check Granola directly if you think something's missing. "
        "Have a great evening! 🚀"
    )


def build_message_from_granola_data(granola_data: list) -> str:
    """Generic fallback for future days when granola data is passed as JSON."""
    if not granola_data:
        return build_no_meetings_message(is_weekend=False)

    today = datetime.now(timezone.utc).strftime("%A, %B %-d, %Y")
    lines = [
        f"Hey Manan! 👋 Here's your *Daily Decision Brief* for *{today}*.\n",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "*Today's Meetings:*",
    ]
    for m in granola_data:
        title = m.get("title", "Untitled")
        summary = m.get("summary", "No summary available.")
        lines.append(f"\n*{title}*\n{summary}")

    lines.append("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append("Have a great evening, Manan! 🚀")
    return "\n".join(lines)


def main():
    token = os.environ.get("SLACK_TOKEN", "").strip()
    if not token:
        print("ERROR: SLACK_TOKEN environment variable is not set.")
        print(
            "Please add your Slack Bot Token (with chat:write scope) as a secret "
            "in the Cursor Dashboard under Cloud Agents > Secrets."
        )
        print("Secret name: SLACK_TOKEN")
        sys.exit(1)

    granola_data_raw = os.environ.get("GRANOLA_DATA", "").strip()
    if granola_data_raw:
        try:
            granola_data = json.loads(granola_data_raw)
            message = build_message_from_granola_data(granola_data)
        except json.JSONDecodeError:
            message = build_mar17_message()
    else:
        message = build_mar17_message()

    print("Sending daily summary to Slack...")
    print(f"Channel: {SLACK_CHANNEL}")
    print(f"Message length: {len(message)} chars")
    print("---")
    print(message)
    print("---")

    try:
        result = send_slack_message(token, SLACK_CHANNEL, message)
        if result.get("ok"):
            print(f"✅ Message sent successfully! ts={result.get('ts')}")
        else:
            print(f"❌ Slack API error: {result.get('error')}")
            sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP error: {e.code} {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
