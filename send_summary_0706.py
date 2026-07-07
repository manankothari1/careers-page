#!/usr/bin/env python3
"""Chief of Staff Daily Digest — Monday, July 6, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = 'D06E4QMHCNN'


def get_token():
    for var in ['SLACK_TOKEN', 'SLACK_BOT_TOKEN', 'SLACK_API_TOKEN']:
        t = os.environ.get(var)
        if t:
            return t
    return None


def s(text):
    return {'type': 'section', 'text': {'type': 'mrkdwn', 'text': text}}


def build_blocks():
    blocks = [
        {
            'type': 'header',
            'text': {
                'type': 'plain_text',
                'text': 'Chief of Staff Daily Digest — Monday, July 6',
                'emoji': True
            }
        },
        {
            'type': 'context',
            'elements': [{
                'type': 'mrkdwn',
                'text': '3 meetings today :calendar: | 12 decisions locked :white_check_mark: | Sprint week is GO :rocket:'
            }]
        },
        s('Manan, what a Monday! :star2: You kicked off Q3 with a bang — three power-packed meetings, a company-wide strategy alignment, and some genuinely sharp decisions across design, engineering, and go-to-market. Here\'s every decision you made today with full context and clear next steps:'),
        {'type': 'divider'},
        s('*:dart: DECISIONS MADE TODAY (12)*'),

        s('*1. :no_entry: Abigail (incoming designer) is NOT joining — position will NOT be backfilled*\n*Decision:* You\'re absorbing day-to-day design with AI + the existing design system. Fatty covers design-heavy lifting; Cindy reviews.\n*Why it\'s right:* Family medical situation — pragmatic call. Don\'t wait for a hire when AI + team can cover. Acceptance criteria will carry more weight as a quality gate.\n*:arrow_right: Action:* Connect with Ray for design workflow templates (he built the pricing page in code, saving 60-70% of FE time).'),

        s('*2. :recycle: Copy Job → Reactivate Job is LOCKED*\n*Decision:* Reactivated jobs don\'t trigger Indeed\'s duplicate flag. Copied jobs without sponsorship get zero visibility.\n*Why it\'s right:* Data confirmed: 41% of Q2 ICP jobs were copies. ~50 had zero applicants by D30. ATS users like Homebase get more leeway than individual users — a real differentiator to lean into.\n*:warning: Action:* Review Source Claiming Banner end-to-end with Matan before it ships (today or tomorrow).'),

        s('*3. :rotating_light: OpenAI fallback model needed — P0 reliability risk*\n*Decision:* A billing cap outage caused screener failures across applicants. As HP Assistant dependency grows, this is a single point of failure.\n*Why it\'s right:* Self-inflicted outage, but it exposed a critical gap. The more agentic features you ship, the worse this gets without a fallback.\n*:arrow_right: Action:* Confirm eng team is tracking this and has a timeline.'),

        s('*4. :rocket: Q3 Company Strategy locked: 4 priorities, shortened planning cycles*\n*Decision:* GTM Excellence | AI Assistant | Hiring (ICP = frequent frontline hirers) | Quality (elevated as explicit company-level focus for the first time). Q3 kickoff instead of H2 — tighter learning loops.\n*Why it\'s right:* This is the tech inflection point — Homebase is the scrappy upstart vs. ADP\'s empire. Speed wins. Q2 missed all goals but captured strong learnings; Q3 is about tighter bets.\n*For Hiring specifically:* Narrow to FFH (~10% of customers, food & bev). Line cook = #1 priority to unlock (most in-demand, hardest to fill, biggest halo effect if solved).'),

        s('*5. :wrench: Harness Framework = OpenSpec — Deadline July 10*\n*Decision:* OpenSpec selected as the framework for the Harness agentic dev platform.\n*Why it\'s right:* Building a workflow from ideation → spec → agent execution → QA → production. Homebase bot is already live (June 24) with 260 code contributions. EOY goal: every team runs agentic workflows.\n*:arrow_right: Action (Carlo):* Schedule Harness check-in this week.'),

        s('*6. :key: Culinary Agents integration — unblocked by secret setup*\n*Decision:* Work is complete on Homebase\'s side. Last blocker = generate a secure random secret (~8 chars), store in 1Password, share link with the Culinary Agents contact.\n*Why it\'s right:* The integration is ready. This is a quick unlock with a clear path.\n*:arrow_right: Action (Manan):* Email Culinary Agents contact for requirements → generate secret → store in 1Password → share link.'),

        s('*7. :bar_chart: Quantitative measurement mandate (from John Waldmann)*\n*Decision:* ALL tests must be explicit weekly hypotheses with measurable outcomes. Track: % of ICP jobs with zero applicants, CTR by job type, boost rate for hard-to-fill roles.\n*Why it\'s right:* John pushed hard on this — and he\'s right. Anecdotes are great for direction; data is what drives conviction and alignment.\n*:arrow_right: Action (Manan):* Reframe all applicant flow tests as explicit weekly hypotheses.'),

        s('*8. :speaking_head_in_silhouette: Messaging winners confirmed by channel*\n*Decision:* Data is now definitive — different messages for different audiences:\n• *External/paid:* "Smart Hire" wins (CTR, CPC, conversion)\n• *Cold trials:* "Personal Recruiter" drives signups (22 of 28)\n• *In-platform nudges:* "Homebase Advantage" wins (1.4-1.5x CTR, 4x email clicks)\n*Why it\'s right:* Existing users resonate with "we know your business"; non-users respond to end-to-end process framing. These are now your segmented playbooks.'),

        s('*9. :phone: Usman\'s pitch shifting to "we know your business" / Homebase Advantage framing*\n*Decision:* Multi-location prospects ($100-300/month on Indeed) are the sweet spot. $100/month price point not triggering pushback — objections are "we\'re good where we are," not price.\n*Why it\'s right:* Pain arc builds empathy, but the Homebase data advantage is the real differentiator for this segment. This framing is proven in-platform; now test it in sales calls.\n*:arrow_right: Action (Dana):* Draft revised Homebase Advantage call script → share with Matan TODAY.'),

        s('*10. :busts_in_silhouette: Next talent pool test: push notifications to recently terminated employees*\n*Decision:* First test (50 line cook jobs, 38K pool, 122 clicks, 13 applies) is running well. Next test = push notification to recently terminated employees.\n*Why it\'s right:* John\'s insight: the re-engagement sweet spot is ~2 weeks after leaving — either in need or dissatisfied with the new job. Perfect timing for a Homebase nudge.'),

        s('*11. :art: Design-to-code workflow is now the team\'s design process*\n*Decision:* Fadi + Ray proved it: pricing page built in code (not Figma) saved 60-70% of FE implementation time. With no incoming designer, this is the go-forward process.\n*Why it\'s right:* Pragmatic adaptation. AI-assisted design + existing design system + strong acceptance criteria = the new quality standard.\n*:arrow_right: Action (Manan):* Connect with Ray for AI-assisted design workflow tips and templates.'),

        s('*12. :scales: Talent rebalancing: no senior backend coverage*\n*Decision:* Engineer placed on extended leave mid-sprint caused missed security ticket + Datadog observability work. Martin + Jatin discussing options today. Shopify backfill arrives end of August.\n*Why it\'s right:* Can\'t absorb another sprint at this capacity — the security ticket miss is a real risk.\n*:arrow_right: Action (Martin + Jatin):* Finalize rebalancing plan today.'),

        {'type': 'divider'},

        s(':white_check_mark: *YOUR ACTION ITEMS — Manan*\n\n:fire: *P0 (Today/Tomorrow):*\n• Email Culinary Agents contact for secret requirements, generate ~8-char secret, store in 1Password\n• Review Source Claiming Banner end-to-end with Matan before it ships\n• Confirm OpenAI fallback model is on eng\'s radar\n\n:large_orange_circle: *P1 (This Week):*\n• Connect with Ray on design workflow + AI-assisted templates\n• Reframe all applicant flow tests as explicit weekly hypotheses (John\'s mandate)\n• Confirm Dana\'s Homebase Advantage script is drafted and shared with Matan'),

        {'type': 'divider'},

        s(':busts_in_silhouette: *TEAM ACTION ITEMS (track these)*\n• *Carlo:* Schedule Harness check-in this week (Jul 10 deadline, OpenSpec framework)\n• *Dana:* Draft revised Homebase Advantage outreach script → share with Matan *today*\n• *Dana + Jatin:* Identify product surface for Homebase Advantage signal test (zero-state or nudge variant)\n• *Matan:* Re-engage 2 prospects who didn\'t book a call; run Source Claiming Banner E2E with you\n• *Martin + Jatin:* Finalize talent rebalancing plan (no senior backend coverage on core sprint)\n• *Eng (urgent):* Implement OpenAI fallback model — screener failures are a revenue risk'),

        {'type': 'divider'},

        s(':eyes: *WATCH LIST (carry-overs — these need your attention)*\n:rotating_light: *Boost purchase bug* — 2 reporters in 2 days can\'t buy boosts. Revenue-impacting. What\'s the status with Matan?\n:money_with_wings: *ZipRecruiter holiday spend* — was burning $2K/1.5 days with no job-level caps. How much burned Jul 3-6?\n:clock1: *Rami\'s email blast* — 12 days overdue (was due Jun 25). Where does this stand?'),

        {'type': 'divider'},

        s(':star: *You absolutely crushed it today, Manan.* You navigated a surprise org change without missing a beat, locked in the biggest strategic pivot of the quarter (reactivate > copy), and left every meeting with clear owners and measurable next steps. John\'s quantitative mandate is exactly the push the team needed, and the "we know your business" framing is now yours to run across every channel. Breathe — you\'re building something real. Tomorrow is going to be just as good. :muscle:'),

        {
            'type': 'context',
            'elements': [{
                'type': 'mrkdwn',
                'text': '_Chief of Staff Daily Digest | Jul 6, 2026 | Meetings: Hiring Week in Review (9am), Sprint Kick Off (10am), Sprint Planning - Applicants (11am)_'
            }]
        }
    ]
    return blocks


def send_slack(token, blocks):
    payload = json.dumps({
        'channel': CHANNEL,
        'blocks': blocks,
        'text': 'Chief of Staff Daily Digest — Monday, July 6, 2026'
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        data=payload,
        headers={
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json; charset=utf-8'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        return {'ok': False, 'error': str(e) + ' | ' + body}
    except Exception as e:
        return {'ok': False, 'error': str(e)}


def preview(blocks):
    lines = ['\n=== CHIEF OF STAFF DIGEST PREVIEW (Jul 6, 2026) ===\n']
    for b in blocks:
        t = b.get('type', '')
        if t == 'header':
            lines.append('[HEADER] ' + b['text']['text'])
        elif t == 'section':
            lines.append(b['text']['text'])
        elif t == 'context':
            for el in b['elements']:
                lines.append('[ctx] ' + el['text'])
        elif t == 'divider':
            lines.append('-' * 60)
        lines.append('')
    lines.append('=== END PREVIEW ===\n')
    sys.stdout.buffer.write('\n'.join(lines).encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()


def main():
    token = get_token()
    blocks = build_blocks()
    if not token:
        print('No Slack token found. Showing preview:')
        preview(blocks)
        print('\nTo send for real: add SLACK_TOKEN or SLACK_BOT_TOKEN in Cursor Dashboard > Cloud Agents > Secrets.')
        return
    result = send_slack(token, blocks)
    if result.get('ok'):
        print('Message sent successfully! ts=' + str(result.get('ts', '')))
    else:
        print('Error sending message: ' + str(result.get('error', 'unknown')))
        preview(blocks)


if __name__ == '__main__':
    main()
