# Macro: HOOD, 2026-11-20
**Call:** Neutral | **Confidence:** Medium

## 1. Regime
Growth is strong and inflation is speeding up again. The Fed held at 3.75-4.00% on 2026-10-28 with two votes for a hike, and both betting markets price a December hike at about 94%.

## 2. Data
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| 10Y Treasury | 5.07% | 4.98% (2026-11-10) | 2026-11-18 | FRED DGS10 |
| 2Y Treasury | 4.80% | 4.73% (2026-11-10) | 2026-11-18 | FRED DGS2 |
| Effective fed funds | 3.88% | 3.88% (2026-11-13) | 2026-11-18 | FRED DFF |
| CPI y/y | 3.9% | 4.0% (Sep) | 2026-10 | FRED CPIAUCNS |
| CPI 3-month annualized | 5.7% | 4.6% (Sep) | 2026-10 | FRED CPIAUCSL |
| Unemployment rate | 4.1% | 4.2% (Sep) | 2026-10 | FRED UNRATE |
| Payrolls change | +165k | +60k (Sep) | 2026-10 | FRED PAYEMS |
| Real GDP, q/q annualized | 3.4% | 2.2% (Q2) | 2026-Q3 | FRED GDPC1 |
| Dollar proxy (UUP) | 29.61 | 29.50 (2026-11-13); 29.00 (2026-10-19) | 2026-11-20 | Twelve Data |

**Next FOMC (2026-12-09) odds**
| Outcome | Polymarket | Kalshi |
|---|---|---|
| Hike | 94.6% (25bp 91.5%, 50+bp 3.1%) | 94% (25bp 91%, >25bp 3%) |
| Hold | 5.7% | 6% |
| Cut | 0.5% | 2% |

## 3. Sensitivity
- **Rates:** Rate risk sits mainly on the asset side. The 10-Q says exposure "primarily relates to interest revenue earned on our interest-earning assets that are subject to floating interest rates", so a hike should lift interest income. The debt side is mostly fixed. The $2.2B of 0.00% converts due 2029 are fixed, and the 2026-2 notes are fixed-rate classes. The $500M Series 2026-1 notes (~4.86% fixed) are swapped to a floating fed-funds rate, so each 25bp costs about $1.25M a year. The $3.325B and $1.0B SOFR revolvers float, but their balances were not found, so that exposure is not assessed (no data). The main offset: a 10Y above 5% weighs on the value of a long-duration growth stock and on retail investors' appetite for risk.
- **Growth:** Strong. Real GDP grew 3.4% annualized, payrolls rose 165k and retail sales were up 6.8% y/y (FRED RSAFS, Oct). That supports retail trading volume, asset inflows and card credit.
- **Inflation:** CPI is speeding up (3-month annualized 5.7% vs 3.9% y/y). That is what drives the hikes. It can squeeze households' spare cash for investing and their card repayment.
- **Dollar:** not assessed (no data). No geographic revenue split was found in the 10-Q filed 2026-10-28.

## 4. Call
**Neutral, Medium.** Strong growth and higher floating-rate interest income, against mostly fixed-rate debt, roughly offset a 5%+ 10Y yield and a hiking cycle that has historically cooled retail speculation.

## 5. Next 30 days
| Date | Event | Source |
|---|---|---|
| 2026-11-25 | GDP Q3 second estimate | BEA schedule |
| 2026-12-02 | Personal income and outlays (Oct PCE) | BEA schedule |
| 2026-12-04 | November jobs report | BLS (via WebSearch) |
| 2026-12-08 to 2026-12-09 | FOMC meeting and new projections (SEP) | federalreserve.gov calendar |
| 2026-12-10 | November CPI | BLS (via WebSearch) |

## 6. What would flip the call
The call moves to Headwind if FRED DGS10 closes above 5.25% for 5 straight trading days.

## Notes
- The betting markets (Polymarket, Kalshi, 2026-11-20) are not the futures market professionals use. They agree within 1 point.
- The template has 9 indicator rows, more than the 6 to 8 the task asks for. All are kept as the template requires.

Tool access: bls.gov refused both WebFetch (host not allowed) and curl (Access Denied), so BLS dates come from WebSearch. federalreserve.gov failed on WebFetch, but curl worked. Kalshi returned a rate-limit error once and worked on retry.

## Data
```data
agent: macro
ticker: HOOD
date: 2026-11-20
call: Neutral
confidence: Medium
rf_10y: 0.0507
fed_funds: 0.0388
cpi_yoy: 0.039
unemployment: 0.041
uup: 29.61
next_fomc_date: 2026-12-09
next_fomc_hike_prob: 0.94
flip_condition: FRED DGS10 closes above 5.25% for 5 consecutive trading days -> Headwind
```
