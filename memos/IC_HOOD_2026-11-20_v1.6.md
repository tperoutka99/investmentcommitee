# IC Memo: HOOD (Robinhood Markets, Inc.)
**Date:** 2026-11-20 | **Price:** $64.81 | **Market cap:** $58.4B | **Verdict:** PASS
**Conviction:** Medium | **Position:** None

## Verdict
PASS. At $64.81 the stock trades 26% above the $51.53 bull case and 2.26x the $28.65 base. To justify the price, ROE has to stay at 32.8% forever. Meanwhile all of Q3's growth came from event contracts, a legally exposed line (V1, V4 Verified). The business is good, but the price is not.

## Thesis
- The price needs too much. The reverse DCF needs a permanent ROE of 32.8%, against 22% in the base case. Even the industry-beta base ($40.31) is 38% below the price.
- Growth is narrow. Event contracts went from $27M to $173M. Revenue outside them was $1,251M vs $1,247M (V1 Verified). Some new event contracts have been stopped after state actions, and North Carolina and Kentucky taxes start 2027-01-01 (V4 Verified).
- Earnings are weakening. Q3 pretax income fell 1.4% and net income fell 15.8% (V2 Verified). Net interest fell 9% despite the hike (V3 Verified). Quality is real but already priced in: a 45.7% TTM operating margin and $3,129M of net cash (V5, V6 Verified).

## Macro backdrop
Neutral, Medium. Growth is strong (Q3 GDP 3.37%), but the 10Y is at 5.07% and a December hike is about 94% priced. Since V3 shows hikes are no longer lifting net interest, I lean toward Headwind.

## Valuation
On the bottom-up beta of 1.90: bear $11.87, base $28.65, bull $51.53. The price is above the whole range. The short seller's bear price is $31.42. On industry beta (0.60) the cases are $16.32 / $40.31 / $73.13, and the price sits in the upper half even there. The analyst mean target is $127.32, and FY2027 consensus revenue ($6,880M) is above the analyst's $6,359M.

## Bear case and response
| Bear point | Status | Response |
|---|---|---|
| All growth is event contracts, which face legal and tax attack | Unresolved | Flat core revenue, state exits and the 2027 taxes are verified (V1, V4). The Ninth Circuit result (V9) and Meta (V11) are not weighted. |
| Earnings are getting worse under a revenue beat | Unresolved | Pretax -1.4%, tax rate 12.3% to 23.8% and net income -15.8% are all verified (V2). |
| Credit risk and leverage are rising; hikes no longer help | Partly resolved | User receivables +31% (V7) and net interest -9% (V3) are verified. The card figures (V8) and CEO sales (V10) are unchecked. Net cash cushions the risk. |

Status is exactly one of: Resolved / Partly resolved / Unresolved.

## Data flags
- Price check (+0.1%): no flag. I use the fresh $64.81.
- C1 growth: consensus is above the analyst, which argues against the short seller's 8%. Even the bull case is below the price, so it is not decisive.
- C2 macro: I keep Neutral with a Headwind tilt (V3).
- C3 beta: the largest sensitivity. The industry-beta base ($40.31) still does not reach the price.
- C4 revolver: undrawn, no effect.
- V1–V7 Verified: they support the thesis as written.
- V8, V9, V10 Not checked: excluded from the thesis and given low weight.
- V11 Not found: excluded.
- V12 Verified: the CPI is corrected to 3.74%. The macro view does not change.

## Kill criteria
- The price closes at or below $28.65 (base value): the PASS is void, and we re-underwrite for a BUY.
- The Q4 report (est. 2027-02-09) shows revenue outside event contracts up 10% or more y/y: re-underwrite.
- Event-contract revenue in Q4 is at or above $173M after the 2027-01-01 state taxes, with no new state exits disclosed in the 10-K: re-underwrite.

## Catalysts
| Date | Event |
|---|---|
| 2026-12-09 | FOMC decision (hike about 94% priced) |
| 2026-12-10 | November CPI |
| 2027-01-01 | North Carolina and Kentucky prediction-market taxes take effect |
| 2027-02-09 | Q4 2026 earnings (estimated) |

## Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $64.81 | Robinhood (Data flags) | 2026-11-20 |
| Base value (bottom-up beta) | $28.65 | Equity, dcf.py | 2026-11-20 |
| Reverse DCF ROE | 32.8% | Equity | 2026-11-20 |
| Q3 revenue outside event contracts | $1,251M vs $1,247M | 10-Q (V1) | 2026-09-30 |
| Cash / debt | $5,829M / $2,700M | 10-Q (V6, V5) | 2026-09-30 |
| Receivables from users | $23,598M | 10-Q (V7) | 2026-09-30 |
| Next earnings | 2027-02-09 (est.) | Robinhood | 2026-11-20 |

## What changed since last memo
- The verdict moves from WATCH (buy at $40) to PASS. The base value fell from $43.45 to $28.65 and the bull case from $73.02 to $51.53, so the price is now above the bull case.
- The reverse DCF test is now ROE (32.8%) instead of operating margin (62.4%).
- Debt is corrected from $2,200M to $2,700M (V5 Verified).
- The short seller's bear price fell from $38 to $31.42, and the earnings deterioration is now verified (V2).
- CPI is corrected to 3.74% for September (V12).

## Data
```data
agent: memo
ticker: HOOD
date: 2026-11-20
verdict: PASS
conviction: Medium
position: None
price: 64.81
value_bear: 11.87
value_base: 28.65
value_bull: 51.53
short_bear_price: 31.42
macro_call: Neutral
buy_below: 28.65
exit_below: none
exit_above: none
kill_events: Q4 2026 report shows revenue outside event contracts up 10% or more y/y ; Q4 event-contract revenue at or above 173M after 2027-01-01 state taxes with no new state exits disclosed
watch_trigger: none
review_by: 2027-02-09
```
