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
