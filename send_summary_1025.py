#!/usr/bin/env python3
"""
Chief of Staff Daily Digest - Sunday Oct 25, 2026 PDT (5pm PDT = Mon 2am Paris)
No new meetings today. Sunday evening: Week recap + Monday Battle Plan.
"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

def build_payload():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Chief of Staff Daily Digest",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Sunday Oct 25, 2026 | 5pm PDT | Paris: 2am Mon Oct 26*\n_No new meetings today. You had a full weekend. Here's where we stand and exactly what tomorrow looks like._"
            }
        },
        {"type": "divider"},

        # WEEK GRADE
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*WEEK GRADE: A-*\nSolid execution week. Magic Link decided and in flight. Indeed bug contained. Intent capture architecture locked. But you've got two overdue deliverables staring at you right now."
            }
        },
        {"type": "divider"},

        # WEEK DECISIONS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*BIG DECISIONS THIS WEEK (Oct 20-25 PDT)*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*1. OTP IS DEAD - MAGIC LINK WINS*\nFull OTP replacement (not fallback). IBK building, ~1 week dev-done. Old experiment frozen. Staged rollout same split. Rationale: 64% OEM send success is unacceptable -- magic link gets to 100%."
                },
                {
                    "type": "mrkdwn",
                    "text": "*2. INDEED COMPANY FIELD BUG - CONTAINED*\nBob's PR merged Oct 22. Company field temporarily paused. Rationale: stop the bleeding while you work the proper fix. Second bug (fraud-flagged 'do not syndicate' jobs still syndicating) still open with Bob/Carlo."
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*3. HIRING INTENT CAPTURE ARCH - LOCKED*\nJD rules decided (1 hire vanilla / 2+ hires 'multiple' / urgency <=2wk 'urgently hiring'). Divij + Sina starting next sprint. JD rules doc still OUTSTANDING -- Divij is blocked on you."
                },
                {
                    "type": "mrkdwn",
                    "text": "*4. ENTITLEMENTS ROLLOUT - RESUMING*\nStarting Mon Oct 26 at 1%, Wed Oct 28 at 5% (Adam Hewitt). After being paused. Watch for noise from billing/CS teams as it ramps."
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*5. HBA BERNAL BAKERY INTERVIEW*\nTop gaps confirmed: read-only (#1), bulk edits (#1 request), mobile access critical, memory/teachability high interest. 183 ever / 28 active (~2%). Evolve vs rebuild POC still in progress."
                },
                {
                    "type": "mrkdwn",
                    "text": "*6. APPLICANT EMAIL FIX + JOBCASE PARKED*\nIszael taking over applicant email fix from Aaron. Jobcase formally parked -- Iszael closing out."
                }
            ]
        },
        {"type": "divider"},

        # OVERDUE ALERTS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":rotating_light: *OVERDUE RIGHT NOW - YOU OWN THESE*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":red_circle: *JD RULES FOR DIVIJ -- CRITICAL, BLOCKING SPRINT*\nWas due this weekend. Divij is sitting idle waiting for this to start the data pipeline work. Write and send tonight or absolute first thing Monday.\n\nThe rules:\n• 1 hire, ~30 days = vanilla JD, no change\n• 2+ hires = 'multiple [role] positions available'\n• urgency <=2 weeks (ASAP/1wk/2wk) = 'urgently hiring'\n• Vanilla (1 hire, >2 wk) = no change\n\nStill TBD: posted date vs activated date as urgency reference; definition of ASAP. Make a call -- don't let perfect be the enemy of shipped."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":red_circle: *2029 VISION ONE-PAGER -- JOHN IS WAITING*\nBoard meeting opened Oct 15. Fadi submitted his. Yours is missing. This is a C-suite deliverable with your name on it -- block 90 minutes tonight or first thing Monday. Non-negotiable."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":yellow_circle: *INDEED SUPPORT REPLY -- 4 DAYS OUTSTANDING*\nDraft and send your Indeed support reply re: company field bug. Bob is updating Michael, but you need to own the Indeed relationship piece."
            }
        },
        {"type": "divider"},

        # MONDAY BATTLE PLAN
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":crossed_swords: *MONDAY OCT 26 BATTLE PLAN*\n_Jatin is back. This is a high-leverage day._"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*BEFORE STANDUP (PDT morning / CEST afternoon):*\n:fire: *1. Ping Jatin FIRST THING* -- Soheil is missing from standup invite. Fix it before standup starts or Soheil misses another week.\n\n:fire: *2. Facebook API -- ESCALATE TODAY* -- Day 31, zero movement since Oct 9. IBK + Bob loop. This has been on the watch list 31 days. It's time to make noise. Escalate to Skye if needed.\n\n:fire: *3. Indeed XML Feed with Jatin* -- Make it private immediately. Jatin is back, this is conversation #1. Medium-term migration path: JobSync API."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*DURING THE DAY:*\n4. :handshake: *Matt McAllister (new CMO)* -- Week 2 starts today. He's from Yelp and you have zero relationship yet. Get 30 mins on calendar before end of week.\n\n5. :thinking_face: *Spec Swarm N+1 Decision* -- Decide with Fadi TODAY: bring hiring count+speed into next Swarm or wait N+2? Must be decided BEFORE Tuesday's GTM Lookahead with Matan. Don't walk into that meeting without a position.\n\n6. :mega: *Pre-align Matan + Skye before Tuesday GTM* -- Research opacity issue (rewrites without product input). Have the conversation with Skye now so Tuesday isn't a surprise.\n\n7. :lock: *Magic Link check-in with IBK* -- Confirm four pending items: link expiry time, email send/fail monitoring, active-tab JS detection, new experiment key registration. Also tag Fatty for Verify CTA designs.\n\n8. :calendar: *Nihilus subscription* -- Nov 3 deadline = 8 DAYS. Did Izzy scope the build cost? Need this to make the Q4 vs Q1 removal decision. Chase if no update.\n\n9. :clock9: *Fadi sync 9:30am PT* -- Confirm the recurring invite is actually on Fadi's calendar.\n\n10. :eyes: *Entitlements rollout* -- Adam Hewitt's team starts 1% today. No action needed but ears open for CS/billing noise."
            }
        },
        {"type": "divider"},

        # WATCH LIST ALERTS
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":warning: *WATCH LIST -- THINGS THAT WILL BITE YOU*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "• :hourglass_flowing_sand: *NIHILUS: Nov 3 = 8 DAYS* -- $8K/month now, $100K+/yr at scale. Decision: stay Q4, remove Q1. Izzy scoping cost.\n• :baby: *CARLO KT* -- Paternity through mid-Feb. He has critical institutional knowledge. No KT confirmed = knowledge RISK. Don't let this wait another week.\n• :robot_face: *COMMS ASSISTANT production decision* -- Malcolm leaving Nov-Dec. Decision OVERDUE.\n• :document: *DEPARTURES SIGNAL DOCS* -- 30+ days overdue. Zane, Sean, Jon W, Bobby.\n• :mag: *ORCA COMMS QA* -- Matan built the skill. Needs manual QA with IBK. Easy win, just schedule it.\n• :handshake: *WELCOME TECH PILOT* -- Agreed Oct 20. Manan + Skye still need to shortlist pilot employers.\n• :gift: *GIFT CARDS OWED* -- Lola E. Erickson ($50), Michele Landry ($50), Ryan Reilly ($50). Send these.\n• :email: *UNSENT EMAILS* -- John Waldman (EarnBetter NDA), Marina/Mundo Academy (27+ days). Send tomorrow."
            }
        },
        {"type": "divider"},

        # METRICS SNAPSHOT
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":bar_chart: *METRICS SNAPSHOT (as of week end)*\n• FFH paying: ~210 (Q4 goal: 500) | Capture rate: ~7-8%\n• Indeed: *RECOVERED* (Day 63) | ZipRecruiter: ~11,500 apps/wk\n• D5 zero-applicant rate: 41% | Healthy job rate: 30% (target: 80%)\n• Magic Link: OTP → 64% success → target 100%\n• Facebook API: *STILL DOWN* Day 31\n• HBA: 183 ever / 28 active (~2%)"
            }
        },
        {"type": "divider"},

        # CLOSING
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":sunrise: *YOU'VE GOT THIS.*\nIt's 2am Paris time but Monday morning is going to come fast. Jatin is back, the team is in motion, and you have two deliverables (JD rules + 2029 one-pager) that only you can unblock. Knock those out and Monday runs itself.\n\n_See you at 5pm PDT tomorrow. -- Your Chief of Staff_"
            }
        }
    ]

    return {
        "channel": CHANNEL,
        "text": "Chief of Staff Digest: Sunday Oct 25 | Monday Battle Plan",
        "blocks": blocks
    }


def preview(payload):
    sys.stdout.buffer.write(
        ("\n=== SLACK PREVIEW (no token available) ===\n\n" +
         json.dumps(payload, indent=2, ensure_ascii=False) +
         "\n\n=== END PREVIEW ===\n").encode("utf-8", errors="replace")
    )


def send_slack(payload, token):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body
    except urllib.error.URLError as e:
        return {"ok": False, "error": str(e)}


def main():
    payload = build_payload()

    token = (
        os.environ.get("SLACK_TOKEN") or
        os.environ.get("SLACK_BOT_TOKEN") or
        os.environ.get("SLACK_API_TOKEN") or
        ""
    ).strip()

    if not token:
        print("No SLACK_TOKEN found -- preview mode.")
        preview(payload)
        sys.exit(0)

    print("Sending to Slack...")
    result = send_slack(payload, token)
    if result.get("ok"):
        print(f"SUCCESS: message sent, ts={result.get('ts')}")
    else:
        print(f"FAILED: {result.get('error')}")
        preview(payload)
        sys.exit(1)


if __name__ == "__main__":
    main()
