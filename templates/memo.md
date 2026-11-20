# IC Memo: <TICKER> (<Company>)
**Date:** <YYYY-MM-DD> | **Price:** $<price> | **Market cap:** $<cap> | **Verdict:** <BUY / PASS / WATCH>
**Conviction:** <High / Medium / Low> | **Position:** <None / Starter / Full>

## Verdict
<2-3 sentences: the decision and the single most important reason.>

## Thesis
- <Bullet tied to a number>
- <Bullet tied to a number>
- <Bullet tied to a number>

## Macro backdrop
<Call and 1-2 sentences.>

## Valuation
<What the price implies; bear / base / bull values; where the price sits in that range.>

## Bear case and response
| Bear point | Status | Response |
|---|---|---|
| | | |
| | | |
| | | |

Status is exactly one of: Resolved / Partly resolved / Unresolved.

## Data flags
- <How each flag affects your view, one line each>

## Kill criteria
- <Measurable condition>
- <Measurable condition>
- <Measurable condition (optional)>

## Catalysts
| Date | Event |
|---|---|

## Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|

## What changed since last memo
<Bullets, or "No prior memo.">

## Data
```data
agent: memo
ticker: <TICKER>
date: <YYYY-MM-DD>
verdict: <BUY|PASS|WATCH>
conviction: <High|Medium|Low>
position: <None|Starter|Full>
price: <number>
value_bear: <number>
value_base: <number>
value_bull: <number>
short_bear_price: <number>
macro_call: <Tailwind|Neutral|Headwind>
buy_below: <price at which this becomes / stays a BUY, or "none">
exit_below: <price kill level, or "none">
exit_above: <price at which to take profit or re-underwrite, or "none">
kill_events: <the non-price kill criteria, separated by " ; ">
watch_trigger: <the WATCH trigger, or "none">
review_by: <YYYY-MM-DD: the date to recheck this call, usually the next earnings date>
```
