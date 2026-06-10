# Daily Decision Summary — Chief of Staff Automation

## What This Does

Every day at 5 PM PDT, this automation:
1. Reviews all of Manan's Granola meeting notes for the current day
2. Compiles a beautifully formatted summary of decisions, action items, and rationale
3. Sends the summary as a Slack DM to channel **D06E4QMHCNN**

## Required Setup

### Slack Authentication (choose one option)

**Option A — Slack MCP (Preferred)**
Authenticate the Slack MCP in your Cursor desktop IDE:
1. Open Cursor → Settings → MCP Servers → Slack
2. Complete the OAuth flow
3. The Slack MCP will then be available in Cloud Agent runs

**Option B — Slack Bot Token (Fallback)**
1. Create a Slack App at https://api.slack.com/apps
2. Add scopes: `chat:write`, `im:write`
3. Install to your workspace and copy the Bot OAuth Token (`xoxb-...`)
4. Add it as a Cursor Cloud Agent secret: `SLACK_BOT_TOKEN`
5. Ensure the bot is added to the DM channel D06E4QMHCNN

The automation will automatically use whichever is available.

## How to Run This Automation Manually

The cron is set to trigger at midnight UTC (5 PM PDT). To trigger manually:
- Go to Cursor → Cloud Agents → Automations → "Daily Decision Summary"
- Click "Run Now"

## Agent Instructions for Daily Run

When this automation triggers, follow these exact steps:

### Step 1: Get Today's Meetings
Use the Granola MCP to list meetings for the current day (in PDT timezone — midnight UTC = 5 PM PDT of the previous calendar day):
```
list_meetings(time_range="custom", custom_start="<TODAY_PDT>T00:00:00-07:00", custom_end="<TODAY_PDT>T23:59:59-07:00")
```
If no meetings today, also check yesterday in case of timezone edge cases.

### Step 2: Get Meeting Details
For each meeting found, call `get_meetings([id1, id2, ...])` to get full summaries and notes.

### Step 3: Compose the Summary
Format a warm, helpful, and motivating message for Manan that includes:
- **Decisions made** (clearly labeled per meeting)
- **Action items** with owners and context (Manan's items numbered + bolded)
- **Rationale** for major decisions (helps Manan speak confidently to them later)
- **Carryover items** from recent past meetings if still relevant
- An **encouraging closing note** — make Manan feel great about their day

### Step 4: Send the Slack Message

**Try in this order:**

1. **Slack MCP** — Use the `send_message` tool to channel `D06E4QMHCNN`
2. **Python fallback** — If the Slack MCP is not authenticated, run:
   ```bash
   python3 /workspace/slack_helper.py "D06E4QMHCNN" "<message>"
   ```
   This requires `SLACK_BOT_TOKEN` to be set as an environment variable.

### Step 5: Confirm Delivery
After sending, confirm the message was delivered and output the summary in your response.

## Slack Formatting Reference

Use Slack markdown in messages:
- `*bold*` for bold text
- `_italic_` for italic
- `:emoji_name:` for emojis
- `>` for blockquotes
- ` ``` ` for code blocks
- Bullet points with `•`

## Target Channel

- Channel ID: `D06E4QMHCNN`
- This is Manan's personal DM (or a designated channel for chief-of-staff updates)

## Contact

- Manan Kothari: mkothari@joinhomebase.com
- Homebase / Joinhomebase
