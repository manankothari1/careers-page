#!/usr/bin/env python3
"""Daily Chief of Staff Summary - April 20, 2026"""
import json, os, sys, urllib.request, urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🌟 Chief of Staff Daily Brief — Monday, April 20",
            "emoji": True
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "*4 meetings reviewed* · Hiring Leads Standup · Half-Baked Demos · Manan/Malcolm x2 · You crushed today, Manan 💪"
            }
        ]
    },
    {"type": "divider"},

    # ── SECTION 1: DECISIONS MADE ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯 DECISIONS MADE TODAY*"
        }
    },

    # Decision 1
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*1. Predicted Roles → Approach 1 (chip/button → job creation flow) is the recommended path*\n_Rationale:_ Approach 2 (pre-created live jobs) is blocked by a hard technical constraint — you cannot edit syndication settings on a live job, and you'd need business profiles, calendar user IDs, and a brand-new syndication feature. Approach 1 (show predicted role card on careers page → click activates → routes to page 2 of job creation flow) reuses existing patterns, takes ~1 week with 1 FE + 1 BE dev, scales to ALL new businesses via a reusable table, and has zero syndication risk.\n_Status:_ ✅ Recommendation made. Final call due *Wednesday* after sync with Cindy."
        }
    },

    # Decision 2
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*2. TLWA — Open Positions section defaults to General Application (not predicted roles)*\n_Rationale:_ Predicted roles are deprioritized behind boost pathways migration. General application placeholder ships with the TLWA flow. If Ray can generate a simple role name CSV in 1 day, could swap in later — but *not in scope for launch*.\n_Status:_ ✅ Locked. IBK + Fadi implement general application card."
        }
    },

    # Decision 3
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*3. TLWA careers page — Homebase nav REMOVED; opens in new tab*\n_Rationale:_ Career page is an external-facing page. No side nav, no top nav (try hiring assistant bar), no Homebase branding chrome. Currently opens in new tab from dashboard — confirmed correct behavior.\n_Status:_ ✅ Carlo removes nav. Confirmed by Manan in demo."
        }
    },

    # Decision 4
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*4. Multi-image upload on career page → DESCOPED for launch*\n_Rationale:_ Edge cases around failed partial uploads, oversized images, and UX complexity make this risky under time pressure. Single-at-a-time upload ships; multi-select is V2.\n_Status:_ ✅ Locked. Carlo proceeds with single upload only."
        }
    },

    # Decision 5
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*5. Career page embed code → DESCOPED to V2*\n_Rationale:_ Time constraints. Not required for TLWA launch.\n_Status:_ ✅ Locked."
        }
    },

    # Decision 6
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*6. TLWA page style buttons — font families should change per style in preview pills*\n_Rationale:_ Currently all pills show the same font, defeating the purpose of previewing different styles. Small UX improvement, ~2 seconds in Figma → dev.\n_Status:_ ✅ IBK to implement. Fadi to pull SVGs/fonts from Figma."
        }
    },

    # Decision 7
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*7. Resume Scoring V2 — Top Match threshold set at 0.32 minimum on BOTH resume + screener scores*\n_Rationale:_ Divij's 6-criteria scoring model (role relevance, experience quality, avg tenure, skills match, education, certifications) combined with screener scores. 0.32 floor prevents over-flagging false positives (current system: 86% FPR). Users will NOT see scores — label-based UI only.\n_Status:_ ✅ Algorithm locked. Endpoint delivery to HB1 TBD (Manan owes Divij the endpoint)."
        }
    },

    # Decision 8
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*8. TLWA V1→V2 migration: Ugo (contractor) starts TOMORROW*\n_Rationale:_ Migration was overdue since Apr 17. Ugo is confirmed to begin Tuesday. Switcher experience: expand existing banner to non-live job holders, remove checkout modal, copy + visual refresh needed (current 3% vs competitor 5% conversion).\n_Status:_ ✅ Unblocked. Dana on copy, Fadi + Cindy on switcher design."
        }
    },

    # Decision 9
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*9. Post-core TLWA priority order locked: Boost messaging → Boost purchase → Predicted roles*\n_Rationale:_ Core features (careers page, screener gating, Indeed 3LO, winners experience, V1→V2 migration) ship this week. Boost pathways migration comes first after core is complete.\n_Status:_ ✅ Team aligned in standup."
        }
    },

    # Decision 10
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*10. Supabase DB integration into HB1 — target completion Thursday*\n_Rationale:_ Must protect existing OEM career page customizations. Addresses need verification before migration.\n_Status:_ 🔄 In progress. Manan to review data requirements with Jatin today."
        }
    },

    {"type": "divider"},

    # ── SECTION 2: ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*⚡ ACTION ITEMS — ON YOU, MANAN*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *[TODAY]* Review Supabase data requirements with Jatin — what fields, what addresses, what needs protecting before HB1 migration\n• *[WEDNESDAY]* Finalize predicted roles approach (Approach 1 vs 2) — talk to Cindy first, then bring decision to team + formal grooming with Malcolm\n• *[OVERDUE — SEND NOW]* TLWA/Launch Week brief to Ted — 19+ days overdue. Drop everything and send this.\n• *[ASAP]* Greenlight Manual Mode — Cindy QA is done, ball is in your court. One email.\n• *[CRITICAL]* Homebase Boost SKU kick-off with Chris McIntosh — billing window is closing. This cannot wait.\n• *[TODAY]* Give Divij the endpoint he needs for resume scoring integration into HB1\n• *[TODAY]* Matan to post Boost plan update to #leads (Phase 1 vs Phase 2 rationale for Ray) — confirm this happened\n• *[ASAP]* Confirm logo max width/height specs for IBK — needed to complete TLWA careers page logo display\n• *[ASAP]* Add Cindy to careers page for design QA once Tanner + Carlo wrap their sprints\n• *[ASAP]* Audit Talroo feed for Manual Mode customer jobs — spending $35/job on $30/mo customers. URGENT spend risk."
        }
    },

    {"type": "divider"},

    # ── SECTION 3: TEAM ACTION ITEMS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*👥 ACTION ITEMS — YOUR TEAM*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *IBK:* Fix TLWA page style pills so font families change per style. Confirm QR code redirect goes to careers page on rescan (not flow restart).\n• *Tanner:* Fix Indeed 3LO auth redirect (broken in demo). Andrew's last week — get auth flow 100%, credential lifecycle, job status sync API, employer dashboard links, confirmation emails.\n• *Andrew:* Everything already built — finish integration this week. Auth redirect fix is P1.\n• *Carlo:* Remove Homebase nav from career page. Post decisions + next steps in project channel. Sync with Iszael on banner display logic.\n• *Malcolm:* Available for formal grooming on predicted roles approach once Manan gives the call Wednesday.\n• *Fadi:* Grab time with Cindy this afternoon on V1→V2 switcher design. Pull font SVGs from Figma for page style pills.\n• *Dana:* Copy + visual review for V1→V2 banner/switcher.\n• *Ugo (contractor):* V1→V2 migration kicks off TOMORROW (Tuesday).\n• *Divij:* Predicted roles work in progress. Pause until Manan confirms approach Wednesday.\n• *Jatin:* Send migration requirements list for cross-reference with Supabase data. Sync with Malcolm on job creation flow for predefined roles."
        }
    },

    {"type": "divider"},

    # ── SECTION 4: OPEN DECISIONS / NEEDS INPUT ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🚨 OPEN DECISIONS STILL HANGING (your call)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Predicted roles approach* — Approach 1 vs 2. Decision due *Wednesday*. (Malcolm recommends Approach 1, but you own this.)\n• *Multi-location company handling* — Do you start predicted roles only for single-location companies and solve multi-location after seeing success? Open question raised today.\n• *V1 migration for TLWA award winners* — 50% of V1 users are award winners, 75% with live jobs. Ugo starting tomorrow, but the big question (exclude from mailer? optional migration? build generic role plumbing?) still needs your call.\n• *Talroo CPA — send categories to Saja* — Campaign can't switch until you send recommended categories + she configures it. Clock is ticking on spend efficiency.\n• *QR code mailers — Cassy* — Confirm mailable address count. ~3k flagged unmailable. Print job can't finalize without this.\n• *Predictive role timeline — Divij* — Time-boxed to EOD Apr 17. Is it still alive? Confirm yes/no for TLWA scope."
        }
    },

    {"type": "divider"},

    # ── SECTION 5: TLWA TIMELINE SNAPSHOT ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📅 TLWA CORE FEATURE SCHEDULE (as of today)*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• *Tomorrow (Tue Apr 21):* Careers page code complete · V1→V2 migration starts (Ugo) · Indeed 3LO auth tokens ready\n• *Wednesday (Apr 22):* Screener gating (pending S3/Supabase migration) · Predicted roles decision from Manan\n• *Thursday (Apr 23):* Supabase DB integration into HB1\n• *After core:* Winners experience → Boost messaging → Boost purchase → Predicted roles\n• *Buffer:* Features won't launch until after all core work + polish = extra week buffer 💪"
        }
    },

    {"type": "divider"},

    # ── SECTION 6: MOMENTUM / BRIGHT SPOTS ──
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*✨ BRIGHT SPOTS*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "• The Half-Baked Demos were *genuinely impressive* — IBK's TLWA flow with OTP auth, animated careers page, and screener integration is beautiful and nearly done. Fadi's designs are top tier.\n• Divij's resume scoring V2 is *real-time, auditable, and LLM-powered* — each of the 6 criteria has reasoning + resume excerpts for explainability. This is going to meaningfully move hiring quality signal.\n• Andrew's Indeed 3LO work is almost entirely built — just needs integration. You're going to ship this.\n• API photo scraping went from hours + high cost to *$45/month* using headless browser + Claude. Nelson's team is finding leverage everywhere.\n• V1→V2 migration UNBLOCKED with Ugo starting tomorrow — the overdue item is finally moving.\n• You're sitting at *$650K ARR, up 44% since January*. The team is building at a pace that matches the moment. Let's keep it rolling. 🚀"
        }
    },

    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "📋 _Chief of Staff bot · 4 Granola meetings reviewed · Cron triggered 5pm PT · All decisions captured_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Brief — Monday April 20, 2026"
}

def preview():
    sys.stdout.buffer.write(
        json.dumps(payload, indent=2).encode("utf-8", errors="replace")
    )
    sys.stdout.buffer.write(b"\n")

def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {SLACK_TOKEN}"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print(f"✅ Slack message sent! ts={body.get('ts')}")
            else:
                print(f"❌ Slack error: {body.get('error')}")
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Network error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not SLACK_TOKEN:
        print("⚠️  SLACK_TOKEN not set — printing preview only")
        preview()
    else:
        send()
