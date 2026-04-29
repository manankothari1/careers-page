#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari - Apr 29, 2026 (covering Apr 28 meetings)"""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Debrief - Tuesday Apr 28 :brain:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Great work today - you covered a lot of ground. Two meaty sessions, and you came out of both with real clarity on where you're taking hiring. Here's your full debrief. :rocket:"
        }
    },
    {"type": "divider"},

    # ─────────────────────────────────────────────
    # MEETING 1
    # ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Meeting 1 of 2 — Applied AI Jamming: Hiring (3:30 PM)*\n_With: Fadi, Divij, Dana, Ted, Jatin, Pabadeh_"
        }
    },
    {"type": "divider"},

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mega: Big Direction Shift*\nYou kicked off a new era for these sessions: *moving from progress reviews to strategic brainstorming*. You explicitly told the team: 'we've been in execution mode, and we want to get back into innovation mode — that requires more bi-directional thought partnership, not just top-down execution.' This is a meaningful cultural and process decision for the hiring team."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 1: Six core product hypotheses locked as north star*\n*What you decided:* You presented and aligned on 6 hiring assistant hypotheses as the directional framework going forward:\n  1. Deliver a *short list of interview-ready candidates* with clear reasoning\n  2. Pull out *business-specific hiring criteria* beyond what OAMs would naturally write (e.g. 'can handle dinner rush solo'; 'wouldn't hire from X coffee shop')\n  3. *Every hire makes the assistant smarter* for that business forever — build feedback loops and customization\n  4. *Predict hiring needs* from signals only Homebase has (sales, seasonality, turnover, scheduling)\n  5. *Manager's role = small reactions, not large efforts* — replace deterministic scoring with dynamic context-aware next best actions\n  6. *Confidence in hire quality AND reliability* — proprietary show-up signals from platform data\n\n*Why:* Customers consistently report hiring as their biggest pain point. Today's system is still too generic, too deterministic, and asks OAMs to do too much. These hypotheses are designed to flip that dynamic.\n\n*Status:* Directional / not yet prioritized. Dana to continue refining core product list; Manan refining applicant flow list. Ray alignment step next."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 2: 'Personal recruiter' framing confirmed as the product vision*\n*What you decided:* The analogy of an *internal TA doing a live back-and-forth intake call with a hiring manager* is the right mental model — not a tool, but a recruiter who knows your business intimately and adapts over the hiring lifecycle.\n\n*Why:* This framing makes the value of the assistant visceral and aspirational. It also clarifies what 'intake' means: it's not filling out a form — it's a calibration conversation that the system uses to tune all downstream recommendations.\n\n*Implication:* The modality question (typing vs. voice) is secondary. Ted noted that models are getting better at inferring and working on longer time horizons, so forcing a modality debate now may be premature."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 3: Applicant-side hypotheses kicked off — 3 main pillars*\nYou walked the team through your early-stage applicant flow hypotheses:\n  1. *Job optimization* — salary competitiveness alerts, title optimization (Indeed deranking for multi-role titles), platform-specific performance data, AI-readable JD content\n  2. *Existing applicant/employee database utilization* — weekly job digest, third-party job scraping + matching, post-termination job nudges, previous applicants (still untapped!), predictive pipeline pre-build for seasonal businesses\n  3. *Job seeker agent concept* — inspired by the Jack/Jill app: a personal agent that applies to jobs on behalf of the candidate based on their stated criteria\n\n*Why:* Applicant supply is the foundation of marketplace dynamics. If we can own the supply side AND the demand side, Homebase becomes the destination — not a distribution channel.\n\n*Status:* Fadi pushed for A/B/C prioritization — you agreed to do that pass before the next meeting. These are still pre-prioritized hypotheses."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 4: Applicant intake + portable profile architecture confirmed*\n*What you decided:* The right long-term architecture is a *generic screener as applicant intake* (capturing preferences, availability, role interests) plus *1-2 job-specific questions per application*. This profile should be *portable* — carried across all job interactions, reducing screener repetition for candidates.\n\n*Why:* 100 baristas applying to 100 cafes shouldn't do 100 identical screeners. It's bad UX and it signals that we're a tool, not a platform. The intake model also unlocks personalized job matching.\n\n*Tie-in:* This exact topic came up in your IN/Hiring Sync earlier today (see below)."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 5: Don't anchor to what's been built — rebuild what makes sense*\n*What you decided:* When asked how much of the existing product you're willing to reinvent, your answer was clear: *no sacred cows*. Keep what makes sense (core data models: candidate management, status tracking, filtering); discard or rebuild what doesn't. Foundation tools stay as the 'tools layer'; the agent layer goes on top.\n\n*Why:* You're designing for a future state. Anchoring to legacy architecture would constrain the vision."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 6: Fraud job detection improved — new prompts live*\nPabadeh / team shipped a new set of prompts for fraud job detection. *Accuracy improved AND a new category of fraud jobs that the previous round missed is now being caught.*\n\n*Action:* Confirm with team on Slack how to handle the new flagged jobs operationally. No hard blocker identified."
        }
    },

    {"type": "divider"},

    # ─────────────────────────────────────────────
    # MEETING 2
    # ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Meeting 2 of 2 — IN/Hiring Sync (10:30 AM)*\n_With: Brad, Dana + Identity team_"
        }
    },
    {"type": "divider"},

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 7: Human model = thin PII layer; persona = company employment record*\n*What you decided:* You aligned with the identity team on their model: a *human* is a thin PII record (email + phone combo). A *persona* is only created when a human is *hired* at a company — it's the employment record. Applicants live as applicant records, not personas.\n\n*Why:* This keeps the hiring flow clean (no premature persona creation) and allows for Homebase-specific signals (e.g. clock-in reliability, employee verification badges) to be attached when a human is known to be a Homebase employee."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 8: Need a separate applicant model before human creation — don't force authentication to apply*\n*What you decided:* You and the identity team aligned: *creating a human record on every application is risky* (fat-fingered emails, reused phones). The right approach is:\n  - Keep a *lightweight applicant record* at application time (no forced auth)\n  - Create the human only at the *authentication step*\n  - Auth hooks: (a) applicant wants to see previous applications, OR (b) you entice them ('we found 5 more jobs for you — sign in to see them')\n\n*Why:* Frictionless one-shot applications must remain frictionless. Auth is a carrot, not a gate."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 9: Duplicate human records are acceptable — don't over-solve for multi-email users*\n*What you decided:* People use different emails intentionally (plus-addressing, separate inboxes). You agreed to *allow for duplicate humans* and not try to perfectly de-duplicate. Combining records can be an optional user-initiated action (e.g. 'we see this phone is associated with another email — link them?').\n\n*Why:* Over-engineering identity matching creates more data problems than it solves, especially in a frictionless application flow."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 10: Keep both application entry points fully supported (API + web hook)*\n*What you decided:* Confirmed that two application routes must always be supported:\n  1. *API-based* (Indeed, ZipRecruiter) — they host the job and send applicants back via API\n  2. *Web hook / XML* (Facebook Jobs, Talroo) — we host the job page; applicants land on our native page\n\n*Why:* Our job distribution strategy depends on both. The native page must work for unauthenticated applicants because partner traffic lands here directly."
        }
    },

    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decision 11: Identity team to document their model with markdown + mermaid charts*\n*What you decided:* You asked the identity team to create a *running markdown file* with model associations and authentication flow diagrams (mermaid charts) so hiring team can stay aligned as both products evolve in parallel.\n\n*Why:* Both teams are changing fundamental data models. You need a lightweight async way to stay in sync without a weekly sync every week."
        }
    },

    {"type": "divider"},

    # ─────────────────────────────────────────────
    # ACTION ITEMS
    # ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:clipboard: Your Action Items from Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*From Applied AI Jamming:*\n• :fire: *TODAY* — Update the brainstorming doc in the repo (push the PR — Ray is waiting for your updated version)\n• *This week* — Do an A/B/C prioritization pass on your applicant flow hypotheses before next session\n• *This week* — Align with Ray on which hypotheses to invest energy in first (core product vs. applicant flow)\n• *This week* — Identify V1 entry points for the loftiest hypotheses (Ted: show don't tell, vibe code a prototype)\n• *Ongoing* — Track the Jack/Jill job seeker agent model as a competitive/inspirational reference\n• *Backlog* — Voice vs. typing modality experimentation: experiment, don't decide prematurely"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*From IN/Hiring Sync:*\n• *Follow up with identity team* — Check that they've created the markdown + mermaid doc for model associations + auth flows\n• *Share with Dana + Bob* — Ensure they've seen the identity model so it informs hiring product architecture decisions\n• *Flag to identity team* — As hiring product evolves (applicant profile, marketplace), keep them looped in proactively"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Carry-forward fire items (still open!):*\n• :rotating_light: *TLWA brief to Ted* — 20+ days overdue. Send. Now.\n• :rotating_light: *TLWA company list freeze* — 55,696 vs 54,000 discrepancy\n• *Sprint 2610 grooming* — TODAY (Tuesday Apr 28/29)\n• *HB Assistant tool definitions* — Due before Thu May 1\n• *Matan* — Post Boost plan to #leads + survey customers on hiring spend (overdue Apr 23)\n• *Nelson* — metro_area + bucketed_role + matching_roles (overdue Apr 8)\n• *Greenlight Manual Mode* — Cindy QA done. Ball is in your court.\n• *TLWA V1→V2* — Ugo, Friday deadline. Check in."
        }
    },

    {"type": "divider"},

    # ─────────────────────────────────────────────
    # WHAT'S GREAT
    # ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:star: What You Crushed Today*\nYou're in rare form, Manan. The shift from execution to innovation mode is huge — and the fact that you called it out explicitly in front of the eng/design team signals real leadership. The six hypotheses framework you walked through is genuinely ambitious and grounded. And in the identity sync, you navigated some gnarly data model territory with clarity and pragmatism ('allow for duplicates; don't over-engineer'). Two completely different meetings, both left with clear next steps. Strong day. :muscle:"
        }
    },

    {"type": "divider"},

    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Daily debrief by your Chief of Staff | Covering Apr 28, 2026 | 11 decisions across 2 meetings"
            }
        ]
    }
]

payload = {
    "channel": SLACK_CHANNEL,
    "text": "Your Daily Decision Debrief - Tue Apr 28 (11 decisions, 2 meetings)",
    "blocks": blocks
}


def preview():
    print("\n=== SLACK MESSAGE PREVIEW ===\n")
    for block in blocks:
        if block["type"] == "header":
            print(f"\n{'='*60}")
            print(f"  {block['text']['text']}")
            print(f"{'='*60}")
        elif block["type"] == "section" and "text" in block:
            text = block["text"]["text"]
            text = text.replace("*", "").replace(":white_check_mark:", "✓").replace(":fire:", "🔥")
            text = text.replace(":clipboard:", "📋").replace(":star:", "⭐").replace(":rocket:", "🚀")
            text = text.replace(":calendar:", "📅").replace(":mega:", "📣").replace(":muscle:", "💪")
            text = text.replace(":rotating_light:", "🚨").replace(":brain:", "🧠")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            print("-" * 60)
        elif block["type"] == "context":
            for el in block.get("elements", []):
                print(f"  [{el.get('text','')}]")
    print("\n=== END PREVIEW ===\n")


def send_to_slack():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SLACK_TOKEN}"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"✅ Slack message sent successfully! ts={result.get('ts')}")
            else:
                print(f"❌ Slack API error: {result.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if not SLACK_TOKEN:
        print("⚠️  SLACK_TOKEN not set — printing preview instead.\n")
        preview()
        sys.exit(0)
    send_to_slack()
