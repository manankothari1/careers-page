#!/usr/bin/env python3
"""Weekend digest for Manan — Sat Oct 24 PDT (triggered midnight UTC Oct 25)."""

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
            'text': '\U0001f4cb Saturday Debrief — Week of Oct 19-24, 2026',
            'emoji': True
        }
    },
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': '*Chief of Staff \xb7 Sat Oct 24 \xb7 Paris, France \xb7 No meetings today (weekend \U0001f3d6\ufe0f)*'
            }
        ]
    },
    {'type': 'divider'},

    # Mood + grade
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f31f Week Grade: A \u2014 You shipped the hardest call of Q4.*\n\n'
                'Manan, this was a genuinely excellent week. You made a bold architectural decision on magic link, mitigated a live production bug, '
                'unlocked a full ML pipeline for hiring intent capture, and kept every long-running workstream moving. '
                'You\'re in Paris, it\'s Saturday, and you still have two things that cannot wait. Let\'s make the most of it.'
            )
        }
    },
    {'type': 'divider'},

    # Big decisions of the week
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3af BIG DECISIONS THIS WEEK*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*1. \U0001f517 Magic Link replaces OTP entirely (Oct 23)*\n'
                '\u2022 *Decision:* Full replacement for all OEMs \u2014 not a fallback, a complete swap. Removes Stitch SDK. Targets 100% send success vs 64% today.\n'
                '\u2022 *Why:* No reliable pre-send OTP failure detection; fallback approach keeps Datadog amber permanently. Magic link is cleaner.\n'
                '\u2022 *Key design call:* User must click Verify button (not auto-verify) \u2014 email scanners consume one-time tokens automatically.\n'
                '\u2022 *Architecture:* Poll every few seconds when tab is active; refetch on focus-regain; device-agnostic success screen.\n'
                '\u2022 *Rollout:* New experiment key, same 90/10 split, staged. Est. ~1 week dev-done (IBK).\n'
                '\u2022 *Open items:* Link expiry time, email monitoring, active-tab JS detection \u2014 IBK confirms. Manan: tag Fatty for Verify CTA designs.\n'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*2. \U0001f41b Indeed Company Field Bug \u2014 Mitigated (Oct 22)*\n'
                '\u2022 *Decision:* Temporarily pause company field; remove net new jobs identifier; leave existing jobs as-is (no repost cascade).\n'
                '\u2022 *Why:* Multiple businesses sharing same name caused routing/dedup conflict. Bob\'s PR merged mid-call. Pausing is safest while long-term fix is scoped.\n'
                '\u2022 *Still outstanding:* Draft + send Indeed support reply. Bob is updating Michael. This is on you, Manan \u2014 it\'s been 2 days.\n'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*3. \U0001f9e0 Hiring Intent Capture \u2014 Architecture Locked (Oct 21)*\n'
                '\u2022 *Decision:* ML pipeline design approved. Divij/Sina/Fadi aligned on approach.\n'
                '\u2022 *Why blocked:* Entire pipeline blocked on JD rules product verdict from Manan. Due this weekend.\n'
                '\u2022 *JD rules you need to write:* (1) 1 hire ~30d \u2192 vanilla JD; (2) 2+ hires \u2192 \'multiple [role] positions available\'; (3) urgency \u22642wk \u2192 \'urgently hiring\'; (4) vanilla (1 hire >2wk) \u2192 no change. TBDs: posted vs activated date; ASAP definition.\n'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*4. \U0001f4ac Applicant Email \u2014 \'Your Profile\' Link Permanently Removed (Oct 22)*\n'
                '\u2022 *Decision:* Candidate profile V1 is sunset. Remove the link from applicant email permanently.\n'
                '\u2022 *Why:* Profile V1 not coming back. Short-term: plain text \'You applied to [role] on [date]\'.\n'
                '\u2022 *Owner:* Iszael taking over from Aaron.\n'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*5. \U0001f4e6 Jobcase Integration \u2014 Officially Parked (Oct 22)*\n'
                '\u2022 *Decision:* No reply from Jamie/Jane 3+ weeks. Formally close out.\n'
                '\u2022 *Owner:* Iszael to close the loop.\n'
            )
        }
    },
    {'type': 'divider'},

    # Weekend action items
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f525 THIS WEEKEND \u2014 2 Things That Cannot Wait*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                ':rotating_light: *1. Write JD Rules for Divij \u2014 DUE TODAY* (he is blocked, sprint is blocked)\n'
                'Takes 30 minutes. Here\'s the frame you already agreed on:\n'
                '\u2022 1 hire, ~30 days \u2192 vanilla (no change)\n'
                '\u2022 2+ hires, same role \u2192 \'multiple [role] positions available\'\n'
                '\u2022 Urgency \u22642 weeks (ASAP/1wk/2wk) \u2192 \'urgently hiring\'\n'
                '\u2022 Vanilla (1 hire >2wk) \u2192 no change\n'
                'Remaining TBDs: posted vs activated date; ASAP definition. Decide and write. Ping Divij when done.\n\n'
                ':rotating_light: *2. Write 2029 Vision One-Pager \u2014 CRITICAL OVERDUE* (board meeting was Oct 15)\n'
                'Fadi submitted his. You have not. Block 90 minutes today or tomorrow. This one has your name on it.'
            )
        }
    },
    {'type': 'divider'},

    # Monday battle plan
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u26a1\ufe0f MONDAY BATTLE PLAN (Oct 26)*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                ':one: *Ping Jatin (back from Austin)* \u2014 Indeed XML feed make-private + Soheil on standup invite\n'
                ':two: *Tag Fatty* \u2014 Verify CTA designs for magic link success screen\n'
                ':three: *Draft + send Indeed reply* \u2014 company field bug. Matan + Bob have context. 5-minute email.\n'
                ':four: *Facebook API escalation* \u2014 Day 31. All calls failing. Bob + IBK. Escalate now.\n'
                ':five: *Spec Swarm N+1 decision with Fadi* \u2014 BEFORE Tuesday GTM. Bring hiring count+speed into next Swarm or wait N+2?\n'
                ':six: *Pre-align with Matan + Skye* \u2014 before Tuesday Oct 27 GTM Lookahead meeting\n'
                ':seven: *Matt McAllister intro* \u2014 New CMO, Week 2. From Yelp. Block 30 mins. This is relationship capital you want.\n'
                ':eight: *Confirm entitlements rollout* \u2014 Adam Hewitt: 1% Monday, 5% Wednesday. Stays on track?\n'
                ':nine: *Carlo KT* \u2014 Not confirmed. Knowledge risk. Paternity through mid-Feb. Don\'t let this drift another week.\n'
                ':keycap_ten: *Matan dynamics* \u2014 Talk to Skye. Research opacity + email rewrites without product input. Address it now while patterns are fresh.'
            )
        }
    },
    {'type': 'divider'},

    # Watch list
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f6a8 WATCH LIST \u2014 Items That Will Bite You If Ignored*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                ':red_circle: *Nihilus Subscription \u2014 Deadline NOV 3 (9 days).* Izzy to scope build cost. Leaning: stay Q4, remove Q1. Decision needed before renewal.\n'
                ':red_circle: *Facebook API \u2014 ALL CALLS FAILING. Day 31.* Bob + IBK. Zero traction since Oct 9. Escalate Monday.\n'
                ':red_circle: *Indeed XML Feed \u2014 MAKE PRIVATE.* Jatin back Monday. Follow up immediately. Medium-term: JobSync API.\n'
                ':orange_circle: *Match Explanation Workshop \u2014 Outputs need capturing.* Happened Friday evening. IBK attended. What were the outputs?\n'
                ':orange_circle: *COMMS ASSISTANT production decision \u2014 OVERDUE.* Malcolm leaves Halloween. Decide before he\u2019s gone.\n'
                ':orange_circle: *DEPARTURES SIGNAL DOCS \u2014 30+ days overdue.* \u2192 Zane, Sean, Jon W, Bobby. This is institutional memory at risk.\n'
                ':yellow_circle: *Welcome Tech Pilot* \u2014 Amir sent one-pager + deck. Manan + Skye: shortlist pilot employers.\n'
                ':yellow_circle: *Orca Comms Quality QA* \u2014 Matan built skill. Needs manual QA with IBK.\n'
                ':yellow_circle: *46 Old Experiments* \u2014 Jatin surfaced. Manan + Fadi quick review needed.\n'
                ':yellow_circle: *Gift cards owed:* Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50). Do this Monday.\n'
                ':yellow_circle: *Emails unsent:* John Waldman (EarnBetter NDA), Marina/Mundo Academy (27+ days). These people are waiting.\n'
            )
        }
    },
    {'type': 'divider'},

    # Closing note
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f1eb\U0001f1f7 Enjoy Paris, Manan.*\n\n'
                'You\u2019ve got until Friday Oct 30 before you head back. You made some great calls this week \u2014 '
                'the magic link decision alone is going to meaningfully improve OEM signup quality and remove a painful SDK dependency. '
                'The team is aligned, the roadmap is holding, and Monday is going to be a good day.\n\n'
                '_Two things before you close this message: JD rules for Divij, and the 2029 one-pager. Those are your weekend deliverables. Everything else can wait until Monday._\n\n'
                '\u2014 Your Chief of Staff \U0001f4bc'
            )
        }
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'text': 'Saturday Debrief \u2014 Week of Oct 19-24, 2026 | Grade: A | 5 big decisions, 2 weekend deliverables, full Monday battle plan inside.'
}

def preview():
    sys.stdout.buffer.write(b'\n=== SLACK PREVIEW (no token) ===\n')
    sys.stdout.buffer.write(('ALT TEXT: ' + payload['text'] + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(b'\nBLOCKS:\n')
    for b in blocks:
        if b.get('type') == 'section' and 'text' in b:
            txt = b['text'].get('text', '')
            sys.stdout.buffer.write(txt.encode('utf-8', errors='replace'))
            sys.stdout.buffer.write(b'\n---\n')
        elif b.get('type') == 'header':
            txt = b['text'].get('text', '')
            sys.stdout.buffer.write(('HEADER: ' + txt).encode('utf-8', errors='replace'))
            sys.stdout.buffer.write(b'\n---\n')
    sys.stdout.buffer.write(b'=== END PREVIEW ===\n')

token = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN') or
    ''
).strip()

if not token:
    preview()
    print('\nNOTE: No Slack token found. Add SLACK_TOKEN or SLACK_BOT_TOKEN in Cursor Dashboard > Cloud Agents > Secrets.')
    sys.exit(0)

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=data,
    headers={
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json; charset=utf-8'
    },
    method='POST'
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('SUCCESS: Message sent to', CHANNEL)
    else:
        print('ERROR from Slack API:', result.get('error'), result)
        sys.exit(1)
except urllib.error.URLError as e:
    print('NETWORK ERROR:', e)
    sys.exit(1)
