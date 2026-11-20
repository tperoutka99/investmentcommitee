# Data flags: AMD, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $433.41 | $717,325M (1,655.07M shares incl. World Labs issue) | Equity and short reports | 2026-11-20 |
| Fresh quote | $433.73 | $717,855M (1,655.07M shares) | Robinhood | 2026-11-20 18:10 UTC |

**Difference:** +0.1%. No flag (under 2%). The stock is down 11% on the day from the $489.19 close on 2026-11-19.

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | Target operating margin (R&D capitalized) | Equity: 38% (base year 29.7%) | Short: about 30%; the analyst's own config then gives $288 instead of $371 | Judgment. The single largest driver of the base value |
| C2 | Warrant dilution | Equity: 53M / 160M / 320M shares in bear / base / bull; $407 base with none | Short: 320M shares (19%) treated as a real cost, plus $4.5B of warrant value deducted from future revenue | Partly judgment. Terms verified (V3) |
| C3 | Macro call strength | Macro: Headwind, Low | Short: Headwind but too mild, because AMD guarantees $8.5B of partner obligations | Judgment. The guarantees are verified (V4) |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Strict cash $15,776M; short-term investments are debt securities | Verified | 10-Q filed 2026-11-04: cash and equivalents $7,404M + short-term investments $8,372M. Fair-value note: corporate debt $5,931M, US government and agency $2,325M, non-US government $11M, time deposits $86M, plus asset-backed securities |
| V2 | Q3 net income ($2,428M) helped by a one-off $772M tax benefit | Verified | 10-Q tax note: Q3 income tax benefit of $555M (effective rate -29.6%) on pretax income of $1,868M, which "included a discrete tax benefit related to stock-based compensation of $772 million" |
| V3 | Customer warrants for up to 320M shares at $0.01, OpenAI and Meta | Verified | 10-Q: two customers (October 2025 and February 2026), each up to 160 million shares at $0.01, vesting on purchase milestones and stock-price targets; the risk factors name OpenAI OpCo., LLC and Meta Platforms, Inc. "exercisable for up to a combined 320 million shares" |
| V4 | Off-balance-sheet exposure: $8.5B guarantees, $13.3B uncommenced data-center leases for partners, $6.2B cloud-capacity commitments | Verified | 10-Q Note 11: "maximum potential amount of future payments under these guarantees was $ 8.5 billion"; leases "expected to be assigned or subleased to commercial partners ... $ 13.3 billion", starting Q2 FY2027; "commitments for cloud compute capacity arrangements ... were $6.2 billion" |
| V5 | World Labs acquisition ($8.2B, all stock) closed 2026-11-13; Taalas ($2.9B incl. up to $1.4B contingent) pending | Verified | 10-Q (pending-acquisitions note) and 8-K/A filed 2026-11-16, Item 3.02 (closing on November 13, 2026, paid in common stock). The 14.98M share count was not checked |
| V6 | CEO Lisa Su sold shares at about $502–526 on 2026-11-16 | Partly verified | Form 4 filed 2026-11-18: Lisa T. Su, Chair, President & CEO, code S sales on 2026-11-16 at $502.06–$505.21 in the lots read. The 70,000-share total and the $526 top were not summed |
| V7 | 9-month operating cash flow and capex; Q3 FCF $554M | Partly verified | 10-Q: 9M operating cash flow $6,523M, capex $1,845M (9M FCF $4,678M). The Q3-only $554M needs the Q2 10-Q, which was not read |
| V8 | Analyst price-target cuts (Mizuho, BofA) | Not found | Web only; no company filing |
| V9 | Q4 revenue guide of about $17.0B | Not checked | 8-K filed 2026-11-03 not read |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- Target net debt for World Labs and Taalas: not assessed (both private). The equity analyst gives $0.55/share per $1B.
- Taalas cash/stock split not disclosed; the analyst deducted the $1.5B upfront payment as cash.
- bls.gov refused automated requests; BLS dates come from WebSearch.
- 13F holdings: not assessed (no data).
- The equity DCF's self-audit flags imputed ROC above 40% in base years 4–10 (peak 42.6%) and bull years 2–10 (peak 58.0%).
- Next earnings date 2027-02-02 is an estimate (Robinhood).

## Data
```data
agent: data_flags
ticker: AMD
date: 2026-11-20
fresh_price: 433.73
fresh_price_time: 2026-11-20T18:10:41Z
price_diff_pct: 0.001
verified: 5
partly_verified: 2
contradicted: 0
not_found: 1
not_checked: 1
```
