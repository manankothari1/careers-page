# Daily Meeting Summary — Chief of Staff Automation

This repo powers an automated daily debrief for Manan Kothari (PM at Homebase).

A Cursor AI Cloud Agent runs every day at midnight UTC (5 PM PDT), reviews all Granola meeting notes for the day, and sends a structured summary to Slack with decisions, action items, and strategic context.

## Setup

### Required: Slack Bot Token

Add a `SLACK_BOT_TOKEN` secret in **Cursor Cloud Agents → Secrets** (or ask your admin to set it up as a team secret).

The bot needs the following OAuth scopes:
- `chat:write` — to post messages
- `im:write` — to send DMs

### How It Works

1. The cron trigger fires at `0 0 * * *` (midnight UTC = 5 PM PDT)
2. The Cloud Agent (Cursor AI) uses the **Granola MCP** to pull all meetings for the current day
3. It analyzes transcripts and notes to extract: decisions, action items, rationale, and strategic context
4. It formats and sends a rich Slack message to `D06E4QMHCNN` (your DM channel)

### Manual Test

```bash
export SLACK_BOT_TOKEN=xoxb-your-token-here
python3 daily_summary.py summaries/2026-05-18.json
```

## Daily Summaries Archive

Summaries are stored in `summaries/YYYY-MM-DD.json` for reference.
