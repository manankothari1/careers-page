# careers-page

---

## Chief of Staff — Daily Decision Summary Bot

A Cursor Cloud Agent automation that runs every day at **5pm PDT**, reviews all your Granola meeting notes, and sends you a rich Slack digest with decisions, action items, rationale, and priority follow-ups.

### What it does

Every evening at 5pm PDT the bot:
1. Pulls all your Granola meeting notes from the day
2. Extracts decisions, action items, owners, and rationale from each meeting
3. Composes a beautiful, structured Slack message and sends it to your DM

### Setup

#### 1. Granola API Key
- Open the Granola desktop app
- Navigate to **Settings → Connectors → API keys**
- Click **Create new key**, select *Personal notes* scope
- Copy the key and add it to Cursor as a secret named `GRANOLA_API_KEY`

#### 2. Slack Bot Token
- Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app (or use an existing one)
- Under **OAuth & Permissions**, add the `chat:write` scope
- Install the app to your workspace and copy the **Bot User OAuth Token** (starts with `xoxb-`)
- Add it to Cursor as a secret named `SLACK_BOT_TOKEN`
- Alternatively: authenticate the **Slack MCP server** in Cursor (Settings → MCP)

#### 3. Slack Channel ID
- The default channel is `D06E4QMHCNN` (your DM)
- Override with the `SLACK_CHANNEL_ID` environment variable/secret if needed

### Running manually

```bash
pip install -r requirements.txt
GRANOLA_API_KEY=grn_... SLACK_BOT_TOKEN=xoxb-... python daily_summary.py
```

### Files

| File | Purpose |
|------|---------|
| `daily_summary.py` | Standalone automation script (Granola API + Slack API) |
| `requirements.txt` | Python dependencies |
| `today_summary.md` | Latest generated summary (updated each run) |