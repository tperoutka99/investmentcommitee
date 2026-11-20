# Data flags: HOOD, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $64.77 | $58,325M (900.49M shares) | Equity and short reports | 2026-11-20 16:40 UTC |
| Fresh quote | $64.81 | $58,358M (900.49M shares) | Robinhood | 2026-11-20 16:53 UTC |

**Difference:** +0.1%. No flag (under 2%).

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | Base-case book-equity growth | Equity: 15% (ROE 22%); FY2027 revenue $6,359M vs consensus $6,880M | Short: about 8%, because revenue outside event contracts grew 0.3% | Judgment. The 0.3% is verified (V1). Consensus is above the analyst |
| C2 | Macro call | Macro: Neutral, "a hike lifts income" | Short: Headwind; net interest fell 9% after the September hike | Judgment. The 9% fall is verified (V3) |
| C3 | Beta | Bottom-up 1.90 (SCHW, IBKR, COIN, SOFI) | Industry table 0.60 (Brokerage & Investment Banking) | Gap 1.30: base $28.65 vs $40.31. The short seller argues the 0.60 is not credible for this revenue mix |
| C4 | RHS revolver size | Equity: $3,250M (8-K 2026-03-24) | Macro task facts: $3,325M (10-Q 2026-10-28) | Minor. The 10-Q gives a $3.325B commitment as of 2026-09-30. Undrawn either way, so no valuation effect |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Event contracts $173M vs $27M; revenue $1,424M vs $1,274M; revenue outside event contracts ≈ flat (+0.3%) | Verified | 10-Q filed 2026-10-28, revenue disaggregation note ($1,251M vs $1,247M) |
| V2 | Q3 pretax income -1.4%, tax rate 12.3% to 23.8%, net income to Robinhood -15.8%; $60M other expense in Q3 | Verified | 10-Q income statement: pretax $634M to $625M; tax $78M to $149M; net income attributable $556M to $468M; other income (expense) $(1)M to $(60)M |
| V3 | Net interest revenue fell 9% | Verified | 10-Q: $456M to $415M |
| V4 | Robinhood has stopped offering certain new event contracts after state actions; North Carolina and Kentucky prediction-market taxes start 2027-01-01; federal excise tax not collected or remitted | Verified | 10-Q filed 2026-10-28 (risk factors and tax disclosure): "decide, to stop offering certain new event contracts as a result of actual or threatened state enforcement actions"; "North Carolina and Kentucky have each enacted new state-level taxes on prediction market operators, effective January 1, 2027" |
| V5 | Debt $2,700M principal (equity report; the earlier v1.4 run used $2,200M) | Verified | 10-Q cash flow: "Proceeds from issuance of long-term borrowings ... 2,700" (9M 2026) = $2.2B convertible + $500M Series 2026-1 notes |
| V6 | Strict cash $5,829M | Verified | 10-Q cash-flow reconciliation, cash and cash equivalents at 2026-09-30 |
| V7 | Receivables from users $23.6B, +31% in nine months | Verified | 10-Q balance sheet: $17,994M (2025-12-31) to $23,598M (2026-09-30) |
| V8 | Purchased card receivables $786M to $1.51B (+92%); allowance 8.1% | Not checked | The 10-Q's card allowance tables were located but not read for these totals |
| V9 | Ninth Circuit denied RHD relief against Nevada | Not checked | The 10-Q lists RHD's August 2025 Nevada suit; the appellate outcome was not located in the text searched |
| V10 | CEO sold $148.9M at an average $119.15 and adopted a new plan to sell 1.9M shares (10-Q Item 5) | Not checked | Item 5 text and the CEO's Form 4s were not read |
| V11 | Meta building a rival prediction-market app; Louisiana lawsuit; about $6B of October net deposits from one family's Trump Account contribution | Not found | Web only. No 8-K after 2026-10-28 |
| V12 | Macro CPI y/y 3.74% for September 2026 (no October figure) | Verified | FRED CPIAUCNS: Sep 2026 336.940 / Sep 2025 324.800 = +3.74%. October 2025 is blank in FRED (2025 shutdown), so October y/y cannot be computed. The v1.4 run's "3.9% (Oct), 4.0% (Sep)" was wrong; the ADBE and SPCX v1.x macro reports carried the same figures |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- Robinhood's investor site and bls.gov refuse automated requests; agents used the 8-K earnings release and WebSearch.
- Revenue by region not found, so the dollar exposure is not assessed.
- 13F holdings: not assessed (no data).
- "Pending acquisitions" in the Q3 release are unidentified: not assessed. The equity analyst gives $1.11/share per $1B of target net debt.
- The equity template's comps table has no P/B or ROE columns, so the financial-firm multiples could not be shown in it.
- Next earnings date 2027-02-09 is an estimate (Robinhood).

## Data
```data
agent: data_flags
ticker: HOOD
date: 2026-11-20
fresh_price: 64.81
fresh_price_time: 2026-11-20T16:53:53Z
price_diff_pct: 0.001
verified: 8
partly_verified: 0
contradicted: 0
not_found: 1
not_checked: 3
```
