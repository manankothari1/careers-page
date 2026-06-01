# Daily Decision Summary — Chief of Staff Automation

This Cursor Cloud Agent runs every day at **midnight UTC (5pm PDT)** to review your Granola meeting notes and send a rich decision summary to your Slack DM.

## What it does

1. Pulls all Granola meeting notes for the current day (PDT timezone)
2. Extracts decisions made, action items, follow-ups, and rationale from each meeting
3. Formats a clear, readable daily digest
4. Sends it to Slack channel `D06E4QMHCNN`

On days with no meetings (weekends, holidays), it sends an end-of-week lookback with open action items and upcoming week preview.

## Setup

### Required: Slack Bot Token

The automation needs a Slack Bot Token to post messages. To set it up:

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Under **OAuth & Permissions**, add the `chat:write` bot scope
3. Install the app to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
4. In the Cursor Dashboard: **Cloud Agents → Secrets → Add Secret**
   - Name: `SLACK_BOT_TOKEN`
   - Value: your `xoxb-...` token
5. Make sure the bot is invited to your DM channel (`D06E4QMHCNN`)

### Alternative: Authenticate Slack MCP

If you prefer using the Cursor Slack MCP instead:
1. Open Cursor Settings → MCP
2. Find the Slack MCP server and authenticate it
3. The agent will use the MCP tools automatically on the next run

### Granola MCP

Granola MCP should already be authenticated in your Cursor MCP settings. Verify it shows as **ready** (not `needsAuth`).

## Schedule

Cron: `0 0 * * *` — runs daily at midnight UTC (5pm PDT)

## Files

- `daily_digest.py` — core automation helpers (Slack sending, date utilities)
- `send_today_digest.py` — generated each run with today's specific message content
- `requirements.txt` — Python dependencies

## Local testing

```bash
pip install -r requirements.txt
SLACK_BOT_TOKEN=xoxb-your-token python3 send_today_digest.py
```
