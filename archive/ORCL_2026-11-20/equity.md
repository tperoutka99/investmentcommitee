# Equity: ORCL, 2026-11-20
**Base value:** $159.39 | **Bear / Base / Bull:** $47.09 / $159.39 / $314.39 | **Price:** $102.45 (Robinhood quote, 2026-11-20 17:01 UTC)

## 1. Business
Oracle sells database and enterprise applications as cloud subscriptions and license support, and rents compute (now mostly AI GPU capacity) through OCI. Software support ($19.8B FY26) is the cash base; OCI ($18.1B FY26, +121% in Q1 FY27) is the growth engine. Value hinges on converting $664B of RPO profitably without the capex swamping the balance sheet.

## 2. Quality
| | FY2023 | FY2024 | FY2025 | FY2026 | TTM |
|---|---|---|---|---|---|
| Revenue growth | 17.7% | 6.0% | 8.4% | 17.3% | 29.6% (Q1 y/y) |
| Gross margin | n/a | 71.4% | 70.5% | 65.8% | 64.0% |
| Operating margin (GAAP) | 26.2% | 29.0% | 30.8% | 30.6% | 32.1% |
| FCF margin | 17.0% | 22.3% | -0.7% | -35.2% | -40.0% |
| ROIC (R&D capitalized) | 14.2% | 12.5% | 12.3% | 10.2% | 9.1% |
| Net debt / EBITDA | 4.45x | 3.91x | 4.11x | 4.55x | 3.89x (3.60x pro forma Nov) |
| Diluted share change | -0.7% | +2.1% | +1.5% | +1.7% | +3.1% (Q1 y/y) |

Source: scripts/edgar_facts.py (EDGAR XBRL, 10-K 2026-06-22, 10-Q 2026-09-11). Gross margin from the filings' cost lines (excluding amortization); ROIC = R&D-adjusted EBIT × 0.79 / average invested capital incl. leases and research asset; net debt includes leases; FY2023 gross margin not in latest 10-K.

## 3. Management
- Q1 FY27: revenue +30% to $19.3B, OCI +121%, RPO $664B; FY27 guide ≥$90B revenue, non-GAAP EPS $8.10; FCF −$5B ([IR](https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/)).
- Q2 guide: revenue +30–34%, cloud +65–71%, EPS $1.85–1.93; $20B ATM fully sold ([IR](https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/)).
- Investor Day (2026-10-28): FY30 revenue $225B+, non-GAAP margin 40%+, EPS $21+; FCF positive 2H FY28, $30B+ FY29; new raises capped at $20B ($10B equity, $10B debt) ([EDGAR 8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/1341439/000119312526435853/d75538dex991.htm); investor.oracle.com did not resolve).

## 4. Pending deals, financing, legal and tax
| Item | Size | Status | Funding / cash still due | In valuation as | Source |
|---|---|---|---|---|---|
| Common stock, 86.2M sh at ~$116 | $10.0B ($9.88B net) | Closed 2026-11-04 | Funded | +$9,877M cash, +86.2M sh | 8-K 2026-11-04; 424B5 |
| Senior notes 7.00%–8.65%, 2029–2046 | $10.0B | Closed 2026-11-04 | Held as cash | +$9,951M debt and cash | 8-K 2026-11-04; 424B2, FWP |
| $20B ATM | $19.9B net, 141M sh | Fully used Q1 FY27 | None left | In Aug-31 cash/shares | 10-Q |
| Series D mandatory convertible pref | $4,954M | Converts 2029-01-15 | n/a | +31.24M sh (max ratio) | 10-Q; 424B5 |
| Investor Day $20B raise cap | $20B | Appears used by Nov offerings | n/a | Before/after another $10B equity at $102.45: $159.39/$157.70; cases use before | 8-K 2026-10-28 |

No pending acquisitions or divestitures (no 1.01/2.01/2.03/3.02 8-Ks since the 10-Q). Legal and tax: None above the threshold ($3.1B); privacy and securities class actions have no accrual. The $13.2B aggregate gross unrecognized tax benefits (10-K) is booked as expense, multi-jurisdiction, not subtracted (−$4.16/share if it were).

## 5. Valuation
| Input | Value | Source | As of |
|---|---|---|---|
| Risk-free rate | 5.07% | FRED DGS10 | 2026-11-18 |
| Equity risk premium | 4.41% | Damodaran implied ERP | 2026-11-01 |
| Bottom-up beta (relevered) | 1.56 (unlevered 1.08) | scripts/peers.py | Yahoo chart prices, 2026-11-20 |
| Industry-table beta (relevered) | 1.78 (unlevered 1.23) | Damodaran, Software (System & Application) | Jan 2026 |
| Initial WACC -> stable | 9.87% -> 8.65% | scripts/dcf.py | 2026-11-20 |
| Terminal growth / ROC | 4.0% / 12% | own (g < rf) | 2026-11-20 |

**Peer betas:** MSFT 1.09/1.08, AMZN 1.41/1.34, GOOGL 1.28/1.24, CRM 1.18/0.99, IBM 0.88/0.66 (raw/unlevered). D/E includes leases. Base: $159.39 bottom-up, $151.64 industry; gap 0.22.

**Revenue vs consensus ($M)**
| Fiscal year | Mine | Consensus avg | Low | High | Analysts |
|---|---|---|---|---|---|
| FY2027 (May-27) | 90,258 | 90,460 | 89,100 | 91,690 | 38 |
| FY2028 (May-28) | 126,362 | 131,820 | 122,210 | 139,640 | 38 |

Within 10% (Yahoo consensus, 2026-11-20). Years 3+ are my own (no consensus); my FY30 $194B vs guide $225B+.

**Scenarios** (scripts/dcf.py, dcf_config.json)
| Case | Per share | Industry beta | TV share | Drivers |
|---|---|---|---|---|
| Bear | $47.09 | $43.55 | 79.0% | FY30 $150B; margin 27%; ROC 9% |
| Base | $159.39 | $151.64 | 78.6% | FY30 $194B; margin 34%; sales/capital 0.5–1.5; ROC 12% |
| Bull | $314.39 | $301.02 | 77.5% | FY30 $228B (guide); margin 40%; ROC 15% |

**Reverse DCF:** $102.45 implies 0.69x base growth (year 1 23.6%, 10-yr CAGR 11.5%), or a 26.4% target margin vs 35.0% adjusted FY26.
**Growth-invariance test:** terminal g 2% → $137.19, 3% → $146.48, 4% → $159.39, 5% → $178.90; with ROC = WACC → $129.27.
**Self-audit flags:** None (all PASS; max imputed ROC 17.1%). Q1's −$5.4B FCF is double-counted (FY26 base, Aug-31 cash): −$1.70/share, conservative.

**Comps** (scripts/peers.py)
| | EV/Sales | EV/EBIT | P/E | P/B | ROE | FCF yield |
|---|---|---|---|---|---|---|
| ORCL (pro forma, ex-leases) | 5.5x | 17.2x | 16.8x | 4.2x | 28.3% | -9.0% |
| MSFT | 10.4x | 22.0x | 25.4x | 7.7x | 30.3% | 1.7% |
| AMZN | 3.5x | 26.8x | 20.2x | 4.4x | 22.0% | -1.7% |
| GOOGL | 6.9x | 20.7x | 14.4x | 5.0x | 34.8% | 0.6% |
| CRM | 4.1x | 20.5x | 15.7x | 3.9x | 25.2% | 10.0% |
| IBM | 4.0x | n/m | 19.4x | 6.1x | 31.4% | 6.8% |

ORCL row by hand (script missed its debt); with leases 6.1x / 19.1x. SAP dropped (stale XBRL).

Analysts (Robinhood, 2026-11-07): 37 / 5 / 1, mean target $244.11.

## 6. Bull thesis
1. RPO $664B is 9.2x TTM revenue; base needs only $194B FY30 vs the $225B guide.
2. Price implies 11.5% CAGR or a 26.4% margin vs 30% growth and 35% margin today; industry-beta value still $151.64.
3. Funding done: $56.9B pro forma cash, $20B raise cap used, FY29 FCF guide $30B+ vs −$28.7B TTM.

## 7. Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $102.45 | Robinhood get_equity_quotes | 2026-11-20 |
| Market cap | $318,614M pro forma (Robinhood $309,843M pre-offering) | computed; Robinhood | 2026-11-20 |
| Shares outstanding | 3,109.95M (cover 3,023.74M + 86.21M); 3,175.19M in DCF (+pref, +34M plans) | 10-Q cover; 8-K | 2026-11-04 |
| Cash (strict) | $37,077M (cash $36,369M + debt securities $708M; money-market and time deposits); $56,905M pro forma; matches Q1 release | 10-Q fair-value note | 2026-08-31 |
| Debt | $179,094M ($135,288M borrowings + $43,806M leases) | 10-Q; 424B2 | 2026-11-04 |
| Net debt | $122,189M | computed | 2026-11-04 |
| Enterprise value | $441,227M (incl. leases, minority) | computed | 2026-11-20 |
| Next earnings | 2026-12-14 (after close) | Robinhood (confirmed) | 2026-11-20 |

Tool access: investor.oracle.com unresolvable (WebFetch and curl); used oracle.com/news and the EDGAR 8-K exhibit instead. All other assigned tools worked.

## Data
```data
agent: equity
ticker: ORCL
date: 2026-11-20
price: 102.45
market_cap_m: 318614
shares_m: 3109.95
cash_m: 56905
debt_m: 179094
net_debt_m: 122189
ev_m: 441227
rf: 0.0507
erp: 0.0441
beta_bottom_up: 1.56
beta_industry: 1.78
wacc_initial: 0.0987
terminal_g: 0.04
terminal_roc: 0.12
value_bear: 47.09
value_base: 159.39
value_bull: 314.39
value_base_industry_beta: 151.64
tv_share_base: 0.7857
implied_growth: 0.69x base path; year-1 23.6%, 10-yr revenue CAGR 11.5%
implied_margin: 0.264
rev_cy_mine_m: 90258
rev_cy_consensus_m: 90460
rev_ny_mine_m: 126362
rev_ny_consensus_m: 131820
analyst_mean_target: 244.11
next_earnings: 2026-12-14 (confirmed)
dcf_config: /home/user/investmentcommitee/runs/ORCL_2026-11-20/downloads/equity-analyst/dcf_config.json
```
