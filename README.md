# Chief of Staff Automation — Manan Kothari

Daily end-of-day Slack briefing for Manan Kothari, PM at Homebase.

## What It Does

Runs every day at midnight UTC (= 5 PM PT). Reviews all Granola meeting notes from the current day, then sends a structured Slack DM covering:

- All decisions made during the day (with rationale)
- Clear action items & owners
- Overdue/carry-forward items
- Priority stack for the next day

On weekends or days with no meetings, it sends a weekly recap + Monday prep briefing.

## Setup

### 1. Add Slack Bot Token

Add a secret named `SLACK_TOKEN` in **Cursor Dashboard → Cloud Agents → Secrets**.

The bot needs the `chat:write` scope and must be invited to the DM channel.

### 2. Cron Schedule

Automation is configured to run at `0 0 * * *` (midnight UTC = 5 PM PT).

## Files

- `send_summary_MMDD.py` — generated fresh each run for the specific date
- `README.md` — this file

## Slack Channel

DM Channel ID: `D06E4QMHCNN`
