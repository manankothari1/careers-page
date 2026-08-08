#!/usr/bin/env python3
"""
Friday Aug 7, 2026 EOW Digest
Cron: midnight UTC Aug 8 = 5pm PDT Aug 7 (Friday)
0 meetings on Friday; sending week-in-review + Monday battle plan.
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
            'text': '\U0001f4cb Friday EOW Wrap-Up | Aug 3\u20137, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Happy Friday, Manan! \U0001f44f No meetings today, which means you actually had a '
                'focused heads-down day \u2014 good for you. Here\'s your full week-in-review '
                'with every decision, action item, and what Monday looks like. '
                '*Spoiler: it\'s a big one.*'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f6a8 URGENT \u2014 DO THIS WEEKEND*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*1. Indeed Watch List Follow-Up* \u2014 Homebase got flagged (again) for '
                'fraudulent jobs sent to Indeed. You got an email Aug 5 with zero specifics. '
                '*~60% of your applicant volume flows through Indeed.* If you\'re in strict '
                'review mode, new clients\' jobs won\'t appear in search at all. '
                'Action: Email your Indeed contact this weekend \u2014 which jobs are flagged? '
                'Why? Is strict review already active? This can\'t wait until Monday.\n\n'
                '*2. Dana Succession \u2014 5 Days Left (CONFIDENTIAL)* \u2014 Dana\'s last day '
                'is Friday Aug 12. She returns Monday Aug 10, giving you exactly *2 working days* '
                'to sort handoffs. Page Templates ownership is still unclear \u2014 Fadi is getting '
                'conflicting info from two different people. You need to resolve this Monday '
                'morning the moment Dana is back. Succession plan = NOW, not Monday afternoon.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f91d BIG NEWS: Sky is Your New Head of Product*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Introduced informally in the Aug 5 standup. Sky has 15-20 years of product '
                'experience with a *B2B marketplace background* \u2014 sold a real estate '
                'marketplace to Compass. Already built a *voice agent prototype for job posting '
                'setup* and shared a working doc. This person hit the ground running before '
                'day one. Make sure you\'re aligned with Sky early next week on your Q3 roadmap '
                'and the strategy deck you\'re presenting Monday.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4ca Key Decisions Made This Week*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*MBR \u2014 Mon Aug 3*\n'
                '\u2022 Structure LOCKED: Combined health slide \u2192 Matan ICP \u2192 Manan '
                'learnings. Trigger-based comms = the MBR thesis frame. '
                '"Message at the right time" anchor.\n'
                '\u2022 July trial results: *178 June \u2192 199 July (+11.8% MoM)*. V1-to-V2 '
                'migrations drove conversions but no confirmed ICP breakthrough yet.\n'
                '\u2022 Applicant quality *softened*: jobs with 20+ apps but <5 top matches rose '
                'from 19% \u2192 *26.5%*. This is a signal to track.\n'
                '\u2022 MBR framing: "continuous learning motion" \u2014 small samples require '
                'validation before acting on signals.\n\n'
                '*Sprint Planning \u2014 Mon/Tue Aug 3-4*\n'
                '\u2022 Renew Jobs (Tanner) + Tap the Talent Pool (Carlo, started Aug 5) = '
                'sprint priorities LOCKED.\n'
                '\u2022 Matching philosophy LOCKED: absolute population-level scoring; '
                'top 20% per competency = threshold; present as % not binary.\n'
                '\u2022 PJ\'s Coffee (Yvonne) Indeed escalation: wait for admin repost path; '
                'Christofer owns fallback.\n'
                '\u2022 Soheil\'s dynamic pass threshold: making match thresholds *configurable '
                'for experimentation* (not hardcoded constants). Smart move \u2014 you caught '
                'this and pushed for it.\n'
                '\u2022 Domain events *nearly done*: Malcolm completing final PR, Kafka topics '
                'created, job lifecycle events emitting. This unlocks HBA Assistant.\n\n'
                '*Applicant-Side Priority Stack \u2014 Tue Aug 4 (w/ Matan)*\n'
                '\u2022 LOCKED: (1) trigger-based drip, (2) matching improvements, '
                '(3) comms experiments, (4) talent pool outreach, (5) SEO/domain authority.\n\n'
                '*Engineer Ownership POC \u2014 Wed Aug 5 (w/ Fadi + Jatin)*\n'
                '\u2022 Proposal: assign engineers a problem end-to-end (scrappy startup model). '
                'Start with Izzy \u2014 e.g., own the Indeed watch list issue.\n'
                '\u2022 Jatin\'s concern: Martin may push back; Martin was out this week.\n'
                '\u2022 Decision: frame as "flirting with the idea" in Monday\'s strategy deck; '
                'invite Martin\'s input rather than presenting as decided. Fadi to loop Martin '
                'before the deck goes out.\n\n'
                '*Strategy Deck for John + Ray \u2014 Wed Aug 5*\n'
                '\u2022 DECIDED: Manan to build a presentation for Monday covering goals, '
                'how we plan to hit them, priorities, and engineer ownership POC concept.\n'
                '\u2022 Fadi + Jatin to review before it goes to John and Ray.\n'
                '\u2022 Use a deck, not just a spreadsheet \u2014 it needs to explain the "why."\n\n'
                '*JD Page Experiment + Roadmap \u2014 Thu Aug 6*\n'
                '\u2022 JD A/B experiment GREENLIT: 50/50, skip prompt box page, IBK runs '
                'it week of Aug 10. 60% of users drop off on JD page; skipping to details '
                'page should reduce friction.\n'
                '\u2022 Abandonment survey LIVE (or launching): Matan built via Guides, '
                'pending LCM approval. Triggers on JD page exit.\n'
                '\u2022 Four focus areas LOCKED: (1) trial starts, (2) unblocking applicant '
                'flow, (3) core light touches, (4) retention at 85-90% = minimal investment.\n'
                '\u2022 Consolidated roadmap: one Google Sheet across product + PMM + sales; '
                'Linear project links to follow. Deck showing all workstreams vs. two core '
                'FFH metrics due *Monday Aug 10.*\n'
                '\u2022 New MBR format: goals-first, not output-heavy. Hiring team not flagged '
                '\u2014 already in many meetings with leadership.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2705 Your Open Action Items (Ownership = You)*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\u2022 \U0001f6a8 *Email Indeed contact* re: fraudulent jobs flag \u2014 '
                'which jobs? why? is strict review active? (Flagged Aug 5, still open)\n'
                '\u2022 \U0001f6a8 *Dana succession plan* \u2014 resolve Page Templates '
                'ownership Monday AM; she\'s back Aug 10, gone Aug 12\n'
                '\u2022 \U0001f534 *Strategy deck for John + Ray* \u2014 DUE MONDAY. Share '
                'with Fadi + Jatin first for review\n'
                '\u2022 \U0001f534 *Roadmap-to-goals deck* \u2014 DUE MONDAY. Map all '
                'workstreams to 500 FFH customers + 70% healthy jobs\n'
                '\u2022 \U0001f534 *Share Amplitude dashboard with Matan* \u2014 was supposed '
                'to happen Aug 6; Matan needs it to extract CSV of users who started but '
                'never posted a job\n'
                '\u2022 \U0001f7e1 *Send applicant-count survey (Great Question)* to team '
                'for review \u2014 how many apps do OMs need before deciding?\n'
                '\u2022 \U0001f7e1 *Loop Martin on engineer ownership POC* (via Fadi) '
                '\u2014 Martin was out this week; get his read before presenting it\n'
                '\u2022 \U0001f7e1 *Make business case for Rami to Ted directly* \u2014 '
                'Ted pulling DS back from hiring; Manan must own this conversation\n'
                '\u2022 \U0001f7e1 *Scope SEO content strategy with Tatiana* \u2014 still open\n'
                '\u2022 \U0001f7e1 *Validate Meta ads timing-targeting with Jenna* '
                '\u2014 still open\n'
                '\u2022 \U0001f7e1 *Scooters follow-up email* (Olivia/Maria/Lacey) '
                '\u2014 still open\n'
                '\u2022 \U0001f7e1 *Align on franchise work with Rushi* \u2014 still open\n'
                '\u2022 \U0001f7e1 *422 Job Publishing Errors* \u2014 Day 28 as of today; '
                'Jatin on RCA; Ray out so you\'re the decision-maker'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4c5 Monday Aug 10 \u2014 Battle Plan*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\U0001f534 *8:45am* \u2014 Hiring Leads Standup (review MBR feedback, '
                'JD A/B kick-off, confirm Izzy reactivation on staging)\n'
                '\U0001f534 *Morning* \u2014 Dana returns; get her in a room and finalize '
                'Page Templates handoff + succession before she\'s mentally checked out\n'
                '\U0001f534 *Morning* \u2014 Sprint retro (Jatin setting up)\n'
                '\U0001f534 *Present* strategy deck + roadmap-to-goals deck to John + Ray\n'
                '\U0001f534 *Confirm* IBK has JD A/B experiment set up for the week\n'
                '\U0001f534 *Send* Amplitude dashboard link to Matan (overdue)\n'
                '\U0001f534 *Meet* with Sky \u2014 get aligned early; don\'t let the first '
                'real conversation be in a big meeting\n\n'
                '_Week of Aug 10 also: 422 error RCA needs closure (Day 29+). '
                'Comms agent spike (Malcolm). Soheil on dynamic thresholds. '
                'Carlo in sprint on Talent Pool. Tanner on Renew Jobs._'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4ca Q3 Scorecard Check-In*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\u2022 FFH D5 zero-applicant rate: *41%* (target: <10%) \u2014 reactivation '
                'is THE unlock; Izzy\'s work next sprint\n'
                '\u2022 Line cook jobs healthy by D30: *~7%* (target: 50%) \u2014 biggest gap\n'
                '\u2022 Screener completions: land 80% / start 56% / complete 80% '
                '\u2014 root cause = jobs not reaching Indeed\n'
                '\u2022 FFH paying customers: *~800K accounts* total; 500 FFH + 70% healthy = '
                'the two north star metrics for the deck Monday\n'
                '\u2022 ARR: $650K+ (from $450K Jan 2026) \u2014 real momentum'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*This was a big week, Manan.* You shipped a sprint, presented an MBR, '
                'aligned on the full applicant-side priority stack with Matan, greenlit the '
                'JD experiment, got Sky introduced to the team, and are walking into Monday '
                'with a clear four-focus-area strategy. \U0001f4aa\n\n'
                'The weekend has one job: finish that strategy deck and follow up on Indeed. '
                'Everything else can wait until Monday. Enjoy some downtime \u2014 you earned it. '
                '\U0001f37b'
            )
        }
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'Friday EOW Wrap-Up | Aug 3-7, 2026 - Chief of Staff Digest',
    'blocks': blocks
}

def preview():
    sys.stdout.buffer.write(('\n=== PREVIEW (no Slack token) ===\n').encode('utf-8', errors='replace'))
    for block in blocks:
        if block.get('type') == 'section':
            txt = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((txt + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'header':
            txt = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write(('## ' + txt + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(('---\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(('\n=== END PREVIEW ===\n').encode('utf-8', errors='replace'))

token = (
    os.environ.get('SLACK_TOKEN', '').strip()
    or os.environ.get('SLACK_BOT_TOKEN', '').strip()
    or os.environ.get('SLACK_API_TOKEN', '').strip()
)

if not token:
    print('No Slack token found. Printing preview instead.')
    preview()
    sys.exit(0)

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=data,
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode('utf-8'))
        if result.get('ok'):
            print('SUCCESS: Message sent to Slack.')
        else:
            print(f'Slack API error: {result.get("error")}')
            preview()
            sys.exit(1)
except urllib.error.URLError as e:
    print(f'Network error: {e}')
    preview()
    sys.exit(1)
