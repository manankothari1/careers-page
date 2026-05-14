#!/usr/bin/env python3
"""
Daily Decision Summary — Wednesday May 13, 2026
Chief of Staff summary for Manan Kothari, PM @ Homebase
Slack channel: D06E4QMHCNN
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
            'text': '\U0001f4cb  Chief of Staff Daily Brief  \u2014  Wednesday, May 13',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Manan \u2014 you had a seriously *productive* day today. '
                'Two back-to-back deep-dives on Indeed Sponsored Jobs unlocked major progress. '
                'You diagnosed a blocking bug, confirmed the fix, AND mapped the entire product flow with Cindy. '
                'That\'s the kind of day that makes sprint goals feel real. Here\'s your full debrief. \U0001f525'
            )
        }
    },
    {'type': 'divider'},

    # ───── MEETING 1 ─────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4cd Meeting 1 of 2 \u2014 3LO Debug Session*\n'
                '_11:30 AM PDT \u00b7 Manan, Tanner, Jatin_'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3af Decisions Made*\n\n'
                '*1. Root cause confirmed \u2014 missing OAuth scope (UNBLOCKED \u2705)*\n'
                '> The "Forbidden" error from the Indeed Job Status API was caused by a missing '
                '`employer.hosted_job` scope. We were only requesting `employer_access` and `offline_access`. '
                'Without the hosted_job scope, the token can\'t read the job data subtree. Fix is clear and surgical.\n\n'
                '*2. No source claiming required*\n'
                '> Gustavo\'s earlier suggestion about "source claiming" was referring to company page management '
                '(Glassdoor-style employer branding). 3LO authentication alone \u2014 with the correct scopes \u2014 '
                'is sufficient to fetch job status. Source claiming is explicitly *descoped* from the roadmap.\n\n'
                '*3. Job creation stays on 2LO (no change needed)*\n'
                '> Even after 3LO is connected, jobs continue to be created via two-legged auth programmatically. '
                'This is intentional and correct. No change to the job creation flow.\n\n'
                '*4. OAuth credentials to be stored in 1Password*\n'
                '> The Indeed OAuth client ID and credentials need to be documented in 1Password and shared '
                'via Slack to Tanner. This is a security/vendor hygiene fix that\'s long overdue.\n\n'
                '*5. Indeed company page management \u2014 explicitly NOT on the roadmap*\n'
                '> The "fast responder" badge on Indeed could theoretically drive applicant volume via '
                'disposition sync, but until there\'s evidence it moves the needle, this stays out of scope.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u26a1 Action Items \u2014 3LO*\n\n'
                '\u25b8 *Tanner \u2014 TODAY/TOMORROW*: Add `employer.hosted_job` to OAuth scope config '
                'in codebase + write unit test confirming all 3 scopes (`employer_access`, `offline_access`, '
                '`employer.hosted_job`) are present in the constructed authorize URL\n'
                '\u25b8 *Tanner \u2014 TODAY*: Email Gustavo requesting enablement of `employer.hosted_job` '
                'scope on Indeed\'s partner console\n'
                '\u25b8 *Tanner \u2014 TODAY*: Share Indeed OAuth credentials via Slack + store in 1Password\n'
                '\u25b8 *Manan + Tanner \u2014 May 14*: Run end-to-end test session using Manan\'s Indeed '
                'account to confirm scope fix resolves the Forbidden error\n'
                '\u25b8 *Jatin*: No further action needed on 3LO \u2014 confirmed out of scope for this fix'
            )
        }
    },
    {'type': 'divider'},

    # ───── MEETING 2 ─────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4cd Meeting 2 of 2 \u2014 Cindy / Manan: Sponsored Jobs API Flow*\n'
                '_1:00 PM PDT \u00b7 Manan, Cindy_'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3af Decisions Made*\n\n'
                '*6. Boost messaging: let Metan + Usman drive first, then review*\n'
                '> Cindy raised a legitimate UX concern: customers don\'t understand what "Home Base Boost" '
                'means vs. "Indeed Sponsored Post." Rather than preempt, you\'re letting Metan/Usman develop '
                'the messaging brief first \u2014 you and Cindy will be reviewers. Smart move: gather evidence '
                'before designing around an assumption.\n\n'
                '*7. Boost copy direction locked: multi-partner framing, no partner names*\n'
                '> Don\'t say "career page boost." Don\'t name Talroo. The right framing is: '
                '"your job is distributed across multiple partner job boards." This builds trust '
                'without confusing customers or creating dependencies on specific partner brands.\n\n'
                '*8. Kill the Boost to-do / promo reminder*\n'
                '> The boost "to-do" reminder was also functioning as a promo email. With Boost being added '
                'directly into the job creation flow, customers will see it enough. The to-do is a promo, '
                'not a genuine task. Kill it \u2014 it creates noise and dilutes the real entry point.\n\n'
                '*9. Indeed Sponsored flow = full-screen experience (no modal)*\n'
                '> The Indeed OAuth flow, billing setup, and account verification cannot live in a modal. '
                'It\'s a multi-step process with redirects. Full-screen is the only viable UX.\n\n'
                '*10. UI ownership boundary locked*\n'
                '> *Home Base owns:* email input dialog (to trigger Indeed account setup) + '
                'budget/campaign setup UI\n'
                '> *Indeed owns:* account verification, billing setup (credit card), OAuth flow\n'
                '> This is clean. Don\'t bleed into Indeed\'s territory.\n\n'
                '*11. Billing stays 100% with Indeed \u2014 no HB refund handling needed*\n'
                '> Customers enter their credit card with Indeed directly. Indeed charges them. '
                'If they don\'t use the full budget, we don\'t issue refunds \u2014 Indeed handles it. '
                'This keeps Homebase out of payments complexity entirely for v1.\n\n'
                '*12. Campaign predictions API \u2014 DESCOPED from v1*\n'
                '> The predicted cost/volume tool that Indeed shows before budget is set is its own '
                'separate build. Not required for v1 Sponsored Jobs to function. Clearly marked as future work.\n\n'
                '*13. Show one-time campaign first; monthly recurring is secondary*\n'
                '> Given HB jobs expire at 30 days, a recurring monthly campaign creates edge cases. '
                'Default to one-time sponsorship in the UI. Confirm with Gustavo if we can limit the '
                'API to one-time only.\n\n'
                '*14. End date max = job expiry date*\n'
                '> A sponsored campaign cannot outlive the job listing. We\'ll enforce this in the UI: '
                'end date picker max = the day the job expires. Edge case: what if they boost on day 29? '
                'They get 1 day. That\'s fine for v1.\n\n'
                '*15. Stop sponsorship capability is required for v1*\n'
                '> Two use cases: (a) customer wants to stop early before end date (got enough applicants), '
                '(b) job goes inactive on HB before campaign ends (we auto-cancel). '
                '"Manage" option needed in the boost modal. Wire to Indeed\'s stop sponsorship API.\n\n'
                '*16. 3LO access revocation: v1 = support-only, no UI*\n'
                '> If a customer wants to disconnect their Indeed account from HB, they\'ll need to reach '
                'out to support. Not building a revocation UI in v1. Low risk given usage levels.\n\n'
                '*17. Sponsored job analytics: descoped from v1*\n'
                '> We won\'t surface campaign performance data in-app for v1. If customers want it, '
                'they can view it directly on Indeed. We can link out if needed.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u26a1 Action Items \u2014 Sponsored Jobs Flow*\n\n'
                '\u25b8 *Manan \u2014 DONE (during call)*: Email Gustavo 4 open technical questions:\n'
                '  \u2003\u2022 Is campaign predictions API required for Sponsored Jobs?\n'
                '  \u2003\u2022 Can we limit API to one-time campaigns only (no monthly recurring)?\n'
                '  \u2003\u2022 Is campaign objective setup required?\n'
                '  \u2003\u2022 What are the secondary user authorization requirements?\n\n'
                '\u25b8 *Cindy*: Create base flow diagram for the entire end-to-end Indeed Sponsored Jobs process '
                '(for Monday review with Manan)\n'
                '\u25b8 *Cindy*: Full-page boost design review with Matan (was due today \u2014 confirm status)\n'
                '\u25b8 *Manan*: Review Metan/Usman messaging brief when ready \u2014 share with Cindy to review together\n'
                '\u25b8 *Manan + Cindy*: Follow-up meeting Monday to review Gustavo\'s responses + Cindy\'s flow diagram\n'
                '\u25b8 *Team*: Research criteria for keeping HB jobs active beyond 30 days '
                '(edge case for sponsored campaign end dates)'
            )
        }
    },
    {'type': 'divider'},

    # ───── CARRY-FORWARD ─────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u23f0 Don\'t Sleep On These \u2014 Carry-Forward Items*\n\n'
                '\u25b8 *Ray\'s detailed plan \u2014 DUE TODAY EOD* \u2014 make sure he delivers '
                '(6-week vision: OEM spend + marketplace)\n'
                '\u25b8 *Boost Pathways review \u2014 TODAY* \u2014 confirm this happened or reschedule\n'
                '\u25b8 *Vision doc \u2014 URGENT* \u2014 3 things true by year-end; exec presentation is May 19 '
                '(that\'s 6 days away \u2026 \U0001f6a8)\n'
                '\u25b8 *Matan one-pager* \u2014 Boost sales motion kicks off May 25-26; pinger needs to be '
                'drafted NOW (13 days away)\n'
                '\u25b8 *Cindy designs due May 23; she\'s OOO May 25+* \u2014 all feedback must close before '
                'she leaves for BC\n'
                '\u25b8 *Rami onboarding* \u2014 joining in 2-3 days; prep context doc + Vij DS review is urgent\n'
                '\u25b8 *Tomorrow (May 14, Fri)*: Optional Usman sales training 12:30pm + Martin/Manan 1:1 follow-up'
            )
        }
    },
    {'type': 'divider'},

    # ───── OPEN QUESTIONS ─────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u2753 Open Questions Pending Gustavo (Indeed)*\n\n'
                '1. Is campaign predictions API required for Sponsored Jobs API?\n'
                '2. Can we limit to one-time campaigns only (skip monthly recurring)?\n'
                '3. Is campaign objective setup mandatory or skippable?\n'
                '4. Secondary user authorization \u2014 what\'s the actual requirement?\n'
                '5. Will `employer.hosted_job` scope resolve the Forbidden error for job status? '
                '(Tanner\'s email + test tomorrow will confirm)\n\n'
                '_Gustavo\'s response speed will determine if Indeed Sponsored Jobs ships in 2611 or slips. '
                'Chase him if no reply by EOD Thursday._'
            )
        }
    },
    {'type': 'divider'},

    # ───── CLOSING ─────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4aa Today\'s Score*\n\n'
                'You turned a vague blocking bug into a confirmed root cause AND a test plan in one morning session. '
                'Then you spent the afternoon with Cindy making real architectural decisions on the most complex '
                'product surface in your sprint. The 3LO scope fix is surgical, the flow ownership is clear, '
                'and you\'re not over-building v1. This is *exactly* the kind of focused, high-leverage day '
                'that compounds into a killer demo on May 19.\n\n'
                'The only things standing between you and shipping Sponsored Jobs are Gustavo\'s inbox and '
                'Tanner\'s PR. Both are in motion. \u2728\n\n'
                '_\u2014 Your Chief of Staff_'
            )
        }
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'text': 'Daily Decision Summary \u2014 Wednesday May 13, 2026'
}


def preview():
    out = '\n===== SLACK MESSAGE PREVIEW =====\n'
    out += f'Channel: {CHANNEL}\n'
    out += '---------------------------------\n'
    for block in blocks:
        if block.get('type') == 'section':
            text_obj = block.get('text', {})
            out += text_obj.get('text', '') + '\n\n'
        elif block.get('type') == 'header':
            out += '### ' + block['text']['text'] + ' ###\n\n'
        elif block.get('type') == 'divider':
            out += '---\n\n'
    out += '=================================\n'
    sys.stdout.buffer.write(out.encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()


def send():
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=body,
        headers={
            'Authorization': f'Bearer {TOKEN}',
            'Content-Type': 'application/json; charset=utf-8'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('ok'):
                print(f'[OK] Message sent to {CHANNEL}')
            else:
                print(f'[ERROR] Slack API error: {result.get("error")}')
                preview()
    except urllib.error.URLError as e:
        print(f'[ERROR] Network error: {e}')
        preview()


if __name__ == '__main__':
    preview()
    if TOKEN:
        print('\n[INFO] Slack token found. Sending message...')
        send()
    else:
        print('\n[WARN] No SLACK_TOKEN found. Add it in Cursor Dashboard > Cloud Agents > Secrets.')
        print('[INFO] Preview above is what would be sent.')
