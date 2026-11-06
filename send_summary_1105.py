#!/usr/bin/env python3
"""Daily digest for Manan Kothari -- Wednesday Nov 5, 2026 PST"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN") or
    os.environ.get("SLACK_BOT_TOKEN") or
    os.environ.get("SLACK_API_TOKEN") or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f9e0 Chief of Staff Daily Digest -- Wednesday, Nov 5",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey Manan! \U0001f44b Big day today -- you cast the scheduling vision to the whole team and "
                "got real alignment. Here's everything that happened, every decision you made, and what you need "
                "to do before you sleep. Day grade: *A-* \u2b50"
            )
        }
    },
    {"type": "divider"},

    # --- THEME ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f3c6 TODAY'S THEME*\n"
                "> \U0001f4c5 SCHEDULING VISION CAST -- BDD DOC IS THE NEXT UNLOCK -- RACHEL EMAIL CANNOT WAIT ANOTHER DAY"
            )
        }
    },
    {"type": "divider"},

    # --- MEETING 1: STANDUP ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4cb Meeting 1 of 2 \u2014 Hiring EPD Standup \u2014 8:45 AM PST*\n\n"
                "*Updates that matter to you:*\n"
                "\u2022 *Jatin* built 'Scheduling Reimagined' (HTML \u2192 commentable Google-Doc-style link) in ~20 mins. "
                "Tiger had independently started the same idea -- Jatin releases it first. "
                "Needs Vercel deploy so *you* can upload the scheduling doc for async team comments. "
                "Watch for the link.\n"
                "\u2022 *Fadi* moving candidate profile work to done; exploring UX polish items after Skye sync. "
                "No project to track it -- team agreed to revive a *UX/Product Polish catch-all* project in Linear. "
                "*Fadi* creates it, *Jatin* systematizes.\n"
                "\u2022 *Tiger*: Close job flow testing in final batch -- nearly done. "
                "Still blocked on Indeed job posting ID clarification (21-day PDF vs. 30-day API docs still unresolved).\n"
                "\u2022 *Iszael*: Wrapping spike today; SLO ongoing; Facebook integration being monitored; "
                "following up with JobCase on test replies.\n"
                "\u2022 *Soheil*: SLO wrapped; building Prompt Chips tickets for next sprint; "
                "scout for hiring accountants; Orca tasks.\n"
                "\u2022 *Gbolade*: UX updates partially blocked -- Fadi sync today expected to unblock.\n"
                "\u2022 Scout verdicts due *TOMORROW* (automated Jatin reminder sent).\n"
                "\u2022 Enzheng session *canceled* tomorrow (Retro conflict) -- revisit next week."
            )
        }
    },
    {"type": "divider"},

    # --- MEETING 2: SCHEDULING DISCOVERY ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f5fa Meeting 2 of 2 \u2014 Discovery: Hiring Leads (Scheduling Vision) \u2014 11:00 AM PST*\n"
                "_Full team: Fadi, Bob, Jatin, Skye, Matan, Iszael, Gbolade, Soheil, Tiger_\n\n"
                "*What this was:* You walked the whole EPD team through the ideal-state scheduling architecture. "
                "This was a *vision cast*, not MVP scoping -- sequencing is the next conversation."
            )
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f7e2 Decisions Made (Scheduling Architecture):*\n\n"
                "1\ufe0f\u20e3 *Availability model locked:* Availability belongs to the *person*, "
                "shared across all jobs. Book on one job, that time is blocked everywhere. "
                "Multi-location interviewers included. Calendly-style.\n\n"
                "2\ufe0f\u20e3 *Multi-interviewer pooling:* Candidates see one *combined* availability pool across all interviewers. "
                "If two interviewers share a slot and candidate books it, job poster defaults as interviewer. "
                "Otherwise: least-booked interviewer gets assigned.\n\n"
                "3\ufe0f\u20e3 *Job-level booking rules:* Configurable *per job* (not just globally) for notice period + advance window. "
                "Today: fixed 2-day notice, 7-day max ahead. That changes in the new system.\n\n"
                "4\ufe0f\u20e3 *3-block time offering:* OAMs can send up to 3 specific time blocks to a candidate. "
                "Jatin flagged friction risk (makes it overhead for every booking). "
                "*You ruled: design decision, not arch blocker -- taking offline.* Deferred.\n\n"
                "5\ufe0f\u20e3 *Off-platform time recording:* Fadi surfaced it -- OAM and candidate agree on time outside Homebase, "
                "OAM needs to record it manually. *Manan to add to BDD doc.*\n\n"
                "6\ufe0f\u20e3 *No-times-work flow:* Candidate sees no open slots \u2192 requests more times from OAM. "
                "OAM sends a *new booking link*. Candidate never proposes their own times.\n\n"
                "7\ufe0f\u20e3 *Multi-round interviews:* Up to 3 rounds, each with its own format, length, interviewers, title, description. "
                "Entry-level = 1 round. Management = phone screen + in-person. Currently 0 round support in product. Big gap.\n\n"
                "8\ufe0f\u20e3 *Zoom support:* To be added to the scheduling doc. Currently in-person + phone only.\n\n"
                "9\ufe0f\u20e3 *Linear structure:* 'Revamping Scheduling' becomes an *initiative*. Each feature = a project. "
                "*Jatin* to convert. *You* to move product work into Linear to join standup. "
                "Architecture + system design (Bob + Jatin) informs sequencing first -- get primitives right so later features build cleanly.\n\n"
                "10\ufe0f\u20e3 *Nihilus sequencing factor (Skye):* All scheduling work must account for Nihilus dependency -- "
                "identify what's blocking vs. non-blocking before finalizing build timeline."
            )
        }
    },
    {"type": "divider"},

    # --- WORKSPACE INTEL ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4e1 Workspace Intel (3 customer-facing meetings today)*\n\n"
                "\U0001f3aa *Linda / Matt Paetkau \u2014 Adventure Air Sports (trampoline parks, 120-130 employees):*\n"
                "Very excited about HBA and shift fill. Key signal: wants a *wage-threshold soft approval* "
                "when shift replacement earns more than the person they're covering. "
                "Also: wants MCP connector to Claude/ChatGPT *more* than walled-in AI tool -- "
                "'would pay more for that than a walled product.' Linda to pass to product team.\n\n"
                "\U0001f4ca *Homebase & Sean (bi-weekly):*\n"
                "Reports page feedback. Big framing insight: past-data overtime charts are the *wrong* question. "
                "What matters is *forecasting* future OT before you can stop it -- not analyzing what already happened. "
                "'You've already cut that check.' Sean literally built his own scheduling tool with 9 prioritized constraints "
                "that generates schedules he wouldn't need to change. Weekly email digests: he turns them all off. "
                "'It's not changing anything I'm going to do today.'\n\n"
                "\U0001f3a8 *Young Art USA / Homebase Assistant demo (Ginhee + Lauren):*\n"
                "12-year customers. Switched from ADP to HB Payroll mid-year. Super excited about HBA. "
                "Top requests: break reminders direct to *employees* (not just managers), "
                "year-over-year labor comparison, labor segmentation to exclude remote/admin from studio ratio, "
                "employee performance dashboard for reviews (late clock-ins, missed breaks, coverage count), "
                "I-9 automation, HR compliance flagging. Already using a custom AI bot. "
                "Committed to giving feedback once HBA access opens."
            )
        }
    },
    {"type": "divider"},

    # --- YOUR ACTION ITEMS ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f525 YOUR ACTION ITEMS (do these tonight or first thing tomorrow)*\n\n"
                "\U0001f534 *[CRITICAL] SEND THE RACHEL EMAIL.* "
                "3 questions to Rachel Rosenberg at Indeed were *finalized Nov 4*. "
                "Job requisition ID clarification. 21 vs 30 day rule. Expiration date field. "
                "Tiger is blocked on close flow work until this resolves. This is now Day 2 past ready. DO IT.\n\n"
                "\U0001f534 *[CRITICAL] 2029 Vision One-Pager.* "
                "20+ days overdue. Board meeting opened Oct 15. Fadi submitted his. You have not. "
                "Every day that passes makes this worse.\n\n"
                "\U0001f7e0 *[URGENT] JD rules for Divij.* "
                "Day 12 overdue. Divij is literally idle waiting for you. "
                "Rules: 1 hire \u224830d=vanilla; 2+ hires='multiple positions available'; urgency <=2wk='urgently hiring'. "
                "Unresolved: ASAP definition + posted vs. activated date. Write this up and send it today.\n\n"
                "\U0001f7e0 *[URGENT] BDD doc updates (from today's scheduling session):*\n"
                "   - Add: OAM manually records off-platform agreed time\n"
                "   - Add: Candidate requests more times flow (OAM sends new link)\n"
                "   - Add: Zoom interview format support\n"
                "   - This BDD doc is what unblocks Jatin + Bob from starting the spike.\n\n"
                "\U0001f7e0 *[URGENT] Define scheduling feature priority sequencing.* "
                "You committed to this today. Jatin can't convert to Linear initiative until you've done this. "
                "What gets built first matters enormously given Nihilus dependency.\n\n"
                "\U0001f7e1 *Ping Skye re: Nihilus 60-day cancellation notice.* "
                "Deadline is ~late November. She needs to draft the parity migration plan. "
                "If she doesn't start this week, you're at risk.\n\n"
                "\U0001f7e1 *Confirm Sina's capacity with Jatin.* "
                "He's confirmed still on HBA shift fill handlers. "
                "That conflicts with his promise to put Sina on hiring count/speed. "
                "You need a straight answer. It's been unresolved since Nov 2.\n\n"
                "\U0001f7e1 *Tag Fatty for Verify CTA designs* on magic link success screen. "
                "Still pending from before Paris.\n\n"
                "\U0001f7e1 *Check Magic Link rollout status.* "
                "Gbolade was supposed to bump past 20% today (Nov 5). Did it happen? "
                "Any issues? Send success rate was 100% yesterday -- confirm it's holding.\n\n"
                "\U0001f7e1 *Write Scheduling Ideal State doc.* "
                "Malcolm is gone. Jatin called it essential in the Nov 3 deep dive. "
                "Today's session gives you the raw material -- don't let it sit.\n\n"
                "\U0001f7e1 *Tallroo dates email.* Still outstanding. Send November meeting invite including Skye.\n\n"
                "\U0001f7e1 *Prompt chips min wage.* "
                "Justin is back (Nov 3). Write the MD file and ping him -- he's waiting."
            )
        }
    },
    {"type": "divider"},

    # --- WATCH LIST ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4f0 Watch List \u2014 Active Fires*\n\n"
                "\u2022 *Indeed FSA Review* -- Jessica: no response, 9+ days past due. Escalate to Ashley Lutz *now*.\n"
                "\u2022 *Payroll double invoice* (~1,100 customers) -- Brant running daily ACH refund task. Fix merging soon.\n"
                "\u2022 *Entitlements* at 25% -- Adam blocked on PRs 1210, 1214, 1212 (HRM review backlog). Watch.\n"
                "\u2022 *Change payment method (Flex)* -- Edwin BACK, targeting rollout *next week*.\n"
                "\u2022 *Facebook API rate limiting* -- Day 14+. Iszael monitoring. No Meta response. Escalate NOW if nothing today.\n"
                "\u2022 *Nihilus cancellation notice deadline* -- ~late November. Skye hasn't started migration plan.\n"
                "\u2022 *Interview Confirmation BDD spec* -- OVERDUE. Jatin + Bob can't start spike without it.\n"
                "\u2022 *Janneke KT* -- HBA institutional knowledge. Leave imminent. URGENT.\n"
                "\u2022 *Carlo KT* -- Paternity through mid-Feb. Knowledge risk unresolved.\n"
                "\u2022 *Matt McAllister (new CMO)* -- Week 3. Get 30 mins. Don't let this drift."
            )
        }
    },
    {"type": "divider"},

    # --- FOOTER ---
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4c8 Key Metrics Snapshot*\n"
                "Magic Link: 100% send success @ 20% rollout \u2714\ufe0f | Entitlements: 25% cohort | "
                "Nihilus cost: ~$10.5K/mo (cleaning up) | Indeed: RECOVERED \u2714\ufe0f | HBA: 28 active users\n\n"
                "_You logged a solid A- today, Manan. The scheduling vision landed well -- "
                "the whole team is aligned on what you're building. Now the BDD doc and sequencing work are on you, "
                "and the Rachel email is literally just sitting there. You've got this. \U0001f4aa "
                "Chief of Staff signing off for the night._"
            )
        }
    }
]

payload = json.dumps({"channel": CHANNEL, "blocks": blocks, "unfurl_links": False})

def preview():
    sys.stdout.buffer.write((
        "\n========== SLACK DIGEST PREVIEW (Nov 5, 2026) ==========\n\n"
        "HEADER: Chief of Staff Daily Digest -- Wednesday, Nov 5\n\n"
        "THEME: SCHEDULING VISION CAST -- BDD DOC IS THE NEXT UNLOCK -- RACHEL EMAIL CANNOT WAIT ANOTHER DAY\n\n"
        "DAY GRADE: A-\n\n"
        "2 MANAN MEETINGS:\n"
        "  8:45am -- Hiring EPD Standup\n"
        "  11:00am -- Discovery: Scheduling Vision (full EPD)\n\n"
        "3 WORKSPACE MEETINGS:\n"
        "  Linda/Matt Paetkau (Adventure Air Sports) -- HBA + shift fill feedback\n"
        "  Sean Bi-Weekly -- Reports framing: forward-looking not backward-looking\n"
        "  Young Art USA (Ginhee + Lauren) -- HBA demo, excited, 12-year customers\n\n"
        "10 DECISIONS:\n"
        "  1. Availability belongs to person, Calendly model, shared across jobs\n"
        "  2. Multi-interviewer combined pool; least-booked assigned on ties\n"
        "  3. Job-level configurable booking rules (not global-only)\n"
        "  4. 3-block time offering to candidates -- deferred (friction concern)\n"
        "  5. Off-platform time recording use case to be added to BDD doc\n"
        "  6. No-times-work flow: OAM sends new link; candidate never proposes times\n"
        "  7. Multi-round interviews: up to 3 rounds, each configurable\n"
        "  8. Zoom support: to be added to scheduling doc\n"
        "  9. Linear: 'Revamping Scheduling' becomes initiative; features become projects\n"
        "  10. Nihilus dependency must factor into all scheduling sequencing (Skye)\n\n"
        "TOP ACTION ITEMS:\n"
        "  [CRITICAL] Send Rachel email (TODAY -- 2 days past ready)\n"
        "  [CRITICAL] 2029 Vision one-pager (20+ days overdue)\n"
        "  [URGENT] JD rules for Divij (Day 12 overdue -- he's idle)\n"
        "  [URGENT] BDD doc: add 3 missing use cases\n"
        "  [URGENT] Define scheduling feature priority sequencing\n"
        "  Ping Skye re: Nihilus 60-day notice deadline\n"
        "  Confirm Sina capacity with Jatin\n"
        "  Tag Fatty for magic link Verify CTA designs\n"
        "  Check Magic Link rollout bump status\n"
        "  Write Scheduling Ideal State doc\n\n"
        "=========================================================\n\n"
    ).encode("utf-8", errors="replace"))

if not TOKEN:
    print("No SLACK_TOKEN found -- printing preview.")
    preview()
    sys.exit(0)

req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=payload.encode("utf-8"),
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    if body.get("ok"):
        print(f"Sent! ts={body.get('ts')}")
    else:
        print(f"Slack error: {body.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
