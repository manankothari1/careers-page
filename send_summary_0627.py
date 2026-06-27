#!/usr/bin/env python3
"""
Weekly decision digest for Manan Kothari - Week of Jun 23-27, 2026
Sends to Slack DM channel D06E4QMHCNN
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'

# Build the Block Kit payload
blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': 'Your Week in Review: Jun 23-26, 2026'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Happy Saturday, Manan! What a week. 9 meetings, a new partnership, a team re-org on analytics, a new hire incoming, and some real clarity on Q3. Here\'s everything you decided, why it matters, and what needs to happen next. You\'re in a strong spot heading into next week. Let\'s ride.'
        }
    },
    {'type': 'divider'},

    # ─── BIG DECISIONS ───────────────────────────────────────────────────────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:dart: KEY DECISIONS THIS WEEK*'
        }
    },

    # Decision 1
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*1. Rewrote the Indeed success metric* — Ray/Manan (Jun 25)\n*Decision:* Replaced the vague "increase indeed-sourced applicants by 25" with a measurable, action-oriented goal: *FFH jobs with zero Indeed applicants on D5 < 10%* (currently sitting at 41%).\n*Why it matters:* This single metric creates a forcing function for source claiming, copy-a-job, reactivation, and sponsored posts — all the adjacent work you\'ve been debating how to prioritize. It\'s also testable and reportable to execs.\n:arrow_right: *Action (Manan):* Draft v3 of the Q3 goals doc in the three-bucket structure and share with Ray before it goes to John.'
        }
    },
    {'type': 'divider'},

    # Decision 2
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*2. Kicked off Culinary Agents partnership* — Culinary Agents & Homebase (Jun 24)\n*Decision:* Moving forward on integration. 2.7M hospitality workers, bulk PPP pricing (~$69/post at 500-tier), existing XML/API feed already compatible. Ray sending job feed to Alice to start ~2-week implementation.\n*Why it matters:* This is a new applicant source that\'s highly targeted for your exact ICP (FFH), plugs directly into your ATS pipeline, and could move the needle on "healthy job" rates without touching your Indeed strategy.\n:arrow_right: *Action (Manan):* Get a dedicated follow-on call with Alice on Indeed-boosting mechanics via Culinary Agents — she confirmed it\'s live and working well.\n:arrow_right: *Action (Ray):* Send job feed to Alice. Schedule ATS + AI screener demo for their team.'
        }
    },
    {'type': 'divider'},

    # Decision 3
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*3. Greenlighted talent pool email blast for line cooks* — Rami/Manan Launch (Jun 25)\n*Decision:* 86 line cook jobs, no pre-filtering by health status (let AI run first), 25-mile radius, 2,000-user cap per job ranked by recency. Target: 5,000-10,000 emails total. UTM tracking: `utm_campaign=generic` vs. `utm_campaign=recruiter`.\n*Why it matters:* This is the first real experiment on the talent pool pillar. You\'ll get data on whether personal recruiter framing outperforms generic outreach — which directly validates or kills the broader positioning hypothesis.\n:arrow_right: *Action (Rami):* CSV was due EOD Friday — confirm it arrived and the blast is queued for this weekend/Monday morning.\n:arrow_right: *Action (Manan):* Ping Ted about ML/data platform support (Shamir or Dvich).'
        }
    },
    {'type': 'divider'},

    # Decision 4
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*4. Set Abby\'s onboarding roadmap* — Manan/Cindy (Jun 25)\n*Decision:* Abby starts July 7. First sprint priorities in order: (1) Indeed source claiming, (2) Automatic go-live (fraud check pre-verification), (3) Job seeker manual intake. Hold her out of the leads standup initially; Manan serves as her interface for team context.\n*Why it matters:* Getting Abby productive fast is critical — she has an engineering background and can ship code, so the ramp should be quick. Starting her on source claiming is perfect since it\'s high priority and well-scoped.\n:arrow_right: *Action (Manan):* Send Cindy the line cook D5/D30 healthy rate analysis + any relevant applicant flow links for the onboarding doc.'
        }
    },
    {'type': 'divider'},

    # Decision 5
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*5. Chose intercept modal (not inline) for job title + salary warnings* — Cindy/Manan (Jun 25)\n*Decision:* Surface role title and salary optimization recommendations via an intercept modal when users click "Next" after job details — not inline live edits. Warning framing is *critical* (bad titles get flagged by Indeed and cost applicants), salary framing is a strong nudge. Rollout FFH-only first.\n*Why it matters:* Batching all recommendations into one review step with "Apply for me" CTA is cleaner UX and reduces decision fatigue. The conversion risk from adding a step is real, so treating as an experiment is the right call.\n:arrow_right: *Action (Cindy):* Design options for both patterns due Monday midday. Needs to be ready for Wednesday look-ahead.\n:arrow_right: *Action (Manan):* Send design options to Fadi for polish after Cindy delivers.'
        }
    },
    {'type': 'divider'},

    # Decision 6
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*6. Reframed outbound calling goal: test excitement, not bookings* — Hiring Leads Standup + Dana 1:1 (Jun 23/26)\n*Decision:* Usman was selling "free recruiter" instead of testing the personal recruiter value prop. Shift: goal is to validate whether the positioning resonates (people excited on calls), not to maximize intake conversions. Dana revised script, Usman role-playing. Target: 30-50 connections/week.\n*Why it matters:* Zero calls booked since the reframe — which is fine. The experiment wasn\'t measuring the right thing before. Now it is.\n:arrow_right: *Action (Manan):* Listen to Usman\'s call recordings this week. Are people excited? That\'s the signal you\'re looking for.\n:arrow_right: *Action (Dana):* Daily test performance report hitting Manan\'s inbox — share Usman\'s talk track doc too.'
        }
    },
    {'type': 'divider'},

    # Decision 7
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*7. Job description generator as the fix for Indeed duplicate flagging* — Dana 1:1 (Jun 26)\n*Decision:* Root cause of flagged/reposted jobs on Indeed = duplicate detection policy. Proposed fix: use the job description generator to create a sufficiently differentiated description on repost, avoiding the flag.\n*Open question:* What % difference does Indeed actually require? They won\'t say — idea floated to probe with a test company.\n*Why it matters:* One customer already complained directly to you about wasted time. This is a credibility issue. The fix is elegant because it uses tooling you\'re already building.\n:arrow_right: *Action (Manan):* Before committing to ship the source claiming in-product banner (Ray + Matan want it soon), define the full experience — especially trial user handling and how it interacts with the existing trial banner. Don\'t let them rush this one.'
        }
    },
    {'type': 'divider'},

    # Decision 8 - org news
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*8. :warning: Dana is leaving end of September* — Dana 1:1 (Jun 26)\n*Decision noted:* Dana disclosed she\'s leaving at end of September and has already spoken to Ray.\n*Why it matters:* Dana is a key partner on outbound calling, source claiming, and the personal recruiter experiment. You have ~3 months of runway with her. Make sure her knowledge is transferred and that Abby or someone else is ramped on these surfaces before she\'s out.\n:arrow_right: *Action (Manan):* No immediate action required, but start thinking about knowledge transfer plan for Dana\'s surfaces before end of Q3.'
        }
    },
    {'type': 'divider'},

    # ─── OPEN QUESTIONS ────────────────────────────────────────────────────────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:thinking_face: OPEN QUESTIONS HEADING INTO NEXT WEEK*\n\n:one: *Did Rami\'s CSV arrive EOD Friday?* If yes, is the email blast queued? This is time-sensitive — data compound quickly.\n\n:two: *Comms agent ownership?* Currently Dana/Fatty/Davi. Ray wants screener completions in scope. Do you take it over or let the current owners run? Decide before next standup.\n\n:three: *Source claiming banner — trial users?* Ray and Matan want this by Monday. You need to answer: does it apply to trial users? How does it interact with the existing trial banner? Don\'t ship without answers.\n\n:four: *Indeed spend goal framing for v3 goals doc* — "optimal channel for each marginal dollar" needs to be written in exec-friendly language. What\'s the north star metric here?'
        }
    },
    {'type': 'divider'},

    # ─── MASTER ACTION LIST ────────────────────────────────────────────────────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:white_check_mark: YOUR MASTER ACTION LIST (Manan owns)*'
        }
    },
    {
        'type': 'section',
        'fields': [
            {
                'type': 'mrkdwn',
                'text': '*:red_circle: URGENT (this weekend/Monday)*\n• Draft v3 Q3 goals doc → share with Ray before John sees it\n• Confirm Rami\'s CSV + email blast status\n• Define source claiming banner UX (trial user + banner interaction) before Ray ships it\n• Ping Ted re: Shamir/Dvich for ML platform support on email blast'
            },
            {
                'type': 'mrkdwn',
                'text': '*:large_yellow_circle: HIGH (this week)*\n• Listen to Usman\'s call recordings — track excitement signals\n• Send Cindy: line cook analysis (D5/D30) + onboarding links for Abby\n• Review Cindy\'s design options for role/salary modal (due Mon midday)\n• Decide: take over comms agent ownership or not\n• Culinary Agents: schedule follow-on call on Indeed-boosting'
            }
        ]
    },
    {
        'type': 'section',
        'fields': [
            {
                'type': 'mrkdwn',
                'text': '*:large_blue_circle: MEDIUM (carry forward)*\n• Indeed duplicate detection: probe with test company?\n• Build Q3 OKR dashboard (track toward 80% healthy jobs)\n• ZipRecruiter follow-up call (1-2 weeks)\n• Salesforce table requirements → write up for Nelson\n• Share Q3 strategy + roadmap docs with full team'
            },
            {
                'type': 'mrkdwn',
                'text': '*:white_circle: OTHERS\' COURT (monitor)*\n• Dana: daily test performance report + Usman\'s talk track doc\n• Cindy: design options Mon midday\n• Rami: CSV + Linear board access + flag reasons doc\n• Ray: send job feed to Alice (Culinary Agents)\n• Alice: partner agreement review + 2-week feed impl.\n• Nelson: syndicate analytics handoff before EOMonth'
            }
        ]
    },
    {'type': 'divider'},

    # ─── PULSE CHECK ────────────────────────────────────────────────────────────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:bar_chart: WEEK AT A GLANCE*\n• *9 meetings* across 4 days (Jun 23-26)\n• *1 new partnership kicked off* (Culinary Agents)\n• *1 experiment launched* (talent pool line cook blast)\n• *1 new hire ramping* (Abby, Jul 7)\n• *1 key org change noted* (Dana out end of September)\n• *Q3 goals now locked* — three buckets, Indeed-first, line cook lens\n• *Zero state page shipped* :white_check_mark:'
        }
    },
    {'type': 'divider'},

    # ─── CLOSING NOTE ───────────────────────────────────────────────────────────
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Manan — you made a ton of consequential calls this week with clarity and conviction. The Indeed goal reframe alone will sharpen everything downstream. The Culinary Agents partnership is a quiet win that could compound fast. And the fact that Ray told you directly "I trust Manan, he is going to get us out of this problem" — that\'s the CEO\'s words echoed through your skip. You\'re the one. Enjoy your weekend and come back Monday ready to ship. :rocket:'
        }
    },
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': 'Chief of Staff digest | Jun 27, 2026 | Based on Granola notes from Jun 23-26'
            }
        ]
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'Your Week in Review: Jun 23-26, 2026 — 9 meetings, 8 decisions, full action plan inside.',
    'blocks': blocks
}


def preview():
    print('=' * 70)
    print('SLACK DIGEST PREVIEW — Manan Kothari | Week of Jun 23-26, 2026')
    print('=' * 70)
    for block in blocks:
        btype = block.get('type', '')
        if btype == 'header':
            sys.stdout.buffer.write(('\n### ' + block['text']['text'] + '\n').encode('utf-8', errors='replace'))
        elif btype == 'section':
            if 'text' in block:
                sys.stdout.buffer.write((block['text']['text'] + '\n').encode('utf-8', errors='replace'))
            if 'fields' in block:
                for f in block['fields']:
                    sys.stdout.buffer.write((f['text'] + '\n').encode('utf-8', errors='replace'))
        elif btype == 'divider':
            print('-' * 60)
        elif btype == 'context':
            for el in block.get('elements', []):
                sys.stdout.buffer.write((el['text'] + '\n').encode('utf-8', errors='replace'))
    print('=' * 70)


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
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('ok'):
                print(f'SUCCESS: Message sent to {CHANNEL}')
                print(f'Timestamp: {result.get("ts")}')
            else:
                print(f'ERROR: Slack API returned ok=false')
                print(f'Error: {result.get("error")}')
                print(f'Full response: {json.dumps(result, indent=2)}')
    except urllib.error.HTTPError as e:
        print(f'HTTP ERROR {e.code}: {e.reason}')
    except urllib.error.URLError as e:
        print(f'URL ERROR: {e.reason}')


if __name__ == '__main__':
    token = (
        os.environ.get('SLACK_TOKEN') or
        os.environ.get('SLACK_BOT_TOKEN') or
        os.environ.get('SLACK_API_TOKEN')
    )
    if token:
        print(f'Token found ({"SLACK_TOKEN" if os.environ.get("SLACK_TOKEN") else "SLACK_BOT_TOKEN" if os.environ.get("SLACK_BOT_TOKEN") else "SLACK_API_TOKEN"}). Sending...')
        send_slack(token)
    else:
        print('No Slack token found in environment. Showing preview...')
        print('To send: set SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN env var.')
        preview()
