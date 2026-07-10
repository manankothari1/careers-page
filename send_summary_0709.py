#!/usr/bin/env python3
"""Daily digest for Manan Kothari - Jul 9, 2026 (PDT)"""
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
            "text": "🧠 Chief of Staff Daily Digest — Thursday, Jul 9"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Big day, Manan. Three meetings, one major theme: *V1→V2 migration is real, the clock is ticking, and customers are confused.* Here's everything you decided today and what needs to happen next."
        }
    },
    {"type": "divider"},

    # ── MEETING 1: HIRING LEADS STANDUP ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 8:45am — Hiring Leads Standup*\n_Ray, Fadi, Dana, Matan, Jatin, Nelson, Jeff, Usman_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "1. *V1→V2 cutover locked: July 20th morning* — Plan is in place with Gana, Ugo, and IBK. No more V1 jobs by then; only 123 locations still have a live job and all will be expired before the cutover. Clean slate.\n"
                "2. *No customer migrates with an active job* — All remaining active V1 jobs expire by July 20, so migrants land in V2 without a live job. Tour triggers off a location ID list (not an Amplitude event).\n"
                "3. *Two separate comms tracks needed before July 20* — (a) Customers still in trial: clarify it's not a paywall ('this is a preview of the paid tier; you go back to free posting after'). (b) Newly migrated customers with no trial: confirm they haven't lost anything. This is urgent.\n"
                "4. *Tour language already updated* — Already says 'this is free, you didn't lose anything, your candidates are still here.' Good. Now make sure the pre-migration banner matches.\n"
                "5. *Bulk job title cleanup before July 20* — Remove location suffixes like 'Barista at [Location]' from badly formed job titles. Remove ONLY the offending location part; do not change the core title (e.g. keep 'Bud Tender'). Customers won't notice.\n"
                "6. *FFH health rate dip is real and concerning* — Noticeable drop over past 2-3 weeks. Hypothesis: ~50% increase in jobs posted to FFH tied to V1→V2 migration, with Indeed flagging them as duplicates. You're investigating with Ugo."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why this matters:* The July 20 cutover is 11 days away. Customer confusion is already causing churn risk (one customer nearly left over comms). The pre-migration comms are the biggest lever you have right now — if people understand what's happening, they stay calm. And the FFH health dip is a potential Q3 goal threat: if V1→V2 duplicates are suppressing Indeed indexing, your D5 zero-applicant rate problem just got significantly worse."
            )
        }
    },

    {"type": "divider"},

    # ── MEETING 2: UGU / MANAN ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 9:45am — Ugochukwu / Manan (1:1)*\n_Ugu_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "7. *V1→V2 migration timeline confirmed* — Bulk dormant-location migration ran June 15 (location-only, no job records touched). V1 job creation cutoff: June 10. Two paths: bulk dormant migration vs. forced-migration reposts.\n"
                "8. *Leading hypothesis: forced-migration reposts → Indeed duplicate flag → FFH health dip* — Job volume nearly doubled week of June 15 (the forced-migration reposts). These jobs likely got flagged as duplicates on Indeed, explaining the D30 healthy job rate collapse for that cohort.\n"
                "9. *May 15–21 cohort dip = unsolved mystery* — The hypothesis above doesn't explain why jobs created May 15–21 (maturing June 15–21) also dipped. This is the hole in the logic. Nelson needs to dig in.\n"
                "10. *activated_at correctly resets on repost* — Confirmed: when a job is reposted, it goes to pending → active, and activated_at resets. This means the dormant-location logic correctly excluded recently reposted jobs. Good.\n"
                "11. *~10–15 rogue companies flagged* — Malcolm identified ~10–15 companies that posted V1 jobs after the cutoff date. Still unresolved whether those slipped through on created_at vs. activated_at logic."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why this matters:* This is a root-cause investigation on the biggest threat to your Q3 #1 goal (FFH D5 zero-applicant rate <10%). If forced-migration reposts are inflating Indeed duplicate flags, you have a fixable, time-boxed problem — but you need to confirm it fast and patch it before the July 20 cutover adds another wave of potential duplicates."
            )
        }
    },

    {"type": "divider"},

    # ── MEETING 3: EPD LEADS SYNC ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 1:30pm — Hiring - Applicants: EPD Leads Sync & Prep*\n_Jatin_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Decisions Made:*\n"
                "12. *Roadmap tooling: Manan stays on Librarian, adds changelog tab* — Core team moving to Google Sheets, but Jatin is happy to work with whatever you prefer. Solution: add a changelog tab to Librarian so Jatin can track edits without cluttering the main view.\n"
                "13. *New EPD Leads sync agenda locked (6 items)* — (1) Current sprint status, (2) Next sprint + definition of ready, (3) Three-sprint lookahead + spike planning, (4) Triage review (applicants-specific), (5) Product polish and quality, (6) Customer signal forcing function. Clean structure.\n"
                "14. *Linear project comment updates: deprecated* — Not being done on either side. Engineers are heads-down; Dana and Jatin don't need it. Your pain is pace, not visibility. The update workflow is more noise than signal. Killing it.\n"
                "15. *Reactivate Jobs confirmed as Copy Jobs replacement (short-term)* — Prevents job flagging and creates a cleaner sponsorship path. Copy Jobs return LATER with a similarity check: if a new job matches a previous one, system recommends reactivating the old job. Rami builds the similarity endpoint, likely reusing the same gRPC endpoint as role + salary recommendations.\n"
                "16. *Source Claiming: design-ready by Tuesday* — Requirements are ready. Fadi is the blocker. You're meeting Fadi tomorrow. Jatin's bar: first-pass design minimum to bring to review (requirements-only not enough).\n"
                "17. *Salary Recommendations + Automatic Go Live: likely punting to 2616 at earliest* — Rami hasn't started the DS work. Engineering won't kick off until 2615 at the earliest, making Automatic Go Live a stretch. You need to confirm with Rami and update the roadmap.\n"
                "18. *Rami is behind — escalate to Ray* — Rami flagged as behind overall, blocking Salary Reco and downstream items. You need to chat with Ray about DS capacity and enablement.\n"
                "19. *Senior engineering quality group: Jatin standing this up* — Will own quality and polish across both Applicants and Core. Once running, it feeds quality issues into the roadmap. Good forcing function."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Why this matters:* Rami being behind is a quiet crisis. He's blocking Salary Recs, Automatic Go Live, AND the Copy Jobs similarity endpoint. That's three roadmap items at risk. Getting ahead of this with Ray now is better than explaining a sprint miss in two weeks."
            )
        }
    },

    {"type": "divider"},

    # ── ACTION ITEMS ──
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "⚡ Your Action Items"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*🔴 P0 — Do Today / This Cannot Wait:*\n"
                "• *Carlo Harness/OpenSpec check-in* — DEADLINE IS TODAY (Jul 10). Confirm this happened or escalate NOW.\n"
                "• *Investigate FFH health dip with Ugu* — Is Indeed flagging V1→V2 jobs as duplicates? You need the answer before July 20.\n"
                "• *Review July 20 cutover plan* — It's attached to the leads agenda. Block time and read it. 11 days out.\n"
                "• *Confirm Dana sends migrated customer list* — She said today. Chase her.\n"
                "• *Source Claiming Banner E2E sign-off* — Matan has been blocked on your approval since Jul 8. This is still outstanding.\n"
                "\n"
                "*🟡 P1 — This Week:*\n"
                "• *Meet Fadi tomorrow on Source Claiming design* — Target: first-pass design by Tuesday. Jatin's bar is clear.\n"
                "• *Chat with Ray about Rami DS capacity* — Rami is behind and it's blocking multiple roadmap items. Do this proactively.\n"
                "• *Confirm Rami's timeline on Salary Recs + update roadmap in Librarian* — Automatic Go Live is likely punting. Reflect this now.\n"
                "• *Loop Nelson in on May 15–21 cohort dip* — No explanation yet for why healthy jobs dropped for that specific cohort.\n"
                "• *Add changelog tab to Librarian* — Small task, big impact for Jatin sync rhythm.\n"
                "• *Review Jatin's PR* — Flagged as urgent; needed before July 20 cutover.\n"
                "• *Confirm Usman's Salesforce triggers for no-trial migrations* — If no op is created for no-trial accounts, interventions could be misconfigured.\n"
                "• *Pre-migration banner copy review* — Should not be AI-first or misleading. Check it.\n"
                "• *Bulk rename job titles with location suffixes* — Remove suffixes before July 20. Don't alter core titles.\n"
                "\n"
                "*🟢 P2 — This Sprint / Don't Drop:*\n"
                "• Confirm Izzy started on role recommendation backend (carry-over)\n"
                "• Follow up with Michael + Cornelius on their Indeed account cases (carry-over Jul 8)\n"
                "• Write proposal for next talent pool email experiment (carry-over)\n"
                "• Pull 13 applicant + 127 clicker emails → Ted (carry-over Jul 7)"
            )
        }
    },

    {"type": "divider"},

    # ── DELEGATIONS ──
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📋 Delegations — What to Chase"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Dana* — Migrated customer list in shareable format (promised for today)\n"
                "• *Carlo* — Harness/OpenSpec check-in (DEADLINE TODAY — confirm it happened)\n"
                "• *Fadi* — Source Claiming first-pass design by Tuesday\n"
                "• *Usman* — Confirm Salesforce op triggers are correctly set up for no-trial migrations\n"
                "• *Jatin* — Meet Rami on Copy Jobs similarity endpoint + gRPC contract\n"
                "• *Ugochukwu* — Confirm exact V1 job cutoff date (messaged team during your call)\n"
                "• *Nelson* — Dig into May 15–21 cohort dip (why did healthy job rate drop for that cohort?)\n"
                "• *Matan* — Track B source claiming started? Guide in use?\n"
                "• *Tanner* — Copy→Reactivate ship date?"
            )
        }
    },

    {"type": "divider"},

    # ── WATCH LIST ──
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "👀 Watch List"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *FFH D5 zero-applicant rate* — Currently 41%. Q3 goal: <10%. The V1→V2 duplicate flag hypothesis could mean this metric is actively getting WORSE right now.\n"
                "• *July 20 cutover* — 11 days. Customer comms are broken. This needs your attention this week.\n"
                "• *Rami DS capacity* — Blocking Salary Recs, Auto Go Live, and Copy Jobs endpoint. Quiet crisis.\n"
                "• *Boost purchase bug* — Still unresolved. Revenue impacting. Where does this stand?\n"
                "• *OpenAI fallback model* — P0 flagged Jul 6. Engineering backlog status still unknown.\n"
                "• *Dana leaving end of September* — Succession/knowledge transfer planning hasn't started (that you've mentioned)."
            )
        }
    },

    {"type": "divider"},

    # ── CLOSING ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Bottom line:* You had a dense, high-signal day. The V1→V2 migration story is crystallizing — customer confusion + potential Indeed duplicate flooding = two fires burning simultaneously with the same root cause. The good news: you have 11 days and you know exactly what needs to happen. Clear the Carlo deadline today, sign off on Source Claiming, and get ahead of Rami's capacity issue with Ray before it becomes a sprint miss.\n\n"
                "_You're doing great — keep stacking those reps. Tomorrow's going to be a good one. 💪_"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest — Jul 9, 2026",
    "blocks": blocks
}

def preview():
    lines = [
        "=" * 70,
        "DAILY DIGEST PREVIEW — Jul 9, 2026",
        "=" * 70,
        f"Channel: {CHANNEL}",
        "",
        "MEETINGS COVERED:",
        "  1. Hiring Leads Standup (8:45am) — 6 decisions",
        "  2. Ugochukwu / Manan (9:45am) — 5 decisions",
        "  3. EPD Leads Sync & Prep (1:30pm) — 8 decisions",
        "",
        "TOTAL DECISIONS TODAY: 19",
        "",
        "P0 ACTION ITEMS:",
        "  - Carlo Harness deadline: TODAY",
        "  - FFH health dip investigation with Ugu",
        "  - Review July 20 cutover plan",
        "  - Chase Dana for migrated customer list",
        "  - Source Claiming Banner sign-off (unblocks Matan)",
        "",
        "KEY THEME: V1→V2 migration = customer comms crisis + FFH duplicate risk",
        "  11 days to July 20 cutover. Rami DS capacity is a quiet crisis.",
        "",
        "SLACK_TOKEN not set — message not sent.",
        "Add SLACK_TOKEN in Cursor Dashboard > Cloud Agents > Secrets.",
        "=" * 70,
    ]
    out = "\n".join(lines) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))

def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
                print(f"     ts={body.get('ts')} channel={body.get('channel')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not TOKEN:
        preview()
    else:
        send()
