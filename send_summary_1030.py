#!/usr/bin/env python3
"""Chief of Staff daily digest - Friday Oct 30, 2026 PDT"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL_ID = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Chief of Staff Daily Digest — Friday, Oct 30 :airplane_arriving::tada:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*BIG DAY, Manan.* Today was the first formal sprint close, Malcolm's last standup before leave, "
                "AND your last day in Paris. You absolutely crushed the week. Here's how it all landed."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:calendar: Meetings Today (Oct 30 PDT — 4 captured)*\n"
                "• 7:52am — *Hiring Product Roadmap & Resourcing* w/ Jatin\n"
                "• 8:45am — *B&B Standup & Ticket Refinement* (workspace)\n"
                "• 9am — *Hiring EPD Standup* (full team + Malcolm's final)\n"
                "• 11am — *Schedule Squad Review* (SBA forecasting UX, workspace)"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":brain: *BIG DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Scheduling = Patches, Not a Rebuild :wrench:*\n"
                "Malcolm delivered his final verdict in today's standup: *incremental patches to the existing Nihilus-based system* — "
                "NOT a full rebuild, and NOT a vendor switch in Q4 or Q1. Series of modular improvements, "
                "each flow mapped, each problem color-coded (green/yellow/red). Jatin fully endorsed. "
                "_Rationale: Full rebuild is a massive product + engineering undertaking across too many flows. "
                "Patches give you progress while Manan designs the ideal future state._\n"
                "> *What this means:* You're NOT designing patches. You're designing the ideal state — Skye made this clear. "
                "Your job is to define what scheduling SHOULD be. Malcolm's doc is the map of what exists. "
                "Then the gap between ideal and reality gets closed incrementally."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Jatin Will Defend Divij Against Ankit's DS Audit :shield:*\n"
                "Ankit Bhatia is doing a company-wide audit of DS staffing — asking every team if engineers could "
                "replace their DS resources. Jatin's position: *keep Divij, offer an engineer for one week in trade.* "
                "You walked Jatin through exactly why Divij is irreplaceable: match co-build requires DS, "
                "screener toggle decoupling requires DS, fraud prompt revision requires DS. "
                "_Rationale: Engineering can potentially absorb Hiring Count & Speed, but everything else is legitimately DS work. "
                "Losing Divij now would be a critical hit to your sprint._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Soheil = Engineering Partner for Hiring Count & Speed + Prompt Chips :electric_plug:*\n"
                "Jatin assigned Soheil in standup as the eng partner for getting hiring count & speed into production. "
                "He's already doing prompt chip updates, so this is a natural fit. "
                "_Rationale: Soheil has the adjacent context. Keeps the work in the sprint without loading Tiger or IBK._"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. (Confidential) Matan Going ~40% to Core PMM :hushed:*\n"
                "Keep this DL: Susie got fired, leaving only Linda and Matan as PMMs. "
                "Skye is pulling Matan to split ~40% of his time to core product marketing. "
                "This is not public yet. _Rationale: company-level PMM gap, forced reallocation._ "
                "You will feel this — Matan's capacity for hiring team work, the 3 projects (intent propensity, "
                "onboarding wizard, pricing/packaging), and your local testing env setup all get squeezed. "
                "Start mentally resetting Matan's bandwidth."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Fraud Prompt Needs Another Revision After Magic Link Ships :warning:*\n"
                "You flagged this in the roadmap call with Jatin: the fraud prompt has too many false positives "
                "right now (intentionally conservative). Once OTP -> Magic Link ships and we have better identity "
                "verification, *we need another pass on the fraud model with Divij* to tune down false positive rate. "
                "_This is a Divij work item — add it to the queue._"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rocket: *NOTABLE SHIPPING / MILESTONES TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *:jack_o_lantern: Spooky Season feature SHIPPING TODAY* — IBK + Fadi. Halloween UI, "
                "designed by Fadi, going live Oct 30. Off after today.\n"
                "• *Customer Entitlement Events NOW LIVE* — JJ confirmed the entitlement event emitter merged "
                "and emitting. Adam's workers consuming them are in PR. Entitlements rollout pipeline is functioning.\n"
                "• *Change Payment Method flag target = NEXT WEEK* — Edwin: BB259 endpoint solution found, "
                "3DS work nearly done. Flag turn-on expected end of next week.\n"
                "• *Malcolm's LAST STANDUP* :saluting_face: — Leaves today. Returns last week of December. "
                "He shared his scheduling spike doc with the team. Scheduling context is now handed off to you."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *BLOCKERS & WATCH ITEMS — STATUS UPDATES*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Facebook API — Rate Limiting RESURFACES (Day 35+):* Iszael found new errors starting Oct 20 "
                "(no code change on our side). Waiting on Facebook response in the Meta Slack channel. "
                "Jatin CC'd. Not the same as the original API failure but new rate-limit errors. *Still critical.*\n"
                "• *Jobcase Feed Test:* Iszael following up today. They tested late (jobs expired), new jobs added. "
                "Waiting on Jobcase to confirm. Jatin CC'd.\n"
                "• *Tiger's Close Flow Bug:* Interview cancel -> Nihilus infinite spinner. Tiger fixing today. "
                "Also testing disposition sync flow with Manan — needs an Indeed-unflagged job.\n"
                "• *Carlos's Indeed Status Spike* (Tiger inheriting): ~midweek next week. Tiger + Soheil potentially.\n"
                "• *Billing Data Gap Discovered (Brant/Chris):* Secure trial end events have NOT been emitting for 1+ year "
                "= unreported revenue in APH. David Lin now investigating. Revenue accounting discrepancy risk. "
                "Not Manan's issue directly, but *entitlements rollout downstream risk.*\n"
                "• *Sina Status UNKNOWN:* You flagged in standup — haven't heard from Sina on hiring intent capture start. "
                "Jatin will follow up with Ankit + Sina."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":memo: *YOUR ACTION ITEMS — DO NOT LET THESE SLIDE*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Immediate (tonight / this weekend):*\n"
                "1. :page_facing_up: *Write the Scheduling Ideal State doc* — Malcolm is gone. "
                "This is now 100% on you. Define what scheduling SHOULD look like for customers. "
                "Answer Bob's open questions doc. This is *critical* — Malcolm's spike docs are your starting point.\n"
                "2. :page_facing_up: *Scheduling behaviors with Fadi* — You said in standup you're compiling use cases. "
                "Get these finished before you get back into SF mode Monday.\n"
                "3. :page_facing_up: *Interview Confirmation BDD spec* — You told the team you're working on this. "
                "Jatin + Bob need it to start the spike. Write it.\n"
                "4. :page_with_curl: *JD Rules for Divij* — DAY 6 OVERDUE. This is literally blocking him. "
                "Takes 10 minutes. Just send it.\n"
                "5. :paintbrush: *Tag Fatty for Verify CTA designs (Magic Link success screen)* — "
                "STILL on this list. Do it Sunday.\n"
                "\n*This week (Mon-Tue):*\n"
                "6. :mag: *Review Malcolm's scheduling doc with Skye* — He's adding it to the Linear ticket. "
                "Block 45 mins with Skye early next week.\n"
                "7. :spiral_note_pad: *2029 Vision One-Pager* — Still CRITICAL OVERDUE. "
                "You presented the vision at kickoff. The board has been open since Oct 15. Write it.\n"
                "8. :speaking_head_in_silhouette: *Matan bandwidth reset* — Have a quiet 1:1 with Matan Monday "
                "to understand how his 40% PMM split affects the 3 projects. Adjust plans accordingly.\n"
                "9. :handshake: *Indeed FSA Review status* — Still no update from Jessica (was due Oct 27). "
                "Escalate to Ashley Lutz Monday. You cannot let this sit another week.\n"
                "10. :e-mail: *Indeed company field bug reply to Indeed support* — 8 DAYS OUTSTANDING. "
                "Draft and send.\n"
                "11. :e-mail: *Doreen (Welcome Tech EA) decline email* — Decline Q4, suggest Q1 reconnect.\n"
                "12. :gift: *Gift cards owed* — Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50).\n"
                "13. :e-mail: *Emails unsent* — John Waldman (EarnBetter NDA), Marina/Mundo Academy (28+ days). "
                "Both overdue."
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":trophy: *SPRINT CLOSE SCORECARD — Sprint 1 (First Formal Close)*\n"
                "Today was the first Friday close under Skye's new ceremony structure. "
                "IBK shipped Magic Link (gated at 0%, ready to roll). Spooky season shipped. "
                "Entitlement events live. Close flow in final testing (Tiger). "
                "Disposition sync in progress. Malcolm's scheduling spike delivered on his last day. "
                "That's a solid sprint close for a sprint that had Malcolm going out and Paris timezone lag.\n\n"
                "*Day Grade: A-* :star::star::star::star-half:\n"
                "_Theme: PATCHES NOT REBUILD — MALCOLM PASSES THE TORCH — PARIS CHAPTER ENDS_"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":crystal_ball: *MONDAY BATTLE PLAN (Nov 2)*\n"
                "You're back in SF, back in PDT rhythm. Here's what Monday looks like:\n"
                "• 8am-ish: Hiring Leads Standup — check in on Tiger's close flow + Carlos spike handoff\n"
                "• Block with Skye: Malcolm's scheduling doc review (add to calendar NOW)\n"
                "• Matan 1:1: reset expectations on his 40% PMM split\n"
                "• Indeed FSA: escalate to Ashley Lutz if still no Jessica response\n"
                "• Nihilus decision: the Nov 3 deadline is *4 DAYS AWAY* — Izzy needs scope, Skye is talking to Nihilus. You need to be in the room for this decision.\n\n"
                "_:heart: Welcome home, Manan. Paris was real. SF is ready. Let's finish Q4 strong._"
            )
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Chief of Staff Digest — Friday Oct 30, 2026",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK DIGEST PREVIEW (Oct 30 PDT) ===\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("=== END PREVIEW ===\n").encode("utf-8", errors="replace"))

if not TOKEN:
    print("SLACK_TOKEN not set — printing preview only.")
    preview()
    sys.exit(0)

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
        body = json.loads(resp.read().decode("utf-8"))
        if body.get("ok"):
            print("Slack message sent successfully!")
            print(f"  ts: {body.get('ts')}")
        else:
            print(f"Slack API error: {body.get('error')}")
            preview()
            sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
