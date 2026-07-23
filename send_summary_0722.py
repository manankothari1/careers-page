import json, os, sys, urllib.request, urllib.error

TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "Your Daily Decision Brief - Wednesday, July 22", "emoji": True}
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! Great day of meetings. You had *2 sessions* today and made some genuinely important calls that push the line cook problem forward in a meaningful way. Here's everything you decided, why it matters, and what needs to happen next."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:busts_in_silhouette: HIRING LEADS STANDUP* | 8:45 AM"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bar_chart: Key Decisions & Rationale*\n\n*1. Line cook data locked as the load-bearing proof point*\n>*Decision:* Share the fill-rate-by-role graph with Dana for design review.\n>*Why:* The data is striking - line cook fills at only *7%* healthy vs 35-55% for barista/server/counter service, with a 54-55% unhealthy rate. This is the single most convincing visual to anchor the 'why this matters' story for John and leadership. You called it the 'load-bearing piece of data.' Nailed it.\n\n*2. Post-job-creation boost experiment = proof of intent*\n>*Decision:* Use the boost modal results (~20-25% of users boosted immediately after job creation) as supporting evidence for proactive hiring interventions.\n>*Why:* If people are willing to spend money the moment they post a job, they'll respond to nudges at the right moment. This validates the 'trigger-based' test bucket Dana is proposing. Solid foundation.\n\n*3. Dana's 4 FFH adoption blockers validated by the room*\n>*Decision:* Align on Dana's framing ahead of today's John check-in. No pushback - everyone in the room agreed these are the real barriers.\n>*The 4 blockers:* (1) Hiring pain is normalized - OMs don't feel urgency if no open role right now. (2) Perceived switching cost from Indeed - even unhappy Indeed users default to inertia. (3) Right message, wrong moment. (4) Trust gap - every hiring tool claims speed, Homebase has no differentiated proof yet.\n>*Why it matters:* This reframes the whole product from reactive (triggered by pain) to proactive. You articulated it perfectly - it's about preventing the pain, not reacting to it. That's a real strategic shift.\n\n*4. 3 test buckets approved for John check-in*\n>*Decision:* Dana presents three buckets to John today. Room is aligned.\n>*(1) Indeed job scraping + 1-click repost* - Remove the switching cost. You flagged Indeed's duplicate-flagging policy risk; Dana's call: small cohort, validate click-through first, figure out policy later. You're both right - test the behavior, then solve compliance.\n>*(2) Trigger-based outreach* - Surface signals that predict upcoming hiring need (Usman's locally-hosted signals model is already running).\n>*(3) Candidate-first experience* - Show OMs candidates available in their area as proof of Homebase value before they've posted.\n\n*5. Usman's candidate email experiment: greenlit*\n>*Decision:* Usman runs a 'candidates in your area right now' email experiment. Can execute in ~2 days.\n>*Why:* Even though it's slightly misleading (candidates won't be reserved), the test question is simply: does seeing 'people who fit your needs exist here' drive trial? That's worth knowing. You understood the nuance.\n\n*6. 'How soon do you need to hire?' UX question = valuable but not the immediate unlock*\n>*Decision:* Deprioritized for now. Dana agreed it's worth pursuing but won't crack the trial breakthrough problem today.\n>*Why:* Good call to not let perfect be the enemy of good. Keep it in the backlog."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Your Action Items from This Meeting*\n• *SEND Dana the Linear project link* for applicant flow design work (she asked in the thread - she needs it for today's design review)\n• *Share job health graph + boost experiment results* with Dana - it's in the weekly Google doc under 'post job creation boost' line item; offer to send directly"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bar_chart: ANALYTICS WEEKLY* | 10:00 AM"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Key Decisions & Rationale*\n\n*1. Two-flag architecture LOCKED for SBA onboarding*\n>*Decision:* Flag 1 = `modal_seen` (suppresses modal indefinitely after first display). Flag 2 = `sba_entered` (suppresses tooltip + pulsing once user enters SBA). Both flags must be true to stop all prompting.\n>*Why:* Clean, binary logic. No cooldown complexity. Follows user intent.\n\n*2. No cooldown period, no hard-coded reset date*\n>*Decision:* Rejected both in favor of the two-flag approach.\n>*Why:* Cooldown adds compounding logic complexity (tracking timestamps, multiple state transitions). Hard-coded dates don't work with phased rollout - cohorts launch at different times. Right call.\n\n*3. Pulsing icon APPROVED for V1*\n>*Decision:* Include a pulsing border animation on the SBA button at launch. Tooltip on hover always available. Pulsing stops only when user enters SBA.\n>*Why:* Your users are highly habitual. Even a visually present button gets ignored if it's not calling attention to itself. You've seen this in user interviews - they miss new buttons even when looking right at them. The pulse is the nudge.\n\n*4. Tooltip auto-surfaces on next session if modal was dismissed*\n>*Decision:* After modal dismissal, tooltip shows outright on the user's next session (not same session, not on hover - proactively displayed). Subsequent visits without SBA entry: tooltip continues each session with 'don't show me this again' option.\n>*Why:* Balances persistence with respecting intent. If they dismiss the modal, you're not giving up - you're just giving them a breath before the next touchpoint. The explicit 'don't show again' respects their final decision.\n\n*5. Jumpstart drawer suppressed whenever modal is shown*\n>*Decision:* Modal and jumpstart drawer are mutually exclusive - modal wins.\n>*Why:* Jumpstart overlays the SBA CTA entirely. Can't have both competing for the same real estate.\n\n*6. Clicking the SBA icon goes straight to SBA on subsequent visits*\n>*Decision:* First time = modal opens. Every click after that = straight to SBA.\n>*Why:* After the first intro, the user knows what SBA is. Don't make them read the onboarding again.\n\n*7. Roles usage definition LOCKED*\n>*Decision:* 'Using roles' = role set as default in the roster. NOT incidental assignment via shift scheduling dropdown.\n>*Why:* This is the 'correct' usage of the feature and gives the cleanest signal for the usage marker. FYI: secondary role usage is ~10%, tertiary ~4% - for context when you see these numbers."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: Team Action Items from This Meeting*\n• *Gurkiran:* Join Amplitude call with Meg - unblock grayed-out survey trigger + confirm multi-trigger support for SBA exit survey (all 3 cases: publish, escape hatch, mid-flow abandonment)\n• *Gurkiran:* Ask Nick about panel collapse event feasibility before deciding if it's worth adding\n• *Niko:* Screenshot finalized SBA onboarding flow diagram, publish to Confluence (include subsequent-use note: clicking icon goes straight to SBA after first time)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:fire: WATCH LIST - Things That Still Need Your Attention*\n\n:rotating_light: *Carlo Ferrer - 11+ DAYS OVERDUE* on Harness/OpenSpec. This is now a management issue. Has anything moved here?\n\n:rotating_light: *422 Job Publishing Errors* - 146 locations, day 12. Jatin owns RCA. Did you get a status update today?\n\n:memo: *Rami - JD Experiment:* Verify formatting signal + finalize prompt. You were pairing Thu AM - that's TOMORROW. Prep what you need.\n\n:memo: *Fadi brain dump* - Was this sent? It was a P0 from Jul 20.\n\n:memo: *Tatiana - Sitemap + MSA table* - Still outstanding from Jul 20 action items.\n\n:memo: *Izzy - Rami to Izzy handoff* on salary recs - confirm this happened.\n\n:memo: *Data Platform* - Process overhauled Jul 21. Named DP contact still TBD. Paul + Kanchana sync still needs to be booked.\n\n:memo: *Dana succession* - ~9 weeks to end of September. No plan. Page Templates Aug 14 is coming fast and Dana is off Aug 7. Handoff needs to start NOW."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Tomorrow's Setup*\n\n:star: *Pair with Rami (Thu AM)* - JD quality experiment: verify formatting signal, finalize prompt, prep Tanner for the 50/50 split build.\n\n:star: *John check-in happening today* - Dana was presenting the 3 test buckets. Follow up to see how John reacted. His reaction shapes your next sprint priorities.\n\n:bulb: *Good day, Manan.* The meeting today reframed FFH from a messaging problem to a timing + trust problem. That's a materially better frame. And the clarity on SBA onboarding logic means that ship can move. Keep pushing."
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Your Daily Decision Brief - Wednesday July 22"
}

def preview():
    sys.stdout.buffer.write(("\n=== SLACK PREVIEW ===\n" + json.dumps(payload, indent=2) + "\n").encode("utf-8", errors="replace"))

if not TOKEN:
    print("No SLACK_TOKEN found - printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("ok"):
        print(f"SUCCESS: Message sent to {CHANNEL}. ts={body.get('ts')}")
    else:
        print(f"SLACK ERROR: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"NETWORK ERROR: {e}")
    preview()
    sys.exit(1)
