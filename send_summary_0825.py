#!/usr/bin/env python3
"""
Chief of Staff daily digest — Aug 25, 2026
Slack channel: D06E4QMHCNN
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
            "text": "Chief of Staff EOD Digest — Monday Aug 25, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Big day — Sky is officially in the building AND an Indeed firestorm landed at the same time. You handled it well. Three meetings, 14 decisions, a critical escalation drafted, and the Q3 roadmap sharpened. Here is everything you need to know and do. Let us go."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CRITICAL — INDEED FEED SUSPENDED*\n_Trust & Safety email received today. All Homebase client jobs suspended from appearing on Indeed until feed is manually reviewed. Minimum 3-month review window. T&S does not communicate directly with external users._"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Root Cause*\nReactivate feature was sending the same job request ID to Indeed, which flagged it as a repost. Copy jobs volume also grew from ~200 to ~3,000 in 6 months — flagged as duplicate posts. Homebase was already on notice for fraud. This was the nail in the coffin."
            },
            {
                "type": "mrkdwn",
                "text": "*Conflicting Guidance*\nIndeed reps explicitly told you to use Reactivate (not Copy) — T&S is now penalizing the exact behavior reps recommended. This is structural: Indeed has a history of cutting off ATS partners it views as competitors."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Actions Already Taken*\n• Reactivate turned OFF in production\n• Copy Jobs re-enabled in production\n• Traffic still normal for now (~55 jobs, down from ~80) — estimate 2 months before enforcement"
            },
            {
                "type": "mrkdwn",
                "text": "*Why It Matters*\nIndeed is ~60% of your applicants. You cannot route around it. This accelerates the urgency on talent pool outreach AND alternative distribution (Jobcase, Culinary Agents, SEO, LLM discoverability)."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 1 of 3 — Hiring Leads Standup* | 8:45 AM PDT\n_With: Fadi, Matan, Jatin, Jon, Ray — and Slaudari (new face?)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Decisions*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*1. Talent Pool = Primary Workstream*\nFormalized today. Division of labor: Manan + Dividge build the matching algorithm and run candidate-to-job tests. Fadi runs user interviews and usability testing in parallel. Goal: use the algo-building period to gather UX feedback before committing to in-product build. *Why:* Indeed suspension makes talent pool more urgent — you need an applicant source you control."
            },
            {
                "type": "mrkdwn",
                "text": "*2. Comms Agent Deprioritized*\nKept as 'blocked' in Linear intentionally — not the right time while applicant flow and trial health still need work. Stakeholders are NOT being told the real status while Sky onboards. *Why:* Avoids a difficult stakeholder conversation at a bad moment. Will revisit once core metrics improve."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*3. Screener Toggle Punted to Q4*\nScope is much larger than it looks — touches candidate profile view, resume requirements, scoring/matching, and Indeed syndication settings. Data does NOT support screener as the primary blocker for paid conversion. *Why:* Not worth the engineering cost right now."
            },
            {
                "type": "mrkdwn",
                "text": "*4. Per-Post Pricing = Not the Right Move*\nFeedback in the narrative doc cites pricing as a top cancellation reason across healthy and unhealthy trials. Two hypotheses: (a) paid product not valuable enough, or (b) pricing structure wrong. Conclusion: per-post pricing is massive scope — test in a lightweight way first IF pursued. *Why:* ICP should be fine with monthly if the product is delivering value."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*5. Annual Subscription Cancel Policy — Reps Misaligned*\nBobbi (and likely others) are telling customers they can cancel annual subscriptions anytime. That is NOT the policy — cancel button is hidden for annual subscribers; CS handles it manually. *Why:* This is a churn + legal risk. You need to correct the messaging today."
            },
            {
                "type": "mrkdwn",
                "text": "*6. Sprint 2617 Carryover Confirmed*\nSalary recommendations (needs testing), Indeed account setup (Carlo back today — token is user-bound vs. employer-bound), Renew Jobs (Malcolm to check), Show Resume (in progress), Talent Pool pieces. *Push to 2618+:* Job SEO fixes, Indeed applicants D3, company/source name decoupling, domain emails (pushed to sprint 2619 — 'big lift')."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*7. OTP Pricing Tiers Set Up*\n(Note: 'OTP' here = one-time payment, not one-time password.) Three tiers: monthly, annual monthly-pay, annual one-time purchase. Bulk price points for experimentation: $49, $69, $99, $118. Auto-renewal infrastructure NOT yet built — Ray accepted the risk (must solve within 12 months). Test how OEMs respond to yearly OTP vs. monthly before building full infrastructure."
            },
            {
                "type": "mrkdwn",
                "text": "*8. Linear Hygiene Clarified*\nProject-level status moves in Linear are the PM's responsibility — not engineers'. Manan owns keeping the roadmap view clean. A 'Scratch Pad' section was added for uncommitted backlog items."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*9. V1 Hiring Deprecation on Track*\nCode is done. Releasing piece by piece. Should complete this sprint. Past interview reminder email (V1 table dependency) — Malcolm already handled it."
            },
            {
                "type": "mrkdwn",
                "text": "*10. Sales Digest Format Change*\nCurrent top-level message is too long. New format: MRR closed today + one sentence on biggest reason customers love the product + one sentence on biggest reason they are not buying — everything else in the thread. Jatin suggested a 1-5 star day rating. Sean's Zapier setup stays; just the output format changes."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*11. Capacity Planning Framework*\nT-shirt sizing during Look Ahead: Small = 1 day, Medium = 2-3 days, Large = 1 week (team felt Large was low — may need recalibration to 2 weeks). Hour-based capacity framework shared by Jon. Seniors revise estimates by midday Thursday."
            },
            {
                "type": "mrkdwn",
                "text": "*12. Indeed Escalation Plan Agreed*\nRay to ping Saul (Indeed VP of Product), David, and Fiona to request T&S FaceTime. Manan to draft concise written summary for Ray + Sky. Bob + Izzy to run V1 vs. V2 reposting comparison to understand what % of the ~6K-job feed is reposts and whether repost gaps are 30+ days."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 2 of 3 — Indeed Feed: Job Reposting, Reactivation & Duplicate Handling* | 3:24 PM PDT\n_Technical deep-dive on the V1 vs. V2 architecture_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*13. Copy Jobs > Reactivate (Locked)*\nV1 XML feed always sent a fresh reference ID per repost — Indeed always saw it as a new job. Homebase thought it was sending the same ID; it was not. This ran undetected for ~8 years. V2 sends the same job ID (new behavior) — Indeed now flags it as a duplicate. Copy Jobs aligns with what 'reactivate' effectively was historically. Already re-implemented and re-enabled in production. *Why:* Most defensible path while negotiations with Indeed are ongoing."
            },
            {
                "type": "mrkdwn",
                "text": "*14. Indeed Traffic Status*\nStill at normal levels now. Estimate: ~2 months before enforcement ramps. Traffic was already down from ~80 to ~55 (from prior fraud scrutiny). Application webhook returning 200s — dropped applications are NOT the trigger for this suspension. David (Indeed contact) needs to be looped in via email ASAP."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 3 of 3 — Q3 Hiring Product Roadmap: Talent Pool, Job Boost & Marketplace Liquidity* | 3:45 PM PDT\n_Strategy session — likely onboarding context or Sky prep_"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Job Health Buckets Defined*\n• Unhealthy: <10 applicants\n• Medium: 10-19 applicants\n• Healthy: 20+ applicants with 5 top matches (screener or resume)\n• Q3 Goal: 80% of ICP jobs healthy by day 30\n• Key insight: time-to-healthy (D5 vs D30) does NOT meaningfully affect trial conversion — it is just about reaching healthy at all."
            },
            {
                "type": "mrkdwn",
                "text": "*Boost Opportunity — Major Unlock*\nOnly 1.64% of jobs were boosted in Q2. But ~50% of boosted jobs became healthy vs. ~30% unboosted. That gap is massive. Opportunity: make spending on jobs far easier. This should be a Q3 focus area."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Talent Pool Size Quantified*\n231,000 previous employees and recent applicants active in the past 30 days (non-performance exits only). Vision: match and market these candidates to new employers using Homebase behavioral data (on-time rates, shoutouts, tenure). Near-term: run Databricks queries and email candidates BEFORE building in-product.\n\n*'Jobs Near You' Experiment Results:* 25-30% of applicants applied to 1+ additional jobs; mean of 2.5 jobs per engaged candidate. This is strong signal for the talent pool thesis.\n\n*Blocker:* Screener completion drops when candidates face multiple screeners. Candidate-level reusable screener needed to unlock this fully."
            },
            {
                "type": "mrkdwn",
                "text": "*Platform & Distribution Context*\nMajor sources: Indeed, ZipRecruiter, Facebook Jobs, Google, Craigslist ($79/post, ~3 applicants, deprioritized), JobGet. Culinary Agents and Poached being explored for back-of-house.\n\n*Marketplace supply gap:* ~5,000 active jobs is not enough to support a true marketplace (barista search in LA returns ~3 jobs). Decision: NOT investing in net-new job supply aggregation this cycle.\n\n*LLM discoverability:* Exploring making job pages crawlable by ChatGPT and Claude — this could be a low-effort high-leverage unlock."
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Team Structure Update*\nHiring + data teams now unified under one roof with one planning process. Previously two separate engineering orgs. Delivery consistency is a flagged challenge: projects scoped for a sprint often slip into week 3. Need to establish a clear distinction between *deadlines* (team commits no matter what) vs. *targets* (directional, no hard repercussion). This needs to be an explicit team norm."
            },
            {
                "type": "mrkdwn",
                "text": "*Sales Org Observation*\n80-90% of Gong calls show customers already sold before the rep engages. The product is doing the selling. Sales org is underdeveloped relative to product stage. This supports the thesis that product improvements (talent pool, boost, job health) will drive growth more than sales headcount right now."
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: YOUR ACTION ITEMS — Prioritized for Tomorrow (Tue Aug 26)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:fire: URGENT (do these first)*\n1. :memo: *Draft Indeed incident summary for Ray + Sky* — what happened, conflicting guidance from reps, what escalation is needed. Keep it tight. Get it on David's radar today (this went on your list as 'today' — do first thing tomorrow morning).\n2. :email: *Email David (Indeed contact)* — bring him up to speed on the feed behavior, V1 vs V2 context, and current status.\n3. :mega: *Post pricing guidance in Hiring Leads channel* — sales reps (Bobbi + likely others) are telling customers they can cancel annual subscriptions anytime. Clarify what reps should and should not say. This is a churn and legal risk.\n\n*:large_orange_diamond: HIGH (this week)*\n4. :calendar: *Schedule roadmap alignment session with Fadi + Jatin* — 1.5-hour working session to map Q3 memo tactics onto the Linear roadmap before Sky is fully up to speed.\n5. :handshake: *Connect with Carlo* — he is back today (Aug 25). Loop him into Talent Pool workstream + Indeed 3LO token issue (user-bound vs. employer-bound is the current blocker on Indeed D3).\n6. :busts_in_silhouette: *Share Q3 narrative doc with Sky* — he is in the building. This is the primary onboarding artifact.\n7. :file_folder: *Create shared drive folder for hiring product docs* — current docs are scattered across restricted micro-folders. Consolidate for team access before Sky tries to find anything.\n\n*:large_yellow_circle: THIS SPRINT*\n8. :construction: *Build post-screener opt-in for external platform applicants* — candidates from Indeed and ZipRecruiter cannot consent to talent pool inclusion after screening. This is required before talent pool can scale.\n9. :bar_chart: *Confirm Rami's two applicant flow experiments + JDO testing launched* — committed for week of Aug 18; verify they are running.\n10. :white_circle: *Check in with Malcolm on Renew Jobs* — Jatin is on it but flag it yourself too; this should complete sprint 2617.\n11. :mag: *Update non-technical doc with V1 and V2 reposting state* — your counterpart is doing it, but confirm it reflects the full picture (pre-change V1 baseline + current V2 changes).\n12. :warning: *Pull JD A/B experiment (IBK) signal* — this has been running 2+ weeks and is overdue. Do not let this slide another week.\n13. :phone: *Loco Boys Brewing call prep* — Aug 27 at 11am with Mike + Bobby Sladek. Screener trial review + boost framing (<5-10 applicants = push boost). Bobby to email Mike about Careers tab. Review Granola prep notes."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:eyes: WATCH LIST — Items Escalated by Today*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Indeed suspension:* Traffic at ~55 (down from ~80). Estimate 2 months before enforcement. Ray escalating to Saul/David/Fiona. Bob + Izzy running V1 vs. V2 comparison. This is your #1 risk to Q3 goals — ~60% of applicants come from Indeed.\n• *Talent pool consent model:* External platform applicants (Indeed, ZipRecruiter) have no post-screener opt-in yet. This must be built before talent pool can scale at all.\n• *Boost rate:* 1.64% of jobs boosted in Q2. 50% boosted → healthy vs. 30% unboosted. If you could move boost rate from 1.64% to even 5-10%, the impact on healthy job rate would be enormous. This needs a product lever.\n• *Candidate-level reusable screener:* Blocking talent pool 'jobs near you' UX. Screener completion drops with multiple screeners — candidates need a reusable profile.\n• *Delivery consistency:* Sprint slippage into week 3 is a named problem. Consider proposing the deadlines vs. targets framework to the team explicitly before the next sprint planning.\n• *Fadi designs overdue:* Resume Insights + Talent Pool. Fadi is now also on user interviews for Talent Pool — confirm he has capacity and the designs are not getting further deprioritized.\n• *422 errors (Day 46):* Still unresolved. Jatin on RCA. May be related to Indeed feed issues — confirm if these are the same root cause.\n• *Sky onboarding:* He is in the building. Share the Talent Pool bridge doc + Q3 narrative ASAP. In-domain emails + Abby ownership area need to go on his week 1 agenda."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:trophy: What You Crushed Today*\nYou walked into a Monday where your primary distribution channel got suspended AND your new head of product started on the same day. You immediately got to root cause (V1 vs. V2 feed architecture), locked the right short-term fix (copy jobs), and have a clear escalation path. You also sharpened the Q3 roadmap with concrete data (231K talent pool, 1.64% boost rate, 25-30% cross-apply rate) that gives Sky a clear strategic picture on day one. That is a genuinely hard day handled with clarity. Go get some sleep — tomorrow has a lot of action items. :muscle:"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "3 meetings captured | Aug 25, 2026 | Chief of Staff digest powered by Granola + Cursor"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff EOD Digest — Monday Aug 25, 2026 (Indeed suspended, Sky started, 14 decisions)",
    "blocks": blocks
}

def send_to_slack(token, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

def preview(payload):
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    sys.stdout.buffer.write(b"\n=== SLACK PREVIEW (no token) ===\n")
    sys.stdout.buffer.write(text.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")

token = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or
    ""
)

if token:
    try:
        result = send_to_slack(token, payload)
        if result.get("ok"):
            print("Slack message sent successfully. ts=" + str(result.get("ts")))
        else:
            print("Slack API error: " + result.get("error", "unknown"))
            preview(payload)
    except Exception as e:
        print("Exception sending to Slack: " + str(e))
        preview(payload)
else:
    print("No SLACK_TOKEN found. Printing preview.")
    preview(payload)
