# Daily Decision Summary — Chief of Staff Automation

A Cursor cron automation that fires every day at **5pm PDT** (midnight UTC) and sends Manan a Slack digest of every decision made that day — pulled from Granola meeting notes — with action items, follow-ups, and rationale.

## How It Works

1. **Cursor cron** triggers at `0 0 * * *` (midnight UTC = 5pm PDT)
2. The **Cursor agent** queries the Granola MCP for today's meetings (Pacific time)
3. For each meeting, the agent extracts decisions, action items, follow-ups, and strategic rationale
4. A formatted Slack DM is sent to channel `D06E4QMHCNN`

## Required Setup

### Slack Bot Token (one-time)

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App → From scratch**
2. Name it `Chief of Staff`, select the Homebase workspace
3. Under **OAuth & Permissions** add the `chat:write` bot scope
4. **Install** the app, copy the **Bot User OAuth Token** (`xoxb-...`)
5. Add it to **Cursor Dashboard → Cloud Agents → Secrets** as `SLACK_BOT_TOKEN`
6. Invite the bot to your DM: in Slack, open a DM with the bot and confirm channel ID `D06E4QMHCNN`

### MCP Servers (already configured in Cursor)

- **Granola MCP** — authenticate in Cursor Dashboard → MCP Servers → Granola
- **Slack MCP** *(optional alternative to bot token)* — authenticate in Cursor Dashboard → MCP Servers → Slack

## Running Manually

```bash
pip install -r requirements.txt

# Preview today's message without sending
python3 daily_summary.py --dry-run

# Preview for a specific date
python3 daily_summary.py --date 2026-05-28 --dry-run

# Send for today (requires SLACK_BOT_TOKEN env var)
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

## Automation Schedule

| Setting | Value |
|---------|-------|
| Cron | `0 0 * * *` |
| Fires at | Midnight UTC = **5pm PDT** |
| Slack channel | `D06E4QMHCNN` |
| Meeting source | Granola MCP |
