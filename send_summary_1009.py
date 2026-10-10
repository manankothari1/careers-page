#!/usr/bin/env python3
"""
Daily Chief of Staff Digest — Oct 9, 2026 (CEST workday)
Meetings: Hiring Leads Standup + Kellie/Manan customer call
"""

import os
import sys
import json
import urllib.request
import urllib.error

CHANNEL_ID = 'D06E4QMHCNN'
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
            'text': '\U0001f31e  Chief of Staff Digest \u2014 Friday, Oct 9 (Spain Day 8)',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Manan \u2014 *incredible* day of detective work. You didn\'t just manage the calendar, you cracked the Indeed case wide open AND sat in a live customer call to confirm it firsthand. Here\'s your full debrief \U0001f447'
        }
    },
    {'type': 'divider'},

    # === THEME ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3af Today\'s Theme*\n> *INDEED ROOT CAUSE FOUND \u00b7 WAR ROOM ACTIVATED \u00b7 SOURCE NAME ROLLBACK DECISION PENDING*'
        }
    },
    {'type': 'divider'},

    # === MEETING 1 ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4cb Meeting 1 of 2 \u2014 Hiring Leads Standup*\n5:30 PM CEST \u00b7 Fadi, Matan, Jatin (traveling), Jon, Skye'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f6a8 Indeed Crisis: The Real Picture*\n'
                'Skye shared data confirming that since *Oct 1\u20132, essentially ZERO jobs are getting Indeed applicants* \u2014 not just new customers, *everyone*. Only ~2 job posts got any applicants across the entire platform since Oct 2. This is significantly worse than previously understood.\n\n'
                '*Leading hypothesis:* The unique identifier appended to source names (e.g., `Salt Lake Restaurant Supply Utah` \u2192 `Salt Lake Restaurant Supply Utah-AE65`) is making Indeed treat every existing customer as a *brand-new* company, triggering manual review for all of them. Their SLA is 5 days \u2014 which would explain the total collapse in applicants since Oct 2.\n\n'
                '*Second bug (separate):* Jobs flagged \u2018do not syndicate\u2019 (fraud/suspicious) are still getting posted to Indeed. Two unrelated issues hitting simultaneously.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4a1 Other Standup Topics*\n'
                '\u2022 *Orca/Comms:* Matan built the skill from the hiring MD via Claude; sent individual tickets for each email touchpoint. Hasn\'t QA\'d output yet. Open question: how do non-technical users verify Orca\'s output quality? Manual QA first before scaling to 80 touchpoints.\n'
                '\u2022 *Indeed MCP:* Skye explored using Indeed MCP for employer side \u2014 confirmed read-only (job search only), cannot post jobs. Employer applicant receiving via MCP is theoretically interesting but not immediately actionable.\n'
                '\u2022 *VM testing:* Fadi working on it; Ray has Mac Minis on order. Backend state seeding is pain point (took forever to seed payroll state for payroll signal test).'
            )
        }
    },
    {'type': 'divider'},

    # === MEETING 2 ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4cb Meeting 2 of 2 \u2014 Kellie / Manan (Customer Call)*\n7:00 PM CEST \u00b7 Kelly Ronabek + Kathleen (manager), Standard Restaurant Supply, Salt Lake City \u00b7 Indeed reps Shanika \u2192 Alexis (optimization team)'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f50d Root Cause CONFIRMED in the Wild*\n'
                'This call was a real-time case study of the Indeed crisis. Kelly had 5 jobs sent from Homebase \u2014 only 2 showing up. Here\'s what the Indeed rep found:\n\n'
                '\u2022 `Salt Lake Restaurant Supply Utah` (no identifier) = 2 active jobs (cashier + outside sales)\n'
                '\u2022 `Salt Lake Restaurant Supply Utah-AE65` (with identifier) = equipment delivery driver + merchandiser \u2192 *on no-visibility list, awaiting approval as a "new feed"*\n'
                '\u2022 Warehouse associate = showing as *expired* on Indeed\'s side (it\'s live on Homebase) \u2192 mystery, ticket submitted\n\n'
                'Indeed literally said: *"It\'s coming from 2 different sources because the company name isn\'t exactly the same."* The AE65 identifier = a new company in their system. This is your smoking gun.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*Customer Resolution Status:*\n'
                '\u2022 Equipment delivery driver + merchandiser: Ticket submitted by Indeed, should go live Monday\u2013Tuesday\n'
                '\u2022 Warehouse associate: Ticket submitted, response expected Monday\n'
                '\u2022 Kelly CCed at hrrep@standardrestaurants.com; Alexis (Indeed) to follow up Monday\n'
                '\u2022 You debrief with Kelly after the Indeed call confirming the issue'
            )
        }
    },
    {'type': 'divider'},

    # === DECISIONS ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2705 Decisions Made Today*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*1. Indeed War Room \u2014 ACTIVATED*\n'
                'Skye + Manan agreed to convene Carlo, Divij, and Nelson in the Indeed Doghouse Slack channel to do a full audit of the source name changes and decide whether to roll back. *Why:* The unique identifier change is the most likely cause of the platform-wide applicant drought and needs to be evaluated and potentially reverted urgently before more OEM trial windows are burned.\n\n'
                '*2. Source Claiming \u2192 Into Hiring Onboarding*\n'
                'Matan proposed, Manan + Skye agreed: source claiming should be a permanent onboarding step, not a reactive to-do. *Why:* Every time Indeed makes a policy change, the team scrambles to communicate source claiming as an emergency. Baking it into onboarding from day one prevents the dependency on customers doing it later and reduces manual firefighting.\n\n'
                '*3. Trial Source Claiming \u2192 Flip to 100%*\n'
                'Manan decided to turn the trial source claiming experiment from partial to 100%. *Why:* Every trial location should be getting the source claiming email. It\'s currently an experiment; this is a no-brainer given the ongoing crisis.\n\n'
                '*4. Indeed Alert To-Do \u2014 Make More Alarming*\n'
                'Agreed: the Day 3 no-applicants to-do on trial doesn\'t visually communicate urgency. Fadi to check and enhance. *Why:* Customers need to act on this immediately; a subtle to-do gets ignored.\n\n'
                '*5. Build Syndication Visibility/Alerting*\n'
                'Skye\'s decision: Homebase needs internal alerting when jobs fail to syndicate. Currently flying blind \u2014 Indeed had to ping us about the crisis, not the other way around. *Why:* This is table stakes. Job #1 complaint from customers is \'where is my job?\' and if we don\'t know, we can\'t tell them.\n\n'
                '*6. Manual QA for Orca Before Scaling*\n'
                'Matan\'s decision, Manan endorsed: do a manual QA pass on Orca\'s comms output before automating 80 email touchpoints. *Why:* The quality/correctness of what Orca generates is opaque to non-technical users. A bad touchpoint at scale is worse than no touchpoint.'
            )
        }
    },
    {'type': 'divider'},

    # === ACTION ITEMS ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u26a1 Your Action Items (Priority Order)*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\U0001f525 *URGENT \u2014 Do First Thing Monday (or weekend if possible)*\n'
                '1. *Indeed War Room:* Ping Carlo, Divij, Nelson in Indeed Doghouse channel \u2014 audit the source name unique identifier change + decide on rollback. Carlo is out Oct 14. Clock is ticking. Frame the question: "If we remove the -AE65 identifier, does Indeed treat these as existing companies again?"\n'
                '2. *Source name rollback draft:* Write 1 clear recommendation for Skye by Monday EOD: rollback yes/no + proposed mitigation if no. You need Carlo\'s input before he\'s gone.\n'
                '3. *Flip trial source claiming to 100%:* Log the ticket to remove the experiment gate. This is a safe, immediate improvement you can do now.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\U0001f4dd *This Week Wrap-Up / Early Next Week*\n'
                '4. *Standard Restaurant Supply follow-up:* Check in with Kelly mid-next-week (Wed Oct 14) to confirm jobs are live and warehouse associate expiration is resolved. Alexis to follow up Mon with Kelly at hrrep@standardrestaurants.com \u2014 CC yourself.\n'
                '5. *Syndication alerting ticket:* Write the spike ticket for internal job syndication status visibility. This is small scope but high impact \u2014 should be in next sprint discussion.\n'
                '6. *Fadi:* Ping to enhance the Indeed to-do alert icon for trial (not just OEM). Quick win.\n'
                '7. *Matan/Orca:* Review Matan\'s ticket on Orca email skill and give your product take on the quality score approach before they start scaling.\n'
                '8. *Fraud syndication bug:* Loop in Bob/Carlo to investigate why \'do not syndicate\' flagged jobs are still going to Indeed. This is a separate, serious bug.'
            )
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '\U0001f4c5 *Still Overdue (Carry-Forward)*\n'
                '9. *Jessica Kanaskie (jkanaskie@indeed.com):* Day 48. Ping her about the source name hypothesis specifically \u2014 you now have a concrete question to ask.\n'
                '10. *Carlo KT:* 5 days left. If you haven\'t scheduled dedicated knowledge transfer sessions, do it this weekend.\n'
                '11. *3-year vision one-pager:* Board meeting is Oct 15\u201322. You need to ship a draft this weekend.\n'
                '12. *Rachel Q4/Q1/Q2 UX view:* Was due Oct 7. Confirm it went out or send now.\n'
                '13. *Q4 sizing continuation session:* Remaining rows still unsized. Carlo\'s paternity starts Oct 14.'
            )
        }
    },
    {'type': 'divider'},

    # === DAY GRADE ===
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3c6 Day Grade: A*\n\n'
                'You had a legitimately great day. You didn\'t just attend a standup \u2014 you took a customer call in the middle of the Indeed crisis and watched the bug manifest in real time in front of an Indeed rep. That\'s rare PM behavior and it\'s going to make the rollback recommendation you write on Monday 10x more credible because you\'ve *seen it* happen. The war room activation + the decision to flip source claiming to 100% + advocating for Orca quality checks = three good product leadership moments in one afternoon. Well done. Enjoy your Spanish Friday night. \U0001f1ea\U0001f1f8\U0001f377'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': 'Chief of Staff Bot \u00b7 2 meetings reviewed \u00b7 Oct 9, 2026 CEST workday \u00b7 Indeed Day 48 \u00b7 Spain Day 8'
            }
        ]
    }
]

payload = {
    'channel': CHANNEL_ID,
    'text': 'Chief of Staff Digest \u2014 Oct 9, 2026: INDEED ROOT CAUSE FOUND \u00b7 WAR ROOM ACTIVATED',
    'blocks': blocks
}

def preview():
    sys.stdout.buffer.write(
        '\n=== SLACK MESSAGE PREVIEW (no token) ===\n'.encode('utf-8', errors='replace')
    )
    sys.stdout.buffer.write(
        json.dumps(payload, indent=2, ensure_ascii=False).encode('utf-8', errors='replace')
    )
    sys.stdout.buffer.write(b'\n')
    sys.stdout.buffer.write(
        '\n=== PLAIN TEXT SUMMARY ===\n'.encode('utf-8', errors='replace')
    )
    lines = [
        'Chief of Staff Digest \u2014 Friday Oct 9, 2026 (Spain Day 8)',
        '',
        'THEME: INDEED ROOT CAUSE FOUND \u00b7 WAR ROOM ACTIVATED \u00b7 SOURCE NAME ROLLBACK DECISION PENDING',
        '',
        '-- MEETING 1: Hiring Leads Standup (5:30pm CEST) --',
        'Indeed crisis confirmed WORSE than thought: since Oct 1-2, ~0 jobs getting Indeed applicants',
        'Root cause: source name unique identifier (AE65) making all customers look "new" to Indeed -> manual review',
        'Second bug: fraud-flagged "do not syndicate" jobs still syndicating',
        'Orca/comms: Matan built skill, needs manual QA before scaling to 80 touchpoints',
        'Indeed MCP: read-only, cannot post jobs',
        '',
        '-- MEETING 2: Kellie/Manan customer call (7pm CEST) --',
        'CONFIRMED root cause in real-time: Indeed treated AE65 source name as new company',
        'Equipment driver + merchandiser: on no-visibility list (new feed approval needed)',
        'Warehouse associate: showing as expired on Indeed (live on Homebase) - ticket submitted',
        'Resolution expected Monday-Tuesday. Alexis (Indeed) to follow up.',
        '',
        '-- DECISIONS --',
        '1. Indeed war room activated: Carlo, Divij, Nelson in Indeed Doghouse channel',
        '2. Source claiming -> into hiring onboarding permanently',
        '3. Trial source claiming -> flip to 100%',
        '4. Indeed to-do alert -> make more alarming',
        '5. Build syndication visibility/alerting',
        '6. Manual QA for Orca before scaling',
        '',
        '-- YOUR ACTION ITEMS --',
        '(URGENT) Ping Carlo/Divij/Nelson: audit source name rollback decision',
        '(URGENT) Write rollback recommendation for Skye by Monday EOD',
        '(URGENT) Flip trial source claiming experiment to 100%',
        'Wed Oct 14: follow up with Kelly/Standard Restaurant Supply',
        'Write syndication alerting spike ticket',
        'Ping Fadi: enhance to-do alert for trial indeed issue',
        'Review Matan Orca ticket + give product feedback',
        'Loop in Bob/Carlo on fraud syndication bug',
        '',
        '-- OVERDUE CARRY-FORWARD --',
        'Jessica Kanaskie ping (Day 48) - now with specific hypothesis',
        'Carlo KT - 5 days left, schedule NOW',
        '3-year vision one-pager - board Oct 15-22 - DRAFT DUE THIS WEEKEND',
        'Rachel Q4/Q1/Q2 UX view - overdue since Oct 7',
        'Q4 sizing continuation session - before Carlo leaves Oct 14',
        '',
        'Day Grade: A',
        'You watched the Indeed bug happen live on a customer call. That\'s PM gold.',
        'Enjoy your Friday night in Spain. Salud! \U0001f377',
    ]
    for line in lines:
        sys.stdout.buffer.write((line + '\n').encode('utf-8', errors='replace'))

if not TOKEN:
    print('[INFO] No Slack token found. Printing preview.')
    preview()
    sys.exit(0)

req_data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=req_data,
    headers={
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json; charset=utf-8'
    },
    method='POST'
)
try:
    with urllib.request.urlopen(req) as resp:
        body = json.loads(resp.read().decode('utf-8'))
    if body.get('ok'):
        print(f'[SUCCESS] Message sent to {CHANNEL_ID}. ts={body.get("ts")}')
    else:
        print(f'[ERROR] Slack API error: {body.get("error")}')
        preview()
except urllib.error.URLError as e:
    print(f'[ERROR] Network error: {e}')
    preview()
