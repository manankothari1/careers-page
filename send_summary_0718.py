#!/usr/bin/env python3
"""
Weekly wrap digest for Manan Kothari - Saturday Jul 18, 2026.
No meetings today. Covers Jul 13-17 (5 days, 15 Manan meetings).
Sends to Slack DM channel D06E4QMHCNN.
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
            'text': '\U0001f4c5 Weekend Wrap | Week of Jul 13-17, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Happy Saturday, Manan! \U0001f31f No meetings today \u2014 perfect time to zoom out. Here\'s your full week-in-review across *15 meetings* and *~55+ decisions*. You had a genuinely excellent week: big architecture calls locked, a massive milestone hit, and your team is shipping. Let\'s make sure nothing falls through the cracks going into Monday. \U0001f4aa'
        }
    },
    {'type': 'divider'},
    # BIG WINS
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3c6 BIG WINS THIS WEEK*\n\n\u2022 *800K accounts milestone* \u2014 700K\u2192800K in just ~5 weeks (vs 14 weeks for the prior 100K). Organic trial growth + $30 plan removal = compounding \U0001f680\n\u2022 *Reactivation architecture locked* \u2014 copy job officially retired after months. One clean path forward.\n\u2022 *Salary recs unblocked* \u2014 Antoine approach approved, Izzy starting, production flow designed. Months of blocking = gone.\n\u2022 *North star metric defined* \u2014 \u2018move forward rate\u2019 is now your match quality north star. No more ambiguity.\n\u2022 *Sprint Show & Tell* \u2014 9,200 packwork violations resolved, Design Base extraction 11 days early, Gojo CLI live. Your team is shipping fast.\n\u2022 *LCM email automation* \u2014 5.8x enrollment lift, 4.8x advance lift, $379K advances at 10% conversion (vs 1.4% control). Someone built a money printer \U0001f4b0'
        }
    },
    {'type': 'divider'},
    # THEME 1: Reactivation
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f527 THEME 1: Job Reactivation \u2014 Architecture Finalized (Jul 17)*\n\n*What you decided:*\n\u2022 Copy job workflow officially *DEAD*. OEM hits Reactivate \u2192 edit flow \u2192 modify \u2192 post. Full stop.\n\u2022 *\u2018Reactivation group\u2019 concept locked*: every reactivation of the same job shares a stable ID sent to Indeed. Applicants aggregated via association table (invisible on frontend). Health reporting = per 30-day lifecycle only.\n\u2022 Stable ID scoped to *Indeed only* for now. Other boards TBD.\n\u2022 Scope: ~7 tasks, touches multiple tables/services. Bob + Tanner estimating.\n\n*Why it matters:* 41% of FFH jobs have zero D5 applicants \u2014 a huge chunk of this is the copy\u2192duplicate flag destroying source claiming. This fix is the foundation.\n\n*\u26a0\ufe0f Open question (BLOCKING):* Is applicant drop-off on cloned jobs *Indeed-specific or universal*? This determines whether stable ID needs to expand to other job boards. You need to answer this before architecture gets too far.'
        }
    },
    {'type': 'divider'},
    # THEME 2: Salary Recs
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4b0 THEME 2: Salary Recs \u2014 Finally Moving (Jul 15 + 17)*\n\n*What you decided:*\n\u2022 *Antoine approach approved*: query payroll \u2192 salary distribution JSONs for 26 roles \u2192 refresh monthly. No DP dependency.\n\u2022 Izzy starts now (using Nelson\u2019s 50K role table + regex). Rami adds her to Monday meeting.\n\u2022 Rami messages Antoine Monday for data-pull script.\n\u2022 *JD prompt overhaul*: standard section headers (Job Summary, Duties, Skills, Salary & Benefits, Company Description). Salary near top. Ship small first, no data platform work needed. Eval \u2192 talk to Deb \u2192 ship \u2192 measure.\n\u2022 Possible markdown\u2192HTML rendering bug spotted \u2014 Rami investigating.\n\n*Why it matters:* At-market salary \u2192 33.5% chance of 20+ apps. Above market \u2192 38-39%. Below market \u2192 26%. This is a direct lever on your Q3 line cook health metric.\n\n*Action:* Check Monday that Rami messaged Antoine AND added Izzy. Don\u2019t let this slip again.'
        }
    },
    {'type': 'divider'},
    # THEME 3: Match Quality
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3af THEME 3: Match Quality \u2014 North Star Locked (Jul 16)*\n\n*What you decided:*\n\u2022 North star metric = *\u2018move forward rate\u2019*: OEM sends booking link OR accepts candidate-requested interview. NOT raw interview attendance.\n\u2022 Two-metric funnel: % of matches moved to interview \u2192 % hired. Guardrail: % of non-matches moved forward (should decrease).\n\u2022 Roster addition as hiring proxy (top match added to team within X days = hired).\n\u2022 Divij\u2019s combined-score chart dropped \u2014 was simple averaging, not real AND-gate logic. Divij re-pulling with proper AND gating.\n\u2022 *Profile changes are prerequisite for matching work.* Primary question = match accuracy, not volume.\n\n*Why it matters:* You finally have a metric that reflects OEM intent, not just system activity. This anchors Q3 roadmap decisions and makes screener redesign deferrable.'
        }
    },
    {'type': 'divider'},
    # THEME 4: Source Claiming + Line Cook
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f373 THEME 4: Source Claiming + Line Cook Health (Jul 15)*\n\n*What you decided:*\n\u2022 Short-term fix: Scooters Coffee pattern (Jatin).\n\u2022 Scalable uniqueness approach: Jatin + Izzy working in parallel.\n\u2022 Wage optimization experiment design confirmed.\n\u2022 *Instawork = $100/completed interview* ($200-300 for niche). Potential unlock for line cook if we can route hirers there for hard-to-fill roles.\n\u2022 Culinary Agents feed *ready* \u2014 waiting on Ray pricing call.\n\n*Why it matters:* Line cook at 7% healthy (target: 50%). Source claiming is the single biggest lever. These fixes need to ship *this sprint*.'
        }
    },
    {'type': 'divider'},
    # THEME 5: Process / Org
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2699\ufe0f THEME 5: Process + Org Changes (Jul 13-17)*\n\n*What you decided:*\n\u2022 *Definition of Ready updated*: Fadi stops writing product briefs. Dana owns product brief inputs. Design and product brief are now separate inputs.\n\u2022 *Wednesday cadence*: Manan + Ray + Dana align on priorities (async or 15-min sync) \u2192 hand to Fadi before EPD leads meeting.\n\u2022 *Single prioritized product list* spanning applicant flow + core \u2192 handed to Fadi.\n\u2022 *EPD leads meeting* moved to Thursday afternoon (back-to-back with Dana).\n\u2022 Linear = source of truth confirmed company-wide.\n\u2022 Zero state page: John\u2019s directive = no product screenshots.\n\u2022 Landing page: prompt box concept locked (\u2018I hire a line cook\u2019 \u2192 chip \u2192 fills next field + Google Places neighborhood). Two CTAs reduced to one secondary.\n\u2022 New eng PR directive (staff+ review required). Ray escalating, believes team not in high-risk territory.'
        }
    },
    {'type': 'divider'},
    # THEME 6: Dana Handoff - URGENT
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f6a8 THEME 6: Dana Handoff \u2014 URGENT (Jul 17)*\n\n*What you learned:*\n\u2022 Dana is leaving *end of September* \u2014 ~10 weeks from now.\n\u2022 Ray told Dana: \u2018I don\u2019t want to be the leader anymore. You be the leader.\u2019\n\u2022 Dana is managing Usman + Matan at Ray\u2019s insistence (3+ hrs/week of her time).\n\u2022 Dana is off *August 7 week* \u2014 Page Templates rolling out August 14. Handoff must be clean.\n\u2022 *No succession plan exists.* Manan likely absorbs Dana\u2019s scope.\n\n*Why this is your biggest quiet risk:* Dana owns outbound/sales + significant eng coordination. 10 weeks with no handoff plan = chaos in October.\n\n*\u26a0\ufe0f You need to start a Dana transition plan this week.* Even 30 min to map her scope + identify what gets redistributed vs deprioritized will save you.'
        }
    },
    {'type': 'divider'},
    # MONDAY BATTLE PLAN
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f525 MONDAY BATTLE PLAN \u2014 Jul 21*\n\n*P0 (do before anything else):*\n\n1\ufe0f\u20e3 *Carlo Harness/OpenSpec* \u2014 8 DAYS OVERDUE (deadline was Jul 10). You need a status call or you need to escalate. This has been on the list every single day.\n2\ufe0f\u20e3 *Approve Ugu\u2019s backend PR* \u2014 This is blocking in-product OEM setup. Carried since Jul 15.\n3\ufe0f\u20e3 *Message Paul directly* on role rec DP progress. Not a Slack ping \u2014 a real conversation.\n4\ufe0f\u20e3 *V1\u2192V2 cutover check with Ugu* \u2014 Jul 20 was the target. That\u2019s *today (Sunday)*. What\u2019s the status? Did it happen? Any customer impact?\n5\ufe0f\u20e3 *Rami \u2192 Antoine + Izzy* \u2014 Confirm Rami sent the message and added Izzy to Monday\u2019s meeting. Don\u2019t assume.\n6\ufe0f\u20e3 *Answer the architecture question*: Is applicant drop-off on cloned jobs Indeed-specific or universal? Even a quick data pull from Divij or Tanner will unblock the stable ID scope decision.\n\n*P1 (this week, don\u2019t let slip):*\n\n\u2022 Share prioritized product list with Fadi (you + Jatin drafted; align with Dana first)\n\u2022 Book the Wednesday cadence invite (you + Ray + Dana)\n\u2022 Pull Indeed role-specific hiring guides for ~10 FFH roles\n\u2022 Review Bob + Tanner reactivation estimate (7 tasks \u2014 what\u2019s the sprint fit?)\n\u2022 *Start Dana transition plan* \u2014 even a rough scope doc. 10 weeks is shorter than it feels.\n\u2022 Check Instawork WTP: have you talked to 2-3 line cook hirers yet? This data point will unlock or kill the partnership.'
        }
    },
    {'type': 'divider'},
    # WATCH LIST
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f440 WATCH LIST*\n\n\u2022 *V1\u2192V2 cutover* \u2014 Target was Jul 20 (this weekend). Confirm with Ugu first thing Monday.\n\u2022 *Carlo Harness* \u2014 Now 8 days overdue. This becomes a management conversation this week.\n\u2022 *Salary recs* \u2014 Izzy starting, Rami handing off. Watch for blockers in first 48 hrs.\n\u2022 *Match quality* \u2014 Divij re-pulling data with real AND logic. Results will reframe your Q3 baseline.\n\u2022 *Dana succession* \u2014 ~10 weeks. Most important quiet risk in the org right now.\n\u2022 *Page Templates Aug 14* \u2014 Dana off Aug 7 week. Handoff must be designed now.\n\u2022 *Boost purchase bug* \u2014 Revenue-impacting, no owner. Who picks this up?\n\u2022 *SEO gap* \u2014 66K pages live, 15.5K indexed. Big opportunity sitting untouched. Carlo has Search Console data.\n\u2022 *Abby* \u2014 Week 4 starting. She needs a clear ownership area. What\u2019s her domain?'
        }
    },
    {'type': 'divider'},
    # CLOSER
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Manan \u2014 this was a genuinely great week.* \U0001f4af\n\nYou hit 800K accounts, locked two major architectural decisions that have been open for months (reactivation + match quality north star), unblocked salary recs, and shipped 15+ PRs as a team. The compound effect of all these Q3 decisions is real \u2014 the trajectory is right.\n\nGo enjoy the weekend. You\u2019ve earned it. Monday is ready for you. \u2600\ufe0f\U0001f37d\ufe0f'
        }
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'Weekly Wrap | Jul 13-17, 2026 \u2014 Your week-in-review is ready!',
    'blocks': blocks
}

def preview():
    sys.stdout.buffer.write(('\n' + '='*70 + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write('SLACK PREVIEW (channel: {})'.format(CHANNEL).encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(('\n' + '='*70 + '\n').encode('utf-8', errors='replace'))
    for block in blocks:
        if block.get('type') == 'header':
            txt = block['text']['text']
            sys.stdout.buffer.write(('\n### HEADER: ' + txt + '\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'section':
            txt = block['text']['text']
            sys.stdout.buffer.write(('\n' + txt[:2000] + '\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(('\n' + '-'*50 + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(('\n' + '='*70 + '\n').encode('utf-8', errors='replace'))

preview()

# Try to send via Slack API
token = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN') or
    ''
)

if not token:
    print('\n[INFO] No SLACK_TOKEN found. Preview complete. Add SLACK_BOT_TOKEN secret in Cursor Dashboard to enable live sending.')
    sys.exit(0)

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=data,
    headers={
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + token
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('\n[SUCCESS] Message sent to Slack channel {}!'.format(CHANNEL))
        print('Timestamp:', result.get('ts', 'n/a'))
    else:
        print('\n[ERROR] Slack API error:', result.get('error', 'unknown'))
        print('Full response:', json.dumps(result, indent=2))
        sys.exit(1)
except urllib.error.URLError as e:
    print('\n[ERROR] Network error sending to Slack:', str(e))
    sys.exit(1)
