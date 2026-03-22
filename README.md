# Chief of Staff — Daily Decision Summary

A Cursor Cloud Agent automation that runs every day at 5:00 PM PT (midnight UTC) and sends Manan a Slack DM summarizing all decisions made, action items, follow-ups, and context from the day's meetings.

## How It Works

1. **Trigger**: Cron fires at `0 0 * * *` (midnight UTC = 5 PM PT)
2. **Agent** queries Granola for today's meetings via MCP
3. **Agent** synthesizes decisions, action items, rationale, and week-ahead context
4. **`daily_summary.py`** POSTs the formatted Block Kit message to Slack

## Setup

### Required Secret

Add `SLACK_TOKEN` in **Cursor Dashboard → Cloud Agents → Secrets**

- Create a Slack Bot at [api.slack.com/apps](https://api.slack.com/apps)
- OAuth scope required: `chat:write`
- Install to your workspace and copy the `xoxb-...` Bot User OAuth Token
- Add as `SLACK_TOKEN` secret (user-scoped so it applies across repos)

### Slack Channel

Messages are sent to DM channel `D06E4QMHCNN`.

## Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Slack sender utility — called by the agent with a pre-built Block Kit JSON payload |

## Message Structure

On days **with meetings**, the message includes:
- Decisions made (what, why, trade-offs)
- Clear action items with owners
- Open/unresolved items
- Motivational close

On days **without meetings** (weekends, travel, etc.):
- Week-ahead priorities
- Overdue action items
- North Star metrics check-in
- Motivational close
