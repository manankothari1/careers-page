#!/usr/bin/env python3
"""Daily Decision Digest - Thu Jul 30, 2026 (PDT)"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "\U0001f305 Daily Decision Digest \u2014 Thursday, July 30, 2026", "emoji": True}
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": "Your chief of staff reviewed *2 meetings* today. Big structural day \u2014 major org news, product decisions locked, and your plate is full. Let\u2019s make sure nothing falls through the cracks. \u26a1"}]
    },
    {"type": "divider"},

    # ============================
    # BIG NEWS CALLOUT
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f6a8 *CONFIDENTIAL \u2014 Dana\u2019s Last Day is August 12* \U0001f6a8\nThat\u2019s *13 days from now.* Previously understood as \u201cend of September.\u201d The timeline has accelerated significantly. This isn\u2019t public yet \u2014 hold until the formal Slack announcement. But you need to act on succession *immediately*."}
    },
    {"type": "divider"},

    # ============================
    # MEETING 1
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f4cb *Meeting 1: Hiring Leads Standup* \u2014 8:45 AM PDT\n_Ray, Dana, Fadi, Matan, Jatin, Nelson, Jeff, Usman_"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 1 \u2014 Carbox FFH Opportunity: CLOSED*\n\u2192 Carbox is out of Kansas. The FFH opportunity is over. Matan enrolled affected accounts back into standard round-robin cadences last night. No action needed on your end \u2014 already handled. \u2705"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 2 \u2014 Talent Pool UI Card Format: LOCKED*\n\u2192 Card shows: *previous role + overall years of experience + location*\n\u2022 Changed \u201cyears in role\u201d \u2192 total years of experience (cleaner signal)\n\u2022 Rationale: \u201cline cook, 6 years, Mission District\u201d tells the full story at a glance\n\u2192 *Your action:* Generate 7\u20138 candidate profile variations via LLM (line cook, prep cook, etc.) with names + images (AI-generated or Pexels/Unsplash)"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 3 \u2014 Boost Upsell Copy: LOCKED*\n\u2022 \u274c Dropped: \u201c4x applicants\u201d (too vague/bold)\n\u2022 \u2705 New headline: *\u201cCut your hiring time\u201d*\n\u2022 Kept: \u201cGet premium placement on partner job boards\u201d + \u201cFlat fee, no surprises\u201d\n\u2022 Added: \u201cHard to fill role\u201d pill in *yellow* to signal why Boost is being recommended\n\u2022 Loading/invite animation: Fadi\u2019s read is that users fill in gaps and it reads as \u201call invited\u201d \u2014 ship it\n\u2192 Rationale: specificity + urgency over vague ROI claims; yellow pill primes the OEM that this role needs help"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 4 \u2014 Indeed Account Setup Copy + Flow: LOCKED*\n\u2022 Trigger: zero Indeed applicants by Day 3\n\u2022 To-do card: *\u201cConnect your account to Indeed. Indeed may have hidden your post.\u201d*\n\u2022 Interstitial: \u201cIndeed has started to hide free job posts from their feed. Connect your Homebase account to Indeed to ensure your posts aren\u2019t hidden.\u201d + \u201cConnect to Indeed\u201d CTA\n\u2022 Adding a *help article* explaining Indeed\u2019s policy in plain language (noindex \u2014 so Indeed can\u2019t crawl it)\n\u2022 Fadi pulling Indeed 3LO + account setup designs from code into Paper\n\u2192 *Your action:* Draft the Indeed policy help article (AI first pass, then edit). Link new Figma designs into Paper so everything lives in one place.\n\u2192 Rationale: don\u2019t bury the lead \u2014 \u201chidden post\u201d is alarming enough to drive action; help article gives OEMs context without putting it in the UI"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 5 \u2014 MBR Prep Structure: LOCKED*\n\u2022 Ray + Dana both *out next week*\n\u2022 Content owners confirmed:\n  \u2022 Jatin: notable shipped items + usage/adoption data\n  \u2022 Matan: ICP experiments, learnings, what\u2019s next\n  \u2022 Fadi: in-product growth experiments\n  \u2022 *You*: applicant side work, learnings, direction\n\u2022 Matan proposed 30-min alignment call with Dana before she sends bullet points \u2014 Dana to confirm\n\u2022 Dana sending compiled topic list + data sources\n\u2192 *Your action:* Prep your MBR section on applicant flow. Secure that alignment call with Dana + Matan ASAP given her Aug 12 exit."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e1 OPEN \u2014 Comms Agent: Manual Experiment Debate NOT Resolved*\n\u2022 Jatin is pushing for a manual test next week before building\n\u2022 Ray previously dismissed it (\u201cwe\u2019re not employing people to respond to messages\u201d) but Jatin reads that as not-firm\n\u2022 Meanwhile, Cena estimated 1.5\u20132 sprints for data engineering work (contracts for text storage + agent flow)\n\u2022 Ray recommended you + Jatin sit with Cena to *surface hidden assumptions and compress timeline*\n\u2022 Jatin committed to doing that today\n\u2192 *Your action:* Confirm with Jatin whether he synced with Cena. If assumptions were dropped, get the revised timeline. Decide: experiment first or build? This is your call."}
    },
    {"type": "divider"},

    # ============================
    # MEETING 2
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f512 *Meeting 2: Matan / Ray / Manan (Confidential)* \u2014 3:30 PM PDT\n_Ray, Matan, Manan_"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 6 \u2014 Dana\u2019s Exit Details Confirmed (CONFIDENTIAL)*\n\u2022 Last day: *August 12* (13 days)\n\u2022 Departure was somewhat mutual \u2014 Dana was unhappy and wanted to leave\n\u2022 Part of getting into \u201cgood flying formation\u201d before a new GM of Hiring joins\n\u2022 Team had too many people relative to the work\n\u2022 The grand experiment of splitting into two PM teams: *did not work*\n\u2192 Rationale: Better to restructure now and hand a clean org to the incoming GM than have them inherit confusion"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 7 \u2014 You Are Lead PM Starting August 12: LOCKED*\n\u2022 Single roadmap. One unified team.\n\u2022 *Under you:* Matan, Fadi, Jatin \u2014 all reporting into one org\n\u2022 No more split between two engineering teams\n\u2022 New GM of Hiring will *inherit* this structure, not re-split it\n\u2192 Rationale: Simplify the org before the new GM arrives so they\u2019re not walking into ambiguity. You\u2019re the connective tissue.\n\u2192 *Your action:* You have 13 days to get up to speed on *everything* Dana owns. ICP experiments are priority #1 \u2014 lean on Matan now. Page Templates handoff must start this week."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 8 \u2014 Rami (DS) is Temporary: Make the Business Case to Ted*\n\u2022 Ted is taking on more leadership scope after Kan\u2019s departure\n\u2022 Ted pulled back from day-to-day hiring involvement \u2014 Rami\u2019s time on team likely temporary\n\u2022 Ray\u2019s steer: *go directly to Ted* with a business case (applicant quality + Marketplace impact)\n\u2192 *Your action:* Talk to Ted ASAP. Don\u2019t wait. Rami is too valuable to lose without a fight \u2014 especially with JD quality experiments and talent pool email work in flight."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f7e2 DECISION 9 \u2014 Jubs as Sales Partner: Established*\n\u2022 Jubs brought in as stronger product partner on the sales side\n\u2022 Matan already had a 1-hour call; *weekly cadence established*\n\u2022 Matan considering Denver trip in ~1 month for in-depth sales team sessions\n\u2022 Ray adding Jubs to standups\n\u2192 Rationale: Usman has been passive \u2014 Ray had a direct performance conversation. Jubs is the stronger signal amplifier right now. Build this relationship proactively."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\U0001f534 FLAG \u2014 Usman: Performance Issue on Ray\u2019s Radar*\n\u2022 Ray has had a direct performance conversation with Usman\n\u2022 Needs to step into proactive sales manager role or \u201cwon\u2019t bode well\u201d\n\u2022 For now: Jubs is your stronger sales partner\n\u2192 Watch: don\u2019t over-invest in Usman-dependent work until you see the behavior change"}
    },
    {"type": "divider"},

    # ============================
    # YOUR ACTION ITEMS
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f3af *MANAN\u2019S ACTION ITEMS \u2014 Today + Immediate*"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f525 *URGENT (Aug 12 = 13 days):*\n1\ufe0f\u20e3 *Start Dana succession plan NOW* \u2014 ICP experiments, Page Templates handoff. Schedule a knowledge transfer this week.\n2\ufe0f\u20e3 *Talk to Ted about Rami* \u2014 business case: applicant quality + Marketplace impact. Do not wait.\n3\ufe0f\u20e3 *MBR content* \u2014 Secure alignment call with Dana + Matan before Dana goes heads-down. You\u2019re on applicant side."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f4cb *THIS SPRINT:*\n4\ufe0f\u20e3 *Generate talent pool candidate profiles* \u2014 7-8 role variations (line cook, prep cook, etc.), names + images. LLM prompt.\n5\ufe0f\u20e3 *Write Indeed help article* \u2014 plain language, noindex. AI first pass then edit. Link into Paper.\n6\ufe0f\u20e3 *Link Figma designs into Paper* \u2014 Indeed 3LO + Boost modal + account setup all in one place.\n7\ufe0f\u20e3 *Comms agent: confirm Cena sync* \u2014 Did Jatin meet with Cena today? Get revised timeline. Make the experiment-vs-build call.\n8\ufe0f\u20e3 *Franchise ticket* \u2014 Still not written from the Jul 29 Indeed call. This is a P0 that\u2019s been open 2 days.\n9\ufe0f\u20e3 *Scooters follow-up* \u2014 Email to Olivia/Maria/Lacey. Still open.\n\U0001f51f *Carlo Harness/OpenSpec* \u2014 16+ days overdue. This needs a direct conversation, not a Slack message."}
    },
    {"type": "divider"},

    # ============================
    # WATCH LIST
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f6a7 *WATCH LIST \u2014 Still Burning*\n\u2022 \U0001f534 *422 Job Publishing Errors* \u2014 Day 21. Jatin on RCA. Still no resolution.\n\u2022 \U0001f534 *Carlo Harness/OpenSpec* \u2014 16+ days overdue. Management issue.\n\u2022 \U0001f7e1 *Fadi Boost modal Figma* \u2014 4 days overdue since Jul 27. Locked today\u2019s Boost copy \u2014 now ship the Figma.\n\u2022 \U0001f7e1 *Talent Pool Outreach: open questions* \u2014 Databricks\u2192SMS column contract + message storage. Carlo on rake task (1-2 days). Resolve by end of week.\n\u2022 \U0001f7e1 *Matan comms doc* \u2014 Still open. Sonia still blocked.\n\u2022 \U0001f7e1 *Juan Sanchez email issue* \u2014 Still open. Follow up.\n\u2022 \U0001f7e1 *Izzy + Tanner API contract* \u2014 Role/salary reco alignment still needed.\n\u2022 \u26aa *SBA*: watch unassigned grid P1 data (launched Jul 27; friendly testing was negative)\n\u2022 \u26aa *Comms agent ownership (Bob+Jonathan sync)*: sync was Jul 29 3pm \u2014 no Granola notes found. Confirm outcome.\n\u2022 \u26aa *Dana succession* \u2014 Aug 12. Page Templates hand-off. NO PLAN EXISTS. Clock is ticking.\n\u2022 \u26aa *Usman candidate email experiment* \u2014 results still unchecked"}
    },
    {"type": "divider"},

    # ============================
    # CLOSING
    # ============================
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\U0001f4aa *You crushed it today, Manan.* Big org news absorbed, product decisions locked, and the team is moving. The Aug 12 transition is going to be a sprint \u2014 but you\u2019ve got the full picture now and you know exactly what needs to happen. Go get it. \U0001f680"}
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": "Chief of Staff Digest \u2022 Jul 30, 2026 \u2022 2 meetings reviewed"}]
    }
]

def preview():
    print("=" * 70)
    print("SLACK PREVIEW: Daily Decision Digest - Jul 30, 2026")
    print("=" * 70)
    for block in blocks:
        btype = block.get("type", "")
        if btype == "header":
            sys.stdout.buffer.write(("\n## " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif btype == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n\n").encode("utf-8", errors="replace"))
        elif btype == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write(("[ctx] " + el.get("text", "") + "\n").encode("utf-8", errors="replace"))
        elif btype == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
    print("=" * 70)

def send():
    payload = json.dumps({
        "channel": CHANNEL,
        "text": "Daily Decision Digest - Thu Jul 30, 2026",
        "blocks": blocks
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("SUCCESS: message delivered to", CHANNEL)
                print("ts:", body.get("ts"))
            else:
                print("SLACK ERROR:", body.get("error"))
                print("Full response:", json.dumps(body, indent=2))
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print("HTTP ERROR:", e.code, e.reason)
        print(e.read().decode("utf-8"))
        sys.exit(1)
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)

if __name__ == "__main__":
    if not TOKEN:
        print("NOTE: No SLACK_TOKEN found. Printing preview instead.")
        print("To enable delivery: add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets")
        preview()
        sys.exit(0)
    send()
