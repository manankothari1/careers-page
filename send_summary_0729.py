#!/usr/bin/env python3
"""Daily digest for Manan Kothari - Jul 29, 2026 (Wed PDT)"""
import os
import json
import urllib.request
import urllib.error
import sys

CHANNEL = 'D06E4QMHCNN'
token = (os.environ.get('SLACK_TOKEN') or
         os.environ.get('SLACK_BOT_TOKEN') or
         os.environ.get('SLACK_API_TOKEN'))

def build_blocks():
    blocks = []

    # Header
    blocks.append({
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': '\U0001f31f Daily Digest \u2014 Wednesday, Jul 29',
            'emoji': True
        }
    })

    # Intro
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Manan! Big day \u2014 2 meetings, 5 key decisions, and a genuine enterprise win. '
                'You got intel straight from Indeed\'s team, locked a franchise architecture, and greenlit a feature '
                'that could move the needle on your Q3 line cook zero-applicant problem. Here\'s your full rundown \U0001f447'
            )
        }
    })

    blocks.append({'type': 'divider'})

    # Meeting 1 header
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4de 10:30 AM \u2014 Scooters x Indeed x Homebase*\n'
                '_With: Lacey Navarrete (Scooter\'s Coffee), Olivia Anderson + Maria Vaspasiano (Indeed), '
                'Christofer Peralta (Homebase)_'
            )
        }
    })

    # Meeting 1 decisions
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u2705 Decision 1: Franchise Source Naming Architecture \u2014 LOCKED*\n'
                'Unique ID per franchise (e.g. \'Scooters-1234\'), *not* city/state and *not* street address. '
                'Two franchises can share the same city; unique ID is cleanest.\n'
                '_Why it matters:_ Prevents cross-franchise duplicate flags on Indeed + enables per-franchise '
                'advertiser accounts. Olivia does a manual copy-paste to link each unique source name to the '
                'franchise\'s Indeed advertiser ID. Corporate (Lacey) retains master visibility. Franchise '
                'accounts optional \u2014 jobs still post without one.\n\n'
                '*\u2705 Decision 2: Trust & Safety Ticket \u2014 Olivia Owns It*\n'
                'Root cause: Scooters\' website still points to TalentReef (old ATS) \u2014 Indeed flagged the '
                'mismatch. Olivia submitted the ticket (72-hr window). Just need *Lacey to send written '
                'confirmation* of the migration. Best part: one ticket covers all 300+ Scooters locations. '
                'Done.'
            )
        }
    })

    # Meeting 1 intel
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4a1 Intel Straight From Indeed\'s Team (bookmark this):*\n'
                '\u2022 ATS jobs have *NO 30-day timer* on Indeed\'s end \u2014 that 30-day window only applies '
                'to jobs posted directly on Indeed. Keep ATS jobs open as long as you\'re hiring.\n'
                '\u2022 Reposting a job within a few weeks = \'job copy\' flag. Refreshing *decreases* '
                'visibility, not increases it.\n'
                '\u2022 ATS jobs always beat direct Indeed posts; any direct post for the same role then '
                'requires sponsorship.\n'
                '\u2022 Extra verbiage in job titles (e.g. \'Barista \u2013 Sign-On Bonus\') reduces '
                'visibility + triggers sponsorship. Title should be just: Barista.\n'
                '\u2022 Salary discrepancies within job description = flagged.\n'
                '\u2022 Always include *full street address* to prevent cross-franchise duplicate flags \u2014 '
                'city/state is not unique enough.\n'
                '\u2192 *This confirms your Renew Jobs architecture is 100% correct.* '
                'Push the timestamp forward, never close and repost. \U0001f91c'
            )
        }
    })

    blocks.append({'type': 'divider'})

    # Meeting 2 header
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4cb 12:00 PM \u2014 Lookahead (Applicant Flow)*\n'
                '_With: Matan, Ugo, Tanner, Izzy, Jatin, Ray, Carlo, Fadi_'
            )
        }
    })

    # Meeting 2 decisions
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u2705 Decision 3: Talent Pool Outreach \u2014 GREENLIT (1-2 days MVP)*\n'
                'Flow: post hard-to-fill role \u2192 OEM sees modal w/ nearby candidate count (from your '
                'existing MSA CSV) + rotating obfuscated profiles \u2192 OEM edits pre-filled SMS \u2192 '
                'Homebase sends via admin CSV upload \u2192 Carlo runs rake task to raw-send SMS to all rows.\n'
                '_Key calls made:_ Raw text only (no chips/bolding UX \u2014 that\'s complexity without '
                'validation). Two separate lists: display list (count from CSV) vs. send list (Databricks query). '
                'Message stored as: job request ID \u2192 message body in a table.\n'
                '_Rationale:_ Low effort, potentially massive unlock for line cook zero-applicant problem. '
                'Prove hypothesis before investing in automation.\n\n'
                '*\u2705 Decision 4: Sprint Sizing Ritual \u2014 LAUNCHED (Jatin\'s initiative)*\n'
                'Engineers collectively t-shirt-size each incoming project at Lookahead. '
                'S=<3d, M\u22481wk, L=full sprint.\n'
                '_Why it\'s smart:_ Forces PM/eng scope alignment before sprint planning, not after. '
                'Will save you real pain downstream.\n\n'
                '*\u2705 Decision 5: Monday Reassessment Queue \u2014 3 Projects Ready*\n'
                '1\ufe0f\u20e3 Job page SEO fixes (small)\n'
                '2\ufe0f\u20e3 No Indeed Applicants by Day 3 \u2014 reuses Carlo\'s Indeed work (small/medium)\n'
                '3\ufe0f\u20e3 Franchise job posting \u2014 source name + company name fixes '
                '(small \u2014 you\'re filling in ticket content today)\n\n'
                '*Sprint carryover watch:* Reactivate may bleed (8-pt tickets) \u2014 Izzy posts status '
                'Friday, Bob aligns with Izzy tomorrow. Carlo off Fri + Mon (Canada holiday); Indeed Account '
                'Setup targets QA/release next sprint. JD Experiment (Tanner): dev done, waiting on Rami\'s '
                'updated prompt.'
            )
        }
    })

    blocks.append({'type': 'divider'})

    # Action items
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3af Your Action Items*\n\n'
                '*\U0001f6a8 TODAY (don\'t let these slip):*\n'
                '\u2022 Write up Franchise Job Posting ticket content \u2014 you just got off the Indeed call, '
                'do this now while it\'s fresh\n'
                '\u2022 Send follow-up email to Olivia/Maria/Lacey summarizing today\'s Scooters plan '
                '(Christofer on CC) \u2014 you committed to this in the meeting\n'
                '\u2022 *Send Fadi the Boost modal Figma designs* \u2190 overdue since Jul 27, he\'s waiting\n\n'
                '*\U0001f4c5 BY FRIDAY:*\n'
                '\u2022 Resolve Talent Pool open questions: confirm Databricks\u2192SMS column contract w/ Carlo '
                '+ confirm message storage approach (job request ID \u2192 message body in table)\n'
                '\u2022 Align Izzy + Tanner on role/salary reco API contract \u2014 do this while DS is '
                'still building, not after delivery (Jatin flagged this explicitly)\n\n'
                '*\U0001f4cb NEXT SPRINT PREP:*\n'
                '\u2022 Assign unique source names to all 300+ Scooters locations in Homebase feed\n'
                '\u2022 Reach out to Scooters customers to create individual Indeed accounts\n'
                '\u2022 Send Olivia CSV: business name | source name | Indeed account per franchise\n'
                '\u2022 Review Matan\'s comms doc \u2014 Sonia is still blocked building, this is urgent\n'
                '\u2022 Follow up on Juan Sanchez email issue (still open)'
            )
        }
    })

    blocks.append({'type': 'divider'})

    # Watch list
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4ca Watch List*\n\n'
                '\U0001f534 *422 Job Publishing Errors* \u2014 Day 20. Jatin on RCA. Check in today.\n'
                '\U0001f534 *Carlo Harness/OpenSpec* \u2014 16+ days overdue. Have that direct 1:1 conversation. '
                'This doesn\'t resolve itself.\n'
                '\U0001f7e1 *Bob+Jonathan Comms Agent Sync* \u2014 Was scheduled for 3pm today. No Granola notes '
                'found \u2014 confirm it happened and that ownership (data/DS vs. product eng) got resolved. '
                'If it didn\'t happen, reschedule immediately.\n'
                '\U0001f7e1 *Dana succession* \u2014 ~6 weeks left. Off Aug 7. Page Templates handoff must '
                'start NOW. No plan exists yet.\n'
                '\U0001f7e2 *Candidate Matching Thresholds* \u2014 Shipped Jul 28. Learning mode on. '
                'Stay patient.\n'
                '\U0001f7e2 *SBA* \u2014 Launched Monday. Watch unassigned grid data.\n'
                '\U0001f7e2 *FFH Candidate Preview (Fadi)* \u2014 Nearly done. Get him that Figma today!'
            )
        }
    })

    blocks.append({'type': 'divider'})

    # Closing
    blocks.append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Manan, you\'re on fire. The Scooters call was a genuine enterprise win \u2014 you walked out '
                'with a clear franchise architecture, a direct relationship with Indeed\'s team, and a single '
                'ticket that unlocks 300+ (soon 900+) locations. The Talent Pool Outreach you greenlit today '
                'is exactly the kind of low-effort, high-potential bet that moves Q3 metrics. '
                'And learning that Indeed has *no 30-day ATS timer* is a product unlock that will change '
                'how you think about Renew Jobs entirely.\n\n'
                'Tomorrow: nail the comms agent ownership question, get Fadi his Figma, and write that '
                'franchise ticket. You\'ve got this! \U0001f680\U0001f4aa'
            )
        }
    })

    return blocks

def preview(blocks):
    sys.stdout.buffer.write(b'=== PREVIEW: Daily Digest Jul 29, 2026 ===\n\n')
    for block in blocks:
        btype = block.get('type', '')
        if btype == 'header':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write(('### ' + text + '\n\n').encode('utf-8', errors='replace'))
        elif btype == 'section':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((text + '\n\n').encode('utf-8', errors='replace'))
        elif btype == 'divider':
            sys.stdout.buffer.write(b'---\n\n')

def send_message(blocks):
    payload = json.dumps({
        'channel': CHANNEL,
        'blocks': blocks,
        'text': 'Daily Digest - Jul 29, 2026'
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=payload,
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + token
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('ok'):
                print('Daily digest sent successfully to Manan!')
            else:
                print('Slack API error:', result.get('error'))
                print('Response:', json.dumps(result, indent=2))
    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code, e.reason)
        print(e.read().decode('utf-8'))
    except Exception as e:
        print('Error sending message:', str(e))

blocks = build_blocks()
if token:
    send_message(blocks)
else:
    preview(blocks)
    print('\n[No Slack token found - set SLACK_TOKEN, SLACK_BOT_TOKEN, or SLACK_API_TOKEN]')
    sys.exit(0)
