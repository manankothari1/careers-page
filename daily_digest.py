"""
Daily digest sender for Manan Kothari's chief-of-staff automation.
Sends Slack Block Kit messages to DM channel D06E4QMHCNN.
"""
import json
import os
import sys
import urllib.request
import urllib.error


CHANNEL = "D06E4QMHCNN"


def get_token():
    for var in ("SLACK_TOKEN", "SLACK_BOT_TOKEN", "SLACK_API_TOKEN"):
        t = os.environ.get(var, "").strip()
        if t:
            return t
    return None


def send_blocks(blocks: list, text: str = "Daily digest") -> dict:
    token = get_token()
    if not token:
        print("[PREVIEW — no SLACK_TOKEN set]")
        preview(blocks, text)
        return {}

    payload = json.dumps({
        "channel": CHANNEL,
        "text": text,
        "blocks": blocks,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                print(f"Sent to Slack: {result.get('ts')}")
            else:
                print(f"Slack error: {result.get('error')}", file=sys.stderr)
            return result
    except urllib.error.URLError as e:
        print(f"Network error: {e}", file=sys.stderr)
        return {}


def preview(blocks: list, text: str):
    out = f"\n{'='*60}\nPREVIEW: {text}\n{'='*60}\n"
    for b in blocks:
        btype = b.get("type", "")
        if btype == "header":
            out += f"\n### {b['text']['text']}\n"
        elif btype == "section":
            t = b.get("text", {})
            out += f"\n{t.get('text','')}\n"
        elif btype == "divider":
            out += "-" * 50 + "\n"
        elif btype == "context":
            for el in b.get("elements", []):
                out += f"  > {el.get('text','')}\n"
    sys.stdout.buffer.write(out.encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")
