import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = (
    os.environ.get('SLACK_TOKEN') or
    os.environ.get('SLACK_BOT_TOKEN') or
    os.environ.get('SLACK_API_TOKEN') or
    ''
)
CHANNEL_ID = 'D06E4QMHCNN'

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Friday Wrap-Up - May 8, 2026",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan — big Friday. Four meetings, a surprise org restructuring, sprint 2611 clarity locked in, and a new engineering leader relationship officially started. Here's everything you decided today and exactly what needs to happen next. You crushed it. :muscle:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: TODAY'S MEETINGS*\n• 8:30am — Hiring Leads Standup\n• 9:15am — Manan/Dana 1:1\n• 10:00am — Jatin/Dana/Manan\n• 12:00pm — Martin/Manan"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:zap: DECISIONS MADE TODAY — 13 total*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Carlo moves to your applicant flow team for Sprint 2611* _[Jatin/Dana/Manan]_\n*Why:* Dana absorbs the capacity hit and is confident. Carlo is frontend-primary but can handle backend — gives your team the firepower to hit applicant flow goals in 2611.\n*Action:* Confirm Carlo's 2611 ticket assignments before Wednesday's planning session. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. 75/25 engineering capacity split locked for Sprints 2611-2613* _[Jatin/Dana/Manan]_\n*Why:* Balances shipping product work while making real dents in quality debt. Engineers self-select from KTLO backlog after completing product items — autonomy + accountability.\n*Action:* Make sure the KTLO/quality backlog is organized and prioritized before Wednesday (Jatin owns). :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Jason Noble terminated. Bob promoted to oversee Hiring + Distribution engineering* _[Jatin/Dana/Manan]_\n*Why:* Consolidates technical leadership under someone trusted. Bob will gradually delegate to Malcolm (Dana's side) and Izzy (your side) — getting him out of the weeds and into strategic technical direction.\n*Action:* In your next Bob 1:1, paint a clear picture of what 'strategic technical leadership' looks like for your team. Set the expectation explicitly. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. EM hire for your team: SF candidates now on the table despite 2x cost* _[Jatin/Dana/Manan]_\n*Why:* Toronto talent pool is not meeting your bar. The right EM unlocks team velocity — paying SF market rate is worth it given your team's growth stage.\n*Action:* Share JD + hiring criteria with Jatin. Confirm SF-based candidates are budget-approved. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Malcolm: 2-week paternity leave (not the full month previously expected)* _[Jatin/Dana/Manan]_\n*Why:* Smaller coverage gap than feared — good news. Jatin planning Toronto trip end of May specifically to build Malcolm's confidence and leadership readiness.\n*Action:* Confirm Malcolm's exact leave dates with Dana so sprint coverage can be planned. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Predicted Roles features handed off to Dana — fully designed, ready for Sprint 2611* _[Manan/Dana 1:1]_\n*Why:* You deprioritized these from your backlog to free up strategic space for marketplace work. Dana's team picks them up — careers page (company-level) and dashboard (location-level) both spec'd and designed.\n*Action:* Send Dana the Figma links + spec doc this weekend so Fatty can start planning. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Three critical UX bugs get dedicated project: 'Core product 2610 UX fixes'* _[Manan/Dana 1:1]_\n*Why:* These aren't nice-to-haves — they're broken core flows that hurt conversion and trust:\n  • Job posting doesn't redirect to dashboard (requires manual page refresh)\n  • Error states appear before the user does anything wrong\n  • Missing syndication toggle for first-time job posters\nDana is creating the project. IBK is available to fix these.\n*Action:* Prioritize all three bugs and confirm IBK is assigned with Dana. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. Wednesday 2611 planning sessions start — 15-min lead touchpoints* _[Jatin/Dana/Manan]_\n*Why:* Keeps sprint momentum tight without over-meeting. Fatty joins Dana's sessions. Matan + Usman optional for yours.\n*Action:* Confirm Wednesday invite is on calendar with correct attendees. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. Sponsored Jobs API spike assigned to Bob — design must match Indeed's UI/brand* _[Jatin/Dana/Manan]_\n*Why:* This is a spike to de-risk the build, not a full implementation. Concern flagged: Bob has a lot on his plate with the expanded role, so clear scope + timebox is critical.\n*Action:* Set a 1-sprint timebox for Bob's spike. Brief Indeed's design constraints to him before he starts. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. Nihilist billing crisis: moving to standard invoice approval flow* _[Hiring Leads Standup]_\n*Why:* Credit card hit limit — $6K billing dispute, service potentially disrupted. You created a PM vendor inventory Google Sheet to prevent this happening again across all vendors.\n*Action:* Redirect Nihilist, Talo, and ZipRecruiter vendor alerts to hiring-support@joinhomebase.com. Confirm Joseph resolves the $6K dispute before any service interruption. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*11. Show & Tell format locked: TLWA + Deal Breakers + Calendar* _[Hiring Leads Standup]_\n*Why:* No repeat of the 'how we work' segment — audience has seen it. Clean feature-forward format. TLWA demo may move to Monday sprint kickoff instead of Show & Tell.\n*Action:* Decide now: does TLWA demo stay in Show & Tell or move to Monday? Coordinate with Ray on Monday kickoff agenda. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*12. Nelson OOO 2 weeks → all analytics requests through triage only* _[Hiring Leads Standup]_\n*Why:* Team is critically short-staffed (down 3 analysts). No shortcuts — everything goes through triage. Emergency contact is Vlad. Ray providing markdown docs for virtual support.\n*Action:* Queue your most critical data pulls RIGHT NOW before Nelson's absence starts. Boost funnel drop-off %, Indeed purchase options, job title quality %, wage vs. applicants — all still outstanding and due before Wednesday's Cindy sync. :white_check_mark:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*13. Monday 9am PT: 6-week planning call with Martin (+ potentially Jatin + Ray)* _[Martin/Manan]_\n*Why:* Incredible relationship-building session with Martin. He's 30 years deep — ex-Meta (acquired by Zuckerberg), 1Password. His vision aligns perfectly with yours: spec-driven development + agentic workflows once the team stabilizes over the next few sprints. PM + engineer + designer in smaller, tighter units. This Monday call is your first real strategic alignment with him.\n*Action:* This weekend, prep a crisp 6-week view of 2611-2613 priorities + goals. This call could define how your team operates for the rest of the year. :white_check_mark:"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:red_circle: OVERDUE — DON'T LET THESE SLIP FURTHER*\n• *Nelson:* metro_area + bucketed_role + matching_roles _(overdue since Apr 8)_ — Nelson is now OOO 2 weeks. Escalate to Vlad.\n• *Matan:* Post Boost plan to #leads + customer survey _(overdue since Apr 23)_ — ping him Monday.\n• *TLWA brief to Ted:* Still unconfirmed if sent — check this weekend.\n• *Indeed ATS survey:* Check email immediately. Respond before it closes.\n• *Saja (Talroo):* Confirm CPA categories + campaign is configured.\n• *Data pulls for Cindy's Wednesday sync:* Boost funnel drop-off %, Indeed purchase options, job title quality %, wage vs. applicants — must be ready before Wednesday."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: NEXT WEEK AT A GLANCE*\n• *Monday:* 9am PT — 6-week planning call w/ Martin (+ Jatin/Ray) | Sprint kickoff | Engineers back from day off | Charmin wraps email work | Generic rule completion\n• *Wednesday:* First 2611 planning touchpoint w/ leads | Cindy sync — data pulls must be ready\n• *Thursday:* Boost Pathways review — it's ready for you now, don't miss it\n• *Friday:* Martin/Manan 1:1 follow-up\n• *May 11 (Sunday):* Boost Pathways marketing launch :rocket:\n• *May 19:* Sprint 2611 look-ahead\n• *May 22:* Customer Connection Challenge Show & Tell\n• *May 25+:* Cindy PTO (OOO 1+ week in BC — all feedback loops must close before then)\n• *May 29-31:* Dana + Fatty in SF (Ted joining)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: YOUR WEEKEND FOCUS — 3 THINGS*\n\n*1. Prep for Monday's Martin call :brain:*\nBring a crisp 6-week view of 2611-2613. This is your first strategic alignment with him — come in sharp.\n\n*2. Queue your data pulls for Cindy :bar_chart:*\nBoost funnel drop-off, Indeed purchase options, wage vs. applicants — all needed before Wednesday. Do it before Monday morning.\n\n*3. Review Pathways to Boost :eyes:*\nCarlo flagged it ready. 15 minutes now saves an entire async thread Monday."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "13 decisions. Major org moves landed cleanly (Bob elevated, Carlo shifted, EM search expanded to SF, Jason Noble out). Sprint 2611 has a clear shape. And Martin? That relationship is going to compound in a big way — his vision and yours are perfectly aligned. Have a great weekend, Manan. You're building something real. :ocean:"
        }
    }
]


def preview():
    print('=== SLACK MESSAGE PREVIEW ===\n')
    for block in blocks:
        if block.get('type') == 'section':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write((text + '\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'header':
            text = block.get('text', {}).get('text', '')
            sys.stdout.buffer.write(('=== ' + text + ' ===\n\n').encode('utf-8', errors='replace'))
        elif block.get('type') == 'divider':
            sys.stdout.buffer.write(b'---\n\n')


if not SLACK_TOKEN:
    print('No SLACK_TOKEN found — printing preview only.')
    preview()
    sys.exit(0)

payload = json.dumps({
    'channel': CHANNEL_ID,
    'text': 'Friday Wrap-Up: 13 decisions from May 8, 2026 — action items inside.',
    'blocks': blocks
}).encode('utf-8')

req = urllib.request.Request(
    'https://slack.com/api/chat.postMessage',
    data=payload,
    headers={
        'Authorization': 'Bearer ' + SLACK_TOKEN,
        'Content-Type': 'application/json; charset=utf-8'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode('utf-8'))
    if result.get('ok'):
        print('Slack message sent successfully!')
        print('Message timestamp:', result.get('ts'))
    else:
        print('Slack API error:', result.get('error'))
        sys.exit(1)
except urllib.error.URLError as e:
    print('Network error sending Slack message:', e)
    sys.exit(1)
