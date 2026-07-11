#!/usr/bin/env python3
"""Daily Chief of Staff Digest — Jul 10, 2026 (Thu PDT)"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest — Thu Jul 10, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day — three solid meetings, a crisp set of decisions, and some real momentum on the roadmap. Here is everything that mattered today, with your clear next moves. You are crushing it."
        }
    },
    {"type": "divider"},

    # ── MEETING 1: Hiring Team Check-in ──────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 1: Hiring Team Check-in (10:00 AM PDT)*\n_Attendees: Ray, Jatin, Matan, Fadi, Tanner, Dana, Divij, Usman, Nelson + full team_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 1 — V1 Deprecation July 20 is LOCKED*\nAll remaining V1 customers migrate to free V2 on Jul 20. Expired jobs get closed. Comms are in place: email, in-product banner, and a V2 onboarding tour on first login. CS is empowered to extend trials — they should ask customers why they want one before granting.\n*Why it matters:* 10 days out. No more debate. Execution mode only."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 2 — $30 Plan Removed from Product*\nIn-product focus is now $100 and $200 plans only. Sales can still offer $30 for franchises and edge cases, but it is off the table in-product. Removal of $30 is already net positive: higher ASP with only a small conversion dip.\n*Why it matters:* Cleaner pricing story, better margins, simpler experimentation going forward."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 3 — 'Personal Recruiter' Messaging RETIRED for Internal Customers*\nTesting done. Works for cold/net-new audiences (strong Meta signal), but does NOT resonate with existing Homebase customers not yet using hiring. New direction: 'We already know your business' angle. Zero state page, nudges, and emails being updated for ICP focus.\n*Why it matters:* Stops wasting cycles on a message that does not land. Now running two live experiments with the new framing."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 4 — Resume Matching: Match on Resume OR Screener (Not Both Required)*\nResume in match score increases OEM move-forward rate ~100% but significantly reduces total matches shown. Next phase: require resume OR screener OR both — not demanding both at once. This recovers match volume while keeping quality signal.\n*Why it matters:* Directly improves healthy job rate for the ~60% of jobs with resumes."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 5 — Pricing Page: Full-Page Takeover Live*\nNew pricing page replaces the right-drawer. Manual mode is now surfaced as a free option (was previously hidden). More room for value prop, easier to run pricing experiments.\n*Why it matters:* Foundational infrastructure change that unlocks future pricing tests."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 6 — Scheduling UX Changes Locked*\nTwo changes shipping: (1) availability no longer required when posting a job, and (2) OAMs can now suggest specific interview times — not just send a booking link. Also: domain events for job post flow enable posting from within Homebase Assistant.\n*Why it matters:* Reduces friction in the posting and scheduling flow; unblocks Assistant integration."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 7 — Line Cook Remains the #1 Priority Lever*\nOnly 7% of line cook jobs reach healthy by D30 vs 35-50% for barista, counter service, and server. Culinary Agents and Collider agents are the active bets to close that gap.\n*Why it matters:* Until line cook moves, the Q3 goal of 50% healthy line cook jobs stays at 7%. This is the unlock."
        }
    },
    {"type": "divider"},

    # ── MEETING 2: Rami / Manan ───────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 2: Rami / Manan 1:1 (10:30 AM PDT)*\n_Attendees: Rami Abou-Seido_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 8 — Priority Order Locked: Salary Recs First*\nSprint order: salary recommendations → job descriptions → talent pool experimentation. Rami to scope salary rec work and deliver update by EOD Monday Jul 13. He is switching focus to salary THIS afternoon and deprioritizing job descriptions for now. Team presentation: Wednesday Jul 15.\n*Why it matters:* Rami was the blocker — you forced the prioritization call today. Salary recs before talent pool means the DS dependency no longer holds up product eng."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 9 — Salary Analysis Validated: Market Rate Drives Applicants*\nYour analysis (normalizing by role type and MSA) confirmed: jobs well below market get 26.1% with 20+ applications; at market = ~7-8% bump; well above market = ~12% bump. Rami has a separate company-level normalization table. Role normalization will use shortcut approach for now (match against existing table; new jobs without records get no recommendation), but full normalization is the eventual path.\n*Why it matters:* Strong signal that salary recs will meaningfully move healthy job rate."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 10 — Talent Pool Segmentation Experiment Design Locked*\nSegment by: (1) employer type (previous applicants vs. archived employees) and (2) hiring role. Line cook = primary focus. Barista and cashier as secondary learnings. Multi-job support punted until after recency experiment. Run subject line test in parallel: recruiter winner vs. recruiter with job-specific subject line (e.g. 'Barista at Bob's Burgers opportunity'). Primary metric = open rate via Iterable.\n*Why it matters:* Tight scope means faster learnings. Subject line test is low-effort parallel signal."
        }
    },
    {"type": "divider"},

    # ── MEETING 3: Comms Agent ────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 3: Comms Agent Path Forward (11:45 AM PDT)*\n_Attendees: Dana Lobo, Divij Gupta, Bob Gao, Jatin Bhandari_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 11 — Screener is the MVP Scope (Not Scheduling)*\nAligned on screener-only MVP. Your rationale: candidate experience follows chronological order — screener first, then scheduling, then show-up recovery. Screener-only = no write operations needed, just inbound Q&A + link delivery. This is the right cut.\n*Why it matters:* Limits surface area, unblocks sooner, and tests the hypothesis (screener completion from ~40%) before committing to full pipeline integration."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 12 — Comms Agent Work PAUSING to Prioritize Resume Feature*\nDivij ships the internal screener demo on Databricks first (natural stopping point covering the full screener flow end-to-end). Then work pauses. Comms agent discussions continue async while resume work is in progress.\n*Why it matters:* Clean handoff, no half-finished work, and you protect the resume roadmap priority."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 13 — AI Disclosure Not a Current Blocker*\nTeam aligned: the AI disclosure legal requirement applies to screening decisions, not conversational agents. Homebase already discloses AI use to candidates. This is a company-level policy question — Ray raises with execs if needed. Team proceeds with testing in the meantime.\n*Why it matters:* Removes a potential blocker and keeps the team unblocked on the demo. You flagged it, got the answer, moved on. Good call."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *DECISION 14 — Comms Agent Opening Message Must Signal Two-Way Conversation*\nYou flagged: the current opening message reads as one-way/automated, which reduces engagement. Candidates need to know they can ask questions back. This gets fixed before the internal demo ships.\n*Why it matters:* If the first message feels like a notification, candidates disengage. This is a conversion lever."
        }
    },
    {"type": "divider"},

    # ── MANAN'S ACTION ITEMS ──────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*YOUR ACTION ITEMS — Manan*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *P0 — Provide UTMs to Rami for Talent Pool Segmentation Experiment*\nRami needs these for recency experiment tracking across segmented buckets. He is ready to go. Do not let this block him.\n:calendar: *Target: ASAP — before he starts experiment setup*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *P0 — Loop in Paul or Kan (Data Platform) on Salary Rec Role Normalization*\nData platform involvement is required whether you use the shortcut mapping or a full normalization script. Rami's scope depends on knowing which path you are taking.\n:calendar: *Target: Monday Jul 13 (before Rami's scope is due)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *P0 — Check: Did Carlo Hit the Harness/OpenSpec Deadline?*\nThis was flagged as DEADLINE TODAY Jul 10. Need confirmation it shipped or know what the blocker is.\n:calendar: *Target: End of day today — check Slack/Linear*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *P1 — Review Rami's Salary Analysis Doc*\nRami shared his findings; Manan shared his. Confirm alignment before the Jul 15 presentation.\n:calendar: *Target: Monday Jul 13*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *P1 — Prep Jul 15 Team Presentation (Salary Recs + JD Updates)*\nWednesday Jul 15 is the milestone. Make sure Rami's scope and your analysis are synthesis-ready.\n:calendar: *Target: Tue Jul 14 EOD for prep*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *P1 — Source Claiming Banner E2E Sign-Off*\nMatan has been blocked since Jul 8. This is still open.\n:calendar: *Target: Monday Jul 13 — unblock Matan*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *P1 — FFH Health Dip Investigation with Ugu*\nJuly 20 cutover is 10 days away. The V1→V2 duplicate flag hypothesis is still unconfirmed. Nelson is digging into the May 15-21 cohort. You need the Ugu thread closed before migration day.\n:calendar: *Target: Monday Jul 13*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_blue_circle: *P2 — Chat Ray About Rami DS Capacity*\nRami is now in a better position (salary recs scoped, priorities set), but the pattern of DS being a bottleneck is structural. Worth a quick sync with Ray to align on Rami's bandwidth going into next sprint.\n:calendar: *Target: This week*"
        }
    },
    {"type": "divider"},

    # ── DELEGATIONS ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*DELEGATIONS — Things Others Own*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Rami:* Scope salary recommendation work → deliver EOD Mon Jul 13; switch to salary today\n• *Divij:* Update comms agent doc to scope MVP to screener only; ship internal demo on Databricks\n• *Anyone/Divij:* Investigate inbound SMS provider capability for two-way messaging\n• *Ray:* Raise AI disclosure question with execs if needed\n• *Nelson:* May 15-21 FFH cohort dip investigation (ongoing)\n• *Fadi:* Source Claiming first-pass design (target: Tuesday Jul 14)\n• *Carlo:* Harness/OpenSpec — DEADLINE TODAY (confirm status)\n• *Matan:* Track B source claiming — is it started?"
        }
    },
    {"type": "divider"},

    # ── WATCH LIST ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WATCH LIST — Things to Monitor*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *July 20 V1→V2 Cutover — 10 days out.* Comms in place, CS empowered. Stay close to Ugu on the FFH health dip. Do not let the duplicate flag hypothesis go uninvestigated this close to migration.\n\n:rotating_light: *FFH D5 Zero-Applicant Rate: 41%.* Q3 target is <10%. V1→V2 may be actively worsening this. This is the highest-leverage metric right now.\n\n:rotating_light: *Line Cook Jobs Healthy: 7% (Q3 target 50%).* Culinary Agents and Collider agents are the bets. Keep a close eye on early signals.\n\n:warning: *Boost Bug: Still Unresolved.* Revenue-impacting, 2 reporters. Needs an owner and a fix.\n\n:warning: *Dana Leaving End of September.* Succession planning not started. Worth flagging to Ray in the near term.\n\n:white_check_mark: *Screener Personalization Rollout.* Recent results look strong post-100% rollout. Still verifying — keep an eye on data this week."
        }
    },
    {"type": "divider"},

    # ── BIG PICTURE ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THE THEME OF TODAY*\nToday was about *sequencing and scope*. You made three crisp calls that will save weeks: (1) salary recs before talent pool — Rami has a clear runway, (2) screener before scheduling for the comms agent — right order, right scope, (3) 'personal recruiter' messaging retired — you stopped the team from continuing down a dead end. These decisions compound. Great work."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Sleep well, Manan. Tomorrow is Friday — a good day to close the Carlo thread, get the UTMs to Rami, and loop in Paul/Kan. You have got this. :muscle:"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Digest — Thu Jul 10, 2026 — 14 decisions, 7 action items."
}


def preview():
    out = "\n===== SLACK PREVIEW — Jul 10, 2026 =====\n"
    for b in blocks:
        if b.get("type") == "header":
            out += "\n### " + b["text"]["text"] + " ###\n"
        elif b.get("type") == "section":
            out += b["text"]["text"] + "\n\n"
        elif b.get("type") == "divider":
            out += "---\n"
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + TOKEN
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("SUCCESS: Slack message sent to", CHANNEL)
            else:
                print("SLACK ERROR:", body.get("error"), body)
                sys.exit(1)
    except urllib.error.URLError as e:
        print("NETWORK ERROR:", e)
        sys.exit(1)


if __name__ == "__main__":
    if not TOKEN:
        print("No SLACK_TOKEN found — printing preview only.")
        preview()
    else:
        preview()
        send()
