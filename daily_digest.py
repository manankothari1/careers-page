#!/usr/bin/env python3
"""
Daily Decision Digest — Chief of Staff Automation
Reads Granola meetings for the current day and sends a Slack digest.

This script handles the Slack-sending portion. The meeting summarization
is done by the Cursor Cloud Agent which calls this script (or uses Slack MCP).

Required environment variables:
    SLACK_BOT_TOKEN: Slack bot token with chat:write scope (starts with xoxb-)
    SLACK_CHANNEL_ID: Override the default channel (default: D06E4QMHCNN)
"""

import os
import sys
import json
import datetime
import urllib.request
import urllib.error


SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID", "D06E4QMHCNN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


def post_slack_message(channel: str, blocks: list, fallback_text: str, token: str) -> dict:
    """Post a rich Block Kit message to Slack."""
    url = "https://slack.com/api/chat.postMessage"
    payload = json.dumps({
        "channel": channel,
        "text": fallback_text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": str(e), "body": e.read().decode()}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def build_no_meetings_blocks(date_label: str) -> list:
    """Build blocks for a day with no recorded meetings."""
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"\U0001f4cb Your Daily Decision Digest — {date_label}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"Hey Manan! \U0001f44b Looks like you had no recorded Granola "
                    f"meetings today ({date_label}). Either it was a heads-down day, "
                    f"a day off, or meetings just weren't captured. Either way — enjoy "
                    f"the quiet! \U0001f60a\n\nCheck back tomorrow for your digest."
                ),
            },
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": (
                        "\u2728 _Your Chief of Staff — powered by Granola & Cursor_ | "
                        f"{date_label} @ 5:00 PM PDT"
                    ),
                }
            ],
        },
    ]


def build_digest_blocks(summary_sections: list[dict], date_label: str) -> list:
    """
    Build Slack Block Kit blocks from structured meeting summary.

    Args:
        summary_sections: List of dicts with keys:
            - title: str (section title)
            - content: str (mrkdwn content)
        date_label: Formatted date string
    """
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"\U0001f4cb Your Daily Decision Digest — {date_label}",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    for section in summary_sections:
        if section.get("title"):
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{section['title']}*",
                },
            })
        content = section.get("content", "").strip()
        # Slack has a 3000 char limit per text block
        while len(content) > 3000:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": content[:3000]},
            })
            content = content[3000:]
        if content:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": content},
            })
        blocks.append({"type": "divider"})

    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": (
                    "\u2728 _Your Chief of Staff — powered by Granola & Cursor_ | "
                    f"{date_label} @ 5:00 PM PDT"
                ),
            }
        ],
    })
    return blocks


def get_pdt_date_label() -> str:
    """Return today's date in PDT as a formatted string."""
    utc_now = datetime.datetime.now(datetime.UTC)
    pdt_now = utc_now - datetime.timedelta(hours=7)
    return pdt_now.strftime("%A, %B %-d, %Y")


def send_digest(blocks: list, date_label: str) -> bool:
    """Send the digest to Slack. Returns True on success."""
    token = SLACK_BOT_TOKEN
    if not token:
        print(
            "ERROR: SLACK_BOT_TOKEN is not set.\n"
            "Add it in Cursor Dashboard \u2192 Cloud Agents \u2192 Secrets.",
            file=sys.stderr,
        )
        return False

    fallback = f"Daily Decision Digest for {date_label}"
    print(f"Sending digest to channel {SLACK_CHANNEL_ID}...")
    result = post_slack_message(SLACK_CHANNEL_ID, blocks, fallback, token)

    if result.get("ok"):
        print(f"\u2705 Digest sent! ts={result.get('ts')}")
        return True
    else:
        print(f"\u274c Slack error: {result.get('error')}", file=sys.stderr)
        if result.get("body"):
            print(result["body"], file=sys.stderr)
        return False


def main():
    """Entry point for manual/test runs."""
    date_label = get_pdt_date_label()

    if "--no-meetings" in sys.argv:
        blocks = build_no_meetings_blocks(date_label)
    elif "--test" in sys.argv:
        blocks = build_digest_blocks(
            [
                {
                    "title": "\U0001f50d Test Section",
                    "content": "This is a test message from the Daily Digest automation. If you're seeing this, the Slack integration is working correctly! \U0001f389",
                }
            ],
            date_label,
        )
    elif not sys.stdin.isatty():
        # Accept raw JSON blocks from stdin
        try:
            data = json.load(sys.stdin)
            blocks = data.get("blocks", [])
        except json.JSONDecodeError:
            print("ERROR: stdin must be valid JSON with a 'blocks' key.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Usage:", file=sys.stderr)
        print("  python3 daily_digest.py --test              # Send test message", file=sys.stderr)
        print("  python3 daily_digest.py --no-meetings       # Send 'no meetings' notice", file=sys.stderr)
        print("  echo '{\"blocks\":[...]}' | python3 daily_digest.py  # Send custom blocks", file=sys.stderr)
        sys.exit(0)

    success = send_digest(blocks, date_label)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
