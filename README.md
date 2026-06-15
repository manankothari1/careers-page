# Daily Decision Summary — Chief of Staff Automation

A Cursor Cloud Agent automation that runs daily at 5pm PDT, reviews all Granola meeting notes from the day, and sends a formatted decision/action-item summary to Slack.

## How It Works

1. **Cron trigger** fires at midnight UTC (5pm PDT) every day
2. The Cursor Cloud Agent fetches all Granola meetings recorded that day via the Granola MCP
3. It extracts decisions, action items, and rationale from each meeting
4. It posts a formatted summary to your Slack DM channel

## Setup Requirements

### 1. Granola MCP (already configured)
The automation uses Granola's MCP integration to read your meeting notes. Ensure it's connected in Cursor under **Settings > MCP**.

### 2. Slack MCP Authentication
The automation posts messages via the Slack MCP. To authenticate:
1. Open Cursor Desktop
2. Go to **Settings > MCP**
3. Find the Slack integration and click **Authenticate**
4. Authorize with your Homebase Slack workspace

### 3. Slack Channel
The target channel is `D06E4QMHCNN` (your personal DM channel).

## Fallback: Standalone Script

If you prefer to run the summary manually or as a standalone script:

```bash
# Install dependencies
pip install slack-sdk

# Set your Slack bot token
export SLACK_BOT_TOKEN=xoxb-your-token-here
export SLACK_CHANNEL_ID=D06E4QMHCNN

# Run with pre-formatted meeting data
python3 scripts/daily_summary.py --data scripts/meetings.json --date "Monday, June 15, 2026"
```

The meeting data JSON should be an array of objects with the following shape:
```json
[
  {
    "title": "Meeting Title",
    "time": "9:30 AM PDT",
    "decisions": ["Decision 1", "Decision 2"],
    "action_items": ["Action 1", "Action 2"],
    "rationale": "Why these decisions were made"
  }
]
```

## Output Format

Each daily Slack message includes:
- Meeting title and time
- Key decisions made
- Why those decisions were made (rationale)
- Your specific action items with checkboxes
