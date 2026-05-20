# Daily Granola Digest for Manan @ Homebase

This automation runs every day at midnight UTC (5:00 PM PDT) and:
1. Pulls all Granola meeting notes from the current day
2. Generates a structured digest with decisions, action items, and rationale
3. Sends a Slack message to channel `D06E4QMHCNN`

## Setup

### Required Secrets (add via Cursor Dashboard → Cloud Agents → Secrets)

| Secret | Description |
|--------|-------------|
| `SLACK_BOT_TOKEN` | Slack Bot OAuth token with `chat:write` scope. Create at [api.slack.com/apps](https://api.slack.com/apps) |

### Slack App Setup
1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Add the `chat:write` Bot Token Scope under **OAuth & Permissions**
3. Install the app to your Slack workspace
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)
5. Invite the bot to your DM channel: `/invite @YourBotName` in the DM
6. Add `SLACK_BOT_TOKEN` as a secret in Cursor Dashboard

### Granola MCP
Ensure the Granola MCP server is authenticated in your Cursor IDE (already configured).

## How It Works

The automation is triggered by the Cursor Cloud Agent cron schedule (`0 0 * * *`).

Each run:
- Lists all meetings for the current day (PDT timezone)
- Gets full summaries and transcripts for each meeting
- Generates a comprehensive digest covering:
  - Key decisions made in each meeting
  - Rationale behind decisions
  - Action items with owners
  - Master prioritized action item list
  - Daily wins summary
- Sends the digest as a Slack message

## Files

- `daily_digest.py` — Core script for building and sending the digest
- `digests/` — Archived daily digests (auto-generated)
