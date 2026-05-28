# Daily Decision Summary — Chief of Staff Automation

A Cursor Cloud Agent automation that runs daily at 5pm PDT, reviews Granola meeting notes, and sends Manan Kothari a Slack summary of all decisions, action items, and follow-ups from the day.

## How It Works

1. **Cron trigger**: Fires at midnight UTC (5pm PDT) every day
2. **Granola review**: The AI agent queries Granola via MCP to fetch all meetings for the current work day
3. **AI synthesis**: Extracts key decisions, action items, follow-ups, and rationale
4. **Slack delivery**: Sends a rich, formatted message to your DM channel (`D06E4QMHCNN`)

## Setup Requirements

### 1. Slack Bot Token

Add `SLACK_BOT_TOKEN` to your Cursor Cloud Agent secrets:

1. Go to [cursor.com/dashboard](https://cursor.com/dashboard) → Cloud Agents → Secrets
2. Add a new secret: `SLACK_BOT_TOKEN` = your Slack bot token
3. Your Slack app needs the `chat:write` scope and must be installed in your workspace

To get a Slack bot token:
- Go to [api.slack.com/apps](https://api.slack.com/apps)
- Create a new app → "From scratch"
- Add OAuth scope: `chat:write`
- Install to workspace
- Copy the "Bot User OAuth Token" (starts with `xoxb-`)

### 2. Slack MCP Authentication (alternative)

Alternatively, authenticate the Slack MCP in the Cursor desktop IDE:
- Settings → MCP Servers → Slack → Authenticate

### 3. Granola MCP

Granola MCP must be connected (already configured for `mkothari@joinhomebase.com`).

## Files

| File | Purpose |
|------|---------|
| `send_slack.py` | Thin Slack API sender — takes a JSON payload and sends via `SLACK_BOT_TOKEN` |
| `daily_summary.py` | Full daily summary script (for testing/development) |

## Running Manually

```bash
export SLACK_BOT_TOKEN=xoxb-your-token-here
python3 daily_summary.py
```

## Message Format

Each daily message includes:
- **Day Highlights** — What kind of day it was
- **Key Decisions Made** — Each decision with rationale
- **Action Items & Follow-Ups** — Organized by owner (Manan vs. team)
- **Sprint Scoreboard** — Quick status of in-flight work

## Slack Channel

Target: `D06E4QMHCNN` (Manan's DM)
