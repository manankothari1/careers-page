# Daily Decision Summary — Chief of Staff Automation

This repo powers Manan's daily end-of-day Slack briefing. Every day at 5pm PT, the Cloud Agent automation reads all Granola meetings from the day, synthesizes key decisions, action items, follow-ups, and rationale, and posts a summary to Slack (DM: `D06E4QMHCNN`).

## How It Works

1. **Trigger**: Cursor Cloud Agent cron fires daily at midnight UTC (5pm PT)
2. **Read**: Granola MCP fetches all meetings from the current day
3. **Synthesize**: The agent compiles decisions, action items, and context into a structured summary
4. **Post**: Summary is sent to Slack via the Slack API or Slack MCP

## Setup Requirements

### Option A: Cloud Agent Slack Posting (Recommended)

Add `SLACK_BOT_TOKEN` as a secret in the Cursor Dashboard under **Cloud Agents > Secrets**.

The bot token needs the `chat:write` scope. Create one at [api.slack.com/apps](https://api.slack.com/apps).

### Option B: Authenticate Slack MCP

In Cursor IDE, navigate to MCP settings and authenticate the Slack MCP server. Once authenticated, the Cloud Agent will use it automatically.

### Option C: GitHub Actions

Add `SLACK_BOT_TOKEN` as a GitHub repository secret. The included workflow (`.github/workflows/daily-summary.yml`) will run independently of the Cloud Agent.

## Files

- `daily_summary.py` — Script to post a message to Slack via bot token
- `daily_summaries/` — Archive of daily summaries (markdown)
- `.github/workflows/daily-summary.yml` — GitHub Actions workflow (optional backup)

## Running Manually

```bash
# Post a message from a file
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py --file daily_summaries/2026-06-25.md

# Dry run (print without posting)
python3 daily_summary.py --file daily_summaries/2026-06-25.md --dry-run
```
