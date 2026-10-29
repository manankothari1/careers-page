#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Wednesday, October 28, 2026 (PDT)
Slack channel: D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_CHANNEL = 'D06E4QMHCNN'

def get_token():
    for key in ('SLACK_TOKEN', 'SLACK_BOT_TOKEN', 'SLACK_API_TOKEN'):
        val = os.environ.get(key, '')
        if val:
            return val
    return None

BLOCKS = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': '\U0001f4bc Wednesday Wrap-Up \u2014 Oct 28, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Hey Manan! \u2728 Solid Wednesday from Paris \u2014 you made some genuinely important '
                'strategic calls today that will reshape the next two sprints. Day grade: *A-*\n\n'
                '*Theme: SCHEDULING FIRST \u2022 MATCH CO-BUILD DESIGN \u2022 INTERVIEW CONFIRMATION SCOPED*'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4c5 Today\'s Meetings (4)*\n'
                    '`8:30am` Brooke R + Fadi \u2014 Brooke no-show, used time productively\n'
                    '`9:30am` Skye / Manan 1:1 \u2014 major roadmap + product decisions\n'
                    '`10:30am` Discovery: Hiring Leads \u2014 full EPD team\n'
                    '`2:00pm` EPD Leads Sync \u2014 pre-meeting banter only, no work content captured'
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f3af Big Decisions Today*\n\n'

                '*1. MATCH EXPLANATION \u2192 MATCH CO-BUILD (fundamental pivot)*\n'
                'You shifted from "explain the current match" to "co-define match criteria with OAMs upfront during job creation." '
                'Rationale: customers can\'t judge a well-explained match if they never told you what they wanted. '
                'Even a perfect explanation won\'t land if the underlying criteria are wrong. '
                'Fadi is aligned. Skye is aligned. Format TBD (free-text, pills, audio, or inferred defaults).\n\n'

                '*2. ROADMAP SWAP: Scheduling moves UP, Match Co-Build moves DOWN*\n'
                'Scheduling is "medicine" (customers are in pain, problem space is clear, Bob\'s research is done). '
                'Match co-build is a "vitamin" (important but not urgent). '
                'You now have a very narrow window to define scheduling ideal state before Malcolm\'s last day Friday. '
                'Skye is talking to Nihilus tomorrow (subscription renews Jan 3 \u2014 hard deadline). '
                'Bob + Jatin are rounding out the build-vs-buy spike.\n\n'

                '*3. INTERVIEW CONFIRMATION FLOW \u2014 DESIGNED*\n'
                'You designed the flow with Fadi (from Brooke no-show time) and hardened it with Skye:\n'
                '\u2022 24hrs before: "Reply YES to confirm, CANCEL to cancel"\n'
                '\u2022 4hrs before: follow-up if no reply; cancel if no response by 2hrs out\n'
                '\u2022 Freeform replies (e.g. "my kid is sick"): forward raw to OEM, they handle rescheduling\n'
                '\u2022 Respect working hours + role location timezone\n'
                '\u2022 Max 2 options per text; branch from there; no LLM needed\n'
                '\u2022 Skye recommended: write this up in *BDD format* (Given/When/Then) for engineering handoff\n\n'

                '*4. COMMS AGENT IS THE PLATFORM FOR INTERVIEW CONFIRMATION*\n'
                'Discovery alignment: extend comms agent to support toggle-able scenarios. '
                'Malcolm\'s screener nudge is built and ready to release. '
                'Interview confirmation = new spike for Jatin + Bob. '
                'Open arch question: can the system emit events from candidate replies to update OAM dashboard status? '
                '(Screener nudge only prompted action; interview confirmation needs to update status UI.)\n\n'

                '*5. HEALTHY JOB DEFINITION UPDATED*\n'
                'New definition: 10+ applicants AND 2+ OAM touchpoints (messages, confirmed/scheduled interviews).\n'
                'Old definition: 20+ applications + 5+ top matches.\n'
                'Rationale: OAM touchpoints are stronger conversion signals than raw application count.\n\n'

                '*6. WELCOME TECH \u2014 DECLINED FOR Q4*\n'
                'Agreed: product needs to work reliably before changing the commercial model (outcome-based pricing). '
                'Interesting for Q1. Manan to respond to Doreen (Welcome Tech EA) declining + suggest Q1 reconnect.\n\n'

                '*7. SPRINT HYGIENE TIGHTENED*\n'
                'Unfinished tickets go back through prioritization (no auto-carry). '
                'Sprint goal set each cycle. PM/design work tracked in Linear. '
                'Jatin + Matan pushing engineers to keep statuses current. '
                'First formal close: *Friday Oct 30 \u2014 2 days away.*'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u2705 Your Action Items (Today + Outstanding)*\n\n'
                '\U0001f525 *CRITICAL \u2014 Do Today/Tomorrow:*\n'
                '\u2022 *Define ideal scheduling product behavior* \u2014 Malcolm\'s last day is FRIDAY. You have 2 days. Write the product POV and answer Bob\'s open questions doc. This is your tightest window.\n'
                '\u2022 *JD rules for Divij* \u2014 DAY 5 OVERDUE. He is idle and blocking. Write the 4 rules: 1 hire ~30d = vanilla; 2+ hires = \'multiple positions available\'; urgency <=2wk = \'urgently hiring\'; TBD on ASAP definition + posted vs activated date.\n'
                '\u2022 *Write interview confirmation flow in BDD format* \u2014 Given/When/Then. Cover: timezones, working hours, freeform reply forwarding, all cancel paths.\n'
                '\u2022 *2029 Vision One-Pager* \u2014 CRITICAL. Fadi submitted his. John presented the vision Oct 26. You have not. Board meeting opened Oct 15. Write it.\n\n'

                '\U0001f4cb *Action Items from Today:*\n'
                '\u2022 Sync with Fadi tomorrow 10:30am-noon: match co-building direction + brainstorm\n'
                '\u2022 Respond to Doreen (Welcome Tech EA): decline Q4, suggest Q1 reconnect\n'
                '\u2022 Send Tallroo dates for November meeting (include Skye)\n'
                '\u2022 Confirm whether OEMs receive SMS when candidate sends freeform reply (determines notification routing)\n'
                '\u2022 Look up mean number of matches per job (Jatin asked in discovery)\n'
                '\u2022 Tag Fatty for Verify CTA designs on Magic Link success screen (been pending)\n\n'

                '\u23f0 *Still Outstanding from Prior Days:*\n'
                '\u2022 Jatin to push identity EM re: Mary Turpin replacement (Magic Link blocker)\n'
                '\u2022 Confirm Spec Swarm outcome \u2014 did it happen Oct 27? N+1 verdicts?\n'
                '\u2022 Indeed support reply re: company field bug (OUTSTANDING 7 DAYS now)\n'
                '\u2022 Indeed FSA review \u2014 Jessica was expected to respond EOD Oct 27. Did she?\n'
                '\u2022 Omni access \u2014 ping IT\n'
                '\u2022 Matt McAllister intro \u2014 new CMO, week 2+. Get 30 mins.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\u26a0\ufe0f Watch List \u2014 Burning Items*\n\n'
                '\U0001f525 *NIHILUS SUBSCRIPTION \u2014 5 DAYS (Nov 3).* '
                'Skye talking to Nihilus tomorrow. Izzy to scope build cost. Decision before renewal.\n\n'
                '\U0001f525 *MALCOLM OUT FRIDAY.* Last rubber duck session on scheduling: today + tomorrow only. '
                'Don\'t let this window close without extracting the architectural knowledge.\n\n'
                '\U0001f534 *FACEBOOK API \u2014 ALL CALLS FAILING. Day 35.* Bob + IBK. No update since Oct 9. Escalate.\n\n'
                '\U0001f534 *ENTITLEMENTS ROLLOUT* \u2014 5% target was Oct 28. Did Adam confirm?\n\n'
                '\U0001f534 *COMMS AGENT TONE* \u2014 flagged as overly formal in discovery. Fadi wants prompt tuning. Divij to be looped in.\n\n'
                '\U0001f7e1 *MAGIC LINK IDENTITY BLOCKER* \u2014 Mary Turpin on vacation, no replacement assigned. Jatin action needed.\n\n'
                '\U0001f7e1 *MATAN\'s 3 PROJECTS* \u2014 to be reviewed Thursday: (1) intent signals propensity model, (2) product wizard/onboarding, (3) pricing/packaging. Be ready.\n\n'
                '\U0001f7e1 *STANDUP ATTENDANCE* \u2014 Jatin, Jon, Fadi absent Oct 27. You and Matan flagged it. Needs a team conversation.'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                '*\U0001f4a1 Your Chief of Staff\'s Take*\n\n'
                'You had a really productive day intellectually, Manan. '
                'The pivot on match from "explain" to "co-build" is the right call \u2014 it\'s the kind of upstream insight that prevents a ton of rework downstream. '
                'The roadmap swap (scheduling up, match down) is also correct: you can\'t vitamin your way out of a medicine problem.\n\n'
                'But here\'s the thing: *the decisions are made, now the execution is everything.* '
                'You have two critical time-boxed windows closing fast \u2014 Malcolm on Friday and Nihilus on Nov 3. '
                'These aren\'t calendar items, they\'re burning fuses.\n\n'
                'The JD rules for Divij is Day 5. That\'s too long. 15 minutes tonight, you ship it.\n\n'
                '*Tomorrow\'s top 3:*\n'
                '1\ufe0f\u20e3 Write scheduling ideal state doc (Malcolm rubber duck ASAP)\n'
                '2\ufe0f\u20e3 Ship JD rules to Divij (tonight preferred)\n'
                '3\ufe0f\u20e3 Fadi brainstorm 10:30am \u2014 match co-build direction locked\n\n'
                'You\'re crushing it. Now close the loop on what\'s bleeding. \U0001f4aa'
            )
        }
    },
    {'type': 'divider'},
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': '\U0001f916 Chief of Staff Digest \u2022 Wed Oct 28, 2026 \u2022 4 meetings reviewed \u2022 Auto-generated at 5pm PDT'
            }
        ]
    }
]

def send_slack(token):
    payload = json.dumps({
        'channel': SLACK_CHANNEL,
        'blocks': BLOCKS,
        'text': 'Wednesday Wrap-Up \u2014 Oct 28, 2026 | Chief of Staff Digest'
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=payload,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            return result
    except urllib.error.URLError as e:
        return {'ok': False, 'error': str(e)}

def preview():
    sys.stdout.buffer.write('\n=== CHIEF OF STAFF DIGEST PREVIEW (no Slack token) ===\n'.encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(f'Channel: {SLACK_CHANNEL}\n'.encode('utf-8', errors='replace'))
    sys.stdout.buffer.write('--- BLOCKS ---\n'.encode('utf-8', errors='replace'))
    for block in BLOCKS:
        if block.get('type') == 'section':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((text + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'header':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((f'### {text} ###\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'context':
            for el in block.get('elements', []):
                sys.stdout.buffer.write((el.get('text', '') + '\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(b'---\n')
    sys.stdout.buffer.write(b'\n=== END PREVIEW ===\n')

if __name__ == '__main__':
    token = get_token()
    if not token:
        preview()
        print('NOTE: No Slack token found. Add SLACK_TOKEN or SLACK_BOT_TOKEN in Cursor Dashboard > Cloud Agents > Secrets.')
        sys.exit(0)
    result = send_slack(token)
    if result.get('ok'):
        print(f'SUCCESS: Message sent to {SLACK_CHANNEL}')
        ts = result.get('ts', '')
        if ts:
            print(f'Message timestamp: {ts}')
    else:
        print(f'ERROR: {result.get("error", "unknown")}')
        sys.exit(1)
