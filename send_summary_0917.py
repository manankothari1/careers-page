#!/usr/bin/env python3
"""Daily Chief-of-Staff Slack digest — Sep 17, 2026 (Thursday)"""
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
            "text": "🏕️ Chief of Staff Daily Digest — Thursday, Sep 17",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THEME: REACTIVATE FLOW LOCKED · INTENT SIGNALS CONCEIVED · EARNBETTER DEAL ALIVE · COMPLIANCE SPRINT STARTED · QA RESET*\n\n3 meetings today. Grade: *A* 🔥 Big day, Manan — you shipped clarity on 3 major fronts the same morning you leave for Yosemite tomorrow. Last working Thursday before OKR lock. Let's make sure nothing falls through."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 KEY DECISIONS TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Morphing card UX direction LOCKED for Reactivate flow* ✅\n_Fadi / Manan Copy + Reactivate — 10:37am_\n\nTaylor and Alexa independently called it: the morphing card is the winner. Users select an option, the card morphs, follow-up questions appear, then a 'Confirm' button prevents accidental taps. Previous open question between Option A (Skye) and Option C (you) is now resolved by user testing signal — Option C wins. First 2 steps are now combined into one card.\n\n*Why:* Cleaner UX, reduces cognitive load, avoids the 'upsell' feeling of 'keep it open' framing that every reviewer flagged."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Reactivate flow split into TWO separate diagrams* ✅\n_Fadi / Manan — 9:15am_\n\nThe combined flowchart was causing engineering confusion because it merged two fundamentally different conditions: (a) OEM confirmed a hire/closed job, and (b) 30 days elapsed since posting. These now become separate flows with separate dialogue trees.\n\n*Why:* Engineers need to know which condition is checked first. Mixing them made the branching logic opaque and would have slowed implementation."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Intent Signals: Overtime Pay as Hiring Trigger — concept green-lit* ✅\n_Fadi / Manan — 9:15am_\n\nOvertime pain ($15K/month hits) is a visceral, data-backed reason to hire. Preferred placement: *both* the earnings tab dot (high reach) *and* the post-payroll completion modal (high intent), plus an email follow-up with a 'Remind me later' option that creates a Salesforce opportunity. Stretch: modal lets OEM choose email or a sales call.\n\n*Why:* You're not creating new urgency — you're surfacing pain that already exists at the exact moment the OEM feels it. The post-payroll 'sigh of relief' is one of the highest-intent moments in the product. This is the kind of insight that makes Gabe say yes."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. EarnBetter: Mutual test confirmed, no formal contract* ✅\n_Wage Access & EarnBetter — 11:35am_\n\nJon Blackwell confirmed: no blockers to moving forward with marketing churned Homebase employees through EarnBetter. Structure: mutual test with no formal contract — if it generates value, terms get formalized; either side can walk if not. Could shift to CPC if the job feed underperforms.\n\n*Why:* Low-risk entry into a channel with meaningful reach (~80K terminated employees/month). The data moat is the salary signal from cash-out — 'you'd earn 20% more elsewhere' is a genuinely differentiated message nobody else can send."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Indeed Easy Apply compliance: PDF approach, no disable feature* ✅\n_Wage Access & EarnBetter — 11:35am_\n\nIndeed asked for documentation on enabling/disabling Easy Apply. Decision: do NOT build a disable feature proactively. Instead, create a PDF explaining that Homebase auto-enables Easy Apply on all jobs (pulling language from Indeed's own site on the benefits), submit it, and wait to see if Indeed pushes back.\n\n*Why:* Building a disable feature speculatively wastes eng time on something Indeed may never actually require. The PDF buys time and shows compliance intent. Deadline: September 30."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. AI Screener compliance: 4-year data retention confirmed as requirement* ✅\n_Wage Access & EarnBetter — 11:35am_\n\nAll AI screener data must be stored for at least 4 years and accessible to employers on request. California HQ may mean this applies to all employers on the platform regardless of their location. A precedent process exists from a prior security incident.\n\n*Why:* This is a legal requirement, not a product choice. The good news: the process already exists. What's unknown is whether the current data model captures deal-breaker responses correctly — especially now that null values may mean 'no deal breakers' rather than 'data missing.'"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. QA process reset: engineers QA own work + sprint show-and-tell* ✅\n_Wage Access & EarnBetter — 11:35am_\n\nHomebase eliminated the QA function and you've been the bottleneck. New plan: engineers QA their own work before handoff; you do a final pass or sign off. Skye proposed a sprint show-and-tell where engineers demo shipped work — creates accountability and keeps sales/support informed.\n\n*Why:* You can't be a QA org of one at the pace you're shipping. The show-and-tell creates positive peer pressure to actually test before demoing. Tentative date: *Friday, September 25.*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 ACTION ITEMS — BY OWNER*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*YOU (Manan) — priority order:*\n\n🔴 *[OVERDUE TODAY]* Send Q4 thoughts to Skye — OKR lock is *TOMORROW* (Fri Sep 18). Exec review Mon Sep 22. If not sent, do it tonight.\n\n🔴 *[BY SEP 30]* Create + submit Indeed Easy Apply PDF to Indeed. Pull language from Indeed's own site on Easy Apply benefits. Auto-enablement explanation only — no disable feature.\n\n🟡 *[EARLY NEXT WEEK]* Write intent signals concept doc — What is the feature, why it matters, which placements were explored. Deck goes to Gabe early next week.\n\n🟡 *[ASAP]* Start NDA thread with Ray + Skye — Mutual NDA template needed before any customer data is exchanged with EarnBetter. Skye provides template; you start the thread.\n\n🟡 *[ASAP]* Follow up with Jon Salzberg at EarnBetter (jon.salzberg@earnin.com) — Signal that Homebase is moving forward with the churned employee outreach integration. *Note: this email has been overdue 15+ days.*\n\n🟡 *[NEXT WEEK]* Compile Reactivate + Copy project task list — Walk Bob or Madhav through it once done.\n\n🟡 Verify deal-breaker data model — Confirm null = 'no deal breakers on job' is intentional and that screener response data is captured correctly as deal-breaker usage grows."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*FADI (frizk@joinhomebase.com):*\n\n• Create Linear project for Copy + Reactivate — empty project, add his tickets; you fill in write-up\n• Pull Granola screenshots into FigJam + start intent signal designs (targeting tomorrow)\n• Get Alexis's input on payroll placement — she's now the payroll designer and knows every corner\n• Map out the 3-week reactivation window as a *separate* flow (not bolted onto main diagram)\n\n*JON BLACKWELL:*\n• Confirm continued wage access field type — likely Boolean; confirmation unblocks the Iterable trigger\n\n*JOBY:*\n• Loop Jon Blackwell back before anything goes out to churned employees via EarnBetter"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ WATCH LIST — STILL OPEN (carry-forward)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🔴 *INDEED FEED SUSPENDED — Day 25.* Fraud evidence package (you + Divij) → Jessica Kanaskie. David (Indeed Product) intro window closes *Sep 21 — 4 days left.*\n\n🔴 *DEPARTURES SIGNAL DOCS — 15+ DAYS OVERDUE.* Conflict docs + data → Zane, Sean, Jon W, Bobby. Not mentioned in any meeting since Sep 4. Tomorrow is Yosemite — this window is closing.\n\n🔴 *Marina / Mundo Academy — 9 DAYS LATE.* marina@mundoacademy.com. Under 5 minutes. Do it now.\n\n🟡 *Ernan / EarnIn-Jobcase* — reply still pending 10+ days. Iszael blocked. Skye needs to escalate.\n\n🟡 *Pending syndication black box* — 3 states conflated (queue / fraud rejected / ToS flagged), no status history, silently blocking new customers. Flagged today. Needs product spec.\n\n🟡 *Custom deal-breakers risk* — employers can add free-text deal-breakers (e.g. 'Are you Christian?'). On radar, not top of queue — but Skye wants it tracked.\n\n🟡 *422 publishing errors* — 146 locations since Jul 9. Jatin RCA still outstanding.\n\n🟡 *Culinary Agents $69 boost* — Fadi was shipping this today. Confirm it went out.\n\n🟡 *IBK JD A/B signal* — overdue 3+ weeks. Pull before V2 widens."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🏕️ YOSEMITE PRE-FLIGHT CHECKLIST*\n\nLeaving tomorrow (Fri Sep 18). Back Mon Sep 22 = EXEC REVIEW DAY.\n\n☑️ Q4 thoughts → Skye (if not done tonight, find 20 min first thing tomorrow morning)\n☑️ OKR lock is Fri Sep 18 — you need to be aligned with Skye before you drive to Diamond O\n☑️ Create + submit Indeed Easy Apply PDF — this one has a Sep 30 hard date, get a draft ready before you leave\n☑️ Quick note to Fadi confirming intent signals FigJam direction\n☑️ NDA thread with Ray + Skye started (30 seconds to kick it off)\n\nTrip context: Diamond O Campground, Sep 18-21. Executive review on Monday Sep 22 the moment you're back. You are walking into that room as *Senior PM Manan Kothari* for the first time. Come back ready to own the room. 🏔️"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📊 TODAY BY THE NUMBERS*\n• 3 meetings: Fadi/Manan 9:15am · Fadi/Manan Copy+Reactivate 10:37am · Wage Access/EarnBetter 11:35am\n• 7 decisions made\n• 12 action items generated (4 for you, 4 for Fadi, 2 for others)\n• Days since Indeed feed suspended: *25*\n• Days until OKR lock: *1 (tomorrow)*\n• Days until Yosemite: *1 (tomorrow)*\n• Days until exec review: *5 (Monday)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "_Your Chief of Staff signs off. You had a strong Thursday — morphing card locked, intent signals lit up, EarnBetter unblocked, compliance addressed. Don't let Q4 thoughts to Skye slip. Enjoy Yosemite — you've earned it, Senior PM. 🌲_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Digest — Sep 17, 2026 | REACTIVATE LOCKED · INTENT SIGNALS CONCEIVED · EARNBETTER ALIVE · QA RESET | Grade: A"
}


def preview():
    sys.stdout.buffer.write(b"\n=== SLACK MESSAGE PREVIEW (channel: " + CHANNEL.encode() + b") ===\n\n")
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            sys.stdout.buffer.write(("# " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif btype == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n")


token = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

if not token:
    print("No SLACK_TOKEN found — printing preview only.")
    preview()
    sys.exit(0)

req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"Slack message sent successfully! ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        preview()
except urllib.error.URLError as exc:
    print(f"Network error: {exc}")
    preview()
