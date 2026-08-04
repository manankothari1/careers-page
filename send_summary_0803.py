#!/usr/bin/env python3
"""
Daily Decision Summary — Monday Aug 3, 2026 (PDT)
Meeting: MBR Review (9:00 AM PDT) with Matan Chen Zion & Jatin Bhandari
"""
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
            "text": "🧠 Chief of Staff Daily Brief — Monday, Aug 3",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big productive start to the week — you had one focused meeting today with Matan and Jatin to lock down the MBR structure. Here's everything you need to know, including what's coming off the watch list and what needs to happen tomorrow. You're killing it. 💪"
        }
    },
    {"type": "divider"},

    # DECISIONS SECTION
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 DECISIONS MADE TODAY*\n_MBR Review · 9:00 AM · w/ Matan Chen Zion, Jatin Bhandari_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 1: MBR Structure LOCKED* ✅\n*What:* Single combined health slide (trial starts + ARR + applicant flow % + healthy jobs %) — then Matan's ICP section — then Manan's applicant flow learnings. Dana's separate section is gone; it's one unified health narrative.\n*Why:* Cleaner story for leadership. Dana and Manan were siloed; combining into one slide shows the full picture and reduces confusion.\n*Rationale:* Andrew doesn't want Matan presenting in that meeting, so Matan's ICP work feeds Manan's narrative.\n*Action:* Manan to build the combined health slide after Ray reviews notes."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 2: 'Message at the Right Time' Thesis = MBR Frame LOCKED* ✅\n*What:* Cold calling data is the anchor: only owners actively hiring were willing to stay on the line. This is the through-line for the entire ICP section.\n*Why:* It's a company-wide truth everyone already intuitively knows ('small business owners don't have time for shit') — the data now backs it up empirically.\n*Action:* Matan's ICP section frames this; meta ads survey + email test mentioned in passing only (4 replies ≠ real signal). Frame email test as 'ongoing experiment, still gathering signal.'"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 3: Trigger-Based Comms = 'What We're Doing About It' LOCKED* ✅\n*What:* Leading hiring indicators (overtime spend, terminations, shift swaps) → proactive outreach. Example: 'Did you know 1 in 2 businesses that see a spike in overtime spend would save by hiring?' Matan will build comms triggers for each signal.\n*Why:* Rather than cold-calling or blast emails, you meet OEMs when they're showing hiring intent — not when you decide they should care.\n*Rationale:* Supports the 'message at the right time' thesis directly. This is what makes the MBR story cohesive: 'here's what we learned → here's what we're building.'\n*Action:* Matan to design experiments around each trigger signal; share doc with Manan before MBR."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 4: Matan Rebuilding Full Hiring Comms Map in Iterable* 🔄\n*What:* Matan is auditing every trigger, template, and firing status across Iterable + HB1. SendGrid shows templates as 'active' even when they haven't fired in months. This map will be the baseline for all future comms experiments.\n*Why:* Without knowing what's actually firing, you can't run meaningful experiments. Matan discovered he has no visual into HB1's comms layer.\n*Action:* Jatin to walk Matan through admin view + mail item tooling in their next 1:1. Matan to share full comms map with Manan once complete."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 5: MBR Slides Are Gated on Ray Review* 🚦\n*What:* No one builds slides until Ray confirms the narrative makes sense.\n*Why:* With Ray out this week, you're working asynchronously. Building slides before narrative sign-off = wasted effort.\n*Action:* Manan to finish MBR notes → send to Ray for review *today/tomorrow*. Don't start slides until Ray gives the green light."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 6: 'Blocked' Labels in Linear = Daily Push Mechanism ADOPTED* ✅\n*What:* Add 'blocked' labels to all stalled applicant flow items in Linear so Jatin can use them as a daily push signal.\n*Why:* Too many near-done projects (culinary agents, etc.) are sitting in limbo with no forcing function. Labels create visibility and urgency without requiring a meeting.\n*Action:* Manan to right-click + add 'blocked' label on every stalled item today. Jatin checks daily and pushes blockers."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 7: V1→V2 Migration = Fully Complete from User Perspective (Jul 20)* ✅\n*What:* Front end removed from monolith as of Jul 20 — unblocks client annexation work. Back end is inert but still in codebase; ~1 sprint to clear it out, not blocking anything.\n*Why:* Jul 20 was the last day a V1 job could expire; visible uptick in V2 numbers confirms the migration.\n*Action:* Pull the V2 trial starts blip chart (around Jul 20 date) for MBR slide. Nelson showed it in Hiring Leads; Dana noted it too."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 8: Domain Events — Hiring Lifecycle Code Complete* ✅\n*What:* Hiring lifecycle events are code complete; waiting on infra to provision Kafka topics. Most complex milestone done. Next = applicant status events (significantly simpler). This unlocks HB Assistant to answer 'what's going on with my job post?'\n*Why:* This was the hardest part of the domain events work; everything downstream is easier now.\n*Action:* Frame in MBR as 'completed our first milestone — this unlocks Homebase Assistant to read hiring data.' No need to get technical."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 9: Scheduling Feature Data for MBR* 📊\n*What:* ~270 users have used the scheduling feature. ~1/3 want candidate to pick time; slightly under 1/3 want to propose a specific time themselves. Feature is released.\n*Why:* Shows real user adoption signal for MBR.\n*Action:* Clean up the Amplitude funnel chart before including in slides (currently showing confusing 100% formatting)."
        }
    },

    {"type": "divider"},

    # ACTION ITEMS SECTION
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚡ YOUR ACTION ITEMS (Prioritized)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🔴 *P0 — Today/Tonight*\n• *Finish MBR notes → send to Ray* — No slides until Ray confirms narrative. Do this FIRST.\n• *Carlo direct conversation* — He's back from Canada TODAY. 18+ days overdue on Harness/OpenSpec. Also kick off Talent Pool rake task (1-2 days). Don't let another day go by.\n• *Fadi Boost modal Figma* — 8 days overdue. Send it today.\n• *ICP experiments sync with Matan* — Dana is OUT all week, returns Aug 10 with 2 days left before her last day (Aug 12). You need to get fully up to speed on what Matan is running NOW.\n• *422 errors* — Day 25. Ray is out; you're the decision-maker. Check RCA progress with Jatin."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🟡 *P1 — This Week*\n• *Add 'blocked' labels to all stalled Linear items* — Agreed with Jatin in today's meeting. Quick wins: culinary agents + everything else in the applicant flow queue.\n• *Follow up with Gray on culinary agents* — Blocked on vendor side. Send that email.\n• *Ted/Rami business case* — Go direct this week; Ray is out. Make the case for keeping Rami on hiring.\n• *Dana succession* — Aug 12 = 9 days away. Dana off this week, back Aug 10. Only 2 working days left once she returns. Page Templates hand-off must start THIS WEEK.\n• *MBR content* — Drive the applicant side section solo. Ray + Dana both out.\n• *Bob+Jonathan comms agent outcome* — Still unknown from the Jul 29 3pm sync. Confirm what was decided on data/DS vs. product eng ownership before Jatin kicks off manual experiment.\n• *Confirm Jatin/Paul/Ted cadence* — Paul back Tuesday Aug 5. Jatin committing to daily updates."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "🟢 *P2 — Before End of Week*\n• *Scooters follow-up email* (Olivia/Maria/Lacey) — Still open from Jul 29\n• *Franchise ticket* — 5+ days open\n• *Matan comms doc review* — Sonia still blocked on building; unblock her\n• *Juan Sanchez follow-up* — Still open\n• *Indeed noindex help article* — Draft it\n• *Usman candidate email experiment results* — Check them\n• *Izzy + Tanner API contract alignment* — Role/salary reco"
        }
    },

    {"type": "divider"},

    # WATCH LIST
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 WATCH LIST — Critical Countdown*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• 🔴 *Dana last day: Aug 12 = 9 days* — Off this week. Returns Aug 10. 2 days left. CONFIDENTIAL. No succession plan exists yet. Act now.\n• 🔴 *Carlo Harness/OpenSpec: 18+ days overdue* — Back today. Direct conversation, not async.\n• 🔴 *422 errors: Day 25* — Jatin on RCA. You're calling it with Ray out. Stay on top.\n• 🟡 *Fadi Boost modal Figma: 8 days overdue* — Today is the day.\n• 🟡 *Comms Agent manual experiment* — Jatin pushing for this week. Bob+Jonathan outcome unknown. You're making the call with Ray out.\n• 🟡 *MBR: Ray + Dana both OUT* — You're driving applicant side solo. Finish notes, gate on Ray review.\n• 🟡 *Talent Pool Outreach* — Carlo back today; kick off rake task (1-2 days).\n• 🟢 *Rami (DS)* — Ted pulling back post-Kan. Make business case to Ted directly this week."
        }
    },

    {"type": "divider"},

    # CLOSE
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💡 The Big Picture*\nToday was a really important alignment meeting — you walked in and locked the MBR narrative, the ICP framing, and the comms experimentation thesis all in one shot. The 'message at the right time' story is tight and it'll land well with leadership. The biggest risk this week isn't MBR prep — it's Dana. Nine days and counting with no succession plan. Everything else can slip a day; that cannot.\n\nYou've got this. Get to Carlo first thing tomorrow morning and finish those MBR notes tonight. 🚀"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Daily Brief · Monday Aug 3, 2026 · 1 meeting reviewed · Generated at 5pm PDT"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Brief — Monday Aug 3, 2026 | MBR structure locked, 9 decisions, P0 action items inside."
}


def preview():
    print("=" * 70)
    print("PREVIEW — no Slack token found")
    print("=" * 70)
    for block in blocks:
        if block["type"] == "header":
            sys.stdout.buffer.write(("\n### " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block["type"] == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            sys.stdout.buffer.write(b"---\n")
        elif block["type"] == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))


def send_slack():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("✅ Slack message sent successfully!")
                print("   Channel:", body.get("channel"))
                print("   Timestamp:", body.get("ts"))
            else:
                print("❌ Slack API error:", body.get("error"))
                print("   Full response:", json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print("❌ HTTP error:", e.code, e.reason)
        sys.exit(1)
    except Exception as e:
        print("❌ Unexpected error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if not TOKEN:
        preview()
        print("\n⚠️  No SLACK_TOKEN found. Add it in Cursor Dashboard → Cloud Agents → Secrets.")
        sys.exit(0)
    else:
        send_slack()
