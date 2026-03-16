#!/usr/bin/env python3
"""
Chief of Staff Daily Summary
Sends Manan's end-of-day decision digest to Slack.
Runs at midnight UTC (5pm PT) via cron: 0 0 * * *
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone


SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_API_URL = "https://slack.com/api/chat.postMessage"


def send_slack_message(token: str, channel: str, blocks: list, text: str) -> bool:
    payload = json.dumps({
        "channel": channel,
        "text": text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        SLACK_API_URL,
        data=payload,
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
                print("✅ Slack message sent successfully.")
                return True
            else:
                print(f"❌ Slack API error: {body.get('error', 'unknown')}")
                return False
    except urllib.error.URLError as e:
        print(f"❌ Network error sending Slack message: {e}")
        return False


def text_block(text: str) -> dict:
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}


def divider() -> dict:
    return {"type": "divider"}


def header_block(text: str) -> dict:
    return {"type": "header", "text": {"type": "plain_text", "text": text, "emoji": True}}


def build_no_meetings_message(is_weekend: bool, date_str: str) -> tuple[list, str]:
    if is_weekend:
        fallback = f"Rest up, Manan! No meetings recorded for {date_str}. Big week ahead."
        blocks = [
            header_block("Weekend Wrap-Up"),
            text_block(
                f"Hey Manan! No meetings recorded for *{date_str}* — and that's a *good* thing. "
                f"Recharge, because next week is going to be big. 💪\n\n"
                f"Here's what's queued up for the week ahead:\n"
                f"• *Deal Breakers sign-off* — Wednesday\n"
                f"• *Malcolm:* One-click posting target — Friday\n"
                f"• *Andrew:* \"Show the work\" feature target — Friday\n"
                f"• *Tanner:* Port job page (week 1 of sprint)\n"
                f"• *IBK:* Interview availability (full sprint)\n"
                f"• *Cindy:* Zero state page experiments rolling\n"
                f"• *Nelson + Manan:* Syndication speed metric to add\n\n"
                f"You've got this. See you Monday! 🙌"
            ),
        ]
    else:
        fallback = f"No meetings captured in Granola for {date_str}. Here's your offsite prep summary."
        blocks = [
            header_block(f"Daily Digest — {date_str}"),
            text_block(
                f"Hey Manan! No meetings were captured in Granola for *{date_str}* — "
                f"likely a big in-person day at the SF offsite with conversations happening live. "
                f"Here's your carry-forward brief from last Friday so you walk into tomorrow fully armed. 🚀"
            ),
        ]
    return blocks, fallback


def build_mar16_offsite_message(date_str: str) -> tuple[list, str]:
    """
    Special message for Mon Mar 16 — SF offsite Day 1.
    No Granola meetings recorded today; synthesizing from Mar 13 sessions.
    """
    fallback = "SF Offsite Day 1 — Daily Digest & Carry-Forward Brief for Manan"

    blocks = [
        header_block(f"Daily Digest — {date_str} | SF Offsite: Day 1 🌉"),
        text_block(
            "Hey Manan! Welcome to San Francisco — no Granola meetings captured today "
            "(makes sense for a travel + offsite kickoff day!). Here's your *full carry-forward "
            "brief* from last Friday's marathon session so you walk into tomorrow's roadmap work "
            "totally locked and loaded. You crushed a massive sprint-end week — the team is in "
            "great shape heading into the offsite. Let's go! 💪"
        ),
        divider(),

        # ── DECISIONS & KEY CONTEXT ──
        header_block("Key Decisions from Fri Mar 13"),

        text_block(
            "*1. Two priorities locked for the new sprint*\n"
            ">Decided to focus the hiring team's sprint on two things only: "
            "*applicant flow improvements* and *trial growth initiatives*. "
            "Everything else is secondary.\n"
            ">_Rationale:_ ARR is tracking ~3%/week; need to hit 5-6% to reach the ~$600K target. "
            "Top-of-funnel (trial conversion) is the biggest lever.\n"
            ">• *Action — Manan:* Come to Tuesday/Wednesday roadmap session with an exhaustive "
            "list of initiatives across trial flow, core product, and applicant flow. "
            "No rehashing — come prepared.\n"
            ">• *Action — Dana:* Same prep — exhaustive options list before roadmap session. "
            "Meet Manan at Dolores Park Mon afternoon after Dana lands (private convo)."
        ),

        text_block(
            "*2. Deal Breakers sign-off scheduled for Wednesday Mar 18*\n"
            ">Backend is dev-complete. Frontend wrapping early this week. "
            "Product/design sign-off is locked for *Wednesday*.\n"
            ">• *Action — Manan:* Block time Wednesday for Deal Breakers sign-off review. "
            "Confirm with Dana + team that FE is wrapped by EOD Tuesday."
        ),

        text_block(
            "*3. Appcast integration officially killed*\n"
            ">Decided to discontinue Appcast due to abysmal performance "
            "(1.4% conversion vs. 15-20% from other partners). Not worth maintaining.\n"
            ">• *Action — Manan + Andrew:* Coordinate cleanup of Appcast XML feed. "
            "Get it off the codebase this sprint."
        ),

        text_block(
            "*4. Demo screener ungating scoped as stretch goal*\n"
            ">Decided to explore making the demo screener publicly accessible (no login required) "
            "as a top-of-funnel unlock. Security grooming needed first.\n"
            ">• *Action — Dana, Izzy, Bob:* Scope the ungating work offline this week. "
            "Bring a groomed estimate back before sprint planning ends."
        ),

        text_block(
            "*5. V1 → V2 migration: Izzy owns it as a stretch goal*\n"
            ">Quick repost / migration milestone descoped from company page work but kept alive "
            "as Izzy's stretch goal this sprint.\n"
            ">• *Action — Manan:* Check in with Izzy early this week on confidence level "
            "and timeline. Don't let this slip to carryover again."
        ),

        text_block(
            "*6. Andrew becomes team Claude skills specialist*\n"
            ">Decided Andrew will go deep on Claude Code and present to the full EPD team "
            "before the next retro (April 10). Fadi and Dana looped in on implementation approach.\n"
            ">• *Action — Andrew:* Claude skills presentation to EPD by April 10.\n"
            ">• *Action — Manan:* Confirm Andrew has the runway/support to make this happen "
            "during the offsite — it's a real force multiplier for the whole team."
        ),

        text_block(
            "*7. Sprint carryover problem: 3 intervention points adopted*\n"
            ">Agreed the recurring carryover issue needs structural fixes at three stages: "
            "(1) crafting phase MVP scoping, (2) shaping meetings with eng input, "
            "(3) pre-grooming early callouts.\n"
            ">• *Action — Manan:* Use SF offsite to finalize the new process with the team. "
            "Get alignment on what 'dev-done by sprint end' actually requires from PM/design."
        ),

        text_block(
            "*8. Unit testing: Carlo leads FE coverage analysis*\n"
            ">The free trial mode incident (paid card showing in free mode) was traced to "
            "missing unit test coverage. Carlo is leading a frontend analysis to identify gaps.\n"
            ">• *Action — Carlo:* Deliver FE unit test coverage report + concrete project brief "
            "example to team. Jatin has the backend analysis done.\n"
            ">• *Action — Bob + Jatin:* Plan hiring public interface tech debt work."
        ),

        text_block(
            "*9. Jeff situation: Ray handling*\n"
            ">Jeff appears checked out / likely job searching. Ray will push hard on hiring "
            "commitment next week. Decision: don't reassign Jeff's work yet — let Ray manage "
            "the conversation first.\n"
            ">• *Action — Manan:* Stay in the loop with Ray on Jeff status. Be ready to "
            "re-scope if Ray's conversation doesn't land."
        ),

        text_block(
            "*10. New marketing lead joins at offsite*\n"
            ">Confirmed: new growth-focused marketing lead is meeting the team this week in SF. "
            "Will run both in-product and external touchpoint experiments.\n"
            ">• *Action — Manan:* Make sure to connect with the new marketing lead early "
            "in the offsite. Align on hiring team's top growth levers (careers page, "
            "zero state, V1→V2 upgrade flow) so they can hit the ground running."
        ),

        divider(),

        # ── WINS ──
        header_block("Wins to Celebrate 🏆"),
        text_block(
            "• *Andrew:* Indeed integration SHIPPED after a year-long effort. Huge.\n"
            "• *Google Calendar certification:* Big Mac, Andrew, Tanner, Ivy, Fadi — done.\n"
            "• *DoorDash POS integration:* Moving to real merchants in Milestone 1.\n"
            "• *Child labor law compliance* launching Monday at Scooters Grow Conference — "
            "600+ locations protected.\n"
            "• *Job page experiment:* Manan + Bob + Martin completed successfully.\n"
            "• *Top matches metric:* Up to 20% (key OKR). 📈"
        ),

        divider(),

        # ── TOP 5 TOMORROW ──
        header_block("Your Top 5 for Tomorrow (Tue Mar 17)"),
        text_block(
            "1. *Roadmap session prep:* Come with exhaustive initiative list — "
            "trial flow, applicant flow, core product.\n"
            "2. *Meet the new marketing lead:* Align on hiring team's top-of-funnel levers.\n"
            "3. *Deal Breakers:* Confirm FE is wrapping so Wed sign-off isn't at risk.\n"
            "4. *Demo screener ungating:* Nudge Dana + Izzy + Bob to have a scoping "
            "conversation today/tomorrow.\n"
            "5. *Sprint process:* Finalize the 3-intervention carryover fix with the team."
        ),

        divider(),
        text_block(
            "_You walked into this week having shipped Indeed (finally!), locked DoorDash, "
            "and kept ARR moving. The offsite is your moment to set the growth trajectory "
            "for Q2. The team is energized, the sun is out in SF, and you've done the work. "
            "Go make it count, Manan. 🙌_"
        ),
    ]

    return blocks, fallback


def build_message_from_granola_data(granola_data: list, date_str: str) -> tuple[list, str]:
    """Build Slack message from parsed Granola meeting data."""
    if not granola_data:
        return build_no_meetings_message(is_weekend=False, date_str=date_str)

    all_decisions = []
    all_action_items = []
    meeting_titles = []

    for meeting in granola_data:
        title = meeting.get("title", "Untitled Meeting")
        meeting_titles.append(title)
        decisions = meeting.get("decisions", [])
        for d in decisions:
            all_decisions.append({
                "meeting": title,
                "decision": d.get("decision", ""),
                "rationale": d.get("rationale", ""),
                "action_items": d.get("action_items", []),
            })
        for ai in meeting.get("action_items", []):
            all_action_items.append({"meeting": title, "item": ai})

    fallback = f"Daily Decision Digest — {date_str} | {len(granola_data)} meetings"

    blocks = [
        header_block(f"Daily Digest — {date_str}"),
        text_block(
            f"Hey Manan! Here's your end-of-day brief covering "
            f"*{len(granola_data)} meeting{'s' if len(granola_data) != 1 else ''}* today. "
            f"You made some solid calls — let's make sure nothing falls through the cracks. 💪"
        ),
        divider(),
        header_block("Decisions Made Today"),
    ]

    if all_decisions:
        for i, d in enumerate(all_decisions, 1):
            action_lines = ""
            if d["action_items"]:
                action_lines = "\n" + "\n".join(
                    f">• *Action:* {ai}" for ai in d["action_items"]
                )
            rationale_line = f"\n>_Why:_ {d['rationale']}" if d.get("rationale") else ""
            blocks.append(text_block(
                f"*{i}. {d['decision']}*\n"
                f">_From:_ {d['meeting']}"
                f"{rationale_line}"
                f"{action_lines}"
            ))
    else:
        blocks.append(text_block("No explicit decisions captured today — check the meeting notes for context."))

    if all_action_items:
        blocks.append(divider())
        blocks.append(header_block("Loose Action Items"))
        item_lines = "\n".join(f"• {ai['item']} _(from {ai['meeting']})_" for ai in all_action_items)
        blocks.append(text_block(item_lines))

    blocks.append(divider())
    blocks.append(text_block(
        "_Great work today, Manan. Rest up and keep shipping. 🙌_"
    ))

    return blocks, fallback


def main():
    token = os.environ.get("SLACK_TOKEN", "").strip()
    if not token:
        print(
            "❌ SLACK_TOKEN environment variable is not set.\n"
            "To fix this:\n"
            "  1. Go to Cursor Dashboard → Cloud Agents → Secrets\n"
            "  2. Add a secret named SLACK_TOKEN with your Slack Bot Token\n"
            "     (needs chat:write scope for channel D06E4QMHCNN)\n"
            "  3. Re-run this automation\n"
        )
        sys.exit(1)

    now_utc = datetime.now(timezone.utc)
    # Cron fires at midnight UTC = 5pm PT (end of business day)
    today_str = now_utc.strftime("%A, %B %-d, %Y")

    # Check for pre-built GRANOLA_DATA env var (set by run_daily_summary.py)
    granola_raw = os.environ.get("GRANOLA_DATA", "").strip()

    if granola_raw:
        try:
            granola_data = json.loads(granola_raw)
        except json.JSONDecodeError as e:
            print(f"⚠️  Could not parse GRANOLA_DATA JSON: {e}. Using no-meetings fallback.")
            granola_data = []
        blocks, fallback = build_message_from_granola_data(granola_data, today_str)
    else:
        # No GRANOLA_DATA passed — use date-aware special handling
        # Mar 16 = SF offsite Day 1
        date_today = now_utc.strftime("%Y-%m-%d")
        is_weekend = now_utc.weekday() >= 5  # Saturday=5, Sunday=6

        if date_today == "2026-03-16":
            blocks, fallback = build_mar16_offsite_message(today_str)
        elif is_weekend:
            blocks, fallback = build_no_meetings_message(is_weekend=True, date_str=today_str)
        else:
            blocks, fallback = build_no_meetings_message(is_weekend=False, date_str=today_str)

    success = send_slack_message(token, SLACK_CHANNEL, blocks, fallback)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
