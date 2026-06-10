# Daily Decision Summary — Chief of Staff Automation

This repository powers a daily Cursor Cloud Agent automation that acts as Manan's chief of staff at Homebase.

## What It Does

Every day at **5 PM PDT**, the automation:
1. Retrieves all Granola meeting notes from the current day
2. Analyzes decisions made, action items, and strategic rationale
3. Sends a comprehensive, formatted summary to Slack channel `D06E4QMHCNN`

## Setup

See [AGENTS.md](./AGENTS.md) for full setup instructions, including how to authenticate Slack.

**Quick start:**
1. Authenticate the Slack MCP in Cursor IDE (Settings → MCP → Slack), OR
2. Add `SLACK_BOT_TOKEN` as a Cursor Cloud Agent secret

## Files

- `AGENTS.md` — Instructions for the daily automation agent
- `slack_helper.py` — Python fallback for sending Slack messages via bot token