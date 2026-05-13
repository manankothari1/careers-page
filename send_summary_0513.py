#!/usr/bin/env python3
"""
Chief of Staff Daily Summary — May 12, 2026 (PDT)
Sends Slack DM to Manan Kothari with decisions, action items, and rationale.
"""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

BLOCKS = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":sun_with_face: *Good evening, Manan!* Here's your end-of-day intel"
                " for *Tuesday, May 12* — you had 4 meetings and moved a TON of important"
                " pieces forward today. Seriously, strong day. Let's make sure nothing"
                " slips through the cracks. :rocket:"
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 1 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:one:  Ted / Manan — 10:30 AM  |  Marketplace Deep Dive*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:white_check_mark: Decisions Made*\n"
                ">• *Rami (senior DS) is joining the marketplace team* within 2-3 days, once he wraps the cash-out project for John Boldman. He'll work alongside Vij and inherit the existing (never-shipped) role-matching foundation.\n"
                ">• *Two experiment tracks locked:*\n"
                ">   (1) Reach out to *previous applicants in the last 30 days* (better quality signal than the 2-year window that bombed in early 2026)\n"
                ">   (2) *OEM candidate lists* — give customers curated lists for direct outreach\n"
                ">• *Week-of-May-19 goals:* Scope 2611 sprint, fully understand Vij's existing DS work, onboard Rami to context.\n"
                ">• *Offsite week (May 25):* Ted is pushing to have Rami attend offsite for dedicated marketplace strategy alignment — define V1 matching algorithm requirements.\n"
                ">• *POC timeline: 2612/2613 (June 8-15)* — Ted is skeptical but it's the target. Foundational matching work must come first.\n\n"
                "*:brain: Rationale*\n"
                ">The early 2026 experiment failed for 3 fixable reasons: matching was too crude (business-category level only), time window was too broad (2 years), and email copy was weak. With 90K applicants/month between V1 and V2, even a 5-10% conversion would *double or triple* Homebase-sourced volume. The ROI is massive — this is the right bet to double down on.\n\n"
                "*:dart: Your Action Items*\n"
                ">• :calendar: *This week:* Review Vij's DS work and share context doc with Ted + Rami before May 19\n"
                ">• :calendar: *By May 19:* Scope 2611 sprint with engineering team\n"
                ">• :calendar: *Confirm with Ted:* Is Rami approved for offsite attendance? Push on this — it's worth the investment for alignment.\n"
                ">• :warning: *Watch:* Ted is skeptical about June POC. If Vij's existing work is strong, June is doable. If not, reset the clock now — better to know early."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 2 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:two:  Usman / Manan — 11:00 AM  |  Homebase Boost Sales Motion*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:white_check_mark: Decisions Made*\n"
                ">• *Boost = primary sales tool* for low applicant flow. 24-hour window after trial start is the key health signal — Boost is the lever to pull when jobs are struggling.\n"
                ">• *Manan will join Day-2 sales demos* when Boost is introduced. Calls aren't pre-scheduled, so you'll need a heads-up system with Usman.\n"
                ">• *One-pager:* Matan drafts the initial version (his domain), Usman collaborates, then iterate based on real customer objections and reactions.\n"
                ">• *Sales training session:* Offered Friday 9:30 AM (your 12:30 PM). Prioritize the team's selling time — don't block prime hours.\n"
                ">• *Indeed Hello:* Still buggy. NOT ready for sales pitching yet. Docs exist for training purposes only.\n"
                ">• *Career Sites:* Every business owner can now customize + embed. Need a consistent intro script.\n\n"
                "*:brain: Rationale*\n"
                ">Low applicant flow is the #1 deal-killer at trial close. Boost directly solves the problem Usman's team faces most — making this the centerpiece of the sales narrative is exactly right. The one-pager ensures message discipline across the team so every rep tells the same story.\n\n"
                "*:dart: Your Action Items*\n"
                ">• :calendar: *Immediately:* Ping Matan — one-pager is due as top priority. Usman needs it before the sales motion kicks off May 25-26.\n"
                ">• :calendar: *Coordinate with Usman:* Set up the notification flow so you actually *can* join Day-2 calls when needed. Don't leave this as 'figure it out later.'\n"
                ">• :calendar: *Friday 12:30 PM:* Block your calendar for potential sales training (confirm with Usman).\n"
                ">• :warning: *Don't let the team pitch Indeed Hello.* Make sure Usman has explicitly told reps it's off-limits until the bug is fixed."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 3 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:three:  Manan / Ray Weekly — 3:15 PM  |  6-Week Strategy + Vision*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:white_check_mark: Decisions Made*\n"
                ">• *Vision communication is your new #1 leadership priority.* Pick 3 things to be true by year-end and write them down in plain language. 'As good or better than relying on a human' is the standard.\n"
                ">• *Two themes for the next 6 weeks:*\n"
                ">   (1) *Unlock OEM spend* — Homebase Boost (branded, purchased, differentiated from free) + Sponsored Jobs API + human-led nudges\n"
                ">   (2) *Tap the marketplace / own our destiny* — Match active job seekers (past 30 days) to additional jobs; curate candidate lists; location-based matching via Supabase\n"
                ">• *Sponsored Jobs API: high-risk of delay.* Indeed dependencies = unpredictable response times. Won't complete by 26.12. Plan: build front-end journeys in advance using API specs if available.\n"
                ">• *Homebase Boost = #1 priority this sprint.* Source attribution shifting from 'Indeed' to 'Home Base Boost' — big for brand differentiation.\n"
                ">• *Removed from scope:* Talent pool save candidates (too complex, too much UX work). Dollar-for-dollar matching (fundraiser analogy — deemed ineffective).\n"
                ">• *Target:* 4+ experiments in applicant flow over 6 weeks.\n"
                ">• *Ray deliverable:* Detailed plan from vision doc by Thursday EOD, aligned with exec presentation Tuesday May 19.\n\n"
                "*:brain: Rationale*\n"
                ">The feedback you received — 'hard for a team to work towards a vision I don't share' — is a gift. It confirms your instinct to simplify and document. The two-theme structure is smart: OEM spend fixes the revenue problem fast; marketplace/own-destiny builds the moat. Cutting dollar-for-dollar matching and talent pool saves scope and focuses the team on things that can actually move the needle in 6 weeks.\n\n"
                "*:dart: Your Action Items*\n"
                ">• :fire: *TODAY/TOMORROW:* Draft the vision doc. Keep it to one page. 3 things that will be true by Dec 31. Share with Ray so he can use it as the plan's foundation.\n"
                ">• :calendar: *Thursday EOD:* Receive and review Ray's detailed plan — experiment lists for both themes, definite vs. 'if capacity' columns, aligned for Tuesday May 19 exec presentation.\n"
                ">• :calendar: *Tuesday May 19:* Exec presentation on 6-week plan. Make sure you and Ray are fully aligned before that meeting.\n"
                ">• :warning: *Sponsored Jobs API risk:* Align with Bob on what 'front-end journey in advance' looks like this sprint. Don't let the spike drag on without a clear deliverable."
            )
        }
    },
    {"type": "divider"},

    # ── MEETING 4 ──────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:four:  Matan / Manan — 4:00 PM  |  Boost Launch GTM + 2610/2611 Roadmap*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*:white_check_mark: Decisions Made*\n"
                ">• *Launch timeline locked:* QA complete May 22, sales motion kicks off May 25-26.\n"
                ">• *Usman owns talk track + one-pager* for Boost messaging and positioning (Matan drafts, Usman collaborates — consistent with what you agreed in the 11 AM).\n"
                ">• *Deep link in transactional emails* must be updated once messaging is finalized — this is a live dependency, don't forget it.\n"
                ">• *Existing cadence confirmed:* Day 2-3 trigger for <5 applicants; Day 5 follow-up for <15 applicants. Sequence: transactional email → EK calls → SMS/calls via Salesforce.\n"
                ">• *Roadmap visibility gap acknowledged.* Matan is building a comprehensive roadmap in Linear. Lead times established: 6-8 weeks for Tier 1 launches, 2-4 weeks for Tier 2.\n"
                ">• *Cross-functional structure:* PMM, Sales, CS, Data Science will be included in look-aheads going forward. Joint roadmap showing all team contributions per initiative.\n"
                ">• *Matan needs earlier involvement in planning meetings.* This is an ongoing tension — he feels excluded and it's showing up in late marketing materials.\n"
                ">• *2610 scope confirmed:* Homebase Boost, Sponsored Jobs API spike, ZipRecruiter test, Careers page 2.1 (embed codes, location editing, UX improvements).\n"
                ">• *2611 planned features:* Full Sponsored Jobs API (Tier 2 GTM needed), CPC experiment (50c days 1-3, 45c days 4-7, 40c day 8+), full-page boost modal post-job-posting, boost modal UI upgrades (3-column, recommendation system).\n\n"
                "*:brain: Rationale*\n"
                ">Matan's frustration about being excluded is a signal about process, not personality. If marketing materials keep coming in late, the root cause is insufficient lead time in planning — not Matan. The 6-8/2-4 week lead time standard is exactly right, and getting it into Linear creates accountability. The CPC experiment (50c→45c→40c step-down) is clever — lets you optimize spend while maintaining applicant flow quality.\n\n"
                "*:dart: Your Action Items*\n"
                ">• :fire: *TOMORROW (May 13):* Cindy contacts Matan for copy review on full-page boost design — make sure this happens. Confirm with Cindy.\n"
                ">• :calendar: *Before May 22 QA complete:* Update deep link in transactional emails once Matan's messaging is finalized.\n"
                ">• :calendar: *Next sprint planning:* Explicitly add Matan to planning invites 6-8 weeks out for Tier 1 items. Don't let this slip.\n"
                ">• :memo: *Matan's GTM roadmap:* Ask for a share link to the Linear board — you want visibility before the exec presentation May 19.\n"
                ">• :warning: *2611 CPC experiment needs a hypothesis statement.* Make sure engineering knows the success metric before they build the step-down logic."
            )
        }
    },
    {"type": "divider"},

    # ── MASTER ACTION ITEM ROLLUP ──────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":clipboard: *MASTER ACTION ITEM ROLLUP — What Needs to Happen Next*\n\n"
                "*Tonight / First Thing Tomorrow:*\n"
                ">:fire: Draft the vision doc — 3 things true by year-end, one page, share with Ray\n"
                ">:fire: Ping Matan: one-pager for Boost sales must be prioritized NOW (May 25-26 launch is 13 days away)\n"
                ">:fire: Confirm with Cindy she's contacting Matan tomorrow for full-page boost copy review\n\n"
                "*By Thursday EOD:*\n"
                ">• Receive Ray's detailed 6-week plan (experiment lists, definite vs. 'if capacity,' May 19 exec-aligned)\n"
                ">• Coordinate with Usman on Day-2 demo notification flow — set this up concretely\n"
                ">• Review Vij's existing DS work; prep context doc for Rami\n\n"
                "*By Friday:*\n"
                ">• Optional: join Usman's Friday 9:30 AM sales training (12:30 PM your time) — confirm attendance\n"
                ">• Confirm with Ted: Rami attending offsite? Push for yes.\n\n"
                "*By May 19 (Tuesday — Exec Presentation):*\n"
                ">• Scope 2611 sprint with engineering team\n"
                ">• Align with Ray on exec presentation content\n"
                ">• Get Matan's Linear GTM roadmap link — review before presentation\n\n"
                "*Before May 22:*\n"
                ">• Update deep link in transactional emails (dependency: Matan finalizes messaging first)\n"
                ">• All Cindy design feedback closed (she's OOO May 25+ in BC)\n\n"
                "*Open Risk to Watch:*\n"
                ">:warning: Sponsored Jobs API is high-risk (Indeed dependencies). Set a clear spike deliverable with Bob — what does 'front-end journey in advance' look like?\n"
                ">:warning: Ted is skeptical on June POC timeline for marketplace. Assess Vij's DS work urgently — if it's weaker than expected, reset now.\n"
                ">:warning: Matan feeling excluded is a real cultural issue. One invite to the next planning cycle fixes this — don't let it fester."
            )
        }
    },
    {"type": "divider"},

    # ── CLOSING ───────────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                ":star2: *Today in one sentence:* You locked the Boost launch timeline, built the"
                " marketplace experiment framework, and committed to finally writing down the"
                " vision your team has been waiting for — all in one day.\n\n"
                "_That's the kind of PM day that compounds. Go rest. Tomorrow's got a lot"
                " riding on it. :muscle:_"
            )
        }
    }
]

PAYLOAD = {
    "channel": CHANNEL,
    "blocks": BLOCKS,
    "text": "Chief of Staff Daily Summary — May 12, 2026"
}


def preview():
    print("\n===== SLACK MESSAGE PREVIEW =====\n")
    for block in BLOCKS:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(("-" * 60 + "\n").encode("utf-8", errors="replace"))
    print("=================================\n")


def send():
    token = (
        os.environ.get("SLACK_TOKEN")
        or os.environ.get("SLACK_BOT_TOKEN")
        or os.environ.get("SLACK_API_TOKEN")
    )
    if not token:
        print("[INFO] No Slack token found. Printing preview instead.\n")
        print("[HINT] Add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets\n")
        preview()
        return

    data = json.dumps(PAYLOAD).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}  ts={body.get('ts')}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                preview()
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        preview()


if __name__ == "__main__":
    send()
