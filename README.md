# Daily Decision Digest — Chief of Staff Automation

This repo powers a daily Slack digest that reviews Granola meeting notes and summarizes all decisions, action items, and rationale from the day — sent every evening at 5 PM PDT.

## What It Does

Every day at 5 PM PDT, the automation:
1. Reads all Granola meeting notes from the current day
2. Extracts key decisions, rationale, and action items
3. Sends a beautifully formatted Slack message to your DM channel

## Setup

### Required Secrets (Cursor Dashboard → Cloud Agents → Secrets)

| Secret Name | Description |
|---|---|
| `SLACK_BOT_TOKEN` | Slack Bot Token (starts with `xoxb-`) — required for sending messages |

### Getting a Slack Bot Token

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Under **OAuth & Permissions**, add the `chat:write` bot scope
3. Install the app to your workspace
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)
5. Invite the bot to your DM: `/invite @your-bot-name` in Slack
6. Add the token as `SLACK_BOT_TOKEN` in Cursor Dashboard → Cloud Agents → Secrets

### Alternatively: Connect the Slack MCP

In Cursor IDE → Settings → MCP → Slack → Connect your workspace. This eliminates the need for a manual bot token.

## Running Manually

```bash
# With a Slack bot token:
export SLACK_BOT_TOKEN=xoxb-your-token-here
echo "Test message" | python3 daily_digest.py

# Test mode:
SLACK_BOT_TOKEN=xoxb-... python3 daily_digest.py --test
```

## Schedule

The automation runs via Cursor Cloud Agent cron: `0 0 * * *` (midnight UTC = 5 PM PDT).

## Slack Channel

Channel ID: `D06E4QMHCNN` (your DM channel)
