# Data flags: ORCL, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $102.45 | $318,614M (3,109.95M shares, pro forma for the Nov stock sale) | Equity and short reports | 2026-11-20 17:01 UTC |
| Fresh quote | $102.57 | $318,971M (3,109.95M shares) | Robinhood | 2026-11-20 17:15 UTC |

**Difference:** +0.1%. No flag (under 2%).

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | Sales-to-capital | Equity: 0.5–1.5 in the base case | Short: about 0.3; observed 0.13 (capital +$141.9B vs revenue +$18.8B since FY24) | Judgment. Drives the base value; terminal value is 78.6% of it |
| C2 | Macro flip condition | Macro: 10Y below 4.50% with a Fed hold flips to Neutral | Short: Oracle's 7.00–8.65% coupons reflect its own credit spread, so a lower 10Y does not fix its funding cost | Judgment. The coupons are verified (V4) |
| C3 | Unrecognized tax benefits | Equity: $13.2B gross (10-K), not subtracted (-$4.16/share if it were) | Short: $10.1B | Different measures of the same 10-K disclosure (gross vs the portion that would affect the tax rate); not checked |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Strict cash $37,077M ($36,369M cash and equivalents + $708M marketable securities) | Partly verified | 10-Q filed 2026-09-11 balance sheet. The fair-value note says investments "consist of money market funds, time deposits and marketable equity securities", and its table shows only money-market funds ($28,204M) and time deposits ($844M). Whether all $708M is debt securities is not confirmed; the amount is under 2% of cash |
| V2 | $10.0B stock sale: 86,206,897 shares, closed 2026-11-04 | Verified | 8-K filed 2026-11-04, Item 8.01 ("agreed to issue and sell 86,206,897 shares ... closed on November 4, 2026") |
| V3 | Investor Day cap: additional raises through FY30 limited to $20B ($10B equity, $10B debt), set 2026-10-28; used up by the Nov 4 offerings | Verified | 8-K filed 2026-10-28, Ex.99.1: "Committed to limiting additional capital raises through FY30 to $20 billion, excluding refinancing of existing debt, split between $10 billion in equity and $10 billion in gross debt"; with V2 and V4, both halves were issued within a week |
| V4 | $10B senior notes at 7.000%–8.650%, 2029–2046 | Verified | 424B2 filed 2026-11-02/04: $2.0B 7.000% 2029, $1.75B 7.450% 2031, $2.25B 7.850% 2033, $2.5B 8.000% 2037, $1.5B 8.650% 2046 |
| V5 | $288B of data-center leases not yet commenced, 15–19-year terms; 13% of the $664B RPO due within 12 months | Verified | 10-Q filed 2026-09-11: "$ 288 billion of additional lease commitments, substantially all related to data center arrangements ... expected to commence between the second quarter of fiscal 2027 and fiscal 2029 and for terms of fifteen to nineteen years"; RPO "$ 664 billion ... approximately 13 % as revenues over the next twelve months" |
| V6 | Q1 FCF -$5.4B only after $11.4B of customer prepayments (≈ -$16.8B without them) | Verified | 10-Q cash flow: operating cash flow $23,103M including "Increase in deferred revenues from customer prepayments with significant financing component 11,363"; capex $(28,499)M |
| V7 | 10-K risk factor: excess data-center space "without receiving corresponding revenue" | Verified | 10-K filed 2026-06-22: "we could be locked into multi-year commitments for excess data center space and related capital expenditures, as well as associated financings, without receiving corresponding revenue." Whether it is new in this 10-K was not checked |
| V8 | Ellison adopted a plan to sell up to 50M shares, then cancelled it with no sales | Verified | 10-Q Item 5 (plan adopted 2026-06-22, up to 50 million shares); 8-K filed 2026-09-14, Item 8.01: "has cancelled his 10b5-1 Plan ... No Oracle stock was sold under the plan prior to termination" |
| V9 | ~54% of RPO is OpenAI's; Tencent ($7B) and Microsoft deals lost | Not found | Web only. The 10-Q text searched does not name OpenAI or any customer concentration; no 8-K on either deal |
| V10 | In June, Oracle said it did not expect to issue more debt in calendar 2026 | Not found | Not located in the 424B5 (2026-06-23), 10-K or 10-Q text searched |
| V11 | S&P rating BBB- (cut in July); CDS around 305bp | Not found | Web only; no company filing checked states the rating |
| V12 | Next earnings 2026-12-14, after close | Not checked | Robinhood (equity report: confirmed) |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- investor.oracle.com did not resolve; the equity analyst used oracle.com/news and the EDGAR 8-K exhibits.
- The fixed vs floating split of the $125.3B of borrowings was not found in the 10-Q.
- bls.gov refused automated requests; BLS dates are from WebSearch.
- scripts/peers.py missed Oracle's own debt, so the analyst computed ORCL's comps row by hand; SAP was dropped for stale XBRL.
- 13F holdings: not assessed (no data).
- The equity analyst notes Q1's -$5.4B FCF is counted twice in its model (about -$1.70/share, conservative).

## Data
```data
agent: data_flags
ticker: ORCL
date: 2026-11-20
fresh_price: 102.57
fresh_price_time: 2026-11-20T17:15:13Z
price_diff_pct: 0.001
verified: 7
partly_verified: 1
contradicted: 0
not_found: 3
not_checked: 1
```
