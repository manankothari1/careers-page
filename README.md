# Daily Decision Summary — Chief of Staff Automation

Sends Manan Kothari a Slack DM every evening (5pm PT / midnight UTC) with a summary of all decisions made during the day's meetings, including rationale and action items.

## Setup

### 1. Create a Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps) and click **Create New App → From scratch**
2. Name it something like "Chief of Staff" and pick your Homebase workspace
3. Under **OAuth & Permissions → Scopes → Bot Token Scopes**, add: `chat:write`
4. Click **Install to Workspace** and copy the **Bot User OAuth Token** (starts with `xoxb-`)
5. In Slack, open a DM with the bot (search for it by name) to initialize the channel

### 2. Add the Secret to Cursor

In the Cursor Dashboard: **Cloud Agents → Secrets → Add Secret**

| Key | Value |
|-----|-------|
| `SLACK_TOKEN` | `xoxb-your-token-here` |

### 3. Automation Trigger

The automation is configured with a daily cron: `0 0 * * *` (midnight UTC = 5pm PT).

Each run:
1. Queries Granola for today's meetings
2. Extracts decisions, rationale, and action items
3. Sends a formatted Slack DM to channel `D06E4QMHCNN`

## Files

- `daily_summary.py` — Core script that builds and sends the Slack message
- `run_daily_summary.py` — Integration contract documentation

## Message Format

The Slack message includes:
- Per-meeting decision breakdown with rationale
- Consolidated action items list
- Encouraging closing note
- Graceful "no meetings" message on quiet days
