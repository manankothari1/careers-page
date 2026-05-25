# Daily Meeting Digest — Chief of Staff Automation

A Cursor Cloud Agent that wakes up daily at 5 PM PT, reviews all of Manan's Granola meeting notes from the day, and sends a comprehensive digest to Slack with decisions, action items, follow-ups, and rationale.

## What It Does

Every day at midnight UTC (5 PM PT), this agent:

1. **Fetches** all Granola meeting notes from the current day via the Granola MCP server
2. **Analyzes** each meeting for: key decisions, rationale behind decisions, action items, follow-ups, and risks
3. **Compiles** a structured, human-friendly digest organized by meeting
4. **Sends** the digest to Slack channel `D06E4QMHCNN` (your DM)

## Setup Requirements

### Option A: Slack MCP Server (Recommended)
Authenticate the Slack MCP server in the **Cursor Dashboard → Cloud Agents → MCP Servers**. Once authenticated, the agent uses it automatically.

### Option B: Slack Bot Token (Fallback)
1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add the `chat:write` OAuth scope
3. Install the app to your workspace
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)
5. Add it as a secret in **Cursor Dashboard → Cloud Agents → Secrets** with the key `SLACK_BOT_TOKEN`

## Files

- `daily_digest.py` — Slack sender utility; accepts a message via stdin or CLI args and sends to the configured channel
- `README.md` — This file

## Digest Format

Each daily digest includes:

```
🌟 Hey Manan! Your Chief of Staff is here...

For each meeting:
  📋 Meeting title + time + attendees
  ✅ Key decisions made
  💡 Rationale behind decisions
  ⚠️  Risks / flags
  🎯 Action items (owner + deadline)

🎯 Master action list for the next day/week
📊 Summary stats (# meetings, areas covered, action item count)
```

## Cron Schedule

```
0 0 * * *   (midnight UTC = 5 PM PT)
```

## Notes

- If there are no meetings for the current day (e.g. weekends, holidays), the agent sends a digest of the most recent working day's meetings
- All meeting data is sourced from Granola (requires Granola MCP to be connected and authenticated)
