# Data flags: <TICKER>, <YYYY-MM-DD>

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | | | | |
| Fresh quote | | | Robinhood | |

**Difference:** <x%>. <"No flag (under 2%)" or "FLAG: over 2%".>

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|

<Write "None." under the table if empty.>

## Verification
| # | Claim | Status | Source |
|---|---|---|---|

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- <One line each, or "None.">

## Data
```data
agent: data_flags
ticker: <TICKER>
date: <YYYY-MM-DD>
fresh_price: <number>
fresh_price_time: <ISO time>
price_diff_pct: <decimal>
verified: <count>
partly_verified: <count>
contradicted: <count>
not_found: <count>
not_checked: <count>
```
