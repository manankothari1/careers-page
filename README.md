# careers-page

## Daily Decision Summary Automation

`daily_summary.py` is a Cursor Cloud Agent cron that runs every day at midnight UTC (5 PM PT).

It reads Manan's Granola meeting notes for the day, extracts decisions, action items, and follow-ups, and sends a formatted Slack message to channel `D06E4QMHCNN`.

### Setup

1. Create a Slack Bot with `chat:write` scope and invite it to the DM channel `D06E4QMHCNN`.
2. Add the bot token as a secret in **Cursor Dashboard → Cloud Agents → Secrets**:
   - Key: `SLACK_BOT_TOKEN`
   - Value: `xoxb-...`

The automation trigger is configured as a daily cron (`0 0 * * *` UTC).
