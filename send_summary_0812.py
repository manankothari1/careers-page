#!/usr/bin/env python3
"""Daily Chief-of-Staff Digest — Aug 12, 2026"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
DATE = "Tuesday, Aug 12, 2026"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Brief — Tuesday, Aug 12 :briefcase:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day today — 3 back-to-back meetings and some real momentum. Here's everything you decided, what it means, and what needs to happen next. You crushed it."
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:wave: Meeting 1 — Manan / Dana (10:30 AM) | Dana's Last Day*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":bulb: *Decisions Made*\n"
                "1. *Zero state page experiment → pause before killing.* Numbers (23 vs 15) look statistically thin for a month of data. Before pulling the plug, re-check the date range and run it against the OG baseline. Don't kill something prematurely.\n"
                "2. *Scheduling bugs → escalate to triage.* Charmina completed a full spike with linked docs and structured recs — and nobody has touched it. Dana's framing is right: patching without diagnosis means it never stays fixed. This needs dedicated brain space from Fadi or you.\n"
                "3. *Intake is the unlock for matching.* Dana's strong conviction: matching will never be good without a proper intake step. Voice/conversational intake that surfaces deal-breakers automatically is the direction. Key assumption still to validate: will OMs trust the AI to act on that intake?\n"
                "4. *Personal recruiter vision is still correct.* Docs to read: Agentic Hiring Vision + Personal Recruiter narrative (both in the handoff doc under 'Relevant Docs').\n"
                "5. *Sky onboarding strategy: stake a position NOW.* Dana's parting advice — while Sky knows nothing about the product, you have maximum influence. Shape the direction before anyone else does."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *Your Action Items from this meeting*\n"
                "• Re-examine zero state page experiment data — check date range + compare vs OG baseline *before* killing it\n"
                "• Read Agentic Hiring Vision + Personal Recruiter docs in Dana's handoff\n"
                "• Schedule time to review Charmina's scheduling spike (it's sitting in Linear with linked docs)\n"
                "• Set up comms agent experiment vs. normal screener — align with Nockling on rollout\n"
                "• Decide: who owns the intake work? Fadi or someone else?"
            )
        }
    },
    {
        "type": "context",
        "elements": [{
            "type": "mrkdwn",
            "text": ":black_heart: Dana's last day. She left you with a clear vision and a strong point of view. Honor it by actually reading those docs."
        }]
    },
    {"type": "divider"},

    # ── MEETING 2 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bar_chart: Meeting 2 — Hiring ICP Experimentation Weekly Review (12:00 PM) | Matan, Ray, John, Usman, Jon*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":bulb: *Decisions Made*\n"
                "1. *Indeed feed: resubmitted for re-review.* You went to Indeed office hours and got the fraud flag into the re-review queue. This is the prerequisite before you pitch the domain-provisioning idea to them — smart sequencing. Don't introduce anything new until fraud is cleared.\n"
                "2. *Careers page outreach: strong signal, scale it.* You, Matan, Fadi, and Jatin manually built 30-40 careers pages for OEMs and sent them Friday — 65% open rate, 12% CTR. Small n but remarkable. The 'free page, no strings attached' thesis is proving out. This deserves a real experiment at scale.\n"
                "3. *Indeed policy wedge: personalized alert to 500-1K OEMs.* The 3-free-post cap + corporate domain email requirement are coming. Send a news-alert-style outreach (not a newsletter) to OEMs ahead of enforcement — lead with education, close with Homebase help. Matan building the content.\n"
                "4. *Meta ads: 8 campaigns live.* 4 vs FFH, 4 vs non-ICP OAMs. Attribution tracking is the current blocker — Matan to align with Jen. Hiring CPAs already look better than general Homebase ads, so if attribution holds up, there's a real top-of-funnel investment case here.\n"
                "5. *Domain provisioning: needs scoping.* The SMB-domain concept (owner name + Homebase domain) came up. Needs more thinking — email-only vs. full web presence are very different bets. Not committed yet.\n"
                "6. *Jobcase partnership: follow up.* Dana surfaced this before leaving. Could reduce Indeed dependency and add applicant volume. Worth a meeting to assess fit.\n"
                "7. *Sales framing locked: drop the word 'AI.'* Screener is 'a screener that does the job for you.' The 2:1 dislike-to-like ratio on AI framing is real, but passionate advocates exist. Don't lead with AI."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *Your Action Items from this meeting*\n"
                "• Monitor Indeed re-review — confirm fraud flag is cleared before next Indeed conversation\n"
                "• Follow up with Matan on attribution setup for Meta campaigns (unblock Jen conversation)\n"
                "• Decide: do you invest in scaling the careers page outreach? If yes, what's the experiment design?\n"
                "• Follow up on Jobcase partnership meeting (Matan owns, but you need to weigh in on fit)\n"
                "• Matan to share intent-signal tool access with Usman + Jon to strengthen their prospecting scripts"
            )
        }
    },
    {
        "type": "context",
        "elements": [{
            "type": "mrkdwn",
            "text": ":fire: 65% open rate on manually-built careers pages is legitimately exciting. That's worth a real experiment."
        }]
    },
    {"type": "divider"},

    # ── MEETING 3 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:gear: Meeting 3 — Applicants EPD Leads Sync (2:00 PM) | Jatin + Fadi*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":bulb: *Decisions Made*\n"
                "1. *Sprint cadence changing — starts Sprint 18 (not next sprint).* New flow: Tuesday look ahead, Wednesday morning breakdown + end-of-day feasibility/trade-off share from leads, Thursday heads-down, locked by Friday. Jatin wants team buy-in first — retro Tuesday 1-2pm ET.\n"
                "2. *Fadi gets protected morning focus blocks.* Fadi is stretched thin with 3 overlapping meetings today. Agreed: 2-hour morning block + 1-hour end-of-day. He can skip non-essential meetings (e.g. look ahead when designs are simple). Held.\n"
                "3. *Future prototypes for Jan: NOT high leverage right now.* You pushed back on Fadi treating Jan prototypes as a side project. Better ROI: designs ready ahead of sprint to reduce in-sprint rework cycles. Redirect his focus.\n"
                "4. *Resume Insights — manual mode behavior locked.* For OAMs NOT on AI plan: show resume, hide insights, use existing 'show matches' toggle pattern with paywall/upgrade prompt. Button variant: tertiary plain (no white background). Fadi has designs by Monday.\n"
                "5. *Culinary Agents: CONTRACT SIGNED, test launching NOW.* Legal delay is over (Rushi signed off). 27 line cook jobs at $69/job going live. Success metric: meaningful applicant flow for those customers. If it works, offer as a paid channel for back-of-house roles. You're sending the go-live email today.\n"
                "6. *Renew Jobs: Option 1 wins.* Renew button (extends +30 days) + extend base expiry to 60-90 days. Indefinite expiry is too risky (Indeed may flag jobs as stale/fraudulent). Malcolm owns back end; Matan as secondary after comms agent work.\n"
                "7. *Talent pool confirmed as the core strategic direction.* Both you and Fadi aligned. You're writing a doc for Sky to land this as the north star. Sky target start: Aug 25.\n"
                "8. *Carlo on bereavement (back tomorrow, out next week).* Indeed 3LO work is his — Jatin expects him to finish before he leaves again. Watch this closely.\n"
                "9. *Tanner flagged as behind on Indeed account setup.* Unclear what's blocking. Needs a follow-up."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":white_check_mark: *Your Action Items from this meeting*\n"
                "• *TODAY: Send go-live email to Culinary Agents* — confirm 27 test jobs can be posted\n"
                "• Write talent pool strategy doc for Sky (for Aug 25 onboarding)\n"
                "• Push Myan to share ICP nudge experiment results — team has zero visibility into performance\n"
                "• Fadi: resume insights designs ready by Monday (multi-page scrolling = main open issue)\n"
                "• Fadi: add talent pool designs + prototype link to Linear (stale; engineers are blocked)\n"
                "• Jatin: team retro Tuesday 1-2pm ET, then share sprint volume numbers tomorrow\n"
                "• Chase Tanner on what's blocking Indeed account setup\n"
                "• Monitor Carlo's 3LO work before his second leave period"
            )
        }
    },
    {
        "type": "context",
        "elements": [{
            "type": "mrkdwn",
            "text": ":rocket: Culinary Agents is live. Talent pool is locked as the direction. Clean day."
        }]
    },
    {"type": "divider"},

    # ── OVERDUE WATCH LIST ────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: Open Watch List Items (carried over)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *422 Job Publishing Errors* — Day 32+. Jatin on RCA. Ray is out = you're the decision-maker. Status?\n"
                "• *Fadi Boost Modal Figma* — 13+ days overdue. Did you unblock him today?\n"
                "• *Amplitude dashboard to Matan* — overdue since Aug 6. Send it.\n"
                "• *IBK: JD A/B experiment* — running week of Aug 10 (50/50). Any early signal?\n"
                "• *New GM of Hiring start date* — Aug 18 or Aug 25? Ray to confirm. Chase this.\n"
                "• *Meet Sky ASAP* — target start Aug 25. Get on his calendar before he starts.\n"
                "• *Strategy deck + Roadmap-to-goals deck* — were due Aug 10. Confirm delivered to John/Ray.\n"
                "• *Hiring team operating model write-up* — write and share with Ray.\n"
                "• *Sales reps: schedule direct time* — mirror Ray/Claire approach. Not done yet.\n"
                "• *Gbolade: 15-min PM session* — still open.\n"
                "• *Catherine (Indeed): free trial exemption follow-up* — fraud call was Aug 11. Did you send the follow-up?\n"
                "• *Abby ownership area* — week 10, still unclear. Assign something real."
            )
        }
    },
    {"type": "divider"},

    # ── CLOSING ───────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Today's Single Most Important Action: :point_right: Send the Culinary Agents go-live email.*\n\n"
                "Everything else can wait until tomorrow. But that email is holding up 27 line cook jobs and a test that could change your back-of-house applicant strategy. Do it now if you haven't.\n\n"
                "Big picture: you closed the day with Culinary Agents live, talent pool locked as your north star, a solid careers page signal, and Dana's handoff complete. That's a strong exit on a hard day. :muscle:"
            )
        }
    },
    {
        "type": "context",
        "elements": [{
            "type": "mrkdwn",
            "text": "Chief of Staff digest | Aug 12, 2026 | 3 meetings reviewed"
        }]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Daily Chief-of-Staff Digest — Aug 12, 2026"
}


def preview():
    sys.stdout.buffer.write(
        b"\n=== SLACK DIGEST PREVIEW (Aug 12, 2026) ===\n"
    )
    for block in blocks:
        if block.get("type") == "section":
            txt = block.get("text", {}).get("text", "")
            if txt:
                sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("### " + txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                txt = el.get("text", "")
                sys.stdout.buffer.write(("[context] " + txt + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n\n")
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n")


token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

if not token:
    preview()
    print("\nNo Slack token found. Add SLACK_BOT_TOKEN in Cursor Dashboard → Cloud Agents → Secrets to enable live delivery.")
    sys.exit(0)

req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"Message sent successfully to {CHANNEL}")
    else:
        print(f"Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
