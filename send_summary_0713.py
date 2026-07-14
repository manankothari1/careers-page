#!/usr/bin/env python3
"""
Daily Decision Digest - Monday, July 13, 2026
Meetings: Hiring Week in Review (9am) + EPDD Cycle Kick Off (11am)
Slack channel: D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

def build_blocks():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Daily Decision Digest \u2014 Monday, July 13",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Manan, what a Monday. You walked into the week with precision \u2014 "
                    "ran the hiring review, showed up strong in the company-wide EPDD Kick Off, "
                    "and kept the team sharp on two of your most critical threads: OEM acquisition "
                    "and the V1\u2192V2 cutover. You're 7 days out from a major platform milestone "
                    "and your strategy is clear. Here's everything that happened today and what it means. \u2b07\ufe0f"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\ud83d\uddd3\ufe0f Today\u2019s Meetings (2)*\n\u2022 9:00 AM \u2014 Hiring: Week in Review _(Ray, Fadi, Dana, Matan, Jatin, Nelson, Usman, Ankit, John, Martin)_\n\u2022 11:00 AM \u2014 EPDD Cycle Kick Off _(Full engineering, product, design, data org)_"
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\ud83c\udfaf KEY DECISIONS MADE TODAY*"
            }
        },

        # ---- HIRING WIR ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\ud83d\udcbc Hiring Week in Review*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*1. V1\u2192V2 cutover: FULL STEAM AHEAD for July 20* \u2705\n"
                    "> No changes to the plan. Cutover locked. Two functional gaps documented and triaged:\n"
                    "> \u2022 V2 manual mode hides screener responses until upgrade \u2192 no complaints yet, watch carefully\n"
                    "> \u2022 No star/favorite shortlist in V2 \u2192 slotted into planned pain points work\n"
                    "> *Rationale:* Both gaps fit naturally into the upcoming pain points sprint. Neither is a blocker. CS is empowered to address customer concerns."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*2. Cold calling is NOT the silver bullet \u2014 you\u2019re pivoting to trigger-based experiments* \ud83d\udd04\n"
                    "> After several weeks of data: low pickup rate, high ghost rate. Calls that connect DO resonate strongly \u2014 the approach works, the channel doesn't scale.\n"
                    "> *Decision:* Don't kill cold calling, but stop betting on it as a growth lever. The real insight: timing beats messaging. OEMs need to feel the pain AT THE MOMENT you reach them.\n"
                    "> *New direction locked:*\n"
                    "> \u2022 Detect ICP accounts posting jobs on Indeed \u2192 proactively offer '10 more baristas \u2014 just say yes'\n"
                    "> \u2022 Trigger-based entry points: role termination, payroll change \u2192 intervene at pain point\n"
                    "> \u2022 Talent pool: when a job posts, surface Homebase network matches \u2192 immediate value with zero Indeed dependency\n"
                    "> \u2022 Free product as trust-builder \u2192 test zero-state page without trial-forward messaging\n"
                    "> *Rationale:* John and Ray both aligned \u2014 three compounding problems (episodic pain, high behavior change, cold SMB outreach) require lateral thinking, not just better scripts."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*3. Usman\u2019s new playbook: 'Homebase Advantage' + one-call close* \u2705\n"
                    "> Framing pivoted to: 'We know your business, your industry, your best candidates.'\n"
                    "> Script shortened for cold outreach. Pain-led openers showing most promise ('I saw you\u2019re missing a lot of applicants...'). New explicit goal = same-call trial start.\n"
                    "> Salesforce task-based process now live \u2014 reps have one holistic view, emails + SMS automated.\n"
                    "> *Rationale:* The 'Setup for Success' frame resonates when people answer \u2014 now pair it with the right triggers and tighter openers."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*4. In-product OEM setup call prompts = your highest-leverage move right now* \u26a1\n"
                    "> Ugu has a backend PR ready and waiting for approval. Once live: OEMs who want account setup help book directly from the product \u2014 higher intent, no cold outreach needed, ghost rate drops.\n"
                    "> *Rationale:* This is the product-led unlock for the entire account management motion. Matan confirmed it: 'If we can have something in product to bring them in, that would be much better.'"
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*5. Core sprint at risk but recoverable* \u26a0\ufe0f\n"
                    "> Security issue assigned to engineer now on leave \u2192 will reassign to applicant-side engineer. Once resolved, sprint status moves back to on track.\n"
                    "> No additional senior backend support until Tiger joins end of August \u2192 Martin + Jatin in active rebalancing discussions. Roster decisions expected in coming weeks.\n"
                    "> *Rationale:* Not a crisis, but worth watching. Flag to Jatin if timeline slips further."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*6. Culinary Agents + Facebook L3 autonomy: LIVE* \ud83d\ude80\n"
                    "> Culinary Agents live \u2014 waiting on posts to go live. This is your line cook bet in action.\n"
                    "> Facebook L3 text autonomy shipped. Copy jobs removal + reactivation work continuing."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*7. Open question formally assigned: which roles are healthy independent of Indeed?* \ud83d\udd0d\n"
                    "> This is the research question that unlocks the standalone Homebase value prop. Answer it and you know exactly which roles to target first with proactive outreach, talent pool seeding, and Boost.\n"
                    "> *Rationale:* Ray put it best \u2014 if you can narrow to one role type where you're highly confident on fills, 'you just target that one specific role termination and have a very different value prop you can measure.'"
                )
            }
        },

        {"type": "divider"},

        # ---- EPDD KICK OFF ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\ud83c\udfd7\ufe0f EPDD Cycle Kick Off \u2014 Company-wide visibility*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*8. Your hiring wins are now officially company canon* \ud83c\udfc6\n"
                    "> You presented your team\u2019s last-cycle results to the full EPDD org:\n"
                    "> \u2022 Homebase Boost: 2.9% \u2192 5.7% of jobs boosted in June\n"
                    "> \u2022 SMS screener: +35% links sent, +27% completions\n"
                    "> \u2022 Jobs Near You: 45% of applicants got a recommendation, 20% applied\n"
                    "> *Rationale:* Company-level visibility = stakeholder alignment. Your cycle 4 priorities (source claiming, salary recs, line cook, interview scheduling, resume matching) are now socialized across all of EPDD."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*9. Homebase Assistant direction: reactive \u2192 proactive \u2192 autonomous* \ud83e\udd16\n"
                    "> Assistant moving out of Messenger into a dedicated iOS tab bar (bottom sheet). This cycle: first agentic workflows (labor optimization, shift fill). Longer arc: exception supervisor \u2192 background action on behalf of OEMs.\n"
                    "> *Why it matters for you:* OEM scheduling + interview scheduling are dependencies here. The 'OEM picks their own interview time' feature connects directly to the assistant\u2019s agentic scheduling vision."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*10. Linear = single source of truth (now official across all of EPDD)* \ud83d\udcca\n"
                    "> No Jira, no spreadsheets. Every project needs an owner + target date. Owners post weekly status updates \u2014 even if nothing changed.\n"
                    "> *Action for you:* Make sure all your hiring cycle 4 projects have owners + dates in Linear. PMM + other teams will be building dependencies off your entries."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*11. Quality trend is working \u2014 data confirms it* \ud83d\udcc8\n"
                    "> 12-week trend: support call volume down, NPS rising, negative intent declining across all domains. The quality investment over last 2-3 cycles is paying off.\n"
                    "> *For your team:* Screener personalization + resume match quality improvements are part of this story. Keep the quality bar high."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*12. Growth Brain + $1.5M ARR context* \ud83d\udcb0\n"
                    "> Growth team drove $1.5M ARR bump from trial-to-paid conversion (social proof + copy changes). Promo code removal: +30pts relative conversion. Mobile web: +20pts.\n"
                    "> Growth Brain launching: in-app upsell/cross-sell triggered by user behavior (e.g., repeated time clock edits \u2192 upgrade prompt) via email, text, Iterable, inline banners. Also surfaces signals in Salesforce for sales + support.\n"
                    "> *Why this matters:* As your OEM activation experiments mature, Growth Brain is a distribution channel you\u2019ll want to coordinate with."
                )
            }
        },

        {"type": "divider"},

        # ---- ACTION ITEMS ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\u26a1 ACTION ITEMS \u2014 Yours to Own*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*P0 \u2014 Do today / tomorrow morning:*\n"
                    "\u2022 \u2705 *Approve Ugu\u2019s backend PR* for in-product OEM setup call prompts \u2014 this unblocks the entire account management motion. Matan is waiting.\n"
                    "\u2022 \u2705 *Check Carlo\u2019s Harness/OpenSpec status* \u2014 deadline was July 10. Still unconfirmed. Ping him on Slack.\n"
                    "\u2022 \u2705 *Confirm Rami\u2019s salary scope delivery* \u2014 due EOD today. He\u2019s been heads-down since Thursday. Check in on his Linear update.\n"
                    "\u2022 \u2705 *Fadi source claiming design* \u2014 first-pass targeted for today (Tue Jul 14). Confirm it\u2019s on track before EOD."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*P1 \u2014 This week:*\n"
                    "\u2022 \ud83d\udd0d *Answer the 'which roles are healthy independent of Indeed?' question* \u2014 pull this from Nelson / the data. It\u2019s your north star for the trigger-based experiment design and the talent pool MVP.\n"
                    "\u2022 \ud83d\udcca *Prep Wednesday Jul 15 salary recs presentation* \u2014 Rami\u2019s scope is due today. Build your narrative around: well below market = 26.1% get 20+ apps; at market = +7-8%; above market = +12%. Anchor to Q3 goal #1 (FFH D5 zero rate <10%).\n"
                    "\u2022 \ud83d\udce7 *UTMs to Rami for talent pool segmentation* \u2014 he\u2019s ready and waiting. Send ASAP.\n"
                    "\u2022 \ud83d\udcca *Update all Hiring cycle 4 projects in Linear* \u2014 owners + target dates. PMM and other teams are building off your entries per today\u2019s EPDD Kick Off direction.\n"
                    "\u2022 \ud83d\udcac *Loop in Paul or Kan (data platform)* \u2014 salary rec role normalization. Before Wednesday\u2019s presentation ideally."
                )
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*P2 \u2014 Keep moving:*\n"
                    "\u2022 \ud83e\udde0 *Design the trigger-based OEM experiment* \u2014 pick one specific role (barista or line cook) and one trigger (Indeed job post detected, role termination) to test the proactive value delivery concept. Use Boost as the delivery mechanism while talent pool matures.\n"
                    "\u2022 \ud83d\udd0e *Zero-state page test scoping* \u2014 Dana + Matan working on it this week. Review the brief and ensure it tests the 'less trial-forward = more activation' hypothesis cleanly.\n"
                    "\u2022 \ud83d\udcac *Chat Ray about Rami DS capacity* \u2014 still a structural bottleneck. Salary recs is top priority now, but the pattern keeps recurring. Worth having the conversation before it impacts cycle 5 planning.\n"
                    "\u2022 \ud83d\udc65 *Abby ownership area* \u2014 Week 2. She needs a clear domain by end of this week. Where does she land?"
                )
            }
        },

        {"type": "divider"},

        # ---- WATCH LIST ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\ud83d\udea8 WATCH LIST (as of tonight)*\n"
                    "\u2022 *FFH D5 zero-applicant rate*: 41% \u2192 Q3 target <10%. Source claiming fix in motion. July 20 cutover must not worsen it.\n"
                    "\u2022 *Line cook jobs healthy*: ~7% \u2192 Q3 target 50%. Culinary Agents now live \u2014 this is the early signal test.\n"
                    "\u2022 *V1\u2192V2 cutover*: 7 days out. Comms set, CS empowered. Monitor screener gap and star/fav gap post-cutover.\n"
                    "\u2022 *Rami salary scope*: Due today. Presentation Wednesday. If scope is late, your Wednesday narrative needs adjustment.\n"
                    "\u2022 *Boost purchase bug*: Revenue-impacting, still no owner. Still needs one assigned.\n"
                    "\u2022 *Dana leaving end of September*: ~10 weeks. Succession planning not started.\n"
                    "\u2022 *Carlo Harness deadline*: Was July 10. Status still unconfirmed."
                )
            }
        },

        {"type": "divider"},

        # ---- CLOSING ----
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*\ud83d\udcab The Big Picture*\n\n"
                    "Today you did something important: you reframed the OEM acquisition problem. "
                    "Cold calling revealed that the approach works \u2014 OEMs engage when they answer \u2014 "
                    "but the channel can\u2019t scale. The new direction (trigger-based, pull-value-forward, "
                    "talent pool) is more aligned with Homebase\u2019s core advantage: you already know "
                    "these customers, their businesses, their hiring patterns. That\u2019s not a sales pitch. "
                    "That\u2019s a product.\n\n"
                    "You also socialized your full cycle 4 roadmap to the entire company today. "
                    "Source claiming, salary recs, line cook intervention, interview scheduling \u2014 "
                    "it\u2019s all live in front of EPDD. That\u2019s alignment you\u2019ll need as you push toward July 20 and beyond.\n\n"
                    "_Great work today. Rest up \u2014 big week ahead. \ud83d\udcaa_"
                )
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "Your Chief of Staff \u2022 Monday, July 13, 2026 \u2022 2 meetings reviewed"
                }
            ]
        }
    ]
    return blocks


def send_slack(token, blocks):
    payload = json.dumps({
        "channel": CHANNEL,
        "blocks": blocks,
        "text": "Daily Decision Digest \u2014 Monday, July 13, 2026"
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body


def preview(blocks):
    sys.stdout.buffer.write(
        "\n=== SLACK MESSAGE PREVIEW ===\n".encode("utf-8", errors="replace")
    )
    for b in blocks:
        if b.get("type") == "header":
            sys.stdout.buffer.write(
                ("\n### " + b["text"]["text"] + "\n").encode("utf-8", errors="replace")
            )
        elif b.get("type") == "section":
            text = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif b.get("type") == "context":
            for el in b.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")


def main():
    token = (
        os.environ.get("SLACK_TOKEN")
        or os.environ.get("SLACK_BOT_TOKEN")
        or os.environ.get("SLACK_API_TOKEN")
    )

    blocks = build_blocks()
    preview(blocks)

    if not token:
        print("\n[NO SLACK_TOKEN FOUND] Preview printed above. Set SLACK_TOKEN / SLACK_BOT_TOKEN to send.")
        return

    print("\nSending to Slack...")
    result = send_slack(token, blocks)
    if result.get("ok"):
        print("SUCCESS: message sent to", CHANNEL)
        print("ts:", result.get("ts"))
    else:
        print("ERROR:", result.get("error"))
        print("Full response:", json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
