# Chief of Staff Bot — Daily Decision Brief

This repo powers a daily Slack summary of all Granola meeting notes, sent to Manan every evening. The Cursor Cloud Agent runs on a cron schedule (midnight UTC / ~5pm PDT), reviews every meeting from the day, extracts decisions, action items, and rationale, then DMs the summary to Slack.

## How It Works

1. **Cron trigger** fires at `0 0 * * *` (midnight UTC).
2. The Cursor Cloud Agent reads today's Granola meetings via the Granola MCP.
3. A structured daily brief is compiled (decisions, action items, hypotheses, parking lot).
4. The brief is saved to `summaries/YYYY-MM-DD.md` as a permanent record.
5. The brief is sent to Slack DM channel `D06E4QMHCNN` via the Slack API.

## Setup

### 1. Slack Bot Token (Required)

Add `SLACK_BOT_TOKEN` as a secret in the [Cursor Cloud Agent dashboard](https://cursor.com/dashboard):

- Create a Slack app at https://api.slack.com/apps
- Add the `chat:write` OAuth scope
- Install to the Homebase workspace
- Copy the **Bot User OAuth Token** (`xoxb-...`)
- Add it as `SLACK_BOT_TOKEN` in Cursor Secrets

### 2. Slack MCP (Optional — for richer sending)

Authenticate the Slack MCP server in Cursor IDE under Settings → MCP Servers.

### 3. Granola MCP (Required — already configured)

The Granola MCP server must be authenticated. It is currently working.

## Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Main script: loads summary and sends to Slack |
| `summaries/YYYY-MM-DD.md` | Daily brief archive (one file per day) |

## Manual Run

```bash
# Dry run (print only, no Slack send)
python3 daily_summary.py --date 2026-06-02 --dry-run

# Send for a specific date
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py --date 2026-06-02
```
