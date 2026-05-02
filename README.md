# Manan's Daily Decision Summary Bot 🤖

A Cursor Cloud Agent automation that runs every day at midnight UTC (5pm PT) and:

1. Reviews all of Manan's Granola meetings for the day
2. Extracts decisions, action items, rationale, and follow-ups
3. Sends a beautifully formatted Slack DM to Manan

---

## Setup

### Required Secret

Add the following secret in **Cursor Dashboard → Cloud Agents → Secrets**:

| Secret Name | Value |
|---|---|
| `SLACK_BOT_TOKEN` | Your Slack Bot OAuth token (`xoxb-...`) |

### Slack Bot Permissions Required

Your Slack bot needs these OAuth scopes:
- `chat:write` — to post messages
- `im:write` — to send DMs

The bot must be invited to the DM channel `D06E4QMHCNN` (just send the bot a message in that DM to open the channel).

---

## Files

- `daily_summary.py` — Core Slack posting utility
- `run_daily_summary.py` — Orchestrator script (accepts JSON summary via stdin or file arg)

---

## How It Works

The Cursor Cloud Agent automation:
1. Fetches today's meetings via the Granola MCP (`list_meetings`, `get_meetings`)
2. Synthesizes decisions, action items, and context from meeting summaries
3. Formats the summary as rich Slack Block Kit message
4. Posts to `D06E4QMHCNN` using the Slack Web API

---

## Trigger

**Schedule:** `0 0 * * *` (midnight UTC = 5pm PT)

This means every weekday at 5pm PT, Manan gets his daily wrap-up.
