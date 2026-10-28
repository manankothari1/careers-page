#!/usr/bin/env python3
"""Daily digest - Tuesday Oct 27 2026 PDT (cron midnight UTC Oct 28)"""

import json
import os
import sys
import urllib.request
import urllib.error

# ── Slack config ─────────────────────────────────────────────────────────────
CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

# ── Block Kit payload ─────────────────────────────────────────────────────────
blocks = [
    # ── Header ──────────────────────────────────────────────────────────────
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest  |  Tuesday, Oct 27, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5 meetings captured today (Paris Day 5 — back in SF Friday!)*\n"
                "Day Grade: *B+*   |   Theme: *SCHEDULING CRISIS DIAGNOSED — DESIGN FROM SCRATCH — INDEED FSA IN MOTION*\n\n"
                "You had a legitimately strategic day, Manan. You diagnosed one of Homebase's biggest customer headaches at the root-cause level, locked two important Magic Link design decisions, and opened real doors at Indeed around FSA. "
                "The only shadow: Divij's JD Rules are now Day 4 overdue and that debt compounds daily."
            )
        }
    },
    {"type": "divider"},

    # ── Meetings Overview ────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MEETINGS TODAY*"
        }
    },
    {
        "type": "section",
        "fields": [
            {"type": "mrkdwn", "text": "*8:45 AM*  Hiring Leads Standup"},
            {"type": "mrkdwn", "text": "Fadi, Matan, Jatin, Jon, Skye"},
            {"type": "mrkdwn", "text": "*9:15 AM*  Email Verification Magic Link"},
            {"type": "mrkdwn", "text": "Fadi, IBK"},
            {"type": "mrkdwn", "text": "*11:30 AM*  Scheduling Problem Spaces + Review"},
            {"type": "mrkdwn", "text": "Malcolm, Bob"},
            {"type": "mrkdwn", "text": "*12:30 PM*  Indeed Partner Office Hours"},
            {"type": "mrkdwn", "text": "Rachel Rosenberg (Indeed)"},
            {"type": "mrkdwn", "text": "*1:30 PM*  Mike + Fadi (External)"},
            {"type": "mrkdwn", "text": "Crown Way Oil — external no-show"},
        ]
    },
    {"type": "divider"},

    # ── Big Decisions ────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*BIG DECISIONS TODAY*"
        }
    },

    # Decision 1 - Scheduling
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. SCHEDULING: Design the ideal state from scratch (Bob's recommendation — accepted)*\n"
                ":mag: *What you decided:* Stop patching the current scheduling system. Set aside existing constraints, define the 'Cadillac' target state, then plan an incremental migration path.\n"
                ":brain: *Why:* Root cause analysis with Bob and Malcolm confirmed 24 of 29 Linear tickets trace to just 3 structural problems: (a) no decision on whether Nylas or Homebase owns scheduling truth, (b) settings follow the job creator not the job manager, (c) every new option (manual/auto, Google Cal, multi-manager) multiplies QA surface exponentially. Only 17% of customers have Google Calendar integrated — and auto-scheduling adoption is even lower. The system was never deliberately designed.\n"
                ":rotating_light: *Why it matters:* Scheduling is the #1 customer complaint. Malcolm is your rubber duck on this and he leaves *Friday*. This POV needs to exist before he's gone."
            )
        }
    },

    # Decision 2 - Magic Link: No confirm button
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. MAGIC LINK: Auto-verify on click — no extra confirm button*\n"
                ":mag: *What you decided:* Landing page auto-verifies when the user clicks the link. No additional 'Confirm' step.\n"
                ":brain: *Why:* Fadi's pushback was correct — user already clicked the link, a second confirm is redundant friction. IBK's note clinched it: email copy already says 'close this tab and go back to your job post,' which covers the email-scanner pre-click edge case.\n"
                ":white_check_mark: *Status:* Designs cover all five landing page states (verified, expired, already used, already verified, failed) plus two modal states. Gate at 0%, ready to roll 10-20%."
            )
        }
    },

    # Decision 3 - Magic Link: Default email template
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. MAGIC LINK: Use Stitch default email template (not custom)*\n"
                ":mag: *What you decided:* Use Stitch's out-of-the-box email template rather than building a custom one.\n"
                ":brain: *Why:* Reduces dependency on the identity team. Email copy already exists (confirmed via fake inbox demo). The custom template would create a critical-path dependency on an already-understaffed team (Mary Turpin on vacation, no replacement assigned yet).\n"
                ":rotating_light: *Open question:* Whether Stitch uses SendGrid — if yes, team gets full copy/template control anyway."
            )
        }
    },

    # Decision 4 - Indeed: Tech review call
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. INDEED: Request a dedicated technical review call with Indeed's Integrations Delivery (ID) team*\n"
                ":mag: *What you decided:* Don't rely on office hours for the new job posting flow review. Request a formal call with ID team + a Homebase engineer to walk through the diagram.\n"
                ":brain: *Why:* The new flow (post ID vs reference ID, 120-day window, 3-week repost logic) is too technically detailed for office hours. The ID team doesn't attend office hours. Fallback: email the diagram + questions for a 24-48hr turnaround.\n"
                ":white_check_mark: *Status:* Rachel to coordinate with Ashley (and Jessica). You'll bring an engineer and the flow diagram."
            )
        }
    },

    # Decision 5 - Indeed: Language strategy
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. INDEED: Agreed language strategy for hiring intent in job descriptions*\n"
                ":mag: *What you decided:* Use 'hiring multiple positions/roles' (not specific count) and 'urgently hiring' (for speed signal).\n"
                ":brain: *Why:* Avoids the Jobcase-style duplicate/fraud risk of repeating job posts. Maps cleanly to numberOfHires and hiringTimeline API fields. Rachel to verify neither phrase triggers Indeed's fraud detection before you ship.\n"
                ":rotating_light: *Pending:* Rachel's confirmation + FSA status from Jessica (expected response by EOD today)."
            )
        }
    },

    {"type": "divider"},

    # ── Action Items ─────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*YOUR ACTION ITEMS (Manan owns)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":fire: *CRITICAL — DO TONIGHT/TOMORROW AM:*\n"
                "• :red_circle: *JD RULES FOR DIVIJ* — Day 4 overdue. Write them NOW (1 hire=vanilla; 2+=multiple; urgency<=2wk=urgently). Divij is idle. Every day this slips = a day of blocked DS work.\n"
                "• :red_circle: *2029 VISION ONE-PAGER* — Still not written. Fadi submitted his. Board meeting opened Oct 15. John is waiting.\n"
                "• :orange_circle: *Write scheduling product POV* — Define ideal scheduling from the customer's perspective before Malcolm leaves Friday. Covers: source of truth, settings ownership, flow simplification. Hand off to Bob + Malcolm.\n"
                "• :orange_circle: *Answer Bob's scheduling open questions* — The three root-cause sections in his second doc need your product framing before engineering can size the rebuild.\n\n"
                ":calendar: *THIS WEEK:*\n"
                "• :blue_circle: Push Jatin to get identity EM to assign Mary Turpin replacement — Magic Link is on the critical path waiting for identity team Stitch allow-list work\n"
                "• :blue_circle: Check IBK: can his team create the Stitch email template themselves? (or is identity team needed?)\n"
                "• :blue_circle: Query auto-scheduling adoption rate (Bob has 17% Google Cal integration; need the auto-scheduling cut)\n"
                "• :blue_circle: Review Matan's Linear project comments + confirm QA email checklist is clearly listed for engineers\n"
                "• :blue_circle: Check Jessica's FSA response (expected EOD today) — if nothing, escalate to Ashley Lutz\n"
                "• :blue_circle: Tag Fatty for Verify CTA designs on Magic Link success screen (this has been pending since Oct 26 sprint kickoff)\n"
                "• :blue_circle: Facebook API — Day 34. Bob + IBK. No update since Oct 9. Escalate immediately.\n"
                "• :blue_circle: Address standup attendance issue with full team (flagged as recurring by you + Matan)\n"
                "• :blue_circle: Matan local testing env walkthrough — plan for next week after you're back in SF"
            )
        }
    },
    {"type": "divider"},

    # ── Watch List ────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WATCH LIST + STATUS UPDATES*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":rotating_light: *NEW RISK ADDED: SCHEDULING SYSTEM* — officially confirmed as a ground-up redesign effort today. Malcolm (your only rubber duck on this) is out Friday. Window to extract his knowledge = 3 days.\n\n"
                ":white_check_mark: *MAGIC LINK* — progressing well. Gate ready. Design decisions locked today. Blocker: identity team (Mary on vaca). Jatin action needed.\n\n"
                ":hourglass: *INDEED FSA REVIEW* — Jessica (Rachel's manager) response expected by EOD today. If nothing by tomorrow morning, escalate to Ashley Lutz directly.\n\n"
                ":hourglass: *ENTITLEMENTS ROLLOUT* — 5% rollout target was today (Oct 28). Monitor for CS/billing noise.\n\n"
                ":red_circle: *FACEBOOK API* — Day 34. Still failing. No update. ESCALATE.\n\n"
                ":red_circle: *NIHILUS SUBSCRIPTION* — Deadline Nov 3 = 6 days away. Decision needed.\n\n"
                ":orange_circle: *SPEC SWARM* — Was supposed to happen today (Oct 27). No meeting captured — confirm outcome with Jatin. Did it happen? What are the N+1 verdicts?\n\n"
                ":orange_circle: *COMMS ASSISTANT decision* — Malcolm leaving Nov-Dec. Needs to happen before he's gone.\n\n"
                ":orange_circle: *B&B INTEL* — Discount dashboard showing 40% reject rate on verify_code (5.99k total, 2.39k HTTP 422). One user tried ~100 codes. Brant owns investigation. FYI: Entitlements domain events work in progress (Jeevash); Chargebee migration story map in review.\n\n"
                ":calendar: *DEPARTURES SIGNAL DOCS* — 30+ days overdue. Zane, Sean, Jon W, Bobby."
            )
        }
    },
    {"type": "divider"},

    # ── Personal Note ─────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*A NOTE FROM YOUR CHIEF OF STAFF*\n\n"
                "The Mike meeting was a reminder that external customers don't always show up — and that's okay. "
                "What stood out more was the candid moment with Fadi. You're both stretched thin and you both know it. "
                "That conversation about the IC/lead hybrid trap was real — and it's worth sitting with. "
                "The pull toward family (being closer to your parents, not wanting your brother to carry it alone) shows who you are. "
                "There's no urgency to decide anything today, but it's clearly on your mind for a reason.\n\n"
                "The scheduling session was one of the most strategically valuable hours you've had in weeks. "
                "You unlocked a real architectural diagnosis that's been invisible because it hides behind 29 individual tickets. "
                "Now write the POV before Malcolm walks out the door Friday. That's the play.\n\n"
                ":airplane: *Fly safe home Friday, Manan. SF awaits.*"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest | Tue Oct 27, 2026 | Paris -> SF Friday | _Questions? Just reply here._"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Digest - Tuesday Oct 27, 2026"
}

# ── Send or preview ───────────────────────────────────────────────────────────
def preview():
    sys.stdout.buffer.write(
        "\n======= DAILY DIGEST PREVIEW (no Slack token) =======\n".encode("utf-8")
    )
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(
                ("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif block.get("type") == "section":
            if "text" in block:
                sys.stdout.buffer.write(
                    (block["text"]["text"] + "\n\n").encode("utf-8", errors="replace")
                )
            if "fields" in block:
                for f in block["fields"]:
                    sys.stdout.buffer.write(
                        ("  " + f["text"] + "\n").encode("utf-8", errors="replace")
                    )
                sys.stdout.buffer.write(b"\n")
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block.get("type") == "context":
            for e in block.get("elements", []):
                sys.stdout.buffer.write(
                    (e.get("text", "") + "\n").encode("utf-8", errors="replace")
                )
    sys.stdout.buffer.write(b"\n=====================================================\n")


if not TOKEN:
    preview()
    print("\n[INFO] No Slack token found. Set SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN.")
    print("[INFO] Add it in Cursor Dashboard > Cloud Agents > Secrets to enable live delivery.")
    sys.exit(0)

# Send to Slack
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"[OK] Digest sent to Slack channel {CHANNEL} (ts={result.get('ts')})")
    else:
        print(f"[ERROR] Slack returned error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error sending to Slack: {e}")
    preview()
    sys.exit(1)
