#!/usr/bin/env python3
"""Daily Decision Digest — Aug 26, 2026 (EOD Wed PDT)"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

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
            "text": "Chief of Staff Daily Digest — Wed Aug 26 :sparkles:",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "No new personally-captured meetings today — but there's plenty to unpack. Here's your full EOD brief."
            }
        ]
    },
    {"type": "divider"},

    # ── SECTION 1: Missed meeting from Aug 25 ─────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:clipboard: CATCH-UP: Product x Sales Hiring (Aug 25, 8am)*\n_Manan · Bobby Sladek · Jon Wanczyk · Sean Gohman · Zane Williams_\n\nThis one wasn't in yesterday's digest — here's what was locked:"
        }
    },
    {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "emoji", "name": "white_check_mark"},
                    {"type": "text", "text": " ", "style": {"bold": True}},
                    {"type": "text", "text": "Indeed messaging LOCKED", "style": {"bold": True}},
                    {"type": "text", "text": " — 3 core talking points for sales:\n"}
                ]
            },
            {
                "type": "rich_text_list",
                "style": "ordered",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": "Direct Indeed customers get 3 free posts/month — Homebase has no such cap"}]
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": "Reactivating old jobs avoids the 'same or similar job' sponsorship flag (copying triggers it)"}]
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": "Indeed now requires a corporate email — most small biz don't have one — Homebase is the safer on-ramp"}]
                    }
                ]
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "emoji", "name": "white_check_mark"},
                    {"type": "text", "text": " Volume objection REFRAMED", "style": {"bold": True}},
                    {"type": "text", "text": " — Don't promise 80 applicants. Sell 5-10 high-quality interviews you actually run, not 75 you throw away."}
                ]
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "emoji", "name": "white_check_mark"},
                    {"type": "text", "text": " Background checks = stealth sales hook", "style": {"bold": True}},
                    {"type": "text", "text": " — 5 free with subscription (vs $30-65/check elsewhere). Best for kids programs, dog boarding, tutoring. Pre-sell question locked: 'How many checks/month are you running and what are you paying?'"}
                ]
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "emoji", "name": "white_check_mark"},
                    {"type": "text", "text": " Careers page discoverability flagged", "style": {"bold": True}},
                    {"type": "text", "text": " — Share button buried under 3-dot menu. Almost no customer finds it. Surface QR code + copy link much more prominently — this is a product fix."}
                ]
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "emoji", "name": "white_check_mark"},
                    {"type": "text", "text": " Google crawling of careers pages coming in ~2 weeks", "style": {"bold": True}},
                    {"type": "text", "text": " — Jobs already rank; soon the full careers page will too, with all jobs nested. New SEO unlock."}
                ]
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:zap: Actions from Product x Sales Hiring:*\n:bust_in_silhouette: *You* — Design a careers page A/B test with Jon (does activation lift call conversion or paid rate?)\n:bust_in_silhouette: *Jon* — Surface applicant sourcing mix in Salesforce (flag accounts where Homebase sourced 25-30%+ of applicants)\n:bust_in_silhouette: *Bobby* — Log niche sales questions in team chat (start FAQ: 'How do our background checks compare to Checkr?')\n:bust_in_silhouette: *You + Jon* — Book a longer recurring Product x Sales block that includes Sean and doesn't get overwritten"
        }
    },
    {"type": "divider"},

    # ── SECTION 2: Customer interview insight ─────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mag: FRESH CUSTOMER INSIGHT: Lindsy Lockett Interview (Aug 26, 2:30pm)*\n_Workspace shared note (Matan + Lizzyshantelle) — talent agency owner, active Hiring Assistant user_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Funnel proof point that should be in your back pocket:* 192 applicants → 52 screeners → 14 matches. Screener transcripts are so valuable she uses them to *skip redundant interview questions entirely.* She consented to testimonial use. :trophy:\n\n*Product gaps she surfaced (for your roadmap radar):*\n• No 1099/contractor onboarding packet — she stopped using Hire button (defaults to W2)\n• No export of applicant activity log after job closes — she feeds this into her own AI system\n• No free-text notes field on the hiring to-do dashboard\n• Interviews shown out of chronological order\n• No deduplication — same candidate can apply twice, no alert"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: Your call on this:* None of these are blocking Q3 OKRs, but deduplication + interview ordering are quick wins that hit screener completion rate. Flag for Jatin or backlog for sprint 2619."
        }
    },
    {"type": "divider"},

    # ── SECTION 3: Tomorrow's agenda ──────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:alarm_clock: TOMORROW — Thu Aug 27*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":mega: *11:00 AM — Loco Boys Brewing (Mike + Bobby Sladek)*\n\nThis is a real customer on your radar — 46 views, only 4 applicants on their bartender role. They need help.\n\n*Your game plan:*\n• Lead with boost framing: <10 applicants = actively push Boost. Show the 50% boosted → healthy stat.\n• Bobby to email Mike about Careers tab before the call\n• Screener trial review — show the funnel data\n• Come with a specific recommendation, not just options"
        }
    },
    {"type": "divider"},

    # ── SECTION 4: Watch list ──────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: WATCH LIST — Top 6 Open Items (as of EOD Aug 26)*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*🔴 Indeed Feed: SUSPENDED*\nAll Homebase jobs off Indeed. Min 3-month review. Bob+Izzy on V1/V2 reposting comparison. Ray escalating to Saul/David/Fiona. *Did you draft the summary for Sky? Did you email David?*"
            },
            {
                "type": "mrkdwn",
                "text": "*🔴 422 Errors: Day 48*\n146 locations since Jul 9. Jatin on RCA. Possible overlap with Indeed feed. *Status from Jatin today?*"
            },
            {
                "type": "mrkdwn",
                "text": "*🟡 Sky: Week 1 Starts Now*\nShare Q3 narrative doc + Talent Pool bridge doc. Week 1 agenda: 422 status, Fadi all-in, Abby ownership, in-domain emails. Set tone early."
            },
            {
                "type": "mrkdwn",
                "text": "*🟡 Annual Cancel Policy*\nBobbi + others still telling customers they can cancel anytime — they cannot. *Did you post guidance in Hiring Leads?*"
            },
            {
                "type": "mrkdwn",
                "text": "*🟡 JD A/B Experiment (IBK)*\nRunning 2+ weeks. OVERDUE. Pull the signal — this is blocking roadmap calls."
            },
            {
                "type": "mrkdwn",
                "text": "*🟡 Fadi Designs*\nResume Insights 9+ days overdue. Talent Pool not even in Linear. Izzy is blocked. Nudge tomorrow if not resolved."
            }
        ]
    },
    {"type": "divider"},

    # ── FOOTER ─────────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Bottom line:* Lighter day on the calls, but high-value intel. The Product x Sales meeting alone is a goldmine for Indeed positioning going into a week where the feed is suspended. You're locked, loaded, and running the business like a pro. :muscle:\n\n_Your Chief of Staff — Auto-sent at 5pm PDT_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest — Wed Aug 26 :sparkles:",
    "blocks": blocks
}

def preview():
    msg = "\n===== SLACK DIGEST PREVIEW =====\n"
    msg += "To: D06E4QMHCNN\n"
    msg += "Date: Wed Aug 26, 2026 EOD\n\n"
    msg += "--- CATCH-UP: Product x Sales Hiring (Aug 25, 8am) ---\n"
    msg += "Decisions:\n"
    msg += "  [1] Indeed messaging LOCKED — 3 talking points for sales\n"
    msg += "  [2] Volume objection REFRAMED — 5-10 quality > 75 discards\n"
    msg += "  [3] Background checks = stealth sales hook\n"
    msg += "  [4] Careers page share button buried — product fix needed\n"
    msg += "  [5] Google crawling careers pages in ~2 weeks (SEO unlock)\n"
    msg += "Actions:\n"
    msg += "  -> You: Design careers page A/B test with Jon\n"
    msg += "  -> Jon: Surface sourcing mix in Salesforce\n"
    msg += "  -> Bobby: Log niche sales FAQ in team chat\n"
    msg += "  -> You+Jon: Book longer recurring Product x Sales block\n\n"
    msg += "--- FRESH CUSTOMER INSIGHT: Lindsy Lockett (Aug 26, 2:30pm) ---\n"
    msg += "  Funnel: 192 applicants -> 52 screeners -> 14 matches\n"
    msg += "  Gaps: 1099 onboarding, applicant export, notes field, ordering, dedup\n"
    msg += "  Testimonial consent: YES\n\n"
    msg += "--- TOMORROW Aug 27 ---\n"
    msg += "  11:00am: Loco Boys Brewing (Mike + Bobby)\n"
    msg += "  Lead with boost framing (<10 apps = push Boost)\n\n"
    msg += "--- WATCH LIST ---\n"
    msg += "  [RED] Indeed Feed: SUSPENDED (Day 1+)\n"
    msg += "  [RED] 422 Errors: Day 48, 146 locations\n"
    msg += "  [YLW] Sky: Week 1 - share narrative + talent pool docs\n"
    msg += "  [YLW] Annual cancel policy: Correct reps NOW\n"
    msg += "  [YLW] JD A/B (IBK): OVERDUE, pull signal\n"
    msg += "  [YLW] Fadi designs: 9+ days overdue, Izzy blocked\n"
    msg += "================================\n"
    sys.stdout.buffer.write(msg.encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()

if not TOKEN:
    print("[INFO] No SLACK_TOKEN found — printing preview only.")
    print("[INFO] Add SLACK_TOKEN/SLACK_BOT_TOKEN/SLACK_API_TOKEN in Cursor Dashboard > Cloud Agents > Secrets to enable live sends.")
    preview()
    sys.exit(0)

req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"[OK] Message sent successfully! ts={result.get('ts')}")
    else:
        print(f"[ERROR] Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"[ERROR] Network error: {e}")
    preview()
    sys.exit(1)
