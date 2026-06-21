# Daily Decision Summary — Chief of Staff Automation

A Cursor Cloud Agent automation that runs every day at 5pm PT, reviews all Granola meeting notes from the day, and sends a Slack DM with a structured summary of decisions, action items, and rationale.

## How It Works

1. **Trigger:** Cron runs at `0 0 * * *` (midnight UTC = 5pm PDT)
2. **Granola:** The agent reads all meetings for the current day via the Granola MCP
3. **Summary:** Decisions, action items, follow-ups, and rationale are extracted and formatted
4. **Slack:** The summary is posted to your DM channel (`D06E4QMHCNN`)

## Setup

### 1. Slack Bot Token

You need a Slack bot with `chat:write` permission.

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App → From Scratch
2. Add OAuth scope: `chat:write`
3. Install to your workspace
4. Copy the **Bot User OAuth Token** (`xoxb-...`)
5. Add it to Cursor Cloud Agent Secrets:
   - Go to [cursor.com](https://cursor.com) → Cloud Agents → Secrets
   - Add secret: `SLACK_BOT_TOKEN` = `xoxb-your-token-here`
6. Invite the bot to your DM: `/invite @your-bot-name` in Slack

### 2. Granola MCP

Authenticate the Granola MCP in Cursor Desktop IDE:
- Settings → MCP → Granola → Connect

### 3. Slack MCP (optional)

Authenticate the Slack MCP in Cursor Desktop IDE for enhanced Slack features.

## Files

- `daily_summary.py` — Slack delivery helper script
- `requirements.txt` — Python dependencies

## Testing

```bash
export SLACK_BOT_TOKEN=xoxb-your-token
python daily_summary.py --test
```
