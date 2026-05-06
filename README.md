# Homebase PM Daily Summary Bot

A Cursor Cloud Agent automation that runs daily at 5pm UTC, reviews all of Manan's Granola meeting notes for the day, synthesizes decisions made, and sends a structured summary to Slack (channel `D06E4QMHCNN`).

## What it does

1. Fetches all Granola meetings for the current day via the Granola MCP tool
2. Extracts decisions, action items, rationale, and follow-ups from each meeting
3. Sends a beautifully formatted daily decision summary to Slack as a direct message

## Setup

### Prerequisites

- Granola MCP connected in Cursor (already configured)
- Slack MCP connected **or** a `SLACK_BOT_TOKEN` secret added in Cursor Cloud Agent secrets

### Adding the Slack token

1. Go to [cursor.com/settings](https://cursor.com/settings) → Cloud Agents → Secrets
2. Add a secret named `SLACK_BOT_TOKEN` with your Slack bot OAuth token
3. The token needs `chat:write` scope and must be invited to the DM channel

### Running manually

```bash
pip install -r requirements.txt
SLACK_BOT_TOKEN=xoxb-your-token python3 daily_summary.py
```

## Schedule

This automation is triggered by a cron schedule (`0 0 * * *` — midnight UTC = 5pm PDT) via Cursor Cloud Agents.
