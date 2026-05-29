# Daily Decision Summary — Chief of Staff Automation

A Cursor automation that runs daily at **5pm PDT** and sends Manan a Slack digest of every decision made during the day, with action items, follow-ups, and rationale — pulled directly from Granola meeting notes.

## How It Works

1. **Cursor cron trigger** fires at 5pm PDT (midnight UTC)
2. The **Cursor agent** queries the Granola MCP for today's meetings and transcripts
3. The agent synthesizes decisions, action items, and rationale into a clear summary
4. The summary is sent as a **Slack DM** to channel `D06E4QMHCNN`

## Setup

### Required Secrets (add in Cursor Dashboard → Cloud Agents → Secrets)

| Secret | Description |
|--------|-------------|
| `SLACK_BOT_TOKEN` | Slack bot token (`xoxb-...`). The bot needs `chat:write` scope and must be added to the DM channel. |
| `GRANOLA_API_TOKEN` | *(Optional)* Your Granola access token. Only needed to run `daily_summary.py` standalone (not as a Cursor agent). |

### Slack Bot Setup (one-time)

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App**
2. Choose **From scratch**, name it `Chief of Staff`, select your Homebase workspace
3. Under **OAuth & Permissions**, add the `chat:write` bot scope
4. **Install** the app to your workspace
5. Copy the **Bot User OAuth Token** (`xoxb-...`) → add to Cursor secrets as `SLACK_BOT_TOKEN`
6. In Slack, open the DM with yourself or the bot and note the channel ID (`D06E4QMHCNN` is already configured)

### MCP Configuration (already set up in Cursor)

- **Granola MCP**: Provides `list_meetings`, `get_meetings`, `get_meeting_transcript` tools
- **Slack MCP**: *(optional alternative)* Authenticate in Cursor Dashboard → MCP Servers

## Running Manually

```bash
# Install dependencies
pip install -r requirements.txt

# Dry run (preview without sending to Slack)
python3 daily_summary.py --dry-run

# Run for a specific date
python3 daily_summary.py --date 2026-05-28 --dry-run

# Send for today (requires SLACK_BOT_TOKEN)
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

## Automation Schedule

The Cursor cron automation runs daily at `0 0 * * *` (midnight UTC = 5pm PDT).

The agent workflow:
1. Queries Granola MCP for today's meetings (Pacific time)
2. Fetches full summaries and transcripts for each meeting
3. Synthesizes decisions, action items, and strategic rationale
4. Sends a formatted Slack message to `D06E4QMHCNN`
