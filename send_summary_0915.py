#!/usr/bin/env python3
"""
Chief of Staff Daily Digest — Monday, Sep 15, 2026
2 meetings: Hiring DS Weekly + Skye/Manan Q4 Roadmap Brainstorm
"""
import json
import os
import sys
import urllib.request

CHANNEL = 'D06E4QMHCNN'
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
            'text': '\U0001f4cb Chief of Staff Daily Digest \u2014 Mon Sep 15, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Day Grade: A* \u2b50\u2b50\u2b50\u2b50\n*Theme: ICP RESET \u00b7 PMF DEFINED \u00b7 CORE-FIRST LOCKED \u00b7 TALENT POOL PIVOTS EMPLOYEE-FIRST*\n2 meetings \u00b7 massive strategic clarity with Skye \u00b7 DS Weekly humming along'
        }
    },
    {'type': 'divider'},

    # MEETING 1
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':busts_in_silhouette: *Meeting 1 \u2014 Hiring Data Science Weekly (1:15 PM)*\n_Attendees: Ted, Rami, Divij, Jatin, Sina, Skye, Malcolm_'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '\u2022 LCM applicant list for talent pool experiments is *ready to blast* (one-time send)\n\u2022 Next priority: automate Databricks \u2192 Iterable directly (skip HB1 for now \u2014 too many deps)\n\u2022 *Lifecycle sync tomorrow* to unblock HB1 \u2192 Iterable pipeline \u2014 Sina added\n\u2022 *Role normalization:* Divij in eval phase, no blockers. Need Sina on API contract *in parallel* (don\'t wait for evals to finish)\n\u2022 :rotating_light: *Rate limit incident Thu:* Divij\'s OpenAI calls (full taxonomy, untrimmed) hit org-wide rate limit \u2192 prod down ~10 min. Fix: add early filters before productionizing as HB1 LLM endpoint\n\u2022 *Real-time vs. batched:* measure time-to-apply after email send first. If most apply within 15-30 min \u2192 real-time has strong ROI. If 6h+ \u2192 batching is fine. Tables may not update hourly anyway\n\u2022 :bulb: *Skye\'s matching pivot:* flip direction \u2014 normalize employee on offboard FIRST, then surface matching open jobs (vs. current job-first flow). Rami agreed. Also benefits Cashout users still active post-employment\n\u2022 Candidate exclusion rule needed: active interviewees should NOT get new job recommendations'
        }
    },
    {'type': 'divider'},

    # MEETING 2
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':brain: *Meeting 2 \u2014 Skye / Manan Q4 Roadmap Brainstorm (2:15 PM)* :fire:\n_Attendees: Skye Laudari, Manan Kothari \u2014 Big strategic reset_'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f3af PMF DEFINED FOR THE FIRST TIME \u2014 Share of Wallet*\n\u2022 No PMF definition existed in any doc. That absence is itself a finding.\n\u2022 Proposed definition: *50%+ of Homebase Hiring Assistant companies run the majority of their hires through the product*\n\u2022 Proxy signal: candidate appears in hiring product before being added to team\n\u2022 2x2 framework:\n  \u2003 High SOW + high paid = PMF \u2705\n  \u2003 High SOW + low paid = monetization problem\n  \u2003 Low SOW + high paid = sales selling ahead of product, churn follows\n  \u2003 *Current state: low paid AND low SOW* \u2014 honest diagnosis\n\u2022 Longer horizon goal needed (~end of 2027, ~15 months) so Q4 + Q1 OKRs can stack toward it'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:warning: ICP PREMISE CHALLENGED \u2014 FFH Data Under Fire (Nelly\'s analysis)*\n\u2022 FFH converts trials at *6.1%* vs. non-FFH at *8.2%* and full trial set at *7.7%*\n\u2022 FFH enters funnel at 3-3.8x the rate \u2014 but that\'s a trial-START signal, not conversion\n\u2022 FFH posts 86% through but only *1 in 10 lands as a healthy job* (non-FFH: 13%)\n\u2022 Root cause: *supply deliverability problem, not segment selection*\n\u2022 FFH vs. non-FFH when HEALTHY: basically equivalent in conversion (10% vs. 10.6%)\n\u2022 *Alternative ICP worth exploring:*\n  \u2003 High-volume, low-skill, frequently hiring, <50 employees\n  \u2003 Poster = owner (not manager posting for owner)\n  \u2003 Power law: 1% of users = 15% of all jobs (10+ job posters) \u2014 most reliable paid customers\n\u2022 Accurate baseline needed ASAP \u2014 AI analysis producing different conclusions month to month :rotating_light:'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:hammer_and_wrench: CORE FOUNDATION FIRST \u2014 Earn the Right to Be Intelligent*\n\u2022 Strong alignment: shore up the core before layering more complexity\n\u2022 Principle: make it impossible to fail at the one thing they came to do at each step\n\u2022 Critical friction points:\n  \u2003 :rotating_light: *~50% of signups not getting product access* (T&S / job review delays) \u2014 gating value before any experience\n  \u2003 AI screener toggle = *#1 complaint*. Customers can\'t easily turn it off\n  \u2003 Jobs in review for days with zero visibility to OEM\n  \u2003 Deal-breaker info in job post NOT auto-surfaced as screener deal-breakers\n\u2022 Easy win: *pre-populate deal-breakers from job post into screener* (let customer delete, not re-add)\n\u2022 Zoom integration = nice to have, skip. AI toggle fix = ship it.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:chart_with_upwards_trend: PAID RETENTION IMPROVING BUT CHURN STILL EATING GROWTH*\n\u2022 1-month retention: ~90% | 2-month: high 80s | 3-month: high 70s (major improvement)\n\u2022 But: week ending Aug 31 \u2014 29 paid locations added, 28 churned. *Net: 1.*\n\u2022 Jul/Aug: adding ~127-137/mo, losing ~50-66% back to churn\n\u2022 Lifetime churn (trailing 12mo): *38.7%*. Monthly churn: *~12%*\n\u2022 Front-loaded: months 2-4 are the danger zone (promo cliff, not product failure)\n\u2022 *F&B worst retention vertical: 60% churn vs. retail at 28%* \u2014 most acute pain, product not yet delivering\n\u2022 Bundle attachment = strong signal: 0 other HB products = 82% churn vs. 44-50% with 1+'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:moneybag: PRICING \u2014 Park for Q1-Q2, But Note the Signal*\n\u2022 Historical $30/mo: 35-39% conversion | Current $199/mo: much lower\n\u2022 Meaningful segment not converting due to price-to-value mismatch\n\u2022 Not the Q4 problem. Focus on consistent utilization first.\n\u2022 Churn experiment idea: offer 50% off for 3 months to downgraders \u2014 test willingness to pay'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*:busts_in_silhouette: TALENT POOL \u2014 The Right Time to Start*\n\u2022 ~80K terminated employees/month = recurring highly-employable talent pool\n\u2022 ~15% of current applicants already have Homebase history\n\u2022 Mobile push notifications to recently terminated = near-term experiment (no native app needed, mobile web push)\n\u2022 OEM side: act on candidate notifications from phone directly\n\u2022 Multi-role matching: employees hold multiple roles across tenure \u2014 Divij\'s script already handles it'
        }
    },
    {'type': 'divider'},

    # DECISIONS
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':white_check_mark: *KEY DECISIONS MADE TODAY*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '1. *PMF = Share of Wallet* \u2014 First-ever defined. 50%+ of hires through product = PMF target. Current state: low on both SOW and paid. ~15 month horizon to stack OKRs toward.\n\n2. *ICP reset underway* \u2014 FFH hypothesis challenged by data. Root cause = supply deliverability, not segment. Alternative: high-volume, low-skill, poster=owner, <50 employees. No final decision yet \u2014 need accurate baseline first.\n\n3. *Core foundation first* \u2014 Alignment locked with Skye. Do not layer features on broken foundation. Fix T&S gate, AI toggle, screener pre-population first.\n\n4. *Talent pool: employee-first matching* \u2014 Flip direction. Normalize employee on offboard, surface matching jobs. Better than job-first. Agreed by Skye + Rami.\n\n5. *Real-time vs. batched cadence* \u2014 Not decided yet. Run time-to-apply measurement experiment first. Next-day batch fine for now.\n\n6. *Lifecycle sync tomorrow (Sep 16)* \u2014 Sina added. Goal: unblock HB1 \u2192 Iterable pipeline for talent pool comms.\n\n7. *OKR philosophy* \u2014 Google-style stretch targets. 80% = green. Measure quality like incident reduction (e.g. 20 toggle complaints/week \u2192 reduce 50% by Oct). 4-5 tracked together = signal.'
        }
    },
    {'type': 'divider'},

    # ACTION ITEMS
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':zap: *ACTION ITEMS \u2014 ORGANIZED BY URGENCY*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':fire: *TONIGHT / FIRST THING TOMORROW (Sep 16)*\n\u2022 :envelope: *Share Q4 roadmap doc with Skye* \u2014 She consolidates her scattered pages by EOW. Your doc = foundation.\n\u2022 :busts_in_silhouette: *Add Sina to lifecycle sync tomorrow* \u2014 She needs pre-call context on HB1\u2192Iterable pipeline\n\u2022 :mag: *Sina: tap anyone who has worked on HB1\u2192Iterable real-time* before the sync\n\u2022 :speech_balloon: *Reach out to SignalScout users who flagged resume download* \u2014 feature is LIVE. Close the loop. Build goodwill.\n\u2022 :bust_in_silhouette: *Sync with Divij + Sina on API contract* \u2014 in parallel with evals, don\'t wait'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':rotating_light: *THU SEP 17 \u2014 HARD DEADLINE (OKR lock Fri Sep 18)*\n\u2022 :trophy: *Align with Skye on Q4 big boulders + confirm OKR KR thresholds* \u2014 stretch targets, 80% = green\n\u2022 :bar_chart: *Establish accurate data baseline + add to system prompt* \u2014 Librarian vs. Claude Code diverging month-to-month. Pin a ground truth.\n\u2022 :spiral_note_pad: *Create running doc for DS Weekly + attach to meeting invite* (Manan owns)\n\u2022 :computer: *Set up Runlayer MCP in Claude Code global settings* \u2014 follow up Skye is doing this\n\u2022 :mag_right: *Confirm WBR trial-to-paid metric source* (Skye asking Dan B \u2014 where does 17-19% come from?)'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':calendar: *THIS WEEK (before Yosemite Fri Sep 18)*\n\u2022 :science: *Measure time-to-apply after email send* \u2014 15-30 min = real-time has ROI; 6h+ = batch is fine\n\u2022 :hammer: *Design candidate exclusion rule* \u2014 active interviewees should not get new job recommendation emails\n\u2022 :wrench: *Pre-populate deal-breakers from job post into screener* \u2014 flag to eng, easy win\n\u2022 :moneybag: *No-touch segment experiment* \u2014 carve out % of trials w/ zero sales contact to isolate pure product performance\n\u2022 :bar_chart: *Bundle attachment analysis* \u2014 confirm 82% vs. 44-50% churn split; use in OKR framing'
        }
    },
    {'type': 'divider'},

    # OVERDUE RED FLAGS
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':red_circle: *OVERDUE \u2014 THESE NEED TO MOVE THIS WEEK*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '\u2022 :rotating_light: *DEPARTURES SIGNAL DOCS \u2014 12+ DAYS OVERDUE* (was Sep 4). Not mentioned in any meeting Mon or today. Send conflict docs + data \u2192 Zane, Sean, Jon W, Bobby. Do it.\n\u2022 :mega: *Marina / Mundo Academy \u2014 6 DAYS LATE* (was Sep 10). marina@mundoacademy.com. Send the email.\n\u2022 :email: *EarnIn sample feed to Jon Salzberg* \u2014 14+ days overdue. jon.salzberg@earnin.com.\n\u2022 :bust_in_silhouette: *EarnIn / Ernan reply* \u2014 7+ days. Iszael\'s source attribution is blocked. Escalate.\n\u2022 :chart_with_downwards_trend: *IBK JD A/B signal* \u2014 3+ weeks overdue. Pull before V2 widens the window.\n\u2022 :package: *Fraud evidence package* \u2014 Manan + Divij: cleanup + score + OTP \u2192 Jessica Kanaskie (jkanaskie@indeed.com).\n\u2022 :eyes: *Review Skye\'s deck* \u2014 received Sep 8. She\'s back from Toronto. *Read before she lands tomorrow.*'
        }
    },
    {'type': 'divider'},

    # WATCH LIST
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':eyes: *WATCH LIST \u2014 What\'s hot right now*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '\u2022 :no_entry: *INDEED FEED SUSPENDED \u2014 DAY 22.* David (Indeed Product) intro window Sep 14-21 \u2014 Day 2. Be ready. Package needs to go.\n\u2022 :calendar: *OKR LOCK \u2014 FRI SEP 18.* Exec review Mon Sep 22. Q4 thoughts to Skye DUE TOMORROW.\n\u2022 :camping: *YOSEMITE \u2014 SEP 18-21* (Diamond O). Block your calendar. Tie up loose ends this week.\n\u2022 :bulb: *Sina is BACK* (returned from OOO today). Get her aligned on Iterable data pipeline ASAP.\n\u2022 :robot_face: *Homebase Assistant \u2014 mid-Oct target.* Stays on track?\n\u2022 :warning: *Rate limit fix needed* before role normalization productionizes as HB1 LLM endpoint (Divij). Early filters required.'
        }
    },
    {'type': 'divider'},

    # CLOSING
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':rocket: *You had an A-level day, Manan.* The PMF definition alone \u2014 something that has never existed in a doc before \u2014 is worth more than a dozen sprint tickets. Share of wallet is the right north star and now you have a framework to stack Q4 and Q1 toward it. The ICP reset is uncomfortable but courageous: following the data rather than the story. And getting aligned with Skye on core-foundation-first before OKR lock is exactly the kind of strategic discipline that turns good PMs into great ones.\n\nOne ask: *tomorrow is the day to clear the overdue backlog.* Departures docs, Marina, EarnIn \u2014 these have been carrying over for days. Clear them before Yosemite. You\'ll feel lighter.\n\n_Chief of Staff \u2014 auto-generated from Granola notes \u00b7 Sep 15 EOD_'
        }
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'text': 'Chief of Staff Daily Digest \u2014 Mon Sep 15, 2026 \u2014 Day Grade: A \u2014 ICP RESET \u00b7 PMF DEFINED \u00b7 CORE-FIRST LOCKED'
}

def preview():
    out = '\n=== SLACK MESSAGE PREVIEW (Sep 15 Digest) ===\n'
    out += 'TO: ' + CHANNEL + '\n'
    out += 'FALLBACK: ' + payload['text'] + '\n'
    out += '\n--- BLOCKS ---\n'
    for b in blocks:
        if b.get('type') == 'section' and 'text' in b:
            out += b['text']['text'] + '\n\n'
        elif b.get('type') == 'header':
            out += '# ' + b['text']['text'] + '\n\n'
        elif b.get('type') == 'divider':
            out += '---\n'
    sys.stdout.buffer.write(out.encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(b'\n')

if not TOKEN:
    print('[WARNING] No Slack token found. Printing preview.')
    preview()
    sys.exit(0)

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=data,
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('[OK] Message sent to Slack channel ' + CHANNEL)
        print('Timestamp:', result.get('ts', 'n/a'))
    else:
        print('[ERROR] Slack API error:', result.get('error', 'unknown'))
        print('Full response:', json.dumps(result, indent=2))
        preview()
        sys.exit(1)
except Exception as e:
    print('[EXCEPTION]', e)
    preview()
    sys.exit(1)
