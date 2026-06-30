#!/usr/bin/env python3
"""
Daily Decision Digest — Jun 29, 2026 (Mon PDT)
Chief of Staff summary for Manan Kothari
Slack channel: D06E4QMHCNN
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
            "text": "Chief of Staff Daily Digest — Monday, Jun 29 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! \U0001f44b Big day today \u2014 4 meetings packed with meaningful forward progress. "
                "You made some real, crisp decisions that are going to accelerate the OEM onboarding and applicant quality story. "
                "Here\u2019s your full rundown."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4ca Meeting 1 of 4 \u2014 Hiring Week in Review* (9:00 AM | Ray, John, Dana, Matan, Usman, Nelson, Ankit)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 1 \u2014 Ship resume-inclusive matching NOW, no more A/B testing*\n"
                ">*What:* Resume signal is driving 100%+ higher accept/advance rates vs. control. Team aligned to roll out without further experimentation.\n"
                ">*Why:* The data is directionally unambiguous \u2014 resumes objectively improve match quality. Waiting for a larger sample is opportunity cost, not rigor.\n"
                ">*Watch out:* Healthy job rate (20 apps + 5 top matches threshold) will likely *dip* short-term as the bar rises. Don\u2019t panic \u2014 it\u2019s expected.\n"
                ">*Your action:* \u2705 Get added to the match-definition alignment discussion (Dana to loop you in)."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 2 \u2014 Retire \u201cPersonal Recruiter\u201d messaging; go all-in on \u201cHomebase Advantage\u201d*\n"
                ">*What:* Personal recruiter framing is not landing \u2014 especially with V1 switchers who feel the AI angle is off-putting or the add-on framing feels like a downgrade. \u201cHomebase Advantage\u201d (we know SMBs, we\u2019ll help you hire smarter) is resonating across both Dana\u2019s outreach AND sales calls.\n"
                ">*Why:* Two separate problems confirmed: (1) V1 customers feel downgraded, not upgraded \u2014 needs \u201csame + more\u201d messaging fix; (2) growth beyond V1 is a separate challenge. Don\u2019t conflate them.\n"
                ">*Your action:* No explicit action on you \u2014 but flag this framing shift to Cindy / PMM as you finalize designs today."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 3 \u2014 Usman shifts cold-call approach: pain-point-first, then pitch*\n"
                ">*What:* Customers hanging up at the word \u201chiring\u201d suggest prior negative touchpoints. Usman will now lead with pain points (no-shows, phone tag, resume volume) before introducing Homebase.\n"
                ">*Why:* 75 dials, 38 pickups, 10 positive responses, 1 intake booked last week \u2014 reasonable early signal but customers are primed negatively. Changing the opener is the lowest-risk lever.\n"
                ">*Your action:* Track hang-up cohort separately \u2014 Usman is doing this, but make sure you\u2019re reviewing his call notes next session."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 2 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4ac Meeting 2 of 4 \u2014 Matan / Manan 1:1* (9:30 AM | Matan Chen Zion)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 4 \u2014 OEM onboarding: to-do item, not another banner*\n"
                ">*What:* Source claiming will live in a to-do checklist, NOT a banner. The trial banner already occupies that prime real estate \u2014 layering another banner there is wrong UX.\n"
                ">*Why:* To-do approach is visually distinct, eye-catching, and frames setup as actionable without cluttering the main UI. Framing: \u201cMake sure your implementation is set up properly\u201d (not \u201cConnect to Indeed\u201d \u2014 avoids sounding like a self-serve technical task).\n"
                ">*Your action:* \u2705 Already aligned with Matan. Next: confirm with Cindy today."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 5 \u2014 Two-phase OEM onboarding plan: SMS/email NOW, in-product to-do next week*\n"
                ">*What:* Short-term (this week) \u2014 SMS + email outreach using already-built templates; just needs Salesforce config. No engineering required. Medium-term (next week) \u2014 in-product to-do that books a Calendly call with Sean or Matan (round-robin).\n"
                ">*Why:* Speed. Templates are ready. Don\u2019t wait for the product to be built when you can start driving OEM setup calls today.\n"
                ">*Your action:* \u26a0\ufe0f *Follow up with Matan:* Did he get Ray\u2019s sign-off on the SMS/email templates? Was the goal EOD today. If not, nudge him."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 6 \u2014 Three-legged auth + source claiming: rep-assisted, done live on setup call*\n"
                ">*What:* Three-legged auth (OEM provides Indeed-linked email \u2192 Homebase passes email + AK code \u2192 OEM claims employer account + adds CC) is too complex for OEMs to self-complete. Rep walks them through it live.\n"
                ">*Why:* Low completion likelihood without hand-holding. Setup call jobs: (1) source claiming, (2) 3LO auth, (3) JD optimization, (4) calendar setup.\n"
                ">*Your action:* Make sure Sean is fully briefed (Matan\u2019s action to share Calendly link + source claiming doc)."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 3 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f527 Meeting 3 of 4 \u2014 Ugochukwu / Manan 1:1* (10:30 AM | Ugochukwu Nneji)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 7 \u2014 Calendly: in-product modal, not external link*\n"
                ">*What:* The Calendly booking will be embedded in-product (modal), not linked externally. Ugu flagged this is a known pattern (used in v2 migration and other flows). External link was assumed because hiring zero-state currently links out \u2014 but that\u2019s legacy.\n"
                ">*Why:* In-product embed gives you browser-level events for booking detection. External link gives you nothing to programmatically dismiss the to-do.\n"
                ">*Your action:* \u2705 Decision made. Ugu investigating Calendly embed event API."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 8 \u2014 To-do dismissal: trigger on booking confirmed, not modal close*\n"
                ">*What:* \u201cComplete Account Setup\u201d to-do is marked done when an OAM *actually books* a call \u2014 NOT when they close the modal without booking.\n"
                ">*Why:* Closing without booking = not done. The open question is *how* to detect the booking reliably (Calendly embed events, success toast trigger). Ugu will investigate. Race condition risk if modal closes before toast fires.\n"
                ">*Your action:* Follow up with Ugu on Calendly event findings \u2014 this is a blocker for dev spec."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 4 ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6ab Meeting 4 of 4 \u2014 Half-Baked Demos* (11:00 AM | Mostly canceled \u2014 low attendance)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 9 \u2014 Command AI: officially dead*\n"
                ">*What:* Confirmed dead. No further investment or evaluation.\n"
                ">*Your action:* If any eng is still evaluating Command AI, shut it down."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f7e2 *Decision 10 \u2014 Hiring onboarding Figma designs are mostly solid; two fixes needed*\n"
                ">*What:* \u201cComplete Account Setup\u201d to-do is directionally right. Two issues: (1) alignment is off, (2) byline copy needs work. Modal from the to-do is solid but too long \u2014 Ted to revise content.\n"
                ">*Your action:* \u26a0\ufe0f *Send modal copy to Ted* (your action). Fix alignment on the to-do. Both should be quick."
            )
        }
    },
    {"type": "divider"},

    # ── MASTER ACTION LIST ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f3af Your Master Action List \u2014 Jun 29 EOD*\n\n"
                "*\U0001f525 Do Today / Tonight:*\n"
                "\u2022 \u26a0\ufe0f Send modal copy to Ted (Hiring designs)\n"
                "\u2022 \u26a0\ufe0f Fix alignment on \u201cComplete Account Setup\u201d to-do in Figma\n"
                "\u2022 \u26a0\ufe0f Share Figma + spec doc access with Ugochukwu (he\u2019s never worked on to-dos)\n"
                "\u2022 \u26a0\ufe0f Add analytics events to to-do interactions + share list with Ugu for review\n"
                "\u2022 \u26a0\ufe0f Confirm Cindy alignment on designs (target: midday or EOD)\n"
                "\u2022 \u26a0\ufe0f Follow up: did Matan get Ray\u2019s sign-off on SMS/email templates?\n"
                "\u2022 \u26a0\ufe0f Follow up: did Matan share Calendly link + source claiming doc with Sean?\n"
                "\u2022 \u26a0\ufe0f Check Aventa \u2014 clarify Salesforce column requirements\n\n"
                "*\U0001f4c5 Carry-Forward from Last Week (still hot):*\n"
                "\u2022 \u2757 Draft v3 Q3 goals doc (3-bucket structure, share with Ray before John)\n"
                "\u2022 \u2757 Confirm Rami\u2019s email blast status (was due EOD Jun 25 \u2014 now overdue)\n"
                "\u2022 \u2757 Listen to Usman\u2019s call recordings \u2014 track excitement signals\n"
                "\u2022 \u2757 Decide comms agent ownership (take it or leave with Dana/Fadi/Davi)\n"
                "\u2022 Follow up with Ugu on Calendly embed event detection (blocker for dev spec)\n"
                "\u2022 Follow up with Jenna on SEO indexing guidance\n"
            )
        }
    },
    {"type": "divider"},

    # ── BOTTOM LINE ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f9e0 Bottom Line / Your Big Themes Today:*\n\n"
                "You made 10 clean decisions across 4 meetings \u2014 that\u2019s a lot of forward momentum for a Monday. "
                "The biggest moves: (1) shipping resume matching without waiting, (2) the two-phase OEM onboarding plan that gets SMS/email out the door *this week* with zero engineering, "
                "and (3) locking in the to-do-based source claiming UX. \n\n"
                "The \u201cPersonal Recruiter\u201d messaging retirement is also quietly important \u2014 it\u2019s a signal that V1 switcher resistance is real and the product/marketing team needs a cleaner upgrade narrative.\n\n"
                "Your most time-sensitive action: *send modal copy to Ted* and *share Figma + spec with Ugu* so engineering doesn\u2019t stall tomorrow morning. You\u2019ve got this, Manan \U0001f4aa"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest \u2014 Monday Jun 29, 2026",
    "blocks": blocks
}


def preview():
    print("\n=== SLACK MESSAGE PREVIEW (no token found) ===\n")
    try:
        sys.stdout.buffer.write(
            ("Channel: " + CHANNEL + "\n\n").encode("utf-8", errors="replace")
        )
        for b in blocks:
            if b.get("type") == "section":
                text = b.get("text", {}).get("text", "")
                sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
            elif b.get("type") == "header":
                text = b.get("text", {}).get("text", "")
                sys.stdout.buffer.write(("=== " + text + " ===\n\n").encode("utf-8", errors="replace"))
            elif b.get("type") == "divider":
                sys.stdout.buffer.write(b"---\n"
                )
    except Exception as e:
        print(f"Preview error: {e}")
    print("\n=== END PREVIEW ===")


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
                print(f"[OK] Message sent to {CHANNEL}: ts={body.get('ts')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')} | {body}")
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] URL error: {e.reason}")
        sys.exit(1)


if __name__ == "__main__":
    if TOKEN:
        print(f"Token found (starts with: {TOKEN[:10]}...). Sending to Slack...")
        send()
    else:
        preview()
