# Macro: ORCL, 2026-11-20
**Call:** Headwind | **Confidence:** Medium

## 1. Regime
US growth is strong (Q3 real GDP 3.4% annualized) while inflation is speeding up again (CPI 3-month annualized 5.7%), and a Fed that held at 3.75-4.00% on Oct 28 (two dissents wanted a hike) is now priced about 91-93% to hike on Dec 9.

## 2. Data
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| 10Y Treasury | 5.07% | 4.98% (2026-11-10) | 2026-11-18 | FRED DGS10 |
| 2Y Treasury | 4.80% | 4.73% (2026-11-10) | 2026-11-18 | FRED DGS2 |
| Effective fed funds | 3.88% | 3.63% (2026-09-16) | 2026-11-18 | FRED DFF |
| CPI y/y | 3.74% (Sep 2026 vs Sep 2025) | 3.40% (Aug 2026) | Sep 2026 | FRED CPIAUCNS |
| CPI 3-month annualized | 5.72% (Jul-Oct) | 4.56% (Jun-Sep) | Oct 2026 | FRED CPIAUCSL |
| Unemployment rate | 4.1% | 4.2% (Sep) | Oct 2026 | FRED UNRATE |
| Payrolls change | +165k | +60k (Sep) | Oct 2026 | FRED PAYEMS |
| Real GDP, q/q annualized | 3.37% (Q3) | 2.22% (Q2) | Q3 2026 | FRED GDPC1 |
| Dollar proxy (UUP) | 29.61 | 28.21 (2026-09-01), +5.0% | 2026-11-20 | Twelve Data |

**Next FOMC (2026-12-09) odds**
| Outcome | Polymarket | Kalshi |
|---|---|---|
| Hike | 93.0% (25bp 90.5%, 50bp+ 2.5%) | 91% (25bp 89%, >25bp 2%) |
| Hold | 6.3% | 7% |
| Cut | 0.5% | 2% |

## 3. Sensitivity
- **Rates:** Most exposed channel. Notes payable and other borrowings total $125.3B ($7,625M current, $117,712M non-current); the fixed/floating split was not found. The November 424B2 priced $10B of fixed notes at 7.000%-8.650% (about 7.77% weighted, roughly $777M a year in interest), so each refinancing now locks in costs near 8%. The $7.6B current portion will roll over at these rates. A 10Y above 5% also lowers what long-dated cash flows are worth today.
- **Growth:** Supportive. The FOMC describes capital investment as "robust", and strong GDP backs enterprise IT and cloud budgets in the Americas (71% of revenue).
- **Inflation:** Negative overall. Faster inflation raises the cost of labor, power and building; it keeps the Fed hiking; and pricing set in contracts adjusts with a lag.
- **Dollar:** Moderate headwind. EMEA 19% ($3,726M) plus Asia Pacific 10% ($1,908M) is 29% of $19,345M quarterly revenue. UUP is up 5.0% since Sep 1, which shrinks the dollar value of those sales. "Americas" includes some non-US revenue, so 29% understates the exposure.

## 4. Call
**Headwind, Medium.** The company carries $125.3B of debt and is now borrowing at 7-8.65%, while the market expects a Fed hike and a 10Y above 5%; together these outweigh the support from strong capex-led growth.

## 5. Next 30 days
| Date | Event | Source |
|---|---|---|
| 2026-11-25 | GDP Q3 second estimate; Personal Income and Outlays, Oct (PCE) | bea.gov |
| 2026-12-04 | Employment Situation, Nov | bls.gov (via WebSearch) |
| 2026-12-09 | FOMC decision + projections (SEP) | federalreserve.gov |
| 2026-12-10 | CPI, Nov | bls.gov (via WebSearch) |
| 2026-12-15 | PPI, Nov | bls.gov (via WebSearch) |

## 6. What would flip the call
The 10Y Treasury (FRED DGS10) closes below 4.50% while the Fed holds on Dec 9; that would move the call to Neutral.

## Notes
- The Oct 2025 CPI value is missing (2025 shutdown), so the Oct 2026 y/y cannot be computed; Sep 2026 is the latest exact y/y.
- These odds come from betting markets, not fed funds futures. Polymarket volume is $45.8M; Kalshi Dec volume is about 18.7M contracts (both read 2026-11-20).
- The 424B5 was not read.

Tool access: Kalshi rate-limited on the first call and worked on retry. WebFetch on federalreserve.gov failed (DNS), so I used curl and it worked. bls.gov curl was denied, so BLS dates come from WebSearch.

## Data
```data
agent: macro
ticker: ORCL
date: 2026-11-20
call: Headwind
confidence: Medium
rf_10y: 0.0507
fed_funds: 0.0388
cpi_yoy: 0.0374
unemployment: 0.041
uup: 29.61
next_fomc_date: 2026-12-09
next_fomc_hike_prob: 0.93
flip_condition: 10Y Treasury (FRED DGS10) closes below 4.50% with a Fed hold on 2026-12-09
```
