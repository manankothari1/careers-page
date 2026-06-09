# Daily Decision Summary — Chief of Staff Automation

Automated daily end-of-day brief for Manan Kothari (PM at Homebase).

Runs via Cursor Cloud Agent on cron `0 0 * * *` (midnight UTC = 5 PM PDT).
Reviews all Granola meeting notes for the day and posts a decision summary to Slack channel `D06E4QMHCNN`.

## Setup

1. **Slack**: Authenticate the Slack MCP server in Cursor settings, OR add `SLACK_BOT_TOKEN` as a secret in Cursor Dashboard → Cloud Agents → Secrets (bot needs `chat:write` scope)
2. **Granola**: Already configured and working via Cursor MCP

## Local Testing

```bash
pip install -r requirements.txt
SLACK_BOT_TOKEN=xoxb-your-token python daily_summary.py
# or dry run:
python daily_summary.py --dry-run
```

See `AGENTS.md` for full automation behavior documentation.