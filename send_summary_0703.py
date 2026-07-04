#!/usr/bin/env python3
"""
End-of-week Slack digest for Manan Kothari
Week: Jun 29 - Jul 3, 2026 (July 4th holiday weekend edition)
Channel: D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'

blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': '🎆 End-of-Week Wrap | Jul 4th Weekend Edition',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Happy Friday before the long weekend, Manan! 🇺🇸 You earned this break. '
                'You had *8 meetings across 4 days* (Jun 29 – Jul 2) — no meetings today since you\'re off. '
                'This was a *massive week* — you killed a flawed feature, pivoted the entire reactivation strategy, '
                'scoped a brand-new recommendations system, and locked the OEM onboarding playbook. '
                'Here\'s everything you decided and what\'s next. 💪'
            )
        }
    },
    {'type': 'divider'},

    # ── BIG STORY ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*🚨 THE BIG STORY: Copy Jobs → Reactivate Jobs Pivot*\n'
                '_(Ray/Manan + Tanner/Manan, Jul 1 | Sprint Lookahead, Jul 2)_\n\n'
                'You discovered Indeed now flags reposted jobs as *duplicates requiring sponsorship* '
                '— even with different descriptions, pay, or shift times. ~50% of copied jobs get *zero applicants* by D5/D30, '
                'directly destroying your North Star metric (70% ICP jobs healthy by D30).\n\n'
                '*Decision:* Kill Copy Jobs entirely. Reactivate Jobs is the only path forward (same job ID = no duplicate flag).\n\n'
                '*Why it works:* Auto-approve if no edits; back in review if edited post-reactivation. '
                'Must re-syndicate across *all* boards (Facebook Jobs, Talroo, ZipRecruiter — not just Indeed). '
                'Secondary win: clears clutter from customers\' closed jobs section.\n\n'
                '*Critical constraint:* Copy job removal and reactivate must ship *simultaneously* '
                '— customers can\'t be left with no way to repost. Carlo flagging as blocker in Linear.'
            )
        }
    },
    {'type': 'divider'},

    # ── ALL DECISIONS ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*📋 All Decisions This Week*'
        }
    },

    # Indeed / Reactivation decisions
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*1. Copy Job Feature — KILLED* _(Jul 1)_\n'
                'Indeed flags copies as duplicates requiring sponsorship, no workaround exists.\n'
                '_Why:_ ~50% copied jobs → 0 applicants by D30. Mission-critical to fix.\n\n'

                '*2. Reactivate = Only Path Forward* _(Jul 1)_\n'
                'Same job ID avoids Indeed\'s duplicate flag. Confirmed with Tanner as buildable.\n'
                '_Action:_ Carlo marks copy job removal as *blocker* on reactivate in Linear.\n\n'

                '*3. Reactivation Logic* _(Jul 2)_\n'
                'Auto-approve if no edits. If edited post-reactivation → back in review (fraud check).\n'
                'Must re-syndicate across all boards: Facebook Jobs, Talroo, ZipRecruiter.\n\n'

                '*4. Job Requisition Concept* _(Jul 1)_\n'
                'Group multiple hiring rounds under one role WITHOUT new job IDs — solves applicant bucket problem.\n'
                '_Action:_ Needs owner. Consider Tanner. Spec to be written.\n\n'

                '*5. Auto-Reactivation at Day 29* _(Jul 1)_\n'
                'If an unclosed job hits Day 29, auto-reactivate on OEM\'s behalf.\n'
                'Tanner confirmed buildable. Needs opt-out UX design (Manan to spec).\n\n'

                '*6. Facebook Jobs — Net New Only* _(Jul 1)_\n'
                'Skip backfill. Enable for net new postings only.\n'
                '_Action:_ Tanner to turn on.\n\n'

                '*7. Indeed Oct 1 Sponsorship Policy* _(Jul 1)_\n'
                'Test reactivation via Ashby to check if ATS reactivations are exempt from sponsorship flag.\n'
                '_Action:_ Ivana to test. Manan to run Claude Code on Indeed policy page for clarification.'
            )
        }
    },

    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*8. ZipRecruiter — Risk Flagged, Unresolved* _(Jul 1)_\n'
                'Burned $2K in 1.5 days. No job-level spend caps available.\n'
                '_Action:_ Find job-level caps or pause Zip spend immediately upon return.\n\n'

                '*9. Homebase Positioning = "Riverboat Guide"* _(Jul 1)_\n'
                'Help OEMs spend smarter and set volume expectations — NOT "we have a special Indeed deal."\n'
                'Framing: personal recruiter / success partner.\n\n'

                '*10. Job Post Recommendations — 3 Areas Scoped* _(Jul 2)_\n'
                'Targets ~1/3 of 800 ICP jobs in Q2 with non-ideal titles.\n'
                '• *Role titles:* flag promo language, pay/shift in title, non-standard names (e.g. "coffee ninja")\n'
                '• *Salary:* flag below-market pay with warning\n'
                '• *Job description:* DS prompt work only, no engineering effort\n\n'

                '*11. Recommendation Modal UX* _(Jul 2)_\n'
                'Blocking modal (no X, dark overlay). Appears after OEM clicks "Next" on job description page.\n'
                '2–4 second wait (DS processing). Add copy: "this may take a couple of seconds."\n'
                'If both recommendations unchecked → button changes "Update and Continue" → "Continue."\n\n'

                '*12. Recommendations as Experiment* _(Jul 2)_\n'
                'Traffic throttle between default and updated job creation flow (not just a kill switch).\n'
                'Monitor drop-off in job creation. Carlo adding to acceptance criteria.\n\n'

                '*13. DS Dependency Timeline* _(Jul 2)_\n'
                'Role rec agent: committed Jul 3. Salary rec agent: end of next week (known spill risk).\n'
                '_Action:_ Whoever implements to align directly with DS on handoff interface.'
            )
        }
    },

    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*14. Transactional Email Trigger Updated* _(Jul 2)_\n'
                'Changed from "0 by Day 1 / under 15 by Day 5" → *"under 5 by Day 3."*\n'
                'Tanner owns (Charmaine out 2 months). Change in SendGrid.\n\n'

                '*15. Source Claiming — Test Kept Clean* _(Jun 30)_\n'
                '3LO excluded from current test — single variable, clean experiment.\n'
                'Source claiming = *priority #1* in every OEM success call (above calendar + job description).\n\n'

                '*16. Source Claiming Call Script Locked* _(Jun 30)_\n'
                'Opening: "personal recruiter / success framing" — NOT "do you have an Indeed account?"\n'
                'Three-bucket playbook confirmed for Sean: no account / has Indeed / other ATS.\n'
                'Test two call-order approaches: source claiming first vs. account overview first.\n\n'

                '*17. OEM Onboarding Two-Phase Motion* _(Jun 29)_\n'
                'Phase 1: SMS/email outreach. Phase 2: in-product to-do.\n'
                '3LO auth + source claiming done *live* with rep on setup call.\n\n'

                '*18. Calendly — In-Product Modal Embed* _(Jun 29)_\n'
                'Not an external link — embed directly. To-do dismisses on confirmed booking, not modal close.\n\n'

                '*19. Resume-Inclusive Matching — Rolling Out* _(Jun 29 Week-in-Review)_\n'
                '100%+ higher accept/advance rate in variant. No further A/B testing needed. Ship it.\n\n'

                '*20. "Personal Recruiter" Messaging Retired* _(Jun 29)_\n'
                'Go all-in on *"Homebase Advantage"* framing across all surfaces.\n\n'

                '*21. Command AI — Officially Dead* _(Jun 29)_\n'
                'No further investment. Deprioritize any Command AI dependencies.\n\n'

                '*22. Sprint Carryover Approach* _(Jul 2)_\n'
                'Items not done by EOW move to 26/14 Excellence project.\n'
                'Team self-assigns upcoming work items (Martin\'s recommendation — not top-down).'
            )
        }
    },
    {'type': 'divider'},

    # ── URGENT ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*🔥 URGENT — Do Not Let This Slide*\n\n'
                '• *Boost Purchase Bug:* 2 reporters in 2 days can\'t buy boosts. Matan tagged you in the boost thread. '
                'Revenue-impacting. Needs investigation before you fully check out. Make sure Matan has a path forward.\n\n'
                '• *ZipRecruiter Spend:* $2K burned in 1.5 days with no caps. Flag to pause or find limits before the weekend bleeds more budget.\n\n'
                '• *Rami\'s Email Blast:* Was due EOD Jun 25 — nearly *10 days overdue.* Status check when you\'re back Monday.'
            )
        }
    },
    {'type': 'divider'},

    # ── MANAN ACTION ITEMS ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*✅ Your Action Items (Prioritized)*\n\n'
                '*When you\'re back Monday:*\n'
                '1. 🔍 Analyze reactivation applicant discount — V1 jobs, CDC table in Databricks (run w/ Claude Code)\n'
                '2. 📄 Run Claude Code on Indeed\'s Oct 1 policy page — clarify which reactivation scenarios trigger sponsorship\n'
                '3. 💸 ZipRecruiter: find job-level spend caps or pause Zip entirely\n'
                '4. 📞 Follow up with Ivana — did she test reactivation via Ashby?\n'
                '5. 📝 Spec: Reactivation UX with applicant expectation-setting (dashboard tile + to-dos)\n'
                '6. 📝 Spec: Job Requisition concept (who builds it — Tanner?)\n'
                '7. 📝 Spec: Auto-reactivation Day 29 opt-out UX\n'
                '8. 📝 Spec: Gaming-detection logic for close → reactivate time windows\n'
                '9. 📋 Send final call script to Sean + confirm Calendly link is shared\n'
                '10. 📋 Draft v3 Q3 goals doc (3-bucket structure — share with Ray before John)\n\n'
                '*Carries from prior weeks:*\n'
                '• Confirm Rami\'s email blast status (VERY overdue since Jun 25)\n'
                '• Send modal copy to Ted (hiring onboarding)\n'
                '• Follow up with Jenna on SEO indexing guidance\n'
                '• Decide comms agent ownership (take or leave with Dana/Fadi/Davi)\n'
                '• Add analytics events to to-do interactions + share with Ugu\n'
                '• Clarify Salesforce column requirements with Aventa\n'
                '• Poached: add baristas/cashiers for broader sample (currently only 3 line cooks)\n'
                '• Confirm Cindy alignment on designs'
            )
        }
    },
    {'type': 'divider'},

    # ── TEAM ACTION ITEMS ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*👥 Team Action Items to Track*\n\n'
                '• *Tanner:* Enable Facebook Jobs (net new only) | SendGrid trigger change (under 5 by D3)\n'
                '• *Carlo:* Mark copy job removal as blocker on reactivate in Linear | Add experiment setup to role rec AC\n'
                '• *Ugu:* Account setup UI → review-ready (was targeting Jul 3 — check status Monday)\n'
                '• *Matan:* Investigate boost purchase bug (2 reporters in 2 days) — REVENUE RISK\n'
                '• *Ivana:* Test reactivation via Ashby → is ATS reactivation exempt from Indeed\'s Oct 1 sponsorship flag?\n'
                '• *Izzy:* Unblocked once Culinary Agents respond to secret handshake request\n'
                '• *Usman:* Share Aventa sync outcome to project channel\n'
                '• *DS Team:* Role rec agent was committed Jul 3; salary rec agent end of next week (watch for spillover)'
            )
        }
    },
    {'type': 'divider'},

    # ── WHAT'S NEXT ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*🔭 What\'s Next — Week of Jul 7*\n\n'
                '• 🆕 *Abby joins Monday Jul 7* — new PM hire with engineering background. Get her ramped on the reactivation pivot and Q3 goals doc.\n'
                '• 🚀 Reactivate jobs + copy job removal ship together (Carlo\'s blocker flag)\n'
                '• 🤖 Role recommendation agent handoff (was committed Jul 3 — confirm it landed)\n'
                '• 💰 OEM Boost: get to the bottom of the purchase bug before it becomes a churn signal\n'
                '• 📊 Source claiming call results from Sean (two call-order approaches)\n'
                '• 🔄 3LO + source claiming sprint (Ugu + Matan + Sean — next sprint scope)\n'
                '• 📈 Q3 goals doc v3 — share with Ray, then John'
            )
        }
    },
    {'type': 'divider'},

    # ── FOOTER ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '_This was a landmark week, Manan. You made a courageous call killing Copy Jobs — '
                'admitting a feature was broken and replacing it with a smarter, cleaner solution takes guts. '
                'The reactivation pivot, the recommendations system, and the OEM onboarding playbook '
                'are all pointing in the right direction. Q3 is yours to win. 🏆_\n\n'
                '_Enjoy the 4th of July weekend. You\'ve earned it. See you Monday! 🎇_'
            )
        }
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'End-of-Week Wrap | Jul 4th Weekend Edition — 8 meetings, 22 decisions, your full action list inside.',
    'blocks': blocks
}


def preview():
    sys.stdout.buffer.write(b'\n=== SLACK MESSAGE PREVIEW ===\n')
    for block in blocks:
        if block.get('type') == 'section':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((text + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'header':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write(('=== ' + text + ' ===\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(b'---\n')
    sys.stdout.buffer.write(b'=== END PREVIEW ===\n')


def send_slack(token):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {token}'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print(f'[OK] Message sent to {CHANNEL}')
            else:
                print(f'[ERROR] Slack API error: {body.get("error")}')
                print(json.dumps(body, indent=2))
    except urllib.error.HTTPError as e:
        print(f'[ERROR] HTTP {e.code}: {e.read().decode()}')
    except urllib.error.URLError as e:
        print(f'[ERROR] URL error: {e.reason}')


token = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN')
)

if token:
    send_slack(token)
else:
    print('[WARN] No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN).')
    print('[WARN] Add the token as a secret in Cursor Dashboard > Cloud Agents > Secrets.')
    print('[WARN] Printing preview instead:\n')
    preview()
    print('\n[INFO] Script completed (preview mode — no message sent).')
