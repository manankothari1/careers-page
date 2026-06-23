# careers-page

## Daily Decision Summary — Slack Automation

This repo contains the daily PM chief-of-staff automation for Manan at Homebase.

### How It Works

A Cursor Cloud Agent cron job fires every day at midnight UTC (5 PM PDT).
The agent:
1. Pulls all Granola meeting notes from the current day
2. Extracts key decisions, action items, and rationale from each meeting
3. Sends a formatted Slack summary to `D06E4QMHCNN`

### Setup Requirements

**Cursor MCP Authentication:**
- **Granola MCP** — authenticate via Cursor Dashboard → Settings → MCP ✅
- **Slack MCP** — authenticate via Cursor Dashboard → Settings → MCP (needed for auto-send)

**OR via Environment Secret (fallback):**
- Add `SLACK_BOT_TOKEN` to Cursor Dashboard → Cloud Agents → Secrets
- The bot must have `chat:write` and `im:write` scopes

### Running Manually

```bash
SLACK_BOT_TOKEN=xoxb-... python3 daily_summary.py
```

### Files

- `daily_summary.py` — standalone script that builds and sends the daily summary
