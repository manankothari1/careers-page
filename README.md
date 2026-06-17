# Homebase PM Daily Decision Summary

Cursor Cloud Agent automation that reviews your Granola meetings at 5pm PDT every day and sends a structured decision summary to Slack.

## What It Does

Every day at 5pm PDT (midnight UTC), this automation:
1. Fetches all your Granola meetings from the current day
2. Compiles a structured summary of decisions, action items, follow-ups, and rationale
3. Posts a rich Slack message to your DM channel

## Setup

### Required: Add Your Slack Bot Token

This automation needs a Slack Bot Token to post messages. To set it up:

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create a new app
2. Add the `chat:write` OAuth scope under Bot Token Scopes
3. Install the app to your workspace and copy the **Bot OAuth Token** (starts with `xoxb-`)
4. Go to **Cursor Dashboard → Cloud Agents → Secrets** → Add `SLACK_BOT_TOKEN` = `xoxb-your-token-here`

Once added, the token will be auto-injected into every Cloud Agent run.

### Required: Authenticate Granola MCP

Ensure your Granola MCP server is connected in Cursor Settings → MCP Servers.

## Daily Summary Format

Each summary includes:
- **Key Decisions** — what was decided and why it matters
- **Action Items** — who owns what and by when
- **Rationale** — strategic context for each decision
- **Full Checklist** — all action items consolidated in one table

Summaries are also saved to `daily_summaries/YYYY-MM-DD.md` as a permanent record.

## Manual Run

```bash
pip install slack-sdk
SLACK_BOT_TOKEN=xoxb-your-token python3 send_daily_summary.py
```
