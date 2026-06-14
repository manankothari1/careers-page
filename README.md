# Daily Decision Summary — Chief of Staff Automation

A Cursor Cloud Agent automation that runs at 5pm PDT every day, reviews all Granola meeting notes from the day, and sends a formatted decision/action-item summary to Slack DM `D06E4QMHCNN`.

## How It Works

1. A Cursor Cloud Agent cron (`0 0 * * *` UTC = 5pm PDT) triggers this automation daily
2. The agent fetches today's Granola meeting notes via the Granola MCP or Granola API
3. It extracts decisions, rationale, and action items from each meeting
4. It posts a richly formatted summary to Slack

## Setup

### Required Secrets (Cursor Dashboard → Cloud Agents → Secrets)

| Secret | Description |
|--------|-------------|
| `SLACK_BOT_TOKEN` | Slack bot token (`xoxb-...`). Create a Slack app with `chat:write` scope, add to your workspace, and copy the Bot OAuth token. |
| `GRANOLA_API_KEY` | Granola API key (`grn_...`). Generate in Granola desktop: Settings → Connectors → API keys. Requires Business or Enterprise plan. |

### Creating a Slack Bot

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App → From scratch
2. Name: "Daily Chief of Staff" · Workspace: Homebase
3. OAuth & Permissions → Bot Token Scopes → add `chat:write`
4. Install to Workspace → copy the **Bot OAuth Token** (`xoxb-...`)
5. Invite the bot to your DM: open the DM in Slack, click the `+` to add an app

### Running Standalone

```bash
pip install -r requirements.txt
export SLACK_BOT_TOKEN=xoxb-...
export GRANOLA_API_KEY=grn_...
python3 daily_summary.py
```

## Files

- `daily_summary.py` — Main automation script (standalone runner using Granola + Slack APIs directly)
- `send_today_summary.py` — One-time script to send a pre-composed summary (used by the cloud agent when Granola data is fetched via MCP)
- `requirements.txt` — Python dependencies
