#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Wednesday Oct 21, 2026 (PDT)
Sent at midnight UTC (5pm PDT) to Manan Kothari's DM: D06E4QMHCNN
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
            'text': '\U0001f4cb Wednesday Wrap-Up  |  Oct 21, 2026  |  Grade: A-',
            'emoji': True,
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3af DAY THEME: HIRING INTENT CAPTURE LOCKED \xb7 SPEC SWARM RISK CALL TO MAKE*\n'
                'Focused, productive day, Manan. Two back-to-back sessions on the same feature = rare, '
                'and you made the most of it. Design is locked, DS/platform is unblocked, and the logic '
                'flow is solid. One real decision still pending (Spec Swarm N+1?), and a few overdue '
                'items are getting loud. Let\'s make sure tomorrow counts.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4c5 MEETINGS TODAY (2)*'
        }
    },
    {
        'type': 'section',
        'fields': [
            {
                'type': 'mrkdwn',
                'text': '*8:15 AM PDT*\n<https://notes.granola.ai/d/a51b0681-2ceb-475d-b6e1-ad7740304401|Hiring Count + Frequency>\nManan, Divij, Sina, Fadi'
            },
            {
                'type': 'mrkdwn',
                'text': '*10:30 AM PDT*\n<https://notes.granola.ai/d/88ff59bc-a969-490e-8c8b-5ae6de258de6|Discovery \u2014 Hiring Leads>\nManan, Fadi, Bob, Jatin, Skye, IBK, Malcolm'
            }
        ]
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2696\ufe0f KEY DECISIONS MADE TODAY*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*1. JD rules for count + urgency \u2014 DECIDED* \u2705\n'
                '\u2022 Vanilla case (1 hire, \u223c30 days) \u2192 no change to job description\n'
                '\u2022 Multiple hires \u2192 "multiple [role] positions available"\n'
                '\u2022 Urgency \u22642 weeks (ASAP/1wk/2wk) \u2192 "urgently hiring"\n'
                '_Rationale: avoids overloading the JD while giving job seekers actionable signals. '
                'Correlates to Indeed\'s own "urgently hiring" tag. For job boards that won\'t expose '
                'it as a metadata field, embedding it in the text is the pragmatic path._\n'
                '\u26a0\ufe0f *Still open:* posted date vs. activated date as urgency reference; '
                'definition of "ASAP". Divij needs this nailed down to proceed \u2014 Manan owns.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*2. UI direction locked: chips, not dropdowns* \u2705\n'
                '\u2022 Drop the "what to include" checklist (polarizing, easy to misread as required)\n'
                '\u2022 Update prompt chips to append count + speed inline\n'
                '\u2022 Fallback: job details page collects what OEM skips in the chip\n'
                '\u2022 Hire count indicator ("1 of 2") added to job card (dashboard + job tab only; '
                'job details page excluded \u2014 too busy)\n'
                '_Rationale: ~73% of chip users who edit the chip convert. Chips give momentum without '
                'adding UI complexity. Dropdown version technically cleaner but design too heavy; '
                'Fadi owned the call. IBK preferred deterministic dropdowns \u2014 good debate, '
                'pragmatism won._'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*3. Speed data: collect now, use later* \u2705\n'
                '\u2022 Speed options locked: ASAP / within 1 week / within 2 weeks / within a month / specific date\n'
                '\u2022 "No rush" removed (if no rush \u2192 pick a date)\n'
                '\u2022 Not wired into product logic today\n'
                '_Rationale: low-lift to collect upfront, high value later. Indeed "urgently hiring" tag '
                'is an immediate win. Future use: ASAP hires \u2192 recommend boosting; non-urgent \u2192 '
                'recommend social sharing. Fadi\'s framing: "one extra line in the prompt, why not?"_'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*4. Close flow edge case \u2014 bug identified + fix spec\'d* \u26a0\ufe0f\n'
                'Gap found: if OEM hits "keep open" after filling all their intended roles, '
                'and the job then hits the 27-day mark, the expiry check diamond never fires '
                'again \u2014 so they never get a nudge to close.\n'
                '_Fix: add a branch off the "close" path that loops back into the 27-day expiry check. '
                'Fadi owns the design update._'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*5. Spec Swarm N+1 \u2014 judgment call pending* \u23f3\n'
                'You floated bringing hiring count+speed into *next Tuesday\'s Spec Swarm* if '
                'designs are ready. Jatin\'s guidance: it\'s your and Fadi\'s call, but know the '
                'risk \u2014 no verdict spike done \u2192 carryover risk if scope is underestimated.\n'
                '_This is the one decision still open from today. You and Fadi need to decide '
                'before Tuesday. If you bring it in, own the risk. If you wait, it goes to '
                'Lookahead N+2 the week after._'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*6. Matan (GTM) process integration \u2014 agreed* \u2705\n'
                '\u2022 Matan brings GTM work into Lookahead N+1 as a one-off next Tuesday\n'
                '\u2022 Normal N+2 cadence from then on\n'
                '\u2022 You + Skye to pre-align with Matan *before* Spec Swarm/Lookahead N+2\n'
                '_Rationale: Matan has been working in a silo on GTM comms; this brings him into '
                'the sprint cadence so product-sales alignment happens before work is committed, '
                'not after._'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*7. Discovery meetings off auto-record* \u2705\n'
                'Jatin is removing discovery from the EPDD pipeline. Only Look Ahead + Swarm '
                'will be auto-recorded. Your explicit preference: keep discovery informal so '
                'you can speak freely; share Granola notes if anything needs broader visibility.\n'
                '_Also locked: job request state model needs a partial-fill redesign '
                '(Malcolm: engineering heads-down, no product input needed yet). '
                'Domain events work makes the product more predictable and easier to debug._'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u26a1 YOUR ACTION ITEMS \u2014 Manan only*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f525 DO TONIGHT (or first thing tomorrow \u2014 blocking others):*\n'
                '\u2022 *Write JD inclusion rules for count + urgency* \u2192 send to Divij. '
                'He can\'t finalize the prompt logic without this. '
                '(Define: when to say "multiple positions"; when to say "urgently hiring"; '
                'reference date; ASAP definition)\n'
                '\u2022 *Decide with Fadi: Spec Swarm N+1 (Tuesday) or wait for N+2?* '
                'No verdict spike = real carryover risk. Make this call proactively; '
                'don\'t let Tuesday sneak up.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4c6 TOMORROW (Thurs Oct 22):*\n'
                '\u2022 *Align with Matan + Skye* on what he brings into Lookahead N+1 '
                '(pre-Spec Swarm. You committed to this in today\'s meeting.)\n'
                '\u2022 *Share prototype link* in #project-hiring-intent-capture '
                '(Sina requested it; Fadi + Sina already added)\n'
                '\u2022 *Match explanation pre-work:* audit raw match data, identify gaps. '
                'Workshop is *Friday Oct 23* \u2014 that\'s tomorrow. This cannot wait.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f6a8 CRITICAL OVERDUE (these are getting loud):*\n'
                '\u2022 *2029 Vision one-pager \u2014 BOARD MEETING OPENED OCT 15.* '
                'Fadi submitted his + design deck. You have NOT submitted yours. '
                'This is on John directly. Block 90 min, do it now.\n'
                '\u2022 *Town Hall Q&A questions \u2014 TOMORROW Oct 22.* '
                'Overdue since Monday Oct 19. Submit before end of day.\n'
                '\u2022 *Facebook API \u2014 ALL CALLS FAILING. Day 28.* '
                'No update since Oct 9. Ping Bob + IBK today.\n'
                '\u2022 *Nihilus subscription \u2014 Nov 3 deadline = 12 days.* '
                'Izzy to scope build cost. Decision needed before renewal. Get a status today.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4e1 WATCH LIST \u2014 What\'s Hot Right Now*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\U0001f7e2 *Indeed:* RECOVERED \u2014 Day 60. Back to pre-outage volume. '
                'Arch review still a formal gate before close flow ships.\n'
                '\U0001f7e1 *Match Explanation Workshop:* *TOMORROW Friday Oct 23.* '
                'Pre-work: audit raw match data. Fadi running the FigJam session.\n'
                '\U0001f7e1 *Welcome Tech Pilot:* Amir to send one-pager + deck. '
                'You + Skye to shortlist 2-3 pilot employers.\n'
                '\U0001f7e1 *HBA Janneke KT:* Still URGENT \u2014 days left before leave. '
                'Check in with Daniel Chao.\n'
                '\U0001f534 *Carlo KT:* Paternity leave through mid-Feb, not confirmed. '
                'Do async Slack/doc KT NOW.\n'
                '\U0001f534 *Jatin:* Out Thu-Fri this week (Austin bachelor party). '
                'Engineering questions wait until Monday.\n'
                '\U0001f534 *Matan dynamics:* Talk to Skye (research opacity, email rewrites '
                'without product input). Don\'t let this slip with the sprint crunch coming.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3af TOMORROW\'S PRIORITY ORDER*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '1. *JD rules doc \u2192 Divij* (if not done tonight)\n'
                '2. *Decide Spec Swarm N+1 with Fadi* \u2014 text him tonight if you can\n'
                '3. *Matan + Skye alignment call* (pre-Lookahead)\n'
                '4. *Match explanation pre-work* (Friday workshop is do-or-die)\n'
                '5. *Town Hall Q&A questions* \u2014 just submit them\n'
                '6. *2029 one-pager* \u2014 block 90 min, this is the real one'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4ca DAY GRADE: A-*\n'
                'You ran a tight, focused ship today, Manan. Two sessions, same feature, '
                'full alignment across product + design + DS + engineering + GTM. '
                'Design direction locked, logic flow solid, team unblocked. '
                'The A- comes from the growing pile of overdue items (one-pager, Facebook API, '
                'Nihilus) that didn\'t move today. You\'re shipping great work \u2014 '
                'just don\'t let the administrative debt compound. Tomorrow\'s a big one: '
                'match workshop + town hall + Spec Swarm decision. '
                'You\'ve got this. \U0001f4aa'
            )
        }
    },
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': '_Chief of Staff Digest \u2014 Oct 21, 2026 \u2014 auto-generated from Granola notes_'
            }
        ]
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'unfurl_links': False,
    'unfurl_media': False,
}


def preview():
    sys.stdout.buffer.write(
        json.dumps(payload, indent=2, ensure_ascii=False).encode('utf-8', errors='replace')
    )
    sys.stdout.buffer.write(b'\n')


token = (
    os.environ.get('SLACK_TOKEN')
    or os.environ.get('SLACK_BOT_TOKEN')
    or os.environ.get('SLACK_API_TOKEN')
)

if not token:
    print('No Slack token found — PREVIEW MODE:')
    preview()
    sys.exit(0)

req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json; charset=utf-8',
    },
    method='POST',
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('Message sent! ts=' + str(result.get('ts')))
    else:
        print('Slack API error: ' + str(result.get('error')))
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print('Request error: ' + str(e))
    preview()
    sys.exit(1)
