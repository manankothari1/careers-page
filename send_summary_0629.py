#!/usr/bin/env python3
"""
Daily Digest - Sunday Jun 29 00:00 UTC = Sunday Jun 28 5pm PDT
Monday Battle Plan for Manan Kothari
"""

import json
import os
import sys
import urllib.request
import urllib.error


CHANNEL = 'D06E4QMHCNN'


def build_payload():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Sunday Debrief + Monday Battle Plan  |  Week of Jun 29",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hey Manan! No meetings today (Sunday) -- you earned the rest. :muscle: But tomorrow kicks off what could be *the most pivotal week of Q3*, so let's make sure you walk in locked and loaded. Here's your full debrief from last week + exactly what to attack first thing Monday morning."
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:trophy: Last Week's Big Wins (Jun 22-26)*\n_13 meetings, 13 decisions -- here's what mattered most:_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":white_check_mark: *Indeed goal locked* — New metric: FFH jobs w/ zero Indeed applicants on D5 < 10% (currently 41%). This is tight, measurable, and ties in source claiming + job reposting + copy-a-job. Ray is aligned. John gets the v3 doc next.\n\n"
                    ":white_check_mark: *Talent pool email blast green-lit* — 86 line cook jobs, 25-mile radius, 2K cap/job, recency-ranked. Rami had the CSV ready EOD Jun 25. UTM tracking (utm_campaign=generic vs recruiter) is in. This experiment is *live or very close to live*.\n\n"
                    ":white_check_mark: *Role title + salary optimization UX decided* — Intercept modal (not inline), critical warning framing for title, softer nudge for salary. Cindy is designing options now, due to you *Monday midday today*.\n\n"
                    ":white_check_mark: *Zero state page shipped* — 49% lift in ICP trial starts from 'drive off the lot' framing. No product changes, just positioning. Proof that copy + framing is your highest-leverage lever right now.\n\n"
                    ":white_check_mark: *Abby onboarding plan locked* — Starts Jul 7 (one week from today!). First project: Indeed source claiming. Then auto go-live, then manual intake. Cindy is prepping an onboarding doc."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:fire: URGENT: Do These First Monday Morning*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*1. Review Cindy's design options* :art:\nDue: Mon midday\nIntercept modal vs inline for title/salary recommendations. She's shipping options to you this morning. Give feedback before Wednesday look-ahead."
                },
                {
                    "type": "mrkdwn",
                    "text": "*2. Confirm email blast status* :email:\nDue: ASAP\nRami was supposed to send CSV EOD Jun 25 so blast goes out 'tomorrow morning' (Jun 26). Has it gone out? If not, unblock immediately."
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*3. Draft v3 Q3 goals doc* :memo:\nDue: Before it goes to John\nThree-bucket structure (OEM spend, talent pool, funnel optimization). Ray is aligned on substance, just needs John's formatting. Share with Ray first."
                },
                {
                    "type": "mrkdwn",
                    "text": "*4. Ping Ted re: Shamir/Dvich* :mega:\nNeed ML/data platform support for email blast pipeline. Shamir may be back this week. Dvich is involved in hiring -- either works."
                }
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:calendar: This Week's High-Priority Actions (Jun 29-Jul 3)*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":large_orange_circle: *Listen to Usman's call recordings* — Track excitement signals, not booking rate. Dana reframed the script; have any calls come in since? The personal recruiter hypothesis is still unvalidated.\n\n"
                    ":large_orange_circle: *Define source claiming banner UX* — Ray + Matan want this shipped ASAP but key questions are unresolved: (a) does it show to trial users? (b) how does it interact with the existing trial banner? Don't let this ship underbaked.\n\n"
                    ":large_orange_circle: *Send Cindy: line cook analysis (D5/D30) + onboarding links for Abby* — She's building the onboarding doc. Line cook data is also context for the new line cook Q3 goal.\n\n"
                    ":large_orange_circle: *Decide comms agent ownership* — Ray left this open. You can take it or let Dana/Fatty/Davi own it. The screener funnel data suggests the drop-off problem is overstated (~70% click, ~60% start, ~80-90% complete once started). Make a call and communicate it.\n\n"
                    ":large_yellow_circle: *Send table name/schema to Anudeep* — Fallback pipeline if High Touch doesn't connect to Iterable. Confirm with Rohit on the High Touch route first.\n\n"
                    ":large_yellow_circle: *Follow up with Jenna on SEO indexing guidance* — Carlo is running the headless browser spike; Jenna's guidance on optimize-tagging-first is needed before deciding between headless browser vs. admin access.\n\n"
                    ":large_yellow_circle: *Verify Homebase Boost source display* — Close the ticket. Quick win.\n\n"
                    ":large_yellow_circle: *Loop Tanner into job description + salary rec UI design*"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:rocket: Countdown to Key Milestones*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":countdown: *7 days* — Abby starts (Jul 7). Have her onboarding plan + first ticket (source claiming) crystal clear.\n"
                    ":countdown: *~2 weeks* — Culinary Agents feed integration kicks off. Confirm follow-on call with Jeff Silverstein on Indeed-boosting mechanics.\n"
                    ":countdown: *EOMonth* — Nelson transitions to ~5hrs/week. Spec-driven dev formalized. Make sure his open deliverables (Salesforce table write-up, Q3 OKR dashboard) are handed off cleanly."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:bar_chart: Q3 Pulse Check*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Healthy job rate*\n30% of ICP jobs\n:dart: Target: 80%"
                },
                {
                    "type": "mrkdwn",
                    "text": "*FFH jobs w/ 0 Indeed applicants D5*\n41% (new goal: <10%)\n:fire: This is your north star"
                },
                {
                    "type": "mrkdwn",
                    "text": "*OEM boost rate*\n1.64% of jobs\n:dart: Target: 10% spending"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Trial volume*\n700K+ (broke the 600s barrier!)\n:chart_with_upwards_trend: Zero state page is working"
                }
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*:brain: Chief of Staff's Take*\n\n"
                    "Last week was *strategically clarifying* — you came out with a sharper Indeed goal, a validated framing win (49% lift!), and a concrete experiment in flight. The week ahead is about *execution and unblocking*. Three things could slip if you're not careful:\n\n"
                    "1. :warning: *Email blast* — if it hasn't gone out yet, that's your most time-sensitive unblock. Find out now.\n"
                    "2. :warning: *Source claiming banner* — Ray + Matan have momentum but the UX questions are real. Define it before it gets shipped half-baked.\n"
                    "3. :warning: *Q3 goals doc* — Ray needs this before John. Don't let the format block the substance from landing.\n\n"
                    "You've got Ray's full trust, a designer who's ahead of the work, and a new PM starting in a week. This is your moment. Go crush it. :muscle:"
                )
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "Chief of Staff digest | Sunday Jun 28, 2026 5pm PDT | Based on 13 meetings from Jun 22-26 | Next digest: Mon Jun 29 5pm PDT"
                }
            ]
        }
    ]

    return {
        "channel": CHANNEL,
        "text": "Sunday Debrief + Monday Battle Plan | Week of Jun 29",
        "blocks": blocks
    }


def send_slack(payload, token):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=utf-8'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            return result
    except urllib.error.URLError as e:
        return {'ok': False, 'error': str(e)}


def preview(payload):
    sys.stdout.buffer.write(('\n=== SLACK MESSAGE PREVIEW ===\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(f'Channel: {payload["channel"]}\n'.encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(f'Fallback: {payload["text"]}\n'.encode('utf-8', errors='replace'))
    sys.stdout.buffer.write('--- BLOCKS ---\n'.encode('utf-8', errors='replace'))
    for block in payload['blocks']:
        btype = block.get('type', '')
        if btype == 'header':
            line = '[HEADER] ' + block['text']['text']
        elif btype == 'section':
            if 'text' in block:
                line = '[SECTION] ' + block['text']['text'][:200]
            elif 'fields' in block:
                line = '[FIELDS] ' + ' | '.join(f['text'][:80] for f in block['fields'])
            else:
                line = '[SECTION]'
        elif btype == 'divider':
            line = '---'
        elif btype == 'context':
            line = '[CONTEXT] ' + block['elements'][0]['text']
        else:
            line = f'[{btype.upper()}]'
        sys.stdout.buffer.write((line + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write('=== END PREVIEW ===\n'.encode('utf-8', errors='replace'))


if __name__ == '__main__':
    token = (
        os.environ.get('SLACK_TOKEN') or
        os.environ.get('SLACK_BOT_TOKEN') or
        os.environ.get('SLACK_API_TOKEN') or
        ''
    )

    payload = build_payload()

    if not token:
        print('No SLACK_TOKEN found. Showing preview only.')
        print('Add SLACK_TOKEN (or SLACK_BOT_TOKEN) in Cursor Dashboard > Cloud Agents > Secrets.')
        preview(payload)
        sys.exit(0)

    print(f'Sending digest to channel {CHANNEL}...')
    result = send_slack(payload, token)
    if result.get('ok'):
        print(f'Successfully sent! ts={result.get("ts")}')
    else:
        print(f'ERROR sending: {result.get("error")}')
        preview(payload)
        sys.exit(1)
