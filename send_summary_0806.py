#!/usr/bin/env python3
"""Daily Chief of Staff digest for Manan Kothari - Aug 6, 2026 (Thu PDT)."""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
DATE_LABEL = "Thursday, August 6, 2026"

TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"Chief of Staff Daily Digest — {DATE_LABEL} 🗂️",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! Big day — you had *1 meeting* and made some really sharp product decisions. "
                "You were running the show today with data-backed conviction. Here's everything that mattered. 💪"
            ),
        },
    },
    {"type": "divider"},

    # ── MEETING ──────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Meeting Today*\n*Hiring Leads Standup* — 8:45 AM PDT\nWith: Fadi Rizk, Matan Chen Zion, Jatin Bhandari, Ray Sandza, Usman Zafar, Jon Wanczyk",
        },
    },
    {"type": "divider"},

    # ── DECISIONS ────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Decisions Made Today*",
        },
    },

    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. JD Prompt Box A/B Experiment — GREENLIT ✅*\n"
                ">*Decision:* Run a 50/50 A/B test that skips the prompt-box page entirely — drop users directly onto the job-details screen.\n"
                ">*Why:* 60% of users who land on the JD page do nothing. Of those who finish, ~⅓ just type 'cashier' to skip through, ~⅓ use prompt chips mainly as a pass-through, and only 5% paste a full JD. The real magic is page 2 — once users hit it, 80-90% complete the flow. Your hypothesis: the prompt box is the confusion point, not intent.\n"
                ">*Fadi's take:* Skeptical of the regression risk (blank form vs. AI-assist), but aligned on running the test first.\n"
                ">*Eng lift:* ~1 day. IBK has capacity. *Target: week of Aug 10.*"
            ),
        },
    },

    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. In-Product Abandonment Survey — LAUNCHING TODAY 🚀*\n"
                ">*Decision:* Matan to build a pop-up survey via Guides today (pending LCM approval). Trigger: user lands on the JD text-box page, then bounces. Options: 'can't upload my own JD,' 'this is confusing,' 'not hiring right now,' 'other (open text).'\n"
                ">*Why:* Before investing in the A/B test, get directional data on *why* people drop off — is it confusion, low intent, or a missing upload path? Survey gives you the 'why' cheaply and fast.\n"
                ">*Caveat:* Matan flagged ~95% ignore rate on nudges, so treat signal as directional, not statistically definitive."
            ),
        },
    },

    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Consolidated Hiring Roadmap — STRUCTURE LOCKED 🗺️*\n"
                ">*Decision:* One unified Google Sheet roadmap covering all hiring workstreams (product, PMM, sales). Matan to translate his PMM roadmap into the sheet by EOD today or within a week. Linear projects will be linked to each row for drill-down.\n"
                ">*Why:* Engineering team and leadership can now look at a single view across hiring and see what's in-flight, what's coming, and who owns what. Usman confirmed it gives him clarity on job security agent, B-turn off screener, and resume-mandatory work.\n"
                ">*Next:* Share with eng team once Matan's roadmap is added."
            ),
        },
    },

    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Q3 Four Focus Areas — FRAMEWORK LOCKED 🎯*\n"
                ">*Decision:* Explicitly scoped team investment to exactly four buckets:\n"
                ">• *Trial starts:* career page entry point, capture employers already on Indeed, get net-new FFH trials started.\n"
                ">• *Unblocking applicant flow:* job-not-reaching-Indeed is the #1 applicant blocker — identify and fix every reason.\n"
                ">• *Core light touches:* targeted product fixes (e.g., screener toggle with retained candidate profile).\n"
                ">• *Retention:* it's 85-90%, so minimal investment — don't over-index here.\n"
                ">*Why:* Explicitly deprioritizing retention investment frees up bandwidth for trial starts and applicant flow, which are the levers for 500 FFH paying customers and 70% healthy jobs."
            ),
        },
    },

    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. MBR Format Change — ACKNOWLEDGED ✅*\n"
                ">*Decision:* New MBR format is: (1) Are you hitting your goals? (2) What are you doing to address them? (3) What's blocking you? Old format was output-heavy 'show and tell' — easy to hide behind shipped work without hitting goals.\n"
                ">*Good news for you:* Hiring team was NOT flagged for a review — leadership is already in your meetings and knows the context.\n"
                ">*Jon Wanczyk's read:* 'Here's what we did, here's what we learned, here's what we're changing, here's our blockers' — the right format."
            ),
        },
    },

    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. JD Drop-off Root Cause — HYPOTHESIS CONFIRMED 📊*\n"
                ">*Decision:* Primary drop-off driver is the prompt box page, not the downstream flow. Data breakdown of users who *complete* job posting:\n"
                ">• ~33% type just a job title (e.g., 'cashier') to skip to page 2\n"
                ">• ~33% use prompt chips; half click through without modifying, then adjust on the JD itself\n"
                ">• ~5% paste a full JD (LLM extraction is broken — important bug to log)\n"
                ">• ~9% click 'start with your own job description'\n"
                ">*Implication:* People aren't confused by the JD editing experience. They're confused by/not motivated on the *first* page. The experiment will prove or disprove this cleanly."
            ),
        },
    },

    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Applicant-Count Survey — BUILDING TODAY 📋*\n"
                ">*Decision:* Manan building a survey (via Great Question) to ask OMs: how many applicants do you need before making a hiring decision?\n"
                ">*Why:* Current data shows OMs *are* making decisions at ~15 applicants, but doesn't tell you if that's desperation (too few) or satisfaction (enough). This survey distinguishes those two signals — critical for calibrating 'healthy job' thresholds and match quality targets.\n"
                ">*Next:* Send draft to team for review before launch."
            ),
        },
    },

    # Decision 8
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Amplitude Analytics Support for Matan — REDIRECTED ↩️*\n"
                ">*Decision:* You backed off offering to pull Amplitude CSV for Matan (users who started a job post but never posted). Redirected him to Rohit or Nelson — or to figure it out himself.\n"
                ">*Why:* You don't have capacity. The right call — Matan can extract the data himself or get a data resource. Don't let this become a blocker for the experiment."
            ),
        },
    },

    {"type": "divider"},

    # ── ACTION ITEMS ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚡ Your Action Items — Today & This Week*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "🔴 *TODAY (Aug 6):*\n"
                "• *Share Amplitude dashboard with Matan* — he needs it to extract users who started but never posted a job. Don't let this slip.\n"
                "• *Review Matan's abandonment survey pop-up* — he's building it today; you need to approve for LCM before it goes live.\n"
                "• *Send applicant-count survey draft to team* — get Fadi + Matan eyes on it before Great Question launch.\n"
                "• *Sync with Fadi on sprint timelines* — he flagged wanting a product sync on next few sprints. Schedule 30 min.\n\n"
                "🟡 *THIS WEEK (by Mon Aug 10):*\n"
                "• *Build roadmap-to-goals deck* — map ALL workstreams to 500 FFH paying customers + 70% FFH healthy jobs. Present Monday.\n"
                "• *Confirm Matan added PMM roadmap to the Google Sheet* — he committed to EOD today or within a week. Nudge him.\n"
                "• *Fadi + Page Templates* — he's getting conflicting info from two people. Help unblock or escalate who owns the canonical answer.\n"
                "• *Fadi Boost modal Figma* — this is now 10+ days overdue and Fadi is blocked on you. Send it TODAY.\n"
                "• *Dana succession* — she returns Aug 10, last day Aug 12. You have 2 working days. Page Templates hand-off must start NOW.\n"
                "• *Validate Meta ads feasibility with Jenna* — still open from last week.\n"
                "• *Set up SEO scoping session with Tatiana* — domain authority strategy is still open.\n"
                "• *Rami business case to Ted* — Ted is pulling back on DS involvement. Make the case directly this week.\n"
                "• *422 errors* — Day 27. Keep pressure on Jatin for RCA."
            ),
        },
    },

    {"type": "divider"},

    # ── WATCH LIST ───────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🚨 Watch List — Urgent*\n\n"
                "⏰ *Dana Succession — 6 DAYS LEFT (Aug 12 last day)*\n"
                "Dana OFF this week (Aug 3-8), returns Mon Aug 10 → only 2 working days remaining. "
                "No one owns the hand-off. This is the most urgent org risk right now.\n\n"
                "🔴 *422 Job Publishing Errors — Day 27*\n"
                "Jatin on RCA, Ray OUT, you are the decision-maker. Push for update today.\n\n"
                "🟡 *Fadi Boost Modal Figma — 10+ days overdue*\n"
                "Fadi is blocked on you. He reminded you indirectly today by mentioning page templates chaos. Unblock him.\n\n"
                "🟢 *Izzy Reactivate — should be on staging TODAY*\n"
                "Confirm with Izzy that the Aug 6 staging target was hit.\n\n"
                "🟢 *Carlo (Tap the Talent Pool) — Sprint started Aug 5*\n"
                "Carlo back and leading. Check in on post-job-creation flow progress."
            ),
        },
    },

    {"type": "divider"},

    # ── CLOSING ──────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*💬 Your CoS Take*\n\n"
                "You were operating at your best today, Manan — data-driven, decisive, and setting a clear direction for the team. "
                "The JD experiment is the right call: low lift, high learning, and you had the receipts to back it. "
                "Fadi's skepticism was healthy and you handled it perfectly — 'let's just run it and see.'\n\n"
                "The four-focus-area framing is exactly the kind of strategic clarity your team needs right now, "
                "especially with the org in transition. Locking down the consolidated roadmap is going to make Monday's deck much easier to build.\n\n"
                "The one thing I'd push you hard on: *Dana's last day is 6 days away.* "
                "Everything else can slip a day. That one cannot. 🎯"
            ),
        },
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Your Chief of Staff Daily Digest | Powered by Granola + Cursor Automation | Aug 6, 2026",
            }
        ],
    },
]

payload = {
    "channel": CHANNEL,
    "text": f"Chief of Staff Daily Digest — {DATE_LABEL}",
    "blocks": blocks,
}


def preview():
    sys.stdout.buffer.write(
        ("\n=== PREVIEW ===\n" + json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode(
            "utf-8", errors="replace"
        )
    )


def send():
    if not TOKEN:
        print("[WARN] No Slack token found — printing preview only.")
        preview()
        return

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Slack message sent successfully. ts={body.get('ts')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                preview()
    except urllib.error.URLError as exc:
        print(f"[ERROR] Network error: {exc}")
        preview()


if __name__ == "__main__":
    send()
