#!/usr/bin/env python3
"""Daily decision digest for Manan Kothari — Jul 1, 2026 (PDT)"""
import json, os, sys, urllib.request, urllib.error

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
            "text": "Chief of Staff Daily Briefing — Tuesday, July 1",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Great day of alignment — you had two back-to-back meetings that essentially *resolved one of your biggest product architecture debates*: Copy vs. Reactivate. You got buy-in from Ray AND walked Tanner through the technical path. That's a clean win. Here's everything you decided, why, and what you own next. Let's go! :rocket:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Today's Meetings (July 1, 2026)*\n• 1:00 PM — Ray / Manan: Copy/Re-Activate Strategy\n• 3:00 PM — Tanner / Manan: Re-Activate & Copy (Technical Deep-Dive)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:mega: TL;DR — Today's Big Theme*\n\nYou've officially killed the Copy Job feature. Indeed flags *any* new job with overlapping details as a duplicate requiring sponsorship — no amount of description tweaks fixes this. Reactivate is now the only path. You got CEO-level alignment with Ray at 1pm and technical buy-in from Tanner at 3pm. This was a high-leverage day."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bulb: Decisions Made Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":one: *Copy Job Feature — KILLED (emergency removal)*\n*Decision:* Remove copy job from the product entirely.\n*Why:* Indeed flags any new job with the same role type (title, pay, description overlap) as a duplicate and demands sponsorship. Even renaming the role and changing the description triggers it. Manan confirmed directly with Indeed reps — there is no workaround. Keeping copy in the product actively sets customers up for a sponsorship cliff.\n*Watch out for:* Customers who previously used copy may have dirty data — may need a cleanup pass."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":two: *Reactivate = the only path forward*\n*Decision:* All job re-listing goes through reactivate (same job request ID, same Indeed job). No more new IDs.\n*Why:* Keeps the Indeed job 'alive' — no duplicate flag, no forced sponsorship. V1 already had this; it just needs to be exposed to customers.\n*Caveat:* Reactivated jobs rank lower organically ('less fresh') — steady trickle vs. flood on a new post. But still infinitely better than copy, which gets zero organic applicants."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":three: *Job Requisition Concept — introduced to solve applicant buckets*\n*Decision:* Candidate management (separate applicant pools per hiring round) will be solved via a 'job requisition' layer that groups hiring rounds under one role — NOT by creating new job IDs.\n*Why:* Customers want to track 'hired for this round' separately, but creating a new job ID to do so is exactly what breaks Indeed. Decoupling requisition from job ID is the right architecture.\n*This is a design + eng task — no one assigned yet.*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":four: *Auto-reactivation at Day 29 — agreed as buildable*\n*Decision:* If a job hits Day 29 and hasn't been manually closed, auto-reactivate on the OEM's behalf.\n*Why:* An unclosed job at Day 29 almost certainly means the employer is still hiring. Auto-reactivating keeps them on Indeed without them having to think about it. Tanner confirmed this is architecturally doable.\n*Open question:* What's the UX for letting employers know this happened / opt out?"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":five: *Facebook Jobs — backfill skipped, enable for net new only*\n*Decision:* Facebook integration is ready. Skip backfill of existing jobs. Enable for net new job postings only.\n*Why:* Backfilling would require an API call on every existing job — not worth the effort relative to benefit. Net new jobs will automatically get the Facebook distribution going forward.\n*Owner:* Tanner to turn this on."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":six: *Indeed Oct 1 Sponsorship Policy — needs testing via Ashby*\n*Decision:* Before locking in the reactivation UX, test whether Indeed's new Oct 1 policy flags reactivations via ATS (Ashby) or only direct Indeed reactivations.\n*Why:* Indeed's policy docs are ambiguous. Ray's gut says Indeed is 'coming for ATS-sourced jobs too within ~12 months,' but ATS reactivation may currently be exempt — which matters for how you position reactivation to customers.\n*Owner:* Ivana to reactivate a job via Ashby and check for sponsorship flag."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":seven: *ZipRecruiter budget cap — problem flagged*\n*Decision/Finding:* ZipRecruiter burned through a $2K budget in 1.5 days with no job-level caps available. This is a significant risk for OEM spend efficiency.\n*Status:* No resolution yet — flagged for further investigation. You may need to pause or restructure Zip spend until job-level caps are available."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":eight: *Homebase positioned as 'riverboat guide' for sourcing*\n*Decision:* Value prop framing: Homebase helps customers spend smarter, sets expectations on applicant volume, and recommends sponsorship when speed matters. NOT 'we have a special deal with Indeed.'\n*Why:* The 'special deal' framing won't last (Indeed is tightening policies). The 'guide' framing is durable and builds trust.\n*This needs to flow into sales scripts, onboarding UX, and in-product messaging.*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Your Action Items (Manan owns)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:fire: Do Today / Tomorrow*\n• *Analyze reactivation applicant discount* — Pull V1 jobs that were reactivated and map reactivation events to applicant flow spikes. Use Claude Code + CDC table in Databricks. Confirm whether reactivated jobs get ~40% of new-job volume. This is the data backbone for the entire reactivation narrative.\n• *Run Claude/Claude Code on Indeed's Oct 1 policy page* — Screenshot the policy, pass the URL, give it specific scenarios. Get clarity on the sponsorship rules before you design the UX.\n• *Prioritize copy job removal in sprint* — This is an emergency fix. Make sure Tanner has it scoped and in-flight ASAP.\n• *Follow up with Ivana on Ashby reactivation test* — Did she test it? What did Indeed return?"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:pencil: Design / Spec Work (this week)*\n• *Design reactivation UX with applicant expectation-setting* — Use the job tile dashboard and to-dos to communicate estimated applicant volume and sponsorship options. This is the 'riverboat guide' brought to life in product.\n• *Define the 'job requisition' concept* — Write a quick spec on how to group hiring rounds under one role without creating new job IDs. Who's building this? Tanner? Needs a PM owner.\n• *Design auto-reactivation (Day 29) opt-out UX* — If you're auto-reactivating on OEM's behalf, how do they opt out? What's the in-product notification?\n• *Add gaming-detection logic to reactivation* — Consider a warning: 'Reactivating too soon won't restore Indeed freshness until X date.' Investigate close → reactivate time windows to detect abuse."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:chart_with_upwards_trend: Data / Experiment Follow-ups*\n• *Poached experiment* — Only 3 line cook postings so far. Add baristas/cashiers for a broader sample. Follow up on where this stands.\n• *ZipRecruiter* — Figure out job-level budget caps or pause Zip spend. $2K in 1.5 days is unsustainable without controls."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:hourglass: Carry-Forward — Still Needs You (from Jun 30 + before)*\n• Send finalized call script to Sean (source claiming)\n• Confirm Ugu's ETA on 'Finish Account Setup' to-do\n• Define success tracking for the two source claiming call-order approaches\n• Document 50/50 A/B test hypothesis for Sprint 2626 backlog\n• Send modal copy to Ted (hiring onboarding designs)\n• Follow up: Rami email blast status (was due EOD Jun 25 — very overdue :rotating_light:)\n• Draft v3 Q3 goals doc (3-bucket structure, share with Ray before John)\n• Decide comms agent ownership (take or leave with Dana/Fadi/Davi)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:trophy: Today's Win*\nYou walked into today with a product architecture ambiguity (copy vs. reactivate) and walked out with full alignment from both your CEO and your eng lead — in the same afternoon. That's not small. The copy → reactivate switch is foundational for everything OEM-related in H2. Great work. Now go run that reactivation discount analysis and design the riverboat guide UX. :sunglasses:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot | Jul 1, 2026 | 2 meetings | 8 decisions | Homebase Applicant Flow"
            }
        ]
    }
]

payload = {"channel": CHANNEL, "blocks": blocks, "unfurl_links": False, "unfurl_media": False}

def preview():
    sys.stdout.buffer.write(b"\n=== DAILY DIGEST PREVIEW (Jul 1, 2026) ===\n")
    for b in blocks:
        if b.get("type") == "section":
            txt = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt[:300] + ("..." if len(txt) > 300 else "") + "\n\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "header":
            sys.stdout.buffer.write(("## " + b.get("text", {}).get("text", "") + "\n\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"===========================================\n")

def send():
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8", "Authorization": f"Bearer {TOKEN}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            resp = json.loads(r.read())
            if resp.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
                return True
            else:
                print(f"[ERROR] Slack API error: {resp.get('error')}")
                return False
    except Exception as e:
        print(f"[ERROR] Request failed: {e}")
        return False

if __name__ == "__main__":
    preview()
    if not TOKEN:
        print("\n[WARN] No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN).")
        print("Add the token as a secret in Cursor Dashboard > Cloud Agents > Secrets.")
        sys.exit(0)
    send()
