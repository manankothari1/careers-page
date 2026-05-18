# Daily PM Summary Bot — Homebase

This repo contains the automation that serves as Manan's AI chief of staff at Homebase.

Every day at **5pm PT** (midnight UTC), it:
1. Pulls all Granola meeting notes from that day
2. Synthesizes key decisions, action items, and rationale
3. Posts a warm, actionable debrief to Slack (channel `D06E4QMHCNN`)

## Setup Requirements

### Cursor Secret Required

Add the following secret in **Cursor Dashboard → Cloud Agents → Secrets**:

| Secret Name | Description |
|---|---|
| `SLACK_BOT_TOKEN` | Slack Bot OAuth token (starts with `xoxb-`) |

### Slack Bot Permissions Needed

Your Slack bot needs these OAuth scopes:
- `chat:write` — to post messages
- `im:write` — to post to DMs/channels

### How to Create a Slack Bot Token

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App
2. Add OAuth scopes: `chat:write`, `im:write`
3. Install app to workspace
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)
5. Add it as `SLACK_BOT_TOKEN` in Cursor secrets

## Files

- `daily_summary.py` — standalone Slack sender (used when invoked with pre-built summary data)
- `README.md` — this file

## How it Works

The automation runs as a Cursor Cloud Agent on a cron schedule (`0 0 * * *`). The agent:
1. Uses the **Granola MCP** to query today's meetings
2. Synthesizes decisions/actions using AI analysis
3. Posts a formatted Slack message using the **Slack Web API**

If no meetings are found for today (e.g. weekends), it reviews the most recent business day.
