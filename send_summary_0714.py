#!/usr/bin/env python3
"""Daily Chief of Staff Digest — Tuesday, July 14, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = 'D06E4QMHCNN'
TOKEN = os.environ.get('SLACK_TOKEN') or os.environ.get('SLACK_BOT_TOKEN') or os.environ.get('SLACK_API_TOKEN', '')

blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': ':spiral_note_pad: Chief of Staff Daily Digest | Tuesday, July 14',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Hey Manan :wave: — solid execution day. One focused standup, two cross-team company sessions, and you shipped design work last night that\'s already moving toward a ship-this-week. Here\'s your full debrief.'
        }
    },
    {
        'type': 'divider'
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:calendar: TODAY\'S MEETINGS (3)*\n• 7:00 AM — SB: Full Pod — Us + Inspiration _(Scheduling pod retro — cross-team observer)_\n• 8:45 AM — Hiring Leads Standup _(your team — decisions below)_\n• 11:30 AM — Process Reset _(Scheduling pod org update — Ramona returning as senior EM)_'
        }
    },
    {
        'type': 'divider'
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:white_check_mark: DECISIONS MADE TODAY*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*1. Salesforce Intervention System is LIVE* :rocket:\n*Decision:* Ray\'s system is fully operational with 4 intervention types: Welcome, Low Applicant Flow, Low Early Engagement, and Ready to Convert. Reps now burn down tasks in a prioritized queue — they no longer self-direct. Hiring HQ in Salesforce shows all jobs, applicant counts, screener completions, and top matches per job.\n*Why it matters:* This is the scalable infrastructure you\'ve been building toward. Unhealthy job signals can now trigger automated Salesforce actions — the trigger-based strategy locked Jul 13 now has its plumbing. You confirmed cold calling is no longer the primary bet; this system is the new motion.\n*Your alignment:* You flagged the in-product version of this is the next frontier — Fadi picks up that work next week or the week after.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*2. Opportunity Creation Logic Fix — Confirmed for Next Sprint* :wrench:\n*Decision:* Current Salesforce opportunity creation is based on "first job post" — which breaks for returning users and V1 migrants. Fix: trigger opportunity creation off a "trial started" domain event. Jatin confirmed it\'s ticketed and will get in for next sprint.\n*Why it matters:* V1 migrants represent a big chunk of your pipeline. Without this fix, they fall through the Salesforce net entirely — no intervention, no conversion follow-up.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*3. V1 Migration Trial Spike Flagged as Concerning — Investigation Live* :rotating_light:\n*Decision:* Last week was a high-trial week; ~70%+ attributed to V1 migrations. But auto-trial was turned off. Over 200 unexpected trials were created — source unknown. Dana is investigating whether these users genuinely opted into a trial from manual mode vs. an unintentional trigger.\n*Why it matters:* 200+ unexpected trials could mean (a) a bug that\'s converting people who shouldn\'t be converted — metric inflation, or (b) V1 users finding their own path to trial, which is actually great signal. Either way you need the answer before Jul 20 cutover in 6 days.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*4. Applicant Flow Designs Ready — Two Tracks* :art:\n*Decision:* You completed the reactivate + job details flow last night. Two designs now ready for Fadi review: (1) Branch-based flow — could ship THIS WEEK if engineering checks out. (2) HTML file — targets the upcoming sprint, needs to be design-ready by end of this week for look-ahead.\n*Why it matters:* Fadi and Jatin need these today to hit your sprint timeline.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*5. Look-Ahead Cadence Cleaned Up* :broom:\n*Decision:* Look-ahead stays on Wednesday. Jatin is deleting his duplicate Tuesday look-ahead. Jatin added as optional to your Wednesday look-ahead invite.\n*Why it matters:* Jatin now has visibility into applicant flow deadlines without the overhead of attending everything.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*6. Indeed Source Name Change — Green Light* :white_check_mark:\n*Decision:* Customer confirmed the source name change. You\'re making the update and sending the PR over.\n*Why it matters:* Small but important — source name accuracy is foundational to source claiming integrity.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*7. Salesforce Alignment Protocol Established* :handshake:\n*Decision:* Ray asked that any Salesforce ideas go through him early — not raw field requests. He\'s confident the system can do anything you need; just lead with the outcome you want, not the implementation.\n*Why it matters:* Keeps the Salesforce data model clean. You acknowledged and aligned.'
        }
    },
    {
        'type': 'divider'
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:dart: YOUR ACTION ITEMS — P0 FIRST*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:red_circle: P0 — DO TODAY*\n• :mega: *Send Fadi the reactivate/job details branch link + HTML file* — branch may ship this week, HTML targets next sprint. He\'s waiting.\n• :mega: *Send Jatin a context message* before he reviews the designs — he needs background on the two flows.\n• :mega: *Send Indeed source name change PR* — customer already confirmed, change is ready.\n• :mega: *Add Jatin as optional to Wednesday look-ahead invite* — confirmed in standup.\n• :mega: *SALARY RECS PRESENTATION IS TOMORROW (Jul 15)* — confirm Rami\'s scope landed EOD Jul 13 ✓, prep your anchors: well below market = 26.1% get 20+ apps; at market = +7-8%; above market = +12%. This is your most important deliverable of the week.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:large_yellow_circle: P1 — THIS WEEK*\n• Approve Ugu\'s backend PR for in-product OEM setup call prompts _(from Jul 13 — still open)_\n• Confirm Fadi\'s source claiming first-pass design is done _(targeted Jul 14 — check with him)_\n• Follow up on Carlo Harness/OpenSpec status _(deadline was Jul 10 — 4 days overdue — this needs a status today)_\n• Answer "which roles are healthy independent of Indeed?" → Nelson/data _(from Jul 13)_\n• Loop in Paul or Kan on salary rec role normalization _(ahead of presentation tomorrow)_'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:large_blue_circle: P2 — WHEN YOU HAVE CYCLES*\n• Chat Ray about Rami DS capacity structural bottleneck\n• Review Dana\'s V1 migration trial investigation results (200+ unexpected trials)\n• Abby ownership area — needs clear domain by end of this week\n• Send UTMs to Rami for talent pool segmentation\n• Update hiring cycle 4 projects in Linear with owners + target dates'
        }
    },
    {
        'type': 'divider'
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:eyes: WATCH LIST — THINGS TO STAY ON*\n\n• *V1→V2 Cutover: 6 days out (Jul 20)* — 200+ unexpected V1 trials are the new wrinkle; Dana investigating. Comms set, CS empowered. Monitor screener gap + star/fav gap post-cutover.\n• *Carlo Harness/OpenSpec: OVERDUE (Jul 10 deadline)* — 4 days with no confirmation. This one needs a status TODAY.\n• *Ugu\'s backend PR:* Still waiting on your approval. Unblocks in-product OEM setup call prompts (P0 from Jul 13 Hiring WIR with John).\n• *FFH D5 zero-applicant rate:* Still at 41% (Q3 target <10%). Source claiming fix is the unlock — check Fadi\'s design progress.\n• *Salary Recs presentation: TOMORROW (Jul 15)* — Rami scope should have landed. If not, you need to know tonight.\n• *Boost purchase bug:* 2 reporters, revenue-impacting — still no owner as of Jul 13.\n• *Dana leaving end of September:* ~10 weeks. No succession planning started yet.\n• *Abby (Week 2):* Needs clear ownership area by end of this week — don\'t let this drift.'
        }
    },
    {
        'type': 'divider'
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:trophy: THE BIG PICTURE — WHERE YOU STAND*\nYou\'re 6 days from the most significant product moment of Q3: the V1→V2 cutover. The Salesforce intervention system going live today is a huge unlock — trigger-based engagement is the new motion, and the infrastructure is now there. Tomorrow\'s salary recs presentation is your highest-leverage internal moment this week. You finished design work last night at home. That\'s the kind of energy that separates great PMs from good ones. Keep that up.'
        }
    },
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': '_Your Chief of Staff :briefcase: | Jul 14, 2026 at 5:00 PM PDT | 3 meetings reviewed_'
            }
        ]
    }
]

def preview():
    print('=' * 70)
    print('CHIEF OF STAFF DAILY DIGEST — Jul 14, 2026')
    print('=' * 70)
    for block in blocks:
        if block['type'] == 'header':
            sys.stdout.buffer.write(('\n### ' + block['text']['text'] + '\n').encode('utf-8', errors='replace'))
        elif block['type'] == 'section':
            sys.stdout.buffer.write(('\n' + block['text']['text'] + '\n').encode('utf-8', errors='replace'))
        elif block['type'] == 'divider':
            print('\n' + '-' * 70)
    print('\n' + '=' * 70)

def send():
    payload = {
        'channel': CHANNEL,
        'blocks': blocks,
        'text': 'Chief of Staff Daily Digest | Tuesday, July 14, 2026'
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
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
                print('SUCCESS: Slack message sent to', CHANNEL)
                return True
            else:
                print('ERROR: Slack API error:', result.get('error', 'unknown'))
                return False
    except urllib.error.URLError as e:
        print('ERROR: Network error:', e)
        return False

if TOKEN:
    sent = send()
    if not sent:
        print('\n--- PREVIEW (send failed) ---')
        preview()
else:
    print('No SLACK_TOKEN found — preview only.\n')
    preview()
