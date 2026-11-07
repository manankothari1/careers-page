#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Friday, November 6, 2026 PST
Manan Kothari | PM at Homebase | Slack DM: D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Friday Nov 6 Debrief -- Chief of Staff Report",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day Grade: A-* | Today was one of the best Fridays in a while. "
                "Sprint closed strong, the demos were real and working, and the company "
                "all-hands had genuinely great news. Two things keep it from an A: "
                "Fadi's departure timeline is now a live risk, and Jatin reversed on "
                "Nihilus -- virtual calendar is a *blocker* now, not parallel work. "
                "You need to reconcile that with Skye before Monday.\n\n"
                ":pushpin: *THEME: SPRINT CLOSED STRONG -- FADI'S CLOCK IS TICKING -- FOUNDATION BEFORE FEATURES*"
            )
        }
    },
    {"type": "divider"},
    # ---- MEETINGS ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Meetings Today (5)*\n"
                "8:30am -- SB Standup & Planning (workspace) | "
                "11:00am -- Hiring Demo + Sprint Retro | "
                "11:00am -- Company Sprint Show & Tell | "
                "12:30pm -- Linda / Bobby Hill (customer) | "
                "1:00pm -- Jatin / Manan (sprint planning)"
            )
        }
    },
    {"type": "divider"},
    # ---- SECTION 1: BIG DECISIONS ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:zap: BIG DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Magic Link is now at 40/60 -- CONFIRMED WORKING :white_check_mark:*\n"
                "What: Gbolade bumped OTP magic link from 20% to a 40% variant / 60% control split. "
                "Live demo failed on staging but Datadog and Amplitude confirmed it's live in prod -- "
                "4 links sent, 3 verified. Send success rate holding.\n"
                "Why: 20% rollout data was clean enough to push forward. Plan is to keep climbing.\n"
                "Action: *Watch Datadog + Amplitude* over the weekend for any fraud or delivery anomalies. "
                "IBK sent a Loom of the flow -- review it."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Facebook Apply SLO recovered to 92% -- Temporarily safe :green_heart:*\n"
                "What: Two root causes fixed -- (a) retry loop inflating error rate patched, "
                "(b) Meta raised our rate limit from 240 to 300 (team's highest-ever usage was 240). "
                "Meta is in a code freeze until end of Thanksgiving.\n"
                "Why: Jatin talked directly to Lisa at Meta and got the limit raised.\n"
                "Decision: Spike Facebook Easy Apply in sprint 26-23, build it in 26-24. "
                "Jatin is confident on delivery by end of November (not December 15 as previously flagged).\n"
                "Risk: Limit is temporary; Easy Apply launch will push volume toward new ceiling."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Indeed Disposition Sync is LIVE -- 2,000+ statuses sent :rocket:*\n"
                "What: Tiger shipped disposition sync to Indeed. 2,000+ disposition statuses "
                "sent successfully. SLO monitoring now in place.\n"
                "Decision: Tiger to add a breakdown by disposition type to the Indeed detailed dashboard "
                "(Manan's ask, confirmed by Tiger)."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Sprint 26.22 closed: 93% completion, 105 tickets done :trophy:*\n"
                "What: Strong sprint close. 2 of 4 Q4 spikes complete. Remaining 2 "
                "(screener toggle/matching + purge job resume requirements) go to Bob "
                "once he finishes breaking down scheduling work.\n"
                "Sprint retro format improvements locked:\n"
                " -- Sprint goal to be defined at kickoff + self-rated at close (Skye + Manan to implement)\n"
                " -- Scope growth slide to separate planned growth vs. unplanned pull-ins (Manan's ask)\n"
                " -- Points metric to be included in outcomes slide (Jatin to reissue)\n"
                " -- Orca work moved to a separate project; hiring team is not the Orca team\n"
                "Action: *Send Bob your priority list* for the remaining 2 spikes (screener toggle + purge job resume)."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. NIHILUS REVERSAL -- Virtual calendar build is now a BLOCKER :rotating_light:*\n"
                "What: In Thursday's vision session, the virtual calendar migration was described as "
                "parallel work (not blocking scheduling features). Today in your 1pm with Jatin, he "
                "reversed: 'I think it'll be a blocker.' Build the virtual calendar foundation first, "
                "THEN build scheduling features on top. Nihilus stays in the OAuth corner in the interim. "
                "Possibly rip out Nihilus entirely in Q2.\n"
                "Why: Moving fast on scheduling features before the foundation is set creates rework risk.\n"
                "Risk: This materially changes the scheduling roadmap sequencing you need to present Monday.\n"
                "Action: *Reconcile this with Skye before the Monday Lookahead.* "
                "Thursday's session implied non-blocking; today Jatin said blocking. Get alignment."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Indeed Job Reactivation Edge Case -- Release strategy decided*\n"
                "What: OEMs reactivating jobs (within 21 days) that were previously flagged on Indeed "
                "would perpetuate the problem -- same job ID = same flagged job. "
                "Proposed fix: check if previous job had *zero Indeed applicants* as a signal that "
                "it was flagged, and if so, use a new post ID instead of reactivating.\n"
                "Decision: Tiger to add this check quickly next week before the broader posting work releases. "
                "Release with this bandaid, follow up with more robust logic.\n"
                "Jatin's estimate: once Indeed responds to the 3 questions, ~1 week to delivery including testing.\n"
                "Action: *Tiger next week (early): add zero-applicant check.* "
                "Loop Jatin in once Indeed responds. You still need to check whether the email to Rachel was sent."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Q4 Roadmap Trimmed -- 3 items officially punted*\n"
                "What: Manan and Skye reviewed the roadmap this week and cut:\n"
                " -- Unified candidate messaging -- PUNTED (future quarter TBD)\n"
                " -- Background checks (billing + legal name) -- PUNTED to Q1\n"
                " -- Smart deal breakers -- PUNTED\n"
                "Why: Team capacity with Carlo + Malcolm out, and scheduling must be the priority.\n"
                "Action: Confirm these cuts are reflected in Linear. "
                "Also: *Match Co-Build must fit in sprint 26-25* (Jatin's requirement). "
                "No eng assigned yet. Add to Monday Lookahead as a resourcing discussion."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Company all-hands: ARR $106M, New CFO, CTV Campaign live :bar_chart:*\n"
                "What: October ARR at $106M, up 14% YoY, just under plan. Added $2.5M in October "
                "(strong Cashout + TMAP). CTV campaign launched on Peacock, Tubi, Paramount+ via MNTN -- "
                "cost per owner signup improving week over week, on track to double signups 3rd consecutive week.\n"
                "Leadership: *Michael Washinushi joins as CFO (Day 5)* -- previously FreshBooks, based in Toronto. "
                "People team now reports to him. *Kate Kodesh departing* after 2.5 years.\n"
                "Also shipped: Designbase icon overhaul complete (Huge Icons, 170+ assets replaced). "
                "Homebase Releases site live at joinhomebase.com/releases."
            )
        }
    },
    {"type": "divider"},
    # ---- SECTION 2: CRITICAL FLAGS ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CRITICAL FLAGS -- Act on these*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*FLAG 1: FADI MAY BE LEAVING -- 3 weeks :skull:*\n"
                "On the 1pm call with you and Jatin, Fadi joined and said: "
                "'What I want to do before I leave is get on this scheduling shit ASAP so you guys are in a good spot' "
                "and 'I've got 3 weeks to do this.'\n"
                "If Fadi (your only designer) is departing, this is a *critical capacity crisis* -- "
                "Malcolm is already out through December, and scheduling design is entirely on Fadi right now.\n"
                "Action: *Talk to Fadi directly today or over the weekend.* What is his timeline? "
                "Is there a handoff plan? Can he get the full end-to-end scheduling design done in 3 weeks? "
                "Skye needs to know ASAP if she doesn't already."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*FLAG 2: RACHEL EMAIL / INDEED -- Confirm it was sent*\n"
                "The Demo meeting said 'still awaiting a response from Indeed.' "
                "The watch list had this as UNSENT as of yesterday. "
                "Confirm with Tiger whether the email to Rachel (3 questions on job requisition ID, "
                "repost window, expiration date field) was actually sent. If not, *send it now.* "
                "Day 3+ since the questions were finalized."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*FLAG 3: JD RULES FOR DIVIJ -- Day 13 overdue, he is IDLE*\n"
                "1 hire ~30d = vanilla; 2+ hires = 'multiple positions available'; "
                "urgency <=2wk = 'urgently hiring'. TBD: ASAP definition + posted vs activated date.\n"
                "Action: *Send these rules to Divij this weekend.* He cannot move forward without them."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*FLAG 4: Skye / OEM Goals + Prompt Chips -- EOD today*\n"
                "Skye flagged that you should sync with Fadi about job creation as part of "
                "upcoming OEM goals work and whether prompt chips changes will persist or change. "
                "You said you'd get clarity from Skye before EOD today.\n"
                "Action: *Message Skye now if you haven't already.*"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*FLAG 5: 2029 Vision one-pager -- DAY 22+ overdue*\n"
                "Board meeting opened Oct 15. Fadi submitted his. John is waiting.\n"
                "Action: This has to happen this weekend."
            )
        }
    },
    {"type": "divider"},
    # ---- SECTION 3: WEEKEND BATTLE PLAN ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: WEEKEND BATTLE PLAN -- Priority Order*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Today (tonight):*\n"
                "1. Talk to Fadi -- confirm his departure timeline and what he can design before he leaves\n"
                "2. Confirm Rachel email status with Tiger -- if unsent, draft and send tonight\n"
                "3. Connect with Skye on OEM goals + prompt chips question (before EOD)\n\n"
                "*Saturday:*\n"
                "4. Send JD rules to Divij (Day 13 overdue) -- 20 minutes, write them out and hit send\n"
                "5. Write Scheduling Ideal State doc -- Malcolm is gone, you are now the keeper of this vision. "
                "The virtual calendar decision changes the sequencing. Update accordingly.\n"
                "6. Send Bob priority list for screener toggle + purge job resume spikes\n\n"
                "*Sunday:*\n"
                "7. 2029 vision one-pager -- *do this. It's day 22+.*\n"
                "8. Write Interview Confirmation BDD spec -- Jatin + Bob cannot start until you do\n"
                "9. Define scheduling priority sequencing for Monday Lookahead "
                "(must reconcile Nihilus-as-blocker with Skye before this meeting)"
            )
        }
    },
    {"type": "divider"},
    # ---- SECTION 4: WATCH LIST ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: UPDATED WATCH LIST*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":green_circle: *MAGIC LINK*: 40/60 (up from 20%). Working in prod. Watch fraud signals.\n"
                ":green_circle: *FACEBOOK*: SLO at 92%. Temporarily safe (limit 300, team max was 240). "
                "Spike in 26-23, build in 26-24.\n"
                ":yellow_circle: *INDEED RACHEL EMAIL*: Sent or awaiting -- confirm with Tiger.\n"
                ":red_circle: *FADI DEPARTURE*: NEW. 3-week window. Confirm and escalate to Skye.\n"
                ":red_circle: *JD RULES FOR DIVIJ*: Day 13 overdue. Divij is idle.\n"
                ":red_circle: *INTERVIEW CONFIRMATION BDD*: Overdue. Jatin + Bob are blocked.\n"
                ":red_circle: *2029 ONE-PAGER*: Day 22+ overdue. John is waiting.\n"
                ":red_circle: *SCHEDULING IDEAL STATE DOC*: Malcolm is gone. This is on you.\n"
                ":yellow_circle: *NIHILUS*: Virtual calendar is now a blocker per Jatin. "
                "60-day cancellation notice due ~late November. Skye needs to draft parity plan.\n"
                ":yellow_circle: *ENTITLEMENTS*: At 25%. Adam blocked on PRs 1210, 1214, 1212.\n"
                ":yellow_circle: *SINA CAPACITY CONFLICT*: Still unresolved. Get straight answer from Jatin Monday.\n"
                ":yellow_circle: *MATCH CO-BUILD*: Must fit in 26-25. No eng assigned. Monday Lookahead.\n"
                ":yellow_circle: *JATIN CAREER PIVOT*: Martin asked if Jatin wants to go hands-on EM again. "
                "Not decided. Would reshape how much he can manage the hiring pod."
            )
        }
    },
    {"type": "divider"},
    # ---- CUSTOMER SIGNAL ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:busts_in_silhouette: Customer Signal: Bobby Hill / Tunnels of Moosejaw*\n"
                "26-year-old tourist attraction in Saskatchewan. 30-35 staff. Using Homebase 4-5 years. "
                "Very satisfied ($500/year, doesn't even remember the price). "
                "Pain points: (1) *break rounding* -- breaks scheduled 1hr but often 57min or 1:01, "
                "requires manual correction each approval cycle; (2) *clock-out reminders* -- "
                "wants a location-aware ping at end of shift. Linda passing both to the product team."
            )
        }
    },
    {"type": "divider"},
    # ---- CLOSER ----
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*One more thing before you close your laptop:*\n"
                "Jatin, IBK, and Tiger all gave you shoutouts in the sprint retro today. "
                "IBK: 'Manan for raising the product bar.' Tiger: 'Manan for navigating complex product scenarios.' "
                "Manan: 'Jatin for new structure and process that has sped things up rather than slowed things down.'\n\n"
                "You are building something real. The sprint close numbers back it up. "
                "Now get through the weekend work and walk into Monday with a plan.\n\n"
                "_Your chief of staff, signing off for the week._"
            )
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": BLOCKS,
    "text": "Friday Nov 6 Chief of Staff Debrief -- Day Grade A-"
}

def preview():
    sys.stdout.buffer.write(
        b"\n=== PREVIEW: FRIDAY NOV 6 CHIEF OF STAFF DIGEST ===\n\n"
    )
    for block in BLOCKS:
        if block.get("type") == "section":
            text_obj = block.get("text", {})
            if text_obj.get("type") == "mrkdwn":
                line = text_obj.get("text", "")
                sys.stdout.buffer.write((line + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            text_obj = block.get("text", {})
            line = text_obj.get("text", "")
            sys.stdout.buffer.write(("=== " + line + " ===\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n\n")
    sys.stdout.buffer.write(b"=== END PREVIEW ===\n\n")


def send(token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"[SUCCESS] Message sent to {CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {result.get('error', 'unknown')}")
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")


if __name__ == "__main__":
    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN")
    )
    preview()
    if token:
        print(f"[INFO] Token found ({len(token)} chars). Sending to Slack...")
        send(token)
    else:
        print("[INFO] No SLACK_TOKEN found -- preview mode only. Add token in Cursor Dashboard > Cloud Agents > Secrets.")
