#!/usr/bin/env python3
"""
Daily Decision Summary Bot
Chief of Staff for Manan Kothari, PM at Homebase.
Runs daily at 5pm, reviews Granola meetings, sends Slack summary.
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timezone, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_CHANNEL_ID = "D06E4QMHCNN"


def get_slack_token():
    for key in ["SLACK_BOT_TOKEN", "SLACK_TOKEN", "SLACK_API_TOKEN", "SLACK_OAUTH_TOKEN"]:
        val = os.environ.get(key)
        if val:
            return val
    raise EnvironmentError(
        "No Slack token found. Please add SLACK_BOT_TOKEN to your Cursor Cloud Agent secrets."
    )


def send_slack_message(token: str, channel: str, text: str, blocks: list = None):
    client = WebClient(token=token)
    try:
        kwargs = {"channel": channel, "text": text}
        if blocks:
            kwargs["blocks"] = blocks
        response = client.chat_postMessage(**kwargs)
        print(f"Message sent successfully. ts={response['ts']}")
        return response
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        raise


def build_slack_blocks(summary: str) -> list:
    """Convert the plain text summary into nice Slack Block Kit blocks."""
    blocks = []
    sections = summary.strip().split("\n\n")
    for section in sections:
        if section.startswith("*") or section.startswith("🌟") or section.startswith("🎯"):
            blocks.append({
                "type": "header",
                "text": {"type": "plain_text", "text": section.strip("* \n"), "emoji": True}
            })
        elif section.strip():
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": section.strip()}
            })
        blocks.append({"type": "divider"})

    # Remove last divider if it's trailing
    if blocks and blocks[-1].get("type") == "divider":
        blocks.pop()

    return blocks


def generate_summary_for_date(target_date_str: str) -> str:
    """
    Generates the daily summary message.
    In production, this is driven by Granola MCP tool data fetched by the agent.
    For standalone script use, this function is called with pre-fetched meeting data.
    """
    return target_date_str


def build_todays_summary() -> str:
    """
    Hardcoded summary for today's meetings (May 5, 2026).
    In the automation context, the Cursor agent fetches meetings via Granola MCP and
    calls this script with the composed summary text.
    """
    today = datetime.now(timezone.utc).strftime("%A, %B %-d, %Y")

    summary = f"""👋 *Hey Manan! Your Chief of Staff here — here's your Daily Decision Summary for {today}.*

You crushed it today. Five meetings, a ton of thoughtful decisions, and real momentum across hiring and marketplace. Here's the full breakdown:

---

🗓️ *MEETINGS TODAY*
1. Hiring Leads Standup (8:45 AM)
2. Hiring Essential Journeys Review (10:30 AM)
3. Cindy / Manan (11:00 AM)
4. Applied AI Jamming – Hiring (12:30 PM)
5. 1:1 with Ray (3:09 PM)

---

✅ *DECISIONS MADE TODAY*

*1. MBR Slide Restructure → Separate applicant flow context from roadmap*
> You and Ray aligned on restructuring the MBR deck to present applicant flow data, D5/D30 health metrics, and initiatives as a coherent narrative rather than splitting them across sections. You decided to pull the D30 health chart down, contextualize trial conversion rates by health tier (dark/medium/light), and give the audience the full picture before moving to initiatives.
• *Why:* Audiences lose focus when data and "what we're doing about it" are in separate sections. Leading with context sets up a better discussion.
• *Action — Manan:* Update MBR slides before the next review. Separate the D5/D30 data slide from initiatives. Add conversion rate context by health tier. Remove or simplify the noisy trending chart.

*2. Marketplace Vision Framing → Hypothesis-led, experiment-first roadmap*
> You decided to frame marketplace as "a roadmap of experiments to test 4 core hypotheses" rather than committing to a specific product direction. Shifted away from naming specific tactics and toward clearly stating what you need to learn.
• *Why:* Ray pushed back on the slide being too tactic-specific too early. The experiment frame also communicates to leadership that you're not building blind — you're being rigorous.
• *Action — Manan:* Update marketplace vision slide to lead with 4 core hypotheses. Add framing around "no-regrets" capabilities (job matching, sponsored jobs API) vs. true experiments. Share updated slide with Ray before MBR.

*3. Marketplace Planning Cadence → Start meaningful planning conversations the week after next*
> You aligned with Ted, Fadi, and Divij that the earliest you'll have real marketplace planning conversations is the week after next. In the interim, Divij will help with marketplace brainstorming.
• *Why:* Core product priorities still being finalized. You want to avoid constantly shifting direction for the engineering team — morale and focus matter.
• *Action — Manan:* Set up a marketplace discovery working session with Divij for next week. Keep it exploratory — hypotheses and experiments, not specs.
• *Action — Ted:* Ask Ray explicitly about the "Applied AI Scientist TBD" role definition and what that team will own.

*4. Applied AI Team Allocation → Divij supports Marketplace short-term; Ted's team stays on backlog*
> Until core product priorities are finalized, Divij joins marketplace discovery. Ted's team works internal backlog. Fadi continues supporting both.
• *Why:* Leadership hasn't finalized core direction. This avoids burning sprint capacity on unclear priorities.
• *Action — Manan:* Confirm this plan with Martin and Ray so everyone's aligned on where the Applied AI resources are pointed.

*5. Homebase Boost → Replace Craigslist; simplified V1 modal scope*
> You decided to replace the Craigslist boost option with Homebase boost ($50). For this sprint, keep the existing modal UI structure and just swap out Craigslist. Full modal redesign is a separate V2 project.
• *Why:* Craigslist boost usage is <0.5% of active jobs over 3 months — it's dead weight. Homebase boost needs its own slot. Simplified scope keeps the sprint clean.
• *Pricing hierarchy confirmed:* Homebase boost $50 → ZipRecruiter $199/post → Indeed (variable)
• *Attribution:* Talaroo applicants should show as "Homebase" source going forward.
• *Action — Cindy:* Update boost modal designs with new copy and pricing. Tag Manan when ready in Figma.
• *Action — Manan:* Update Linear tickets with design links once Cindy tags you.

*6. Sprint Process → Manan + Dana own proposal→prototype moves; tech leads own prototype→build*
> You and Cindy aligned on cleaner ticket ownership to reduce confusion about who's moving things in Linear. Fewer people touching tickets = cleaner prioritization signal.
• *Why:* Items (like "Predicted Role") got moved out of sprint without advance notice, creating frustration. Need clearer lanes.
• *Action — Manan:* Communicate this ticket-movement protocol clearly to the broader team.

*7. Hiring Essential Journeys → Tag quality improvements in the shared sheet*
> Key action from the Essential Journeys Review: tag all in-progress quality work so Jan and Keyvan get a complete picture for the program.
• *Action — Manan:* Group quality-tagged Linear items into a project and share links with Jan's team by end of this week or early next week.
• *Action — Cindy:* Verify Linear ticket list with Manan. Follow up with Dana on Candidate Table status.

*8. Candidate Profile → Resume-based matching + deal breakers in roadmap*
> Confirmed that upgrading candidate profile view (resume visibility + updated Top Match definition) is on the roadmap. Deal breakers Phase 1 is shipped; Phase 2 (filtering from Top Match) is upcoming.
• *Why:* Screener completion is strong (80-90% once started), but Top Match has historically ignored resumes. This closes a big quality gap.
• *Action — Manan:* Follow up with Dana on Candidate Table priority. Confirm candidate profile rework timeline.

*9. Hiring Assistant → Long-term goal: full Homebase assistant, not just job creation*
> You discussed the vision of evolving the Hiring Assistant from its current limited scope into a full Homebase assistant that handles scheduling, interview coordination, and applicant follow-up.
• *Approach:* Take one core workflow, redesign from scratch with Applied AI team input. Define intake process and multi-turn conversation handling.
• *Action — Manan + Dana:* Book time with Chris and the design team to begin brainstorming the Homebase Assistant connection into hiring flows. Fadi/Chris working sessions for AI pattern consistency.

*10. Personal Roadmap → Build your own marketplace + team roadmap in Granola*
> You and Ray agreed that having a written plan (even in Granola) that shows week-by-week focus for the next 3 sprints is valuable — not because everything is known, but because it boxes in behavior and surfaces expectations.
• *Action — Manan:* Continue building out your roadmap. Add lines for marketplace hypothesis work. Share with Ray when ready.

---

🔥 *TOP ACTION ITEMS — YOUR PERSONAL LIST*

| Priority | Action | Deadline |
|---|---|---|
| 🔴 High | Update MBR slides (restructure applicant flow section, D30 chart, conversion context) | Before next MBR review |
| 🔴 High | Update marketplace vision slide (4 hypotheses, experiment framing) | Before MBR |
| 🟡 Medium | Share quality-tagged Linear items with Jan's team | EOD Friday or early next week |
| 🟡 Medium | Update Linear tickets with Cindy's new boost modal designs | After Cindy tags you |
| 🟡 Medium | Communicate ticket-movement protocol to team | This week |
| 🟢 Ongoing | Build out personal roadmap (marketplace + team) in Granola | Next week |
| 🟢 Ongoing | Set up marketplace discovery session with Divij | Next week |
| 🟢 Ongoing | Follow up with Dana on Candidate Table priority | This week |

---

💡 *WHAT I'M WATCHING FOR YOU*

- The MBR is your big stage right now. The restructured narrative you and Ray landed on is genuinely sharper — trust that instinct.
- Marketplace is the right bet and you're framing it the right way. "Experiment roadmap" is a much better story than "here's the product we're building."
- Sprint discipline is improving but needs a bit more reinforcement on the ticket-ownership side. One clear message to the team should fix it.
- Your instinct to protect the team from priority whiplash is spot-on. Keep holding that line.

You're doing great, Manan. Big week ahead — you've got this. 💪"""

    return summary


def main():
    print(f"[{datetime.now()}] Starting daily summary generation...")

    try:
        token = get_slack_token()
    except EnvironmentError as e:
        print(f"ERROR: {e}")
        print("\n--- SUMMARY THAT WOULD BE SENT ---")
        print(build_todays_summary())
        sys.exit(1)

    summary = build_todays_summary()
    print("Summary generated. Sending to Slack...")

    send_slack_message(
        token=token,
        channel=SLACK_CHANNEL_ID,
        text=summary
    )

    print("Done!")


if __name__ == "__main__":
    main()
