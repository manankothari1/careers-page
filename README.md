# Manan's Daily PM Decision Summary Bot

Automated Chief of Staff that runs every day at **midnight UTC (5 PM PDT)** via Cursor Cloud Agent cron.

It reads all Granola meeting notes from the current day and posts a structured decision summary to Slack — decisions made, rationale, action items, and open questions — so you start each evening with full situational awareness.

## How It Works

1. Cursor Cloud Agent is triggered by cron (`0 0 * * *` = midnight UTC)
2. Agent reads Granola meeting notes for the day via the Granola MCP
3. Agent compiles decisions, action items, and follow-ups
4. Agent posts a formatted summary to Slack channel `D06E4QMHCNN`

## One-Time Setup

### Step 1 — Authenticate the Slack MCP (preferred)

1. Open **Cursor Dashboard → Cloud Agents → MCP Servers**
2. Find **Slack** and click **Connect / Sign in**
3. Authorize the Cursor Slack integration for your workspace

Once connected, the Cloud Agent will use the Slack MCP to send messages automatically — no token management needed.

### Step 2 (alternative) — Add a Slack Bot Token as a Secret

If you prefer direct API access:

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App
2. Add the OAuth scope: `chat:write`
3. Install the app to your Homebase workspace
4. Copy the **Bot User OAuth Token** (`xoxb-...`)
5. Open **Cursor Dashboard → Cloud Agents → Secrets**
6. Add a secret named `SLACK_BOT_TOKEN` with that value
7. Invite the bot to the DM channel: `/invite @YourBotName` in Slack

## Running Manually

```bash
SLACK_BOT_TOKEN=xoxb-your-token python3 daily_summary.py
```

## Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Main script — generates and sends the daily Slack summary |
| `README.md` | This file |
