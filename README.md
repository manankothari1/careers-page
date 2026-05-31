# Daily Decision Summary — Chief of Staff Bot

This repo powers a daily Slack summary that reviews your Granola meeting notes every day at 5pm PDT and sends you a clear digest of decisions, action items, blockers, and follow-ups.

## How It Works

A Cursor Cloud Agent automation is triggered by cron (`0 0 * * *` = midnight UTC = 5pm PDT). It:

1. Fetches today's meetings from Granola
2. Uses AI to extract decisions, action items, blockers, and follow-ups
3. Sends a formatted Slack message to your DM channel (`D06E4QMHCNN`)

## Setup Requirements

### Option A: Slack MCP (Recommended)
1. In your Cursor IDE, go to **Settings → MCP Servers → Slack**
2. Click **Connect** and authorize the Slack OAuth flow for your Homebase workspace
3. Once connected, the bot will work automatically in Cloud Agent runs

### Option B: Slack Bot Token
1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Add `chat:write` OAuth scope
3. Install it to your Homebase Slack workspace
4. Copy the `xoxb-...` Bot User OAuth Token
5. Add it as a secret in **Cursor Dashboard → Cloud Agents → Secrets**:
   - Name: `SLACK_BOT_TOKEN`
   - Value: `xoxb-your-token-here`

## Files

- `daily-summary.js` — Core message formatter and Slack sender module
- `README.md` — This file

## Granola + Slack DM Channel

- Granola account: `mkothari@joinhomebase.com` (Homebase workspace)
- Slack DM channel ID: `D06E4QMHCNN`
