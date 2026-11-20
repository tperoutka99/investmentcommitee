# Data flags: HOOD, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $65.80 | $59.3B (900.49M shares) | Equity and short reports | 2026-11-20 |
| Fresh quote | $65.08 | $58.6B (900.49M shares) | Robinhood | 2026-11-20 16:30 UTC |

**Difference:** -1.1%. No flag (under 2%).

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | FY2027 revenue growth | Equity: 20% a year for 2 years (FY2027 $6,360M); Yahoo consensus FY2027 $6,880M | Short: about 6% ($5.6B), because revenue excluding event contracts is flat | Judgment. Inputs verified in V1 and V2. Consensus is above both |
| C2 | Macro call | Macro: Neutral (floating-rate interest income offsets a 5%+ 10Y) | Short: Headwind (net interest revenue fell 9% despite higher rates) | Judgment. The 9% fall is verified in V3 |
| C3 | Debt counted in valuation | Equity: $2,200M convertible only; excludes $839M of non-recourse credit-card trust borrowings ($0.93/share if counted) | — | Classification. 10-Q balance sheet long-term borrowings are $2,660M at 2026-09-30, which includes the $500M Series 2026-1 trust notes |
| C4 | Beta | Bottom-up 1.89 (crypto and fintech peers) | Industry table 0.60 (Brokerage & Investment Banking) | Gap 1.29. Base $43.45 vs $58.71. Not a factual conflict but the largest sensitivity in the equity report |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Q3 revenue $1,424M vs $1,274M (+12%); event contracts $173M vs $27M; so revenue excluding event contracts ≈$1,251M vs ≈$1,247M (flat) | Verified | 10-Q filed 2026-10-28, revenue disaggregation note and MD&A. The short report says $29M a year ago; the 10-Q says $27M. The conclusion (flat) holds |
| V2 | Crypto revenue -55%; diluted EPS -16% ($0.51 vs $0.61); net income -16% | Verified | 10-Q filed 2026-10-28 (MD&A: cryptocurrencies $268M to $120M; "diluted EPS decreased 16% to $0.51") |
| V3 | Net interest revenue fell 9% | Verified | 10-Q filed 2026-10-28: $456M (Q3 2025) to $415M (Q3 2026) |
| V4 | Not collecting or remitting federal excise tax on event contracts | Verified | 10-Q filed 2026-10-28: "We have not collected or remitted federal excise tax on event contracts offered through RHD because we do not believe these contracts are subject to such tax." The short seller's ≈$164M a quarter is its own estimate (assumed 2% rate and $0.50 average contract price, neither in the filing) |
| V5 | Receivables from users $23.6B, +64% | Partly verified | 10-Q balance sheet: $23,598M at 2026-09-30 vs $17,994M at 2025-12-31 (+31% year to date). The year-on-year +64% was not checked against a 2025-09-30 figure. Platform-asset table: receivables from customers (mainly margin) $22.1B vs $13.8B a year earlier (+60%) |
| V6 | Adjusted Net Income was reissued over a tax sign error | Partly verified | 8-K/A filed 2026-10-28, items 2.02/9.01: Exhibit 99.1 is a "Revised press release dated October 27, 2026". The reason for the revision was not located in the 8-K/A text |
| V7 | Louisiana sued Robinhood and other prediction-market operators on 2026-11-12 | Not found | Web only (The Block). No 8-K filed after 2026-10-28; the 10-Q predates the suit |
| V8 | Strict cash $5,829M; no corporate marketable debt securities | Verified | 10-Q cash-flow reconciliation: cash and cash equivalents at period end $5,829M (2026-09-30). The equity analyst reports it matches the $5.8B in the earnings release |
| V9 | $2.2B 0.00% convertible notes due 2029-10-01, conversion ≈$174.42 | Verified | 10-Q Note 11: "$ 2.2 billion aggregate principal amount of 0.00 % convertible senior notes due 2029"; initial conversion rate 5.7332 shares per $1,000 (= $174.42) |
| V10 | Revenue growth was +32% in Q2 2026 | Not checked | — |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- Robinhood's investor site (investors.robinhood.com) was unreachable, so the equity analyst used the 8-K earnings release and the company newsroom.
- bls.gov blocked both fetch methods; the macro strategist took BLS dates from web search.
- Revenue by region was not found, so the dollar exposure is not assessed.
- 13F holdings: not assessed (no data).
- Two Indonesian acquisitions (announced December 2025) have no disclosed size: not assessed. The equity analyst gives $1.11/share per $1B of target net debt.
- The DCF and comps scripts are built for non-financial companies; the equity analyst adapted the DCF and did the comps by hand.
- Next earnings date 2027-02-09 is an estimate (Robinhood).

## Data
```data
agent: data_flags
ticker: HOOD
date: 2026-11-20
fresh_price: 65.08
fresh_price_time: 2026-11-20T16:30:13Z
price_diff_pct: -0.011
verified: 6
partly_verified: 2
contradicted: 0
not_found: 1
not_checked: 1
```
