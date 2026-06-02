# Daily Decision Summary — Slack Automation

Chief of Staff automation for **Manan Kothari** @ Homebase.

Every day at **5pm PT** (midnight UTC), this Cursor Cloud Agent automation:
1. Fetches all Granola meeting notes from today via the **Granola MCP**
2. Extracts decisions, action items, follow-ups, and rationale
3. Posts a beautiful, human-friendly summary to **Slack channel `D06E4QMHCNN`**

## Setup Requirements

### Slack Authentication

The Slack MCP server must be authenticated **OR** a bot token must be added to Cursor Secrets:

**Option A – Authenticate the Slack MCP (recommended):**
1. Go to [Cursor Dashboard](https://cursor.com/dashboard) > Cloud Agents > MCP Servers
2. Find "Slack" and click **Connect / Authenticate**
3. Follow the OAuth flow to connect your Homebase Slack workspace

**Option B – Add a Bot Token secret:**
1. Create a Slack App at [api.slack.com/apps](https://api.slack.com/apps) with `chat:write` scope
2. Install it to your workspace and copy the **Bot Token** (`xoxb-...`)
3. Go to Cursor Dashboard > Cloud Agents > Secrets
4. Add secret: `SLACK_BOT_TOKEN` = `xoxb-your-token-here`

### Granola Authentication
Granola MCP is already connected — no action needed.

## Manual Testing

Once `SLACK_BOT_TOKEN` is set:

```bash
# Send today's no-meetings summary
python3 send_daily_summary.py --no-meetings

# Send a custom message
python3 send_daily_summary.py --message "Custom message here"

# Send from a file
python3 send_daily_summary.py --file summary.txt
```

## How It Works

The automation prompt instructs the agent to:
- Query Granola for all meetings on the current day (in PT timezone)
- If meetings exist: extract and synthesize all decisions, action items, follow-ups
- If no meetings: surface open action items from recent meetings
- Always highlight time-sensitive upcoming commitments
- Send with an encouraging, chief-of-staff voice via Slack

## Slack Channel
- **Channel ID:** `D06E4QMHCNN` (Manan's DM)
