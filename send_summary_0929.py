#!/usr/bin/env python3
"""Daily digest for Manan Kothari - Sep 29, 2026 (PDT)"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest - Tuesday Sep 29 \ud83d\udcca",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "3 meetings captured | *Day 37 of Indeed suspension* | *6 days* until Spain | *OKR draft DUE TODAY*"
            }
        ]
    },
    {"type": "divider"},

    # ── TODAY'S SCORECARD ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83c\udf1f Day Grade: A- \u2014 EXECUTION ACCELERATES*\n\nBig day, Manan. You locked the job-posting expiry + duplicate-detection architecture, got alignment across Fadi / Malcolm / Tiger / Gbolade on the spike plan, and handled a solid customer call with Penny. The one ding: OKR draft isn\'t submitted yet and the clock is ticking. You\'ve got the substance \u2014 now close the loop."
        }
    },
    {"type": "divider"},

    # ── MEETINGS TODAY ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\uddd3 Meetings Today (3)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "11:30am \u2014 <https://notes.granola.ai/d/8cef4f0f-d856-4bb6-b62d-4a290a221014|Penny M. Weide \u00d7 Manan> (Hannibal Dental Group)\n12:30pm \u2014 <https://notes.granola.ai/d/88be2b1f-0d3d-45a5-bc24-002e361973bb|Fadi \u00d7 Manan Prep>\n1:00pm \u2014 <https://notes.granola.ai/d/8b82a810-5f99-48bc-bc3c-23b529239d49|Job Posting Walkthrough> (Fadi, Malcolm, Tiger, Gbolade)"
        }
    },
    {"type": "divider"},

    # ── KEY DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 Key Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Job Posting Expiry: 30-day default, extend = +1 calendar month from expiry date*\n_Rationale:_ Cleaner for OEMs who don\'t understand 'activated date.' Extend is framed as 'extend by a month' (not 30 days) to avoid confusion. Always show year in tooltip copy (e.g., 'January 2nd, 2027') for December edge cases. Expiry calculated from *post date*, not activated date."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Duplicate Detection: 21-day threshold, exact string match, check after JD page*\n_Rationale:_ Role + location = matching keys. Under 21 days \u2192 edit existing job (same Indeed post ID). Over 21 days \u2192 new job ID. Fuzzy matching via Anthropic API ruled out \u2014 too slow at runtime. Exact string match on posted role title is the right check point (after job description page, before screener). Prompt box not reliable (stores initial input, not final role)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Shipping Strategy: Close flow ships independently of Indeed duplicate work*\n_Rationale:_ Two separate workstreams. Close + interview cancel + source-of-hire question can go live now. Extension piece also shippable if expiry date update + same Indeed post ID is confirmed. Duplicate detection must come first to avoid re-triggering the Indeed feed flag \u2014 don\'t let the carts get ahead of the horse."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Extend button replaces Boost at Day 27 (warning state turns orange)*\n_Rationale:_ UX signal to the OEM that their job is expiring. Extend tooltip shows what it does, confirms, then displays updated expiry. Intuitive and non-alarming."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Q4: Talent Pool deprioritized this quarter*\n_Rationale:_ Jan\'s OKR walkthrough didn\'t land \u2014 she questioned intake need, OEM poaching legalities. You and Fadi are frustrated but aligned: foundational work must come first. This is the right call even if it stings."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Pricing \u2192 root cause of unhealthy trials (non-FPH)*\n_Rationale:_ Non-FPH users hire spiky/seasonally, not year-round \u2014 they can\'t justify the cost. FPH hiring is steady. Action: filter $30 plan subscribers out of health metric numerator. This matters for how you frame your Q4 healthy-trial OKR."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Simple AI call Thursday \u2014 Manan not attending; Penny sends questions in advance*\n_Rationale:_ You\'re staying heads-down with Spain 6 days away and OKRs/Indeed Easy Apply due. Penny\'s a reliable filter."
        }
    },
    {"type": "divider"},

    # ── YOUR ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe5 YOUR Action Items (Manan)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u26a0\ufe0f *DUE TODAY: Submit OKR draft (EOD Sep 29)*\n\u2022 Confirmed in prep call with Fadi. The draft is alive in your head \u2014 get it on paper and submitted."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u26a0\ufe0f *DUE TOMORROW: Indeed Easy Apply PDF (Sep 30)*\n\u2022 This was on the watch list as of yesterday. Draft and submit before EOD tomorrow. No extensions on this one."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u26a0\ufe0f *DUE OCT 2 (3 days): Omni access request*\n\u2022 Looker goes dark Oct 2. File IT help desk ticket NOW if not done. You\'re leaving for Spain same day."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Update Linear ticket with today\'s job posting flow changes*\n\u2022 Notes from both the prep call and the team walkthrough need to be captured in Linear. Do this before sleep."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Send Granola notes to Fadi* (from prep call)\n\u2022 Committed in the meeting. Quick send."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Send Lola E. Erickson $50 gift card*\n\u2022 Promised on Sep 28 call. lola.e.erickson@gmail.com. Under 5 minutes. Do it."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Reply to John Waldman on EarnBetter (scope clarification + paid CPC test proposal)*\n\u2022 $0.07-0.10 CPC, ~100 jobs, $2K budget. This has been on the list since yesterday."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Send Matan job title/salary data*\n\u2022 He texted Sep 24. You already pulled it. Just send it."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Q4 planning session \u2014 today is your last window (Sep 29-30)*\n\u2022 Assign KR owners + map work sequences with Skye. Spain is in 6 days. Don\'t leave without this done."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *Introduce yourself to Matt McAllister (new CMO)*\n\u2022 Day 2 for him. Yelp SMB background = directly relevant to your work. Quick Slack/email intro = fast win."
        }
    },
    {"type": "divider"},

    # ── TEAM ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe6 Team Action Items (follow up to confirm)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Tiger* \u2014 Sync with Malcolm + IBK to divide spike work. Parallel spikes: exact string match timing + post-close attribution. Pull in Bob for Reactivate backend context.\n\u2022 *Fadi* \u2014 Deploy updated prototype to Vercel, link to Linear. Share job scope design doc with the team.\n\u2022 *Gbolade / Team* \u2014 Investigate + fix duplicate email firing (confirmed firing 4+ times; not Homebase-side).\n\u2022 *Team* \u2014 Fix missing candidate notifications in employee-linked flows. Create ticket for consistent custom source name rollout.\n\u2022 *Penny* \u2014 Send Manan questions ahead of Simple AI call Thursday."
        }
    },
    {"type": "divider"},

    # ── CRITICAL WATCH LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udea8 Critical Watch List (ongoing)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\ud83d\udd34 *INDEED FEED: SUSPENDED \u2014 Day 37.* Fraud package with Jessica Kanaskie. 2-3 week review window. No new action until she responds.\n\ud83d\udd34 *FACEBOOK API: FAILING \u2014 Day 6.* Meta developer checkup expired. Bob + IBK leading. Confirm status update today.\n\ud83d\udfe0 *Carlo KT starts THIS WEEK* \u2014 paternity Oct\u2013Feb. Biggest knowledge risk. Block time today.\n\ud83d\udfe0 *EarnIn NDA \u2014 not signed.* Prerequisite before any data exchange. Execute before Spain.\n\ud83d\udfe0 *3-year vision one-pager \u2014 due ~Oct 15-22 (board).* You leave Oct 2. First draft must exist before Spain.\n\ud83d\udfe0 *Comms Assistant \u2014 production decision OVERDUE.* Malcolm out Nov\u2013Dec. Decide before Q4 planning.\n\ud83d\udfe1 *HBA blocker status* \u2014 Skye + Lauren security screening was Sep 28. Follow up on outcome with Ankit.\n\ud83d\udfe1 *OTP ~18 companies impacted* by page-1 enrollment bug. Spot-check + outreach to any with draft jobs."
        }
    },
    {"type": "divider"},

    # ── TOMORROW ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd2e Tomorrow (Wed Sep 30) \u2014 Set Yourself Up*\n\u2022 Submit Indeed Easy Apply PDF (HARD DEADLINE)\n\u2022 Run Q4 planning session with Skye (last chance before Spain)\n\u2022 Brief Divij + Ted + Sina on Q4 roadmap\n\u2022 Kick off Job Posting Spike channel (JW back from OOO today)\n\u2022 Confirm Carlo KT is booked\n\u2022 Confirm Omni access request filed"
        }
    },
    {"type": "divider"},

    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You shipped real architecture clarity today, Manan \u2014 the job posting spike has a real plan now and the team knows who\'s doing what. The expiry/extend/close design is clean and principled. Six days to Spain and you\'re building the right things. OKR draft tonight, then tomorrow is all execution. Let\'s go. \ud83d\ude80"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Generated by your Chief of Staff \u2022 Granola \u00d7 Cursor Automation \u2022 Sep 29, 2026 5:00 PM PDT"
            }
        ]
    }
]

payload = {"channel": CHANNEL, "blocks": blocks, "unfurl_links": False}

def preview():
    sys.stdout.buffer.write(b"\n=== SLACK DIGEST PREVIEW (no token) ===\n")
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n" + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n")

if not TOKEN:
    print("[INFO] No SLACK_TOKEN found - printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    if body.get("ok"):
        print(f"[OK] Slack message sent to {CHANNEL}. ts={body.get('ts')}")
    else:
        print(f"[ERROR] Slack API error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error: {e}")
    preview()
    sys.exit(1)
