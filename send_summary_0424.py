#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari - Apr 24, 2026 (covering Apr 23 meetings)."""

import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
CHANNEL_ID = 'D06E4QMHCNN'

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Debrief - Thursday Apr 23",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Here's your end-of-day breakdown. Two big meetings today - your Hiring Leads Standup and the Hiring / HB Assistant cross-domain sync. You made some sharp calls. Let's recap everything so nothing falls through the cracks."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 1: Hiring Leads Standup (8:45 AM)*\nAttendees: Matan, Cindy, Ray, Nelson, Dana, Fadi"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 1: Do NOT launch Boost email Segment 1 yet*\n*Rationale:* Today's boosts are expensive and low-quality. Pushing OEMs toward paid boosts before Homebase Boost is ready will erode trust and risk churn. The ROI isn't there yet.\n*What IS OK now:* Segment 2 (free boost during trial) - go ahead, since we're already doing the work.\n*Action Items:*\n- Matan: get Homebase Boost rails/piping ready after TLWA V1 ships\n- Once Boost quality is solid: implement Segment 1 emails directing to Homebase Boost\n- Owner: *Manan* to keep an eye on sequencing and greenlight when ready"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 2: Linear cleanup plan locked*\n*Rationale:* Linear is cluttered with Jira leftovers, dead epics, and multiple disconnected lists. The team agreed the root issue is thinking in Jira-mode instead of Linear-mode (projects = committed, time-bounded work; triage = source of truth for ideas).\n*Plan:*\n- Fadi to post the Linear approach in #leads channel today\n- Dana + Manan: clean up triage TODAY (use AI + Linear MCP to surface gaps/dupes)\n- Tomorrow morning: Dana/Manan/Fadi/Ray regroup to review cleaned-up triage\n*Action Item:* Extend your 1:1 with Dana tomorrow to include Linear triage review"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 3: TLWA email overlap is a non-issue - green light*\n*Rationale:* What looked like an overlapping email was just Izzy's placeholder copy - not a real duplication.\n*Resolution:* Triggers go through Iterable (Rohit consumes Amplitude events). No extra engineering needed.\n*Action Items:*\n- Matan: align with Kayla on full email journey map (holding until post-TLWA bandwidth opens)\n- Manan: re-review TLWA brief for career page section (you left comments earlier - pass through it again now that Matan has updated it)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 4: Full email journey audit with Kayla is required before more email launches*\n*Rationale:* Cindy flagged - and you agreed - that without knowing all emails being sent across marketing, transactional, and lifecycle, there's real risk of noise. Homebase already sends a fuckload of noise. Every new trigger needs to be understood in context.\n*Action Item:* Matan + Kayla to map the full journey - this unblocks any future email work confidently"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Meeting 2: Hiring / HB Assistant Cross-Domain Sync (11:00 AM)*\nAttendees: Fadi, Jan, Chris Wallace, Cindy, Ray, Nzaanen, Dana"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 5: Homebase Assistant IS the right channel to route hiring opportunities (with conditions)*\n*Rationale:* Chris demoed shift callout -> hire recommendation flow. The natural, contextual discovery is exactly right. However, for first-time hiring users, there are real risks: they won't understand what they just posted, they'll think we're 'just another ATS', and they'll lose context navigating the product.\n*What you called out:*\n- Screener/deal breaker questions MUST be added (critical to hiring assistant value prop)\n- Syndication toggle OR inference from past behavior is needed before this ships\n- Boost follow-up within 72 hours if applicant volume is low = strong assistant use case\n*Action Item:* Document these three requirements as must-haves before the assistant hiring flow is production-ready"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 6: Full feature set must work without assistant open - AI is additive, not required*\n*Rationale:* AI resistance is real. Not everyone wants to talk to an AI. The product has to be fully functional in traditional workflow mode. The assistant enhances; it never gates.\n*Architecture implication:* This is now a stated principle for the hiring/assistant integration.\n*Action Item:* Make sure this is explicitly documented when you scope the hiring x HB Assistant work"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 7: No hard boundaries between Hiring Assistant and Homebase Assistant - it's one system*\n*Rationale:* Thinking about 'where does hiring assistant end and HB Assistant begin' is the wrong frame. From the user's POV, it's just Homebase - an operational partner that helps with whatever is top of mind. The assistant is a layer that all teams contribute tools to.\n*Analogy you nailed:* Amazon - you can arrive via search, via a friend's link, or via chat. It's all the same system, just different entry points.\n*Action Item:* Align Dana, Fadi, and Chris on this framing explicitly so the team stops siloing assistant thinking"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 8: Natural discovery > in-product marketing for converting users to hiring*\n*Rationale:* Cindy made the sharp point - traditional product marketing (banners -> link -> another page) requires the user to do the work of figuring out what you're trying to tell them. The assistant solves this by *revealing* the product through conversation. You drip value in; it feels natural, not marketing.\n*Business model implication:* This shifts the pressure toward usage-based pricing vs feature-access packages - a hard problem that needs a proper conversation with leadership.\n*Action Item:* Flag this to Ray / leadership as a strategic pricing conversation that needs to happen soon. The assistant is going to break your current package model."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 9: Candidate messaging stays separate for now, but 'blended chat' is on the roadmap*\n*Rationale:* You asked the right question - as candidate messaging (scheduling, interviews) currently lives in the hiring dashboard and team messaging is separate, the assistant creates a 3rd place. The team agreed to keep them decoupled for V1. The future state is an agent that handles routine candidate Q&A, escalates to the owner when uncertain, and lives in the same thread.\n*Key technical blocker:* Authorization model for multi-party chats (owner vs candidate permissions).\n*Action Item:* Schedule a follow-up sync with Jan/Chris/Dana in ~1 week to move this to concrete specs"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Overdue / Hot Items - Do Not Lose*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *TLWA brief to Ted* - 20+ DAYS OVERDUE. Send today.\n:fire: *Predicted roles final decision with Cindy* - still OPEN. Close this.\n:fire: *Linear triage cleanup* - you committed to this today with Dana.\n:warning: *Matan: Boost rails ready post-TLWA V1* - keep on radar\n:warning: *Matan + Kayla: Full email journey map* - unblocks all future email work\n:warning: *Manan: Re-review TLWA brief (career page section)* - check Matan's updates\n:warning: *Andrew's Indeed status endpoint* - due TODAY (Apr 23)\n:warning: *Tanner: 3LO frontend integration* - blocked on Andrew's API\n:warning: *JobGet 30-day paid test* - set budget, confirm with Peter Lee + Dan\n:warning: *Greenlight Manual Mode* - Cindy QA done, ball is in your court\n:warning: *Saja (Talroo)* - send CPA categories + configure campaign\n:warning: *Justin: re-run description batches 93-100 + Supabase RLS audit*\n:warning: *Nelson: metro_area + bucketed_role + matching_roles* - OVERDUE since Apr 8\n:warning: *Fadi: classifier taxonomy alignment + company vs location winner list*\n:warning: *Jatin: May 4th agent demo (Codex/Claude good-cop/bad-cop)*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Tomorrow's Priority Order (Apr 24)*\n1. Send the TLWA brief to Ted - seriously, this one's 20+ days late\n2. Close the predicted roles decision with Cindy\n3. Dana 1:1 - extend it to cover Linear triage cleanup\n4. Confirm Andrew's status endpoint is live\n5. Greenlight Manual Mode if nothing blocking you\n\nYou had a big day, Manan. The HB Assistant conversation was genuinely strategic - you asked exactly the right questions (messaging, first-time UX, business model). The team is aligned on the right architecture. Now go close those overdue items. You've got this."
        }
    }
]

def send_slack():
    payload = {
        'channel': CHANNEL_ID,
        'blocks': blocks,
        'text': 'Your Daily Debrief - Thursday Apr 23'
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=data,
        headers={
            'Authorization': 'Bearer ' + SLACK_TOKEN,
            'Content-Type': 'application/json; charset=utf-8'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            if body.get('ok'):
                print('Slack message sent successfully.')
            else:
                print('Slack API error:', body.get('error', 'unknown'))
                sys.exit(1)
    except urllib.error.URLError as e:
        print('Network error sending to Slack:', e)
        sys.exit(1)

def preview():
    sys.stdout.buffer.write(b'\n=== PREVIEW (no SLACK_TOKEN) ===\n')
    for block in blocks:
        if block.get('type') == 'section':
            txt = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((txt + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'header':
            txt = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write(('=== ' + txt + ' ===\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(b'---\n')
    sys.stdout.buffer.write(b'=== END PREVIEW ===\n')

if __name__ == '__main__':
    if not SLACK_TOKEN:
        print('SLACK_TOKEN not set - printing preview only.')
        preview()
    else:
        send_slack()
