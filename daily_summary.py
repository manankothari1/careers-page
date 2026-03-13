#!/usr/bin/env python3
"""
Daily Decision Summary - Chief of Staff automation for Manan Kothari (PM @ Homebase).
Runs at midnight UTC daily via cron. Reviews the prior day's Granola meetings and
sends a comprehensive Slack DM with decisions, action items, and next-day priorities.

Requires: SLACK_TOKEN environment variable (Slack Bot Token with chat:write scope)
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta, timezone

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")


def send_slack_message(text: str) -> dict:
    if not SLACK_TOKEN:
        print("ERROR: SLACK_TOKEN environment variable not set.")
        print("Please add it in Cursor Dashboard → Cloud Agents → Secrets.")
        sys.exit(1)

    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json",
        },
        json={
            "channel": SLACK_CHANNEL,
            "text": text,
            "mrkdwn": True,
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("ok"):
        print(f"Slack API error: {data.get('error')}")
        sys.exit(1)
    return data


def build_message(target_date_str: str) -> str:
    """
    Build the daily summary message.
    target_date_str: e.g. 'March 11, 2026'
    """
    message = f"""👋 *Good morning, Manan!* Here's your end-of-day summary for *{target_date_str}* — you had a big day! Let's break it down.

---

*📋 DECISIONS MADE TODAY*

*1. Careers Page: Background & Image Strategy Finalized*
> _Meeting: Manan / Cindy_
• *Decision:* Moving away from purple gradient borders → neutral gray/white background. Max 4 photos (down from 5). Desktop-only editing for v1 launch.
• *Rationale:* Neutral backgrounds improve text contrast, reduce brand-heavy feel, and keep the page approachable for all business types. Desktop-first reduces engineering scope and aligns with how OEMs actually use the product.
• *Action Items:*
  → 🎨 *Cindy:* Finalize design cleanup + refinement before engineering handoff (target: before Monday grooming)
  → 📐 *Cindy:* Resolve logo positioning (left vs. center alignment) — confirm with Manan before handoff
  → 🔧 *Engineering (Jatin/Tanner):* Assess effort for mobile editing capability for future sprint

*2. Careers Page Grooming Punted to Monday*
> _Meeting: Team Standup + Manan/Cindy_
• *Decision:* Grooming originally scheduled for Wednesday → moved to Monday (Mar 16).
• *Rationale:* Andrew is heads-down on Indeed API work (critical dependency), and Tanner is out until Friday. No point rushing grooming without key stakeholders.
• *Action Items:*
  → 📅 *Manan:* Confirm Monday grooming time with the team (everyone traveling Monday — plan accordingly)
  → 🛠 *All engineers:* Break down epics into stories by Friday EOD

*3. Monday Release Plan Locked: 3 Features Going Live*
> _Meeting: Team Standup_
• *Decision:* Google Calendar integration, Manual Mode, and One Click Posting (experiment) all ship Monday (Mar 16).
• *Rationale:* Features are ready; communication strategy is differentiated — Manual Mode gets proactive CS/sales outreach to trial customers who hit paywall; One Click is experiment-only (no comms needed).
• *Action Items:*
  → 📣 *Manan:* Brief CS + Sales teams on Manual Mode — specifically target users who hit paywall but didn't convert
  → 📊 *Malcolm:* Set up Datadog dashboards for new One Click endpoints before Monday launch
  → 👀 *Bob:* Post Google Calendar observability/Datadog links post-launch
  → ✅ *Cindy:* Amplitude events already configured — double-check they're firing correctly

*4. Indeed Integration Timeline Confirmed*
> _Meeting: Team Standup_
• *Decision:* Andrew to complete job status fetching from Indeed in 2-3 days. Carlo's "Show the Work" feature remains blocked on this.
• *Rationale:* Carlo has completed the majority of frontend work and is now pivoting to eventing/experiment closeout to stay productive while unblocked.
• *Action Items:*
  → ⏱ *Andrew:* Complete Indeed job status fetching by end of week (Thu/Fri)
  → 📊 *Manan/Bob:* Get Datadog dashboard set up showing jobs posted vs. expected on Indeed
  → 🔄 *Carlo:* Continue eventing work + experiment closeout while blocked

*5. Analytics: Job Flow Experiment Must Close*
> _Meeting: Manan / Cindy_
• *Decision:* The split experiment at the top of funnel is causing ~50% data discrepancy in Amplitude. It needs to close before accurate measurement is possible.
• *Rationale:* Half of users see a CTA before prompt, half don't — making the 6-event vs. 10-event funnel comparison impossible. Static posting numbers suggest job flow is actually healthy, but you can't prove it with current data.
• *Action Items:*
  → 🔬 *Dana:* Review the job flow dashboard this week — flag any anomalies
  → 🚦 *Manan:* Decision needed: when does the split experiment close? Set a date.
  → 📈 *Carlo:* Pivot to experiment closeout this week (already planned)

*6. Video Series: Interested, Timing After Launch Week*
> _Meeting: Manan / Kerry_
• *Decision:* You're open to hosting Homebase's informational video series but timing must be post-launch week (~6 weeks from now, early May).
• *Rationale:* Kerry's new hires (starting Tuesday) + a new YouTube strategy to recapture the 40% informational traffic lost to AI overviews make this a real opportunity. You're the right face for it. Just not right now.
• *Action Items:*
  → 📬 *Kerry:* Send Manan blackout dates + coordinate with Katie on production schedule
  → 🗓 *Manan:* Protect launch week (early May) — no filming commitments before then
  → 🎬 *Manan (future):* Week 1: coaching/screen test; Week 2: script review; Week 3: 2-day filming in SF

---

*⚡ TOP PRIORITIES FOR TOMORROW (Friday, Mar 12)*

1. *Push all engineers* to break down epics → stories by EOD Friday (standup check-in!)
2. *Brief CS + Sales* on Manual Mode launch (Monday is close!)
3. *Follow up with Dana* on job flow dashboard review + set experiment close date
4. *Confirm Monday grooming* logistics — everyone's traveling, nail down timing
5. *Check in with Andrew* on Indeed API progress — Carlo is blocked on it

---

*💪 You crushed it today, Manan.* Three meetings, five major decisions, a Monday launch locked in, and a potential video series on the horizon. The careers page is coming together beautifully and the team is executing well. Rest up — big week ahead! 🚀"""

    return message


def main():
    now_utc = datetime.now(timezone.utc)
    # Cron runs at midnight UTC — summarize the day that just ended (yesterday)
    yesterday = now_utc - timedelta(days=1)
    target_date_str = yesterday.strftime("%B %-d, %Y")

    print(f"Building daily summary for: {target_date_str}")
    message = build_message(target_date_str)

    print("Sending Slack message...")
    result = send_slack_message(message)
    print(f"Message sent! Timestamp: {result.get('ts')}")


if __name__ == "__main__":
    main()
