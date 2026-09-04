#!/usr/bin/env python3
"""Daily Chief of Staff digest — Sep 3 2026 (Thu PDT)"""

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
            "text": "Chief of Staff Daily Digest — Thursday, Sep 3 2026"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Day Grade: A* :star::star::star::star::star:\n*4 meetings. Big day, Manan. You shipped decisions across 4 workstreams, unblocked two major product paths, and got an experiment into the wild. You're playing offense heading into your OOO. Let's lock it down.*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":dart: *TODAY'S THEME:*\nINDEED EXPERIMENT LIVE (20% ROLLOUT) · 120-DAY JOB FLOW ARCHITECTURE LOCKED · TALENT POOL SMS OPT-IN GREENLIT · LINEAR RESET INITIATED · JOBTARGET VENDOR EVAL OPENED"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *MEETING 1 — JobTarget Vendor Eval* (9:00 AM · Tyler Calvey, t.calvey@jobtarget.com)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*What it is:* JobTarget = job distribution platform across 20K+ job sites (Indeed, LinkedIn, ZipRecruiter, niche boards, etc.). Integrates with 90-100 ATS systems via XML feed or API. Embedded as iframe or white-labeled.\n\n*Key Decisions:*\n• :white_check_mark: *EXPLORE AS DISTRIBUTION CHANNEL* — Programmatic campaigns allocate budget to top-performing boards for role/location. Potentially powerful complement to EarnIn/JobCase XML strategy already greenlit.\n• :white_check_mark: *WHITE-LABELING IS ON THE TABLE* — Tyler connecting you with Michael Doenmire (partnerships) to scope feed terms, kickback structure, and white-label feasibility.\n• :white_check_mark: *FEED COST LIKELY FREE* (to be confirmed) — Standard ATS partner model suggests revenue share or traffic kickbacks rather than feed charges.\n\n*Why it matters:* You need distribution diversity badly — Indeed feed has been suspended since Aug 25 (Day 9). JobTarget gives you a single integration that fans out to 20K boards. The programmatic model means spend optimization happens automatically.\n\n*Action Items:*\n• :arrow_right: *YOU (Manan):* Review JobTarget one-pager when Tyler sends it\n• :arrow_right: *Tyler/JobTarget:* Intro to Michael Doenmire (partnerships) to discuss feed terms + white-label options"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *MEETING 2 — Linear Review* (9:30 AM · Skye Laudari, Jatin Bhandari)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Decisions:*\n• :white_check_mark: *LINEAR = EXECUTION TRACKING, NOT ROADMAP PLANNING* — Skye locked this: Linear is bottom-up (tickets → Gantt); roadmap/strategy lives in Google Docs. Kills the two-sources-of-truth risk.\n• :white_check_mark: *JATIN OWNS LINEAR HYGIENE* — ~170 projects visible, many with zero issues. Delete automation artifacts, archive stale tickets. Jatin confirmed ownership per Ankit.\n• :white_check_mark: *SLACK CHANNEL STRATEGY TBD* — Skye, Fatty, and Manan to align. Current debate: project-specific channels vs. consolidating in hiring-EPD. Jatin's preferred model: all ICs in EPD channel.\n• :white_check_mark: *ENGINEERS IN STANDUPS* — Skye wants engineering included for visibility. Thursday standup-free day floated to protect heads-down time.\n• :white_check_mark: *END-OF-SPRINT SHOW-AND-TELL INCOMING* — Sales team attends. Proactive release notes. AI surfaces past customer feedback when feature ships.\n• :white_check_mark: *REPO ACCESS FOR CS/SALES VIA AI AGENT* — Reduces inbound PM drain. You discussed with Fatty last week. Now formally on the roadmap.\n\n*Action Items:*\n• :arrow_right: *YOU (Manan):* Explore repo access for customer support + sales via AI agent\n• :arrow_right: *Skye:* Connect GitHub integration in Linear settings (enables codebase querying via Linear agent)\n• :arrow_right: *Jatin:* Drive Linear hygiene sweep — delete runaway automation projects, archive stale tickets\n• :arrow_right: *Skye + Fatty + Manan:* Align on Slack channel strategy\n• :arrow_right: *Group:* Revisit Definition of Done/Ready usage and accountability"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *MEETING 3 — Fadi / Manan* (10:45 AM · Fadi Rizk)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Decisions:*\n• :white_check_mark: *120-DAY OPEN JOB FLOW — ARCHITECTURE LOCKED* — Remove the arbitrary 30-day auto-close entirely. Default: job stays open 120 days. When OEM closes, prompt: 'Do you plan to hire for this role in the next few months?' Yes = keep open + send disposition sync. No = close, new job request ID next time. *Eliminates the reactivate flow entirely.* This directly addresses Indeed flagging copy/reactivate as declining feed quality.\n• :white_check_mark: *TALENT POOL OPT-IN = SMS, NOT END-OF-SCREENER* — Volume math is clear: 100K applicants/month vs. ~15K screener completers. Even 10% SMS response rate beats 50% end-of-screener response on absolute numbers. Timing: send after interview process concludes, so it feels personal. Store `talent_pool_opt_in` on applicant record. Minimal design lift.\n• :white_check_mark: *ENGINEERS INTO FIGJAM SESSIONS* — Real-time assumption validation. Reduces rework.\n• :white_check_mark: *WEEKLY LINEAR TRIAGE CADENCE* — Product, design, and engineering reviewing triage together. Explicit yes/no decisions with comments.\n\n*Why it matters:* The 120-day flow is the most important call you made today. It solves the duplicate job ID problem that is actively hurting your Indeed feed quality score and directly ties to the suspension risk. SMS opt-in 10x's your addressable Talent Pool pipeline.\n\n*Three Open Questions You Flagged (Manan to resolve):*\n1. Where are we with the disposition sync API?\n2. What happens if OEM doesn't signal how they hired?\n3. Does disposition sync actually reset job relevance/ranking on Indeed?\n\n*Action Items:*\n• :arrow_right: *YOU (Manan):* Send Indeed 120-day flow proposal to Skye for alignment — *before you go OOO*\n• :arrow_right: *YOU (Manan):* Clarify 3 disposition sync questions with Indeed rep (Catherine or Jessica)\n• :arrow_right: *Fadi:* Complete copy + reactivate designs, target near-final by Friday (highest priority while Manan is out)\n• :arrow_right: *Fadi:* Start Talent Pool opt-in via SMS design (store opt-in field on applicant record)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *MEETING 4 — Indeed Account Setup Rollout w/ Carlo* (12:51 PM · Carlo Ferrer)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Decisions:*\n• :white_check_mark: *EXPERIMENT FLAG FOUND + UPDATED* — Flag name: 'Hiring Account Setup Trial' (tagged 2026 July). Split is now live: 30% nothing / 50% standard account setup / 20% Indeed account setup. No additional rollout flags needed. Carlo has eyes on it.\n• :white_check_mark: *AMPLITUDE + DATABRICKS DASHBOARDS QUEUED* — Amplitude for UI user flow; Databricks for back-end token authentication (token only visible server-side). Both needed to track the Indeed account setup experiment properly.\n• :white_check_mark: *SOURCE CLAIM TRACKING TABLE TO BUILD* — Identify who has completed Source Claim through the Indeed flow. Critical for measuring the pilot.\n• :white_check_mark: *CARLO KNOWLEDGE RISK ACKNOWLEDGED* — Carlo is effectively the sole owner of Indeed integration knowledge. Izzy has some overlap. Agreed path: team swarming (multiple people on same project) to distribute the risk.\n\n*Why it matters:* The source claiming pilot you joined on Aug 31 is now in-flight via experiment. This is the path to recovering and improving Indeed traffic quality long-term. The knowledge risk around Carlo is real — if he's unavailable, the team is stuck.\n\n*Action Items:*\n• :arrow_right: *YOU (Manan):* Build Amplitude + Databricks dashboards for Indeed account setup user flow\n• :arrow_right: *YOU (Manan):* Build Source Claim tracking table (who has completed Source Claim)\n• :arrow_right: *Team:* Begin swarming on Indeed knowledge — get more people context on the integration"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *YOUR ACTION ITEMS — TODAY + BEFORE OOO*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "1. :rotating_light: *DEPARTURES SIGNAL DOCS + DATA → SALES* (DUE TOMORROW, Fri Sep 4) — Conflict docs + data to Zane, Sean, Jon W, Bobby. Sales outreach starts Monday Sep 7. This cannot slip.\n2. :rotating_light: *SEND INDEED 120-DAY FLOW PROPOSAL TO SKYE* — Lock alignment before you go OOO. Fadi is unblocked but you need Skye's buy-in first.\n3. :rotating_light: *ROADMAP PROMPT UPDATE* (DUE EOW Fri Sep 4) — You committed to this by end of week.\n4. :red_circle: *POWER USER ANALYSIS → SALES TEAM* — Was due this week. Ship it today/tomorrow if not done.\n5. :red_circle: *VERIFY IN-PRODUCT TERMINATION TRIGGER* — Was this week. Still unresolved.\n6. :red_circle: *OVERTIME DATA CUTS* — (a) OT threshold for trial starters; (b) payroll usage vs. pickup/conversion. This week.\n7. :large_blue_circle: *ROLE NORMALIZATION PRD FOLLOW-UP* — Divij + Sina were due EOD TODAY. Did they deliver? Chase if not.\n8. :large_blue_circle: *LINEAR TICKETS: recency + distance experiments* — Unblocks Divij. Still open.\n9. :large_blue_circle: *DIVIJ CSV FORMAT SPEC FOR ITERABLE* — Blocking experiment coding.\n10. :large_blue_circle: *IBK OTP THREAD SIGN-OFF* — Overdue.\n11. :large_blue_circle: *BUILD AMPLITUDE + DATABRICKS DASHBOARDS* (Indeed account setup) — Post-OOO OK but don't forget.\n12. :large_blue_circle: *BUILD SOURCE CLAIM TRACKING TABLE* — Post-OOO OK.\n13. :large_blue_circle: *EARNIN SAMPLE FEED* — Was due Aug 31. Confirm sent to jon.salzberg@earnin.com. If not, send immediately.\n14. :large_blue_circle: *INDEED FRAUD EVIDENCE PACKAGE* — Manan + Divij. Cleanup + score + OTP. Send to Jessica Kanaskie.\n15. :large_blue_circle: *CLARIFY DISPOSITION SYNC QUESTIONS* — With Indeed rep (Catherine or Jessica): API status, missing hire signal, ranking reset."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":hourglass: *CRITICAL WATCH LIST*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• :rotating_light: *INDEED FEED SUSPENDED — Day 9* (Aug 25 → now). Path: package fraud evidence → send to Jessica → 2-3 week review. Source claiming pilot active via experiment (20% rollout live as of today).\n• :rotating_light: *DEPARTURES SIGNAL → SALES — DUE TOMORROW* (Fri Sep 4 PDT). Sales outreach Monday Sep 7.\n• :rotating_light: *FADI OEM ATTRIBUTE STUDY* — Due today/tomorrow. Check in — did Fadi deliver?\n• :yellow_circle: *JD V2 ROLLOUT* — 2-3% first. Rami shipping. JD A/B experiment from IBK is 2+ weeks running and overdue — pull signal BEFORE V2 rolls out.\n• :yellow_circle: *OTP SCOPE EXPANSION* — Free-tier existing users. Copy update needed (Iszael). Unblocked since Sep 1.\n• :yellow_circle: *422 PUBLISHING ERRORS* — Day 54 now. 146 locations. Jatin RCA still in progress.\n• :yellow_circle: *INDEED CORP DOMAIN DEADLINE OCT 31* — Corp email req PAUSED. ~55.5% at risk. 4 options still undecided. Runway = ~8 weeks.\n• :yellow_circle: *SKYE TORONTO TRIP* — She's visiting engineers in a couple of weeks. Help her prep.\n• :yellow_circle: *MATAN MEETING GREG (VP SALES)* — Should have happened week of Sep 1. Confirm it happened."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":trophy: *CHIEF OF STAFF'S TAKE*\n\nManan — seriously, look at what you got done today. You walked in Thursday morning and in 4 meetings you: opened a new distribution channel (JobTarget), shipped a live experiment on Indeed source claiming, made a foundational architectural call on job IDs that will directly improve your feed quality, and 10x'd your Talent Pool pipeline addressability by switching to SMS opt-in. That's a day.\n\nHeading into OOO with the Indeed experiment live, Fadi holding down the design fort, and Skye integrated is the right state. *The one thing that absolutely cannot slip: get the departures signal docs to sales before you log off tomorrow.* Sales outreach starts Monday and they need the ammo.\n\nThe 120-day job flow decision will pay dividends for months. Great call. Go enjoy the break — you earned it. :rocket:"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Digest — Thu Sep 3 2026",
    "blocks": blocks
}

def preview():
    msg = "\n=== SLACK DIGEST PREVIEW (Sep 3 2026) ===\n"
    for block in blocks:
        if block.get("type") == "section":
            text_obj = block.get("text", {})
            msg += text_obj.get("text", "") + "\n\n"
        elif block.get("type") == "header":
            msg += "### " + block["text"]["text"] + " ###\n\n"
        elif block.get("type") == "divider":
            msg += "---\n"
    sys.stdout.buffer.write(msg.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN")
)

if not token:
    print("No Slack token found — printing preview instead.")
    preview()
    sys.exit(0)

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
        print(f"Slack message sent successfully! ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error sending Slack message: {e}")
    preview()
    sys.exit(1)
