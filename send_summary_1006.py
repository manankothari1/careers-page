#!/usr/bin/env python3
"""Chief of Staff daily digest — Oct 6 PDT (2 meetings captured)."""

import json, os, sys, urllib.request, urllib.error

CHANNEL = "D06E4QMHCNN"
TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
)


def slack_text(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "\U0001f4cb Chief of Staff Daily Digest — Tuesday Oct 6",
            "emoji": True,
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day Grade: A-* \u2b50\n"
                "*Theme:* Q4 ROADMAP STRESS-TESTED WITH EPDD \u00b7 "
                "SCHEDULING CRISIS ESCALATED \u00b7 "
                "COMMS PLATFORM LOCKED \u00b7 "
                "ORCA = NEW EXECUTION ENGINE\n\n"
                "_2 meetings captured today: (1) Q4 Risks, Dependencies & Scope — 9am EDT "
                "(Manan, Fadi, Jatin, Divij, IBK, Malcolm, Bob G, Soheil, Sina, Tiger, Carlo, Skye); "
                "(2) Hiring Comms — 2:30pm EDT (Manan, Matan, Fadi, Skye)_"
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u2705 KEY DECISIONS MADE TODAY*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. AI Screener toggle: Decoupling is NON-TRIVIAL \u2192 Default = turn both off*\n"
                "> *Why:* The entire job flow is built as a single pipeline. Supporting permutations "
                "(screener off + deal breakers on, etc.) requires significant backend re-architecture. "
                "Skye challenged: 'Deal breakers ARE screening questions.' If decoupling is infeasible, "
                "the cleanest path is to disable both together. If easy to decouple, we can offer "
                "one without the other.\n"
                "> *Rationale:* AI screener is the #2 reason customers DON'T convert "
                "(line cook example: AI perception hurts certain verticals). But it's the #1 "
                "reason customers DO convert for other segments. Giving OEMs the steering wheel = unlock.\n"
                "> *Action:* Manan + Divij to formally assess decoupling feasibility before "
                "deciding implementation path. Loop Fadi in on design before building."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. Nylas \u2192 Build in-house Google Calendar OAuth app with Orca* \u26a0\ufe0f ESCALATED\n"
                "> *Why:* Scheduling is fundamentally broken. Root cause still not fully defined. "
                "Bob confirmed Nylas has documented limitations — specific Google Cal actions "
                "don't sync back to Nylas. Multiple hacks in place. Auto-scheduling vs. "
                "non-auto switching has 'weird behavior.' "
                "Skye: 'We pay Nylas $8K/month. If Orca can build a Google OAuth app, let's do it.'\n"
                "> *Rationale:* Owning calendar infra = differentiated scheduling features + "
                "no more vendor limitations. Skye has personally built a Google OAuth app before. "
                "Not a hard build.\n"
                "> *Action:* Jatin to spike a 30-min feasibility session. Soheil is the lead candidate "
                "to build it. If Nylas can't support what we need, replacing it is Q4-worthy."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. 'Move Forward' label \u2192 Ship iteration 1 ASAP*\n"
                "> *Why:* It's a pure label change. Logic exists on the backend already. "
                "Fadi may have already started.\n"
                "> *Rationale:* 'Move Forward' means 2 different things depending on context. "
                "Relabeling to reflect the actual action (Schedule Interview / Add to Team) "
                "removes confusion at zero engineering cost.\n"
                "> *Action:* Fadi to ship v1 copy update this week. "
                "Iteration 2 (custom multi-round interview process setup) = Q1 candidate."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Match Explanation V1 \u2192 UNBLOCKED, proceed now*\n"
                "> *Why:* Skye + Bob (DS) confirmed: backend already has 0-1 competency "
                "scores per screener question (low/medium/high). We just don't show them.\n"
                "> *Rationale:* Simplest path = expose existing screener competency scores + "
                "inputs as the explanation. No new DS work required. Current logic "
                "(resume, screener, deal breakers) is explainable today. Bob added: "
                "introduce weighted deal breakers (non-negotiable vs. preferred) to give "
                "OEMs more nuanced candidate controls.\n"
                "> *Action:* Unblock design session with Vaddy. Bob: note that as matching "
                "algo evolves, match explanations need to reflect the algo at time of match (versioning risk)."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Instant Approval fallback confirmed*\n"
                "> *Why:* Instant approval requires revisiting syndication logic (fraud heuristics). "
                "Risk of higher false positive rate during transition.\n"
                "> *Decision:* Higher false positive rate acceptable in exchange for speed. "
                "Stopgap if instant approval stalls: defer free trial clock start to "
                "POST first-job-approval (every OEM gets 30 full days on a live, approved job).\n"
                "> *Action:* Malcolm to document the stopgap option for Manan + Skye review."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Hiring Comms: Iterable remains the direction* (confirmed by Skye)\n"
                "> *Why:* Engineering dependency exists on both SendGrid AND Iterable, "
                "but Iterable gives long-term autonomy — no-eng trigger management, "
                "better analytics UX, proper suppression/throttle controls. "
                "Marketing ops hire incoming to build proper process.\n"
                "> *Decisions:*\n"
                "> \u2022 Don't wait for Alvin/Fergus new SendGrid design system (~next month ETA). "
                "Use existing designs for new Iterable emails now; update once design system is final.\n"
                "> \u2022 Matan to pilot Orca on 1-2 emails (one kill in SendGrid, one create in Iterable) "
                "before scaling.\n"
                "> \u2022 State of the comms stack: 52 active touchpoints \u2192 42 after 12 kills, "
                "+18 new being added. Journey map doc = new source of truth.\n"
                "> *Action:* Fadi to loop Matan into Fergus (design-base lead) for design alignment. "
                "IBK to investigate Iterable MCP for Orca. Matan + Manan 1:1 Thursday to review Orca pilot plan."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f KEY RISKS SURFACED TODAY*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *Zero-state page data gap:* Carlo + others pushed back on priority of "
                "items 1.1/1.3 (first-screen drop-off). 70% of droppers say they're 'just exploring' — "
                "but is that a signal to serve a better experience or just natural curiosity? "
                "*Pull ZSP vs. drive-off-the-lot experiment data before finalizing priority.*\n\n"
                "\u2022 *Job creation flow is becoming unwieldy:* Fadi flagged clearly — adding "
                "intent capture (headcount/urgency), below-min-wage blocking, deal breaker toggle, "
                "screener toggle = too much friction in one flow. Risk of bloat eroding the "
                "low-friction thesis we shipped 9 months ago. *Needs dedicated quick-fix-vs-rethink session.*\n\n"
                "\u2022 *Geofencing compliance is technically hard:* State/city/county-level laws "
                "(AI disclosure, wage requirements) require ability to geofence job posts. "
                "Skye flagged: Kavon's min-wage work is the closest reference point. "
                "This is a real body of work for Q4 compliance.\n\n"
                "\u2022 *Matching algo versioning:* As the matching algorithm evolves quarter-to-quarter, "
                "match explanations shown to OEMs could become stale or misleading. "
                "Bob flagged: needs versioning consideration in Match Explanation V1 design.\n\n"
                "\u2022 *Screener felony language removal:* Skye flagged ~0.2% of job posts "
                "contain felony-related language that needs to be removed/gated for compliance. "
                "Small lift but legally necessary. Add to Q4 compliance bucket."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u23f0 IMMEDIATE ACTION ITEMS (next 24-48 hrs)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "1\ufe0f\u20e3 *RACHEL Q4/Q1/Q2 UX VIEW \u2014 DUE TOMORROW OCT 7* \u2014 "
                "Q4 is now fully stress-tested after today. Send tonight or first thing "
                "tomorrow morning. Do not let this slip.\n\n"
                "2\ufe0f\u20e3 *T-shirt sizing exercise \u2014 end of week (Oct 9-10)* \u2014 "
                "Jatin is scheduling. Manan, Fadi, Skye to synthesize FigJam notes + risks first. "
                "This determines the actual Q4 sprint plan.\n\n"
                "3\ufe0f\u20e3 *Matan 1:1 Thursday \u2014 Orca pilot + Iterable path decision* \u2014 "
                "Come in with a specific 1-2 email test case ready (one SendGrid kill, "
                "one Iterable create) to pilot Orca's capabilities.\n\n"
                "4\ufe0f\u20e3 *Pull ZSP vs. drive-off-the-lot experiment data* \u2014 "
                "Carlo and others need to see it before the t-shirt sizing session. "
                "Assign to Divij or pull yourself from Omni.\n\n"
                "5\ufe0f\u20e3 *Jatin: Brief Manan + Skye on billing team's pricing/packaging work* \u2014 "
                "Something was already built. Need to know if it's usable or throwaway "
                "before committing Q4 cycles to pricing changes.\n\n"
                "6\ufe0f\u20e3 *IBK: Investigate Iterable MCP for Orca* \u2014 "
                "If Iterable has an MCP, Matan becomes self-sufficient on email management. "
                "High leverage, low effort to check."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f6a8 STILL OPEN \u2014 WATCH LIST (top items)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\u2022 *INDEED FEED \u2014 DAY 44.* \U0001f6a8 Fraud evidence package sent to "
                "Jessica Kanaskie. 2-3 week review. A gentle ping is overdue by weeks. Do it today.\n\n"
                "\u2022 *FACEBOOK API \u2014 DAY 13.* All calls still failing. "
                "Bob + IBK leading. No update today. Flag if this isn't resolved by end of week.\n\n"
                "\u2022 *3-YEAR VISION ONE-PAGER \u2014 OVERDUE.* "
                "Assigned by John. Board meeting ~Oct 15-22. You're in Spain. Draft is due NOW.\n\n"
                "\u2022 *DUNNING BUG \u2014 UNDER INVESTIGATION.* "
                "Skye + Dipesh. Failed-card churned customers not re-added as hiring customers. "
                "~50% willingness to pay. Real revenue leak. Follow up on Dipesh call outcome.\n\n"
                "\u2022 *ANNUAL PLAN AUTO-RENEWAL \u2014 NOT BUILT.* "
                "Jatin pulling doc to confirm first renewals (~June 2027). Still pending. "
                "This is a time bomb if not escalated to billing soon.\n\n"
                "\u2022 *CARLO KT \u2014 URGENT.* Paternity leave Oct-Feb. "
                "You're in Spain. Largest knowledge risk on the team. Schedule async KT this week.\n\n"
                "\u2022 *OKR DRAFT.* Was due EOD Sep 29. Status still unknown. Confirm sent to Fadi.\n\n"
                "\u2022 *GIFT CARDS:* Lola E. Erickson ($50), Michele Landry ($50), "
                "Ryan Reilly ($50 possibly missed). Still owed."
            ),
        },
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "\U0001f30d *Spain Day 5 in the books, Manan.* "
                "Two back-to-back high-stakes sessions and you crushed it \u2014 "
                "walked into a roomful of engineers with sharp takes and held the line on priorities "
                "while staying genuinely open to data. The Nylas escalation alone could save the team "
                "months of scheduling firefights. And Matan's comms audit is the kind of "
                "unglamorous-but-critical work that makes Q4 actually shippable. "
                "\u2615 Keep those espresso shots coming. You're making it look easy from Valencia."
            ),
        },
    },
]

fallback_text = "Chief of Staff Daily Digest - Oct 6: Q4 stress-tested, Nylas escalated, Iterable locked, Orca = new execution engine."


def preview():
    sys.stdout.buffer.write(
        "\n=== SLACK DIGEST PREVIEW ===\n".encode("utf-8", errors="replace")
    )
    for b in blocks:
        if b.get("type") == "section":
            t = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write((t + "\n\n").encode("utf-8", errors="replace"))
        elif b.get("type") == "header":
            t = b.get("text", {}).get("text", "")
            sys.stdout.buffer.write(
                ("=== " + t + " ===\n\n").encode("utf-8", errors="replace")
            )
        elif b.get("type") == "divider":
            sys.stdout.buffer.write(
                "---\n".encode("utf-8", errors="replace")
            )


def send():
    payload = json.dumps(
        {
            "channel": CHANNEL,
            "text": fallback_text,
            "blocks": blocks,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("Slack message sent successfully!")
                print(f"  ts={body.get('ts')}  channel={body.get('channel')}")
            else:
                print(f"Slack API error: {body.get('error')}")
                print(json.dumps(body, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: {e.read().decode('utf-8', errors='replace')}")
    except Exception as ex:
        print(f"Error: {ex}")


if TOKEN:
    send()
else:
    print("No SLACK_TOKEN found — preview only.")
    preview()
