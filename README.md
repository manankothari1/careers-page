# Daily Decision Summary — Chief of Staff Automation

A Cursor Cloud Agent automation that runs every day at **midnight UTC (5:00 PM PDT)**, reviews all Granola meeting notes from the day, and sends a rich Slack summary of decisions, action items, follow-ups, and rationale.

## What it does

Every evening the agent:

1. Queries **Granola** (via MCP) for all meetings recorded that day
2. Reads the full AI-generated summaries and notes for each meeting
3. Synthesises a comprehensive briefing covering:
   - Every decision made, with rationale
   - Manan's personal action items with clear ownership
   - Team action items to track
   - Key open questions that still need answers
4. Posts a rich **Slack Block Kit** message to channel `D06E4QMHCNN`

## Setup

### 1. Authenticate the Slack MCP server

Open **Cursor Desktop → Settings → MCP Servers → Slack** and complete the OAuth flow for your Slack workspace. This gives the Cloud Agent permission to post messages.

### 2. (Optional) Add a Slack bot token for the standalone script

If you want to run `daily_summary.py` locally or as a fallback:

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App**
2. Add OAuth scope: `chat:write`
3. Install to workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
4. Add it to **Cursor Dashboard → Cloud Agents → Secrets** as `SLACK_BOT_TOKEN`

### 3. Cron schedule

The automation is triggered by Cursor's built-in cron:

```
0 0 * * *   (midnight UTC = 5:00 PM PDT)
```

No additional configuration needed — the cron trigger is defined in the Cursor automation dashboard.

## Standalone script

`daily_summary.py` is a self-contained Python implementation that mirrors what the Cloud Agent does. Run it locally to test or regenerate a past day's summary:

```bash
pip install requests
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

Without `SLACK_BOT_TOKEN` it prints the full Block Kit JSON to stdout so you can inspect the message format.

## Message structure

```
┌─ Header: "Your Daily Decision Briefing — <date>"
├─ Intro: meeting count, decision count, action item count
├─ DECISIONS MADE TODAY
│   └─ One block per decision: title · source meeting · decision · rationale · owners
├─ YOUR ACTION ITEMS (Manan owns)
│   └─ Numbered list with owner and context
├─ TEAM ACTION ITEMS TO TRACK
│   └─ Two-column grid: owner → task
├─ KEY OPEN QUESTIONS
└─ Closing note
```

## Requirements

- Python 3.10+
- `requests` library (`pip install requests`)
- Granola MCP server (configured in Cursor)
- Slack MCP server **authenticated** in Cursor Desktop, or `SLACK_BOT_TOKEN` secret
