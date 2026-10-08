#!/usr/bin/env python3
"""
Daily Chief-of-Staff Digest — Wednesday Oct 7, 2026
Sends Slack Block Kit message to D06E4QMHCNN
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = 'D06E4QMHCNN'

# ─── BUILD THE PAYLOAD ────────────────────────────────────────────────────────

blocks = [
    # Header
    {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': 'Your Wednesday Digest — Oct 7 :brain: Chief of Staff'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*Day Grade: A-* | 3 meetings | ~4.5 hours\n:sparkles: *THEME: Q4 SOLUTIONING COMPLETE \xb7 MAGIC LINK UNLOCKS OTP \xb7 INTENT SIGNALS DESIGN APPROVED \xb7 HIRE SMARTER IS THE NEW EXTERNAL STORY*'
        }
    },
    {'type': 'divider'},

    # Meeting 1
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':one: *Fadi / Manan \u2014 Q4 Solutioning* \u2502 9am EDT \u2502 Fadi Rizk, Manan'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*What happened:* Two hours, ~50 problem items, every one tagged for design effort vs. engineering-only, and solutions drafted inline. Manan and Fadi are operating at peak velocity together.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':white_check_mark: *Key Decisions Made:*\n\n\u2022 *OTP \u2192 Magic Link:* ~65% send success rate because 96% of OEMs lack MFA. Decision: replace OTP code with server-side magic link. Fadi cranks 80% prototype before Lookahead; IBK implements next sprint. Three design states: (1) "Check your email" modal, (2) "Verifying \u2192 close tab" page, (3) "Verified" confirmation on return.\n\n\u2022 *Intent Signals / Overtime Modal:* Show trailing 12-month OT pay (not projected extrapolation). $10K threshold = 25% of payroll customers. Copy: "A new hire *can save up to* [X]" + disclaimer. Matan\u2019s smart flag: threshold should be % of total payroll spend, not raw dollar, to normalize for business size \u2014 Manan to follow up with Matan on recalculating.\n\n\u2022 *Prompt Chips \u2014 Minimum Wage Fix:* Remove tips from prompt chips entirely. Use Ultraviolet repo for state/city minimum wage. Manan to write MD file for the team; ping Justin to complete remaining 30% coverage. Front-end wage validation (blocking below-min-wage posting) \u2192 next sprint after prompt chips.\n\n\u2022 *Move Forward Label:* Fadi can ship next week. Change CTA label to match candidate state: pre-interview \u2192 "Schedule Interview," post-interview \u2192 action-oriented label.\n\n\u2022 *Messaging / Applicant Tab:* Remove standalone Applicant tab. Move all candidate comms history into candidate side panel (screener link sent \u2192 interview booked, full sequence visible).\n\n\u2022 *Background Check Bugs \u2014 3 documented:*\n   1. BGC credits don\u2019t auto-reset monthly (despite product promise)\n   2. MitraTech requires legal business name \u2014 update company profile fields\n   3. If candidate skips BGC, OEM gets no refund + payment stuck in limbo\n   + Fadi idea: pre-approve companies at syndication time to remove pre-approval friction\n\n\u2022 *Scheduling:* Window = 5am\u20139pm, no past times selectable, default to available times only, sync 15/30/45-minute slots\n\n\u2022 *Mobile Signup:* Hiring intent not captured \u2014 Manan owns, talk to Cindy (growth PM)\n\n\u2022 *JD Quality Score:* Consider real-time scoring via Orca/JEV for instant quality feedback\n\n\u2022 *Stack Rank:* Too many Very High items. Manan + Skye to stack rank, then Manan + Fadi go deep on match profile designs\n\n\u2022 *46 Old Experiments:* Jatin surfaced 46 disabled hiring-domain experiments. Manan + Fadi to quick-review: keep vs. remove'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':dart: *Your Action Items from this meeting:*\n1. *TODAY:* Write MD file from Ultraviolet repo (already have access) + ping Justin to complete 30% coverage\n2. *ASAP:* Follow up with Matan on OT threshold as % of payroll\n3. *This week:* Schedule Manan + Skye stack rank session (calendar creeping approved)\n4. *Next sprint:* Confirm IBK is scoped for OTP Magic Link implementation\n5. *Side of desk:* Review 46 old experiments with Fadi \u2014 quick keep/remove sweep\n6. *Ongoing:* Decide whether real-time JD score is engineering spike or just Orca task'
        }
    },
    {'type': 'divider'},

    # Meeting 2
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':two: *Hiring Lookahead* \u2502 2:15pm EDT \u2502 Full Eng Team (Jatin, Tiger, Izzy, Fadi, IBK, Soheil, Usman, Michael, Bob, Jon W, Skye, Matan)'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*What happened:* Sprint review + next sprint planning. Team is heads-down and well-coordinated. Carlo is out starting next week until mid-Feb \u2014 capacity dip, but Soheil is back.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':white_check_mark: *Key Decisions & Sprint Outcomes:*\n\n\u2022 *Carryover to next sprint:* Close Job Prompt, Close Job Flow, Close Job Survey (not started); Disposition Sync implementation (Tiger to create new project)\n\n\u2022 *Shipping this sprint:* Job Creation Flow logic (Tiger) + Universe Reopen (Tiger, PRs up); Culinary Agents (Izzy, done)\n\n\u2022 *EarnIn moved to Next:* Too much back-and-forth. Deprioritized.\n\n\u2022 *Jobcase:* Waiting on their team for credentials. Izzy confirmed sent.\n\n\u2022 *OTP Magic Link designs approved:* Mobile device concern addressed \u2014 separate success page is correct (same pattern as Claude MCP re-auth). Polling strategy: every few seconds + instant check on tab return. OEM *must* see the "verified" state.\n\n\u2022 *Intent Signals design feedback:* Matan flagged "on track" language + ambient glow read as *positive/celebratory*, not urgent. Fadi pushing back on red alerts (cross-sell, not alarm). Copy direction: make the pain legible without screaming. Industry benchmark comparison idea from Matan (flight pricing style: low/avg/high) \u2014 Fadi to explore.\n\n\u2022 *Prompt Chips:* 1/3 of OEMs use prompt chips. Fadi checking data model for tipped/non-tipped storage (likely not stored). Skye: ensure Ultraviolet data is available throughout the full job creation flow, not just chips.\n\n\u2022 *Q4 Technical Spikes confirmed (next sprint):* (1) Scheduling constraints / Nihilus limitations, (2) Screener toggle decoupling impact, (3) Matching algo downstream effects of screener off\n\n\u2022 *46 experiments:* Jatin surfacing \u2014 rolling through Orca side-of-desk\n\n\u2022 *INDEED \u2014 NEW NEGATIVE EMAIL:* Another one landed in hiring leads. Skye believes it\u2019s automated AND related to the reposting logic work. This raises urgency on reposting logic fix. :rotating_light: *JESSICA PING IS CRITICALLY OVERDUE. DAY 46.*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':dart: *Your Action Items from this meeting:*\n1. *CRITICALLY OVERDUE \u2014 DO FIRST THING:* Ping Jessica Kanaskie at Indeed (jkanaskie@indeed.com). Day 46. New email in hiring leads. Don\u2019t let another day go by.\n2. Review Tiger\u2019s disposition sync spike \u2014 confirm new project created\n3. Check if tipped/non-tipped is stored in job data model (follow up with Fadi)\n4. Confirm Ultraviolet data availability for full job creation flow (Skye concern)'
        }
    },
    {'type': 'divider'},

    # Meeting 3
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':three: *Product / Marketing / Sales* \u2502 3:45pm EDT \u2502 Matan Chen Zion (PMM), Jon Wanczyk, Bobby Sladek, Sean Gohman, Zane Williams, Skye'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*What happened:* Sales enablement session initiated by Matan (PMM). High-signal conversation about what\u2019s actually working with customers, what isn\u2019t, and where the real moat is. This is the beginning of a sharper go-to-market story.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':white_check_mark: *Key Decisions Made:*\n\n\u2022 *"Hire Smarter, Not Hire Faster" is the new value prop direction.* Matan\u2019s data: median time to hire is 7 days \u2014 same as competitors. Time savings is NOT the moat. New H1 direction: "Fewer tools, smarter hiring." The moat is match quality + certainty + one-stop-shop peace of mind for existing Homebase users.\n\n\u2022 *ROI Calculator: Not building it.* Jon and Bobby want it; Matan pushed back smartly \u2014 if the numbers aren\u2019t accurate, it creates a worse objection. Instead: sales to experiment with "hire smarter" messaging in actual calls.\n\n\u2022 *Sales \u2215 PMM feedback loop:* Use the PMM Slack channel for ongoing objection sharing. Matan sends customer interview digest regularly (sharing candidates with franchisee friend = organic growth signal).\n\n\u2022 *Research underway:* Matan launching study on *healthy F&B trial customers who did NOT convert*. This directly addresses the "why are we losing despite a good product experience?" question that sales keeps raising.\n\n\u2022 *Sales experiment design:* Matan to schedule call; *Jon to draft 3\u20135 specific questions* the full sales team asks every call to validate "hire smarter" hypothesis and rapidly learn what actually lands.\n\n\u2022 *Manan\u2019s call-out:* OEM hiring frequency data (roster additions per year) should inform sales approach. Low-frequency hirers ($99/month doesn\u2019t make sense for them) vs. high-frequency hirers (real ROI story). Jon\u2019s existing instinct to frame it as "less than a cup of coffee" is the right energy but needs the data to back it.\n\n\u2022 *Pricing model question surfaced:* Activation-based vs. subscription. More conversions with activation-based, less ARPU, but potentially net positive. This is a longer-term experiment \u2014 Matan flagged it; no decision yet.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':dart: *Your Action Items from this meeting:*\n1. Align with Matan on "hire smarter" experiment design \u2014 join or support the call he\u2019s scheduling\n2. Make sure Jon\u2019s 3\u20135 question draft gets routed to you for review\n3. Pull OEM roster-addition data (Divij / Omni) to segment high-frequency vs. low-frequency hirers \u2014 this is ammunition for sales and pricing strategy\n4. Flag the activation-based pricing idea to Skye as a Q1 experiment to evaluate'
        }
    },
    {'type': 'divider'},

    # Watch List
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':rotating_light: *OVERDUE / WATCH LIST \u2014 Top 10 (Don\u2019t Let These Slip)*'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '1. :fire: *INDEED FEED \u2014 DAY 46.* New negative email today. Ping Jessica NOW.\n2. :fire: *FACEBOOK API \u2014 DAY 15.* Bob + IBK. No update today. Need status check.\n3. :fire: *3-YEAR VISION ONE-PAGER \u2014 OVERDUE.* Board meeting ~Oct 15\u201322. Draft due NOW.\n4. :warning: *RACHEL Q4/Q1/Q2 UX VIEW \u2014 Was due today Wed Oct 7.* Did this go out? Confirm.\n5. :warning: *T-SHIRT SIZING EOW (Oct 9\u201310).* Jatin scheduling. Need stack rank with Skye first.\n6. :warning: *NYLAS SPIKE.* Jatin to schedule 30-min feasibility with Soheil. Status unknown.\n7. :warning: *MATAN + MANAN 1:1.* Was Thursday Oct 8 (today!). Is it still on?\n8. :warning: *CARLO KT.* Paternity starts next week. Schedule async KT TODAY.\n9. :warning: *ITERABLE 6 EMAILS NOT FIRING.* Carlo fixing. Should be done EOW (Oct 10). Verify.\n10. :warning: *OMNI ACCESS \u2014 PAST DUE.* Looker went dark Oct 2. Verify IT ticket filed.'
        }
    },
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':moneybag: *Gift Cards Still Owed:* Lola E. Erickson, Michele Landry, Ryan Reilly ($50 each)\n:busts_in_silhouette: *Intros Still Pending:* Jon Salzberg (EarnBetter), Matt McAllister (new CMO, Day 12)\n:envelope: *Emails Still Unsent:* John Waldman (EarnBetter NDA + docs), Marina/Mundo Academy (24+ days late)'
        }
    },
    {'type': 'divider'},

    # Closing
    {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': ':trophy: *Bottom Line:* Today was one of your best execution days in recent memory. You and Fadi cleared ~50 problem items in 2 hours and shipped clarity on some of the thorniest Q4 questions. The "hire smarter" pivot is going to sharpen your GTM story meaningfully. The only shadow hanging over the week is Indeed \u2014 send that ping to Jessica before you go to bed tonight. Everything else is momentum.\n\n_You\u2019re crushing it from Spain. Espresso \u20ac2. Decisions = priceless._ :coffee:'
        }
    },
    {
        'type': 'context',
        'elements': [
            {
                'type': 'mrkdwn',
                'text': 'Chief of Staff digest \u2022 Oct 7, 2026 \u2022 3 meetings \u2022 Generated at midnight UTC'
            }
        ]
    }
]

payload = {
    'channel': CHANNEL,
    'text': 'Your Wednesday Oct 7 Chief of Staff Digest is ready :brain:',
    'blocks': blocks
}


def send_slack(token: str, data: dict) -> bool:
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=body,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=utf-8'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('ok'):
                print(f'[OK] Message sent to {CHANNEL}')
                return True
            else:
                print(f'[ERROR] Slack API error: {result.get("error")}')
                return False
    except urllib.error.URLError as e:
        print(f'[ERROR] Network error: {e}')
        return False


def preview(data: dict) -> None:
    sys.stdout.buffer.write('\n=== SLACK PREVIEW (no token) ===\n'.encode('utf-8', errors='replace'))
    for block in data['blocks']:
        if block['type'] == 'header':
            sys.stdout.buffer.write(f"\n### {block['text']['text']}\n".encode('utf-8', errors='replace'))
        elif block['type'] == 'section' and 'text' in block:
            sys.stdout.buffer.write(f"{block['text']['text']}\n\n".encode('utf-8', errors='replace'))
        elif block['type'] == 'divider':
            sys.stdout.buffer.write('---\n'.encode('utf-8', errors='replace'))
        elif block['type'] == 'context':
            for el in block.get('elements', []):
                sys.stdout.buffer.write(f"[{el.get('text','')}]\n".encode('utf-8', errors='replace'))
    sys.stdout.buffer.write('=================================\n'.encode('utf-8', errors='replace'))


if __name__ == '__main__':
    token = (
        os.environ.get('SLACK_TOKEN') or
        os.environ.get('SLACK_BOT_TOKEN') or
        os.environ.get('SLACK_API_TOKEN') or
        ''
    )

    if token:
        success = send_slack(token, payload)
        sys.exit(0 if success else 1)
    else:
        print('[INFO] No Slack token found. Printing preview.')
        preview(payload)
        sys.exit(0)
