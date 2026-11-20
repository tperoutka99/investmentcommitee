# Macro: HOOD, 2026-11-20
**Call:** Neutral | **Confidence:** Medium

## 1. Regime
Growth is strong and inflation is accelerating; the Fed hiked in September, held at 3.75-4.00% on Oct 28 (two members dissented for a hike) and is priced for a December hike.

## 2. Data
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| 10Y Treasury | 5.07% | 5.13% (2026-10-21) | 2026-11-18 | FRED DGS10 |
| 2Y Treasury | 4.80% | 4.81% (2026-10-21) | 2026-11-18 | FRED DGS2 |
| Effective fed funds | 3.88% | 3.63% (2026-09-11, before the hike) | 2026-11-18 | FRED DFF |
| CPI y/y | 3.74% (Sep) | 3.40% (Aug) | 2026-09 | FRED CPIAUCNS |
| CPI 3-month annualized | 5.72% (Oct) | 4.56% (Sep) | 2026-10 | FRED CPIAUCSL |
| Unemployment rate | 4.1% | 4.2% (Sep) | 2026-10 | FRED UNRATE |
| Payrolls change | +165k | +60k (Sep) | 2026-10 | FRED PAYEMS |
| Real GDP, q/q annualized | 3.37% (Q3) | 2.22% (Q2) | 2026-Q3 | FRED GDPC1 |
| Dollar proxy (UUP) | 29.60 | 28.92 (2026-10-21) | 2026-11-20 | Twelve Data |

**Next FOMC (2026-12-09) odds**
| Outcome | Polymarket | Kalshi |
|---|---|---|
| Hike | 93.9% (25bp 91.5%, 50bp+ 2.4%) | 95% (25bp 92%, >25bp 3%) |
| Hold | 6.0% | 7% |
| Cut | 0.5% | 2% |

## 3. Sensitivity
- **Rates:** Mixed. The 10-Q says the exposure is mainly "interest revenue earned on our interest-earning assets that are subject to floating interest rates", so a hike lifts income. The $2.2B 0.00% converts (2029) are fixed. The $500M ~4.86% ABS is swapped to floating fed funds (+25bp is about $1.25M a year). The SOFR revolvers ($3.325B, $1.0B) have unknown balances: not assessed (no data). A 10Y above 5% hurts risk appetite and long-duration valuations.
- **Growth:** Supportive. GDP 3.4%, retail sales +6.8% y/y (FRED RSAFS, Oct) and 4.1% unemployment support trading activity and card credit.
- **Inflation:** Negative. 3-month CPI at 5.7% drives the hikes and squeezes the money households can invest.
- **Dollar:** Not assessed (no data); the 10-Q (2026-10-28) has no geographic revenue split.

## 4. Call
**Neutral, Medium.** Strong growth and higher floating-rate income are offset by tightening and a 10Y above 5%, which hit a high-beta retail broker's valuation and its users' risk appetite.

## 5. Next 30 days
| Date | Event | Source |
|---|---|---|
| 2026-11-25 | Q3 GDP (second estimate) and October PCE | BEA schedule |
| 2026-12-04 | November jobs report | BLS via WebSearch |
| 2026-12-08 to 12-09 | FOMC decision | federalreserve.gov |
| 2026-12-10 | November CPI | BLS via WebSearch |
| 2026-12-23 | Q3 GDP (third estimate) and November PCE | BEA schedule |

## 6. What would flip the call
If FRED DGS10 closes above 5.30% for 5 straight sessions, the call becomes Headwind; if it closes below 4.75%, it becomes Tailwind.

## Notes
- October CPI y/y can't be computed: FRED has no October 2025 CPI. The odds are betting markets, not futures (Polymarket $45.7M volume).

Tool access: bls.gov failed (WebFetch DNS, curl Access Denied); I used WebSearch for BLS dates.

## Data
```data
agent: macro
ticker: HOOD
date: 2026-11-20
call: Neutral
confidence: Medium
rf_10y: 0.0507
fed_funds: 0.0388
cpi_yoy: 0.0374
unemployment: 0.041
uup: 29.60
next_fomc_date: 2026-12-09
next_fomc_hike_prob: 0.94
flip_condition: DGS10 above 0.0530 for 5 sessions flips to Headwind; below 0.0475 flips to Tailwind
```
