# IC Memo: HOOD (Robinhood Markets, Inc.)
**Date:** 2026-11-20 | **Price:** $65.08 | **Market cap:** $58.6B | **Verdict:** WATCH
**Conviction:** Medium | **Position:** None

## Verdict
WATCH. The business is high quality, but $65.08 is 50% above the $43.45 base value and close to the $73.02 bull case. Revenue excluding event contracts is flat (verified), so the price relies on the riskiest revenue line. We buy at or below $40, a margin below base value.

## Thesis
- Quality is real: TTM GAAP operating margin is 45.7% and the balance sheet is net cash. Cash is $5,829M (V8 Verified) against $2,200M of 0.00% converts (V9 Verified).
- The price needs too much. The reverse DCF at $65.80 needs 1.52x the base growth path (19.2% 10-year CAGR) or a 62.4% operating margin.
- Growth is narrow. Q3 revenue excluding event contracts was about $1,251M vs $1,247M (V1 Verified), and crypto revenue fell 55% (V2 Verified).

## Macro backdrop
Neutral, Medium. Floating-rate asset income and fixed-rate debt offset a 5.07% 10Y and a roughly 94% chance of a December hike. The short seller's Headwind case has a point, because net interest revenue fell 9% (V3 Verified) despite high rates.

## Valuation
On the bottom-up beta of 1.89, the cases are bear $19.74, base $43.45 and bull $73.02. The price sits about 85% of the way from bear to bull. Even the industry-beta base ($58.71, beta 0.60) is below the price. The short seller's bear price is $38. The analyst mean target is $127.32, and consensus FY2027 revenue ($6,880M) is above the analyst's $6,360M.

## Bear case and response
| Bear point | Status | Response |
|---|---|---|
| Ex-event-contract revenue flat; state bans; unaccrued excise tax | Unresolved | Flat revenue and the unaccrued excise tax are verified. The $164M/quarter tax figure is the short seller's own estimate, and the Louisiana suit is not found, so neither is weighted. |
| Growth falling fast (Q2 +32% to Q3 +12%, EPS -16%) | Partly resolved | Q3 +12% and EPS -16% are verified. Q2 +32% is not checked. October net deposits above $13B and 5.2M Gold subscribers argue against a collapse. |
| Credit risk growing faster than revenue | Partly resolved | Receivables are $23.6B, +31% year to date. +64% y/y is unchecked; customer receivables are +60% y/y. Card trust debt of $839M is non-recourse ($0.93/share if counted). |

Status is exactly one of: Resolved / Partly resolved / Unresolved.

## Data flags
- Price check (-1.1%): no flag. I use the fresh $65.08; the verdict does not change.
- C1 growth: consensus is above both views. Treated as judgment, and it is the key Q4 test.
- C2 macro: I keep Neutral, but V3 tilts the risk toward Headwind.
- C3 debt: counting the card trust costs $0.93/share. Immaterial to the verdict.
- C4 beta: the largest sensitivity. Even the $58.71 industry-beta base is below the price, so it does not rescue a BUY.
- V1, V2, V3, V8, V9 Verified: they support the thesis as written.
- V4 Verified: the excise tax exposure is real but unsized, and it is a kill criterion.
- V5, V6 Partly verified: credit concern kept at moderate weight. The reason for the reissued figure is unknown, a mild governance negative.
- V7 Not found: Louisiana suit excluded from the thesis.
- V10 Not checked: Q2 +32% not relied on.

## Kill criteria
- Price closes above $73.02 (bull case) before the trigger hits: re-underwrite, and the watch is off.
- The company accrues, or is assessed, federal excise tax on event contracts (10-Q/8-K disclosure).
- The Q4 report (est. 2027-02-09) shows revenue excluding event contracts down y/y, or event-contract revenue below $173M.

## Catalysts
| Date | Event |
|---|---|
| 2026-12-09 | FOMC decision (hike ~94% priced) |
| 2026-12-10 | November CPI |
| 2027-02-09 | Q4 2026 earnings (estimated) |

## Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $65.08 | Robinhood (Data flags) | 2026-11-20 |
| Market cap | $58.6B | Data flags | 2026-11-20 |
| Base value (bottom-up beta) | $43.45 | Equity, dcf.py | 2026-11-20 |
| Reverse DCF margin | 62.4% | Equity | 2026-11-20 |
| Q3 revenue ex event contracts | ~$1,251M vs ~$1,247M | 10-Q (V1) | 2026-09-30 |
| Cash / convert debt | $5,829M / $2,200M | 10-Q (V8, V9) | 2026-09-30 |
| Receivables from users | $23,598M | 10-Q (V5) | 2026-09-30 |
| Next earnings | 2027-02-09 (est.) | Robinhood | 2026-11-20 |

## What changed since last memo
No prior memo.

## Data
```data
agent: memo
ticker: HOOD
date: 2026-11-20
verdict: WATCH
conviction: Medium
position: None
price: 65.08
value_bear: 19.74
value_base: 43.45
value_bull: 73.02
short_bear_price: 38
macro_call: Neutral
buy_below: 40
exit_below: none
exit_above: 73.02
kill_events: Company accrues or is assessed federal excise tax on event contracts ; Q4 2026 report shows revenue excluding event contracts down y/y or event-contract revenue below 173M
watch_trigger: Price at or below 40
review_by: 2027-02-09
```
