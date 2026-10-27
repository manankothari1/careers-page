#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Monday Oct 26, 2026 PDT
3 meetings captured. Sprint kicked off. Vision presented. Ceremony restructured.
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
                "text": "\U0001f4bc Monday Debrief \u2014 Oct 26, 2026",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Day Grade: A \u2b50* \u2014 Big Monday. Sprint launched with full team alignment, company-wide vision delivered, ceremony structure locked. Jatin back and productive. Lots of great momentum.\n\n*Theme: SPRINT STARTS STRONG \u2014 FRIDAY CLOSE = NEW STANDARD*"
            }
        },
        {"type": "divider"},

        # Meetings Today
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f4c5 Meetings Today (3)*\n\u2022 *9:00 AM \u2014 Hiring: Week in Review* (Matan, Jatin, Jan, Jon, Skye) \u2014 Transactional comms QA, sprint structure gaps\n\u2022 *10:00 AM \u2014 Company Sprint Kickoff* \u2014 New team intros, hiring product state + vision presented\n\u2022 *10:30 AM \u2014 Hiring \u003e Sprint Kickoff* (Full team: Jatin, IBK, Tiger, Iszael, Soheil, Malcolm, Bob, Divij, Skye, Fadi, Matan) \u2014 Sprint goals locked, ceremony restructured"
            }
        },
        {"type": "divider"},

        # Decisions
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\u2705 Decisions Made Today*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*1. Sprint priorities locked (3 pillars)*\n\u2022 Indeed job post lifecycle (Tiger)\n\u2022 OTP \u2192 Magic Link (IBK)\n\u2022 Disposition sync \u2014 send candidate interview status back to Indeed\n_Why: Single sprint goal framing going forward (Jatin). These three are the foundational delivery this sprint._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*2. Two transactional emails KILLED immediately*\n\u2022 'Job expiring in 3 days' \u2014 OFF\n\u2022 'Job post expired' \u2014 OFF\n_Why: Both contain a Renew CTA that doesn\\'t exist in the product yet. Live emails pointing to a dead flow = broken OEM experience. Matan owns the kill switch._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*3. Command AI modal rollout PAUSED*\n\u2022 Modal firing before payroll runs (off-cycle payroll trigger)\n\u2022 Second modal incorrectly appearing on sign-up/sign-in screen\n_Why: Wrong timing destroys trust. Matan holds the deployment; will fix trigger before re-enabling. Darren/Soumya/Steve investigating sign-in instance._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*4. Sprint ceremony structure locked (Skye\\'s proposal)*\n\u2022 Sprint closes Fridays: demo against goal, review statuses, decide carryover\n\u2022 Kickoff: board pre-filled before meeting; just hit 'start sprint'\n\u2022 Every sprint must have an outcome-oriented goal (not just ticket completion)\n\u2022 80/20 product vs. engineering tickets; flex with discussion when outside that band\n\u2022 Multi-sprint work \u2192 Linear initiative; each sprint\\'s slice = child project\n_Why: No more ad-hoc carryover or unclear sprint health. First formal close: this Friday._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*5. Engineers now own the ship call*\n\u2022 Manan + Fadi retain right to interject; they no longer run it\n\u2022 Specs as currency: layer 1 spec feeds Orca or Forge, agents draft and break down\n_Why: Clear accountability. Eng owns delivery; product/design owns scope and quality._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*6. 'Hiring: Week in Review' meeting CANCELLED*\n\u2022 Replaced by recurring sprint kickoff after the company-wide kickoff\n\u2022 Manan to schedule with Jatin ASAP\n_Why: No longer fits sprint cadence. The new kickoff covers close, carryover, and new work assignment._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*7. Disposition sync added as sprint priority*\n\u2022 Carlo\\'s job-status-retrieval ticket (Job Sync API, 3-legged auth): UNASSIGNED and at risk\n\u2022 Jatin to reassign \u2014 distinct from disposition sync but adjacent\n_Why: If Carlo\\'s ticket falls through it blocks the full disposition sync story. Jatin is on it._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*8. Homebase hourly market maker vision presented at company kickoff*\n\u2022 Thesis: 80% of workers leaving a Homebase biz find another Homebase biz hiring same role within 15 miles + 30 days\n\u2022 Roadmap: (1) Now \u2014 best standalone job posting; (2) 2027 \u2014 unlock talent network; (3) Beyond \u2014 full marketplace\n\u2022 AI flooding owners with polished applicants \u2192 verified work history becomes the differentiator\n_Why: This is the north star that makes sense of every hiring decision made in Q4. Land it internally and externally._"
            }
        },
        {"type": "divider"},

        # Manan's Action Items
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f3af Your Action Items*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\U0001f6a8 *URGENT \u2014 JD Rules for Divij (Day 3 Overdue)*\nDivij is completely idle. Write and send the rules: 1 hire ~30d=vanilla; 2+ hires='multiple [role] positions available'; urgency \u22642wk='urgently hiring'. TBD: posted vs activated date + ASAP definition. Unblock him TODAY."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\U0001f6a8 *URGENT \u2014 2029 Vision One-Pager (Critical Overdue)*\nYou presented the vision today at company kickoff \u2014 the thesis is now public. John needs the one-pager. Fadi submitted his. You have not. Write it tonight or first thing tomorrow."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\U0001f6a8 *URGENT \u2014 Facebook API (Day 33 \u2014 Escalate now)*\nEscalation was on your Monday list. Did it happen? If not \u2014 do it tomorrow morning. IBK + Bob. Day 33 with no update since Oct 9 is unacceptable."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u26a0\ufe0f *Nihilus Decision \u2014 Nov 3 deadline = 7 days*\nIzzy to scope build cost. You\\'re leaning stay Q4, remove Q1. Decision must happen before renewal. Don\\'t let this slip to the wire."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u26a0\ufe0f *Spec Swarm TOMORROW (Oct 27)*\n\u2022 Sprint 26-23 verdicts all cleared by Manan \u2714\n\u2022 Tomorrow: layer 1 \u2192 layer 2 breakdown; no pre-presenting verdicts needed\n\u2022 Matan to bring QA Linear project with success criteria\n\u2022 Confirm: Spec Swarm N+1 decision \u2014 bring hiring count+speed in or wait N+2?"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u23f0 *Schedule recurring sprint kickoff*\nPing Jatin to get it on the calendar. After company-wide kickoff. Covers sprint close, carryover review, new work assignment."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u23f0 *Set up local testing env with Matan (next week)*\nWalk through Claude-assisted job state setup + Iterable/SendGrid sandbox. Matan is ready to go."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u23f0 *Pre-align with Matan + Skye before the GTM Lookahead N+1 tomorrow*\nMatan\\'s dynamics were flagged as a concern (research opacity, email rewrites without product input). Make sure you\\'ve had the Skye conversation."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u23f0 *Tag Fatty for Verify CTA designs (Magic Link)*\nIBK is building. The Verify button on success screen needs designs. Don\\'t let this block IBK\\'s ~1 week timeline."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\u23f0 *Indeed company field bug \u2014 draft + send support reply (5 days outstanding)*\nBob mitigated Oct 22. You\\'ve been owing Indeed a reply since then. Do it tomorrow."
            }
        },
        {"type": "divider"},

        # Team Action Items Worth Knowing
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f465 Team Action Items (watch these)*\n\u2022 *Jatin:* Reassign Carlo\\'s job-status-retrieval ticket (at risk of falling through); connect Bob on Q4 spikes; add layer 2 spec template to Linear; Google One API key ownership follow-up; ping Fadi + IBK on edge case design blocker\n\u2022 *Matan:* Kill 'Job post expired' + 'Job expiring in 3 days' emails; pause Command AI modal; investigate sign-in modal w/ Darren/Soumya/Steve; post billing email Q in #ask-billing-team; bring QA Linear project to swarm tomorrow\n\u2022 *Skye:* Write sprint expectations doc (first formal close this Friday)\n\u2022 *IBK:* Add comment on edge case ticket; continue Magic Link build"
            }
        },
        {"type": "divider"},

        # Watch List
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f6a8 Overdue / Watch List*\n\u2022 *JD Rules for Divij* \u2014 DAY 3 OVERDUE. Divij idle.\n\u2022 *2029 One-Pager* \u2014 CRITICAL. Vision now presented publicly. Write it.\n\u2022 *Facebook API* \u2014 Day 33. Escalate.\n\u2022 *Nihilus Decision* \u2014 Nov 3 = 7 days left.\n\u2022 *Carlo KT* \u2014 Paternity through mid-Feb. Knowledge risk is growing.\n\u2022 *Janneke HBA KT* \u2014 URGENT. Leave imminent.\n\u2022 *Matt McAllister intro* \u2014 New CMO, Week 2. Get 30 mins this week.\n\u2022 *Indeed XML feed* \u2014 Make private. Jatin is back \u2014 follow up.\n\u2022 *Entitlements rollout* \u2014 1% live today, 5% Wednesday. Monitor CS/billing noise.\n\u2022 *Matan dynamics* \u2014 Talk to Skye (research opacity, email rewrites without product input).\n\u2022 *Prompt chips min wage* \u2014 Write MD file + ping Justin.\n\u2022 *Gift cards owed* \u2014 Lola E. Erickson, Michele Landry, Ryan Reilly ($50 each).\n\u2022 *Match Explanation Workshop outputs* \u2014 Happened Oct 23 (evening). Capture the outputs.\n\u2022 *46 old experiments* \u2014 Manan + Fadi quick review."
            }
        },
        {"type": "divider"},

        # Tomorrow's Plan
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*\U0001f305 Tuesday Oct 27 Battle Plan*\n1\ufe0f\u20e3 Spec Swarm (layer 1 \u2192 layer 2 breakdown; verdicts cleared \u2714)\n2\ufe0f\u20e3 Matan GTM Lookahead N+1 \u2014 pre-align w/ Matan + Skye first\n3\ufe0f\u20e3 JD rules for Divij \u2014 write and send (Day 4 if you wait)\n4\ufe0f\u20e3 2029 one-pager \u2014 draft at minimum\n5\ufe0f\u20e3 Facebook API escalation \u2014 confirm it happened or do it\n6\ufe0f\u20e3 Tag Fatty for Magic Link Verify CTA\n7\ufe0f\u20e3 Schedule recurring sprint kickoff with Jatin"
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_You crushed Monday, Manan. Jatin\\'s back, sprint structure is locked, vision is out in the world. The team needed this kind of clarity and you delivered it. Now \u2014 unblock Divij, write the one-pager, and don\\'t let Facebook API drag into week 5. Tomorrow is a big swarm day. You\\'re ready. \U0001f4aa_"
            }
        }
    ]
    return blocks


def send_slack(token, blocks):
    payload = json.dumps({
        "channel": CHANNEL,
        "blocks": blocks,
        "text": "Monday Oct 26 Daily Debrief - Chief of Staff"
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": str(e)}


def preview(blocks):
    lines = []
    lines.append("=" * 70)
    lines.append("PREVIEW: Monday Oct 26, 2026 PDT Chief of Staff Digest")
    lines.append("=" * 70)
    for block in blocks:
        if block.get("type") == "header":
            lines.append(f"\n### {block['text']['text']} ###\n")
        elif block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            lines.append(text)
            lines.append("")
        elif block.get("type") == "divider":
            lines.append("-" * 70)
    sys.stdout.buffer.write("\n".join(lines).encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


def main():
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN")
    )
    blocks = build_blocks()

    if not token:
        print("[NO SLACK TOKEN] Printing preview only.\n")
        preview(blocks)
        print("\n[ACTION NEEDED] Add SLACK_TOKEN or SLACK_BOT_TOKEN to Cursor Dashboard > Cloud Agents > Secrets to enable live delivery.")
        return

    result = send_slack(token, blocks)
    if result.get("ok"):
        print(f"[OK] Digest sent to {CHANNEL}. ts={result.get('ts')}")
    else:
        print(f"[ERROR] Slack API error: {result.get('error')}")
        print("Falling back to preview:")
        preview(blocks)


if __name__ == "__main__":
    main()
