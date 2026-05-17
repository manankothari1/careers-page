# Manan's Daily PM Briefing Automation

This repo powers the **Chief of Staff** Cursor Cloud Agent — a daily automation that reviews all Granola meeting notes and sends a comprehensive summary to Slack each evening.

## What It Does

Every day at midnight UTC, the automation:
1. Fetches all Granola meeting notes from the current day
2. Synthesizes key decisions, action items, follow-ups, and rationale
3. Sends a beautifully formatted message to your Slack DM (channel `D06E4QMHCNN`)

## Setup Requirements

### 1. Slack Bot Token (Required)
You need a Slack Bot OAuth token with `chat:write` permission. Add it as a Cursor Cloud Agent secret:

- Go to **Cursor Dashboard → Cloud Agents → Secrets**
- Add a secret named `SLACK_BOT_TOKEN` with your Slack Bot OAuth token
- The token format is `xoxb-...`

To create a Slack Bot:
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Create a new app → "From scratch"
3. Add **Bot Token Scopes**: `chat:write`, `chat:write.public`
4. Install to your workspace
5. Copy the "Bot User OAuth Token"

### 2. Granola MCP (Already configured)
The Granola MCP is already connected and working.

### 3. Slack MCP (Optional — Bot Token preferred)
The `SLACK_BOT_TOKEN` secret is the recommended approach. The Slack MCP in Cursor can also be used as a fallback.

## Files

- `daily_summary.py` — Core script for building and sending Slack messages
- `todays_summary.json` — Example/last-run summary data

## Manual Run

```bash
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py todays_summary.json
```
