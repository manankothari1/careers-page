# Chief of Staff Automation

A Cursor Cloud Agent automation that runs every day at 5pm PT, reviews all Granola meeting notes from the day, and sends a Slack DM with a comprehensive briefing: decisions made, action items, follow-ups, and rationale.

## How It Works

1. **Cron trigger** fires at midnight UTC (5 PM PT)
2. The **Cursor Cloud Agent** uses the **Granola MCP** to pull all meeting notes from the current day
3. It synthesizes decisions, action items, follow-ups, and a CoS take
4. It sends the briefing to the configured **Slack DM channel** via the **Slack MCP**

Daily summaries are also saved to `summaries/YYYY-MM-DD.md` as a backup.

## Setup

### Required: Authenticate the Slack MCP Server

The Slack MCP server must be authenticated in Cursor IDE for the automation to send messages:

1. Open Cursor IDE
2. Go to **Settings > MCP Servers**
3. Find the **Slack** MCP server and click **Authenticate / Connect**
4. Authorize with your Slack workspace

### Alternative: Slack Bot Token

If you prefer to use a direct Slack API token instead of the MCP server:

1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add the `chat:write` scope
3. Install the app to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
4. Add it as a secret in **Cursor Dashboard > Cloud Agents > Secrets**:
   - Key: `SLACK_BOT_TOKEN`
   - Value: `xoxb-your-token-here`

Then run the sender manually:

```bash
python3 daily_summary.py < payload.json
```

## Summaries Archive

Past daily summaries are stored in the `summaries/` directory.
