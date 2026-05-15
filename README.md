# Chief of Staff — Daily Decision Summary

Automated daily briefing for Manan Kothari (PM @ Homebase). Runs every day at 5 PM PDT, reviews all Granola meeting notes from the day, and sends a structured decision summary to Slack.

## What It Does

1. Pulls all Granola meetings from the current day
2. Extracts decisions, action items, follow-ups, and rationale
3. Posts a beautifully formatted summary to Slack DM (`D06E4QMHCNN`)

## Setup

### 1. Slack Bot Token (Required)

Add your Slack bot token as a secret in Cursor Dashboard → Cloud Agents → Secrets:

```
SLACK_BOT_TOKEN=xoxb-your-token-here
```

The bot needs the following Slack scopes:
- `chat:write`
- `im:write`

### 2. Run Manually

```bash
# Dry run (prints to stdout, no Slack message sent)
python daily_summary.py --dry-run

# Send today's summary to Slack
python daily_summary.py

# Send summary for a specific date
python daily_summary.py --date 2026-05-14
```

## How the Cron Automation Works

The Cursor automation triggers at `0 0 * * *` UTC (= 5 PM PDT), which:
1. Fetches today's meetings from Granola via MCP
2. Generates a `summaries/YYYY-MM-DD.md` file
3. Posts the summary to Slack

## Summaries Archive

Pre-generated summaries are saved in `summaries/` for reference and auditing.
