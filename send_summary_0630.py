#!/usr/bin/env python3
"""
Daily Decision Digest — Tuesday, June 30, 2026
Chief of Staff summary for Manan Kothari
Covers: Source Claiming meeting (12:00 PM PDT)
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'

# ── Slack payload ─────────────────────────────────────────────────────────────

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Digest — Tuesday, June 30 ✨",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Killer day — you shipped real clarity on the OEM source claiming motion that's been swirling for weeks. One focused meeting, seven crisp decisions. Here's everything you locked in, with the 'why' and your next moves. Let's go! 🚀"
        }
    },
    {
        "type": "divider"
    },
    # ── MEETINGS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 Today's Meetings (1)*\n• 12:00 PM — *Source Claiming* (w/ Matan, Sean + OEM team)"
        }
    },
    {
        "type": "divider"
    },
    # ── DECISIONS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🧠 Decisions Made Today (7)*"
        }
    },
    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. 3LO is OUT of the current source claiming test — keep it clean*\n_Why:_ 3LO adds real complexity and would confuse what you're validating. The current test is purely about the 'set up your account for success' positioning + source claiming flow. 3LO will be its own sprint once this validates.\n_Action:_ Nothing to do here — just hold the line if eng tries to scope-creep it back in."
        }
    },
    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Source claiming is priority #1 in OEM success calls — above calendar & job description*\n_Why:_ Without source claiming, jobs posted through Homebase have no Indeed account linkage. It's the foundational unlock. Calendar integration and JD optimization are valuable but secondary.\n_Action:_ Make sure Sean + OEM team know the call order: source claiming first, then everything else."
        }
    },
    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Call opening script locked: 'personal recruiter / success framing' — NOT 'do you have an indeed account?'*\n_Why:_ Opening with a transactional question kills warmth. The right opener is: 'I'm your personal recruiter at Homebase — my job is to make sure your account is set up for success. The first few days of a job's life are the most crucial...' — then pivot to source claiming naturally.\n_Action:_ 📌 Send Sean the finalized call script today. Confirm he's using this framing before the first outreach calls go out."
        }
    },
    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Three-bucket source claiming flow confirmed for Sean's playbook*\n_Why:_ Customer situations differ and the flow must branch correctly:\n• *Bucket 1 (Never posted anywhere):* Walk them through creating an Indeed account first (biz verification docs needed), then source claim — hardest path but fully mapped\n• *Bucket 2 (Posted on Indeed):* Call Indeed live, source claim immediately — cleanest path\n• *Bucket 3 (Other ATS):* Same as Bucket 2\n_Action:_ 📌 Matan to add XML feed URL + screenshots to the source claiming guide (simplifies finding source name for new reps)."
        }
    },
    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Test two call-order approaches in parallel — learn fast*\n_Why:_ There's a real tension: source claiming first is highest-priority but risks losing momentum if the customer doesn't have an Indeed account. Covering account setup overview first warms them up but risks drop-off before source claiming.\n_Action:_ 📌 Sean will test both and report back. You need to define what 'success' looks like for each — set up a simple tracking mechanism (e.g., Salesforce notes field flagging call type + completion rate)."
        }
    },
    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. 50/50 A/B test ('finish account setup' vs 'connect with Indeed' to-do) — DEFERRED to next sprint*\n_Why:_ Smart instinct to test positioning, but stacking it on top of the current experiment creates confusion and too many concurrent call types. Keep this sprint clean.\n_Action:_ Add to backlog for Sprint 2626. Make sure the hypothesis is documented before you forget it."
        }
    },
    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. In-product 'Finish Account Setup' to-do targets end-of-week for self-serve path*\n_Why:_ The outbound OEM call motion runs this week with no product changes needed. But the self-serve version (in-product to-do) needs to be live so that customers who don't pick up the phone can still trigger the setup flow.\n_Action:_ 📌 Confirm with Ugu that end-of-week ship date for the to-do is still holding. Flag any blockers NOW — don't let this slip to next week."
        }
    },
    {
        "type": "divider"
    },
    # ── CARRY-FORWARD ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔥 Carry-Forward Action Items (still on you from Jun 29)*\nThese were overdue yesterday — let's get them closed:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Send modal copy to Ted* — hiring onboarding designs modal is too long; Ted needs your revised copy to move forward\n• *Fix alignment on 'Complete Account Setup' to-do in Figma* — small fix, big polish signal before Cindy review\n• *Share Figma + spec doc access with Ugu* — he can't build what he can't see\n• *Add analytics events list to Ugu* — to-do interactions need tracking from day one\n• *Confirm Cindy alignment on designs* — don't let this linger into next week\n• *Did Matan get Ray's sign-off on SMS/email templates?* — those go out THIS WEEK, you need confirmation\n• *Did Matan share Calendly link + source claiming doc with Sean?* — Sean's calling tomorrow; he needs this\n• *Clarify Salesforce column requirements with Aventa* — blocking the OEM setup flow"
        }
    },
    {
        "type": "divider"
    },
    # ── LONGER OVERDUE ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚠️ Overdue / Strategic (don't let these become fires)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *v3 Q3 goals doc* — 3-bucket structure, needs to go to Ray before John. Every day this waits is a day of misalignment risk.\n• *Rami's talent pool email blast* — was due EOD Jun 25. Now 5 days overdue. Check status ASAP — if it hasn't gone, escalate.\n• *Comms agent ownership* — take it or leave with Dana/Fadi/Davi. Needs a decision before Dana leaves end of September.\n• *Usman call recordings* — listen for excitement signals to validate the pain-point-first cold-call approach is working.\n• *Calendly embed event detection with Ugu* — blocker for dev spec; needs resolution.\n• *SEO indexing guidance from Jenna* — Carlo's spike is running; Jenna's guidance unlocks the path forward."
        }
    },
    {
        "type": "divider"
    },
    # ── REFLECTION ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💡 Your Big Win Today*\nYou turned a murky, multi-week 'what should the OEM call look like?' debate into a clear, testable playbook — in one meeting. The source claiming guide is solid, the call framing is decided, Sean knows what to do, and you're learning fast with the two-approach test. This is exactly the kind of operational clarity that separates good PMs from great ones. 🏆"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Tomorrow's #1 Priority:* Get those June 29 carry-forwards off your plate (especially Matan's SMS/email template sign-off and Sean's doc share) before you get pulled into new meetings. Have a great Tuesday evening! 🌆"
        }
    }
]

payload = {
    'channel': CHANNEL,
    'blocks': blocks,
    'text': 'Your Daily Decision Digest — Tuesday, June 30, 2026'
}

# ── Send or preview ─────────────────────────────────────────────────────────

def send(token):
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
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print('✅ Digest sent successfully to Manan!')
                print(f'   ts={body.get("ts")}  channel={body.get("channel")}')
            else:
                print(f'❌ Slack API error: {body.get("error")}')
                print(json.dumps(body, indent=2))
    except urllib.error.URLError as e:
        print(f'❌ Network error: {e}')


def preview():
    sys.stdout.buffer.write(b'\n=== DIGEST PREVIEW (no token) ===\n')
    for block in blocks:
        t = block.get('type', '')
        if t == 'header':
            txt = block['text']['text']
            sys.stdout.buffer.write(f'\n### {txt}\n'.encode('utf-8', errors='replace'))
        elif t == 'section':
            txt = block['text']['text']
            sys.stdout.buffer.write(f'\n{txt}\n'.encode('utf-8', errors='replace'))
        elif t == 'divider':
            sys.stdout.buffer.write(b'\n' + b'-' * 60 + b'\n')
    sys.stdout.buffer.write(b'\n=== END PREVIEW ===\n')


token = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN')
)

if token:
    send(token)
else:
    preview()
    print('\n[INFO] No SLACK_TOKEN found. Add it in Cursor Dashboard → Cloud Agents → Secrets.')
    print('[INFO] The digest above is ready to send — just add the token.')
