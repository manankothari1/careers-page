# Daily Decision Summary — Slack Bot

A Cursor Cloud Agent automation that runs every day and sends Manan a chief-of-staff-style Slack summary of all decisions, action items, and follow-ups from his Granola meeting notes.

## What It Does

Every day at midnight UTC (≈ 5–8 PM PT), the automation:
1. Pulls all Granola meeting notes from the day
2. Synthesizes key decisions, action items, team follow-ups, and rationale
3. Sends a warm, comprehensive summary to Slack channel `D06E4QMHCNN`

## One-Time Setup

### 1. Authenticate the Slack MCP (Recommended)
1. Open **Cursor Dashboard → Cloud Agents → MCP Servers**
2. Find the **Slack** integration and click **Authenticate**
3. Complete the OAuth flow and grant DM permissions

### 2. OR Add a Slack Bot Token (Fallback)
If you prefer a bot token instead of the Slack MCP:
1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add `chat:write` and `im:write` OAuth scopes
3. Install to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
4. Go to **Cursor Dashboard → Cloud Agents → Secrets**
5. Add secret: `SLACK_BOT_TOKEN` = your token
6. Invite the bot to the DM channel if needed

### 3. Granola MCP
The Granola integration is already connected and working. No additional setup needed.

## Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Instructions for the Cloud Agent (what to do each day) |
| `send_slack_message.py` | Fallback script to send Slack messages via Bot Token |
| `README.md` | This file |

## Manual Run

To trigger a summary manually, visit **Cursor Dashboard → Cloud Agents** and run the automation, or run the fallback script directly:

```bash
export SLACK_BOT_TOKEN=xoxb-your-token-here
python3 send_slack_message.py D06E4QMHCNN "Your message here"
```

## Cron Schedule

```
0 0 * * *  — runs daily at midnight UTC
```
