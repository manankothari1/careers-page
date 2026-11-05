#!/usr/bin/env python3
"""Daily Chief of Staff Digest -- Wednesday Nov 4, 2026 (PST)"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Brief: Wednesday, Nov 4"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Today's Theme:* INDEED EMAIL LOCKED \u2022 MAGIC LINK CLIMBING \u2022 BILLING FIRE CONTAINED\n\nSolid execution day, Manan. You moved two major workstreams forward, got the billing picture, and have a clear path into tomorrow. The overdue pile is real though \u2014 let's talk about that at the bottom."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcca MEETINGS TODAY*\n\u2022 10:15am \u2014 Gbolade / Manan _(Magic Link OTP rollout check-in)_\n\u2022 10:30am \u2014 Tiger / Manan _(Indeed job posting ID email finalization)_\n\u2022 8:15am workspace \u2014 B&B Standup & Metrics Review _(Hilary + Edwin back; billing fire)_\n\u2022 11:30am workspace \u2014 Shift Fill Whiteboarding _(SB \u27ba HBA architecture; Sina very much occupied)_"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Magic Link stays at 20% today \u2014 bumping Thursday*\n_Meeting: Gbolade / Manan_\nSend success rate is 100%. 5 links sent, 2 verified \u2014 one flagged fraudulent (script-triggered resend), one legit (Corelvia Tech). Decision: hold at 20% for today, Gbolade bumps to a higher percentage tomorrow if stability holds. No action needed from you today."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Three Indeed questions finalized \u2014 email ready to send*\n_Meeting: Tiger / Manan_\nYou and Tiger locked the outbound email to Rachel at Indeed. Three questions:\n\u2022 Is 'job reference ID' in the Marketplace Q&A the same field as 'job requisition ID' in the Job Sync API docs? (Explicitly: not the job posting ID)\n\u2022 Reactivation window: Job Sync API says 30 days; Jessica previously said 21 days. Which applies when reusing the same job posting ID?\n\u2022 Expiration date for extensions: Homebase currently calls expireSourceJobBySourcePostingId and never sends an expiration date. To support extensions, do we also need to send and update the expiration date when it changes?\nDocument simplified: removed the diagram (Tiger's call, good call), text-only scenario tables, cleaned result columns."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Amplitude (not Datadog) is likely the right fraud-monitoring tool for Magic Link*\n_Meeting: Gbolade / Manan_\nDatadog shows raw success rate but can't join to account-level fraud signals. Amplitude funnel already built with is_fake_company boolean filter \u2014 that's your cleanest signal for unique legit businesses verifying. Gbolade to also investigate Databricks (join OTP events with account closure data). No decision to do anything differently today, but the monitoring stack is getting clearer."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Credit card on file being considered as a second fraud layer*\n_Meeting: Gbolade / Manan_\nEmail verification catches most fraud (per fraud team), but actors with their own email domain bypass it entirely. Credit card requirement before trial start is on the table as a backstop \u2014 would catch bad actors whose cards don't check out. Open question: does it replace or layer with email verification? No decision yet, still exploratory."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Entitlements ramp moved to 25% cohort (up from 5%)*\n_Meeting: B&B Standup_\nStatistically significant now. Adam blocked on 3 PRs (1210, 1214, 1212) \u2014 HRM review backlog. While blocked, Adam picking up cap-related tickets. Any issues from Michael Lin go to Adam first. This is momentum \u2014 watch for surface issues at this scale."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Change Payment Method Flex rollout targeting next week*\n_Meeting: B&B Standup \u2014 Edwin is back_\nEdwin's last ticket (flipping the new model for payroll) is in progress. Flex rollout approach: simple on/off feature flag, NOT a percentage ramp. Separate item surfaced: past-due visibility for add-ons (e.g. Tip Manager) \u2014 not currently shown. Hilary raising with Dipesh. This is relevant to your watch list \u2014 update: 'EOW' target becomes 'next week.'"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Payroll double invoice: wait for ACH to clear, then run credits*\n_Meeting: B&B Standup_\n~1,100 customers were double-billed on Nov 1. Root cause: subscription schedule didn't match renewal date. 900+ of those have pending ACH payments \u2014 can't void unpaid invoices yet. Strategy: run refund rate task daily until ACH clears, then pivot to credits. Brant owns the daily execution. Comms already sent to customers promising refunds (before the task was ready, awkward but done). Fix for future double-invoice schedules merging soon."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Security incident: 'fake' payment method ID flagged as social engineering*\n_Meeting: B&B Standup_\nSentry caught a payment method ID containing the word 'fake.' Turned out to be part of a broader incident \u2014 all affected companies had names designed to look like test/pen-test entities (social engineering to avoid scrutiny). Working with Stitch to understand the gap. Sentry noise issue (payment declined errors flooding billing reps channel) assigned to Edwin \u2014 Datadog monitor to be built to catch genuine spikes instead."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. Shift Fill callout timing: decision deferred \u2014 Swaib + Flor assessing effort*\n_Meeting: Shift Fill Whiteboarding (workspace)_\nThis is cross-team FYI context. Current SB implementation creates the callout immediately when 'Find a Cover' is clicked (before candidate list). New design from Deb: callout should be created AFTER the OEM approves the candidate list. Edge case: pre-populated stale candidates if OEM prompts a specific person. Effort TBD from Swaib + Flor. This matters because *Sina is fully committed here* \u2014 not available for hiring count + speed (Jatin said he was resolving the conflict; watch this)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. Shift Fill employee outreach surface still open: Request Feed vs. HBA DM*\n_Meeting: Shift Fill Whiteboarding (workspace)_\nRequest Feed has table migration and event pipeline implications (4+ new event types). HBA DM/messaging path is simpler for Sina and Parya, mobile-synced via OneStream. Risk: OMs with 50+ unread DMs miss callouts. Decision needs Daniel Chao to confirm. Not your decision, but Sina's availability directly affects your sprint \u2014 worth knowing this is still unresolved."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83c\udfaf YOUR ACTION ITEMS (from today)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2b50 *#1 SEND the Indeed email to Rachel (CC Tiger) \u2014 do this tonight or first thing tomorrow*\nThree questions finalized. Tiger cleaning up the doc. The email is *your* deliverable, not Tiger's. Every day this doesn't go out is another day without the answers you need to unblock the job posting ID architecture.\n\n\u2b50 *#2 Watch Magic Link tomorrow morning \u2014 Gbolade is bumping % on Nov 5*\nIf something looks off in Datadog or Amplitude, you'll want to catch it before it scales. Quick check ~10am.\n\n\u2b50 *#3 Ping Jatin: Is Sina's conflict actually resolved?*\nSina was in the Shift Fill whiteboarding session today (1.5 hrs). That confirms active SB/HBA work. Jatin said he was 'doing it right now' on Nov 2. It doesn't look resolved. Get a straight answer today."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udea8 OVERDUE WATCH LIST \u2014 These are bleeding*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\ud83d\udd34 *2029 Vision One-Pager \u2014 20+ DAYS OVERDUE* (CRITICAL)\nFadi submitted his. John's board meeting opened Oct 15. You presented the vision at the company kickoff Oct 26. The one-pager still doesn't exist. This is becoming embarrassing. Write it this week.\n\n\ud83d\udd34 *JD Rules for Divij \u2014 DAY 11 OVERDUE*\nDivij is idle waiting on this. Rules are known: 1 hire ~30d = vanilla, 2+ hires = 'multiple positions available', urgency \u22642wk = 'urgently hiring.' Write the doc today. 30 minutes of your time.\n\n\ud83d\udd34 *Interview Confirmation BDD Spec \u2014 OVERDUE*\nEngineering cannot start the spike (Jatin + Bob) until this is in their hands. The shape is locked. Write the BDD spec.\n\n\ud83d\udd34 *Indeed FSA Review \u2014 8 DAYS PAST DUE*\nJessica at Indeed hasn't responded. This is now overdue enough to escalate directly to Ashley Lutz. Don't wait for Jessica. Send the escalation.\n\n\ud83d\udd34 *Scheduling Ideal State Doc \u2014 CRITICAL (Malcolm is gone)*\nJatin called it out in the Nov 3 deep dive. Malcolm left Oct 30. You are the institutional memory now. Without this doc, the scheduling sprint loses its north star.\n\n\ud83d\udfe1 *Tallroo meeting dates \u2014 email unsent*\nNovember meeting. Include Skye. This is a minor one but it keeps showing up.\n\n\ud83d\udfe1 *Tag Fatty for magic link success screen Verify CTA designs*\nStill pending. 30 seconds to send the Slack message.\n\n\ud83d\udfe1 *Quiet 1:1 with Matan \u2014 schedule it*\nMatan is now ~40% pulled to core PMM (Susie gone). He's stretched. You should be checking in."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcc8 DAY GRADE: B+*\nSolid. You got the Indeed email to 'ready to send' status, which is real progress after the requisition ID gap you discovered Nov 3. Magic Link is running clean at 20%. The billing picture is clearer now that Edwin and Hilary are back. The overdue pile is the only thing keeping this from an A. You know what to do."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udca1 Tomorrow's Priorities*\n1. Send Rachel (Indeed) email \u2014 no excuses\n2. Write JD rules for Divij (30 min, unblock him)\n3. Magic Link check after Gbolade bumps the rollout %\n4. Ping Jatin on Sina's capacity situation (get a real answer)\n5. Start drafting Interview Confirmation BDD spec\n6. Escalate Indeed FSA to Ashley Lutz\n\nYou've got this. \ud83d\udcaa"
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff Daily Digest \u2022 Automated \u2022 Nov 4, 2026 (PST)_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Brief: Wednesday, Nov 4 | INDEED EMAIL LOCKED \u2022 MAGIC LINK CLIMBING \u2022 BILLING FIRE CONTAINED"
}


def preview():
    print("=" * 70)
    print("CHIEF OF STAFF DAILY BRIEF -- Wednesday Nov 4, 2026 (PST)")
    print("=" * 70)
    for b in blocks:
        if b["type"] == "header":
            sys.stdout.buffer.write(("\n>>> " + b["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif b["type"] == "section" and "text" in b:
            sys.stdout.buffer.write((b["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif b["type"] == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif b["type"] == "context":
            for el in b.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    print("=" * 70)


token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
).strip()

if not token:
    print("[INFO] No Slack token found. Printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"[SUCCESS] Message sent to {CHANNEL}. ts={body.get('ts')}")
    else:
        print(f"[ERROR] Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error: {e}")
    preview()
    sys.exit(1)
