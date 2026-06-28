"""
Sunday Jun 28 2026 — Weekly Decision Digest for Manan Kothari
Covers: Jun 22–26, 2026 (13 meetings, no meetings today Sun Jun 28)
"""
import sys
sys.path.insert(0, '/workspace')
from daily_digest import send_blocks

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Weekly Decision Digest  |  Jun 22–26, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Good evening, Manan! Huge week — 13 meetings, major strategic pivots, "
                "and you genuinely moved the ball on every front that matters. "
                "Here is everything you decided, why it matters, and what needs to happen next. "
                "Grab a coffee and let's review."
            )
        }
    },
    {"type": "divider"},

    # ── SECTION 1: KEY DECISIONS ──
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Decisions Made This Week", "emoji": True}
    },

    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. Indeed goal rewritten to a tighter, measurable metric*\n"
                "Ray/Manan 1:1 (Jun 25) — New goal: FFH jobs with zero Indeed applicants on D5 < 10% "
                "(currently sitting at 41%). The old 'increase Indeed-sourced applicants by 25' was too "
                "vague. This single metric now justifies source claiming, copy-job fixes, reactivation, "
                "and the sponsored jobs API all under one umbrella. Smart and clean."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Draft v3 Q3 goals doc in three-bucket structure — share with Ray before it reaches John."}]
    },

    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Outbound calling reframed: validate excitement, not bookings*\n"
                "Hiring Leads Standup (Jun 23) — Usman was selling 'free recruiter' and booking meetings, "
                "but that validates nothing. Pivot: measure whether people light up on the call. "
                "Dana revised the script; Usman role-played it. Target: 30–50 connections/week."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Listen to Usman's recent calls — track enthusiasm signals, not just booking rates."}]
    },

    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. Zero state page shipped — don't wait for Matan*\n"
                "Jun 23 Standup — Fadi pushed it after standup approval. You called it. "
                "The 'drive off the lot' experiment already showed a 49% lift in ICP trial starts "
                "(empty state tiles explain the product better than a landing page). "
                "Decision: keep that experiment live and layer new recruiter messaging into it rather than reverting."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Enable Amplitude recordings on zero state page to capture tile engagement data."}]
    },

    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Culinary Agents partnership: full-steam-ahead on feed integration*\n"
                "Jun 24 (w/ Ray, Jeff & Alice) — 2.7M hospitality workers, industry-specific boards, "
                "and your XML feed is already compatible with their format. Bulk PPP pricing ~$69/post at 500-post tier. "
                "Ray is sending the job feed; Alice's team needs ~2 weeks to automate. "
                "Big unlock: Culinary Agents can *also* boost Indeed reach — worth a dedicated follow-on call."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Schedule Culinary Agents follow-on call specifically on Indeed-boosting mechanics."}]
    },

    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Talent pool email blast green-lit: 86 line cook jobs, 25-mile radius, 2K cap per job*\n"
                "Rami/Manan Launch (Jun 25) — Experiment parameters locked: two treatments "
                "(recruiter-style vs. generic email), hashed randomization by role/business/city. "
                "UTM tracking on all links (utm_campaign=recruiter vs. generic). "
                "High Touch route confirmed as preferred pipeline (analytics team owns it via Rohit). "
                "Rami targets CSV delivery EOD Jun 25; blast was planned for Jun 26 morning."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Confirm Rami sent CSV + blast status. Ping Ted re: Shamir/Dvich for ML/data platform support."}]
    },

    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Abby onboarding roadmap locked: Jul 7 start, three first projects*\n"
                "Manan/Cindy (Jun 25) — Priority order: (1) Indeed source claiming, "
                "(2) Automatic go-live/fraud pre-check, (3) Job seeker manual intake. "
                "Keep her off Leads standup initially to protect onboarding focus; "
                "you'll be her bridge to the leads side in the interim. "
                "Cindy pulling the onboarding doc together."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Send Cindy: line cook D5/D30 analysis + relevant applicant flow links for Abby's onboarding doc."}]
    },

    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Role title & salary optimization: intercept modal (not inline), critical warning framing*\n"
                "Cindy/Manan (Jun 25 PM) — Batching all flags (title, salary) into one 'review before posting' "
                "intercept modal with an 'Apply all recommendations' CTA. "
                "Title warnings framed as critical (bad titles get flagged by Indeed and partner boards). "
                "Salary warnings softer ('you may struggle to fill this role'). "
                "FFH-only rollout to start, treated as an experiment given conversion risk. "
                "Cindy has designs due Monday midday."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Review Cindy's design options first thing Monday morning — feedback cycle needed before Wednesday Sprint Lookahead."}]
    },

    # Decision 8
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. Job description generator as Indeed duplicate-detection fix*\n"
                "Manan/Dana 1:1 (Jun 26) — Reposted/copied jobs are being flagged by Indeed as duplicates "
                "unless paid for, making Homebase look bad to customers. "
                "Fix: generate a sufficiently different description on copy/repost. "
                "Open question: what % difference does Indeed require? They won't say. "
                "Idea floated: test with a fake company to probe their detection logic (proceed carefully)."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Spike: determine how much description change prevents Indeed duplicate flagging before deciding reactivate vs. edit path."}]
    },

    # Decision 9
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*9. Source claiming banner: don't commit to ship date until UX questions resolved*\n"
                "Manan/Dana 1:1 (Jun 26) — Ray and Matan wanted a source claiming banner by 'tomorrow.' "
                "You correctly pumped the brakes: key questions unresolved — does it apply to trial users? "
                "How does it interact with the existing trial banner? "
                "Right call. Ship the right thing, not just the fast thing."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Define source claiming banner experience (trial user handling + trial banner interaction) before committing to any ship date."}]
    },

    # Decision 10
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*10. Comms agent ownership: intentionally left open*\n"
                "Ray/Manan (Jun 25) — Comms agent was added to your goals without your input. "
                "Your concern: screener funnel data shows the drop-off problem may be overstated "
                "(~70% click, ~60% start, ~80-90% complete once started). "
                "Ray's counter: it re-engages drop-offs. Ownership question left open. "
                "You can take it or treat it as Dana/Fatty/Davi doing you a solid."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Decide: own the comms agent or formally leave it with Dana/Fatty/Davi? Either way, close the loop with Ray."}]
    },

    # Decision 11
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*11. Nelson transitioning to ~5 hrs/week by end of June*\n"
                "Jun 23 Standup — No longer a daily staffed analyst. Team owns analytics ops going forward. "
                "Nelson won't proactively pull week-in-review data; you request as needed. "
                "He's still available for sanity-checking experiments. Spec-driven dev formalized: "
                "team members own their specs, agents generate TLDRs and surface questionable assumptions."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Ensure Nelson audits and syndicates all analytics/ops ownership before he transitions."}]
    },

    # Decision 12
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*12. Sprint 2612 off-track — root cause identified, not a systemic problem*\n"
                "Hiring Week in Review (Jun 22) — Unexpected OOOs and over-scoped domain events work. "
                "Applicants side mostly met goals; blocked by Facebook on L3 taxonomy. "
                "Starter plan removed from self-serve: ASP jumped as expected. "
                "Self-serve volume dipped slightly but more than offset by higher ASP. "
                "Still available for franchise sales."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Analyze starter plan removal — who opted out? What does it tell us about price elasticity and funnel shape?"}]
    },

    # Decision 13
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*13. SEO strategy: optimize tagging first, JS-to-HTML conversion later*\n"
                "Sprint Planning (Jun 22) — 300K impressions in 3 months but very low clicks due to weak SEO tagging. "
                "Priority: optimize meta descriptions and indexing first; Jenna (marketing) to provide guidance. "
                "Carlo keeping capacity for this. "
                "Headless browser spike also running in parallel — need a decision on Indeed relationship risk."
            )
        }
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": ":pushpin: *Action:* Follow up with Jenna on SEO indexing guidance. Decide on headless browser vs. admin-access route for Indeed."}]
    },

    {"type": "divider"},

    # ── SECTION 2: FULL ACTION ITEM LIST ──
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Your Open Action Items", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*URGENT — Do these first thing Monday*\n"
                ":red_circle: Draft v3 Q3 goals doc in three-bucket structure — share with Ray before John sees it\n"
                ":red_circle: Define source claiming banner UX (trial user handling + trial banner interaction)\n"
                ":red_circle: Confirm Rami's CSV delivery + email blast went out\n"
                ":red_circle: Ping Ted to identify Shamir or Dvich availability for ML/data platform support"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*HIGH — This week*\n"
                ":large_yellow_circle: Review Cindy's role/salary intercept modal designs (Monday midday deadline)\n"
                ":large_yellow_circle: Send Cindy: line cook D5/D30 analysis + applicant flow links for Abby onboarding doc\n"
                ":large_yellow_circle: Listen to Usman's call recordings — track excitement signals\n"
                ":large_yellow_circle: Decide comms agent ownership (you vs. Dana/Fatty/Davi)\n"
                ":large_yellow_circle: Schedule Culinary Agents follow-on call on Indeed-boosting mechanics\n"
                ":large_yellow_circle: Follow up with Jenna on SEO indexing guidance\n"
                ":large_yellow_circle: Decision: headless browser approach for Indeed (risk vs. admin-access route)"
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*MEDIUM — Don't let these slip*\n"
                ":white_circle: Send table name/schema to Anudeep; confirm High Touch with Rohit\n"
                ":white_circle: Loop Tanner into job description & salary recommendation UI design\n"
                ":white_circle: Verify 'Homebase Boost' source display is correct — close the ticket\n"
                ":white_circle: Build Q3 OKR dashboard (track toward 80% healthy jobs)\n"
                ":white_circle: ZipRecruiter follow-up call (1–2 weeks)\n"
                ":white_circle: Write up Salesforce table requirements for Nelson\n"
                ":white_circle: Share Q3 strategy + roadmap docs with full team\n"
                ":white_circle: Analyze starter plan removal: who opted out? Price elasticity implications?"
            )
        }
    },

    {"type": "divider"},

    # ── SECTION 3: KEY ORG INTEL ──
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Key Context to Keep in Mind", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":warning: *Dana is leaving end of September.* Ray already knows. Handle accordingly "
                "when planning Q3 outbound ownership and transition timelines.\n\n"
                ":brain: *Ray's read on you:* 'I trust Manan, he is going to get us out of this problem.' "
                "Low engagement from the team = they trust you, not that they don't care. "
                "Their houses are on fire. Yours is working. Keep shipping.\n\n"
                ":calendar: *Abby starts July 7.* Her first month = source claiming, then auto go-live, then manual intake. "
                "She has an engineering background — lean into it.\n\n"
                ":chart_with_upwards_trend: *Momentum signal:* Trial volume broke 700K for the first time. "
                "'Drive off the lot' showing 49% lift in ICP trial starts. You have wind at your back."
            )
        }
    },

    {"type": "divider"},

    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": (
                    "Chief of Staff digest | Week of Jun 22–26, 2026 | "
                    "13 meetings | 13 decisions documented | Sent Sun Jun 28 @ 5pm PT"
                )
            }
        ]
    }
]

if __name__ == '__main__':
    send_blocks(
        blocks,
        text='Weekly Decision Digest - Jun 22-26, 2026 | 13 meetings | 13 decisions'
    )
