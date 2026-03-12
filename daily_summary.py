#!/usr/bin/env python3
"""
Daily Chief of Staff Summary - Sends Slack DM to Manan with day's decisions & action items.
Requires SLACK_TOKEN environment variable (Slack Bot Token with chat:write scope).
"""
import os
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_CHANNEL = "D06E4QMHCNN"

def send_daily_summary():
    token = os.environ.get("SLACK_TOKEN")
    if not token:
        print("ERROR: SLACK_TOKEN environment variable not set.")
        print("Please add your Slack Bot Token as a secret named SLACK_TOKEN in the Cursor Dashboard.")
        sys.exit(1)

    client = WebClient(token=token)

    message = build_message()

    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message,
            mrkdwn=True
        )
        print(f"Message sent successfully! ts={response['ts']}")
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        sys.exit(1)


def build_message():
    return """\
:wave: *Hey Manan! Here's your Daily Decision Digest for Wednesday, March 11* :brain::fire:

You crushed it today — 3 meetings, a ton of forward motion across multiple workstreams. Here's your full rundown:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:busts_in_silhouette: *1:1 with Cindy | 9:30 PM*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*Decisions Made:*

:white_check_mark: *Careers Page: Ditch the purple gradient, go neutral*
→ _Rationale:_ The brand-heavy purple background was creating text contrast issues and didn't scale well for the customizable careers page experience. Neutral gray/white is safer and cleaner.
→ *Action:* Cindy to finalize neutral background options and flag any remaining text contrast issues before engineering handoff.

:white_check_mark: *Max 4 images on careers page (down from 5)*
→ _Rationale:_ Simpler auto-sizing logic with 4 images, cleaner UX.
→ *Action:* Cindy to implement hover add/delete states and auto-sizing for 1–4 image configurations.

:white_check_mark: *Desktop-only editing for initial release; mobile = preview only*
→ _Rationale:_ OEMs predominantly edit on desktop. Mobile editing adds engineering complexity and risk to the launch timeline. Ship what matters first.
→ *Action:* Get engineering effort estimate from Bob/Tanner for mobile editing (future sprint consideration).

:white_check_mark: *Careers Page Grooming punted to Monday*
→ _Rationale:_ Andrew is head-down on Indeed API work, Tanner is out until Friday. No point grooming without the right people in the room.
→ *Action:* You + Andrew + Tanner to align on grooming session for Monday. Note: everyone is traveling Monday — coordinate timing carefully.

:warning: *Watch Item — Job Flow Analytics Discrepancy*
→ Amplitude data shows artificially low job flow numbers (~50% of actual), caused by the split experiment at the top of funnel AND mismatched event structures (6 events old vs 10 events new).
→ *Action:* Close the split experiment so you get clean comparable data. Dana's dashboard needs review this week — loop her in.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:people_holding_hands: *Hiring Team Standup | 8:30 PM*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*Decisions Made:*

:white_check_mark: *Monday Release: Google Calendar + Manual Mode + One Click Posting (experiment)*
→ _Rationale:_ These three features are ready or nearly ready. Coordinating a single release event reduces deployment noise.
→ *Actions:*
  • Malcolm to complete Datadog dashboards for new endpoints before Monday
  • Bob to post Google Calendar observability links post-launch
  • CS + Sales team comms drafted for Manual Mode (target: users who hit paywall but didn't convert)
  • No comms needed for One Click (it's an experiment only)

:white_check_mark: *All engineers to break down epics into stories by Friday EOD*
→ _Rationale:_ Sprint planning alignment requires granular story-level tickets before the next sprint kicks off.
→ *Action:* You and Bob to meet before Friday to confirm implementation plan is aligned. Follow up with each engineer if tickets aren't broken down by Thursday EOD.

:white_check_mark: *Indeed Integration: Andrew continues job status fetching work (2-3 days)*
→ _Rationale:_ Core dependency for the "Show the Work" feature. Carlo is blocked on Andrew's API — this unblocks him.
→ *Action:* Andrew to complete by Thursday/Friday. Carlo pivots to eventing work + experiment closeout in the meantime. Bob to add Datadog dashboard for jobs posted vs expected.

:white_check_mark: *Show and Tell Friday needs more engineering demos*
→ _Rationale:_ Engineering demos drive team visibility and energy. Right now there's a gap.
→ *Action:* Nudge 1-2 engineers to prep a quick demo for Friday. Divij's resume matching work or Sharmin's Deal Breakers frontend are good candidates.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:video_camera: *1:1 with Kerry (Video Chats) | 5:30 PM*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*Decisions Made:*

:white_check_mark: *You're (likely) in for the video series — after launch week*
→ _Rationale:_ Katie flagged you as the right face for Homebase product education content. The series targets basic product topics to recapture the 40% informational traffic lost to AI overviews. You're interested but appropriately protecting launch week (6 weeks out).
→ *Action:* Kerry to send blackout dates + coordinate with Katie. You're clear to engage *after* the careers page / QR code launch week. ~Week of April 21+.

:white_check_mark: *Core Web Vitals issues: explore alternative domain strategy*
→ _Rationale:_ 1,200 thin-content hiring pages are hurting domain authority. Using `joinhomebaseapp.com` (from John's collection) to host job listings could protect the main domain while new careers pages are built out.
→ *Action:* Loop in Kerry + engineering to evaluate domain migration feasibility. The redesigned careers/job pages currently in development should help — ensure this is on the careers page launch scope radar.

:white_check_mark: *Kerry's team grows next Tuesday (+2 hires)*
→ Two new folks starting: full-time hire from Kerry's network + contract content marketer (Bubble skills, Phil referral).
→ _No immediate action needed_ — good to know for marketing velocity expectations going up.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:dart: *YOUR TOP 5 PRIORITIES FOR TOMORROW (Thursday, March 12)*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. :one: *Close the job flow split experiment* — you can't measure the funnel accurately until it's closed. Unblock analytics clarity ASAP.
2. :two: *Confirm Monday release readiness* — check in with Malcolm (Datadog dashboards), Bob (Google Calendar observability), and make sure CS/Sales comms are drafted.
3. :three: *Ticket breakdown check-in* — remind engineers (especially Malcolm, Iszael, Divij) that stories need to be broken down from epics by Friday.
4. :four: *Align with Bob on Monday grooming logistics* — everyone's traveling, so nail down the time/format now.
5. :five: *Loop Dana in on the Amplitude dashboard review* — job flow analytics need a fix and she built it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You made a *ton* of smart calls today, Manan — protecting launch week, unblocking engineers before they stall, and locking in the right design tradeoffs on careers page. The Monday release is shaping up well. Keep the momentum going tomorrow — you're building something special at Homebase. :homebase::rocket:

_— Your Chief of Staff_"""


if __name__ == "__main__":
    send_daily_summary()
