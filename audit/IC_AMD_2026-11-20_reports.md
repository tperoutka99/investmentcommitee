# IC_AMD_2026-11-20: analyst reports

**Skill version:** v1.8

## Macro strategist
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


## Equity analyst + valuation
# Equity: AMD, 2026-11-20
**Base value:** $371 | **Bear / Base / Bull:** $143 / $371 / $595 | **Price:** $433.41 (Robinhood last trade, 2026-11-20 17:57 UTC)

## 1. Business
AMD designs CPUs, data-center GPUs (Instinct, Helios racks), FPGAs and semi-custom chips, made by TSMC. Data Center ($8.5B of $13.4B Q3'26 revenue, +97% y/y) is the engine, driven by AI capex and gigawatt GPU commitments from OpenAI and Meta (sweetened with 320M-share warrants). Client/Gaming ($3.7B) and Embedded ($1.1B) are cyclical.

## 2. Quality
| | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Revenue growth | 43.6% | -3.9% | 13.7% | 34.3% | 44.3% (YTD y/y) |
| Gross margin | 44.9% | 46.1% | 49.4% | 49.5% | 53.7% |
| Operating margin (GAAP) | 5.4% | 1.8% | 7.4% | 10.7% | 17.7% |
| FCF margin | 13.2% | 4.9% | 9.3% | 19.4% | 15.5% |
| ROIC (R&D capitalized) | 5.8% | 4.4% | 5.5% | 7.7% | 11.5% |
| Net debt / EBITDA | -0.53x | -0.68x | -0.56x | -0.97x | -0.59x |
| Diluted share change | +27.8% | +3.4% | +0.7% | -0.1% | +1.5% |

Source: scripts/edgar_facts.py (EDGAR XBRL); 10-Ks 2025-02-05, 2026-02-04; 10-Q 2026-11-04. ROIC: R&D-adjusted EBIT x 0.79 / capital incl. research asset and goodwill.

## 3. Management
- Q4'26 guide ~$17.0B +/-3% (+66% y/y), non-GAAP GM ~55%; Q3 beat the top of guidance ([IR, 2026-11-03](https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results)).
- Tone: Su is "confident" in "very strong revenue growth and expanding profitability"; Helios running at Anthropic, Meta, Microsoft, OpenAI, OCI (same release).
- Stack M&A: World Labs closed 2026-11-13 ([IR, 2026-11-16](https://ir.amd.com/news-events/press-releases/detail/1306/amd-completes-acquisition-of-world-labs)); Meta Helios still in test ([IR, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)).

## 4. Pending deals, financing, legal and tax
| Item | Size | Status | Funding / cash still due | In valuation as | Source |
|---|---|---|---|---|---|
| Taalas acquisition | ~$2.9B incl. up to ~$1.4B contingent | Pending, close expected Q4'26 | Cash + stock, split undisclosed; target net debt not assessed (no data, private) | $1.5B upfront deducted; contingent excluded (milestone-linked); $1B target net debt = -$0.55/share | 10-Q 2026-11-04 Note 5 |
| World Labs acquisition | ~$8.2B, all stock | Closed 2026-11-13 | 14,978,322 shares issued; target net debt not assessed (no data, private) | +14.98M shares, no asset value added; -$0.55/share per $1B net debt | 8-K 2026-09-28, 8-K/A 2026-11-16 |
| Senior notes (2029/31/33/36) | $4.75B | Closed 2026-08-17 | Held as cash; $875M notes repaid Sep'26 | In debt and cash (Q3 balance sheet) | 8-K 2026-08-17, 424B5 2026-08-13/14 |
| Customer warrants (OpenAI, Meta) | 320M shares at $0.01 | None vested at 2026-09-26 | Vest on GW purchases + price targets | +53M / 160M / 320M shares bear/base/bull | 8-K 2026-02-24, 10-Q Note 14 |
| Equity investment commitments; Oct'26 public stake | $5.1B + $1.0B | Through FY2028 | Cash for stakes | Excluded: value-neutral swap | 10-Q Note 11 |
| Partner guarantees; uncommenced DC leases | $8.5B; $13.3B | Contingent | On partner default | Excluded; discrete risk | 10-Q Note 11 |

No stock-sale program (both 424B5s are the notes). Legal and tax: none above the threshold ($1,578M); largest is $905M unrecognized tax benefits (Note 15).

## 5. Valuation
| Input | Value | Source | As of |
|---|---|---|---|
| Risk-free rate | 5.07% | FRED DGS10 | 2026-11-18 |
| Equity risk premium | 4.41% | Damodaran implied ERP | 2026-11-01 (November 2026) |
| Bottom-up beta (relevered) | 1.84 (unlevered 1.82) | scripts/peers.py | Yahoo chart prices, 2026-11-20 |
| Industry-table beta (relevered) | 1.505 (unlevered 1.49) | Damodaran, Semiconductor | January 2026 |
| Initial WACC -> stable | 13.06% -> 8.95% | scripts/dcf.py | 2026-11-20 |
| Terminal growth / ROC | 4.0% / 15% | own assumption | 2026-11-20 |

**Peer betas** (raw/unlevered, 104 weeks): NVDA 1.83/1.82, INTC 2.10/1.78, AVGO 2.29/2.21, MRVL 2.32/2.23, QCOM 1.70/1.58. Base $371 (bottom-up) vs $403 (industry). Betas differ by 0.33 (>0.3): peer betas are AI-cycle-amplified.

**Revenue vs consensus ($M)**
| Fiscal year | Mine | Consensus avg | Low | High | Analysts |
|---|---|---|---|---|---|
| FY2026 | 52,166 | 52,230 | 50,270 | 56,000 | 45 |
| FY2027 | 88,682 | 95,880 | 80,690 | 120,270 | 50 |

Within 10% (Yahoo consensus, 2026-11-20). Years 3-10: no consensus exists.

**Scenarios** (scripts/dcf.py, dcf_config.json)
| Case | Per share | Industry beta | TV share | Drivers |
|---|---|---|---|---|
| Bear | $143 | $154 | 55.8% | FY27 +45%, margin 28%, ROC 10%, 53M warrant shares |
| Base | $371 | $403 | 64.8% | FY27 +70%, margin 38%, sales/capital 1.8, 160M warrant shares |
| Bull | $595 | $647 | 68.9% | FY27 +85%, margin 45%, ROC 22%, 320M warrant shares |

Base year FY2026E = 9M actual + Q4 guide. No warrant dilution: $407.
**Reverse DCF:** $433.41 needs base growth x1.12 (FY27 +78.5%, 10-yr CAGR 20.7%, year-10 revenue $342B, above NVDA's ~$303B TTM) or a 43.9% target margin.
**Growth-invariance test:** terminal g 2% -> $330, 3% -> $347, 4% -> $371, 5% -> $407; ROC = WACC -> $313.
**Self-audit flags:** FLAG imputed ROC > 40%: base years 4-10 (max 42.6%), bull years 2-10 (max 58.0%).

**Comps** (scripts/peers.py)
| | EV/Sales | EV/EBIT | P/E | P/B | ROE | FCF yield |
|---|---|---|---|---|---|---|
| AMD | 15.5x | 87.2x | 93.3x | 10.4x | 11.1% | 1.0% |
| NVDA | 10.8x | 16.6x | 16.9x | 14.3x | 84.2% | 3.9% |
| INTC | 4.6x | 157.2x | n/m | 2.4x | -10.5% | 1.3% |
| AVGO | 16.8x | 34.9x | 38.2x | 14.7x | 38.4% | 2.7% |
| MRVL | 11.6x | 70.5x | 41.3x | 5.9x | 14.2% | 1.6% |
| QCOM | 4.0x | 19.7x | 12.2x | 5.4x | 44.8% | 5.2% |

Analysts (Robinhood, 2026-11-09): 51 / 7 / 0, mean target $662.39.

## 6. Bull thesis
1. Visible hypergrowth: Q4 guide $17B is a ~$68B run-rate; consensus FY2027 $95.9B matches my bull ($96.5B, $595).
2. Operating leverage: GAAP operating margin 1.8% (FY2023) to 21% (Q3'26), ROIC 4.4% to 11.5%; a 43.9% margin justifies today's price.
3. Fortress balance sheet: $15.8B strict cash vs $9.2B debt incl. leases, A1/A rated, no equity raise needed.

## 7. Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $433.41 | Robinhood quote | 2026-11-20 |
| Market cap | $717,324M (Robinhood $711,270M) | price x shares | 2026-11-20 |
| Shares outstanding | 1,655.07M (cover 1,640.09M + World Labs 14.98M) | 10-Q cover; 8-K/A | 2026-11-16 |
| Cash (strict) | $15,776M (LT investments $1,348M: non-op line) | 10-Q Note 8; = earnings release | 2026-09-26 |
| Debt | $9,211M (notes 7,079 + leases 2,132) | 10-Q Note 9 | 2026-09-26 |
| Net debt | -$6,565M (net cash) | computed | 2026-09-26 |
| Enterprise value | $710,759M | computed | 2026-11-20 |
| Next earnings | 2027-02-02 (pm) | Robinhood (estimated) | 2026-11-20 |

Notes: ST investments are corporate debt $5,931M, US govt $2,325M, other debt $115M (10-Q Note 8). Q4 GAAP EBIT ($4.3B) and R&D ($2.8B) are my estimates.

Tool access: all assigned tools worked.

## Data
```data
agent: equity
ticker: AMD
date: 2026-11-20
price: 433.41
market_cap_m: 717324
shares_m: 1655.07
cash_m: 15776
debt_m: 9211
net_debt_m: -6565
ev_m: 710759
rf: 0.0507
erp: 0.0441
beta_bottom_up: 1.84
beta_industry: 1.505
wacc_initial: 0.1306
terminal_g: 0.04
terminal_roc: 0.15
value_bear: 142.76
value_base: 371.38
value_bull: 595.23
value_base_industry_beta: 403.31
tv_share_base: 0.6479
implied_growth: base growth path x1.12 (FY27 +78.5%, 10-yr revenue CAGR 20.7%)
implied_margin: 0.4392
rev_cy_mine_m: 52166
rev_cy_consensus_m: 52230
rev_ny_mine_m: 88682
rev_ny_consensus_m: 95880
analyst_mean_target: 662.39
next_earnings: 2027-02-02 (estimated)
dcf_config: /home/user/investmentcommitee/runs/AMD_2026-11-20/downloads/equity-analyst/dcf_config.json
```


## Short seller
# Short seller: AMD, 2026-11-20
**Bear case price:** $255 (-41% vs $433.41) | **Thesis strength:** 3/5

## 1. Top 3 bear points
1. **Reported earnings are running well ahead of cash.** Q3 free cash flow was $554M against $2,428M of net income, helped by a one-off $772M tax benefit. Receivables rose 26% q/q and inventory 35%, against revenue up 16%. Payables (+$4.5B) covered the gap (10-Q 2026-11-04, EDGAR).
2. **AMD is helping fund its own demand.** $34B is off the balance sheet: $13.3B of leases to pass to partners, $8.5B of guarantees on partners' leases and debt, $6.2B of backstopped cloud capacity, and $6.1B of equity stakes. Two customers hold $0.01 warrants on 320M shares ($139B, 19% of shares), and $4.5B of warrant value will come out of future revenue (10-Q, EDGAR).
3. **The premium multiple is cracking, and insiders sold into the top.** The stock trades at 94x TTM GAAP EPS of $4.59 (EDGAR). It is 33% below its $649 October high after three sharp November drops (web). Su sold 70,000 shares at $502-526 on Nov 16 (Form 4, EDGAR).

## 2. Weakest assumption
**Target operating margin of 38% (R&D-capitalized; base year 29.7%).** It should be about 30%. GAAP operating margin was 21.2% in Q3. With only this input changed, the analyst's DCF gives $288, not $371.

## 3. Red flag checklist
| Item | Status | Evidence |
|---|---|---|
| Insider net buying/selling (6 months) | Watch | 0 buys, 157 sales ($238.5M), 153 under 10b5-1 plans; Su $148M (EDGAR) |
| Dilution | Watch | +2.4% over 3 years; 320M warrant shares pending (EDGAR) |
| Receivables / inventory vs revenue | Red | y/y +49% / +57% vs revenue +45% (XBRL) |
| Guidance cuts | Clear | Q4 guided to about $17.0B (8-K 2026-11-03) |
| Downgrades | Watch | Target cuts at Mizuho and BofA (web); no rating cuts |
| Negative news trend | Red | Three sharp November drops (web, Twelve Data) |
| New risk factors | Red | Partner guarantees, cloud-capacity backstops, Helios third-party parts |
| Legal / tax cash still due | Clear | No material lawsuits; $905M uncertain-tax liability (10-Q) |
| Institutions (13F) | not assessed (no data) | Scattered aggregator data only (web) |

## 4. Where the macro call is wrong
Headwind is right but too mild. AMD guarantees $8.5B of partners' obligations, so a 5% 10Y raises the cost of partner defaults.

## 5. Bear case price
**$255.** FY2027 revenue of $80B x 24% GAAP operating margin = $19.2B EBIT. After 15% tax and net interest, $16.6B / 1,708M shares (53M warrant shares included) = $9.72 EPS. At 26x, that is $253, plus $3.8 of net cash per share (rounded to $255).

## 6. Thesis strength
**3/5.** The growth is real, but the price needs margins AMD has never reached.

Web sources: trefis.com/stock/amd/articles/623346 ; trefis.com/stock/amd/articles/625220 ; fool.com/investing/2026/11/05/why-amd-stock-is-down-today ; stocktwits.com/news-articles/markets/equity/amd-earnings-checked-every-box-but-wall-street-remains-split-on-the-stock/cNGLXFjR930

Tool access: all assigned tools worked.

## Data
```data
agent: short
ticker: AMD
date: 2026-11-20
bear_price: 255
thesis_strength: 3
bear_point_1: Reported earnings are running well ahead of cash
bear_point_2: AMD is helping fund its own demand
bear_point_3: The premium multiple is cracking, and insiders sold into the top
weakest_assumption: 38% R&D-capitalized target operating margin should be about 30% (gives $288)
red_flags: 3
watch_flags: 3
```


## Data flags
# Data flags: AMD, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $433.41 | $717,325M (1,655.07M shares incl. World Labs issue) | Equity and short reports | 2026-11-20 |
| Fresh quote | $433.73 | $717,855M (1,655.07M shares) | Robinhood | 2026-11-20 18:10 UTC |

**Difference:** +0.1%. No flag (under 2%). The stock is down 11% on the day from the $489.19 close on 2026-11-19.

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | Target operating margin (R&D capitalized) | Equity: 38% (base year 29.7%) | Short: about 30%; the analyst's own config then gives $288 instead of $371 | Judgment. The single largest driver of the base value |
| C2 | Warrant dilution | Equity: 53M / 160M / 320M shares in bear / base / bull; $407 base with none | Short: 320M shares (19%) treated as a real cost, plus $4.5B of warrant value deducted from future revenue | Partly judgment. Terms verified (V3) |
| C3 | Macro call strength | Macro: Headwind, Low | Short: Headwind but too mild, because AMD guarantees $8.5B of partner obligations | Judgment. The guarantees are verified (V4) |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Strict cash $15,776M; short-term investments are debt securities | Verified | 10-Q filed 2026-11-04: cash and equivalents $7,404M + short-term investments $8,372M. Fair-value note: corporate debt $5,931M, US government and agency $2,325M, non-US government $11M, time deposits $86M, plus asset-backed securities |
| V2 | Q3 net income ($2,428M) helped by a one-off $772M tax benefit | Verified | 10-Q tax note: Q3 income tax benefit of $555M (effective rate -29.6%) on pretax income of $1,868M, which "included a discrete tax benefit related to stock-based compensation of $772 million" |
| V3 | Customer warrants for up to 320M shares at $0.01, OpenAI and Meta | Verified | 10-Q: two customers (October 2025 and February 2026), each up to 160 million shares at $0.01, vesting on purchase milestones and stock-price targets; the risk factors name OpenAI OpCo., LLC and Meta Platforms, Inc. "exercisable for up to a combined 320 million shares" |
| V4 | Off-balance-sheet exposure: $8.5B guarantees, $13.3B uncommenced data-center leases for partners, $6.2B cloud-capacity commitments | Verified | 10-Q Note 11: "maximum potential amount of future payments under these guarantees was $ 8.5 billion"; leases "expected to be assigned or subleased to commercial partners ... $ 13.3 billion", starting Q2 FY2027; "commitments for cloud compute capacity arrangements ... were $6.2 billion" |
| V5 | World Labs acquisition ($8.2B, all stock) closed 2026-11-13; Taalas ($2.9B incl. up to $1.4B contingent) pending | Verified | 10-Q (pending-acquisitions note) and 8-K/A filed 2026-11-16, Item 3.02 (closing on November 13, 2026, paid in common stock). The 14.98M share count was not checked |
| V6 | CEO Lisa Su sold shares at about $502–526 on 2026-11-16 | Partly verified | Form 4 filed 2026-11-18: Lisa T. Su, Chair, President & CEO, code S sales on 2026-11-16 at $502.06–$505.21 in the lots read. The 70,000-share total and the $526 top were not summed |
| V7 | 9-month operating cash flow and capex; Q3 FCF $554M | Partly verified | 10-Q: 9M operating cash flow $6,523M, capex $1,845M (9M FCF $4,678M). The Q3-only $554M needs the Q2 10-Q, which was not read |
| V8 | Analyst price-target cuts (Mizuho, BofA) | Not found | Web only; no company filing |
| V9 | Q4 revenue guide of about $17.0B | Not checked | 8-K filed 2026-11-03 not read |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- Target net debt for World Labs and Taalas: not assessed (both private). The equity analyst gives $0.55/share per $1B.
- Taalas cash/stock split not disclosed; the analyst deducted the $1.5B upfront payment as cash.
- bls.gov refused automated requests; BLS dates come from WebSearch.
- 13F holdings: not assessed (no data).
- The equity DCF's self-audit flags imputed ROC above 40% in base years 4–10 (peak 42.6%) and bull years 2–10 (peak 58.0%).
- Next earnings date 2027-02-02 is an estimate (Robinhood).

## Data
```data
agent: data_flags
ticker: AMD
date: 2026-11-20
fresh_price: 433.73
fresh_price_time: 2026-11-20T18:10:41Z
price_diff_pct: 0.001
verified: 5
partly_verified: 2
contradicted: 0
not_found: 1
not_checked: 1
```


