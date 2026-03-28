#!/usr/bin/env python3
"""Build and send weekly chief-of-staff summary to Manan via Slack."""
import json, os, sys, urllib.request, urllib.error

CHANNEL_ID = "D06E4QMHCNN"
SLACK_API_URL = "https://slack.com/api/chat.postMessage"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff: Week-in-Review + Monday Prep  |  Fri Mar 28"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Today was All-Hands + Malcolm's 2,500 milestone — a well-earned celebration day. No recorded calls today, so here is your full *week-in-review* and *Monday hackathon launch checklist*. You made a ton of great calls this week — let's make sure none of it slips."
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Decisions Made This Week"}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. TLWA QR Flow: Option C Confirmed* (Mar 25)\n*Decision:* 4-step activation — Scan -> Pre-activation reveal -> Activate -> Next steps\n*Why:* Cleanest story arc, concierge-first path drives conversion, self-serve fallback for DIYers. Keeps sales involved without blocking activation.\n*Actions:*\n• Fadi + Manan — define smart defaults (photos, logo, brand color, generic job post) before Mon\n• Jatin + Ray — QR URL routing + printer specs were due today — confirm locked\n• Fadi — run marketing/copywriting meeting for insert content"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Phone/SMS Auth (not email) for TLWA QR* (Mar 25)\n*Decision:* Phone number + SMS verification to prevent QR code hijacking\n*Why:* Email auth leaves the door open for someone else to claim a sticker. Phone + location matching is airtight. Printer can match QR to address for pennies.\n*Actions:*\n• Jatin — ensure auth flow is part of URL routing spec"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Generic Team Member Job Post as TLWA Default* (Mar 25)\n*Decision:* Always-on generic role with 2032 expiry, auto-scheduling OFF, standard screener questions\n*Why:* Eliminates empty state problem. No excuse not to display the sticker. Flagged in DB for differentiated treatment later.\n*Actions:*\n• Manan — confirm DB flag spec with eng; confirm Kvan owns TLW badge display"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Build TLWA Outside HB1* (Mar 25)\n*Decision:* Build outside main HB1 codebase for faster shipping, enables Fadi code contributions\n*Why:* 6-week timeline with preference for 3-4 week completion. Faster iteration > codebase cleanliness at this stage.\n*Actions:*\n• Manan — ensure repo/deployment setup is handed to eng team Mon"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Smart PreSets: 4-Tier Framework + Logo as MVP Element* (Mar 25)\n*Decision:* Tiered personalization (zero info -> category -> specific business type -> full scrape). Logo is the highest-ROI MVP element.\n*Why:* Logo = strong \"this is MY page\" moment. Less risky than images (wrong photo = bad reaction), more impactful than descriptions. Smart placeholder UX (dotted-line Dropbox pattern) drives editing behavior.\n*Actions:*\n• Manan + Jeff — define preset specs for all 4 tiers Monday\n• Fadi — design post-QR scan UX flow\n• Manan — integrate logo scraping tool (currently local) with Supabase this sprint\n• Dana + Ray — in-person QR prototype field testing (confirm scheduled)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Hackathon Sprint: Mon Mar 30, 2 Weeks, 4 Projects* (Mar 24)\n*Decision:* Full team on applicant flow hackathon. 4 projects, minimal design needs each, parallel execution.\n*Why:* Current team has too many parallel tracks. Focus = faster outcomes. No new core features — finish what is in progress.\n*Actions:*\n• Manan — share brief/one-pagers for all 4 projects at kick-off Monday (your #1 priority Sunday)\n• Jeff — begin design on Indeed OAuth + Boost with Indeed\n• Matan — own zero-state + public workplace features\n• Cindy — trial flow improvements"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Indeed OAuth: Two Entry Points, Design-First* (Mar 24)\n*Decision:* Two OAuth flows — (a) View Live Job Posts, (b) Boost with Indeed. Build order: Design -> Build -> Indeed Review -> Launch.\n*Why:* Stopgap while 4-month Sponsored Jobs API is in flight. Gets OEMs authenticated and driving value fast. Up to 5 redirect URIs lets you distinguish entry points cleanly.\n*Actions:*\n• Andrew — 3LO spike review overdue — ping him Monday\n• Manan — email Kenneth + add Ray to Indeed thread (still open)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Homebase Boost via Tellru: $30-$50 SKU* (Mar 24)\n*Decision:* Create purchasable boost using Tellru ($1.70/application vs $13 on ZipRecruiter). Eat cost per new customer to drive acquisition.\n*Why:* Target customers spend $1,200-$20k/year on Indeed. Offering a high-ROI cheap alternative is a wedge. Positions Homebase as the smarter spend.\n*Actions:*\n• Manan + Jeff — design boost purchasing flow + packaging as a hackathon project"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. JobGet Integration: Organic XML Feed First* (Mar 24)\n*Decision:* Start with organic XML feed (30-40 min setup), Easy Apply next, sponsored later\n*Why:* Indeed cutting organic for multiple partners (3rd this week!). Diversification is urgent. JobGet + Snag a Job + 150-200 publisher network = immediate coverage.\n*Actions:*\n• Billy Lan (JobGet) — sending XML + Easy Apply docs; follow up if not received by Monday\n• Jatin — own technical implementation during hackathon"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. 6-Week Team Operating Mode: Finish Before Starting New* (Mar 23)\n*Decision:* No new core features. Finish in-progress work only. Treat customer incidents with urgency. Hackathon mindset for applicant flow.\n*Why:* Team has too many parallel tracks. Focus = faster outcomes. Ray owns Friday deck, Nelson tracking metrics.\n*Actions:*\n• Ray — took over Friday deck and presentation (confirm delivered today)\n• Jatin + Martin — sprint calendar alignment (confirm resolved)"
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Overdue / Critical — Do Not Let These Slip"}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *Manan Boost SKU kick-off with Chris* — billing needs 3-week lead for Early May. Every day you wait shrinks the runway. Book it Monday.\n:red_circle: *Manual Mode green light* — Cindy's QA is done. Ball is in your court.\n:large_yellow_circle: *Andrew 3LO spike review* — overdue. Ping Monday AM.\n:large_yellow_circle: *Email Kenneth + add Ray* to Indeed thread — still open.\n:large_yellow_circle: *Applicant flow brief + prototype* — confirm finalized for Monday kick-off.\n:large_yellow_circle: *All 4 hackathon brief docs* — kick-off is Monday. Sunday is your window."
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Monday Hackathon Kick-off Checklist"}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• [ ] 4 project briefs/one-pagers ready to share with full team\n• [ ] Manan Boost SKU — book time with Chris first thing\n• [ ] Ping Andrew on 3LO spike\n• [ ] Email Kenneth + add Ray to Indeed thread\n• [ ] Confirm TLWA URL routing + printer specs are locked (Jatin/Ray)\n• [ ] Fadi sync on smart defaults for careers page\n• [ ] Confirm JobGet docs received from Billy Lan\n• [ ] Manual Mode — give green light to ship\n• [ ] Add Supabase integration for logo scraping tool to sprint list"
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "North Stars — Where You Stand"}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Paying companies: ~600 vs 2,600 target (H1)\nWeekly trials: 112 vs ~1,000 target\nMonthly retention: 87% vs 95% target\n\nThe hackathon is your biggest lever right now. Applicant flow + job distribution diversification (JobGet, Tellru, Indeed OAuth) = your trial growth engine. You are building something special. Have a great weekend — you earned it."
        }
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Summary | Fri Mar 28, 2026 | Based on meetings Mon Mar 23 - Wed Mar 25 | Next update: Mon Mar 30 EOD"
            }
        ]
    }
]

payload_dict = {
    "text": "Chief of Staff: Week-in-Review + Monday Hackathon Prep | Fri Mar 28",
    "blocks": blocks
}

token = os.environ.get("SLACK_TOKEN", "")
if not token:
    print("SLACK_TOKEN not set — preview mode")
    print(json.dumps(payload_dict, indent=2)[:800])
    print("...")
    print(f"[Would send to channel: {CHANNEL_ID}]")
    sys.exit(0)

data = json.dumps({
    "channel": CHANNEL_ID,
    "text": payload_dict["text"],
    "blocks": blocks,
    "unfurl_links": False,
    "unfurl_media": False,
}).encode("utf-8")

req = urllib.request.Request(
    SLACK_API_URL,
    data=data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"SUCCESS: Message sent to {CHANNEL_ID}. ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        print(json.dumps(result, indent=2))
        sys.exit(1)
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} {e.reason}")
    print(e.read().decode())
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
