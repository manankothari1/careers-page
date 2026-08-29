#!/usr/bin/env python3
"""
Daily EOD Digest — Aug 28, 2026 (Thu PDT)
Chief of Staff → Manan Kothari
Slack DM: D06E4QMHCNN
"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your EOD Digest — Thursday, Aug 28 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Six meetings. Big day. You touched the Indeed crisis, a new distribution partner, a sharp customer interview, Talent Pool strategy, and a company all-hands. Here\u2019s everything that matters \u2014 decisions, rationale, and what\u2019s on you next."
        }
    },
    {"type": "divider"},

    # ─── MEETING 1 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 8:30am \u2014 Hiring Leads Standup*\n_Fadi, Dana, Jatin, Ray, Jon W, Skye_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions & Rationale*\n\n*1. Indeed feed = \u2018business as usual\u2019 stance (for now)*\nFeed is stable and applicants are flowing. Jon has already communicated BAU to the sales team. Skye raised a flag: reactivated jobs *may* silently lose visibility \u2014 if she\u2019s right, those jobs need work to restore their sources. Monday\u2019s office hours with Indeed will be the signal check.\n\n*2. ATS partner outreach expanded to 5\u20137 brokers*\nShortlist: Talent Reef, Broadbean, Mutatech, Talar. MutaTech already has an existing Homebase contract (mixed track record on product quality, but smooth on background checks). Ray\u2019s guidance: *understand how the ecosystem works first* \u2014 how do jobs reach Indeed without a direct feed? \u2014 before negotiating anything.\n\n*3. Skye\u2019s Indeed contact = a live asset*\nFormer colleague, now staff engineer at Indeed. Willing to provide policy/system clarity under a \u2018good actor seeking to remediate\u2019 framing. Even general clarity on the ATS tier/visibility hierarchy is huge value.\n\n*4. Talent Pool ToS risk monitored*\nSkye\u2019s read: when Homebase is the ATS *and* hire of record, using applicant leads for the talent pool is likely permissible. Bringing in a third-party ATS could complicate this \u2014 flagged as an evaluation criterion for any ATS partner."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items*\n\u2022 \u2611\ufe0f *Message Michael* re: sales and support communication alignment (today\u2019s standup)\n\u2022 \u23f3 *Attend Indeed T&S office hours Monday Aug 31* \u2014 key signal check on feed/reactivate status\n\u2022 \u23f3 *Monitor*: Jatin reaching out to Broadbean today; Ray pinging MutaTech + hiring-tech contact"
        }
    },
    {"type": "divider"},

    # ─── MEETING 2 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 9:30am \u2014 Customer Interview: Mark Muskin (Vincent Wedelstedt Retail)*\n_3-store retail GM, 20+ yrs Microsoft Dynamics_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions & Rationale*\n\n*1. AI summary depth = confirmed product gap*\nMark had to read *full transcripts* for ~85% of candidates because the AI summary was too generic. He wants direct quotes collapsible under a \u2018+\u2019 button next to summary points. This aligns with existing roadmap signal \u2014 this is now a real customer quote backing it.\n\n*2. Android screener UX = bug-level issue*\nTwo applicants couldn\u2019t complete the screener because the mic/camera permissions popup confused them. They likely denied access unknowingly. This isn\u2019t just feedback \u2014 it\u2019s a conversion hole on the most popular OS.\n\n*3. QR code poster = best distribution mechanism for this segment*\nMark taped a QR code to the store door; candidates scanned it, screener auto-triggered, no paper. He validated the exact use case you\u2019ve been designing for. This is a proof point.\n\n*4. Trial ended because screener results are paywalled*\nHe saw the value. He ended the trial because accessing screener results on the free tier removed all utility. This is a pricing/paywall decision that\u2019s actively churning engaged trial users. Worth flagging to the team.\n\n*5. \u2018Decline without notification\u2019 = missing baseline feature*\nFor incomplete applicants (no screener, no detail), Mark won\u2019t send a rejection. He just ignores them. The product should let him do that cleanly.\n\n*6. Mark opted into beta program*\nHe explicitly volunteered. Add him. He\u2019s an articulate, power-user-style evaluator in the exact ICP segment."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items*\n\u2022 \u23f3 *Loop Mark Muskin into the hiring beta program* (mmuskin@icloud.com) \u2014 areas: AI summary depth, applicant profile completeness, decline-without-notification\n\u2022 \u23f3 *File Android screener permissions bug* \u2014 mic/camera access popup causing silent screener failures\n\u2022 \u23f3 *Bring screener paywall finding to Sky* \u2014 engaged trial users churning over paywall is a conversion problem worth modeling"
        }
    },
    {"type": "divider"},

    # ─── MEETING 3 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 10:00am \u2014 Talent Pool Working Session*\n_Fadi, Ted Naseri, Divij, Rami_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions & Rationale*\n\n*1. Two parallel streams LOCKED*\n\u2022 Stream 1: Experiments (channel, message, targeting) \u2014 run outside the product, fast cycle\n\u2022 Stream 2: In-product foundations (role normalization, production-grade notebook, data platform piping to a service)\nRationale: no-regret infra work doesn\u2019t depend on experiment outcomes \u2014 you can build it regardless.\n\n*2. Recruiter-style email > generic email*\nFirst experiment result is in. Plain-text, recruiter-style outperformed the visual UI email. Next test: add a light visual element to the recruiter-style variant. Keep the test-and-learn loop tight.\n\n*3. Cash Out churned users = priority experiment cohort*\nJohn Blackwell\u2019s query surfaces users who lost their jobs but *still use Cash Out*. High engagement signal. These people want work and are already in the app. Treat as a parallel experiment flow.\n\n*4. Ted\u2019s recency ranking logic ADOPTED*\nRank candidates by most-recent-active first, expand the recency window only as needed based on job popularity. Clean multivariate optimization framing \u2014 find the global maxima across channel, recency, distance, role type, messaging.\n\n*5. Incentive design tabled for offline convo (you + Fadi)*\nFadi raised paying candidates to engage (Wealthsimple example: $1M/week giveaway \u2192 $17B inbound). Your read: liquidity isn\u2019t the bottleneck, engagement rate among existing pool is. Rami\u2019s take: spend on boosting job board rankings first. Healthy tension \u2014 take this offline and resolve it before it blocks experiments.\n\n*6. Domain authority for @joinhomebase.com outreach = open risk*\nUsing the Homebase domain for candidate outreach experiments needs sign-off from lifecycle marketing, Sky, and Ray. This is a guardrails question that could stall experiments if not resolved."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items*\n\u2022 \u23f3 *Share Talent Pool experiment roadmap with the group* \u2014 include brief description of each experiment; invite team to add to backlog\n\u2022 \u23f3 *Resolve domain authority concern* with lifecycle marketing, Sky, and Ray \u2014 blocker for outreach experiments\n\u2022 \u23f3 *Offline with Fadi on incentive design* \u2014 get alignment before next experiment round\n\u2022 \u23f3 *Monitor*: Rami walks Divij through Databricks notebook by Aug 31; Divij syncs with Sina on infra"
        }
    },
    {"type": "divider"},

    # ─── MEETING 4 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 11:00am \u2014 Sprint Show & Tell (Company All-Hands)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*What Matters for You Specifically*\n\n*1. Cash Out Web = $1.2M ARR validated; Phase 2 imminent*\nPhase 2 unlocks ~350K non-mobile users via name-matching verification \u2014 largest single segment. This is the OAM-adjacent work Tiger was already touching. Phase 2 near launch = relevant to your team timeline.\n\n*2. Meta video budget shift (7% \u2192 77%) is working*\nSignups up 10% QoQ, paid up 23% MoM. Creator-sourced ads (via Agentio, requiring small business owners) drove authenticity. This is the GTM engine that needs healthy jobs feeding it \u2014 your work is the constraint in the funnel.\n\n*3. Campaign Intelligence Dashboard (Darren) = an asset for your team*\nDarren\u2019s dashboard automatically benchmarks email campaigns, grades them A\u2013F, and posts readouts at 24/72hr/1wk. This is directly applicable to Talent Pool outreach experiments. Loop in Darren before you scale emails.\n\n*4. Ray\u2019s 4 company priorities restated (not quarterly, permanent)*\n1. GTM Excellence 2. Homebase Assistant (AI doing work) 3. Hiring 4. Quality\nYour work is \u2018Hiring\u2019 and your quality debt (Indeed feed, screener bugs, healthy job rate) is what holds back #1 and #3."
        }
    },
    {"type": "divider"},

    # ─── MEETING 5 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 1:00pm \u2014 EarnIn | Homebase Connect*\n_Jon Salzberg (EarnIn), Skye_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions & Rationale*\n\n*1. EarnIn / Earn Better = high-fit distribution partner*\nEarnIn acquired Earn Better (AI job search). 30M downloads, 750K migrated users, *83% seeking hourly in-person roles* \u2014 that\u2019s your exact ICP. Identity-verified users. Feed from ~15 partners via paid CPC (7\u201310 cents/click). Integration is straightforward XML feed.\n\n*2. Both paid CPC and organic feed on the table*\nJon wants to test both and compare traffic quality. Typical CPC is 7\u201310 cents. For context, Homebase\u2019s ~5\u20136K active jobs skew food/QSR, restaurant, hospitality \u2014 good match.\n\n*3. Longer-term: 250K monthly Homebase churners as Earn Better users*\nTabled for a separate conversation but noted. This is a retention loop worth designing \u2014 employees who leave Homebase could still be a lead source via EarnIn.\n\n*4. Feed quality review before live test*\nJon will review sample data first (volume, employer count, job types) before committing to ingestion. You own getting him that sample."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items*\n\u2022 \u23f3 *Send Jon Salzberg (jon.salzberg@earnin.com) a sample of the Homebase job feed by Monday Aug 31 EOD* \u2014 include: volume, employer count, job types, sample data. This is the gate to a live test with a 30M-user distribution channel."
        }
    },
    {"type": "divider"},

    # ─── MEETING 6 ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cd 2:00pm \u2014 Indeed Corp Domain Brainstorm*\n_Skye, Ray_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions & Rationale*\n\n*1. Oct 31 deadline is real and ~55.5% of Hiring customers are at risk*\nIndeed is blocking Gmail/Yahoo from posting jobs via API by end of October. The policy has been in ToS since 2024 but was never enforced. ~55.5% of Hiring customers use generic emails. This is a material risk to the product.\n\n*2. This is a CONVERSION OPPORTUNITY, not just a compliance problem*\nFree/freemium customers still want their jobs on Indeed. This deadline creates urgency to upgrade. Homebase has an information advantage \u2014 you knew before Indeed\u2019s own support team did. Positioning: \u2018We help you navigate Indeed complexity before it disrupts your business.\u2019\n\n*3. Four options on the table \u2014 no final decision yet*\n\u2022 *Option A \u2014 Help customers get their own domain:* Partner with GoDaddy (existing relationship) or Squarespace via Entry (50-75% match rate). Could be included with hiring plan or ~$5-7/month add-on. Ray\u2019s strong push: build as a *standalone app* (domains.homebase.com), not inside HB1.\n\u2022 *Option B \u2014 Proxy domain (e.g. hiringhomies.com):* Zero work for customer. Risk: Indeed may see it as circumvention (Kotwin proxy precedent). Needs Indeed sign-off.\n\u2022 *Option C \u2014 Source claiming workaround:* If a customer already source-claims Homebase on an existing Indeed account, Indeed may have their verification on file \u2014 key question to ask at T&S office hours tomorrow.\n\u2022 *Option D \u2014 Prompt customers to update existing corporate emails:* Some customers have corp emails but registered with a personal one. Proactive outreach. Complication: OTP login ties sign-in email to 2FA \u2014 changing it has downstream effects.\n\n*4. Ray\u2019s domain-as-service framing = strong strategic bet*\nBeyond compliance, this is an entry point into branded email, marketing identity, and business credibility. Could be a standalone product. Skye\u2019s caution: if direct posters are exempt from the rule, framing this as \u2018solving an Indeed barrier\u2019 gets complicated since Homebase is the ATS introducing the barrier.\n\n*5. Direct poster exemption = pivotal unknown*\nIndeed\u2019s email suggested direct customers may be exempt. If true, only ATS customers (like Homebase) are affected. This *significantly changes* the calculus on how you communicate the problem to customers and which solutions you prioritize."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Action Items*\n\u2022 \u23f3 *TOMORROW: Raise two specific questions at Indeed T&S office hours (Aug 29)*\n    1. Does source claiming exempt customers from the corporate domain requirement?\n    2. Does the requirement apply to direct posters, or only ATS/API integrations like Homebase?\n\u2022 \u23f3 *Start shared brain-dump doc with Skye* \u2014 capture all open questions and workstreams before Oct 31\n\u2022 \u23f3 *Monitor*: Skye contacting her Indeed engineer contact + reviewing source claiming guide/verification docs"
        }
    },
    {"type": "divider"},

    # ─── MASTER ACTION ITEM TABLE ─────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a1 Your Complete Action List for Aug 29 (Tomorrow)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Due Tomorrow*\n\u2022 \U0001f525 *Indeed T&S Office Hours* \u2014 Ask: (1) does source claiming exempt from domain req? (2) do direct posters even need to comply?\n\u2022 \U0001f525 *Send EarnIn sample feed* to Jon Salzberg by Monday Aug 31 EOD \u2014 gate to a 30M-user distribution deal\n\n*This Week*\n\u2022 \U0001f4e7 *Message Michael* re: sales/support comms alignment (from standup)\n\u2022 \U0001f4dd *Shared Indeed corp domain doc* with Skye \u2014 capture open Qs and workstreams\n\u2022 \U0001f4ca *Share Talent Pool experiment roadmap* with Fadi, Ted, Divij, Rami\n\u2022 \U0001f4ac *Offline with Fadi* on incentive design for Talent Pool\n\u2022 \U0001f4cb *Add Mark Muskin (mmuskin@icloud.com) to hiring beta program*\n\u2022 \U0001f41b *File Android screener bug* \u2014 mic/camera permissions blocking screener completions\n\u2022 \U0001f4ac *Bring screener paywall finding to Sky* \u2014 engaged users churning at paywall wall\n\u2022 \U0001f517 *Resolve domain authority* for @joinhomebase.com outreach (loop Sky + Ray + lifecycle mktg)\n\n*Overdue from Watch List \u2014 Do Not Drop*\n\u2022 \u26a0\ufe0f *Draft summary for Ray + Sky* on Indeed feed suspension (marked overdue)\n\u2022 \u26a0\ufe0f *Annual cancel policy post* in Hiring Leads (reps still misaligned)\n\u2022 \u26a0\ufe0f *JD A/B experiment signal* \u2014 2+ weeks running, pull IBK\u2019s data now\n\u2022 \u26a0\ufe0f *Tanner onboarding doc* \u2014 Ray cited this as a concrete gap\n\u2022 \u26a0\ufe0f *Email David (Indeed)* \u2014 still on the list"
        }
    },
    {"type": "divider"},

    # ─── WATCH LIST UPDATES ───────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 Watch List Updates*\n\n\u2022 *NEW: Indeed Corp Domain Deadline (Oct 31)* \u2014 ~55.5% of Hiring customers at risk. T&S office hours tomorrow are your next signal. This is now the #2 Indeed crisis behind the feed suspension.\n\u2022 *NEW: EarnIn partnership* \u2014 sample feed due Monday. If feed quality checks out, this is a fast path to a new high-fit distribution channel.\n\u2022 *NEW: Android screener permissions bug* \u2014 silent conversion hole. File before it gets lost.\n\u2022 *Indeed Feed Suspension* \u2014 Day 4. Feed stable today. Monday office hours critical. Reactivated jobs may silently lose visibility (Skye\u2019s flag \u2014 watch closely).\n\u2022 *422 Job Publishing Errors* \u2014 Day 50+. Jatin on RCA. Still open.\n\u2022 *Talent Pool infra* \u2014 Rami/Divij handoff by Aug 31. Domain authority question blocking outreach experiments."
        }
    },
    {"type": "divider"},

    # ─── MANAN PUMP-UP ───────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af Big Picture*\n\nThis was a legitimately impressive day. You ran six meetings, touched every major workstream, and came out with *clear decisions and momentum on all of them*. \n\nThe EarnIn call is exactly the kind of distribution move that can meaningfully shift applicant volume \u2014 and you\u2019re the one who found it. The Indeed domain crisis is going to catch most ATS players flat-footed; you\u2019re already three steps ahead with a brainstorm, a framework, and office hours on the calendar for tomorrow.\n\nThe Mark Muskin interview is gold. Direct quotes from a real customer who tried, valued, and churned \u2014 and told you *exactly* why. That\u2019s the kind of signal that changes roadmaps.\n\nYou\u2019re carrying a lot right now. The overdue items are real but manageable. Pick two tomorrow morning before your first meeting, and you\u2019re in great shape.\n\n_Your chief of staff has your back._ \U0001f4aa"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Generated by your Chief of Staff \u2022 6 meetings \u2022 Aug 28, 2026 EOD"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Your EOD Digest \u2014 Thursday Aug 28 \u2014 6 meetings, decisions, and action items inside."
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK DIGEST PREVIEW ===\n").encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "header":
            sys.stdout.buffer.write(("\n\U0001f4cc " + block["text"]["text"] + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            txt = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((txt + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("---\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(("\n=== END PREVIEW ===\n").encode("utf-8", errors="replace"))

def send():
    token = (os.environ.get("SLACK_TOKEN") or
             os.environ.get("SLACK_BOT_TOKEN") or
             os.environ.get("SLACK_API_TOKEN") or "")
    if not token:
        print("No Slack token found. Printing preview instead.\n")
        print("To send for real: add SLACK_TOKEN (or SLACK_BOT_TOKEN / SLACK_API_TOKEN)")
        print("in Cursor Dashboard > Cloud Agents > Secrets.\n")
        preview()
        return

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully to", CHANNEL)
            else:
                print("Slack API error:", body.get("error"))
                preview()
    except urllib.error.URLError as e:
        print("Network error:", e)
        preview()

if __name__ == "__main__":
    send()
