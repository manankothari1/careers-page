#!/usr/bin/env python3
"""Daily digest - Oct 9 UTC (Oct 8 CEST workday) - Spain Day 7"""
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
            "text": "Chief of Staff Daily Digest \u2014 Thursday Oct 8 \U0001f1ea\U0001f1f8",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Good evening, Manan!* \U0001f31f Day 7 in Spain. Massive day \u2014 you shipped the Q4 sizing session you've been building to all week, AND got alignment on the Indeed duplicate strategy with Tiger. Day Grade: *A-*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f4ca *2 MEETINGS TODAY*\n1. Duplicate Job Posting Strategy w/ Tiger \u2014 4:34 PM CEST\n2. Q4 Sizing \u2014 Mandatory (Full Team) \u2014 9:00 PM CEST"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2694\ufe0f *MEETING 1: Duplicate Job Posting Strategy w/ Tiger* \u2014 4:34 PM CEST\n_Context: Only 8.5% of jobs have same-type duplicates open simultaneously (drops to ~4-4.5% with Extend). ~200 jobs currently affected. Indeed penalizes duplicates = fewer applicants._\n\n*Decision Made:*\n\u2022 Net-new job ID alone (\u201cOption A\u201d) does NOT fully solve the problem \u2014 especially in chained duplicate scenarios (Job 1\u21922\u21923\u21924 all linking forward while Job 3 is already flagged)\n\u2022 *Leaning toward Option B: front-end modal warning* \u2014 surface the duplicate, recommend archiving the old post, give OEM the choice\n\u2022 Extend work proceeds in parallel; duplicate job modal logic on hold pending design input\n\n*Rationale:* Asking OEMs 'how many do you want to hire?' won't prevent them from re-opening later. The modal is the only way to change behavior at the moment of creation."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2705 *Action Items from Meeting 1:*\n\u2022 \U0001F3AF *YOU:* Get Fadi's thoughts on the duplicate-warning modal design before Tiger's team builds anything\n\u2022 \U0001f7e1 *Tiger:* Add you and Matan to the Extend email notification thread (Iterable trigger coordination)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f3af *MEETING 2: Q4 Sizing \u2014 Mandatory* \u2014 9:00 PM CEST\n_Full team: Fadi, Carlo, Malcolm, Divij, Sina, Tiger, Bob, Izzy, Jatin, Gbolade_\n_Sizing scale: XS (hrs) | S (1-2 days) | M (~1 week) | L (1 sprint) | XL (1+ sprint / high unknowns)_\n\n*\U0001f3c6 BIG DECISIONS LOCKED:*\n\n\U0001f7e2 *Row 3 \u2014 Hiring Volume & Timeline Capture:*\n\u2022 Start with low-lift (dropdown/input in job details, sized *M*) in Q4\n\u2022 Defer multi-turn prompting agent to Q1 \u2014 use Q4 data to inform design\n\n\U0001f534 *Row 5 \u2014 Screener Toggle:* Sized *XL*\n\u2022 Massive downstream impacts: candidate profile, deal breaker decoupling, applicant link behavior\n\u2022 Key open question still unresolved: decouple screener from deal breakers?\n\n\U0001f7e1 *Row 6 \u2014 Match Explanation:* Sized *L*\n\u2022 Low-lift path: surface existing 0-1 competency scores in readable format for OEM\n\u2022 High-lift: full candidate profile rebuild (defer)\n\n\U0001f534 *Row 7 \u2014 Scheduling Reliability:* Sized *XL*\n\u2022 Spike in current sprint to diagnose root cause BEFORE any scoping\n\n\U0001f7e2 *Row 10 \u2014 JD Quality Score After OEM Edits:*\n\u2022 Real-time scoring too expensive; preferred = in-flow check (on 'Next' click)\n\u2022 Risk: platform-specific quality criteria may differ (Divij flagged)\n\n\U0001f7e1 *Row 11 \u2014 Wage Editing After Salary Reco:* Sized *S-M*\n\u2022 Must be editable within Ultraviolet-defined range only\n\u2022 *Blocked on Row 35 (Ultraviolet hookup) shipping first*\n\n\U0001f7e1 *Row 12 \u2014 Verify Postings Are Live:*\n\u2022 Solution: batched email with job links once platforms confirm live\n\u2022 ZipRecruiter links available; Indeed links only if OEM completed 3LO\n\n\U0001f7e1 *Row 13 \u2014 Candidate Table Filtering:* Sized *L*\n\u2022 Sort by action needed + status pills ('Needs Review', 'Interview Requested')\n\n\U0001f7e1 *Row 35 \u2014 Tips/Min Wage (Ultraviolet):* Sized *L*\n\u2022 ~25K rows; DB table preferred over API pipe\n\u2022 *Blocker: need to investigate how Ultraviolet is currently served (API vs data lake)*\n\n\U0001f7e1 *Row 38 \u2014 Job-Live Email to OEM:* Skipped for now\n\u2022 Frontend error validation shipped; Iterable workaround found\n\u2022 Manan to share workaround with Carlo separately\n\n\u26aa *Row 39 \u2014 Unified Comms View:* Tabled\n\u2022 Bob flagged unclear problem framing; Jatin to revisit with clearer spec\n\n\U0001f7e2 *Row 42 \u2014 Candidate Interview Confirmation:* Sized *M*\n\u2022 24hr reminder \u2192 confirm/decline \u2192 2hr follow-up \u2192 auto-cancel + notify OEM\n\n\U0001f7e2 *Row 43 \u2014 Hard Refresh for State Changes:* Sized *M*\n\nRow 44 \u2014 Pending Syndication Conflation: Sized *S* (may already be solved via Papertrail)\nRow 45 \u2014 BGC Count Monthly Reset: Sized *S* (cron, 30 days from subscription start)\n\n\U0001f7e1 *Row 48 \u2014 Below-Min-Wage Posting:* Front-end validation, *blocked on Row 35*\n\U0001f7e1 *Row 52 \u2014 Booking Link + Fixed Time Conflict:* Likely complex; many permutations\n\U0001f7e2 *Row 55 \u2014 Closed Job Survey (Hire Attribution):* Sized *M* \u2014 Tiger + Malcolm to spike\n\U0001f7e1 *Row 57 \u2014 BGC Refund When Candidate Skips:* Billing dependency flagged\n\U0001f7e2 *Row 58 \u2014 OTP Magic Link:* Sized *M* \u2014 IBK + you to implement, no design changes needed"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2705 *Action Items from Meeting 2:*\n\u2022 \U0001f525 *YOU [DO TONIGHT]:* Send continuation session calendar invite \u2014 Jatin travels tomorrow so schedule ASAP, cancel lower-priority meetings if needed\n\u2022 \U0001f525 *YOU [DO TONIGHT]:* Share Iterable workaround (Row 38) with Carlo \u2014 unblocks job-live email\n\u2022 \U0001f7e1 *YOU + Jatin:* Investigate how Ultraviolet data is currently served (API vs data lake) before committing to Row 35 approach\n\u2022 \U0001f7e1 *Bob + Carlo:* Confirm pending syndication timestamps exist in Papertrail/ActiveRecord (Row 44 may already be solved)\n\u2022 \U0001f7e1 *Team:* Spike resume-required support across partner job boards (Row 49) before scoping\n\u2022 \U0001f7e1 *YOU + Skye:* Break down Row 50 (enable applicants to type) before sizing \u2014 scope too broad\n\u2022 \U0001f7e1 *Tiger + Malcolm:* Spike closed-job survey (Row 55)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f6a8 *URGENT CARRY-OVERS & WATCH LIST*\n\n\U0001f534 *CARLO LEAVES OCT 14 \u2014 6 days.* Q4 sizing continuation session needs to happen BEFORE he goes. You need to send that invite TONIGHT. Also: Carlo KT still needed \u2014 did this happen today?\n\n\U0001f534 *INDEED FEED SUSPENDED \u2014 Day 47.* New negative email in hiring leads flagged yesterday (reposting logic per Skye). *Ping Jessica Kanaskie (jkanaskie@indeed.com) first thing tomorrow.*\n\n\U0001f534 *RACHEL Q4/Q1/Q2 UX VIEW \u2014 was due Oct 7.* Did this go out? Confirm with Rachel.\n\n\U0001f534 *3-YEAR VISION ONE-PAGER.* Board meeting ~Oct 15-22. You're in Spain. Draft is overdue NOW.\n\n\U0001f534 *FACEBOOK API \u2014 Day 16.* Bob + IBK leading. No update today.\n\n\U0001f7e1 *STACK RANK w/ SKYE.* Was supposed to happen today (Thu Oct 8). Did it? T-shirt sizing completed but was stack rank with Skye done first?\n\n\U0001f7e1 *MATAN + MANAN 1:1.* Was scheduled Thu Oct 8. Did it happen?\n\n\U0001f7e1 *NYLAS SPIKE.* Soheil leads. Jatin to schedule 30-min feasibility. Any update?\n\n\U0001f7e1 *SCREENER TOGGLE DECOUPLING.* Confirmed XL today. Manan + Divij spike next sprint.\n\n\U0001f7e1 *OMNI ACCESS \u2014 PAST DUE.* Looker went dark Oct 2. Verify IT ticket.\n\n\U0001f7e1 *GIFT CARDS OWED:* Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50).\n\n\U0001f7e1 *EMAILS UNSENT:* John Waldman (EarnBetter NDA + docs), Marina/Mundo Academy (26 days late).\n\n\U0001f7e1 *ITERABLE 6 EMAILS NOT FIRING.* Carlo fixing. EOW Oct 10. Verify Monday."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f3c6 *TODAY'S WINS*\n\u2022 Q4 sizing session DONE \u2014 this was the hardest logistical lift of the week. You now have a full t-shirt sized backlog across product, eng, DS, and design.\n\u2022 Screener toggle = XL confirmed \u2014 this was always going to be expensive, good to have it locked before sprint planning.\n\u2022 Ultraviolet/min-wage dependency chain now explicit: Row 35 \u2192 Row 11 \u2192 Row 48. Clean sequencing.\n\u2022 OTP Magic Link sized M with no design changes \u2014 clear path for IBK next sprint.\n\u2022 Duplicate job strategy direction set with Tiger \u2014 modal approach, pending Fadi."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f3af *YOUR TOP 3 ACTIONS FOR TOMORROW (FRI OCT 9)*\n1. \U0001f525 *Send continuation sizing session invite TONIGHT* (Jatin travels tomorrow)\n2. \U0001f525 *Share Iterable Row 38 workaround with Carlo* (unblocks him before Oct 14)\n3. \U0001f525 *Ping Jessica Kanaskie about Indeed* (Day 47, critical)\n\n_\U0001F9E0 You're running a tight ship from Spain, Manan. The Q4 sizing is done \u2014 now it's about velocity on the continuation and getting Carlo's knowledge out of his head before Oct 14. Rest tonight, strong finish tomorrow. \U0001F1EA\U0001F1F8\u2615_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest \u2014 Thu Oct 8 (Day 7 in Spain) \U0001f3af Q4 Sizing Done + Indeed Duplicate Strategy",
    "blocks": blocks
}

def send_slack(token: str) -> None:
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
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if not result.get("ok"):
        raise RuntimeError(f"Slack API error: {result.get('error')}")
    print(f"Sent successfully! ts={result.get('ts')}")

def preview() -> None:
    print("=" * 72)
    print("SLACK MESSAGE PREVIEW (no token found)")
    print("=" * 72)
    for b in blocks:
        if b["type"] == "header":
            sys.stdout.buffer.write(("\n### " + b["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif b["type"] == "section":
            sys.stdout.buffer.write((b["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif b["type"] == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    print("=" * 72)

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
).strip()

if token:
    try:
        send_slack(token)
    except Exception as e:
        print(f"ERROR sending: {e}")
        preview()
else:
    preview()
