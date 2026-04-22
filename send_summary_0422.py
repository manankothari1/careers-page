#!/usr/bin/env python3
"""Daily decision summary for Manan Kothari — Apr 22, 2026 (covering Apr 21 meetings)"""
import json
import os
import sys
import urllib.request
import urllib.error

SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Your Daily Decision Brief — Tuesday, April 22 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Manan! Big day. You had *4 meetings* on Apr 21 and made some sharp calls. "
                "Here's everything you decided, why it matters, and exactly what needs to happen next. Let's go! \U0001f680"
            )
        }
    },
    {"type": "divider"},

    # ─── MEETING 1 ───────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4bc Meeting 1 — Michael / Manan | 9:30 AM*\n_Indeed Job Discoverability Deep Dive_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\u2705 Decision: Volume-gated approach to Indeed failures*\n"
                "You and Michael aligned on a tiered response strategy for jobs that don't surface on Indeed:\n"
                "  \u2022 *Low volume* \u2192 handle individual cases as they arise (manual XML lookup + CS handoff)\n"
                "  \u2022 *High volume* \u2192 batch process every few days with multiple XML feeds\n"
                "  \u2022 V2 already fixed the bulk of posting failures; the real bug is *discoverability* — jobs exist on Indeed but are invisible in standard search (e.g., 'barista Houston Texas' returns nothing)\n\n"
                "*\U0001f9e0 Why this matters:* 25% of jobs showed zero search results before V2. Even post-V2, the discoverability gap is silently killing application volume. This is a stealth conversion problem you need to quantify fast before Indeed V3 ships.\n\n"
                "*\U0001f6a8 Action Items:*\n"
                "  \u2022 *Manan* \u2014 Conduct a job discoverability audit on Indeed (test a sample of live jobs as an applicant)\n"
                "  \u2022 *Manan* \u2014 Establish a named Indeed contact + define the required details for failed postings escalation\n"
                "  \u2022 *Michael* \u2014 On standby to handle call volume if V3 spikes; no action until volume data is in\n"
                "  \u2022 *Both* \u2014 Monitor Indeed V3 integration volume once released to calibrate batch vs. individual response"
            )
        }
    },
    {"type": "divider"},

    # ─── MEETING 2 ───────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f916 Meeting 2 — Applied AI Jam: Hiring | 3:30 PM*\n_Predicted Roles Coverage Strategy with Divij, Dana, Ted_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\u2705 Decision 1: Adopt Two-Level coverage approach (Level 3 killed)*\n"
                "  \u2022 *Level 1 \u2014 Historical data expansion* (55% \u2192 ~90% slot 1 coverage): Expand lookback from 12 months \u2192 *all historical* roster additions. Ready as LW-minimum-viable by early May.\n"
                "  \u2022 *Level 2 \u2014 Business category fallbacks* (~90% \u2192 95%+ coverage): Use business category for industry-common role predictions when company data is thin.\n"
                "  \u2022 *Level 3 \u2014 External enrichment (scraped + Google Places)* \u2192 *KILLED*. High effort, negligible marginal gain. Deprioritized entirely.\n\n"
                "*\U0001f9e0 Why this matters:* Right now 54% of slot 1, 46% of slot 2, and only 35% of slot 3 are covered across 47k companies. With Level 1 alone you get to 90% \u2014 that's the LW-viable bar. Level 2 gets you to near-complete. "
                "Generic roles ('team member', 'crew member') are polluting predictions \u2014 you're solving the right root cause.\n\n"
                "*\u2705 Decision 2: Product UX = deep link to job creation flow page 2*\n"
                "  \u2022 Pre-populate *role title only*; user completes shift details, schedule, requirements\n"
                "  \u2022 *Do not* predict wage or schedule \u2014 accuracy too low, risk too high\n"
                "  \u2022 Avoids creating live ghost jobs prematurely (Approach 1 architecture confirmed)\n\n"
                "*\u2705 Decision 3: Data storage = existing Databricks hiring ML intelligence table*\n"
                "  No new infrastructure. Reuse what exists.\n\n"
                "*\u23f0 Timeline locked:* First week of May launch target with Level 1 as minimum viable.\n\n"
                "*\U0001f6a8 Action Items:*\n"
                "  \u2022 *Manan* \u2014 Create Linear project + dedicated channel for predicted roles work \u2192 DO THIS TODAY\n"
                "  \u2022 *Ted* \u2014 Coordinate with Malcolm on product/engineering approach (scope Level 1 + 2 implementation)\n"
                "  \u2022 *Divij* \u2014 Run ground truth validation: 100-200 sample predictions to QA accuracy before ship\n"
                "  \u2022 *Manan* \u2014 Scope dashboard vs. careers page placement decision (QR code / mobile constraints factor in)\n"
                "  \u2022 *Manan + Ted* \u2014 Final predicted roles decision with Cindy is STILL DUE \u2014 this is 1 day overdue, close the loop"
            )
        }
    },
    {"type": "divider"},

    # ─── MEETING 3 ───────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4b0 Meeting 3 — Homebase / JobGet Integration | 4:30 PM*\n_With Peter Lee + Dan (JobGet)_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\u2705 Decision 1: Run a 30-day paid test with JobGet before full integration*\n"
                "  \u2022 Current state: 6,100+ jobs sent via XML feed, only *41 applicants in 2 weeks* \u2014 organic performance is near-zero because JobGet deprioritizes unpaid jobs\n"
                "  \u2022 Paid relationship = unlock significantly more scale + capacity\n"
                "  \u2022 Test approach: 30 days paid, evaluate performance before commitment\n\n"
                "*\u2705 Decision 2: Explore Easy Apply integration*\n"
                "  \u2022 Easy Apply = applicant stays on JobGet platform (vs. redirect to Homebase job page)\n"
                "  \u2022 Organic easy apply jobs get *3-4x more exposure* \u2014 huge lever\n"
                "  \u2022 Currently backlogged at JobGet; paid relationship bumps priority\n\n"
                "*\u2705 Decision 3: CPA pricing confirmed for evaluation*\n"
                "  \u2022 Everyday worker roles (servers, cashiers): *$3\u20137 CPA*\n"
                "  \u2022 Skilled trades / hard-to-fill: *$20+ CPA*\n"
                "  \u2022 CPC range: $0.20\u20130.35 (job boards) / $0.35\u20131.00 (other partners)\n"
                "  \u2022 'Spend Smart' system for 50+ location enterprise clients \u2014 auto-allocates budget by hiring need (restaurants need ~15 applies/hire)\n\n"
                "*\U0001f9e0 Why this matters:* 41 applicants from 6,100 jobs is a 0.67% conversion rate \u2014 broken. JobGet is the 3rd largest job board after Indeed + ZipRecruiter. If paid integration works, it's a material applicant volume unlock, especially for hard-to-fill roles where Talroo is weakest. This is a Talroo complement, not a replacement.\n\n"
                "*\U0001f6a8 Action Items:*\n"
                "  \u2022 *Manan* \u2014 Review Homebase spend allocation for next 3-6 months; determine test budget for 30-day paid pilot\n"
                "  \u2022 *JobGet (Peter/Dan)* \u2014 Send Easy Apply integration documentation + CPA implementation details (XML feed node specs)\n"
                "  \u2022 *Dan* \u2014 Add Dan to existing Slack channel (confirm w/ Dan which channel)\n"
                "  \u2022 *Manan* \u2014 Compare JobGet CPA ($3\u20137) vs. Talroo current CPA (~$2/applicant) to set bid strategy for test\n"
                "  \u2022 *Manan* \u2014 Decide: start with CPC or go straight to CPA for the test? (Programmatic bidding available)"
            )
        }
    },
    {"type": "divider"},

    # ─── MEETING 4 ───────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f5c4\ufe0f Meeting 4 — Career Page Data Transfer Strategy | 9:37 PM*\n_With Izzy + Bob_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\u2705 Decision 1: Separate display name column \u2014 never touch actual company name*\n"
                "  \u2022 Create a new display column in the hiring page table; default to actual company name if blank\n"
                "  \u2022 Actual company name in the main system = *untouched*\n\n"
                "*\u2705 Decision 2: Existing user customization wins over scraped data*\n"
                "  \u2022 Priority order: (1) Existing user customization \u2192 (2) Scraped data as fallback \u2192 (3) Homebase defaults\n"
                "  \u2022 *Do not* override what customers have already set with scraped presets\n"
                "  \u2022 Fill empty fields (e.g., logo, email) with scraped data; don't overwrite populated fields\n\n"
                "*\u26a0\ufe0f Decision 3: Address / company name edge cases = TBD (engineering investigation required)*\n"
                "  \u2022 Izzy + Bob to examine codebase and determine which fields can accurately detect 'user updated vs default'\n"
                "  \u2022 Ambiguous cases (address updates, name changes) need code investigation before ruling\n\n"
                "*\u2705 Decision 4: All companies get the experience \u2014 email for non-print recipients*\n"
                "  \u2022 QR code recipients = print + physical mail\n"
                "  \u2022 Everyone else on the TLWA list = email delivery of career page experience\n\n"
                "*\U0001f6a8 Action Items:*\n"
                "  \u2022 *Manan* \u2014 Cross-reference final TLWA list vs. updated company list (55,696 vs. 54,000 discrepancy \u2014 resolve with source TODAY)\n"
                "  \u2022 *Manan* \u2014 Run worker against missing companies to fill gaps\n"
                "  \u2022 *Manan* \u2014 Write requirements doc for data transfer handling (customization priority rules, field-by-field spec)\n"
                "  \u2022 *Manan* \u2014 Finalize and *freeze* company list \u2014 multiple versions circulating is creating chaos\n"
                "  \u2022 *Manan* \u2014 Schedule morning alignment meeting with Andrew + Tanner (remember CST timezone)\n"
                "  \u2022 *Izzy + Bob* \u2014 Examine codebase: which fields can detect user-customized vs. default values?\n"
                "  \u2022 *Note:* Izzy is *off Thursday, back Tuesday* \u2014 email CTS page work + data transfer work need sequencing this week"
            )
        }
    },
    {"type": "divider"},

    # ─── MASTER ACTION LIST ───────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4cb MANAN'S MASTER HIT LIST \u2014 Apr 22*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f525 Do Today (blocking others):*\n"
                "  1. \u2b50 *Create Linear project + channel for Predicted Roles* (Ted + Divij are waiting)\n"
                "  2. \u2b50 *Close predicted roles decision with Cindy* \u2014 1 day overdue, team is blocked\n"
                "  3. \u2b50 *Freeze the TLWA company list* \u2014 55,696 vs 54,000 needs resolution NOW; multiple versions = engineering confusion\n"
                "  4. *Write requirements doc* for career page data transfer field rules\n"
                "  5. *Schedule Andrew + Tanner morning meeting* (CST timezone)\n\n"
                "*\U0001f4c6 This Week:*\n"
                "  6. Run Indeed job discoverability audit (test live jobs as an applicant)\n"
                "  7. Establish Indeed contact for failed posting escalation\n"
                "  8. Review Homebase spend allocation (3-6 mo) \u2192 set JobGet test budget\n"
                "  9. Confirm JobGet Easy Apply docs + CPA node specs received from Peter/Dan\n"
                "  10. Add Dan (JobGet) to Slack channel\n"
                "  11. Scope predicted roles dashboard vs. careers page placement\n"
                "  12. Run worker against missing career page companies\n\n"
                "*\U0001f6a8 Pending from Others (you need to chase):*\n"
                "  \u2022 *Izzy + Bob* \u2014 Codebase investigation on field-level customization detection\n"
                "  \u2022 *Divij* \u2014 100-200 sample ground truth validation for predicted roles\n"
                "  \u2022 *Ted* \u2014 Sync with Malcolm on predicted roles engineering approach\n"
                "  \u2022 *JobGet* \u2014 Easy Apply docs + CPA XML specs\n\n"
                "*\U0001f551 Still Overdue (carried from prior days):*\n"
                "  \u2022 TLWA brief to Ted \u2014 *20+ DAYS OVERDUE* \U0001f6a8 send this today\n"
                "  \u2022 Greenlight Manual Mode (Cindy QA done, on Manan)\n"
                "  \u2022 Homebase Boost SKU kick-off with Chris McIntosh \u2014 billing window closing\n"
                "  \u2022 Audit Talroo feed for Manual Mode customer jobs\n"
                "  \u2022 Saja (Talroo) \u2014 send CPA categories + configure campaign"
            )
        }
    },
    {"type": "divider"},

    # ─── FOOTER ──────────────────────────────────────────────
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*\U0001f4a1 Your COO Observation for Today:*\n"
                "You made a very disciplined call on predicted roles \u2014 killing Level 3 (external enrichment) keeps the team focused and the May timeline credible. "
                "The JobGet meeting surfaced a critical insight: 6,100 jobs, 41 applicants \u2014 that's a 'technically integrated but commercially broken' situation that needs immediate budget commitment to unlock. "
                "And the TLWA company list version chaos is a silent risk that could derail launch week precision \u2014 freezing it today is not optional.\n\n"
                "_You\u2019re making great decisions, Manan. Now execute. \U0001f4aa_"
            )
        }
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "Chief of Staff Bot \u2022 Apr 22, 2026 \u2022 Covering 4 meetings from Apr 21"
            }
        ]
    }
]

payload = {
    "channel": CHANNEL_ID,
    "text": "Your Daily Decision Brief is ready \U0001f4cb",
    "blocks": blocks
}

def preview():
    sys.stdout.buffer.write("=== SLACK MESSAGE PREVIEW ===\n".encode("utf-8", errors="replace"))
    for block in blocks:
        if block.get("type") == "section":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write((text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "header":
            text = block.get("text", {}).get("text", "")
            sys.stdout.buffer.write(("### " + text + "\n\n").encode("utf-8", errors="replace"))
        elif block.get("type") == "divider":
            sys.stdout.buffer.write("---\n".encode("utf-8", errors="replace"))
        elif block.get("type") == "context":
            for el in block.get("elements", []):
                sys.stdout.buffer.write((el.get("text", "") + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.write("=== END PREVIEW ===\n".encode("utf-8", errors="replace"))

if not SLACK_TOKEN:
    print("SLACK_TOKEN not set — printing preview only.")
    preview()
    sys.exit(0)

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=data,
    headers={
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        if body.get("ok"):
            print(f"Message sent successfully! ts={body.get('ts')}")
        else:
            print(f"Slack API error: {body.get('error')}")
            print(json.dumps(body, indent=2))
            sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e}")
    sys.exit(1)
