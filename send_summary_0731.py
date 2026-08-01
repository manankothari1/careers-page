#!/usr/bin/env python3
"""
Friday EOW Summary - July 31, 2026
Chief of Staff daily digest for Manan Kothari
"""
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
            "text": "Friday Wrap  |  EOW Summary  |  July 31, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! No meetings today, which honestly feels earned after the week you just had. So here's your full week-in-review: every decision locked, every action item, and what's sitting on your plate going into Monday. Let's close the week clean."
        }
    },
    {"type": "divider"},
    # --- ORG NEWS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*CONFIDENTIAL ORG NEWS*\n:rotating_light: *Dana's last day is August 12.* That's 12 days from now. Departure was mutual - part of getting into 'good flying formation' before the new GM of Hiring joins. Starting Aug 12: you're sole Lead PM, single roadmap, one unified team. Matan, Fadi, and Jatin all under you. No more team split. The grand experiment of two PM teams did not work. The new GM will inherit your structure.\n\n:warning: *ICP experiments* - Matan is your bridge while Dana is out. Get up to speed NOW. Dana is off the week of Aug 7, so the clock is ticking."
        }
    },
    {"type": "divider"},
    # --- DECISIONS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*DECISIONS LOCKED THIS WEEK*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*MON Jul 27*\n:white_check_mark: *Role Rec Arch LOCKED* - Hiring package (not HPLM). Single combined gRPC endpoint for role rec + normalization. ~3-4s latency. Role normalization bucket added as top output for Tanner. Rationale: one endpoint = simpler contract, fewer failure points.\n:white_check_mark: *FFH Candidate Preview Design LOCKED* - 3 cards, fake data + real neighborhood names, list view over map, min 10/MSA, 2s auto-expand animation, Boost CTA after invites sent, WhatsApp-style photos. Rationale: shows signal without real PII friction.\n:white_check_mark: *SBA LAUNCHED* - Two-flag arch, pulsing icon. Watch the unassigned grid for P1 data."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*TUE Jul 28*\n:white_check_mark: *Candidate Matching Thresholds SHIPPED* - Resume 0.8 / screener 0.5 / combined 0.4+0.3. Net: 13K flagged from 52K applicants. Ship + learn; don't over-optimize before launch.\n:white_check_mark: *Comms Agent = Experiment First, Build Second* - Validate manually (team texts candidates from personal phones) BEFORE building. Product eng estimate: ~2 months POC with 1 backend eng. Hypothesis must be proven first. Rationale: data/DS vs product eng ownership misalignment = blocker; validate before investing.\n:white_check_mark: *Competency Score Normalization = Global Percentile First* - Simpler. Role-level v2 comes later. Ted scoping timeline with Divij."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WED Jul 29*\n:white_check_mark: *Franchise Source Naming LOCKED* - Unique ID per franchise (not city/state). Prevents cross-franchise duplicate flags + enables per-franchise Indeed accounts.\n:white_check_mark: *Scooters Trust & Safety Ticket* - Olivia Anderson (Indeed CSM) submitted. Covers all 300+ locations in one shot. Root cause was TalentReef still on careers page. Need Lacey's written confirmation.\n:white_check_mark: *Talent Pool Outreach GREENLIT* - Post hard-to-fill role → OEM sees modal with nearby candidate count + rotating obfuscated profiles → edits pre-filled SMS → Homebase sends via admin CSV. MVP: 1-2 days. Raw text only. Carlo on the rake task.\n:white_check_mark: *Sprint Sizing Ritual LAUNCHED* (Jatin's initiative) - S<3d, M~1wk, L=full sprint.\n:white_check_mark: *Monday Reassessment Queue LOCKED* - 3 projects: Job page SEO fixes, No Indeed Applicants by Day 3 (reuses Carlo's work), Franchise job posting.\n:white_check_mark: *Indeed Renew Jobs Strategy VALIDATED* - Push timestamp forward, never close/repost. ATS jobs have NO 30-day timer. Reposting within a few weeks = 'job copy' flag = visibility hit. Keep jobs open for always-hiring roles."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*THU Jul 30*\n:white_check_mark: *Carbox FFH ENDED* - Accounts back to round-robin (1/3, 1/3, 1/3). Matan enrolling affected accounts into cadences.\n:white_check_mark: *Talent Pool Card Format LOCKED* - Previous role + total YoE + location. (Changed 'years in role' to total YoE - 'line cook, 6 years, Mission District' tells the full story.)\n:white_check_mark: *Boost Copy LOCKED* - 'Cut your hiring time' (dropped '4x applicants'). Kept: 'Get premium placement on partner job boards' + 'Flat fee, no surprises'. Added: 'Hard to fill role' yellow pill.\n:white_check_mark: *Indeed Account Setup Copy LOCKED* - To-do card: 'Connect your account to Indeed. Indeed may have hidden your post.' + interstitial explaining Indeed's free post policy + noindexed help article.\n:white_check_mark: *MBR Prep Owners LOCKED* - Jatin: shipped items + data; Matan: ICP experiments + learnings; Fadi: in-product growth; Manan: applicant side. Ray + Dana out next week.\n:white_check_mark: *Manan = Sole Lead PM starting Aug 12* - See ORG NEWS above."
        }
    },
    {"type": "divider"},
    # --- P0 ACTION ITEMS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*YOUR P0 ACTION ITEMS FOR NEXT WEEK*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *URGENT - Dana Succession (12 days)*\nNo succession plan exists. Page Templates handoff must start NOW. Get Matan up to speed on everything Dana owns. Schedule a Dana + Matan + Manan alignment call before Dana is out Aug 7.\n\n:fire: *Talk to Ted about Rami* - Rami's involvement on the hiring team is likely temporary (Ted pulling back after Kan's departure). You need to make a direct business case to Ted: applicant quality + Marketplace impact. Do this before Ted makes a decision for you.\n\n:fire: *Carlo Direct Conversation* - *17+ days overdue* on Harness/OpenSpec. This is a management issue. Have the conversation now.\n\n:fire: *422 Job Publishing Errors* - Day 22. Jatin is on the RCA. Check in Monday.\n\n:warning: *Generate Talent Pool Candidate Profiles* - Use LLM to create 7-8 role variations (line cook, prep cook, etc.) with names, profiles, and images (AI-gen or Pexels/Unsplash). Fadi needs these to finish the UI.\n\n:warning: *Write Indeed Help Article* - Plain-language explanation of Indeed's free post flagging policy. Source from Indeed's free vs. sponsored jobs article, rewrite for OEMs, noindex so Indeed can't crawl it. AI first pass is fine.\n\n:warning: *Link Figma to Paper* - New Boost modal Figma + Indeed account setup designs need to live in Paper (Fadi is pulling existing designs from code into Paper too).\n\n:warning: *MBR Content* - Your section: applicant side work, learnings, direction. Ray + Dana out, so this is yours to own. Dana to send compiled topic list; align with Matan before she does.\n\n:warning: *Get up to speed on ICP Experiments* - Matan has been running these with Dana. Dana out Aug 7. This transition is now critical. Block time with Matan this week.\n\n:warning: *Matan Comms Doc Review* - Sonia is blocked on building until you review Matan's doc. Still open. Do this Monday.\n\n:warning: *Scooters Follow-up Email* - Send to Olivia, Maria, Lacey. Confirm TalentReef migration path and next steps for franchise Indeed accounts."
        }
    },
    {"type": "divider"},
    # --- OPEN QUESTIONS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*OPEN QUESTIONS & UNRESOLVED*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":question: *Comms Agent Manual Experiment* - Jatin wants to run it next week (team texts candidates from personal phones). Ray initially shot it down but Jatin read it as non-conviction. Cena estimated 1.5-2 sprints for data eng. Ray wants you + Jatin to sit with Cena to surface hidden assumptions. Did the Jatin/Cena sync happen Jul 30? And the Bob+Jonathan ownership sync (Jul 29 3pm) - outcome still unknown.\n\n:question: *Fadi Boost Modal Figma* - 5 days overdue since Jul 27. What's the blocker?\n\n:question: *Franchise Ticket* - 3+ days open from the Indeed call. Who's owning the write-up?\n\n:question: *Juan Sanchez* - Still sending emails outside the proper flow. Follow-up still open.\n\n:question: *Usman Experiment Results* - Candidate email experiment results still unchecked.\n\n:question: *Izzy + Tanner API Contract* - Role/salary reco alignment still needed."
        }
    },
    {"type": "divider"},
    # --- WATCH LIST ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*WATCH LIST*\n• :large_red_circle: Dana succession: Aug 12 - 12 days. No plan. Start Monday.\n• :large_red_circle: Carlo: 17+ days overdue. Direct convo needed.\n• :large_red_circle: 422 errors: Day 22. Jatin on RCA.\n• :large_yellow_circle: SBA: launched Jul 27, watch unassigned grid P1 data (friendly testing was negative).\n• :large_yellow_circle: Talent Pool: GREENLIT. Carlo on rake task (1-2 days). Databricks → SMS column contract + message storage still open.\n• :large_yellow_circle: Rami: make the business case to Ted before the window closes.\n• :large_yellow_circle: Comms Agent: resolve ownership + confirm Cena assumptions before Jatin runs the manual experiment.\n• :large_yellow_circle: Matan/Jubs/Denver trip: ~1 month out. Matan to prep shared vision first."
        }
    },
    {"type": "divider"},
    # --- METRICS PULSE ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*METRICS PULSE*\n• FFH D5 zero-applicant rate: *41%* (Q3 target: <10%)\n• Line cook jobs healthy by D30: *~7%* (Q3 target: 50%)\n• Healthy job rate: *30%* (target: 80%)\n• OEM boost rate: *5.7%* (up from 2.9% in May)\n• 422 errors: *146 locations* since Jul 9\n• ARR: *$650K+* (from $450K Jan 2026) :muscle:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Genuinely, this was a massive week. You shipped candidate matching, greenlit Talent Pool Outreach, locked Boost copy, locked Indeed Account Setup, navigated a huge org announcement, AND set up the team structure for a clean handoff. That's a lot. Take the weekend, come back fresh Monday - you have 12 days to execute the Dana succession and it starts then. You've got this. :rocket:"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Friday EOW Summary | July 31, 2026",
    "blocks": blocks
}

def send_slack(token, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

def preview(payload):
    out = "\n=== SLACK MESSAGE PREVIEW ===\n"
    for block in payload.get("blocks", []):
        if block.get("type") == "header":
            out += f"\n### {block['text']['text']} ###\n"
        elif block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            out += f"\n{text}\n"
        elif block.get("type") == "divider":
            out += "\n" + "-" * 60 + "\n"
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

if token:
    print("Sending Slack message...")
    result = send_slack(token, payload)
    if result.get("ok"):
        print(f"Sent successfully! ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        print("Full response:", json.dumps(result, indent=2))
        preview(payload)
else:
    print("No SLACK_TOKEN found. Preview mode:")
    preview(payload)
