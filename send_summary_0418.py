#!/usr/bin/env python3
"""Daily Decision Summary - Apr 18, 2026 (covering Apr 17 meetings)"""
import json, os, sys, urllib.request, urllib.error

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
CHANNEL = 'D06E4QMHCNN'

blocks = [
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': '\U0001f4cb Daily Decision Briefing \u2014 Friday Apr 18, 2026',
            'emoji': True
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Manan \u2014 one meeting logged today: *Ray / Manan* (Thu Apr 17 @ 5pm). Big moves on Talroo + a critical spend risk Ray flagged. Here\u2019s your full debrief. \U0001f447'
        }
    },
    {'type': 'divider'},

    # ── DECISION 1 ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2705 DECISION 1 \u2014 Switch Talroo from CPC \u2192 CPA bidding*\n\n*What was decided:* Move Talroo XML feed from flat CPC (e.g. $0.40/click) to CPA bidding at ~$2\u2013$3 per applicant. Talroo auto-adjusts bid volume to hit that target \u2014 more spend efficiency, real applicants vs. ghost clicks.\n\n*Why:* Current CPC model pays for clicks regardless of conversions. CPA aligns spend to actual outcomes. We already avg ~$2.01/lead via pixel tracking, so $2\u2013$3 is a realistic target.\n\n*Action items:*\n\u2022 \U0001f6a8 *Manan:* Confirm CPA target (start at $2 for entry-level, higher for managerial) and share final numbers with Ray before Monday\n\u2022 *Ray:* Update the Talroo XML feed \u2014 replace CPC node with CPA node and confirm with Saja before campaign switches live\n\u2022 *Saja (Talroo):* Activate CPA campaign on their end once feed is updated'
        }
    },
    {'type': 'divider'},

    # ── DECISION 2 ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2705 DECISION 2 \u2014 Add campaign segmentation to Talroo XML feed*\n\n*What was decided:* Add a campaign-type node to the XML feed to split entry-level vs. managerial roles into separate Talroo campaigns. Entry-level gets a lower CPA target ($2\u2013$3); managerial either gets a higher CPA or gets deprioritized for now.\n\n*Why:* Without segmentation, entry-level jobs eat the entire budget and managerial roles get zero distribution. Segmentation = controlled allocation.\n\n*Action items:*\n\u2022 *Ray:* Add campaign type node to XML feed (entry-level | managerial). This is a fast ticket for Charmin if Ray prefers to delegate\n\u2022 *Manan:* Decide CPA tier for managerial \u2014 push harder or deprioritize for Phase 1? Align with Nelson on job-type classification if needed\n\u2022 *Nelson:* Confirm job description quality thresholds (char/line minimums) so poor-quality jobs don\u2019t get pushed to Talroo at all'
        }
    },
    {'type': 'divider'},

    # ── DECISION 3 ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\u2705 DECISION 3 \u2014 Build incomplete applicant ingestion pipeline*\n\n*What was decided:* Build a daily job that identifies people who clicked through from Talroo but didn\u2019t complete their application, then hits the application endpoint with their info (name, email, phone, address) + job request ID to auto-ingest them as applicants.\n\n*Why:* Talroo already collects partial lead data via pixel tracking. These people raised their hand \u2014 they\u2019re warm leads. Ray estimates this could drive 30%+ increase in Talroo applicants. That\u2019s huge at current spend levels.\n\n*Action items:*\n\u2022 *Manan:* Create "Ray\u2019s Homework" Google doc with full spec for incomplete ingestion + Talroo CPA work \u2014 share in Slack DM today\n\u2022 *Ray:* Build daily job: query Talroo incomplete applicants \u2192 hit application endpoint with job request ID + location (Bob has endpoint structure from V2 job experiment)\n\u2022 *Manan:* Loop in Jatin \u2014 he was skeptical ("they didn\u2019t apply"). Massage the narrative: we have full PII, this is a warm lead, not spam\n\u2022 *Bob:* Share application endpoint structure with Ray (V2 job experiment reference)\n\n*Priority:* CPA + segmentation first \u2014 then incomplete ingestion. Ray out Friday, reconvening Monday.'
        }
    },
    {'type': 'divider'},

    # ── DECISION 4 (CRITICAL) ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f6a8 DECISION 4 \u2014 URGENT: Stop Talroo spend on Manual Mode customers*\n\n*What was decided:* There is NO confirmed control preventing Homebase from spending Talroo budget on jobs posted by Manual Mode customers (who pay $30/mo, not a full hiring subscription). You\u2019re spending up to $35/job on people paying less than you spend. This needs to stop immediately.\n\n*Why Ray flagged it:* "You\u2019re about to spend 50 bucks on people that pay us 30 bucks." As Manual Mode just launched, those jobs could be flowing into the Talroo feed right now with zero spend guard. This is a margin leak that compounds fast.\n\n*Action items:*\n\u2022 \U0001f525 *Manan (TODAY):* Audit the Talroo feed \u2014 confirm whether manual mode customer jobs are included. If yes, add an exclusion filter IMMEDIATELY\n\u2022 *Manan + Charmin:* Add subscription status check to Talroo feed logic: only push jobs from active hiring subscription customers (not manual mode, not free tier)\n\u2022 *Ray:* Once CPA work begins, verify the feed exclusion is in place before switching campaigns live\n\n*Note:* Existing paying hiring customers who\u2019ve been getting free Talroo applicants need a *gradual wean* \u2014 not a cold turkey cutoff. Losing the applicant flow abruptly = churn risk. Plan a transition messaging strategy.'
        }
    },
    {'type': 'divider'},

    # ── OPEN ITEMS ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*\U0001f4cc Open items carried from this week (top 10)*\n\n\u2022 \U0001f6a8 *TLWA brief to Ted* \u2014 NOW 15+ DAYS OVERDUE. Send today.\n\u2022 \U0001f6a8 *TLWA V1 migration decision* \u2014 was due EOD Apr 17. 50% of V1 users = award winners. Decide: exclude from mailer, optional migration, or build generic role plumbing?\n\u2022 *Predictive role timeline* \u2014 time-boxed to EOD Apr 17. What\u2019s the verdict?\n\u2022 *Jeff: desktop TLWA badge designs* \u2014 blocking engineers. Send ASAP.\n\u2022 *Cassy (printer):* confirm mailable address count before QR code print run (~3k flagged)\n\u2022 *Homebase Boost SKU kick-off w/ Chris McIntosh* \u2014 billing window closing\n\u2022 *Manual Mode green light* \u2014 Cindy QA done, on you. Greenlight it.\n\u2022 *Matan: post Boost Phase 1 vs Phase 2 rationale to #leads* \u2014 still pending\n\u2022 *Nelson: metro_area + bucketed_role + matching_roles columns* \u2014 overdue since Apr 8\n\u2022 *Justin: full Supabase RLS audit* \u2014 confirm handoff active'
        }
    },
    {'type': 'divider'},

    # ── CLOSER ──
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'You\u2019re crushing it, Manan. \U0001f4aa One clean 1:1 today \u2014 four real decisions locked, Ray is engaged and ready to execute. The Talroo CPA move is going to make the applicant economics materially better. The spend risk Ray flagged is worth a 15-minute audit tonight \u2014 don\u2019t let that compound into launch week. Go enjoy your Friday. See you Monday. \U0001f680'
        }
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'Daily Decision Briefing \u2014 Apr 18, 2026 (Ray/Manan recap + action items)',
    'blocks': blocks
}

def preview():
    sys.stdout.buffer.write(('\n=== PREVIEW (no SLACK_TOKEN) ===\n' + json.dumps(payload, indent=2, ensure_ascii=False) + '\n').encode('utf-8', errors='replace'))

def send():
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {SLACK_TOKEN}'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print('Message sent successfully!')
            else:
                print(f'Slack error: {body.get("error")}')
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f'Network error: {e}')
        sys.exit(1)

if SLACK_TOKEN:
    send()
else:
    preview()
