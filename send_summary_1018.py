#!/usr/bin/env python3
import json
import os
import sys
import urllib.request

CHANNEL = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)


def build_blocks():
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "\U0001f1ea\U0001f1f8 Last Night in Spain \u2014 Weekend Digest | Sat Oct 17",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Happy last night in Spain, Manan!* \U0001f37b\u2728  "
                    "Zero meetings today \u2014 exactly as a Saturday should be. "
                    "This is your pre-Monday intel brief + full Monday battle plan so you "
                    "land in SF ready to rip. You\u2019re heading into one of the biggest weeks "
                    "of Q4 \u2014 board meeting week, first 26/23 Look-Ahead, and a very hot Indeed "
                    "situation. Let\u2019s go."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f50d Workspace Intel While You Were Off (Oct 15\u201316)*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*1\ufe0f\u20e3  Square Billing Fix \u2014 Decided \u2705 (Chris McIntosh, Oct 16)*\n"
                    "Permission granted: only the *first* location created from Square can bill through Square. "
                    "Every other location added to that company must bill through Homebase. "
                    "Ticket being written now. CS distributions team to quantify affected customers as follow-up.\n"
                    "_Why it matters:_ Latent bug (buying Plus plan through Square incorrectly placed ALL locations "
                    "on Plus, even at the outdated $24.95 price). This guardrail lands before the Chargebee migration "
                    "opens new surface area. No action needed from you."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*2\ufe0f\u20e3  Check \u00d7 Stripe Dunning \u2014 Decided \u2705 (B&B team, Oct 16)*\n"
                    "When Check churns a payroll company (insufficient funds) AND Stripe has a "
                    "past-due invoice simultaneously \u2192 *void the Stripe invoice + mark the "
                    "past_due event as canceled.* No more ghost dunning on already-churned companies.\n"
                    "_Why it matters:_ Right call. Homebase should not be attempting to collect on "
                    "companies Check has already churned. Cleans up a compounding billing edge case."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*3\ufe0f\u20e3  Chargebee Location Mover Edge Case \u2014 Resolved \u2705 (Brant Wellman, Oct 16)*\n"
                    "Found: subscription-level payment method blocks location move in Chargebee. "
                    "Fix = strip subscription-level payment method before moving. "
                    "Key rule: if moving a location to a company *without* a payment method on file, "
                    "customer must re-add one \u2014 Chargebee won\u2019t allow payment methods to cross company boundaries (fraud risk).\n"
                    "Brant now testing company-level consolidated billing (Flow 5). Labor v3 Protobuf "
                    "still blocked on tech-leadership approval \u2014 Hilary pinging Justin Monday."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*4\ufe0f\u20e3  SBA\u00d7HBA Callout Edge Cases \u2014 All Decided \u2705 (Gurkiran + Felix, Oct 15)*\n"
                    "Four edge cases locked ahead of Sunday\u2019s handoff:\n"
                    "\u2022 *Callout on shift with unpublished edits:* Backend architectural constraint \u2014 "
                    "can\u2019t create callout. Decision: notify manager instead of blocking. Deferred from this release.\n"
                    "\u2022 *Manager edits shift with active callout:* Show confirmation "
                    "\u2018Callout will be deleted if you proceed \u2014 are you sure?\u2019 If yes \u2192 "
                    "auto-delete callout + execute change. Manager free to start new callout.\n"
                    "\u2022 *Deleting shift with active callout:* Same pattern \u2014 confirm + auto-cancel callout.\n"
                    "\u2022 *Bulk publish with active callouts:* Skip callout-locked shifts, surface exception clearly."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f4c5 Tomorrow \u2014 Sunday Oct 18 (Travel Day)*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\u26a0\ufe0f *SBA\u00d7HBA Shift Fill Handoff* \u2014 Daniel Christo + Felix DeHerrera\n"
                    "Edge cases are decided and Gurkiran + Felix are aligned (see above). "
                    "Show up ready to confirm integration scope, any remaining open items, and launch timeline.\n\n"
                    "*Also tonight:* If you can squeeze in 30 min \u2014 review 26/23 Look-Ahead "
                    "spec steps 1\u20138 and confirm Fadi\u2019s low-fi is ready. Board meeting week starts Monday. No runway."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f3e0 Monday Oct 19 \u2014 RETURN DAY BATTLE PLAN (SF, Board Meeting Week)*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f525 Fire First (Pre-Meeting, 8am-ish)*\n"
                    "1. *Indeed Source Name Rollback \u2014 Day 56:* "
                    "Ping Ashley \u2014 did she green-light Bob\u2019s PR after meeting T&S on Oct 14? "
                    "Do NOT let this go another day without confirmation. Bob\u2019s PR is raised, "
                    "awaiting merge. Ashley is the unlock.\n"
                    "2. *3-Year Vision One-Pager:* "
                    "Block 90 minutes BEFORE the Look-Ahead. Board meeting opened Oct 15. This is overdue. John is watching.\n"
                    "3. *Town Hall Q&A:* Submit your questions by end of Monday (Town Hall = Friday Oct 23). "
                    "Use the Q4 scope review + board prep as fodder."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f4cb Morning Priority Queue*\n"
                    "4. *26/23 Look-Ahead:* First meeting of the day. "
                    "Spec steps 1\u20138 + Fadi low-fi ready. This sets the cadence for the sprint.\n"
                    "5. *Sync with Divij:* Q4 TS priorities. He has been waiting two weeks. Block 30 min.\n"
                    "6. *Carlo KT \u2014 URGENT:* Paternity started Oct 14. NO KT captured in any meeting. "
                    "Send async Slack/doc immediately: AE65 source name change, "
                    "Iterable 6 emails not firing, \u2018do not syndicate\u2019 bug, continuation sizing.\n"
                    "7. *Indeed Partner Console \u2014 Tiger:* "
                    "Follow-up sent Oct 14 (Tiger CC\u2019d). Escalate if no response from Marketplace Support."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f6a6 Afternoon*\n"
                    "8. *Indeed Release Blocker:* Identify right Indeed contact. "
                    "Coordinate pre-release arch review (Tiger joining). Must resolve before job posting ships.\n"
                    "9. *Fadi Sync \u2014 Intent Capture UX:* Align on experience before bringing to "
                    "engineering for scoping. Blocking 26/23 work.\n"
                    "10. *Syndication Timing Measurement:* Draft requirements + simple viz for Jatin. "
                    "Even a Claude-generated mockup is fine.\n"
                    "11. *IBK \u2014 Facebook API:* No update since Oct 9. Day 24. Ping now.\n"
                    "12. *Dunning Bug \u2014 Ping Dipesh:* Revenue leak. He was in B&B standup Oct 16 \u2014 "
                    "confirm status and whether the Chargebee-Salesforce integration got unblocked.\n"
                    "13. *Pending Syndication Data Split:* Get initial thinking ready for Wednesday Discovery."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\U0001f4cc Whenever You Get a Pocket of Time*\n"
                    "14. *Matt McAllister intro:* New CMO, Day 22 Monday. From Yelp. "
                    "Great week to do it \u2014 everyone is in SF for board week.\n"
                    "15. *Push Cindy on mobile signup:* +900 hiring-interested OEMs/month potential. "
                    "Growth team is hesitant. Too big to sit.\n"
                    "16. *Omni/Looker access:* Went dark Oct 2. Day 16. Ping IT.\n"
                    "17. *Prompt chips min wage:* Write the MD file + ping Justin "
                    "(he also has the Labor v3 Protobuf blocker \u2014 ask Hilary if she needs you to escalate).\n"
                    "18. *Trial source claiming \u2192 100%:* Decision made Oct 9. Still pending. Flip it.\n"
                    "19. *ORCA Comms Quality QA:* Matan built the skill. "
                    "IBK needs manual QA before scaling to 80 touchpoints."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f6a8 Critical Watch List*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "\U0001f534 *INDEED FEED SUSPENDED \u2014 Day 56.* "
                    "ROOT CAUSE CONFIRMED (AE65 suffix). Bob\u2019s rollback PR raised. "
                    "Ashley met T&S Oct 14. Merge confirmation still pending. Monday #1.\n"
                    "\U0001f534 *FACEBOOK API \u2014 Day 24.* All calls failing. Bob + IBK. No update since Oct 9.\n"
                    "\U0001f7e1 *3-YEAR VISION ONE-PAGER:* Board meeting week. Overdue. Block 90 min Monday AM.\n"
                    "\U0001f7e1 *CARLO KT:* Knowledge risk. AE65 source name, Iterable 6 emails, "
                    "do-not-syndicate bug. Do async KT immediately.\n"
                    "\U0001f7e1 *INDEED SECOND BUG:* Fraud-flagged jobs still syndicating. "
                    "Bob/Carlo to investigate \u2014 includes Carlo KT.\n"
                    "\U0001f7e1 *INDEED RELEASE BLOCKER:* Arch review + Indeed contact needed before job posting ships.\n"
                    "\U0001f7e1 *MATCH EXPLANATION WORKSHOP:* Block next Wednesday Discovery. "
                    "Invite Skye, Bob, Matan. FigJam format.\n"
                    "\U0001f7e1 *GIFT CARDS OWED:* Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50).\n"
                    "\U0001f7e1 *EMAILS UNSENT:* John Waldman (EarnBetter NDA + docs), "
                    "Marina/Mundo Academy (26+ days late).\n"
                    "\u26aa *OMNI ACCESS:* Looker dark since Oct 2.\n"
                    "\u26aa *COMMS ASSISTANT production decision:* Malcolm leaving Nov\u2013Dec. Overdue.\n"
                    "\u26aa *DEPARTURES SIGNAL DOCS:* 30+ days overdue \u2014 Zane, Sean, Jon W, Bobby."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Q4 Sprint State:* "
                    "26/22 = buffer sprint \u2705 (swarm on specs only) | "
                    "26/23 Look-Ahead = Monday first meeting \u2605\n\n"
                    "_Timezone note: Starting Monday Oct 19, your digest switches from CEST to PDT "
                    "(you\u2019re back in SF \U0001f966). Same midnight UTC cron, but now it reviews your "
                    "same-calendar-day SF workday instead of the prior CEST day._\n\n"
                    "You crushed it from Spain, Manan. Three weeks of remote work, "
                    "board-week prep, Q4 scope locked, sprint process overhauled, "
                    "F&B research in motion \u2014 all from a 9-hour time zone gap. "
                    "Walk into SF on Monday like you own the place. \U0001f4aa"
                )
            }
        }
    ]


def send_to_slack(blocks):
    payload = json.dumps({
        "channel": CHANNEL,
        "text": "Weekend Digest (last night in Spain) | Sat Oct 17",
        "blocks": blocks
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def preview(blocks):
    lines = []
    for b in blocks:
        btype = b.get("type", "")
        if btype == "header":
            lines.append("\n=== " + b["text"]["text"] + " ===")
        elif btype == "divider":
            lines.append("-" * 70)
        elif btype == "section":
            text = b.get("text", {}).get("text", "")
            if text:
                lines.append(text)
    sys.stdout.buffer.write("\n".join(lines).encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


blocks = build_blocks()

if TOKEN:
    result = send_to_slack(blocks)
    if result.get("ok"):
        print("SUCCESS: Message sent to Slack channel", CHANNEL)
    else:
        print("SLACK ERROR:", result.get("error"))
        print("\nPREVIEW MODE (send failed):")
        preview(blocks)
else:
    print("NO SLACK TOKEN \u2014 PREVIEW MODE:")
    preview(blocks)
