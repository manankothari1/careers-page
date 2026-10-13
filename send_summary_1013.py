#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Monday Oct 13, 2026
Reviews Oct 12 CEST workday (Spain Day 11)
Meetings reviewed: 2 workspace-visible calls (Matan's F&B research + Shan/Sammy scheduling research)
"""
import os
import sys
import json
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

BLOCKS = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f30d CHIEF OF STAFF DAILY DIGEST \u00b7 MONDAY OCT 13 \u00b7 SPAIN DAY 11",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Good morning, Manan! \u2600\ufe0f You had *2 workspace-visible meetings* on Monday that matter for your roadmap. Neither was yours directly \u2014 but both contain signals you need to act on. Here\u2019s what happened and what it means for you."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb MEETING 1 \u2014 7:45 PM \u00b7 Matan x Jeff Mauldin (Ria Pizzeria, F&B Non-Converter Research)*\n_Matan Chen Zion interviewing an F&B SMB owner who trialed Hiring Assistant and didn\u2019t convert_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4a1 Key Insights & Decisions:*\n\n*1. PAY-PER-POST pricing resonates most with seasonal operators \u2014 this is a real signal.*\nJeff said monthly subscriptions feel like \u2018paying for Netflix you never watch.\u2019 He would pay *$100\u2013$250 per job post/hire* \u2014 not a monthly subscription. Month-to-month at $199 is a non-starter for operators who only hire 4\u20135x/year. This validates the need to explore usage-based pricing for low-frequency hirers.\n\n*2. Cultural fit screening is the #1 unlock \u2014 skills are table stakes.*\nJeff said verbatim: \u2018If you can hire for the right character, I can teach them the job \u2014 but I can\u2019t teach them character.\u2019 He\u2019d pay *whatever you charge* for culture-fit screening. Your AI screener needs to move beyond skills/availability toward personality signals. This is your biggest competitive moat.\n\n*3. 30/60/90-day hiring forecast = Jeff does this on pen and paper today.*\nHe literally tracks staff outlook 3 months out on paper. He said: \u2018If you could figure out a way using AI or some tool that could help forecast hiring needs \u2014 that\u2019s a game changer.\u2019 This is *direct validation of your Intent Signals feature.* He also volunteered that his surprise departure (supervisor left suddenly) could have been predicted by shift swaps + lateness patterns. Matan confirmed we\u2019re building exactly this.\n\n*4. Screener question completion is a conversion killer.*\nOf 47 applicants, the vast majority did *not* answer screener questions. Only ~6 scheduled interviews. ~50% of those no-showed. Zero hires from Homebase \u2014 hired a customer\u2019s daughter via referral. The funnel is broken before we even get to AI.\n\n*5. Self-scheduling for interviews = loved it. Zero friction there.*\nJeff specifically called out interview self-scheduling as a time-saver. \u2018I don\u2019t have to go back and forth \u2014 they just pick a slot.\u2019 Interview no-shows are the problem, not scheduling friction.\n\n*6. Virtual interviews are a feature gap.*\nJeff moved from California to Georgia and manages Ria Pizzeria remotely. He wants built-in video interviews \u2014 said younger candidates (<30) would prefer virtual. Google Calendar integration is currently broken. He sees this as a barrier to scaling interview volume.\n\n*\U0001f3af 'Hire Smarter, Not Hire Faster' = VALIDATED.*\nMatan\u2019s pitch of \u2018Hiring shouldn\u2019t be a second job\u2019 landed. Jeff said: \u2018If the tool delivers based on cultural fit and skill set \u2014 I\u2019m all in.\u2019"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb MEETING 2 \u2014 9:40 PM \u00b7 Shan/Sammy x Stacy Dyer (Trianon Coffee)*\n_Shan Shen (designer) + Sammy Halabi (PM) running a product research session on scheduling/timesheet pain points. Stacy = owner, 2-location coffee shop, 11 employees, uses Homebase + Gusto + Square._"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4a1 Key Insights & Decisions (relevant to your work):*\n\n*1. Gusto sync bug is breaking payroll for small operators \u2014 it\u2019s been broken for YEARS.*\nEvery time Stacy adds a new employee in Gusto and hits \u2018sync\u2019 in Homebase, *all existing employees break their mapping.* Only employees from the original sync work. CS hasn\u2019t fixed it in 2+ weeks. She\u2019s been doing manual copy-paste swivel-chair data entry because \u2018there are only 11 of us.\u2019 This is a roster/payroll integration bug \u2014 Sammy owns it but it\u2019s worth knowing this is a live blocker for SMBs.\n\n*2. Tip auto-export Homebase \u2192 Gusto = highest pain point.*\nTip pooling is her most time-consuming task. Tips entered in Homebase as \u2018cash tips\u2019 at clock-out *cannot auto-export to Gusto* \u2014 she manually copy-pastes every pay period. She would love tips to flow automagically into Gusto. Not your problem directly, but informs how payroll frictions drain retention.\n\n*3. Overtime needs weekly view, not bi-weekly \u2014 federal compliance requirement.*\nGusto requires overtime reported by week. Homebase defaults to pay-period (bi-weekly). Stacy has to run a separate report per employee per role for any overtime week. This is a scheduling/payroll pain \u2014 good signal for Sammy\u2019s team. Stacy loved the \u2018Your Numbers\u2019 prototype concept but needs: weekly breakdown + employee-level drill-down + mid-period \u2018heading toward OT\u2019 alerts.\n\n*4. Shift trade OT warning = new feature request.*\n\u2018If someone trades a shift off-platform or across a pay-period week boundary, it silently pushes them into overtime.\u2019 She wants: \u2018This trade will push [employee] into overtime this week \u2014 approve anyway?\u2019 Scheduling team feature, but signals that compliance + money are the core motivators for operators staying on Homebase.\n\n*5. \u2018Your Numbers\u2019 dashboard prototype = validated concept, needs iteration.*\nStacy liked the late clock-in + overtime cards. Key feedback: show overtime by week, add employee-level drill-down (not just aggregate), and label data points as \u201812 min past 90-min avg\u2019 (not just \u2018102\u2019). The directional proof-of-concept works."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a1 YOUR ACTION ITEMS \u2014 TODAY (Tuesday Oct 13)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f525 *OVERDUE \u2014 DO FIRST THING:*\n\n\u2022 *Email Jessica Kanaskie (jkanaskie@indeed.com) \u2014 INDEED DAY 51.* You were supposed to do this yesterday (Monday). The AE65 source name hypothesis needs to be in her inbox NOW. Don\u2019t wait another day.\n\n\u2022 *Carlo KT \u2014 Paternity starts TODAY.* This is your last window. Block 2-3 hrs with Carlo immediately. Priorities: AE65 source name change, Iterable 6 emails fix, \u2018do not syndicate\u2019 bug, Q4 continuation sizing handoff.\n\n\u2022 *Q4 Continuation Sizing \u2014 TODAY or never.* Carlo is gone. This has to happen today."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f4dd *ACTIONS FROM TODAY\u2019S MEETINGS:*\n\n\u2022 *Ping Matan* about Jeff Mauldin interview \u2014 ask him to share the full transcript/notes. The pay-per-post pricing signal + cultural fit + 30/60/90 hiring forecast = 3 separate product bets you need on your radar for Q1 framing. This isn\u2019t just PMM research \u2014 it\u2019s your roadmap.\n\n\u2022 *Verify Row 42 (Interview Confirmation = M) priority for Q4.* Jeff validates: 50% interview no-show rate is a direct conversion killer. If we don\u2019t confirm interviews, we don\u2019t hire anyone. This should be a Q4 must-ship.\n\n\u2022 *Add \u2018pay-per-post\u2019 pricing model as a Q1 experiment flag to Skye.* Jeff = low-frequency seasonal operator. He will never pay $99/mo annual or $199/mo M-t-M. But he\u2019d pay $100\u2013$250 per hire. This is a TAM expansion conversation for next planning cycle.\n\n\u2022 *Escalate Gusto sync bug to Sammy.* Stacy has been manually copy-pasting for 2+ years. CS ticket is unresolved 2+ weeks. This is a retention risk.\n\n\u2022 *Note for Shan\u2019s Your Numbers iteration:* Weekly OT view (not bi-weekly) + employee drill-down + \u2018heading toward OT\u2019 mid-period alert = the 3 must-haves from Stacy."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\u23f0 *STILL OVERDUE FROM LAST WEEK (CRITICAL):*\n\n\u2022 *3-Year Vision One-Pager* \u2014 Board meeting opens Oct 15. This is *Thursday.* Do you have a draft? Even 3 bullet bets is better than silence to John.\n\u2022 *Skye source name rollback recommendation* \u2014 was due yesterday. Send today.\n\u2022 *Trial source claiming \u2192 flip to 100%* \u2014 decision made Oct 9. Still pending. Do it.\n\u2022 *Rachel Q4/Q1/Q2 UX view* \u2014 was due Oct 7. Did it go out?\n\u2022 *Jon\u2019s \u2018Hire Smarter\u2019 3-5 question sales draft* \u2014 review it. Matan is scheduling the call.\n\u2022 *Orca comms QA with IBK* \u2014 Matan built the skill. Manual QA needed before scaling to 80 touchpoints.\n\u2022 *Gift cards owed* \u2014 Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50). Send today."
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f9e0 BIG PICTURE \u2014 WHY TODAY MATTERS*\n\nThe Jeff Mauldin interview is more than a non-converter study \u2014 it\u2019s a *proof point for your Q4/Q1 bets.* Jeff is a seasoned 30-year restaurant operator who tracks hiring forecasts on paper. He can\u2019t justify $99/mo when he hires 4x/year. But he\u2019d pay $100\u2013$250 per hire if the match quality is right. That\u2019s your pricing + positioning problem for Q1.\n\nYour Q4 is about *fixing the funnel so the product earns the right to charge.* Screener completion, interview confirmation (no-shows!), and cultural fit signals are the 3 things standing between you and a hire. Jeff showed you all 3 gaps in one 45-minute call.\n\nAlso: Carlo leaves today. Everything that was supposed to happen Monday has to happen now. Don\u2019t let this slip."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4ca DAY GRADE: B+*\n_Two high-quality research calls happened in the workspace today \u2014 strong customer signal, clear validation of your roadmap bets. Execution risk is all on the Indeed/Carlo/one-pager front. The work is right; the follow-through has to catch up._\n\n\u2014 Your Chief of Staff \U0001f1ea\U0001f1f8"
        }
    }
]

TEXT_FALLBACK = (
    "CHIEF OF STAFF DAILY DIGEST - Monday Oct 13 - Spain Day 11 | "
    "2 workspace meetings: Matan x Jeff Mauldin (F&B non-converter - pay-per-post pricing validated, "
    "cultural fit = #1 want, intent signals confirmed); Shan/Sammy x Stacy Dyer (Gusto sync bug, "
    "tip auto-export, OT weekly view needed). Action items: Email Jessica Kanaskie NOW (Day 51), "
    "Carlo KT TODAY (last day), Q4 continuation sizing TODAY, 3-yr one-pager due THURSDAY."
)


def preview():
    import sys
    lines = [
        "",
        "=" * 70,
        "  CHIEF OF STAFF DIGEST PREVIEW (no Slack token - not sent)",
        "=" * 70,
        f"  Channel: {CHANNEL}",
        "",
        "  FALLBACK TEXT:",
        f"  {TEXT_FALLBACK}",
        "",
        "  BLOCK COUNT: " + str(len(BLOCKS)),
        "=" * 70,
        "",
    ]
    sys.stdout.buffer.write("\n".join(lines).encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")


def send():
    payload = json.dumps({
        "channel": CHANNEL,
        "text": TEXT_FALLBACK,
        "blocks": BLOCKS
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"Slack message sent successfully. ts={body.get('ts')}")
            else:
                print(f"Slack API error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if not TOKEN:
        preview()
    else:
        send()
