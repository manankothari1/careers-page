# careers-page

## Daily Decision Summary (Chief of Staff Automation)

`daily_summary.py` runs every day at midnight UTC via Cursor Cloud Agent cron. It:

1. Reviews all Granola meeting notes from the previous day
2. Extracts decisions, rationale, and action items
3. Sends a comprehensive Slack DM to Manan with a summary + next-day priorities

### Setup

Add the following secret in **Cursor Dashboard → Cloud Agents → Secrets**:

| Secret Name  | Value |
|-------------|-------|
| `SLACK_TOKEN` | Your Slack Bot Token (starts with `xoxb-`). Requires `chat:write` scope. |

The Slack DM is sent to channel `D06E4QMHCNN` (Manan's DM).

### Running manually

```bash
SLACK_TOKEN=xoxb-your-token python3 daily_summary.py
```