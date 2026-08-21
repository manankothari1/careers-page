#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Aug 20, 2026 (Wednesday PDT)
Manan Kothari, PM @ Homebase — Hiring/Applicant Flow
Slack channel: D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest — Wednesday Aug 20 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day today \u2014 a genuine leadership era ends and a new one begins. You navigated it with a lot of class. Here's everything that mattered today, crisp and clean."
        }
    },
    {"type": "divider"},

    # ─── MEETING 1 ───────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd Meeting 1 of 2 \u2014 Hiring Leads Standup* (8:45 AM PDT)\n_With: Ray Sandza \u00b7 Fadi Rizk \u00b7 Matan Chen Zion \u00b7 Jatin Bhandari \u00b7 Jon Wanczyk_"
        }
    },

    # Decisions
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decisions Made*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Ray Sandza's last day is today.* Jon Wanczyk ('J-Dubs') takes over as day-to-day Hiring Sales team lead through end of year.\n_Why it matters: Ray has high trust in this crew and pulled Jon back in because of prior history + positive team feedback. Ray's framing: '50-100% throughput improvement' is possible with clearer leadership and stronger sales partnership. This is a real transition, not a placeholder \u2014 Jon is playing a full-time role on contractor status. Sky starts next week, so this is your leadership structure heading into Q4._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Q3 Strategy Doc \u2014 shared live in Leads Slack channel.* You shared the in-progress doc (human-written, not AI) with Leads NOW. Structure: 'Where we are today / What we learned / What we're going to do about it.'\n_Why it matters: This doc becomes the canonical rallying point for the team's Q3 remainder. Getting it out early (imperfect) > waiting for perfect. Fadi explicitly praised the non-AI voice \u2014 the team is hungry for real thinking._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Soft deadline: team comments on Q3 doc by ~noon tomorrow (Aug 21).* Ray will hold off commenting until after the core 4 weigh in first.\n_Why it matters: Ray is being intentional not to crowd out opinions. This is your one shot to get unfiltered input from Fadi, Matan, Jatin before Sky arrives. Use it._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. #hiring-epdd Slack channel greenlit.* You asked, Ray said go, Jatin to create.\n_Why it matters: #hiring-team has ~50 members (too noisy). You need a tight engineering-product coordination space. This unblocks clean communication for the sprint._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Sean's daily updates \u2014 format changing to summary + thread.* Jon owns this change.\n_Why it matters: Novella-length updates in #hiring-team are killing engagement. One-liner + detail-in-thread = more eyes, more response, more signal. Jon has been asked explicitly._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Product-Sales partnership \u2014 explicitly committed on the record.* You, Ray, and Jon were on a call with sales reps this morning to announce the leadership change. Your joint promise: 'Product will understand what sales needs and will actively partner.' Ray has made this a core success metric.\n_Why it matters: This is now an external commitment, not just an internal one. Credibility on the line. Make sure Jon, Fadi, and Matan are all rowing the same direction here._"
        }
    },

    {"type": "divider"},

    # ─── MEETING 2 ───────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd Meeting 2 of 2 \u2014 Mike Mohrhardt + Bobby Sladek (Loco Boys Brewing) Sales Listen*\n_With: Bobby Sladek \u00b7 Mike (Loco Boys Brewing)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Decisions / Insights*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Boost recommendation threshold locked: < 5-10 applicants in first couple of days = proactively push boost.* Surfaced during Bobby's call with Mike.\n_Why it matters: You're building product intuitions directly from sales calls. This threshold should be codified in sales playbook and potentially surfaced in-product._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Homebase boost routes through Talroo, NOT Zip Recruiter.* Critical framing: 'We tap our own talent pool and optimize spend for you.' External explanation should say Jobget, not Talroo.\n_Why it matters: Reps (and possibly product copy) may be mislabeling this. Sean and Zane are likely unaware. Bobby sharing in Hiring Sales channel. You should validate this is consistent with product messaging._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. Dashboard 'views' = Homebase career page only, not Indeed/ZR.* This is a major customer confusion point.\n_Why it matters: Mike's 46 views are from Google SEO organic traffic \u2014 strong selling point ('we're getting your job found on Google for free'). But if customers think it includes Indeed views and it doesn't, that's a trust/churn risk. Worth flagging for PM review \u2014 is the dashboard label clear enough?_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. Never give customers a reason to go back to Indeed directly.* Framing locked: 'Indeed is expensive and getting harder to navigate; here's why you use us instead.'\n_Why it matters: This is competitive positioning directly relevant to your OTP/Indeed fraud recovery work. The more we reduce Indeed friction for customers while improving our value prop, the stickier they are._"
        }
    },

    {"type": "divider"},

    # ─── ACTION ITEMS ───────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af Today's Action Items (by Owner)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *YOU (Manan) \u2014 By Tomorrow Noon:*\n\u2022 Finish Q3 strategy doc and watch for comments from Fadi, Matan, Jatin by noon Aug 21\n\u2022 Prepare Sky onboarding context (you're writing the Talent Pool strategy doc \u2014 this feeds that)\n\u2022 Review Homebase product messaging on boost/Talroo/Jobget framing after Bobby's insights\n\u2022 Flag dashboard 'views' label as potential PM ticket (customer confusion risk surfaced today)\n\u2022 Connect with Jon Wanczyk to establish a working rhythm now that he's formally your sales partner"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *Jatin:*\n\u2022 Create #hiring-epdd Slack channel\n\u2022 Follow up with Susan (Identity) on step-up auth readiness + email OTP support (OTP flow LOCKED, this unblocks Indeed fraud recovery)\n\u2022 422 error RCA \u2014 Day 39+ as of today, 146 locations. Push for status update."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *Jon Wanczyk:*\n\u2022 Condense Sean's daily updates to summary + thread format (Manan asked explicitly today)\n\u2022 Begin formalizing his day-to-day role with the Hiring Sales team"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *Bobby Sladek:*\n\u2022 Email Mike (Loco Boys) to add a 'Careers' tab linking to his Homebase page\n\u2022 Share Talroo/views/Indeed competitive framing in Hiring Sales channel for Sean + Zane\n\u2022 Reconnect with Mike before 2pm next Thursday (Aug 27)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *Ray:*\n\u2022 Put together Sky onboarding (starts next week)\n\u2022 Review Q3 doc AFTER the core leads have commented (soft: by tomorrow noon)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u25b6\ufe0f *Fadi:*\n\u2022 Resume Insights designs \u2014 still overdue (since Aug 17). Unblock Manan ASAP.\n\u2022 Talent Pool designs \u2014 not in Linear yet. Izzy (front end) is blocked on you.\n\u2022 Comment on Q3 doc by noon Aug 21"
        }
    },

    {"type": "divider"},

    # ─── WATCH LIST ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 Watch List \u2014 Still Open, Still Hot*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Sky starts Monday Aug 25* \u2014 5 days. Talent Pool doc + onboarding context = your most important deliverable right now.\n\u2022 *New GM of Hiring* \u2014 If start was Aug 18, they started 2 days ago. Connect today.\n\u2022 *JD A/B experiment (IBK)* \u2014 Running since week of Aug 10. No signal reported. IBK flagged as too passive \u2014 pull data yourself if needed.\n\u2022 *Indeed OTP/fraud recovery* \u2014 OTP flow LOCKED (Aug 19). Jatin needs to close the Susan/step-up loop ASAP. This is how you get out of Indeed jail.\n\u2022 *Culinary Agents* \u2014 GO-LIVE was Aug 12. First data signal is OVERDUE. Chase Gray/Carlo.\n\u2022 *Carlo Ferrer* \u2014 Out again this week. Owns Talent Pool + Indeed 3LO. Jatin needs a contingency.\n\u2022 *Trial conversion deep dive* \u2014 Recalculate with L3 MoM average (not single-month data). Starter plan removal (May 29) = primary hypothesis. Don't share broadly yet.\n\u2022 *ICP nudge experiment* \u2014 Myan has results. Push for sharing.\n\u2022 *Charmina's scheduling spike* \u2014 Docs linked in Linear. Still nobody has reviewed them.\n\u2022 *Tanner Hartwig* \u2014 Behind on Indeed account setup. What's blocking?"
        }
    },

    {"type": "divider"},

    # ─── CLOSING ────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f9e0 Big Picture Check-In*\n\nManan \u2014 today was a watershed moment. Ray is officially out. Jon Wanczyk is running the sales side. Sky arrives in 5 days. You dropped a real, human-written strategy doc that the team is going to rally around. That's genuine leadership.\n\nYou're walking into next week with:\n\u2022 A new sales partner (Jon) who Ray trusts completely\n\u2022 A new Head of Product (Sky) who needs your context immediately\n\u2022 An OTP flow that's LOCKED and should finally get you out of Indeed jail\n\u2022 A Talent Pool direction that Fadi is passionate about and engineers are ready to build\n\nYour job right now: get the Q3 doc sharp by tomorrow noon, get the Talent Pool strategy doc ready for Sky's arrival, and make sure Jatin's 422 errors get resolved before this becomes a customer-facing crisis.\n\nYou've got this. Go rest. \U0001f4aa"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest \u2022 Aug 20, 2026 \u2022 2 meetings reviewed \u2022 10 decisions captured"
            }
        ]
    }
]


def preview():
    print("\n" + "="*70)
    print("SLACK DIGEST PREVIEW (no token \u2014 would send to D06E4QMHCNN)")
    print("="*70)
    for block in BLOCKS:
        btype = block.get("type", "")
        if btype == "header":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("\n### " + text + "\n").encode("utf-8", errors="replace"))
        elif btype == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif btype == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    print("="*70 + "\n")


def send_slack():
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN") or
        ""
    ).strip()

    if not token:
        preview()
        print("No Slack token found. Add SLACK_TOKEN or SLACK_BOT_TOKEN in Cursor Dashboard -> Cloud Agents -> Secrets.")
        return 0

    payload = {
        "channel": CHANNEL,
        "blocks": BLOCKS,
        "text": "Chief of Staff Daily Digest - Aug 20, 2026",
        "unfurl_links": False,
        "unfurl_media": False,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"Slack message sent successfully! ts={body.get('ts')}")
                return 0
            else:
                print(f"Slack API error: {body.get('error')}")
                preview()
                return 1
    except urllib.error.URLError as e:
        print(f"Network error sending to Slack: {e}")
        preview()
        return 1


if __name__ == "__main__":
    sys.exit(send_slack())
