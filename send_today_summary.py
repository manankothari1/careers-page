#!/usr/bin/env python3
"""
One-shot: compose today's summary from pre-fetched meeting data and send to Slack.
Run by the Cloud Agent cron at midnight UTC (= 5pm PDT).
"""

import os
import json
import requests

SLACK_CHANNEL = "D06E4QMHCNN"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")


SUMMARY = """*Hey Manan! 👋 Here's your Daily Decision Summary for Wednesday, June 17, 2026.*
You had a packed day — 5 meetings, multiple product decisions locked in, and a clear set of next steps. Let's get into it!

---

*🗓️ MEETINGS TODAY*
• 8:15 AM — Nelson / Manan _(1:1)_
• 8:45 AM — Hiring Leads Standup
• 9:00 AM — Michael / Christofer / Manan / Dana _(Indeed escalation)_
• 11:15 AM — Applicant Flow Sprint Lookahead
• 3:00 PM — Jenna / Manan _(SEO deep-dive)_

---

*🔑 KEY DECISIONS MADE*

*1. Indeed: Reactivation > Copy-Paste*
_Decision:_ Confirmed that reactivating old job posts works on Indeed — copy-and-paste triggers duplicate detection and forces paid sponsorship. V2 removed reactivation in favor of copy-paste, which is now clearly causing customer harm.
_Rationale:_ The PJs Coffee case study proved it — reactivating the barista post via admin surfaced the job; copy-paste didn't.
_Next:_ Evaluate 3 options (revert to reactivation / extend 30→60-90 day expiry / customer-controlled close date) and return with engineering lift estimates.

*2. HTML Job Pages → Spike First, Build Later*
_Decision:_ Don't rush into server-side rendering. Spike the project instead — Carlo leads investigation in partnership with you. Loop in Jenna before engineering digs in.
_Rationale:_ Moving from JS to SSR is a significant architecture change that could affect dynamic UI. Jenna's SEO context (job pages used to rank and get indexed) is essential before scoping.
_Next:_ HTML pages tagged as sprint stretch goal pending the Jenna conversation.

*3. Q3 Applicant Flow Strategy — 3 Pillars Locked*
_Decision:_ Q3 strategy finalized around 3 pillars: (1) Enable OEM Spend, (2) Tap the Talent Pool, (3) Optimize the Funnel.
_Rationale:_ Only 30% of ICP jobs hit "healthy" status (20+ applicants, 5+ top matches) by day 30. Goal is 80%. Boosted jobs reach ~50% healthy vs. 26% unboosted, but only 1.64% of jobs are currently boosted — massive low-hanging fruit.
_Out of scope for Q3:_ Net new candidate acquisition, building job supply, poaching active HB employees.
_Next:_ Build OKR dashboard so the team can track weekly progress; share strategy + roadmap docs with full team.

*4. Healthy Job Definition — Keep Universal Threshold*
_Decision:_ Keep the current global 20+ applicants / 5+ top matches threshold for WBR/MBR consistency. Do internal analysis (manager vs. non-manager) to understand role-level nuance without changing the public metric.
_Rationale:_ Changing the definition mid-stream breaks historical comparisons. Niche roles (caregiving, vet) will be flagged but not penalized in reporting.
_Next:_ Nelson runs manager vs. non-manager applicant count analysis by end of week.

*5. ICP Shared Reference Table — Build It Today*
_Decision:_ Create a single FFH (Frequent Frontline Hires) reference table that all stakeholders (Manan, Nelson, Dana, Librarian) read from. Refreshes daily.
_Rationale:_ Everyone was running separate queries against different definitions. One source of truth avoids drift.
_Next:_ Nelson spins it up (~30 min). Manan updates the Homebase context repo to point to this table.

*6. SEO / Indexing — Hold on JS→HTML Conversion*
_Decision:_ Don't convert job pages from JS to HTML until the indexing root cause is fully understood.
_Rationale:_ Job pages on app.joinhomebase.com are intentionally not indexed (to prevent duplicate content from sideway landing pages) — a side effect that's blocking organic job discoverability. The fix needs to be surgical.
_Next:_ Jenna researches programmatic indexing for Homebase One; engineering adds meta descriptions to the job-creation pipeline.

---

*✅ YOUR ACTION ITEMS*

| # | Action | Context |
|---|--------|---------|
| 1 | QA *Purchase Homebase Boost* + post-job creation boost → release | Sprint carryover, both on staging |
| 2 | Build Q3 OKR dashboard | Weekly team tracking against 80% healthy goal |
| 3 | Investigate ICP overlap within 231K talent pool | Share findings with team |
| 4 | Write up Salesforce table requirements → send to Nelson | Feeds into day-5 unhealthy trial calling logic |
| 5 | Review `bucket_role` table → define ICP scope roles | Needed for talent pool targeting |
| 6 | Share Indeed email thread (70+ emails) with team | Source claiming best practices context |
| 7 | Build shared Indeed best-practices doc (w/ rep numbers) | With Chris + team |
| 8 | Evaluate engineering lift: reactivation vs. expiry extension | Return with a recommendation |
| 9 | Share Q3 strategy + roadmap docs with full team | Post in #applicant-flow or equivalent |
| 10 | Condense goals doc to ~3 pages (follow up w/ Usman) | Needed for exec walkthrough |

---

*🤝 OTHERS WHO OWE YOU SOMETHING*

• *Chris Peralta* — Confirm "blocked" = "archived" on Indeed's side; Call PJs Coffee customer to claim company page + source-claim Homebase; Reactivate 2nd PJs job via admin
• *Nelson Tang* — Spin up FFH reference table today; Manager vs. non-manager applicant analysis by EOW (partial output today for Ray's exec meeting)
• *Jenna Brennan* — Research programmatic indexing for Homebase One
• *Carlo Ferrer* — Lead HTML job pages spike investigation with you
• *Usman Zafar* — Condense goals doc to ~3 pages; Review opportunities at risk report; Confirm daily sales report data accuracy

---

*💡 THINGS TO KEEP TOP OF MIND*

• The talent pool is 231K people — you don't know the ICP overlap yet. That number could change the Q3 story significantly.
• Source claiming on Indeed is a *free*, high-impact fix for customers. Worth documenting + training CS on.
• Meta descriptions on job pages are missing and apparently easy to add via the same script that populates titles — quick win for engineering.
• The "personal recruiter" framing is landing much better than "hiring assistant" — 40% connect-to-demo baseline, with Usman hitting 70%. Worth propagating team-wide.

You crushed today, Manan. Big decisions, clear rationale, solid next steps. Go get some rest — tomorrow's exec walkthrough is going to be 🔥"""


def slack_post(text: str, blocks=None):
    if not SLACK_BOT_TOKEN:
        print("⚠️  SLACK_BOT_TOKEN not set — printing summary instead:\n")
        print(text)
        return None
    payload = {"channel": SLACK_CHANNEL, "text": text, "unfurl_links": False}
    if blocks:
        payload["blocks"] = blocks
    resp = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("ok"):
        raise RuntimeError(f"Slack API error: {data.get('error')}")
    return data


if __name__ == "__main__":
    result = slack_post(SUMMARY)
    if result:
        print(f"✅ Sent to Slack — ts={result.get('ts')}")
