# Daily Decision Summary — Chief of Staff Bot

## Friday, June 11, 2026

---

### Today's Meetings (4 total)

---

### 1. Hiring Leads Standup — 8:45 AM PDT
**Attendees:** Manan, Fadi, Dana, Matan, Cindy, Jatin, Ray, Nelson, Jeff, Usman

#### Key Decisions Made:
- **PAUSE Indeed source claiming.** The 3–6 month process with 4–5 day turnaround cycles is burning engineering bandwidth. Decision: redirect engineers to higher-impact work immediately.
- **Validate before building on Jack & Jill.** Matan's "personal recruiter" framing must be tested with 5 real customers *before* committing engineering. Value prop is NOT yet validated.
- **"No regrets" work framing adopted.** Features like comms agent, UX paper cuts, deprecating V1, domain events, and scheduling fixes proceed regardless of which value prop wins.
- **Unhealthy trial auto-trigger.** Auto-fire a sales touchpoint in Salesforce within 24 hours if a trial has fewer than 5 applicants in the first week — no manual check required.
- **Boost as a closing lever.** $50 cost vs. monthly subscription is net-positive. Testing admin-side boost tool so reps can boost on behalf of customers in one click.

#### Action Items:
| Owner | Action | Deadline |
|-------|--------|----------|
| Dana + Matan | Map hypothesis tree, identify big swings to validate | Today |
| Dana + Jatin | Align on intake experiment build approach | Today |
| Fadi, Dana, Jatin, FE | Schedule product walkthrough → surface no-regrets burndown list | ASAP |
| Usman | Design Salesforce auto-trigger: sales motion fires in 24h if < 5 applicants | Soon |
| Manan + Usman | Align on boost positioning + sales call playbook for unhealthy trials | Soon |

#### Rationale:
Indeed source claiming is a losing battle at Homebase's scale (~6K jobs/month vs. 1M+ on Indeed). The value prop uncertainty on Jack & Jill is real — committing a full quarter to an unvalidated belief is high-risk. The "no regrets" framing is smart: it gives engineering meaningful work while the hypothesis tree gets built out.

---

### 2. Product/Sales Bi-Weekly — 9:00 AM PDT
**Note:** Meeting was canceled mid-call. Bobby and note-taker connected before cancellation went through; rest of team never showed.

#### Signal Captured Anyway:
- **Outreach cadence:** Front-loaded (2x/day) felt too aggressive. Every 2–3 days after first contact is working better.
- **Contact overlap risk:** No shared Salesforce tracking across reps → duplicate outreach happening. Customer already complained about being contacted by multiple reps. **This is a burning problem to fix.**
- **Call timing sweet spot:** 10am–noon or 1pm–3pm in prospect's time zone.

#### Action Items:
| Owner | Action |
|-------|--------|
| Usman / RevOps | Implement contact-level outreach tracking in Salesforce to prevent duplicate touchpoints |

---

### 3. Hackathon Unlimited Show & Tell — 10:30 AM PDT
- No meeting notes recorded. Worth following up to capture any outputs or commits from the hackathon team.

---

### 4. Applicant Flow T-Shirt Sizing — 1:30 PM PDT

#### Sizing Decisions Locked In:
| Feature | Eng | Design | Dependencies |
|---------|-----|--------|--------------|
| Homebase Boost for Sales (admin) | Low | None | — |
| Dollar-for-dollar matching | Low | None | Billing |
| Sponsored jobs API (OEM ↔ Indeed) | Medium | Small | — |
| Job seeker manual intake | Low | Low | — |
| Single vs. multi-job email | Low | Low | — |
| SMS vs. email vs. push | Low | Low | — |
| HTML job pages (JS → HTML) | Medium | None | Claude vibe-code |
| Automated email outreach | Medium | None | **DE/Iterable pattern** |
| Employee referral | Medium | Medium | Abigail (buffer needed) |
| Show talent pool to OEM | Large | Medium | — |
| Job creation flow (fraud + role recs + salary recs) | High | High | Treat as ONE design pass |
| Auto go-live (skip "in review") | High | Medium | — |
| Job description optimization (LLM) | Medium | Low | LLM + DE |
| Salary recommendations | Low | Low | LLM |

#### Key Decisions:
- **Job creation flow = one design workstream.** Fraud check, role recommendations, and salary recommendations all touch the same job description screen. Don't split them — introduce error states together. Combined: High effort.
- **Employee referral → Abigail.** Share modal already exists. Reuse it. Build buffer into her timeline.
- **Automated email outreach is potentially zero-product-eng.** If data engineering already has a pattern to hit Iterable directly, product engineering may not be needed at all. **Critical to confirm ASAP.**

#### Action Items:
| Owner | Action |
|-------|--------|
| Manan | Confirm with DE: do they have an existing pattern to call Iterable API directly? |
| Manan + Cindy | Align on job creation flow design pass (fraud + role recs + salary recs together) |
| Manan | Assign employee referral to Abigail with explicit timeline + buffer built in |

---

## Today's Top 3 Follow-Ups (Don't Let These Slip!)

1. **🔴 DE Iterable check** — Could eliminate a full medium-eng project from the roadmap. Confirm today or tomorrow.
2. **🔴 Salesforce contact overlap** — Customers are already getting burned. Needs a fix before it hurts more deals.
3. **🟡 Dana + Matan hypothesis tree** — This is the strategic foundation of Q3. Make sure it happens today as planned.

---

*Generated by Chief of Staff bot at 5:00 PM PDT · Friday, June 11, 2026*
