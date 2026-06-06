# Daily Decision Summary — Homebase PM Chief of Staff

Automated daily end-of-day Slack summary for Manan Kothari at Homebase.

## What It Does

Every day at 5pm PT, this automation:
1. Pulls all meetings recorded in Granola for the current day
2. Extracts decisions made, action items, follow-ups, and rationale
3. Sends a rich, formatted Slack summary to `D06E4QMHCNN`

## Setup

### One-Time Configuration (Required)

**Add your Slack Bot Token to Cursor Secrets:**
1. Go to [Cursor Dashboard](https://cursor.com) → Cloud Agents → Secrets
2. Add a new secret: `SLACK_BOT_TOKEN` = `xoxb-your-token-here`
3. The token needs these Slack scopes: `chat:write`, `im:write`

**Alternative: Authenticate Slack MCP in Cursor**
- In Cursor Desktop → Settings → MCP → Slack → Authenticate

### Running Manually

```bash
SLACK_BOT_TOKEN=xoxb-your-token python3 send_slack_summary.py
```

## Files

- `daily_summary.py` — Full automation script with Granola API integration
- `send_slack_summary.py` — Standalone Slack sender (used by the Cursor automation agent)

## How the Automation Works

The Cursor Cloud Agent cron automation:
1. Triggers daily at midnight UTC (8pm EDT / 5pm PDT)
2. Uses Granola MCP to fetch the day's meetings and transcripts
3. Analyzes each meeting for decisions, action items, and rationale
4. Calls `python3 send_slack_summary.py` (or sends via Slack MCP directly if authenticated)

## Channel

Slack DM channel: `D06E4QMHCNN` (Manan Kothari)
