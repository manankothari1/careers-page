# Daily Decision Summary — Chief of Staff Automation

A daily Slack briefing bot for **Manan Kothari @ Homebase**. Every day at 5pm PDT, it reviews your Granola meeting notes and sends you a comprehensive summary with decisions made, action items, and rationale straight to your Slack DM.

## How It Works

This is a Cursor Cloud Agent automation triggered by a daily cron (`0 0 * * *` UTC = 5pm PDT). The agent:

1. Pulls all your recorded meetings for the day from **Granola MCP**
2. Analyzes each meeting's summary, decisions, and next steps
3. Generates a beautifully formatted **Slack message** with:
   - Decisions made and their rationale
   - Action items broken down by owner
   - Time-sensitive follow-ups flagged
   - Week-ahead priorities (on Sundays)
4. Posts it directly to your Slack DM (`D06E4QMHCNN`)

## Setup

### Step 1: Connect Slack in Cursor (Recommended)

1. Open **Cursor Desktop**
2. Go to **Settings → MCP**
3. Find **Slack** and click **Connect / Authenticate**
4. Authorize the Cursor Slack app with your workspace
5. The automation will use this connection automatically

### Step 2: (Alternative) Add a Slack Bot Token as a Secret

If you prefer to use your own Slack bot token:

1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add the `chat:write` OAuth scope
3. Install it to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
4. In **Cursor Dashboard → Cloud Agents → Secrets**, add:
   ```
   SLACK_BOT_TOKEN = xoxb-your-token-here
   ```

### Step 3: (Optional) Granola API Key for Direct Access

The automation uses your Granola MCP connection (already working). For resilient standalone operation:

1. Open the **Granola desktop app**
2. Go to **Settings → Connectors → API keys**
3. Click **Create new key** (requires Business/Enterprise plan)
4. Add as a Cursor secret:
   ```
   GRANOLA_API_KEY = grn_your-key-here
   ```

## Files

- `daily_summary.py` — Main automation script (Granola API + Slack API)
- `send_today_summary.py` — Pre-built sender for the current summary

## Running Manually

```bash
# Dry run (prints message without sending)
DRY_RUN=1 SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py

# Send with Granola API key
GRANOLA_API_KEY=grn_... SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```
