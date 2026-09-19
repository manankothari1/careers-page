#!/usr/bin/env python3
"""
Daily digest for Manan Kothari — Sep 18, 2026 (Yosemite departure day)
Sends to Slack DM channel D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'

TOKEN = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN') or
    ''
)

blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': '🏔️ Manan\'s Daily Digest — Friday, Sep 18, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Day Grade: A+* | Last day before Yosemite. You cleared 3 substantive meetings, locked intent signals placement, shaped Q4 growth strategy, AND hardened fraud defenses — all before hitting the road. Extremely productive send-off day.\n\n*Theme: INTENT SIGNALS LOCKED · GROWTH STRATEGY SET · FRAUD DEFENSE ADVANCING · TALENT POOL CONSENT SCOPED · LP CLEANUP BEFORE PAID SPEND*'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*📅 Today\'s Meetings (3)*\n• 8:30am — Hiring Leads Standup (Fadi, Matan, Jatin, Jon W, Skye)\n• 10:30am — Hiring <> Growth (Matan, Meg, Skye, Chy, Brennan)\n• 11:30am — Khrystyna / Manan (1:1 fraud + safety)'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*✅ Decisions Made Today*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*1. Intent Signals Placement — LOCKED* _(Hiring Leads Standup)_\nHiring tab ruled out. Payroll is the highest-signal surface. Three placements confirmed:\n  • End-of-payroll summary modal (\'$700 in overtime this period → start hiring trial\')\n  • Payroll Journal for aggregate view (\'$16K overtime over 3 months\') — Jatin\'s addition\n  • Persistent in-product anchor so users can return after dismissing\n  • Post-payroll email reinforcing the message\n*Why:* Overtime pain is felt most acutely at the moment you see the bill. Payroll is the smoking gun, not a hiring tab someone has to navigate to.\n_Next: Fadi drafts full proposal for Gabe (Payroll PM) + Alexis before you return Sep 22._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*2. Talent Pool Opt-In Model — Direction Set* _(Hiring Leads Standup)_\nTwo models debated: opt-out by default (organ donor) vs. explicit pre-checked opt-in.\nConsent scoped by segment:\n  • *Fresh applicants:* opt-in/out via apply flow or screener link click\n  • *Previous employees:* update T&Cs — Homebase may contact them post-tenure\n  • *Previous applicants:* ⚠️ legally gray — T&S team input required before acting on historical data\n  • *SMS \'STOP\':* must only suppress talent pool messages, NOT all marketing — scope to this motion in Iterable\n*Why:* Line cooks skip screeners but are still strong candidates — breadth of pool matters for Q4 quality filtering to work. You want volume first.\n_Next: Manan kicks off thread to move this forward; Matan maps full comms journey (SMS + email)._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*3. Q4 Growth Positioning — Aligned with Growth Team* _(Hiring <> Growth)_\nKey strategic calls:\n  • Q4 growth dollars = *net new signups only* — not existing customer upsell (that\'s LCM)\n  • Reframe: Homebase is an *education-first* platform, not just an intent capture engine\n  • Hiring positioned as a *cross-sell lever*: bring users in via hiring pain, then expand to the suite\n  • ICP nuance: FFH/F&B \'just need a pulse fast\' — *week-to-hire isn\'t a moat*. Semi-skilled industries that need AI screening + candidate profiling = better fit\n  • Winning value props to test: (a) speed when time-constrained, (b) confidence via Homebase expertise, (c) labor cost savings from proactive signals\n  • Proactive signal idea: detect shift swaps/overtime → prompt hiring *before* a vacancy hits\n*Why:* 80% of hiring users are already customers. The real unlock is the 15% who sign up with hiring intent — get them in, then cross-sell.\n_Next: Content articles fast to produce (Profound gap analysis), Superline creator ad test, LP cleanup BEFORE scaling paid spend._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*4. Hiring LP — Hold Paid Spend Until Cleaned Up* _(Hiring <> Growth)_\nPage issues identified:\n  • Pricing for hiring add-on is unclear (3rd most visited, highest-converting page)\n  • Feature-heavy with outdated beta UI screenshot\n  • Hiring not listed as signup reason in app flow (~20% of signups)\nDecision: *do not scale paid hiring traffic until* pricing module added, copy is benefit-led, demo embedded, screenshot updated.\n*Reference benchmark: 7shifts LP.*\n_Next: Matan + Meg own LP cleanup. Brian embeds product demo. Antoine restructuring page. Hold Testimonial Hero video investment._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*5. Fraud: Separate True Fraud vs. ToS Violations* _(Khrystyna 1:1)_\nTwo categories currently conflated — now formally separated:\n  • *True fraud:* MLM schemes, impersonation, fake businesses\n  • *ToS violations:* email/phone numbers in job posts (partner board rules)\nFraud model improved significantly over past 6 weeks (more categories, rigorous eval). Gap: *no defined end-to-end remediation workflow* — who reviews, on what criteria, what action follows.\n*Why it matters:* Juan was updating fraud prompts without testing. Support is manually invalidating accounts one-by-one (10+ per location = hours). This is a massive ops drain and a liability.\n_Next: Khrystyna drafts incident response workflow (job removal, applicant retention 4yr, team ownership). Manan approves async._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*6. Company-Level Fraud Check — Direction Set* _(Khrystyna 1:1)_\n  • Current: largely manual (Michael\'s team). ~50% of medium/high-risk companies get approved → over-flagging\n  • Laura + Ted leading a new Homebase-level company check with DS. Still in planning.\n  • This should sit *outside hiring* — covers all products (payroll, cash out, etc.)\n  • Recommendation pushed: *EIN verification* like Indeed requires\n_Next: Khrystyna raises EIN approach with Laura before October Toronto visit._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*7. Bulk Account Invalidation — Escalated to Stitch Team* _(Khrystyna 1:1)_\nCurrently support invalidates each user account (email, phone, Stitch ID) one-by-one. One fraudulent location = 10+ accounts = hours of manual work.\nDecision: reach out to Andy (or Jonathan) on the identity/Stitch team to build a bulk invalidation solution in the admin panel.\n*Also resolved:* OTP is live and working. Company-level verification = users don\'t re-verify on every new job post. Wider rollout pending final confirmation.\n_Next: Khrystyna contacts Andy/Jonathan on Stitch team._'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*8. Culinary Agents Pricing Modal — Design Feedback Delivered* _(Hiring Leads Standup)_\nFadi\'s 10th+ iteration reviewed. Key direction:\n  • Capitalize \'Agents\' consistently\n  • All tier descriptions → 2 lines for alignment\n  • Add clearer tier differentiation (why pick one over another)\n  • CTA: \'Boost Post\' preferred (Jatin) over \'Get Boost\' / \'Apply Boost\'\n  • Purple border on recommended tier = too subtle; lilac preferred to avoid overusing dark purple\nDesign logic will be dynamic.\n_Next: Fadi iterates on feedback. No blocker on Manan\'s end._'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*🎯 Action Items by Owner*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*You (Manan) — when you\'re back Sep 22:*\n• 🔴 Intent signals deck to Gabe — early week of Sep 22 (FIRST THING)\n• 🔴 Kick off talent pool consent thread (you said you\'d do it)\n• 🔴 Review + approve Khrystyna\'s incident response workflow async\n• 🔴 Indeed Easy Apply PDF compliance doc — due Sep 30 (8 days). Submit asap after return.\n• 🟡 EarnBetter follow-up (Jon Salzberg) — 15+ days overdue\n• 🟡 Departures signal conflict docs (Zane, Sean, Jon W, Bobby) — 19+ days overdue\n• 🟡 Marina / Mundo Academy reply — 9+ days late\n• 🟡 IBK JD A/B signal pull — 3+ weeks overdue\n• 🟡 Review Fadi\'s intent signals proposal (Gabe/Alexis deck)'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Fadi (frizk@joinhomebase.com):*\n• Draft intent signals proposal for Gabe (Payroll PM) + Alexis — all 4 surfaces\n• Create Linear project for Copy + Reactivate\n• Map 3-week reactivation window as separate flow\n• Get Alexis\'s input on payroll placement for intent signals'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Matan (mzion@joinhomebase.com):*\n• Map full applicant communication journey (SMS via Twilio + email via SendGrid)\n• Identify opt-in placement + coordinate with Jatin on SMS gaps\n• Hiring LP cleanup with Meg: pricing module, benefit-led copy, updated screenshot\n• Ask Brian to embed product demo on hiring LP\n• Continue Antoine LP restructure (adding testimonials + numbers)'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Khrystyna (kmanko@joinhomebase.com):*\n• Draft hiring incident response workflow (job removal, 4yr applicant retention, team ownership)\n• Raise EIN-style company verification approach with Laura — before Toronto (October)\n• Contact Andy (or Jonathan, Stitch/identity team) about bulk account invalidation in admin panel\n\n*Chy (cseng@joinhomebase.com):*\n• Reach out to Superline about a hiring-focused creator ad (they\'re already using full Homebase suite)\n\n*T&S Team:*\n• Input on historical previous-applicant consent legality — forward-only or retroactive?\n\n*Jatin (jbhandari@joinhomebase.com):*\n• Iterable Steps 2-4 fix (email pipeline) — still in sprint'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*🚨 CRITICAL — Don\'t Let These Slip While You\'re in Yosemite*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*🔴 David (Indeed Product) intro window closes SEP 21 — in 3 days.*\nYou are OOO Sep 18-21. This window closes while you\'re at the campsite. If you have cell service at Diamond O — even a 5-minute email to Catherine or your Indeed ATS contact to keep the thread warm would be worth it. This is a *once-in-a-suspension* relationship reset.\n\n*🔴 Indeed Feed Still Suspended — Day 26.*\nFraud evidence package → Jessica Kanaskie. 2-3 week review ongoing. No update expected while OOO but flag for Sep 22 first thing.\n\n*🟡 Q4 OKRs locked Sep 18.* Hope you got your thoughts in before departure. If not, surface to Skye immediately Sep 22.'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*🏕️ Yosemite + Sep 22 Exec Review Prep*\n\nYou crushed it today. Three meetings, all substantive, all with clear outputs. You\'re leaving with:\n• Intent signals direction locked (Fadi has the ball)\n• Fraud process finally getting operationalized (Khrystyna has the ball)\n• Growth team aligned on Q4 strategy (Matan + Meg have the ball)\n• Talent pool consent framework scoped (thread for you to kick off)\n\n*When you get back Sep 22, your first 2 hours matter:*\n1. Intent signals deck to Gabe — this week\n2. Exec Review prep — your first as Senior PM. Come in with a clear Q4 narrative (trial journey, quality, talent pool). Skye was writing hers by EOW.\n3. David (Indeed) — any reachable thread to extend the window\n\nEnjoy Diamond O. You earned it. 🌲⛺'
        }
    },
    {'type': 'divider'},
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': 'Chief of Staff digest | Sep 18, 2026 | 3 meetings reviewed | Powered by Granola + Cursor'
            }
        ]
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'text': 'Manan\'s Daily Digest — Sep 18, 2026 | Day Grade A+ | INTENT SIGNALS LOCKED · GROWTH STRATEGY SET · FRAUD DEFENSE ADVANCING'
}


def preview():
    output = '\n=== PREVIEW (no Slack token found) ===\n'
    output += 'TO: ' + CHANNEL + '\n'
    output += 'TEXT: ' + payload['text'] + '\n\n'
    for b in blocks:
        if b.get('type') == 'section' and 'text' in b:
            output += b['text']['text'] + '\n'
        elif b.get('type') == 'header':
            output += '== ' + b['text']['text'] + ' ==\n'
        elif b.get('type') == 'divider':
            output += '---\n'
        elif b.get('type') == 'context':
            for el in b.get('elements', []):
                output += el.get('text', '') + '\n'
    output += '\n=== END PREVIEW ===\n'
    sys.stdout.buffer.write(output.encode('utf-8', errors='replace'))


if not TOKEN:
    preview()
    sys.exit(0)

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=data,
    headers={
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TOKEN,
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('✅ Slack message sent successfully to', CHANNEL)
        print('ts:', result.get('ts'))
    else:
        print('❌ Slack API error:', result.get('error'))
        print('Full response:', json.dumps(result, indent=2))
        preview()
        sys.exit(1)
except urllib.error.HTTPError as e:
    print('❌ HTTP error:', e.code, e.reason)
    preview()
    sys.exit(1)
except Exception as e:
    print('❌ Unexpected error:', e)
    preview()
    sys.exit(1)
