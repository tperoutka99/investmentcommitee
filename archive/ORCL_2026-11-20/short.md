# Short seller: ORCL, 2026-11-20
**Bear case price:** $67 (-35% vs $102.45) | **Thesis strength:** 2/5

## 1. Top 3 bear points
1. **Fixed costs against a backlog that is starting to crack.** $288B of 15-19-year data-center leases not yet started, vs $664B RPO, only 13% due within 12 months (EDGAR 10-Q 2026-09-11). A new risk factor warns of "excess data center space... without receiving corresponding revenue" (EDGAR 10-K 2026-06-22). Reportedly 54% is OpenAI; Tencent and Microsoft deals lost (web; no 8-K).
2. **Funding comes from dilution and near-junk debt.** Q1 FCF was -$16.8B before $11.4B of customer prepayments (EDGAR 10-Q). Despite June's "no additional debt in calendar year 2026" (EDGAR 8-K 06-10), on 11-04 it issued $10B of notes at 7.00-8.65% plus $10B of stock (EDGAR 8-K). That used up the "through FY30" $20B cap within days (EDGAR 8-K 10-28). S&P BBB-; CDS about 305bp (web).
3. **Capital is growing about 7x faster than revenue.** PP&E plus leased assets rose $141.9B since FY24; TTM revenue rose $18.8B; Q1 depreciation +134% (EDGAR XBRL).

## 2. Weakest assumption
**Sales-to-capital of 0.5-1.5.** Should be about 0.3: observed 0.13, 0.33 for FY30 $194B counting the leases. At that rate a 12% ROC is unreachable.

## 3. Red flag checklist
| Item | Status | Evidence |
|---|---|---|
| Insider net buying/selling (6 months) | Watch | 14 sales (13 under 10b5-1, $69.0M) vs 1 buy ($3.5M); Ellison's 50M-share plan cancelled unused (EDGAR) |
| Dilution | Red | Shares +13.5% in 3 years; SBC 7.1% of revenue (EDGAR XBRL) |
| Receivables / inventory vs revenue | Watch | FY26 receivables +21.3% vs revenue +17.3%; inventory immaterial (EDGAR XBRL) |
| Guidance cuts | Red | Financing guidance broken; operating guidance kept (EDGAR 8-K) |
| Downgrades | Red | S&P cut to BBB- in July (web); 37/5/1, mean $244.11 (Robinhood) |
| Negative news trend | Red | Contract losses; stock 54% off its June high (web) |
| New risk factors | Red | 10-K adds excess capacity, non-payment, refinancing (EDGAR) |
| Legal / tax cash still due | Watch | $10.1B unrecognized tax benefits; Dutch privacy suit, no accrual (EDGAR) |
| Institutions (13F) | not assessed (no data) | Scattered reports (web) |

Status is exactly one of: Clear / Watch / Red / not assessed (no data).

## 4. Where the macro call is wrong
The flip condition is wrong: Oracle's 7-8.65% coupons reflect its own credit spread (web), so a 10Y below 4.50% does not fix funding.

## 5. Bear case price
**$67.** Non-OCI business: $49.3B revenue × 40% margin × 0.79 after tax × 15x = $234B. OCI: $142B of capital × 0.7 (ROIC below WACC) = $100B. EV $334B - net debt $122.2B = $211.8B, divided by 3,175M shares = $66.7.

## 6. Thesis strength
**2/5.** Needs 15 years of customer payments and faster capital turnover.

Web sources: thenextweb.com/news/oracle-cancels-tencent-ai-chip-lease ; datacenterdynamics.com/en/news/microsoft-winds-down-2023-compute-deal-with-oracle ; ifre.com/topic-codes/2509450 ; fool.com/investing/2026/03/18/oracles-backlog-potential-windfall-or-ticking-time

Tool access: all assigned tools worked

## Data
```data
agent: short
ticker: ORCL
date: 2026-11-20
bear_price: 67
thesis_strength: 2
bear_point_1: Fixed costs against a backlog that is starting to crack
bear_point_2: Funding comes from dilution and near-junk debt
bear_point_3: Capital is growing about 7x faster than revenue
weakest_assumption: Sales-to-capital 0.5-1.5 should be about 0.3
red_flags: 5
watch_flags: 3
```
