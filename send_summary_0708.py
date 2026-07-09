#!/usr/bin/env python3
"""Daily decision digest — Wednesday Jul 8, 2026"""
import json
import os
import sys
import urllib.request
import urllib.error

CHANNEL = "D06E4QMHCNN"

TOKEN = (
    os.environ.get("SLACK_TOKEN")
    or os.environ.get("SLACK_BOT_TOKEN")
    or os.environ.get("SLACK_API_TOKEN")
    or ""
)

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Chief of Staff Daily Digest — Wednesday Jul 8 🗓️",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey Manan! What a packed Wednesday — 3 meetings, a major Q3 goal rewrite, a critical root-cause confirmed, and a promising screener experiment lighting up the metrics. You are absolutely *crushing it*. Here's everything you decided today, why it matters, and exactly what needs to happen next. Let's go 🚀"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Today at a glance* | 3 meetings · ~17 decisions · 5 personal action items"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 1 of 3 — Hiring Leads Standup* (8:45 AM)\n_Attendees: Fadi, Dana, Matan, Jatin, Ray, Nelson, Jeff, Usman_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 1: Experiment audience narrowed to trial-period FFH users only*\n_Why:_ Targeting all FFH users includes long-tenured hiring staff (1.5+ year customers) who aren't comparable to the ICP you're trying to move. Limiting to trial users = cleaner signal, more actionable results.\n*Action → You:* Make sure this is scoped in the experiment setup before the next run."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 2: Loom voiceover standard adopted for significant tickets*\n_Why:_ Engineering tickets with Looms from prior cycles saved weeks of alignment — scheduling alone went Mon→Thu before shipping. Preserving institutional knowledge as the team scales.\n*Action → Fadi:* Add Loom to current ticket. *Action → You:* Reinforce this expectation in team norms going forward."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 3: Weekly 45-min Thursday 1:1 to be scheduled*\n_Why:_ Mirrors the rhythm already set up with Dana — consistent touchpoints prevent drift on fast-moving work.\n*Action → You:* Block a 45-min Thursday slot this week. (Who is this with — Abby, Ray, or someone else?)"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 2 of 3 — Indeed Job Posting Visibility w/ Chris* (12:46 PM)\n_One-on-one field intelligence call_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 4: Do NOT repost PJs Coffee (barista, Montgomery TX) — advise customer job is live*\n_Why:_ Reposting triggers Indeed's duplicate detection → likely zero applicants. The job IS indexed (you confirmed via incognito search). Drop in applicants (70 → 11) is likely due to job aging + Indeed's opaque relevance algorithm — not a posting error. The risk of reposting outweighs the potential upside.\n*Action → Chris:_ Tell customer the job is live and getting visibility. If she wants to gamble on a repost, make sure source claiming is in place first so you can catch a flagging event immediately.*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 5: Self-serve source claiming is the right long-term path — validated by field*\n_Why:_ Chris has already coached ~3 customers through manual source claiming successfully. The in-product 3LO flow you described (OEM adds Indeed email → Homebase passes partner code → Indeed verifies → source claiming live) matches exactly what reps are doing manually. The product just formalizes it.\n*Action → You:* Follow up with Michael and Cornelius on their Indeed cases — use their responses as more field validation."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 6: Scooter's Coffee banned Indeed account — Friday 3-way call*\n_Why:_ Anomalous case (account banned before ever being created). Chris owns this one — a data point worth flagging to Indeed on account provisioning bugs.\n*Watch → Chris:* Friday call with Indeed + customer. Ask for an update Monday."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 7: AstraChic franchise interest flagged — do not lose this thread*\n_Why:_ A1 wants to push hiring bundles to franchise accounts but is gating on Indeed visibility reliability. This is a revenue-adjacent signal — franchise bundles at scale are a big GTM opportunity.\n*Action → You:* When A1 Slacks you, treat it as a high-priority conversation. Loop in Dana before she leaves in September."
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*📋 Meeting 3 of 3 — Manan / Fadi Applicant Flow Roadmap Chat* (2:00 PM)\n_One-on-one roadmap deep-dive_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 8: Q3 goals completely rewritten — old buckets retired*\n_Old goals:_ OEM spend / Talent pool / Optimize funnel\n_New goals (as of today):_\n• 1️⃣ FFH jobs with zero Indeed applicants on D5 < 10% _(currently 41% — enormous gap)_\n• 2️⃣ 50% of line cook jobs healthy by D30 _(currently ~8%)_\n• 3️⃣ Screener completions +50% relative\n_Why:_ The old framing was activity-oriented; the new goals are outcome-oriented with a specific ICP focus. 41% zero-applicant rate at D5 is the clearest signal of broken supply — fixing it is the entire job.\n*Action → You:* Make sure the updated goals are documented in the team wiki / sprint board this week."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 9: Screener personalization experiment — roll out with scrutiny*\n_Results:_ Screener lands: low 60s → 70-80%. Screener starts: ~43% → ~50%. Winning variant: OEM-framed mandatory language.\n_Why:_ Gains are real but feel large — you noted healthy skepticism. Deliverability improvement is a confounding factor. Rolling out is the right call, but the name normalization cleanup (all-caps / business names) must ship alongside or the personalization breaks.\n*Action → You:* Flag name normalization as a follow-up ticket before full rollout. Ask Rami/Fadi to add cleanup before next batch goes out."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 10: Line cook three-pronged attack — strategy locked*\n• All talent pool outreach concentrated on line cook roles\n• Niche boards: Culinary Agents (more promising) + Poached (mixed)\n• Tradeoff accepted: narrow focus on line cook = better signal, less generalizability\n_Why:_ Line cook is ~8% healthy vs. 60-70% for cashier. It's the largest unsolved problem and the highest-leverage target.\n*Action → You:* Confirm Rami's outreach script has been rerun on non-line-cook jobs (this was from Jul 7 — close the loop)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 11: Root cause of zero Indeed applicants officially confirmed*\n_Root cause:_ OEM copy-job flow triggers Indeed duplicate detection → ~50% of copied jobs hit zero Indeed applicants by D5. Customers have no visibility into this flag; they blame Homebase.\n_Why this matters:_ This is the single biggest driver of the 41% D5 zero-applicant rate. Every day we don't fix the copy→reactivate flow, we're burning customer trust.\n*No new action (was already in motion) — just critical that it ships fast.*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 12: Three-part source claiming fix — all three tracks active simultaneously*\n• Track A: Replace copy job → reactivate job flow (Tanner owns)\n• Track B: Matan + Sean now equipped to do manual source claiming (guide written)\n• Track C: Self-serve 3LO + source claiming in product (Fadi designs, Matan eng)\n_Why:_ These tracks are parallelizable. Track B is immediately live and can start saving customers today. Track C is the long-term moat.\n*Action → You:* Confirm Matan has the guide and has started Track B outreach. Sign off on the Source Claiming Banner E2E (was pending your signoff as of yesterday)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decision 13: Figma design review for 3LO + source claiming flow — tomorrow 3:45-4:30pm*\n_Why:_ Designs are mostly done; session is to align on self-serve vs. book-a-call path tweaks and scope Fadi's design workload.\n*Action → You:* Block 3:45-4:30pm tomorrow on your calendar. Come with a clear POV on where self-serve ends and where 'book a call' begins."
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🎯 Your Personal Action List — Thursday Jul 9",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here's your clean TODO list for tomorrow, in priority order:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🔴 P0 — Do these first*\n• *⚠️ TODAY (carries over from Jul 7):* Confirm Carlo has scheduled Harness/OpenSpec check-in — *deadline is TOMORROW Jul 10*\n• Sign off on Source Claiming Banner E2E (Matan is blocked on your approval)\n• Block 3:45-4:30pm Figma design review with Fadi (3LO + source claiming)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟡 P1 — High priority*\n• Follow up with Michael and Cornelius on their Indeed account cases (per Chris call)\n• Confirm Rami reran outreach script on non-line-cook jobs (was Jul 7 action)\n• Flag name normalization ticket for screener personalization (before next batch)\n• Find 45-min Thursday recurring slot for new 1:1\n• Update Q3 goal doc with new metrics (D5 zero-applicant rate, line cook health, screener completions)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🟢 P2 — When you have a moment*\n• Pull 13 applicant + 127 clicker emails/IDs → send to Ted for join analysis (Jul 7 carry-over)\n• Write proposal for next talent pool email experiment iterations\n• Confirm Izzy started Thursday on role recommendation backend"
        }
    },
    {"type": "divider"},
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "📡 Delegations & Watch List",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*People to chase tomorrow:*\n• *Fadi* → Add Loom to current ticket; prep for 3:45 design review\n• *Carlo* → Harness/OpenSpec check-in status (deadline Jul 10 — URGENT)\n• *Tanner* → Copy→Reactivate flow status: when does it ship?\n• *Matan* → Source claiming guide in hand? Has Track B started?\n• *Chris* → Scooter's Coffee Friday 3-way call outcome\n• *Ted* → Friday jam session still on? Experiment list + email list ready?\n• *Rami* → Non-line-cook outreach script rerun + name normalization scan"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Open risk items:*\n• 🔴 Boost purchase bug — still revenue-impacting, status unknown\n• 🔴 ZipRecruiter holiday spend (Jul 3-6) — unconfirmed total\n• 🟡 OpenAI fallback model — P0 flagged Jul 6, has it hit eng backlog?\n• 🟡 Dana's Homebase Advantage outreach script — was due last Friday"
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🌟 Chief of Staff Take*\n\nToday was a genuinely important inflection point. Rewriting the Q3 goals mid-quarter is a *bold, correct call* — the old framing was diffuse and the new metrics (41% → <10% zero-applicant rate) are specific enough to actually drive behavior. The screener results are exciting but your healthy skepticism is exactly right — run the name normalization cleanup and watch the confounders before declaring victory.\n\nThe Indeed source claiming picture is now fully clear: you have the root cause, a three-track fix, a design session tomorrow, and field validation from Chris's calls. This one is moving fast and that's because you pushed it.\n\nYou're building something real here. Keep going. 💪"
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "_Chief of Staff digest · Jul 8, 2026 · 3 meetings reviewed · Delivered at 5pm PDT_"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Chief of Staff Daily Digest — Wednesday Jul 8, 2026"
}


def preview():
    sys.stdout.buffer.write(b"\n===== SLACK MESSAGE PREVIEW =====\n")
    for block in blocks:
        if block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("## " + text + "\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write(b"---\n")
    sys.stdout.buffer.write(b"===== END PREVIEW =====\n")


def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + TOKEN,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                print("✅ Sent to Slack successfully!")
                print("ts:", body.get("ts"))
            else:
                print("❌ Slack API error:", body.get("error"))
                print(json.dumps(body, indent=2))
    except urllib.error.HTTPError as e:
        print("HTTP error:", e.code, e.read().decode())
    except urllib.error.URLError as e:
        print("URL error:", e.reason)


if not TOKEN:
    print("⚠️  No SLACK_TOKEN found — printing preview only.")
    preview()
else:
    send()
