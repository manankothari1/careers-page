#!/usr/bin/env python3
"""Chief of Staff Daily Digest — Tuesday, Jul 21, 2026"""
import json
import os
import sys
import urllib.request
import urllib.error

TOKEN = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN')
)

CHANNEL = 'D06E4QMHCNN'

intro = (
    'You crushed it today, Manan. :fire: 4 meetings, major experiment architecture locked, '
    'data platform officially unblocked, and the path to fixing D5 zero-applicant rate just '
    'got a whole lot clearer. Here\'s everything you decided today with full context and rationale.'
)

meetings_text = (
    '*:calendar: TODAY\'S MEETINGS (Jul 21, 2026)*\n'
    '1. *SB: Standup* 8:30am — Scheduling team: SBA bugs, John\'s feedback scoped\n'
    '2. *SBA Testing* 9:30am — Page review, tooltip logic locked\n'
    '3. *FFH Experiments w/ Manan* 11:58am — FFH experiment design with Carlo\n'
    '4. *Applicant Flow DS Weekly* 1:15pm — JD experiments, talent pool emails, DP process overhaul'
)

wins_text = (
    '*:trophy: BIG WINS TODAY*\n\n'
    ':star: *JD quality experiment fully designed and scoped* — Tanner has the assignment. '
    'Ratings are the #1 unlock (6K vs 300 avg for top vs bottom listings!). '
    'This could genuinely move the line cook needle.\n\n'
    ':star: *FFH demographic locked on Option 1* — the right call. '
    'Broad > narrow when definitions are still evolving.\n\n'
    ':star: *Data Platform process OVERHAULED* — this is HUGE. Named contact, sprint-scoped, '
    'embedded in your meetings. Role recs blocker is officially getting unstuck.\n\n'
    ':star: *Sponsorship is NOT the lever — ratings are.* '
    'High-rated non-sponsored listings beat sponsored low-rated ones. Saves budget, focuses on content quality.'
)

decisions_1_text = (
    '*:clipboard: DECISIONS MADE TODAY (7)*\n\n'
    '*1. JD Experiment: LOCKED* — 50/50 split, Tanner builds it\n'
    '• Ratings = #1 signal (top 10 avg 6K ratings vs ~300 for bottom 10)\n'
    '• Bold/paragraph formatting = #2 signal (Rami verifies manually before adding to prompt)\n'
    '• Logos = future work (needs Indeed employer graph API integration)\n'
    '_Why: Directional signal on what makes line cook JDs win on Indeed. '
    'Direct unlock for your Q3 line cook goal (<10% D5 zero-applicant rate)._\n\n'
    '*2. Sponsorship \u2260 the lever \u2014 Ratings are*\n'
    '• High-rated non-sponsored listings outrank low-rated sponsored ones\n'
    '_Why: Saves budget and refocuses effort on content quality over paid promotion._\n\n'
    '*3. Three Talent Pool Email Experiments: SCOPED*\n'
    '• P1: Activity recency (buckets: 0-1, 1-3, 3-6, 6-12, 12+ months; 2yr cutoff; unsubscribe from Iterable as secondary signal)\n'
    '• P2: Distance (recency fixed at 1mo; 5-mile increments up to 50mi)\n'
    '• P3: Recruiter email UI (keep recruiter copy, swap to branded template — open rate 55% vs 42% but click-through 1.54% vs 2.26%)\n'
    '_Why: You\'re flying blind on recency drop-off. This gets you the data to make email experiments stop being guesswork._'
)

decisions_2_text = (
    '*4. FFH Demographic: Option 1 LOCKED* — broad (food/drink/dining/hospitality + in trial)\n'
    '• No CSV-based enrollment; API activation trigger only (hitting a hiring page = enrollment event)\n'
    '_Why: FFH definition is still evolving. Build for flexibility now, filter data down later. '
    'Can\'t invent it retroactively._\n\n'
    '*5. No backfilling for FFH experiment*\n'
    '• Only enroll active users post-launch (hitting a hiring endpoint is sufficient "active" signal)\n'
    '_Why: Backfilling inactive users adds noise and cleanup debt with no signal benefit._\n\n'
    '*6. Carlo + Ugo = ONE experiment* (split demographics, not two separate experiments)\n'
    '• Users not in Ugo\'s account setup experiment fall into Indeed account setup experiment\n'
    '_Why: Analytics clarity. Two overlapping experiments = reporting nightmare downstream._\n\n'
    '*7. Data Platform process OVERHAULED*\n'
    '• Named DP contact assigned specifically to hiring team\n'
    '• Invited to team meetings when DP work is in scope\n'
    '• Their tasks scoped into sprint planning upfront (timelines visible before sprint starts)\n'
    '• Escalation path: Ted + Paul facilitate if pace is too slow\n'
    '• *Manan goes direct with Paul + Kanchana* — no more routing through Ted/Rami\n'
    '_Why: Role recs has been blocked by DP bottlenecks for too long. This fixes the structural problem._'
)

p0_text = (
    '*:zap: YOUR ACTION ITEMS*\n\n'
    ':red_circle: *P0 \u2014 Do Tonight:*\n'
    '• :mega: *Message Paul + Kanchana DIRECTLY* about role recs DP assignee — confirmed in DS Weekly today; you own this now\n'
    '• :rotating_light: *Carlo (OpenSpec/Harness): NOW 11+ DAYS OVERDUE* — has this been resolved? This is a management issue. Address it.\n'
    '• :pushpin: *Tatiana: send sitemap criteria + MSA table* — still pending from Jul 20\n'
    '• *Confirm Rami \u2192 Antoine \u2192 Izzy salary data handoff happened*\n'
    '• *Send Fadi brain dump* (from Jul 20 — confirm this is done!)\n\n'
    ':large_yellow_circle: *P1 \u2014 This Week:*\n'
    '• *Pair with Rami Thursday morning* — finalize recency, distance, and recruiter UI experiment scripts\n'
    '• *When Rami pings (prompt ready): loop in Tanner immediately* for JD 50/50 experiment kickoff — don\'t let this lag\n'
    '• *Ugo: confirm account setup timeline* (FFH flag bug + experiment overlap with Carlo\'s now resolved in architecture)\n'
    '• *Book Jatin + Kanchana + Paul sync* (from Jul 20 — confirm this happened)\n'
    '• *Schedule squad retro* (from Jul 20)\n'
    '• *422 job publishing errors: check Jatin\'s RCA* (146 locations, now day 12 — this is still critical)'
)

horizon_text = (
    ':large_blue_circle: *Longer Horizon:*\n'
    '• *Logos on JD pages* = needs Indeed employer graph API — flag to eng for sizing; don\'t let this get lost\n'
    '• *Matching algorithm*: Rami flagged it needs to move from notebook \u2192 prod infra — get it on the roadmap\n'
    '• *Role normalization script endpoint* for broader use — scope for a future sprint\n\n'
    ':warning: *Dana succession: ~9 weeks left. No plan. Biggest quiet risk.* '
    'Page Templates Aug 14 = CRITICAL handoff. Dana\'s off Aug 7. This must start NOW.'
)

watchlist_text = (
    '*:eyes: WATCHLIST*\n'
    '• *422 errors:* 146 locations, day 12. Jatin on RCA. Check for update today.\n'
    '• *Account setup release:* FFH flag bug, Ugo testing. Watch for EOW.\n'
    '• *Replica identity blocker:* Justin Lambert sign-off still needed.\n'
    '• *Salary recs:* Izzy + Tanner in sprint. Rami handoff status: confirm.\n'
    '• *Divij:* Re-pulling match data with real AND logic. Expect output this week.\n'
    '• *Abby:* Week 6. Ownership area still needs to be assigned. Don\'t let this slide.\n'
    '• *Dana:* Aug 7 vacation + Sep departure. Page Templates Aug 14 = CRITICAL handoff. Start NOW.'
)

closing_text = (
    'You\'re building something real here, Manan. :rocket: The JD experiment alone could be a '
    'massive unlock for line cooks \u2014 that 6K vs 300 rating delta is wild signal. '
    'And getting data platform embedded in your sprint process is exactly the kind of structural '
    'fix that pays dividends every single sprint from here on. Keep pushing. '
    'Go get \'em tonight. :muscle:'
)

blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': ':briefcase: Chief of Staff Daily Digest \u2014 Tuesday, Jul 21, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': intro}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': meetings_text}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': wins_text}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': decisions_1_text}
    },
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': decisions_2_text}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': p0_text}
    },
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': horizon_text}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': watchlist_text}
    },
    {'type': 'divider'},
    {
        'type': 'section',
        'text': {'type': 'mrkdwn', 'text': closing_text}
    }
]


def preview():
    output = '=== PREVIEW ===\n'
    for b in blocks:
        if b['type'] == 'header':
            output += f'\n[HEADER] {b["text"]["text"]}\n'
        elif b['type'] == 'section':
            output += f'\n{b["text"]["text"]}\n'
        elif b['type'] == 'divider':
            output += '\n' + '-' * 60 + '\n'
    sys.stdout.buffer.write(output.encode('utf-8', errors='replace'))


def send():
    payload = json.dumps({
        'channel': CHANNEL,
        'blocks': blocks,
        'text': 'Chief of Staff Daily Digest \u2014 Tuesday, Jul 21, 2026'
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=payload,
        headers={
            'Authorization': f'Bearer {TOKEN}',
            'Content-Type': 'application/json; charset=utf-8'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print(f'[OK] Slack message sent! ts={body.get("ts")}')
            else:
                print(f'[ERROR] Slack API error: {body.get("error")}')
                if body.get('needed'):
                    print(f'       Needed scope: {body.get("needed")}')
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f'[ERROR] HTTP {e.code}: {e.reason}')
        sys.exit(1)
    except Exception as e:
        print(f'[ERROR] Unexpected: {e}')
        sys.exit(1)


if TOKEN:
    send()
else:
    print('No Slack token found (SLACK_TOKEN / SLACK_BOT_TOKEN / SLACK_API_TOKEN). Running preview.')
    preview()
