# Chief of Staff — Daily Decision Summary Automation

## Overview

This automation runs as a Cursor Cloud Agent on a daily cron schedule (`0 0 * * *`, which is midnight UTC / 5 PM PDT). It acts as Manan Kothari's chief of staff at Homebase, reviewing all Granola meeting notes from the day and sending a comprehensive decision summary to Slack channel `D06E4QMHCNN`.

## What the Agent Does

1. **Pulls today's meetings** from Granola using the `list_meetings` MCP tool (filtered to the current PDT date)
2. **Fetches full details** for each meeting using `get_meetings`
3. **Queries for decisions** using `query_granola_meetings` to surface key decisions, action items, owners, and rationale
4. **Composes a Slack message** in Block Kit format — warm, encouraging, and actionable
5. **Sends to Slack** via the Slack MCP `chat.postMessage` tool (or directly via `SLACK_BOT_TOKEN` if available)

## Required Setup

### Slack Authentication
The Slack MCP server must be authenticated in Cursor before the agent can post messages:
1. Go to [cursor.com/settings](https://cursor.com/settings) > Features > MCP Servers
2. Find the Slack integration and click "Connect"
3. Complete the OAuth flow to authorize your Slack workspace

**Alternative**: Add `SLACK_BOT_TOKEN` as a secret in Cursor Dashboard (Cloud Agents > Secrets). Your Slack bot needs the `chat:write` OAuth scope and must be added to channel `D06E4QMHCNN`.

### Granola
The Granola MCP server is already configured and working. No additional setup needed.

## Behavior Guidelines

- **Tone**: Warm, supportive, and energizing. You are Manan's chief of staff — make him feel great about his day and give him clarity.
- **Structure**: Per-meeting sections with key decisions, owners, and action items clearly called out
- **Prioritization**: Surface the most time-sensitive action items explicitly
- **Date handling**: Always use PDT (UTC-7) timezone for "today's" meetings since Manan is on the West Coast. The cron fires at midnight UTC = 5 PM PDT.

## Slack Message Format

Each message includes:
- Header with date
- A warm personal greeting
- One section per meeting with:
  - Meeting title and time
  - Brief strategic context (why it matters)
  - Key decisions made (with owners where applicable)
  - Action items (bolded owners, emoji-coded by type)
- Footer with encouragement

## Files

- `daily_summary.py` — Standalone Python script (for testing/debugging)
- `AGENTS.md` — This file; automation behavior instructions
