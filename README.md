# Chief of Staff — Daily Decision Summary

A Cursor Cloud Agent automation that runs every day at **5pm PDT** (midnight UTC), reviews all of Manan's Granola meeting notes for the day, and sends a rich Slack summary with decisions, action items, rationale, and follow-ups.

## How It Works

1. **Cron trigger** fires at `0 0 * * *` (midnight UTC = 5pm PDT)
2. **Granola MCP** reads all meetings recorded that day
3. **Agent** synthesizes decisions, rationale, action items, and open questions
4. **Slack** receives a formatted summary in channel `D06E4QMHCNN`

## Setup Requirements

### 1. Slack Bot Token (Required)

The automation sends messages via the Slack Web API. You need to:

1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add these OAuth scopes: `chat:write`, `im:write`
3. Install the app to your Homebase workspace
4. Copy the **Bot User OAuth Token** (`xoxb-...`)
5. Add it as a Cursor Cloud Agent secret:
   - Cursor Dashboard → Cloud Agents → Secrets → **`SLACK_BOT_TOKEN`**

### 2. Granola MCP (Already Connected)

The Granola MCP is already configured and connected to `mkothari@joinhomebase.com` / Homebase workspace.

### 3. Slack MCP (Optional Alternative)

Alternatively, authenticate the Slack MCP server in Cursor (Cursor Dashboard → MCP → Slack → Connect). If authenticated, the agent can use it directly instead of the bot token.

## Running Locally

```bash
# Preview today's message (no token needed)
python3 chief_of_staff.py

# Send to Slack (requires SLACK_BOT_TOKEN)
SLACK_BOT_TOKEN=xoxb-your-token python3 chief_of_staff.py
```

## Slack Message Format

Each daily message includes:

- **Header** with today's date
- **Decisions made** — each with the rationale behind it
- **Action items** — who needs to do what, and by when
- **Carry-over items** — open items from recent meetings if no meetings today
- **Motivational close** — because Manan deserves it 💪

## Files

| File | Purpose |
|------|---------|
| `chief_of_staff.py` | Main automation script — pre-built today's message + Slack sender |

## Slack Channel

Direct message channel ID: `D06E4QMHCNN`
