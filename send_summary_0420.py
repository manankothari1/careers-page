#!/usr/bin/env python3
"""Daily decision summary - Monday Apr 20, 2026"""
import json
import os
import sys
import urllib.request


SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")
CHANNEL_ID = "D06E4QMHCNN"


def build_payload():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Good morning, Manan! :sunrise: Your Monday Battle Plan — Apr 20",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Happy Monday! No meetings today or Sunday — you earned the rest. "
                    "Big week ahead with Launch Week in sight. Here's everything you need to hit the ground running. "
                    "One major update: *Jeff Gombos was terminated on Apr 16.* His design work on TLWA badge & desktop "
                    "designs was blocking engineers — you need to assess that immediately. Let's go. :muscle:"
                ),
            },
        },
        {"type": "divider"},
        # ─── CODE RED ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:rotating_light: CODE RED — Act Today*",
            },
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "ordered",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "TLWA Brief → Ted: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": "Now 18+ days overdue. Send it TODAY. No more delays. Ted needs this to plan Launch Week resourcing.",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Jeff's Design Handoff — UNBLOCK ENGINEERS: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Jeff was terminated Apr 16. His desktop designs for the TLWA badge were blocking your engineers. "
                                        "Immediately assess: (1) Are Figma files accessible? (2) Who owns design going forward? "
                                        "(3) Is there enough to ship, or do you need a design contractor fast?"
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Greenlight Manual Mode — NOW: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": "Cindy's QA is done. This is sitting on you. Stop the bleeding and greenlight it today.",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "URGENT — Audit Talroo Feed for Manual Mode Jobs: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "You may be spending $35/job on customers paying $30/month. "
                                        "This is a direct margin killer. Confirm the fix is in before another cent goes out."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Homebase Boost SKU Kick-off w/ Chris McIntosh: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": "Billing window is closing. Get this on the calendar immediately or the SKU misses Launch Week.",
                                },
                            ],
                        },
                    ],
                }
            ],
        },
        {"type": "divider"},
        # ─── DECISIONS NEEDED ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:thought_balloon: Open Decisions — You Need to Close These*",
            },
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "ordered",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "V1 Migration for TLWA Award Winners: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "50% of V1 users = TLWA award winners. 75% of users with live jobs = award winners. "
                                        "Was due EOD Apr 17 — now 3 days overdue. Options: (A) Exclude from mailer, "
                                        "(B) Optional V2 migration, (C) Build generic role plumbing first. "
                                        "Missing V2 features: past-applicant visibility + quick-repost. Decide today."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Predictive Roles — Yes or No for Launch Week: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Was time-boxed to EOD Apr 17. Still no confirmed decision with Divij. "
                                        "The mail delays (~3k unmailable addresses) might buy you a few extra days — "
                                        "but confirm with Cassy first, then decide go/no-go with Divij today."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "QR Mailer Address Count — Cassy Confirmation: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "~3,000 flagged unmailable. Fadi needs confirmed final count before print run. "
                                        "Call/Slack Cassy today."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "CTA Hierarchy in Job Creation Flow: ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Users now see Boost CTA + one-time posts + 3LO login simultaneously. "
                                        "Map the full CTA hierarchy with Cindy + Matan before Launch Week. "
                                        "Risk: CTA noise kills conversion."
                                    ),
                                },
                            ],
                        },
                    ],
                }
            ],
        },
        {"type": "divider"},
        # ─── DECISIONS MADE LAST WEEK (APR 16) ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:white_check_mark: Last Week's Key Decisions (Apr 16) — Lock In Follow-Ups*",
            },
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "ordered",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Talroo → CPA Bidding (Apr 16, Talroo Connect): ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Switched from flat CPC to CPA. 4 tiers: Entry Level $3-5 | Managerial | "
                                        "Specialized (cooks/chefs/bartenders) | Desperation (hard-to-fill, higher CPA). "
                                        "$35/job budget cap. Current avg $2.01/lead via pixel. "
                                        "WHY: More efficient — pay for actual applicants, not clicks. System auto-adjusts bids. "
                                        "FOLLOW-UPS: Saja sends recommended categories + configures campaign (due tomorrow). "
                                        "Nelson defines job description quality thresholds. Manan adds category + CPA nodes to XML feed."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Predefined Roles = Entry Point to Job Creation Flow (Apr 16, Jatin/Manan): ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Decided: predefined roles are NOT pre-created hidden jobs. "
                                        "They're an entry point into the job creation flow (user lands on step 2, fills in wage/schedule). "
                                        "WHY: Gives users full ownership of the job, cleaner UX, avoids hidden job complexity. "
                                        "FOLLOW-UPS: Jatin to sync with Malcolm on one-click post + job creation flow integration. "
                                        "Manan: accelerate Divij's role-matching with cloud code. "
                                        "Supabase import: conditional — only write if field is empty (don't override existing data)."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Boost Entry Points + Phase 1 Strategy (Apr 15, Cindy/Manan + Apr 16 standup): ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "3 entry points locked: (1) Job creation flow, (2) Jobs section (rocket icon → 'Sponsor Your Job'), "
                                        "(3) Email/push. Phase 1: auto-boost every trial user's job for free ($35 cap). "
                                        "Drop Zip/Craigslist from modal. Rename 'Boost' → 'Sponsored Job.' "
                                        "Day-1 trigger: <5 apps, max 2 sends per user. "
                                        "WHY: Build applicant-volume habit during trial, set expectations before paywall. "
                                        "FOLLOW-UPS: Matan posts Boost plan to #leads. Create Linear ticket for entry points + attribution. "
                                        "Manan + Cindy + Matan: map CTA hierarchy BEFORE Launch Week."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Fadi's Business Classifier — Company vs Location Level (Apr 16, Manan/Fadi): ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "Classifier built (Haiku + Sonnet judge, 55k winners → 15 industry categories). "
                                        "Found mismatch: Fadi's data is company-level but need location-level. "
                                        "7k companies have multiple locations. "
                                        "DECISION: If <10% of locations differ from parent company type → auto-apply company classification. "
                                        "If >90% differ → run individual location classification. "
                                        "WHY: Cost-effective fallback, avoids over-engineering the edge case. "
                                        "FOLLOW-UPS: Fadi confirms final company vs location winner list. "
                                        "Fadi confirms Haiku/Sonnet taxonomy aligns with Cindy's 15 categories."
                                    ),
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Incomplete Applicant Ingestion Pipeline (Apr 16, Ray/Manan): ", "style": {"bold": True}},
                                {
                                    "type": "text",
                                    "text": (
                                        "DECIDED to pursue after Launch Week. Daily job to auto-ingest clicked-but-not-applied leads "
                                        "via app endpoint (Bob has the endpoint structure from V2 job experiment). "
                                        "WHY: 30%+ projected increase in Talroo applicants. High ROI. "
                                        "BLOCKER: Jatin needs convincing — frame as warm lead re-engagement, NOT spam. "
                                        "FOLLOW-UPS: Create 'Ray's Homework' Google doc (Talroo CPA + segmentation + incomplete ingestion specs). "
                                        "Bob shares application endpoint with Ray."
                                    ),
                                },
                            ],
                        },
                    ],
                }
            ],
        },
        {"type": "divider"},
        # ─── HOMEWORK QUEUE ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:pencil: Your Homework Queue — Clear These This Week*",
            },
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "bullet",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Create 'Ray\'s Homework' Google doc — Talroo CPA + segmentation + incomplete ingestion specs (send to Ray before he returns Monday)",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Send TLWA brief to Ted (18+ days overdue — this is the one)",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Assess Jeff's Figma files — TLWA badge desktop designs must reach engineers today",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Greenlight Manual Mode — tell Cindy",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Confirm address count with Cassy (printer) before QR print run",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Send Saja (Talroo) recommended CPA categories — coordinate campaign config before switch goes live",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Send predicted role docs + intro Divij ↔ Nelson (confirm yes/no on LW timeline today)",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Send 3LO spec doc to team as pre-read",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Matan: remind to post Boost plan update to #leads (Phase 1 vs Phase 2 rationale for Ray)",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Nelson: follow up on metro_area + bucketed_role + matching_roles columns (overdue since Apr 8)",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Justin: confirm Supabase RLS full audit is active + re-run company descriptions batches 93-100",
                                },
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "TLWA careers page QA with Fadi before 50k QR codes go out",
                                },
                            ],
                        },
                    ],
                }
            ],
        },
        {"type": "divider"},
        # ─── LAUNCH WEEK READINESS ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:rocket: Launch Week Readiness Checklist*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    ":white_check_mark: Boost entry points decided (3 locked)\n"
                    ":white_check_mark: Boost Phase 1 strategy finalized (auto-boost trial users)\n"
                    ":white_check_mark: Talroo CPA structure decided\n"
                    ":white_check_mark: 3LO architecture locked (Andrew owns token refresh)\n"
                    ":white_check_mark: TLWA badge design direction set (bottom-up gradient fallback)\n"
                    ":x: TLWA brief → Ted (OVERDUE)\n"
                    ":x: Jeff design handoff (terminated Apr 16 — urgent triage)\n"
                    ":x: V1 migration decision for award winners\n"
                    ":x: Predictive roles go/no-go with Divij\n"
                    ":x: Manual Mode greenlighted\n"
                    ":x: Boost SKU kick-off w/ Chris McIntosh\n"
                    ":x: CTA hierarchy mapped before LW\n"
                    ":x: QR mailer final count confirmed"
                ),
            },
        },
        {"type": "divider"},
        # ─── BRIGHT SPOTS ───
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*:star2: You're Crushing It — Momentum Check*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "ARR: *$650K (+44% from $450K in January)* :chart_with_upwards_trend:\n"
                    "GTM OS ML: *70% of top 250 companies converted in 7 days* :fire:\n"
                    "Lifecycle: *46% team app upgrades influenced*\n"
                    "Taru feed: *~300 → ~1,100 jobs* — nearly 4x growth\n"
                    "Applied AI Jam: Signal Scout + Data Genie agent unlocked :robot_face:\n\n"
                    "The fundamentals are strong, Manan. You've got a clear roadmap, strong team alignment, "
                    "and a Launch Week that could be transformational for Homebase Hiring. "
                    "Close out the open decisions today and the rest of the week will flow. Let's go! :rocket:"
                ),
            },
        },
    ]
    return {"channel": CHANNEL_ID, "blocks": blocks, "text": "Monday Apr 20 Battle Plan — Manan Kothari"}


def send_to_slack(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    return result


def preview(payload):
    encoded = json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8", errors="replace")
    sys.stdout.buffer.write(b"\n=== SLACK PAYLOAD PREVIEW ===\n")
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.write(b"\n=== END PREVIEW ===\n")


def main():
    payload = build_payload()
    if not SLACK_TOKEN:
        print("WARNING: SLACK_TOKEN not set. Printing preview only.")
        print("Add SLACK_TOKEN to Cursor Dashboard > Cloud Agents > Secrets to enable live sending.")
        preview(payload)
        return 0
    result = send_to_slack(payload)
    if result.get("ok"):
        print(f"Message sent successfully. ts={result.get('ts')}")
        return 0
    else:
        print(f"ERROR sending message: {result.get('error')}")
        preview(payload)
        return 1


if __name__ == "__main__":
    sys.exit(main())
