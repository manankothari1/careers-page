# careers-page

This repo also hosts the **Daily Decision Summary** automation — a Chief of Staff agent that runs every day at 5 PM PDT, reviews all Granola meeting notes from the day, and sends a structured summary to Slack.

## Daily Decision Summary Automation

### What it does
1. Reads all Granola meetings from the current day
2. Extracts decisions made, rationale, action items, and follow-ups
3. Posts a formatted summary to Slack channel `D06E4QMHCNN`

### Setup — one-time steps

**1. Add `SLACK_BOT_TOKEN` as a Cursor Secret**

- Go to **Cursor Dashboard → Cloud Agents → Secrets**
- Add a secret named `SLACK_BOT_TOKEN` with your Slack bot token (starts with `xoxb-`)
- The bot needs the `chat:write` scope
- The bot must be a member of the DM/channel `D06E4QMHCNN`

**2. Authenticate the Slack MCP in Cursor IDE** *(alternative path)*

- Open Cursor IDE → Settings → MCP → Slack → Sign in

Once either of the above is complete, the automation will work on its next cron run (midnight UTC = 5 PM PDT).

### Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Core module: Slack posting helper + message builder |
| `send_today_summary.py` | One-shot script: runs the full automation for today |

### Running manually

```bash
export SLACK_BOT_TOKEN=xoxb-...
python3 send_today_summary.py
```
