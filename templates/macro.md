# Macro: <TICKER>, <YYYY-MM-DD>
**Call:** <Tailwind / Neutral / Headwind> | **Confidence:** <High / Medium / Low>

## 1. Regime
<One sentence: where the economy and the Fed are.>

## 2. Data
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| 10Y Treasury | | | | FRED DGS10 |
| 2Y Treasury | | | | FRED DGS2 |
| Effective fed funds | | | | FRED DFF |
| CPI y/y | | | | FRED CPIAUCNS |
| CPI 3-month annualized | | | | FRED CPIAUCSL |
| Unemployment rate | | | | FRED UNRATE |
| Payrolls change | | | | FRED PAYEMS |
| Real GDP, q/q annualized | | | | FRED GDPC1 |
| Dollar proxy (UUP) | | | | Twelve Data |

**Next FOMC (<date>) odds**
| Outcome | Polymarket | Kalshi |
|---|---|---|
| Hike | | |
| Hold | | |
| Cut | | |

## 3. Sensitivity
- **Rates:** <tie to the debt-structure fact, quoting its numbers>
- **Growth:**
- **Inflation:**
- **Dollar:** <tie to the revenue-by-region fact, quoting its numbers>

## 4. Call
**<Call>, <Confidence>.** <One-sentence reason.>

## 5. Next 30 days
| Date | Event | Source |
|---|---|---|

## 6. What would flip the call
<One measurable condition.>

## Notes
- <Optional: data caveats. Write "None." if there are none.>

Tool access: <every assigned tool that failed and what you used instead, or "all assigned tools worked">

## Data
```data
agent: macro
ticker: <TICKER>
date: <YYYY-MM-DD>
call: <Tailwind|Neutral|Headwind>
confidence: <High|Medium|Low>
rf_10y: <decimal, e.g. 0.0507>
fed_funds: <decimal>
cpi_yoy: <decimal>
unemployment: <decimal>
uup: <price>
next_fomc_date: <YYYY-MM-DD>
next_fomc_hike_prob: <decimal, or "not assessed">
flip_condition: <one line>
```
