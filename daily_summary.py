#!/usr/bin/env python3
"""
Chief of Staff Daily Summary - sends Slack Block Kit message to Manan.
Usage: python3 daily_summary.py '<json_payload>'
If SLACK_TOKEN is not set, prints a preview and exits with code 1.
"""
import sys
import os
import json
import urllib.request
import urllib.error

CHANNEL_ID = "D06E4QMHCNN"
SLACK_API_URL = "https://slack.com/api/chat.postMessage"


def send_slack_message(token: str, blocks: list, text: str) -> dict:
    payload = json.dumps({
        "channel": CHANNEL_ID,
        "text": text,
        "blocks": blocks,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        SLACK_API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 daily_summary.py '<json_payload>'")
        sys.exit(1)

    raw = sys.argv[1]
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON payload: {e}")
        sys.exit(1)

    blocks = data.get("blocks", [])
    text = data.get("text", "Daily Decision Summary")

    token = os.environ.get("SLACK_TOKEN", "")
    if not token:
        print("=" * 70)
        print("PREVIEW MODE (SLACK_TOKEN not set)")
        print("=" * 70)
        print(f"Channel: {CHANNEL_ID}")
        print(f"Fallback text: {text}")
        print("-" * 70)
        for block in blocks:
            btype = block.get("type", "")
            if btype == "header":
                txt = block.get("text", {}).get("text", "")
                print(f"\n### {txt}")
            elif btype == "section":
                t = block.get("text", {})
                print(t.get("text", ""))
            elif btype == "divider":
                print("-" * 50)
            elif btype == "context":
                for el in block.get("elements", []):
                    print(f"  [{el.get('text', '')}]")
        print("=" * 70)
        sys.exit(1)

    result = send_slack_message(token, blocks, text)
    if result.get("ok"):
        print(f"Message sent successfully. ts={result.get('ts')}")
    else:
        print(f"Slack API error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
