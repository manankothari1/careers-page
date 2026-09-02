#!/usr/bin/env python3
"""Daily chief-of-staff digest for Manan Kothari — Sep 1, 2026 (Tuesday PDT)."""

import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌆 Your End-of-Day Brief — Tuesday, Sep 1",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Theme of the day:* Sprint locked, Talent Pool experiment architecture crystallized, "
                "Indeed recovery narrative taking shape — and JD V2 is closer to the launchpad than you think.\n\n"
                "Two meetings today: *Sprint Planning (continued)* at 11am and *Hiring DS Weekly* at 1:15pm. "
                "Dense, high-signal sessions. Here's what you decided and what you need to do about it."
            ),
        },
    },
    {"type": "divider"},
    # ── DECISIONS ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📌 Decisions Made Today*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*1. JobCase + EarnIn XML integrations — GREENLIT ✅*\n"
                "Same pattern as existing feeds (JobGet, Telru, Appcast). Start small: ~100 jobs organic, "
                "30–50 paid per integration. EarnIn CPC = 7–10¢ vs. $1+ for ZipRecruiter — extraordinary unit economics. "
                "JobCase = 120M registered / 30M monthly actives, heavy retail + food service. "
                "_Why it matters:_ diversifies away from Indeed dependency while feed is under review. "
                "_Front-end work needed:_ surface source attribution (e.g. 'applied via JobCase')."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*2. OTP expansion scope — RESOLVED ✅*\n"
                "OTP will expand to free-tier existing users. Paying customers (subscription, hiring, payroll) are exempt. "
                "*The key blocker is now unblocked:* OTP sends to _login email_, not business-profile email — "
                "which means existing users can be verified without the mismatch risk Stitch raised. "
                "Copy must feel universal, not new-user-specific. Iszael's framing: "
                '"new verification step to improve feed quality." This is the right message for the moment.'
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*3. JD V2 — ready to ship without eng work ✅*\n"
                "Formatting cleanup is purely prompt-side. Rami ships once finalized. "
                "Rollout plan: *2–3% first* to validate pipeline + dashboard, then full 50/50 experiment. "
                "~12–14 of 20 generated JDs are already good; remaining need explicit constraints in the prompt. "
                "Rami will write a V1→V2 one-pager for the record. "
                "Note: Tanner's last day was today — experiment setup (50/50 split) is reportedly done."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*4. Deprioritized this sprint — locked 🔒*\n"
                "• *Indeed D3 source claim applicants:* trial flow needs validation before expanding — correct call, don't rush it.\n"
                "• *'Show jobs live' email:* ~1 week of work when picked up; hasn't been active in a long time. Safe to defer."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*5. Talent Pool experiment architecture — finalized ✅*\n"
                "Three active streams:\n"
                "  1️⃣ *Email format:* test recruiter-style WITH Homebase graphic (prior data: recruiter = higher opens, generic = higher CTR → hybrid test is the logical next step)\n"
                "  2️⃣ *Activity recency + distance filtering* — prioritized first; 90-day window yields ~2K, unrestricted = ~100K, so window calibration matters\n"
                "  3️⃣ *Cash-out churned users* — queries exist, code not yet written\n\n"
                "New additions:\n"
                "• *Opt-in at screener end:* 'Would you like to receive additional jobs in this area?' + social proof framing — covers Indeed/Zip applicants who lack opt-in today\n"
                "• *Candidate redistribution guardrail:* only share with other businesses _after_ original role is filled or applicant rejected — important trust protection"
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*6. Role normalization — path to production scoped ✅*\n"
                "Agent exists but not deployed. Main bottleneck: ~30K token prompt with embedded lookup tables. "
                "Fix: externalize tables to CSV/JSON. *No net-new architectural pattern* — no eng blockers from product side. "
                "Divij + Sina drafting PRD. *Due: Thu Sep 3 EOD* — so they can feed into Sprint Planning."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*7. Indeed recovery — narrative taking shape ✅*\n"
                "Corporate email req = dropped. Source claiming pilot = incoming (a few weeks). "
                "Indeed considering letting Homebase *pay for sponsorship on behalf of customers* — "
                "that would be a significant unlock if it materializes. "
                "Proactively packaging fraud evidence (cleanup + improved agent score + OTP) will expedite "
                "removal from heightened review. This is the right play."
            ),
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*8. You acknowledged being a bottleneck — and made a plan ✅*\n"
                "Working with Marty + Sky to offload lower-priority items. "
                "This is exactly the right move at this stage of sprint. "
                "The team can see you're self-aware and moving on it — that matters."
            ),
        },
    },
    {"type": "divider"},
    # ── YOUR ACTION ITEMS ─────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✅ Your Action Items (Manan-owned)*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "1. *Create Linear tickets: activity recency + distance experiments* — "
                "Divij needs a clean handoff base from Rami. Document both experiments clearly. Do this tonight or first thing tomorrow.\n\n"
                "2. *Send Divij the CSV format spec for Iterable experiment output* — "
                "He can't start coding without it. This is blocking the stream-2 experiment.\n\n"
                "3. *Review + sign off on IBK's OTP thread* — "
                "Thread already started. Your input is the unlock. Don't let this sit another day.\n\n"
                "4. *Align with Darren (lifecycle/marketing) on Iterable pipeline params* — "
                "Marketing is cautious about domain authority. Need agreed parameters before talent pool emails can scale.\n\n"
                "5. *Package fraud improvement evidence for Indeed (with Divij)* — "
                "Combine: fraudulent company cleanup + fraud agent score improvements (Paria + Divij) + OTP rollout. "
                "Send to Jessica Kanaskie (jkanaskie@indeed.com). This directly accelerates feed restoration."
            ),
        },
    },
    {"type": "divider"},
    # ── OVERDUE ──────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 Overdue — Don't Let These Slip*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "🔴 *EarnIn sample feed → Jon Salzberg (jon.salzberg@earnin.com)* — was due Aug 31 EOD. "
                "Did this go out? If not, send it NOW. You just greenlit EarnIn as a distribution channel today — "
                "don't let the relationship go cold before the first deliverable lands.\n\n"
                "🔴 *Tanner's onboarding doc* — his last day was TODAY (Sep 1). "
                "Yes, you missed the window for onboarding. But a thoughtful parting note + handoff doc is still worth sending. "
                "It closes the loop for the team and for Tanner.\n\n"
                "🟠 *JD A/B experiment signal (IBK)* — 2+ weeks running. Pull the signal. "
                "Rami is literally about to ship V2 and you haven't closed out V1 learnings yet. "
                "Do this before V2 rolls out.\n\n"
                "🟠 *Fadi OEM attribute study check-in* — due Sep 4 (Thursday, two days). "
                "Make sure Fadi isn't blocked. Quick async ping is enough.\n\n"
                "🟡 *Roadmap prompt update* — due EOW (Friday Sep 4). Larger 'Now' section + color by function. "
                "Don't let this slip to next week."
            ),
        },
    },
    {"type": "divider"},
    # ── WATCH LIST ────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👀 Keep on Radar*",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *Role normalization PRD* (Divij + Sina) due *Thu Sep 3 EOD* — this feeds into next sprint planning\n"
                "• *Rami's V1→V2 one-pager* — needs to be written before he transitions to Marketing\n"
                "• *422 publishing errors* — Day 52, 146 locations. Jatin on RCA. Chase status.\n"
                "• *Matan's bi-weekly PM/Sales sync* — started today (Sep 1). Check in on how it went.\n"
                "• *Sky's GitHub access + homebase-context git clone command* — did this happen?\n"
                "• *Source claiming pilot timeline* — Jessica said 2–3 weeks. Clock started Aug 31.\n"
                "• *Marina / Mundo Academy* — follow up ~Sep 10"
            ),
        },
    },
    {"type": "divider"},
    # ── CLOSER ───────────────────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Day grade: B+*\n\n"
                "You made real structural progress today — JobCase + EarnIn greenlit, OTP expansion unblocked, "
                "Talent Pool experiment streams crystallized, Indeed recovery narrative is coalescing. "
                "The sprint has shape. The team is moving.\n\n"
                "What's holding this back from an A: EarnIn feed is overdue, Tanner never got his doc, "
                "and JD A/B signal is still sitting. None of those are hard — they just need an hour of focus. "
                "Tomorrow morning, knock out the EarnIn email first, then close the IBK OTP thread. "
                "Everything else will fall into place.\n\n"
                "_You're doing great work, Manan. The momentum is real._ 💪"
            ),
        },
    },
]

payload = {
    "channel": CHANNEL,
    "text": "Your End-of-Day Brief — Tuesday Sep 1 🌆",
    "blocks": blocks,
}


def preview():
    sys.stdout.buffer.write(
        ("\n=== SLACK PREVIEW (no token) ===\n" + json.dumps(payload, indent=2) + "\n").encode(
            "utf-8", errors="replace"
        )
    )


def send(token):
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
                print(f"✅ Slack message sent! ts={body.get('ts')}")
            else:
                print(f"❌ Slack API error: {body.get('error')}")
                preview()
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        preview()


token = os.environ.get("SLACK_TOKEN") or os.environ.get("SLACK_BOT_TOKEN") or os.environ.get("SLACK_API_TOKEN")
if token:
    send(token)
else:
    print("⚠️  No SLACK_TOKEN found — printing preview only.")
    preview()
