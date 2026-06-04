# Chief of Staff Daily Decision Summary

An automated daily brief that reviews your Granola meetings and sends a structured decision summary to Slack — every day at midnight UTC (5pm PDT / 8pm EDT).

## What It Does

Each day, this Cursor Cloud Agent automation:
1. Pulls all your Granola meeting notes for the day
2. Synthesizes key decisions, action items, follow-ups, and rationale
3. Sends a beautifully formatted Slack message to your DM channel

## Setup

### Prerequisites

1. **Granola MCP** — Already configured and working ✅
2. **Slack MCP** — Requires authentication in Cursor Dashboard:
   - Go to Cursor Dashboard → Cloud Agents → Secrets
   - Add `SLACK_BOT_TOKEN` with your Slack bot token (`xoxb-...`)
   - Your bot needs the `chat:write` permission scope
   - Target channel: `D06E4QMHCNN` (your DM)

### Slack Bot Setup (One-Time)

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App
2. Add OAuth scope: `chat:write`
3. Install to your workspace
4. Copy the Bot User OAuth Token (`xoxb-...`)
5. Add it as `SLACK_BOT_TOKEN` in Cursor Dashboard → Cloud Agents → Secrets
6. Invite the bot to your DM: `/invite @your-bot-name`

### Manual Send (Testing)

```bash
export SLACK_BOT_TOKEN=xoxb-your-token-here
python3 send_daily_summary.py
```

## Files

- `send_daily_summary.py` — Today's pre-built summary + Slack send logic
- `daily_summary.py` — Reusable helper functions for building Slack Block Kit messages

## Automation Schedule

The Cursor Cloud Agent cron runs at `0 0 * * *` (midnight UTC).
This corresponds to:
- 5:00 PM PDT (Pacific Daylight Time)
- 8:00 PM EDT (Eastern Daylight Time)
