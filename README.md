# Daily Decision Summary — Chief of Staff Bot

A Cursor Cloud Agent cron automation that runs daily at **midnight UTC (5 PM PDT)** to review all of Manan's Granola meeting notes from the day and send a concise Slack DM with:

- **Decisions made** with rationale
- **Action items** (owner-tagged)
- **Team follow-ups** to track
- **Open questions / risks** to watch

## How It Works

1. **Trigger**: Cursor cron fires at `0 0 * * *` (midnight UTC = 5 PM PDT)
2. **Granola**: The Claude agent fetches all meetings from the current PT day via the Granola MCP tool
3. **Analysis**: Claude compiles decisions, action items, follow-ups, and risks from transcripts and AI summaries
4. **Slack**: The summary is sent as a DM to channel `D06E4QMHCNN` via the Slack API

## Setup

### Required Secret

Add the following to **Cursor Dashboard → Cloud Agents → Secrets**:

| Secret Name       | Description                                      |
|-------------------|--------------------------------------------------|
| `SLACK_BOT_TOKEN` | Slack bot OAuth token with `chat:write` scope    |

The Slack bot must be invited to the DM channel `D06E4QMHCNN` (or the token must belong to the workspace user).

### Granola MCP

The Granola MCP server must be connected and authenticated in your Cursor workspace.

## Standalone Script

`daily_summary.py` can be run independently as a fallback:

```bash
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

If `SLACK_BOT_TOKEN` is not set, the formatted message is printed to stdout.

## Slack Channel

DM Channel ID: `D06E4QMHCNN`
