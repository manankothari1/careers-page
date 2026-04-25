#!/usr/bin/env python3
"""Daily Chief of Staff Summary - Apr 25 (covering Apr 24 meetings)"""
import json, os, sys, urllib.request, urllib.error

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
CHANNEL_ID = 'D06E4QMHCNN'

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Briefing \u2014 Friday Apr 24",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan! You crushed it today \u2014 7 meetings, a board debrief, sprint planning, and a full team check-in. Here is every decision you made, why it matters, and exactly what needs to happen next. Let\u2019s get after it. \ud83d\udcaa"
        }
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 1
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 1 \u2014 3LO deploys Monday behind feature gate; prod-only testing*\n*Meeting:* 3LO (12:30 PM) \u2014 Manan, Tanner, Andrew\n\n*What you decided:* Tanner ships the 3LO frontend on Monday behind a feature gate. All testing must happen in production because Indeed provides no sandbox environment. Bob owns backend monitoring and production smoke-testing.\n\n*Why it matters:* Andrew is leaving \u2014 this is the last chance to ship with full context transfer. Shipping behind a gate keeps risk low while enabling real production verification.\n\n*Rationale:* Fake job posts risk Indeed penalties. Staging tests are impossible. Feature-gating gives you a controlled blast radius."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Tanner* \u2014 deploy frontend Mon; gate on; ready for prod testing\n\u2022 *Bob* \u2014 own backend smoke tests + DataDog/Sentry monitoring post-launch\n\u2022 *Manan* \u2014 coordinate with Bob on prod test plan (do this TODAY)"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Tanner: Monday deploy\n\u2022 Bob: test plan before gate opens\n\u2022 Manan: align with Bob by EOD Fri"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 2
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 2 \u2014 3LO seasonal token refresh: watch-and-wait (180-day fix deferred)*\n*Meeting:* 3LO (12:30 PM)\n\n*What you decided:* The current token refresh logic stops refreshing unused tokens after ~53 days. A fix to extend refresh up to 180 days regardless of usage was discussed but NOT committed to. Andrew flagged it; the team deferred it as a future improvement.\n\n*Why it matters:* Seasonal businesses (e.g. ice cream shops) will be forced to reauthenticate every summer if this isn\u2019t fixed. Not urgent for launch, but a real churn risk for seasonal SMBs.\n\n*Rationale:* Andrew is leaving \u2014 not the right time to scope a new behavior. Andrew\u2019s docs on the Google calendar OAuth edge cases can be referenced."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 add to backlog: '3LO: refresh unused tokens up to 180 days for seasonal accounts'\n\u2022 *Bob* \u2014 review Andrew\u2019s token documentation before it\u2019s lost"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Ticket creation: next sprint grooming\n\u2022 Bob: this week while Andrew is still accessible"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 3
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 3 \u2014 Boost modal copy must be fixed NOW; long-term redesign queued*\n*Meeting:* 3LO (12:30 PM)\n\n*What you decided:* The current '8x more applicants' messaging is inconsistent across the three boost modal states. Short-term: fix the copy to be consistent. Long-term: comprehensive modal redesign is on the roadmap.\n\n*Why it matters:* Mixed messaging erodes trust during a conversion moment. This is a customer-facing quality issue live in prod right now.\n\n*Rationale:* Naming migration to 'Sponsored Job' is already decided \u2014 this copy fix is a prerequisite for that rollout."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 write consistent copy for all 3 boost modal states\n\u2022 *Tanner or IBK* \u2014 implement copy update (quick win, no design blocker)\n\u2022 *Manan* \u2014 queue comprehensive modal redesign for post-TLWA sprint"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Copy draft: Mon\n\u2022 Implementation: this sprint\n\u2022 Redesign: post-TLWA"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 4
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 4 \u2014 Divij released from Predicted Roles; existing chips cover 65% for TLWA*\n*Meeting:* Hiring Leads Standup (8:30 AM) \u2014 Manan, Ray, Fadi, Dana, Cindy, Jatin, Nelson +\n\n*What you decided:* Divij will NOT build predicted roles for TLWA. Instead, use the existing industry-tailored prompt chips (already live) to cover 65% of companies. Manan can backfill the remaining 35% manually if there\u2019s time. Divij is freed to work on applicant flow matching and agentic features.\n\n*Why it matters:* Applicant flow is described as an 'existential crisis.' Competition will catch up in ~4 months. Divij\u2019s time is worth far more on marketplace innovation than a nice-to-have personalization feature.\n\n*Rationale:* 65% coverage with chips is good enough for TLWA launch. The remaining 35% is not a showstopper. Grooming is scheduled for Tuesday when more resources are available."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 confirm chips are correctly configured for all industry types\n\u2022 *Manan* \u2014 attempt manual backfill of remaining 35% if bandwidth allows\n\u2022 *Team* \u2014 grooming on Tuesday to finalize dashboard vs careers page placement\n\u2022 *Jatin* \u2014 review Boost documentation + Linear ticket (confirmed in standup)"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Chips audit: before TLWA launch\n\u2022 Grooming: Tuesday\n\u2022 Jatin: Boost ticket review EOD today"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 5
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 5 \u2014 Sprint 2610 priority stack locked: Purchase Boost \u2192 V1\u2192V2 migration \u2192 OTP \u2192 JobGet*\n*Meeting:* Prioritize List(s) (12:00 PM) \u2014 Manan, Dana, Cindy, Fadi\n\n*What you decided:* Sprint 2610 top 4 priorities in order: (1) Purchase Homebase Boost \u2014 billing done, XML feed updates needed for CPC; (2) Migrate V1\u2192V2 \u2014 backfill, one-click repost, deprecate V1; (3) One-Time Purchase job posts \u2014 replaces $30 plan; (4) JobGet Easy Apply redirect fix. ZipRecruiter CPC and Resume Matching are secondary.\n\n*Why it matters:* Trial goal is 21k in H1; you\u2019re at ~100/week and need 800/week. Every item on this list is either a revenue unlock or a conversion improvement.\n\n*Rationale:* Billing team already built most of the backend for Boost and OTP \u2014 these are nearly free wins. V1\u2192V2 migration is TLWA-critical. JobGet Easy Apply redirect is leaking applicants today."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Bob + Jatin* \u2014 review sprint estimates async (needed for planning)\n\u2022 *Manan* \u2014 schedule weekly/bi-weekly prioritization cadence with Dana, Cindy, Fadi\n\u2022 *Manan* \u2014 write project brief templates with business context (not just engineering overviews)\n\u2022 *Dana* \u2014 coordinate XML feed updates for CPC changes (Boost purchase dependency)\n\u2022 *Team* \u2014 backlog cleanup: 307 items, 200+ are Sentry tickets \u2014 bulk-close or triage"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Estimates: before next sprint start\n\u2022 Backlog cleanup: this week\n\u2022 Brief template: by Mon\n\u2022 Cadence: schedule this week"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 6
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 6 \u2014 Resume Matching: 50/50 blend approach confirmed; endpoint creation next*\n*Meeting:* Prioritize List(s) (12:00 PM)\n\n*What you decided:* Resume Matching uses a 50/50 blend of resume + screener signals (as agreed). Divij\u2019s work is ready for consumption. The blocker is endpoint creation \u2014 this is secondary priority in Sprint 2610.\n\n*Why it matters:* Resume matching directly improves applicant quality scores, which feeds the 'healthy job rate' problem (currently 8% \u2014 way too low).\n\n*Rationale:* Divij\u2019s ML work is already done. This is a pure engineering integration task. Worth unblocking soon."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Engineering* \u2014 create resume matching endpoint (secondary sprint priority)\n\u2022 *Manan* \u2014 confirm Divij\u2019s work is fully documented before he context-switches to agentic"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Endpoint: Sprint 2610 (secondary)\n\u2022 Documentation confirm: this week"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 7
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 7 \u2014 Linear structure locked: triage = project-less; Proposal \u2192 Prototype \u2192 Build workflow*\n*Meeting:* Prioritize List(s) (12:00 PM)\n\n*What you decided:* Everything in triage stays project-less until ready for planning. Items move to projects when going from Proposal \u2192 Prototype. Disable auto-Slack-channel creation during project conversion to avoid noise. Naming cleaned up (Pathways to Boost vs Boost V1 confusion resolved).\n\n*Why it matters:* 307 items in backlog with no clear workflow is a planning tax. This structure gives the team a shared mental model.\n\n*Rationale:* The Linear agent already created 215 tickets from Granola + Slack history \u2014 without a clear intake system, this becomes debt immediately."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 document the Proposal/Prototype/Build definitions and share with team\n\u2022 *Dana* \u2014 audit existing projects, convert any misplaced triage issues\n\u2022 *Team* \u2014 disable Slack channel auto-creation for future project conversions"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Definitions doc: Mon\n\u2022 Audit: this week"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 8
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 8 \u2014 Marketplace strategy: must be hypothesis-driven; 2-hr brainstorm moved to next week*\n*Meeting:* Manan / Ray (2:00 PM)\n\n*What you decided:* Before executing on marketplace ideas (QR code agent, applicant CRM, re-engage past employees), you will research hypothesis frameworks and map assumptions explicitly. The 2-hour brainstorming session moves from 2 weeks out to NEXT WEEK. Ray will stay hands-off to avoid biasing your research.\n\n*Why it matters:* The board gave explicit permission to spend hiring margin on buying applicants. This is a significant strategic unlock. Getting the framework right before building is how you avoid wasted engineering cycles.\n\n*Rationale:* Ray\u2019s point: the team builds as if the idea is the final answer vs. testing the hypothesis. The QR code agent example has multiple untested assumptions. Josh Leverton\u2019s spreadsheet approach was cited as a reference model."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 research hypothesis-driven product frameworks (start tonight or tomorrow AM)\n\u2022 *Manan* \u2014 schedule 2-hr marketplace brainstorm for next week (not 2 weeks out)\n\u2022 *Manan* \u2014 map hypotheses for: (a) owners willing to spend, (b) prev applicants as source, (c) former employees as source\n\u2022 *Manan* \u2014 investigate Indeed API dashboard link issue (jobs link to dashboard, not job post)"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Framework research: weekend\n\u2022 Brainstorm scheduled: Mon\n\u2022 Hypothesis map: before brainstorm\n\u2022 Indeed API investigation: Mon"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 9
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 9 \u2014 HB Assistant integration: hiring team defines tools + structured outputs; team autonomy preserved*\n*Meeting:* Team Check-in (2:30 PM)\n\n*What you decided:* The hiring team will define their own tools (job cards, candidate cards, structured outputs) for HB Assistant integration. Domain-specific components stay owned by hiring. Shared infrastructure via orchestrator. Architecture principle: full feature set works WITHOUT assistant open.\n\n*Why it matters:* Agentic era experimentation starts next Thursday. The hiring team needs to be ready with clear tool definitions or they\u2019ll be playing catch-up.\n\n*Rationale:* Announced in the all-hands as a key Q2 initiative. The pattern (separate but integrated, user-initiated) mirrors Google Gemini + Sheets."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 schedule show-and-tell with HB Assistant team (announced in check-in)\n\u2022 *Hiring team* \u2014 define tool list + structured output specs before next Thursday\n\u2022 *Jatin* \u2014 lead agentic demo on May 4 (Codex/Claude good-cop/bad-cop format)"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Show-and-tell: schedule this week\n\u2022 Tool definitions: by next Thursday\n\u2022 Jatin demo: May 4"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # DECISION 10
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udfe2 DECISION 10 \u2014 TLWA = team 'rebirth' moment; marketplace innovation starts immediately after*\n*Meeting:* Team Check-in (2:30 PM) + Q2 Town Hall (10:00 AM)\n\n*What you decided:* TLWA launch is the team\u2019s rebirth moment. Post-TLWA, the focus immediately shifts to marketplace innovation (applicant flow, agentic features). Two existential challenges named by board: (1) more awareness + trial starts, (2) applicant flow. Board explicitly approved spending hiring margin on buying applicants.\n\n*Why it matters:* The board said the product is sellable when customers see demos, and gave strategic permission to spend. You have a green light. The question is speed of execution.\n\n*Rationale:* 'Cognitive dissonance' was the board\u2019s exact words \u2014 everything looks good but results aren\u2019t there yet. The window to act is now."
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*\u2705 Action Items*\n\u2022 *Manan* \u2014 draft marketplace innovation roadmap (first cut) for post-TLWA sprint\n\u2022 *Manan* \u2014 align with Ray on 'spending hiring margin' \u2014 what does this mean tactically? (JobGet budget? Talroo expansion?)\n\u2022 *Matan* \u2014 post Boost plan to #leads + survey customers on hiring spend (still open from Apr 23)"
            },
            {
                "type": "mrkdwn",
                "text": "*\ud83d\udcc5 Due*\n\u2022 Roadmap first cut: next week\n\u2022 Tactical alignment with Ray: Mon\n\u2022 Matan survey: OVERDUE \u2014 this week"
            }
        ]
    },
    {"type": "divider"},

    # ============================================================
    # OVERDUE ITEMS
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udd34 OVERDUE \u2014 Items that need your immediate attention*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *TLWA brief to Ted* \u2014 20+ DAYS OVERDUE. Send today or first thing Saturday AM.\n\u2022 *Nelson: metro_area + bucketed_role + matching_roles* \u2014 OVERDUE since Apr 8. What\u2019s the status?\n\u2022 *Matan: post Boost plan to #leads + customer survey* \u2014 was due Apr 23. Chase this today.\n\u2022 *Andrew: Indeed status endpoint* \u2014 was due Apr 23. Confirm it\u2019s live before he\u2019s gone.\n\u2022 *Predicted roles: Linear project + channel needed* \u2014 still open, nothing created.\n\u2022 *Greenlight Manual Mode: Cindy QA done, on Manan* \u2014 blocking Cindy.\n\u2022 *Saja (Talroo): send CPA categories + configure campaign* \u2014 revenue at risk.\n\u2022 *Justin: re-run descriptions batches 93-100 + Supabase RLS audit* \u2014 security + content gap."
        }
    },
    {"type": "divider"},

    # ============================================================
    # UPCOMING MILESTONES
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83d\udcc5 UPCOMING MILESTONES*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u2022 *Mon Apr 28* \u2014 3LO frontend deploys (Tanner); marketplace brainstorm scheduled; Bob test plan ready; Boost copy draft done\n\u2022 *Tue Apr 29* \u2014 Sprint grooming (Predicted Roles placement decision)\n\u2022 *Thu May 1* \u2014 Agentic era experimentation starts; HB Assistant show-and-tell\n\u2022 *Mon May 4* \u2014 Jatin agentic demo (Codex/Claude good-cop/bad-cop); Fadi candidate profile redesign starts; Greenlight Manual Mode must be off Manan\u2019s plate\n\u2022 *~May 5* \u2014 Juan risk logic review; Auto syndication watch-and-wait window closes\n\u2022 *H1 Goal* \u2014 21k trials (need 800/week; currently at ~100/week \u2014 this is the north star)"
        }
    },
    {"type": "divider"},

    # ============================================================
    # FOOTER
    # ============================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\ud83e\udde0 Today\u2019s Scorecard:* 7 meetings | 10 decisions | Board debrief absorbed | Sprint locked | Team transition managed (Andrew\u2019s farewell) | Strategic direction set (hypothesis-driven marketplace)\n\n_You\u2019re building something real, Manan. The board sees it \u2014 now it\u2019s about execution velocity. Get some rest this weekend. \ud83c\udf1f_"
        }
    }
]

payload = {
    'channel': CHANNEL_ID,
    'text': 'Chief of Staff Daily Briefing - Friday Apr 24',
    'blocks': blocks
}

def send_slack():
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + SLACK_TOKEN
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print('SUCCESS: Slack message sent.')
            else:
                print('ERROR from Slack API:', body.get('error', 'unknown'))
                sys.exit(1)
    except urllib.error.URLError as e:
        print('NETWORK ERROR:', e)
        sys.exit(1)

def preview():
    sys.stdout.buffer.write(b'\n=== PREVIEW (no SLACK_TOKEN) ===\n')
    sys.stdout.buffer.write(json.dumps(payload, indent=2, ensure_ascii=False).encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(b'\n================================\n')

if SLACK_TOKEN:
    send_slack()
else:
    print('SLACK_TOKEN not set \u2014 printing preview.')
    preview()
