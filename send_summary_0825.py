#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Monday, August 25, 2026
Sky's First Day as Head of Product
No Granola meetings captured today (likely onboarding/introductions all day)
Sending comprehensive Monday Sky Week 1 Battle Plan
"""

import os
import sys
import json
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'
TOKEN = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN') or
    ''
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Monday Digest - August 25, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Good evening, Manan.* No Granola meetings captured today — Sky's first day was almost certainly all onboarding, introductions, and culture immersion. That's fine and expected. But the watch list doesn't sleep, and tomorrow the real clock starts. Here's your full picture."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":rotating_light: *CRITICAL — 422 ERRORS (Day 46)*\n146 locations unable to publish jobs since July 9. This is the single most urgent thing on your plate. Jatin is on RCA. First order of business tomorrow morning — get a status update before standup. If it's not resolved this week, escalate. Customers are losing jobs silently."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":star2: *SKY IS IN THE BUILDING*\nThe new Head of Product started today. 15-20 years of experience, B2B marketplace background, sold a real estate company to Compass, and built a voice agent prototype for job posting. He gets it. Your job this week:\n\n• *Share the Talent Pool strategy doc* — bridge framing, locked. This is your north star narrative and the first thing he should internalize.\n• *Week 1 priorities to align on with Sky:* (1) 422 errors — he needs to know this is Day 46 and CRITICAL, (2) Fadi all-in on Talent Pool — 1-2 engineers, stop everything else, (3) Abby's ownership area — define it clearly before she's lost, (4) In-domain emails — earmarked for Sky's first week, put it on his agenda.\n• *Meet the New GM of Hiring* if they also started today — connect them to Sky ASAP."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":art: *FADI DESIGNS — STILL OVERDUE (9+ days)*\n• *Resume Insights designs:* Overdue since Aug 17. BLOCKING sprint delivery.\n• *Talent Pool designs:* Not in Linear. Izzy (front end) is blocked waiting.\n*Action:* Direct conversation with Fadi tomorrow. Not a Slack message — a conversation. What's the blocker? Do you need to reprioritize something off his plate?"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":handshake: *CARLO IS BACK*\nCarlo Ferrer was out the week of Aug 18. He should be back today. He leads *Talent Pool development* and *Indeed 3LO*. Loop him in first thing tomorrow — especially important with Sky starting and Talent Pool being the strategic centerpiece."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":bar_chart: *JD A/B EXPERIMENT — PULL SIGNAL*\nThe IBK JD prompt box A/B experiment has been running since the week of Aug 10. That's 2+ weeks of data. Pull the signal today or first thing tomorrow. You committed to this Monday. Don't let it slip."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":mega: *HIRING LEADS STANDUP — CONFIRM THESE TOMORROW*\n• Did #hiring-epdd channel get created? (Jatin committed to it Aug 20)\n• Q3 strategy doc comments — were they resolved by the Aug 21 deadline?\n• Two applicant flow experiments + JDO testing — did they launch week of Aug 18? (Rami committed, Divij owns now)\n• Sean's daily updates — confirm they're in summary+thread format (Jon Wanczyk owns)"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: *THIS WEEK'S CALENDAR*\n\n*Tuesday (tomorrow):*\n• Hiring Leads Standup 8:45am — bring the 422 status, Fadi design conversation, Sky intro agenda\n• Your PM/sales sync (Matan's Tuesday) — last one before consolidating to bi-weekly starting ~Sep 1\n• Chase Jobcase: Donnie Mannino (dmannino@jobcase.com) should have sent XML/API docs by now\n\n*Wednesday (Aug 27):*\n• *Mike Mohrhardt / Loco Boys Brewing call at 11am* (with Bobby Sladek)\n  — Bobby to reconnect with Mike before 2pm on screener trial results\n  — 4 applicants on bartender role as of last check (46 views, ~10% apply rate)\n  — Boost framing locked: <5-10 applicants in first couple days = push boost proactively\n  — Reminder: Homebase views dashboard = career page only (not Indeed/ZR) — great SEO story\n  — Email Mike to add a Careers tab to his website (Bobby to do, but follow up)\n\n*This Week:*\n• BarTaco: ~8 weeks left before Paylocity/Grayscale pilot ends. Rushi needs to get Scott Rodney intro from Lisa Mosby. Scott just got back from Chicago.\n• Tatiana (SEO): Scoping session STILL not scheduled. Zero content, huge gap. Chase her.\n• Amplitude dashboard to Matan: OVERDUE since Aug 6. Send it.\n• Gbolade: 15-min PM session still open. Schedule it."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":microscope: *CULINARY AGENTS DATA CHECK — OVERDUE*\nTest went live Aug 12 (27 line cook jobs at $69/job). That's Day 13 post go-live. Data signal is overdue. Chase Gray this week. You need this to inform whether to scale or pull back."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":briefcase: *JOBCASE — FOLLOW UP*\nPilot was greenlit Aug 18. Donnie Mannino committed to sending XML/API docs. If not received, chase today: dmannino@jobcase.com. Budget is $1,500-$2,000. This is your new distribution channel — independent of Indeed. Don't let it stall."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":trophy: *Q3 SCOREBOARD*\n• FFH D5 zero-app rate: *41%* (target: <10%) — *WAY off*\n• Line cook jobs healthy by D30: *~7%* (target: 50%) — *WAY off*\n• Screener completions: tracking, need update\n• OEM boost rate: 5.7% (up from 2.9% in May — progress)\n\n*Root cause locked:* Jobs not reaching Indeed due to 422 errors + platform constraints. OTQ email verification sprint coming. Talent Pool = medium-term answer. Culinary Agents = line cook wedge."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":pushpin: *YOUR TOP 5 TOMORROW MORNING (in order)*\n1. *422 errors* — get Jatin's RCA status before standup\n2. *Fadi* — direct conversation on Resume Insights + Talent Pool designs\n3. *Carlo* — loop him in on Talent Pool + Indeed 3LO priorities\n4. *Sky 1:1* — share Talent Pool doc, align on Week 1 agenda\n5. *JD A/B experiment* — pull signal from IBK"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":muscle: You've built a lot of momentum going into this week, Manan. Sky starting is the inflection point you've been waiting for. The 422 bug is the only thing that can derail it — keep pushing on that. Everything else is execution. You've got this."
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Digest | Monday Aug 25, 2026 | 0 Granola meetings captured today | Generated 5:00 PM PDT"
            }
        ]
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': json.dumps(blocks),
    'text': 'Monday Digest - August 25, 2026 | Sky Day 1 Battle Plan',
    'unfurl_links': False,
    'unfurl_media': False
}


def preview():
    out = []
    out.append('=== SLACK PREVIEW (Aug 25 Digest) ===')
    for b in blocks:
        btype = b.get('type', '')
        if btype == 'header':
            out.append('\n== ' + b['text']['text'] + ' ==')
        elif btype == 'section':
            t = b.get('text', {}).get('text', '')
            out.append(t)
        elif btype == 'divider':
            out.append('---')
        elif btype == 'context':
            for el in b.get('elements', []):
                out.append('[context] ' + el.get('text', ''))
    out.append('\n=== END PREVIEW ===')
    sys.stdout.buffer.write('\n'.join(out).encode('utf-8', errors='replace') + b'\n')


def send():
    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Authorization': 'Bearer ' + TOKEN,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('ok'):
                print('SUCCESS: Message sent to ' + CHANNEL)
            else:
                print('ERROR: Slack API returned error: ' + result.get('error', 'unknown'))
                sys.exit(1)
    except urllib.error.URLError as e:
        print('ERROR: Network error: ' + str(e))
        sys.exit(1)


import urllib.parse

if not TOKEN:
    print('No SLACK_TOKEN found - showing preview only')
    preview()
    sys.exit(0)

send()
