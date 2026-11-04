#!/usr/bin/env python3
"""
Nov 3, 2026 PST Daily Chief of Staff Digest for Manan Kothari
Meetings: Scheduling Deep Dive (10:45am), Availability Discussion (11:30am workspace), Tiger/Manan Job Posting Logic (1:00pm)
"""
import json
import os
import sys
import urllib.request

CHANNEL = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f4cb Chief of Staff Daily Digest \u2014 Tuesday, Nov 3, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! \U0001f44b Big day \u2014 you had *3 meetings* and walked out with one of the most consequential scheduling conversations you've had all quarter. "
                "Here's everything you decided, why it matters, and what you need to do next.\n\n"
                "*Day Grade: B+* \u2014 Strategic clarity gained on Nihilus, an engineering risk surfaced on Indeed, and you finally had the full scheduling deep dive with Skye. "
                "The only thing keeping it from an A is a pile of outstanding deliverables you still own \u2014 more on that below."
            )
        }
    },
    {"type": "divider"},

    # --- MEETING 1: SCHEDULING DEEP DIVE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f5d3\ufe0f MEETING 1 \u2014 Scheduling Deep Dive* (10:45am PST)\n"
                "_You + Bob Gao + Jatin Bhandari + Skye Laudari_\n\n"
                "This was the meeting. You've been building toward it for two weeks, and it delivered. "
                "Skye laid out the full Nihilus strategy, you got alignment on architecture, and the roadmap is now real."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f7e2 Decisions Made:*\n\n"
                "*1. Nihilus stays \u2014 but cornered as 'connected calendar only'*\n"
                "Annual contract renews end of January; 60-day cancellation notice means you need to decide by late November. "
                "Current trajectory: ~$75K\u2013$100K/year at current growth (back to ~8K grants by end of next year). "
                "The plan: keep Nihilus only for OAuth users (Google, Outlook, iCloud), and strip everything else out. "
                "This cuts cost ~90%. There's also a Nihilus Agents product that handles scheduling at much lower cost \u2014 worth exploring as an alternative path.\n"
                "_Why it matters: This was the open question from Oct 29. Now you have a decision framework._\n\n"

                "*2. Virtual calendar migration: dual-write approach, target end of year*\n"
                "89% of your users are on virtual calendars, 11% on OAuth. Virtual calendars are low-lift to replace \u2014 "
                "Homebase already writes all the data to its own DB. The plan: dual-write (copy Nihilus data, write to both simultaneously), "
                "then cut over whenever ready with zero data loss risk. OAuth stays on Nihilus for now \u2014 it's the genuinely hard part.\n"
                "_Why it matters: This is the clearest migration path you've had. Sequencing vs. feature work still needs to be decided._\n\n"

                "*3. Auto-cancel root cause = messaging, not logic*\n"
                "73% of interviews auto-cancel when a match requests one; <1% result in a hire. The root cause isn't the scheduling system \u2014 "
                "it's that the OAM confirmation email said nothing about the need to confirm. You and Skye rewrote the email to explicitly state: "
                "confirm by [date] or interview is canceled.\n"
                "_Why it matters: This is a quick win that improves a core metric without any eng work._\n\n"

                "*4. Future scheduling architecture: multiple interviewers per job*\n"
                "New interviewing model discussed: multiple interviewers per job, candidates book against a combined availability pool. "
                "Interviewer notified after booking; system can load-balance or hide unavailable interviewers. "
                "This makes building the booking UI in-house necessary (Nihilus only supports one calendar per invite).\n"
                "_Why it matters: This is a major product direction change that affects the entire migration plan._\n\n"

                "*5. Skye's top 3 (+ 1 growth unlock) locked in*\n"
                "(1) Job posting: get roles posted successfully, generate applicants via Indeed + boards. "
                "(2) Scheduling + interviewing: seamless candidate time experience. "
                "(3) Match explanation: show OAMs *why* a candidate matches, not just that they do. "
                "(4) Talent pool: unlocked once OAMs trust quality matches over volume.\n"
                "You added two more for next year: pricing/packaging (paid vs. free gates) + top-of-funnel growth once core is solid.\n"
                "_Why it matters: This is now the official stack rank you should be working from._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f3c3 Action Items from Scheduling Deep Dive:*\n"
                "\u2022 *YOU \u2192 Share end-state scheduling flow designs* \u2014 Needed as input before sequencing decisions. This is blocking Skye's migration plan. Do it today or tomorrow.\n"
                "\u2022 *YOU \u2192 Read Malcolm's scheduling deep dive doc* \u2014 Jatin flagged it as essential. You said you'd do it. It's been days. Do it tonight.\n"
                "\u2022 *YOU + Team \u2192 Define ideal end-of-year states as a group* \u2014 Jatin's ask: align on 2\u20133 target states, then work backwards. Schedule this for this week.\n"
                "\u2022 *Skye \u2192 Draft parity migration plan* \u2014 Detailed scope + cost estimate + sequencing before engineering starts. She owns it.\n"
                "\u2022 *Jatin \u2192 15-min sync with Bob* \u2014 Align on plan + open questions before Skye begins the breakdown."
            )
        }
    },
    {"type": "divider"},

    # --- MEETING 2: AVAILABILITY DISCUSSION (WORKSPACE) ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f5d3\ufe0f MEETING 2 \u2014 Availability Discussion* (11:30am PST, Workspace \u2014 Scheduling Pod)\n"
                "_Gurkiran Randhawa's meeting: Danilo, Justin, Ramona, Aldrin, Keyvan, Alexis, Yue Weng, Yuliia_\n\n"
                "You weren't in this one, but it's directly adjacent to your scheduling work and there's a resourcing flare-up worth watching."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4a1 Key Context:*\n\n"
                "*Team Availability deprecation plan is in motion:*\n"
                "Warning banner ships without a rollout flag. Full deprecation stays behind the main availability rollout. "
                "Hard dependency: modal for editing availability must be complete before the deprecated view goes live (Yuliia is on track per the Halfbaked demo). "
                "Target: banner live by end of next week.\n\n"
                "*Hard deadline: mobile wrapped by end of first week of December, one week of testing after that.*\n\n"
                "*\u26a0\ufe0f Resourcing alarm:* Yue Weng was assumed full-time on availability but got pulled onto ShiftView and forecasting today. "
                "Nico is also context-switching across 3\u20134 projects for weeks. Gurkiran flagged: weekly reallocation = velocity loss. "
                "She has a call with Ramona today to resolve Yue Weng's allocation.\n"
                "_What this means for you: If the scheduling pod can't staff availability by December, it hits the same deadline as your scheduling feature work. Watch this closely._"
            )
        }
    },
    {"type": "divider"},

    # --- MEETING 3: TIGER / MANAN ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f5d3\ufe0f MEETING 3 \u2014 Tiger / Manan \u2014 Indeed Job Posting Logic* (1:00pm PST)\n"
                "_You + Tiger Cao_\n\n"
                "You surfaced a potentially significant gap in how Homebase sends job postings to Indeed. "
                "If you've been missing the job requisition ID, Indeed may have been flagging your jobs as duplicates or fraud without telling you."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f7e2 Decisions / Findings:*\n\n"
                "*1. Job requisition ID was never sent to Indeed \u2014 this is a gap*\n"
                "Current state: Homebase only sends the job posting ID (21-day rule governs whether it's the same or new). "
                "Job requisition ID \u2014 which groups related postings within a 120-day window \u2014 is not in the payload at all. "
                "Indeed's docs say the requisition ID is required when it differs from the posting ID. "
                "Risk: without it, Indeed can't tell whether two posting IDs are the same role or duplicates, which may trigger fraud flags.\n"
                "_Why it matters: This could be affecting your FSA review and your organic visibility. It needs to be confirmed before the FSA resolution._\n\n"

                "*2. 21-day rule origin is now murky*\n"
                "The 21-day rule came from Indeed rep Jessica, but it doesn't appear in the latest docs Indeed sent. "
                "Need to confirm whether it still applies, and whether 'job reference ID' in their Q&A is the same field as 'job requisition ID' in their API docs.\n\n"

                "*3. Fix is minimal \u2014 but needs Indeed confirmation first*\n"
                "Backend change is low-lift: job posting ID logic is correct; the gap is just adding the requisition ID send. "
                "But you're not building anything until Indeed confirms the field semantics."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f3c3 Action Items from Indeed Job Posting Logic:*\n"
                "\u2022 *YOU \u2192 Draft and send clarification email to Indeed* \u2014 Confirm: (1) 'job reference ID' = 'job requisition ID'? (2) Two unique posting IDs with same requisition ID within 120-day window = acceptable? Send this week \u2014 it's been 2 months on the FSA review.\n"
                "\u2022 *Tiger \u2192 Build use-case examples doc* \u2014 4\u20135 scenarios (same job/location within 21 days, over 21 days, different location, 120-day expiry) with fake job names + exact IDs planned per scenario. For the Indeed email.\n"
                "\u2022 *Tiger \u2192 Flag risk to Jatin* \u2014 Additional PRs may be needed depending on Indeed's answers; set expectations now."
            )
        }
    },
    {"type": "divider"},

    # --- OVERDUE WATCH LIST ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f6a8 OVERDUE ITEMS \u2014 Still On You*\n\n"
                "These are yours. They don't go away by themselves.\n\n"
                "\u2022 *Interview Confirmation BDD Spec* \u2014 OVERDUE. Jatin + Bob can't start the spike without it. Write it NOW. Shape is locked (3-stage, no auto-cancel, no Cancel in v1).\n"
                "\u2022 *JD Rules for Divij* \u2014 DAY 10 OVERDUE. Divij is idle waiting for you. Rules are mostly decided. Just write the doc.\n"
                "\u2022 *2029 Vision One-Pager* \u2014 CRITICAL. 19+ days. John's waiting. Board is watching. This is the one that matters most and it keeps slipping.\n"
                "\u2022 *Scheduling Ideal State Doc* \u2014 Malcolm is gone. Jatin referenced it today. You need to write it, not inherit it.\n"
                "\u2022 *Tag Fatty for Verify CTA designs (magic link)* \u2014 Still outstanding. 30 seconds to Slack him.\n"
                "\u2022 *Indeed FSA email (company field bug)* \u2014 10+ days outstanding. Tie this into the Tiger/Manan email above.\n"
                "\u2022 *Tallroo dates* \u2014 November meeting. Include Skye. Still not sent.\n"
                "\u2022 *Matan 1:1 (quiet, re: 40% PMM split)* \u2014 Still outstanding. He needs to hear it from you.\n"
                "\u2022 *Prompt chips min wage MD file + ping Justin* \u2014 Justin is back. This is a this-sprint item. Do it now."
            )
        }
    },
    {"type": "divider"},

    # --- NIHILUS STATUS UPDATE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f514 NIHILUS UPDATE \u2014 Deadline Passed, Decision Framework Now Clear*\n\n"
                "The Nov 3 deadline came and went. Based on today's scheduling deep dive, the decision framework is now:\n"
                "Keep Nihilus for OAuth users only (corners it, cuts cost ~90%). "
                "Migrate virtual calendar users in-house (dual-write, target end of year). "
                "Explore Nihilus Agents product as a low-cost path for some scheduling logic.\n"
                "Skye needs to draft the parity migration plan before 60-day cancellation notice deadline (~late November). "
                "*Ping Skye tomorrow to confirm she has the right inputs to start that plan.*"
            )
        }
    },
    {"type": "divider"},

    # --- TOMORROW ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4aa TOMORROW \u2014 Wednesday Nov 4 Battle Plan*\n\n"
                "1. Write the Interview Confirmation BDD spec. First thing. Don't let the team sit idle another day.\n"
                "2. Send JD rules doc to Divij. 15 minutes. It's been 10 days.\n"
                "3. Send Indeed clarification email (coordinate with Tiger on use-case doc first).\n"
                "4. Read Malcolm's scheduling deep dive \u2014 Jatin flagged it as essential. You said you would.\n"
                "5. Share end-state scheduling flow designs with the team (Skye needs them to draft the migration plan).\n"
                "6. Edwin is back \u2014 follow up on change payment method flag turn-on.\n"
                "7. Hilary is back \u2014 check in on billing + businesses state.\n"
                "8. Start drafting 2029 one-pager. Even 200 words is progress. It's 19 days overdue."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_You had a genuinely productive day, Manan. The scheduling conversation with Skye was one of the most substantive you've had all quarter \u2014 "
                "you walked in with open questions and walked out with a framework. Tiger surfaced a real risk on Indeed before it became a bigger problem. "
                "The challenge now is the gap between the decisions you're making in rooms and the docs you're not writing at your desk. "
                "Tomorrow, close that gap. \U0001f4aa_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest \u2014 Tuesday, Nov 3, 2026",
    "blocks": blocks
}

def preview():
    print("\n" + "="*70)
    print("SLACK PREVIEW (no token) \u2014 Nov 3, 2026 Digest")
    print("="*70)
    for b in blocks:
        btype = b.get("type")
        if btype == "header":
            sys.stdout.buffer.write(("\n[HEADER] " + b["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif btype == "section":
            txt = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("\n" + txt + "\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            print("\n" + "-"*70)
    print("\n" + "="*70)
    print("Add SLACK_TOKEN or SLACK_BOT_TOKEN secret in Cursor Dashboard to send.")

if not TOKEN:
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"[OK] Message sent to {CHANNEL}. ts={body.get('ts')}")
    else:
        print(f"[ERROR] Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except Exception as e:
    print(f"[EXCEPTION] {e}")
    preview()
    sys.exit(1)
