#!/usr/bin/env python3
"""Daily decision digest - Monday Jul 20, 2026 (PDT)"""
import json, os, sys, urllib.request, urllib.error

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
            "text": "Chief of Staff Daily Digest - Monday, Jul 20 \U0001f4cb",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Manan, you crushed today. *4 meetings, 20+ decisions locked.* And the headline? *V1\u2192V2 migration is DONE.* \u2705 That\u2019s a massive milestone. Here\u2019s everything you decided today, with your action items front and center."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # BIG WIN CALLOUT
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "\U0001f3c6 *BIG WIN: V1\u2192V2 Migration COMPLETE*\nCore side had a strong week and the V1\u2192V2 cutover shipped. That\u2019s been the target since before Jul 13. Celebrate this one."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # MEETING 1
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u231a 10:30 AM \u2014 Sprint Planning: Applicants*\n_With: Ugu, Tanner, Izzy, Jatin, Carlo_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Locked:*\n\n\u2022 *Sprint priority order FINAL:* Value prop (Ugu) \u2192 Scheduling \u2192 Reactivate jobs\n\u2022 *Reactivate jobs will NOT ship this sprint* \u2014 explicitly deprioritized; plan for next sprint\n\u2022 *Quality + KTL deprioritized* this sprint across the board\n\u2022 *Salary recs back in sprint* \u2014 Tanner owns; unblocked once Izzy\u2019s role recs FE is done (Tue)\n\u2022 *Reactivate lead = Izzy, Tanner supports, Bob advisory only* (no full ownership for Bob)\n\u2022 *Tanner drafts reactivate plan first,* runs by Bob + Ugu before starting\n\u2022 *New way of working for Indeed account setup:* Manan + Carlo + Ferri spec upfront \u2192 feed full context to harness \u2192 Carlo reviews\n\u2022 *No Figma paper trail for Ferri* is an explicit, acknowledged trade-off for speed\n\u2022 *Bob pulled in earlier on large backend projects* \u2014 reactivate slippage traced to late scope reveal\n\u2022 *Thursday EOD sync* (Manan + Jatin + Ferri) shifted to end-of-day; come better prepared\n\u2022 *Triage label:* Manan uses existing \u2018inflow\u2019 label; Jatin builds formal process for moving items\n\u2022 *All Sprint tickets cut + pointed by Tuesday EOD*\n\u2022 *Jatin meets Carlo Monday + Tuesday EOD* at start of each sprint for planning check-ins\n\u2022 *422 error bug flagged* \u2014 Jatin + Ugu to take offline and fix"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f Rationale:* Backend is genuinely strapped. Forcing a hard priority stack means Ugu\u2019s value prop actually ships instead of getting squeezed. Reactivate is the Q3 north star but needs to be done right \u2014 Izzy leading is the right call."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # MEETING 2
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u231a 12:00 PM \u2014 Hiring: Week in Review*\n_With: Fadi, Dana, Matan, Cindy, Jatin, Ray, Nelson, Usman, Ankit, John, Martin_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Locked:*\n\n\u2022 *Account setup release pushed to midweek* \u2014 incorrect FFH flag caused by ICP zero state page experiment tie-in; Ugo completed code but left testing unresolved\n\u2022 *Engineering ownership culture fix:* Engineers must own work through release, not just code completion \u2014 Jatin to speak directly with Ugo\n\u2022 *422 errors = top company priority* \u2014 146 locations affected since Jul 9, job publishing failures = failed trial starts; first time leadership heard about it after 2 weeks\n\u2022 *Alerts channel too noisy* \u2014 Jatin working with Malcolm to improve signal quality; loop Bob on why alerts didn\u2019t fire\n\u2022 *Backend resourcing escalation:* Ray escalating as a company-level priority; Jatin formally requesting a frontend\u2192backend engineer swap; backend hire expected in ~2 months\n\u2022 *Data platform included in kickoff meetings earlier* \u2014 bring Paul + Kanchan in at planning, not post-spec\n\u2022 *Proactive success outreach on new multi-location franchise deal* \u2014 closed without full product trial, high churn risk if they don\u2019t post/hire"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f Rationale:* The 422 error situation is a systemic trust problem \u2014 alerts didn\u2019t fire for 2 weeks on job publishing failures. This is a revenue + NPS risk. The culture issue around Ugo shipping without testing is the right conversation for Jatin to have directly."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # MEETING 3
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u231a 12:30 PM \u2014 Tatiana / Manan: Job + Career Pages (SEO)*\n_With: Tatiana Morand_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Locked:*\n\n\u2022 *Sitemap criteria finalized:* Add company + job pages if (a) active job on Homebase Hiring, OR (b) had a job + General Application open. Never add if company never posted.\n\u2022 *Trigger:* When company posts first job \u2192 add BOTH job page AND careers page to sitemap simultaneously\n\u2022 *jobs.joinhomebase.com = noindex by default* + canonical tag pointing to app job page \u2014 prevents SEO harm, keeps A/B testing live (~20% of traffic)\n\u2022 *33 noindex job pages to investigate* \u2014 likely archived jobs with removal delay; fix = remove from sitemap when archived + auto-redirect expired URLs \u2192 careers page (no 404s)\n\u2022 *MSA x Role Normalization table to be shared with Tatiana* for content use (barista / line cook by region)\n\u2022 *Sitemap work \u2192 project ticket for next sprint*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f Rationale:* You have 66K pages live and only 15.5K indexed \u2014 this is a massive SEO gap. Getting sitemap + canonicalization right is the unlock. The canonical tag decision is especially smart: you protect the 80% of traffic already on app pages while keeping A/B tests running on the subdomain."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # MEETING 4
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u231a 1:00 PM \u2014 Fadi / Manan: Hard to Fill Flow + Indeed UX*\n_With: Fadi Rizk_"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Decisions Locked:*\n\n\u2022 *Step 1 copy finalized:* 'Connect your Indeed account' + helper: 'Will open Indeed to begin connecting, then bring you back to finish'\n\u2022 *Opens in same tab* (deliberate \u2014 avoids stale state when old tab stays open)\n\u2022 *Step 2 copy:* 'Last step: verify your business to complete the connection'\n\u2022 *CTA order flipped:* 'Verify together' primary, 'Book a call' secondary\n\u2022 *Flagging copy reframed:* From 'your job may be flagged' \u2192 'Know if there are any issues with your job post on Indeed'\n\u2022 *Completion modal (not toast)* \u2014 3-item checklist: (1) See your job on Indeed, (2) Know if there are any issues, (3) Sponsor to get more applicants\n\u2022 *Hard-to-fill brainstorm deferred* \u2014 ran out of time; 30-min session locked for tomorrow 12:15 PM (right after lead standup)\n\u2022 *Intervention hypothesis:* Post-job-creation: surface role is hard to fill + recommend boost; salary recs = highest leverage signal; benefits flagging = secondary candidate"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u26a0\ufe0f Rationale:* The same-tab decision is subtle but important \u2014 leaving the old tab open with stale state creates broken auth flows. The flagging copy reframe is a tone win: 'know if there are issues' is helpful, 'may be flagged' is scary. Good call."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # MANAN'S ACTION ITEMS
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f3af YOUR ACTION ITEMS \u2014 Do These Today/Tomorrow:*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f525 TONIGHT (before you sleep):*\n\n1. *Send Fadi the hard-to-fill brain dump doc* \u2014 first-principles thinking on why roles are hard to fill. Tomorrow\u2019s 12:15 session is built around this.\n2. *Update Carlo on Indeed sync flow status* \u2014 let him know updated flow is coming tomorrow morning from Fadi.\n3. *Message data platform team* about role recommendations endpoint \u2014 this was flagged as urgent in sprint planning (blocks Izzy\u2019s final integration)."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4c5 TOMORROW (Tuesday Jul 21):*\n\n4. *Send Tatiana* sitemap criteria notes + Databricks MSA x Role Normalization table access\n5. *Create sitemap project ticket* for next sprint\n6. *Book sync with Jatin, Kanchan, and Paul* \u2014 share Rami\u2019s doc, align roadmap, prevent waterfall conflicts\n7. *Schedule squad retro* (applicant flow team only; aim for after town hall)\n8. *Confirm Rami \u2192 Antoine chain happened* \u2014 was scheduled for Monday; Izzy starts salary recs with Tanner this sprint\n9. *Attend 12:15 PM hard-to-fill brainstorm* with Fadi (30 min)"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\u274c OVERDUE \u2014 Carlo Ferrer: 10 DAYS:*\n\nHarness/OpenSpec has now been overdue for *10 days* (Jul 10 deadline). Sprint planning today gave him context on the Indeed account setup branch, but there\u2019s no explicit resolution on the underlying overdue task. You need a direct conversation about this. Don\u2019t let it hit 2 weeks."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # WATCH LIST
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4f6 WATCH LIST (Updated Jul 20):*\n\n\u2705 *V1\u2192V2 Cutover* \u2014 DONE. Close this one out.\n\u26a0\ufe0f *422 Job Publishing Errors* \u2014 NEW CRITICAL. 135+ locations, 2 weeks of silent failures. Jatin owns, but you need to stay on top of RCA.\n\u26a0\ufe0f *Account Setup Release* \u2014 midweek now (was today). Watch for FFH logic sign-off.\n\u26a0\ufe0f *Reactivate Jobs* \u2014 pushed to next sprint. Tanner drafting plan; Bob advisory. Don\u2019t let scope creep again.\n\u26a0\ufe0f *Salary Recs (Izzy + Tanner)* \u2014 Rami hands off data source tomorrow. Unblocked once role recs FE ships Tue.\n\u26a0\ufe0f *Replica Identity Blocker (Izzy)* \u2014 Thursday EOD cutoff. Justin Lambert needs to sign off.\n\u26a0\ufe0f *Backend Resourcing* \u2014 Ray escalating. FE\u2192BE swap in discussion with Martin + Andrea. ~2 months to hire.\n\u26a0\ufe0f *Dana Succession* \u2014 Off Aug 7. ~10 weeks left. No conversation started. This is still your biggest quiet risk.\n\u26a0\ufe0f *SEO Indexing Gap* \u2014 66K pages live, 15.5K indexed. Sitemap + canonical work scoped today; get it into next sprint.\n\u26a0\ufe0f *Abby* \u2014 Week 5. Still needs clear ownership area.\n\u26a0\ufe0f *Multi-location franchise deal* \u2014 Closed without trial. Someone needs to own success outreach ASAP."
        }
    },
    {
        "type": "divider"
    },

    # =====================================================================
    # CLOSING
    # =====================================================================
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*\U0001f4aa Bottom Line:* You made a lot of high-quality decisions today \u2014 the sprint priority stack was disciplined, the SEO sitemap is now scoped, and the Indeed UX copy is locked. The 422 error situation was ugly to uncover but better to know now than at a QBR. Keep the energy on the data platform alignment and the Carlo conversation. You\u2019re running hot \u2014 now go eat dinner. \U0001f35c\n\n_Your Chief of Staff \u2014 End of Day Jul 20, 2026_"
        }
    }
]

payload = {
    "channel": CHANNEL,
    "blocks": blocks,
    "text": "Daily Decision Digest - Monday Jul 20, 2026"
}

def preview():
    sys.stdout.buffer.write(
        ("\n=== SLACK PREVIEW ===\n" + json.dumps(payload, indent=2) + "\n=====================\n").encode("utf-8", errors="replace")
    )

def send():
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("ok"):
                print(f"[OK] Message sent to {CHANNEL}")
            else:
                print(f"[ERROR] Slack API error: {result.get('error')}")
                print(json.dumps(result, indent=2))
                sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e}")
        sys.exit(1)

if not TOKEN:
    print("[WARN] No SLACK_TOKEN found. Printing preview.")
    preview()
else:
    send()
