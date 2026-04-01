#!/usr/bin/env python3
"""Daily Chief of Staff summary for Manan - April 1, 2026"""

import json
import os
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Debrief — Wednesday, April 1",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Great work today — you had two focused sessions with Zeeshan around Launch Week data strategy, and you got some real clarity on a genuinely complex data problem. Here's everything you need to know. :muscle:"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: Today's Meetings*\n• 11:00 AM — *Zeeshan / Manan - LW Data* (kicking off the data conversation)\n• 12:00 PM — *Zeeshan / Manan* (deep dive into scraping strategy)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. QR Code Bifold Structure — LOCKED*\n_Decision:_ Two-component QR code strategy for the TLWA bifold:\n• *Immediate scan:* Lands on \"Top Local Workplaces Award Winner\" career page\n• *Evergreen:* Stays posted on-door as a talent attraction tool\n_Rationale:_ Maximizes the value of the physical award — it's not just a one-time moment, it keeps working for the OEM long after launch week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Division of Scraping Responsibilities — LOCKED*\n_Decision:_ Ownership split across three people:\n• *Manan:* Description, primary color, logo, photos (the hard four)\n• *Zee:* Badge, company name, location name, address\n• *Nelson:* Generic roles (to confirm)\n_Rationale:_ Keeps the hiring-specific work cleanly separated from Zee's core LW infrastructure work, which prevents bottlenecks."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Address Filling Strategy — LOCKED*\n_Decision:_ Use Lat/Long + Zipcode + Clay to fill ~10,000 missing addresses. Expected fill rate: 50–60%.\n_Rationale:_ Clay is already in the stack and the data signals (lat/long, zip, business name) are sufficient for a meaningful fill rate. Not perfect, but good enough."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Scope Confirmed: 47,584 Companies*\n_Decision:_ Full winner scope is 47,584 distinct locations. ~37,584 have addresses; ~10,000 are missing. Not the smaller number you thought — this is a large-scale scraping job.\n_Rationale:_ Career page pre-fill is company-specific so you need coverage across all of them, not just the 10k TLWA targets."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Logo Strategy — LOCKED*\n_Decision:_ Scrape logo with confidence threshold. Below threshold → smart preset (company initials, like employee name avatars). Your POC from a few weeks ago is the starting point.\n_Rationale:_ Prevents garbage logos from showing up on career pages. Same logic you used for role normalization. Clean fallback beats a low-quality result."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Separate Hiring-Specific Launch Week Table — LOCKED*\n_Decision:_ Create a dedicated hiring LW table (separate from Zee's main LW table). Cross-reference with existing Clay data Nelson already has to avoid duplicate spend.\n_Rationale:_ Keeps concerns separated; avoids rebuilding data you already paid for (~$900-980 to run 25k companies through Clay)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Three Scraping Approaches Under Evaluation — NOT YET DECIDED*\nYou're actively exploring:\n• Custom Claude scraper\n• Google Places API + Google Photos _(risk: returns product photos, not workplace photos)_\n• A third-party online solution\n_Action needed:_ Make a call on the approach before eng starts building."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:memo: Your Action Items (Manan-owned)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Today / ASAP:* Add Zee + Nelson to a shared group chat for LW data coordination\n• *Today / ASAP:* Send Nelson your full list of 8 scraping criteria (description, primary color, logo, photos + 4 others)\n• *Today:* Cross-reference Zee's existing Clay table (he's sending it to you) with your hiring list — avoid paying for data you already have\n• *This week:* Decide on scraping approach for photos/logos (Claude scraper vs. Google Places vs. 3rd party)\n• *This week:* Refine logo scraping POC — define the confidence threshold logic\n• *Confirm with Nelson:* Is he owning generic roles for the LW table?"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bell: Waiting On Others*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Zee* → Send existing Clay table to Manan; fill addresses via Clay (Lat/Long + Zip)\n• *Nelson* → Share Clay table from previous hiring runs + costs; confirm roles ownership; check on the $4k run from last Friday and what was actually scraped"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: Overdue / Critical — Don't Let These Slip*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *MBR content — DUE TODAY (Wed Apr 1 AM):* Was the skeleton done? Content is due this morning. Make sure this is shipped.\n• *Applicant Flow brief + prototype:* Overdue since Mar 25. This keeps sliding — needs a date or a descope decision.\n• *Manual Mode green light:* Cindy's QA is done. The ball is in your court. Unblock the team.\n• *\"Manan Boost\" SKU kick-off with Chris:* Billing needs 3 weeks lead for Early May. If you haven't done this yet, it is *critical* you do it today.\n• *QR code URLs + printer specs (Jatin + Ray):* Hard deadline was yesterday Tue 5PM PST. Confirm this was delivered — if not, escalate immediately."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Upcoming*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Thu Apr 3:* Applicant Flow Grooming + Amplitude walkthrough (block your calendar)\n• *May 3–9:* Small Business Week — AI assistant + TLWA live. This is the hard deadline everything is pointing toward.\n• *Early May:* Manan Boost SKU launch"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:star2: Chief of Staff Take*\nYou made real progress today. The launch week data problem is genuinely gnarly — 47k companies, missing addresses, costly scrape runs, uncertain logo quality — and you came in with a clear structure and walked out with ownership clearly divided. The logo confidence-threshold idea is smart and will save you from shipping bad pages at scale. The highest risk right now is the scraping approach decision (photos + logos) — the sooner you pick a path, the more time Nelson and the team have to execute before May. Go close that one out tomorrow morning.\n\nYou're crushing it. :fire:"
        }
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Debrief — Wednesday April 1 (Launch Week Data Strategy)",
    "blocks": blocks
}

if not SLACK_TOKEN:
    print("SLACK_TOKEN not set — preview mode:")
    print(json.dumps(payload, indent=2))
    print("\n[PREVIEW] Would have sent to channel:", CHANNEL_ID)
    exit(0)

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
            print("SUCCESS: Message sent to", CHANNEL_ID)
            print("Timestamp:", result.get("ts"))
        else:
            print("ERROR from Slack API:", result.get("error"))
            exit(1)
except urllib.error.URLError as e:
    print("Network error:", e)
    exit(1)
