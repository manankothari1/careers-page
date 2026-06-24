#!/usr/bin/env python3
"""Daily decision digest for Manan Kothari - Jun 23, 2026"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"
DATE_LABEL = "Tuesday, June 23"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f":briefcase: Chief of Staff Daily Digest \u2014 {DATE_LABEL}",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! :wave: What a productive Tuesday \u2014 two solid meetings, some big pivots, and real decisions made. You're moving fast and making the right calls. Here's your end-of-day breakdown."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Meetings Today*\n1\ufe0f\u20e3 *Hiring Leads Standup* \u2014 8:45 AM (Fadi, Dana, Usman, Ray, Nelson, Matan, Cindy, Bob, Jatin, Jeff)\n2\ufe0f\u20e3 *Matan / Manan 1:1* \u2014 3:30 PM"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":dart: *DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Outbound Calling: Pivot from Booking \u2192 Excitement Testing* :telephone_receiver:\n\n*What you decided:* Stop optimizing for getting people to book intake meetings. The new north star is testing whether the *value prop lands* \u2014 are people genuinely *excited* on the other end of the call? If yes, great. If no, that's also a win because now you know.\n\n*Why:* Listening to Usman's calls, people were agreeing to meetings but not showing real excitement. That signal is misleading. You need to know if 'hell yeah, I want this' is even achievable with this customer base before scaling.\n\n*Rationale:* Classic product-market fit test principle \u2014 maximize learnings over conversions at this stage. Smart pivot."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Action Items:*\n\u2022 :bust_in_silhouette: *Dana* \u2014 Share revised outbound script with Usman TODAY. Focus the script on surfacing excitement, not closing the meeting.\n\u2022 :bust_in_silhouette: *Usman* \u2014 Connect with Dana post-standup. Role-play the new script. Pull in a third team member if needed to hit *30\u201350 connections this week* (up from ~20).\n\u2022 :eyes: *You (Manan)* \u2014 Listen to call recordings this week. Are people excited? That's the only metric that matters right now."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Zero State Page: SHIPPED \u2014 Don't Block on Matan's Review* :rocket:\n\n*What you decided:* Ship the zero state page without waiting for Matan to review the copy. If he has feedback, he can iterate post-launch.\n\n*Why:* Matan had asked multiple times to review, but you correctly identified this was creating unnecessary friction. Dana and you felt confident in the value prop direction. Ship first, refine second.\n\n*Status:* :white_check_mark: LIVE \u2014 Fadi shipped it during standup."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Job Description + Salary + Role Recs: Manan Represents Design* :art:\n\n*What you decided:* You'll be the design representative in the meeting with Ray for the job description, salary, and role recommendations feature. You'll draft design options and hand off to Fadi for polish \u2014 same workflow used successfully for the pricing page.\n\n*Why:* Fadi is time-constrained this week (paper cuts to address, leaving next week). You have a strong enough sense of the design direction to unblock Ray without Fadi being in every meeting."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Action Items:*\n\u2022 :bust_in_silhouette: *You (Manan)* \u2014 Draft design options using cloud design with Homebase design system. Send to Fadi for polish.\n\u2022 :bust_in_silhouette: *Fadi* \u2014 Receive options from Manan, add polish, implement."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Add Location Modal: Drop the Illustration, Go Text-Only* :scissors:\n\n*What you decided:* The illustration on the add location modal should be dropped in favor of text-only. A minor UX improvement PR has already been pushed.\n\n*Why:* The illustration was adding visual noise without adding value. Clean text-only is faster to load, easier to localize, and just looks better. Small but meaningful product quality win.\n\n*Potential follow-up:* Add a link to a help center article explaining locations (low priority, not blocking)."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Dana Gets Repo Access (Both Homebase + Dotfiles)* :key:\n\n*What you decided:* Unblock Dana to push code changes independently. She needs access to both the Homebase repo and dotfiles repo.\n\n*Why:* You're pushing toward a world where every team member is their own 'single unit' that can ship independently. Dana already pushed the zero state page changes \u2014 give her the keys to do more."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Action Items:*\n\u2022 :bust_in_silhouette: *Dana* \u2014 File IT help desk request for access to *both* the Homebase repo and dotfiles repo.\n\u2022 :bust_in_silhouette: *Jatin* \u2014 Help Dana get set up once access is granted."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Nelson Transitions to Data Engineering (~5 hrs/week) by End of Month* :chart_with_upwards_trend:\n\n*What you decided:* Nelson shifts from daily staffed analyst to reactive data engineering support only. He will *not* proactively pull week-in-review or fill gaps \u2014 team to own analytics ops going forward.\n\n*Why:* The team has matured to the point where people can self-serve analytics. Nelson is needed in higher-leverage places across the org. This is a sign of success, not a downgrade.\n\n*What stays the same:* Nelson is still available for sanity-checking experiments (e.g., move-forward metric calculations for resume experiment). Just ping him with appropriate lead time."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: *Action Items:*\n\u2022 :bust_in_silhouette: *Nelson* \u2014 Syndicate before transitioning. Audit all ops/analytics ownership so nothing falls through the gap.\n\u2022 :bust_in_silhouette: *Team* \u2014 Own your analytics. If you need something from Nelson, proactively ping him (don't assume he'll pull it)."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Spec-Driven Dev: Team Owns Their Specs \u2014 With Human-Readable TLDRs* :memo:\n\n*What you decided:* In the move toward agents + engineers shipping from specs, the *citizen developer* (PM, ops, etc.) is responsible for their spec. Engineers can't be blamed if the spec is wrong. However, specs should include a human-readable summary highlighting the 2\u20133 key decisions \u2014 agents can generate TLDRs and surface questionable assumptions to prompt a back-and-forth with the human reviewer.\n\n*Why:* As you scale with AI-assisted development, the quality of inputs (specs) becomes the bottleneck. Specs with a clear TLDR reduce reviewer fatigue and ensure humans stay in the loop on the stuff that matters \u2014 without having to read 15 dense tickets a day."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":spiral_notepad: *OPEN ITEMS CARRIED FORWARD*\n\n\u2022 :red_circle: *Build Indeed source claiming playbook* \u2014 share with Usman, then hand off\n\u2022 :red_circle: *Evaluate job reactivation fix options* \u2014 V1 restore vs 30\u219260 day expiry vs customer-set close date\n\u2022 :large_yellow_circle: *QA + release: Purchase Homebase Boost + post-job creation boost* \u2014 both ready to ship\n\u2022 :large_yellow_circle: *Build Q3 OKR dashboard* \u2014 track weekly progress toward 80% healthy jobs\n\u2022 :large_yellow_circle: *ZipRecruiter follow-up call* \u2014 schedule 1\u20132 weeks out\n\u2022 :large_yellow_circle: *Investigate ICP overlap in talent pool*\n\u2022 :large_blue_circle: *Salesforce table requirements writeup* \u2014 you write, send to Nelson\n\u2022 :large_blue_circle: *Share Q3 strategy + roadmap docs with full team*"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":trophy: *Quick Wins Today*\n\u2022 Zero state page is LIVE \u2014 shipped it without overthinking it. :fire:\n\u2022 Called the pivot on outbound calling strategy before wasting another week on the wrong metric.\n\u2022 Unblocked Fadi by volunteering to own design representation in Ray's meeting.\n\u2022 Made the call on Nelson's transition \u2014 cleanly communicated, team didn't push back, sign of a healthy org."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Great day, Manan. You're running a tight ship. :anchor: See you tomorrow!"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "text": f"Chief of Staff Daily Digest \u2014 {DATE_LABEL}",
    "blocks": blocks
}


def preview():
    sys.stdout.buffer.write(
        ("\n=== SLACK PREVIEW ===\n" + json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8", errors="replace")
    )


def send(token: str):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    token = (
        os.environ.get("SLACK_TOKEN")
        or os.environ.get("SLACK_BOT_TOKEN")
        or os.environ.get("SLACK_API_TOKEN")
    )
    if token:
        send(token)
    else:
        print("[INFO] No Slack token found. Printing preview.\n"
              "[INFO] Add SLACK_TOKEN or SLACK_BOT_TOKEN secret in Cursor Dashboard > Cloud Agents > Secrets.")
        preview()
