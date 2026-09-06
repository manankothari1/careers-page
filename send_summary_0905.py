import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Weekend OOO Dispatch — Sat Sep 5 \U0001f334",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! \U0001f44b Hope the OOO weekend is treating you well and you're fully unplugged. Zero meetings on the books today (just how it should be on a Saturday). Here's your full situation report so Tuesday landing is crisp.\n\n*Status: OOO \u2705 | Back: Tue Sep 8 | Sep 7 = Labor Day (office closed)*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 CRITICAL — Needs You First Thing Tue Sep 8*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f534 *Indeed Feed Suspended — Day 11*\n> Package fraud evidence with Divij \u2192 send to Jessica Kanaskie. This is the #1 unlocker. Source claiming pilot is live (20% experiment) and Jessica is connecting you + Skye with David (Indeed Product) on source claiming — expect that email intro Sep 14-21 window. Every day of suspension = applicant flow impact.\n\n\U0001f534 *Departures Signal Docs \u2192 Sales — OVERDUE (was Fri Sep 4)*\n> Send conflict docs + data to Zane, Sean, Jon W, Bobby. Sales outreach slipped from Mon Sep 7 (Labor Day) to Tue Sep 8. You committed to this by EOW. First thing Tuesday.\n\n\U0001f534 *120-Day Open Job Flow Proposal \u2192 Skye*\n> You committed to send this BEFORE OOO. Confirm sent / send Tuesday if not. Architecture is locked — Skye just needs the write-up."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f OVERDUE — Queue for Week of Sep 8*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Power User Analysis \u2192 Sales* — 90%+ started w/ Indeed/in-person. Helps reps picture a real customer. OVERDUE.\n\u2022 *Verify In-Product Termination Trigger* — Previous experiment; confirm still active + generating volume.\n\u2022 *Overtime Data Cuts* — (a) OT threshold trial starters; (b) payroll usage vs connect/conversion. OVERDUE.\n\u2022 *EarnIn Sample Feed* \u2192 jon.salzberg@earnin.com — Was due Aug 31. Way overdue.\n\u2022 *Fraud Evidence Package* (with Divij) — Cleanup + score + OTP \u2192 Jessica. Tied to Indeed feed unblock.\n\u2022 *IBK: Pull JD A/B Signal* — Experiment running 2+ weeks. Pull before V2 50/50 rolls out.\n\u2022 *Linear Tickets: Recency + Distance Experiments* — Manan's action, unblocks Divij.\n\u2022 *Divij CSV Spec for Iterable* — Blocking experiment coding.\n\u2022 *IBK OTP Thread Sign-Off* — Pending your review."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb WHAT FADI IS HOLDING (trust him)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Copy + Reactivate Designs* — Was targeting Mon (Labor Day slip). Expect Tue Sep 8.\n\u2022 *Talent Pool SMS Opt-In* — Fadi starting. 100K applicants/month addressable. Architecture locked.\n\u2022 *OEM Attribute Study* — Sep 4 target. Check in Tuesday."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4c5 Calendar Heads Up — Week of Sep 8*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Sep 7 — Labor Day* | Office closed. All outreach slips to Sep 8.\n\u2022 *Sep 7-11 — Homie Heads Down Week* | Light meetings by design. Use for deep work on overdue items.\n\u2022 *Sep 8 — You\u2019re back!* | Land hot. Departures docs + Indeed fraud package = top of list.\n\u2022 *Sep 14-18 — Dreamforce WFH optional (SF office)*\n\u2022 *Sep 14-21 window — Jessica\u2019s intro: You + Skye + David (Indeed Product)* | Re: source claiming\n\u2022 *~Sep 14-17 — Skye Toronto trip*\n\u2022 *Sep 18-21 — Yosemite trip* \U0001f9a5 (Diamond O Campground) | Block calendar now if not done"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f9e0 Chase List (don\u2019t let these slip further)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Role Normalization PRD* — Divij + Sina (was due Sep 3). Chase on return.\n\u2022 *422 Publishing Errors* — Day 11+. 146 locations. Jatin RCA — get status.\n\u2022 *Carlo Knowledge Risk* — Sole Indeed integration owner. Team swarming agreed. Get update.\n\u2022 *Annual Subscription Cancel Policy* — Post in Hiring Leads. OVERDUE.\n\u2022 *Roadmap Prompt Update* — Was due Fri Sep 4. Confirm done.\n\u2022 *Matan \u2192 Greg meeting* — Was week of Sep 1. Confirm it happened.\n\u2022 *Marina / Mundo Academy* — Follow up ~Sep 10.\n\u2022 *Jobcase XML/API docs* — Chase Donnie Mannino (dmannino@jobcase.com)."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4ca Q3 Scoreboard (as of Sep 4 EOD)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "| Metric | Current | Q3 Target |\n| FFH D5 Zero-Applicant Rate | 41% | <10% |\n| Line Cook Jobs Healthy D30 | ~7% | 50% |\n| Overall Healthy Job Rate | 30% | 80% |\n| 422 Errors | 146 locations, Day 11+ | 0 |\n\n\u26a0\ufe0f *Indeed feed suspended Day 11 = applicant flow impact compounding. Fraud package = critical path.*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "You\u2019re doing amazing work, Manan. The Indeed account setup experiment is live (20% rollout), talent pool SMS architecture is locked, and the team is holding down the fort. Enjoy the rest of the weekend \u2014 Tuesday is going to be a great re-entry. \U0001f680\n\n_\u2014 Your Chief of Staff_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Weekend OOO Dispatch \U0001f334 \u2014 Sat Sep 5 | Zero meetings today (as expected). Full battle plan for Tue Sep 8 return inside.",
    "blocks": blocks
}

def preview():
    print("\n" + "="*70)
    print("SLACK MESSAGE PREVIEW (would send to channel D06E4QMHCNN)")
    print("="*70)
    print(payload["text"])
    print("-"*70)
    for block in blocks:
        if block["type"] == "section" and "text" in block:
            sys.stdout.buffer.write((block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block["type"] == "header":
            sys.stdout.buffer.write(("## " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block["type"] == "divider":
            sys.stdout.buffer.write(b"---\n")
    print("="*70)

if not TOKEN:
    print("[PREVIEW MODE] No SLACK_TOKEN found. Add it in Cursor Dashboard > Cloud Agents > Secrets.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8", "Authorization": f"Bearer {TOKEN}"}
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"[SUCCESS] Message sent to {CHANNEL}")
    else:
        print(f"[ERROR] Slack API error: {result.get('error')}")
        preview()
except Exception as e:
    print(f"[ERROR] {e}")
    preview()
