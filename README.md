# Granola Daily Call Summary — Chief of Staff Automation

A Cursor Cloud Agent that wakes up every day at **5pm PDT** (midnight UTC), reviews all of Manan's Granola meeting notes for the day, and sends a comprehensive briefing to Slack with decisions made, action items, follow-ups, and rationale.

## What It Does

Every evening it:
1. Queries the **Granola MCP** for all meetings captured that day
2. Synthesizes each meeting's notes into decisions, action items, and context
3. Posts a rich, structured briefing to the Slack DM channel `D06E4QMHCNN`

The message includes:
- **Key Decisions Made** — with rationale for each choice
- **Action Items & Follow-Ups** — prioritized, attributed, and time-boxed where possible
- **Situational Awareness** — risks, blockers, and context worth tracking
- **Meeting Roster** — quick reference for what was covered and with whom

## Setup Requirements

### 1. Granola MCP
The Granola MCP server must be connected and authenticated in Cursor Settings.
The account `mkothari@joinhomebase.com` (Homebase workspace) is expected.

### 2. Slack — choose one option

**Option A: Slack MCP (preferred)**
Authenticate the Slack MCP server in Cursor Settings > MCP Servers.
Once authenticated, the Cloud Agent uses it directly — no token needed.

**Option B: Slack Bot Token**
1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps)
2. Add OAuth scopes: `chat:write`, `im:write`
3. Install to the Homebase Slack workspace
4. Copy the Bot User OAuth Token (`xoxb-...`)
5. Add it as a secret in **Cursor Dashboard > Cloud Agents > Secrets**:
   - Key: `SLACK_BOT_TOKEN`
   - Value: `xoxb-your-token-here`
6. Invite the bot to the DM channel (`/invite @your-bot` in the DM)

### 3. Cron Schedule
The automation is triggered by a Cursor Cloud Agent cron:
```
0 0 * * *   (midnight UTC = 5pm PDT)
```

## Standalone Testing

```bash
SLACK_BOT_TOKEN=xoxb-your-token python3 daily_summary.py
```

Without the token the script prints the message that would have been sent.

## Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Main script: message builders + Slack sender |
| `README.md` | This file |

## Slack Channel

DM Channel ID: `D06E4QMHCNN` (Manan Kothari's personal DM)
