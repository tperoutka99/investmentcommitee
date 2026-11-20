# Macro: AMD, 2026-11-20
**Call:** Headwind | **Confidence:** Low

## 1. Regime
Strong growth, re-accelerating inflation; the Fed (3.75–4.00%) is priced ~92% to hike December 9.

## 2. Data
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| 10Y Treasury | 5.07% | 4.98% (2026-11-10) | 2026-11-18 | FRED DGS10 |
| 2Y Treasury | 4.80% | 4.73% (2026-11-10) | 2026-11-18 | FRED DGS2 |
| Effective fed funds | 3.88% | 3.88% (2026-10-28) | 2026-11-18 | FRED DFF |
| CPI y/y | 3.74% | 3.40% (Aug) | Sep 2026 | FRED CPIAUCNS |
| CPI 3-month annualized | 5.72% (Jul→Oct) | 4.56% (Jun→Sep) | Oct 2026 | FRED CPIAUCSL |
| Unemployment rate | 4.1% | 4.2% (Sep) | Oct 2026 | FRED UNRATE |
| Payrolls change | +165k | +60k (Sep) | Oct 2026 | FRED PAYEMS |
| Real GDP, q/q annualized | 3.37% (Q3) | 2.22% (Q2) | Q3 2026 | FRED GDPC1 |
| Dollar proxy (UUP) | 29.62 | 29.00 (2026-10-19) | 2026-11-20 | Twelve Data |

**Next FOMC (2026-12-09) odds**
| Outcome | Polymarket | Kalshi |
|---|---|---|
| Hike | 92.8% | 92% |
| Hold | 6.2% | 6% |
| Cut | 0.6% | 2% |

## 3. Sensitivity
- **Rates:** Own interest cost insulated: all $7,125M is fixed-rate notes (2.375%–5.500%), next maturity $625M in 2028, revolver undrawn. Exposure is the valuation multiple.
- **Growth:** Tailwind; 3.4% GDP and "robust" capex (FOMC) support data-center demand.
- **Inflation:** 5.7% 3-month CPI keeps the Fed hiking.
- **Dollar:** International billing 57% of Q3 2026 revenue (64% prior year; 66% nine months); UUP +2.1% in a month is a modest headwind.

## 4. Call
**Headwind, Low.** Hikes and a 5% 10Y outweigh strong capex demand for a high-multiple semiconductor stock.

## 5. Next 30 days
| Date | Event | Source |
|---|---|---|
| 2026-11-25 | GDP Q3 2nd est.; Oct PCE | BEA schedule |
| 2026-12-04 | Nov jobs | BLS (via WebSearch) |
| 2026-12-09 | FOMC decision | Polymarket |
| 2026-12-10 | Nov CPI | BLS (via WebSearch) |
| 2026-12-16 | Nov PPI | BLS (via WebSearch) |

## 6. What would flip the call
10Y (DGS10) below 4.75% five straight sessions.

## Notes
- Oct 2025 CPI blank (shutdown); y/y is Sep/Sep (336.940/324.800); 3-month 337.476/332.813.
- Odds are betting markets, not futures.

Tool access: WebFetch federalreserve.gov failed (used curl); BLS curl refused (used WebSearch).

## Data
```data
agent: macro
ticker: AMD
date: 2026-11-20
call: Headwind
confidence: Low
rf_10y: 0.0507
fed_funds: 0.0388
cpi_yoy: 0.0374
unemployment: 0.041
uup: 29.62
next_fomc_date: 2026-12-09
next_fomc_hike_prob: 0.92
flip_condition: FRED DGS10 closes below 4.75% for five consecutive sessions
```
