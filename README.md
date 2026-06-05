# Daily Decision Summary — Chief of Staff Automation

This repo powers a Cursor Cloud Agent cron job that runs every day at **midnight UTC (5 PM PDT)** and sends Manan a Slack message summarizing all decisions, action items, and rationale from the day's Granola meetings.

## How It Works

1. **Cron fires** at `0 0 * * *` (midnight UTC / 5pm PDT)
2. **Granola MCP** reads all meetings from the current day
3. **AI agent** synthesizes decisions, action items, and rationale for each meeting
4. **Slack API** posts the summary to `D06E4QMHCNN`

## One-Time Setup Required

### 1. Add a Slack Bot Token

The Slack MCP needs a bot token to post messages. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps) with these scopes:
- `chat:write`
- `im:write`

Then add `SLACK_BOT_TOKEN` to your Cursor Cloud Secrets:
> **Cursor Dashboard → Cloud Agents → Secrets → Add Secret**
> 
> Key: `SLACK_BOT_TOKEN`  
> Value: `xoxb-your-token-here`

Make sure the bot is added to the DM channel `D06E4QMHCNN` (Manan's DM).

### 2. Authenticate the Slack MCP (Alternative)

If you're using the Slack MCP server, authenticate it in Cursor IDE:
> **Settings → MCP → Slack → Authenticate**

## Files

- `daily_summary.py` — Core script: builds the summary from meeting data and sends to Slack
- `README.md` — This file

## Running Manually

```bash
# Preview the message without sending
PYTHONPATH=. python3 daily_summary.py --dry-run

# Send for a specific date
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py --date "June 4, 2026"

# Send for today
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

## Channels

- Slack Channel: `D06E4QMHCNN` (Manan's DM)
- Granola Workspace: Homebase (`mkothari@joinhomebase.com`)
