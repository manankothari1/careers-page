#!/usr/bin/env python3
"""Daily PM digest for Manan Kothari — Wed Sep 2, 2026"""
import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN") or ""

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Briefing — Wed Sep 2",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! One meeting today — and it was a *meaty* one. You ran the Product/Marketing/Sales sync and surfaced real signal on where the intent experiment is and where it's going. Strong facilitation today — you kept the room grounded on learnings *and* moved decisively to the next chapter. Here's everything you need to know."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:calendar: Meeting Today*\n*Product / Marketing / Sales* — 1:00 PM PDT\n_Attendees: Manan, Zane Williams, Matan Chen Zion, Sean Gohman, Jon Wanczyk, Bobby Sladek_"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:dart: KEY DECISIONS MADE TODAY*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Departures = next intent signal (starts Monday)*\nYou called it: overtime is too broad. Switching to net departures by EOW. Sales gets scripts + data *Friday*. Outreach kicks off Monday.\n_Why:_ Departures signal a clear roster gap — the framing is simple ('you have a gap, let us fill it') and doesn't require the customer to feel surprised. Termination reason doesn't matter; what matters is the open role.\n_Signal definition:_ Net departures (e.g. fired 7, hired 3 = net gap of 4)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. Overtime ICP is narrower than expected — calibration needed*\nCustomers who converted to trial were those *caught off-guard* by overtime — they had no ready excuse. The majority either (a) deliberately pay overtime as a seasonal retention strategy or (b) are seasonally adjusting. This signal doesn't work broadly.\n_Why:_ You'll cap overtime signal by employee count going forward to filter out false positives (e.g. $11K overtime with 5 employees likely = multi-manager setup, not real signal).\n_Overtime signal stats so far:_ ~150 in list → 24-25 connected → 12 opportunities → 6 trials"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. Happy Homebase customers = highest intent proxy*\nPayroll users in particular are significantly easier to reach and convert. They're already in the habit of taking calls, and they have full overtime clarity in their data.\n_Why:_ Cross-product engagement signals both trust in Homebase and data richness. This should be a filter layer on top of every intent signal going forward."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Walk-in culture is a real product adoption barrier — reframe decided*\nRoughly 10%+ of prospects rely on walk-ins/referrals. QR code + screener has high drop-off and habits are hard to break. The agreed reframe for sales: *Homebase doesn't stop at applicant flow.* Even walk-in hires benefit from screener summaries, scheduling, and candidate profiles.\n_Why:_ This matters because you literally just saw it work — a walk-in QR-code hire who was flagged as a top match on the platform. That's the story to tell."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. 'Get to no quickly' principle adopted for walk-in-first customers*\nCustomers firmly entrenched in walk-in hiring are not worth extended sales time. The call: probe with curiosity, and if they're not willing to change their process even a little, qualify them out fast.\n_Why:_ Monthly recurring revenue, not one-off trials. Seasonal or habit-first customers churn quickly and aren't worth the spend."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. Power user analysis to be shared with sales team*\nYou're going to share your analysis of conversations with customers who *love* the product. All of them started with Indeed/in-person resumes and can't go back once they're in.\n_Why:_ Gives reps a concrete picture of what success looks like and which early signals predict a lasting customer — vs. a customer who'll try for a month and leave."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Josh's payroll caller-ID widget being explored for hiring outreach*\nHis caller ID + callback-request widget has meaningfully increased connect rates for the payroll team. It's being evaluated for hiring sales motion.\n_Why:_ If connect rate is the bottleneck for the intent signal experiment (it is — 24 connects out of 150), even a modest lift here dramatically changes the math."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. New location + no team = future intent signal candidate*\nBobby flagged this one: location added, manager added, but zero active team members after some period of time. Strong indicator of opening a new door and needing to staff up.\n_Why:_ Hiring intent is baked in — they haven't staffed the location yet. Worth queuing for a future experiment."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:white_check_mark: YOUR ACTION ITEMS (from today)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: *[DUE FRIDAY — THIS WEEK] Finalize departures signal: conflict docs + data to sales team*\nSales begins outreach Monday. Signal = net departures. Get Zane, Sean, Jon, Bobby what they need by EOD Friday."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *[THIS WEEK] Share power user conversation analysis with sales team*\nCustomers who love the product all started with Indeed/in-person. This context will help reps sell with confidence and disqualify faster."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *[THIS WEEK] Verify in-product termination trigger + hiring prompt*\nAn experiment was run previously — unclear if it's still active or generating volume. Check with eng and report back. If dead, worth reviving as part of real-time departures signal."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":large_yellow_circle: *[ONGOING] Pull overtime cohort data cuts*\n(a) What was the overtime threshold for customers who started a trial?\n(b) Is there a correlation between payroll product usage and call pickup / conversion rate?"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:rotating_light: CRITICAL WATCH LIST (still burning)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":fire: *Indeed Feed SUSPENDED — Day 9* — Package fraud evidence with Divij → send to Jessica Kanaskie. This is the single most important unblocking action right now.\n\n:fire: *EarnIn sample feed — OVERDUE (was Aug 31)* — jon.salzberg@earnin.com. Confirm sent. If not, send today.\n\n:large_yellow_circle: *Role Normalization PRD — DUE TODAY (Divij + Sina)* — Sep 3 EOD. Did they deliver? Follow up.\n\n:large_yellow_circle: *IBK JD A/B experiment* — 2+ weeks running. OVERDUE to pull signal before JD V2 rolls out.\n\n:large_yellow_circle: *OTP copy update (Iszael)* — Expand to free-tier users. Login email = verification email is solved. Copy: 'new verification step to improve feed quality.'\n\n:large_yellow_circle: *Roadmap prompt update* — Due EOW (Friday Sep 4).\n\n:large_yellow_circle: *Linear tickets: recency + distance experiments* — Create them. Unblocks Divij.\n\n:large_yellow_circle: *Divij CSV format spec for Iterable* — Blocking experiment coding.\n\n:large_yellow_circle: *Fadi OEM attribute study* — Due tomorrow Sep 4."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*:bulb: MANAN'S STRATEGIC READ TODAY*\n\nToday's meeting was really useful signal-sharpening. The intent signal program is working — but you're doing the right thing by *not* over-indexing on a single signal. The overtime → departures pivot is smart: departures are more actionable, the framing is cleaner, and there's less ambiguity in what the customer needs.\n\nThe biggest unlock hiding in plain sight: *payroll users.* If they're connected to payroll, they answer the phone, they trust Homebase, and they see their overtime clearly. Every future intent experiment should layer in product engagement as a filter — it's probably your single best predictor of conversion right now.\n\nThe walk-in culture conversation was important to have openly with the sales team. The QR code reframe is good, but the real win is repositioning Homebase as a full-cycle hiring operating system — not just an applicant source. You made that case clearly today. Make sure it's in the power user doc.\n\nToday grade: *A-* — great facilitation, clear decisions, decisive next steps. Carry that energy into Friday deliverables."
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff bot | Daily digest for Manan Kothari, PM @ Homebase | Sep 2, 2026"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "text": "Chief of Staff Daily Briefing — Wed Sep 2 | Decisions, action items & watch list",
    "blocks": blocks
}

def preview():
    lines = []
    lines.append("=== SLACK MESSAGE PREVIEW (no token) ===")
    lines.append(f"TO: {CHANNEL}")
    lines.append("")
    for b in blocks:
        t = b.get("type", "")
        if t == "header":
            lines.append("[ HEADER ] " + b["text"]["text"])
        elif t == "section":
            txt = b.get("text", {}).get("text", "")
            lines.append(txt)
            lines.append("")
        elif t == "divider":
            lines.append("---")
        elif t == "context":
            for el in b.get("elements", []):
                lines.append("  " + el.get("text", ""))
    lines.append("=== END PREVIEW ===")
    out = "\n".join(lines)
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")

if not TOKEN:
    print("No SLACK_TOKEN found — printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {TOKEN}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        print(f"Slack message sent successfully! ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        preview()
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    preview()
    sys.exit(1)
