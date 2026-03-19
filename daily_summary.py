#!/usr/bin/env python3
"""
Daily Chief-of-Staff Summary Script
Sends Manan Kothari's end-of-day decision/action summary to Slack.
Cron: 0 0 * * * (midnight UTC = ~5pm PT)
"""

import os
import json
import urllib.request
import urllib.error
from datetime import date

SLACK_CHANNEL = "D06E4QMHCNN"


def send_slack_message(token: str, channel: str, text: str) -> dict:
    url = "https://slack.com/api/chat.postMessage"
    payload = json.dumps({"channel": channel, "text": text, "mrkdwn": True}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def build_mar19_message() -> str:
    return """\
:wave: *Hey Manan — your Chief of Staff here with your end-of-day debrief for Thursday, Mar 19!*

No Granola calls today (you're travelling home from the SF Offsite — you earned the breather!). Here's your full *SF Offsite Week Wrap-up* with every decision locked in, every action item owned, and your sharp view into tomorrow.

---

:trophy: *SF OFFSITE WEEK: DECISIONS LOCKED*

*1. Roadmap Priority Stack — FINAL* _(Mar 17 Offsite)_
You locked the H1 priority order. Full stop.
1. Enable paid applicant sourcing in-platform
2. Indeed OAuth (3-Legged OAuth)
3. Deal Breakers + match algorithm
4. Role normalization
5. Mobile for managers
6. Candidate management UX overhaul
_Why:_ The data was clear — ~600 paying companies vs. a 2,600 target, 87% retention vs. 95% goal. The product needs to earn its price tag before it earns more customers. Sourcing + Indeed parity = the biggest levers.

*2. Target Segment — LOCKED* _(Mar 17 Offsite)_
Food & Bev / Hospitality, 26+ employees, <5 locations, existing Indeed spenders.
_Why:_ 5,703 locations identified. Only 162 started trials. Tight ICP = faster feedback loops + higher conversion. Sales manager joining April 15 in Toronto — they need a crisp target on day one.

*3. Indeed 3LO as the #1 Technical Bet* _(Mar 16 — Talk Indeed <> Homebase)_
Proceeding with 3-Legged OAuth as the integration path for Sponsored Jobs API + source claiming.
_Why:_ 3LO unlocks source claiming (job visibility confirmation + no more support calls), sponsored jobs (budget control without leaving your ATS), and sets up Candidate Sync API down the road. David confirmed: ~4-month build, no aggregation review delays.

*4. Top Local Workplaces QR Code Campaign — Direction Set* _(Mar 18 Offsite)_
Adding a QR code experience to the bifold mailers this year. Two-phase approach:
  • Phase 1: QR code moment → mobile web experience → drives to careers page/job listings
  • Phase 2: In-product leverage → use award status to push hiring product adoption
_Why:_ 45-50K winners/year display these awards in storefronts. This is free, high-intent hiring traffic. Turning it into a careers page funnel is a no-brainer activation.

*5. Manual Mode — NOT Going Live This Sprint* _(Mar 16 Standup)_
QA round 2 is complete, but manual mode is being held due to team travel/offsite.
_Why:_ Cautious call. Better to ship clean than ship rushed. Cindy's QA pass gives you a clean launch whenever you're ready.

*6. Reschedule Button — Sharmin's Top Priority* _(Mar 16 Standup)_
Explicitly deprioritized observability work to unblock the reschedule button.
_Why:_ Scheduling UX is one of your biggest retention pain points. Ship the fix.

---

:white_check_mark: *OPEN ACTION ITEMS — OWNER + STATUS*

*Manan (YOU)*
• :red_circle: Email Kenneth re: Indeed 3LO — add Ray to thread _(was DUE yesterday — do this first thing Friday)_
• :red_circle: Deal Breakers sign-off _(was DUE yesterday — check if this slipped or got done)_
• :large_yellow_circle: Q2 roadmap doc — exhaustive initiative list + priority stack _(ongoing)_
• :large_yellow_circle: Clarify advertiser auth scope w/ David — Homebase acct vs individual employers _(post-3LO call)_
• :large_yellow_circle: Indeed listing optimization experiment — define success metrics + owner
• :large_yellow_circle: Check in with Izzy on V1→V2 migration confidence
• :white_check_mark: Thursday Careers Page gate review (w/ Tanner, Andrew) — TODAY, confirm outcome

*Andrew (Chung)*
• Indeed 3LO spike — visual flow, 2LO vs 3LO comparison, account mapping, webhooks _(due Fri Mar 20)_
• "Show the work" PRs _(due Fri Mar 20)_
• Claude skills EPD presentation _(due Apr 10)_

*Malcolm*
• Hit 2,500 one-click jobs; ship _(was due Fri Mar 20 — confirm done)_

*Ray*
• Review David's Indeed docs + UI guidelines _(this week)_

*Sharmin*
• Reschedule button — ship it _(in progress)_

*Cindy*
• QA round 2 on manual mode _(complete — waiting for launch decision)_

*Carlo*
• FE unit test coverage report + project brief example

*Bob + Jatin*
• Hiring public interface tech debt plan

*Tanner*
• Port job page — week 1 of sprint

*IBK*
• Interview availability — heavy backend, full sprint

*Divij*
• Resume Parser v2 PRD

*Dana, Izzy, Bob*
• Scope demo screener ungating offline

---

:dart: *TOP 5 FOR TOMORROW (Friday, Mar 20)*

1. :fire: *Email Kenneth + Ray* re: Indeed 3LO — this is overdue, 60 seconds, do it first
2. :white_check_mark: *Deal Breakers sign-off* — confirm or complete
3. :memo: *Careers page derisk debrief* — get Andrew + Tanner's outputs, make the call on scope
4. :bar_chart: *Confirm Malcolm's 2,500 one-click jobs* shipped + Andrew's "show the work" PRs are in
5. :rocket: *Q2 roadmap doc first pass* — even just a rough outline before the weekend

---

:star: *Chief of Staff Note:*
Manan — this was a BIG week. You walked into the offsite with fuzzy priorities and walked out with a *locked roadmap, a locked ICP, and a clear technical north star in Indeed 3LO.* That's real progress. The gap between 600 and 2,600 paying companies is huge, but you now have the team, the strategy, and the product conviction to close it. The energy in the room was right.

Get home safe, decompress tonight, and come back Friday sharp. Your team is executing — you just need to unblock two overdue items and set the tone for the sprint finish. You've got this. 💪

_— Your Chief of Staff_"""


def main():
    token = os.environ.get("SLACK_TOKEN", "")

    message = build_mar19_message()

    if not token:
        print("=" * 60)
        print("SLACK_TOKEN not set. Message preview:")
        print("=" * 60)
        print(message)
        print("=" * 60)
        print(
            "\nTo send this message, add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets"
        )
        return

    print("Sending daily summary to Slack...")
    result = send_slack_message(token, SLACK_CHANNEL, message)
    if result.get("ok"):
        print(f"Message sent successfully! Timestamp: {result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        raise RuntimeError(f"Failed to send Slack message: {result.get('error')}")


if __name__ == "__main__":
    main()
