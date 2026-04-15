#!/usr/bin/env python3
"""Daily Chief of Staff summary for Manan Kothari -- Apr 15, 2026 (covering Apr 14 meetings)."""

import json
import os
import urllib.request

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

d1 = (
    "*Decision 1 -- 3LO ships with 3 entry points (to-do, job page, boost modal)* :electric_plug:\n"
    "_Meeting: 3LO Grooming + Jeff/Manan 1:1_\n\n"
    "*Why:* Maximizes surface area for Indeed connection without forcing a single funnel. "
    "To-do uses 1/7/14-day cadence (dismissible), job page surfaces via the 'Posted to X boards' modal, "
    "boost modal adds Indeed alongside Craigslist/ZipRecruiter. All roads lead to OAuth.\n\n"
    "*Rationale:* Meeting customers where they are = higher activation. A single entry point risks burying it.\n\n"
    ":white_check_mark: *Action -- Manan:* Send full 3LO spec doc to team as a pre-read *TODAY*\n"
    ":white_check_mark: *Action -- Manan:* Confirm CS escalation process with Michael for 12-hr+ job-sync delays\n"
    ":white_check_mark: *Action -- Jeff:* Create SendGrid email templates (job-live confirmation + delay notification w/ 3 common reasons + alt actions)\n"
    ":white_check_mark: *Action -- Jeff:* Update job boards modal copy: capitalize 'Jobs' in Facebook Jobs, swap Craigslist -> JobGet (capital J+G), alphabetical sort w/ live integrations surfaced first\n"
    ":white_check_mark: *Action -- Andrew:* Hand off 3LO auth GitHub repo to Tanner for front-end experimentation\n"
    ":white_check_mark: *Action -- Tanner:* Pick up front-end 3LO work as Andrew transitions out"
)

d2 = (
    "*Decision 2 -- 1-2 hr 'syncing' buffer state after successful Indeed auth* :hourglass_flowing_sand:\n"
    "_Meeting: 3LO Grooming_\n\n"
    "*Why:* Race condition -- Indeed doesn't push notifications back to Homebase. We must poll/fetch to confirm "
    "a job is live before showing a live link. Showing a dead link immediately post-auth destroys trust.\n\n"
    "*Rationale:* Better to set clear expectations ('your job is being synced, check back in ~1-2 hrs') than show "
    "a broken state. 12-hr escalation is the safety net.\n\n"
    ":white_check_mark: *Action -- Jeff/Andrew/Tanner:* Implement 'syncing' UI state (spinner/pending copy) that resolves only after confirmed live fetch\n"
    ":white_check_mark: *Action -- Jeff:* Finalize boost modal copy + pull Indeed boost pricing for CTA "
    "(current '8x more candidates' messaging needs revision -- it's out of scope for 3LO but don't let it ship stale)"
)

d3 = (
    "*Decision 3 -- No in-product disconnect button for 3LO v1* :lock:\n"
    "_Meeting: 3LO Grooming_\n\n"
    "*Why:* Revoked tokens from Indeed's side return unauthorized responses without notifying Homebase. "
    "Building an in-product disconnect adds scope; graceful fallback (remove to-dos when unauthorized, "
    "keep auth entry points available) covers the edge case without shipping complexity.\n\n"
    "*Rationale:* Ship velocity > edge-case polish in launch week. Users can revoke directly via Indeed account settings.\n\n"
    ":white_check_mark: *Action -- Engineering:* Implement graceful fallback for revoked tokens "
    "(remove to-dos, keep entry points, don't surface auth errors to end user)"
)

d4 = (
    "*Decision 4 -- Resume scoring paused; launch week priority flipped to archived employees + recurring applicants* :arrows_counterclockwise:\n"
    "_Meeting: Applied AI Jam (w/ Ted, Fadi, Divij, Dana)_\n\n"
    "*Why:* Current resume scoring flags 76% of candidates as top matches with an 86% false positive rate -- "
    "only 15% of those actually move forward. Thresholds will ship as-is (screener: 0.1 individual / 0.3 avg). "
    "Meanwhile, 90k applicants in the past 30 days are sitting untapped. 10% re-engagement = 9k new applicants. "
    "That's a bigger needle-mover than incremental scoring tuning right now.\n\n"
    "*Rationale:* Maximize launch week impact by unlocking the largest existing pool first. "
    "Scoring can be recalibrated post-launch with better ground truth.\n\n"
    ":white_check_mark: *Action -- Divij:* Run simulation with updated screener thresholds (0.1 individual, 0.3 average) -- confirm final resume threshold from simulation\n"
    ":white_check_mark: *Action -- Divij:* Switch to archived employees / recurring applicants work *starting tomorrow (Apr 15)*\n"
    ":white_check_mark: *Action -- Manan:* Provide predicted role documentation to Divij + intro Divij <-> Nelson\n"
    ":white_check_mark: *Action -- Manan + Team:* Schedule 20-min alignment call tomorrow to lock new priority order\n"
    ":white_check_mark: *Action -- All:* Manual resume scoring exercise (50-100 samples across roles/biz types) for future calibration -- assign owner + schedule"
)

d5 = (
    "*Decision 5 -- Dynamic thresholding rejected; tiered matching (great/good/poor) deferred to V2* :dart:\n"
    "_Meeting: Applied AI Jam_\n\n"
    "*Why:* Dynamic thresholds based on applicant flow volume would score identical candidates differently "
    "depending on when they apply -- that's a UX nightmare and legally murky. "
    "Tiered matching is the right end state but adds candidate profile redesign scope.\n\n"
    "*Rationale:* Consistency > cleverness for v1. Deferred to V2 with candidate profile redesign.\n\n"
    ":white_check_mark: *Action -- Manan:* Document tiered matching (great/good/poor) as a V2 spec item -- don't let it disappear into the ether"
)

d6 = (
    "*Decision 6 -- Homebase Boost: $50 product, selective deployment (not blanket trial giveaway)* :moneybag:\n"
    "_Meeting: Applicant Flow Brainstorm (w/ Matan, Ray)_\n\n"
    "*Why:* Blanket deployment to all 5k trial users x 2 jobs = up to $500k/month in spend -- not viable. "
    "Selective criteria (day-2 performance trigger: <15 applicants) targets jobs most likely to convert to healthy trials.\n\n"
    "*Rationale:* Quality over quantity. Boost should be a conversion lever, not a fire hose. "
    "$50 at 50c CPC ($1.80/applicant rate target) beats current $35 Taru spend for ranking.\n\n"
    ":white_check_mark: *Action -- Matan:* Survey customers on current hiring spend + applicant sources (critical for boost messaging + ICP validation)\n"
    ":white_check_mark: *Action -- Team:* Finalize boost messaging strategy and UI requirements (attribution: boosted vs unboosted performance must be clearly shown)\n"
    ":white_check_mark: *Action -- Engineering:* Define sophisticated job selection criteria for boost deployment (day-2 trigger logic)\n"
    ":white_check_mark: *Action -- Manan:* Validate Indeed 'first-party publisher' hypothesis -- confirm whether Homebase ATS-posted jobs rank lower than direct employer posts on Indeed "
    "(test: post next 150 jobs directly on Indeed once 3LO is live)"
)

d7 = (
    "*Decision 7 -- Predicted roles + Facebook job logos/images are high-priority launch week add-ons* :chart_with_upwards_trend:\n"
    "_Meeting: Applicant Flow Brainstorm + Applied AI Jam_\n\n"
    "*Why:* Predicted roles model is ready -- just needs front-end exposure. "
    "Critical for trial conversion and careers page appeal. "
    "Facebook job logos have a clear, measurable yield improvement (images ready to ship).\n\n"
    "*Rationale:* Both are low-lift, high-signal features that can move the needle without adding engineering risk to launch week.\n\n"
    ":white_check_mark: *Action -- Manan:* Drive alignment meeting with Ted + Divij to prioritize predicted roles for launch week (already scheduled per notes)\n"
    ":white_check_mark: *Action -- Engineering:* Expose predicted roles model on front end\n"
    ":white_check_mark: *Action -- Engineering:* Implement Facebook job logos/images (clear yield improvement, assets ready)"
)

open_items = (
    "*:rotating_light: Still On Your Plate -- Don't Drop These*\n\n"
    "- *TLWA Launch Week Brief -> Ted* -- NOW *12 DAYS OVERDUE*. Send it.\n"
    "- *Homebase Boost SKU kick-off w/ Chris McIntosh* -- billing window is closing *now*. Unblock this.\n"
    "- *Manual Mode green light* -- Cindy's QA is done. It's on you. Say go.\n"
    "- *Nelson: metro_area + bucketed_role + matching_roles columns* -- overdue since Apr 8. Check in.\n"
    "- *Supabase tables + 60k upsert* -- you need to build this.\n"
    "- *TLWA careers page QA w/ Fadi* -- before 50k QR codes go out.\n"
    "- *IBK/Izzy mobile TLWA version* -- Jeff's designs ready, send to IBK/Izzy.\n"
    "- *Andrew: company-level vs location-level Indeed connection answer* -- resolve in grooming.\n"
    "- *Justin: re-run company descriptions batches 93-100 + QA sample* -- confirm still on track.\n"
    "- *Minh + Manan: Supabase remediation sync (INC-372)* -- still open."
)

footer = (
    "*Manan, you had a genuinely great day.* You made hard calls (killed dynamic thresholding, "
    "deprioritized resume scoring tuning to chase a bigger fish), kept 3LO on track with real engineering clarity, "
    "and framed the Boost strategy around ROI discipline rather than spray-and-pray. "
    "That's exactly the kind of PM judgment that builds products people trust. "
    "Tomorrow: lock the alignment call, unblock Divij, send that TLWA brief, and greenlight Manual Mode. "
    "You've got this. :muscle:"
)

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Your Tuesday, Apr 14 -- Decision Brief", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! Big day -- you had *5 meetings* (Jeff/Manan 1:1, 3LO Grooming x2, "
                "Applicant Flow Brainstorm, Applied AI Jam). Here's every decision you made, "
                "why you made it, and exactly what needs to happen next. You crushed it today. :rocket:"
            )
        }
    },
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d1}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d2}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d3}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d4}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d5}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d6}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": d7}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": open_items}},
    {"type": "divider"},
    {"type": "section", "text": {"type": "mrkdwn", "text": footer}},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": (
                    ":notepad_spiral: Sourced from: Jeff/Manan 1:1 * 3LO Grooming * "
                    "Applicant Flow Brainstorm * Applied AI Jam -- Apr 14, 2026 | Chief of Staff Auto-Briefing"
                )
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Apr 14 Decision Brief is ready -- 7 decisions, 20+ action items. Have a great evening!",
    "blocks": blocks
}


def send_slack(p, token):
    data = json.dumps(p).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


if not SLACK_TOKEN:
    print("=" * 70)
    print("SLACK_TOKEN not set -- PREVIEW MODE (message not sent)")
    print("=" * 70)
    print(json.dumps(payload, indent=2))
    print("\nTo send for real: export SLACK_TOKEN=xoxb-... and re-run.")
    raise SystemExit(0)

result = send_slack(payload, SLACK_TOKEN)
if result.get("ok"):
    print(f"Message sent successfully! ts={result.get('ts')}")
else:
    print(f"Slack API error: {result.get('error')}")
    print(json.dumps(result, indent=2))
    raise SystemExit(1)
