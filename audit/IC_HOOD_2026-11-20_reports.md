# IC_HOOD_2026-11-20: analyst reports

**Skill version:** v1.4

## Macro strategist
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


## Equity analyst + valuation
# Equity: HOOD, 2026-11-20
**Base value:** $43.45 | **Bear / Base / Bull:** $19.74 / $43.45 / $73.02 | **Price:** $65.80 (Robinhood quote, 2026-11-20 16:16 UTC)

## 1. Business
Robinhood earns transaction revenue (options, event contracts, equities, crypto; 61% of Q3 2026 revenue), net interest on margin loans, sweep cash and securities lending (29%), and subscription/other revenue (Gold, Trump Accounts; 10%) (EDGAR 10-Q, 2026-10-28). Revenue is driven by customer assets ($396B, +19% y/y) and net deposits ($71.0B TTM), by retail trading activity, and by short-term rates. Crypto revenue is the volatile piece: down 55% y/y in Q3 while event contracts rose sixfold.

## 2. Quality
| | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Revenue growth | -25.2% | 37.3% | 58.2% | 51.6% | 19.1% (9M y/y) |
| Gross margin | n/a | 92.2% | 94.4% | 95.3% | 95.1% |
| Operating margin (GAAP) | -74.4% | -28.7% | 35.7% | 46.8% | 45.7% |
| FCF margin | -66.9% | 62.2% | -7.0% | 35.4% | 58.4% |
| ROIC (R&D capitalized) | -46.2% | -32.5% | 32.7% | 38.2% | 32.9% |
| Net debt / EBITDA | n/m (net cash, EBITDA below 0) | n/m (net cash, EBITDA below 0) | -3.83x (net cash) | -1.95x (net cash) | -1.50x (net cash) |
| Diluted share change | +78.7% | +1.4% | +1.7% | +1.4% | -0.7% |

Source: scripts/edgar_facts.py (EDGAR XBRL), 10-K 2026-02-18, 10-Q 2026-10-28. Footnotes: gross margin = net revenues less brokerage and transaction costs. FCF = OCF less capex and capitalized software, and it swings with customer balances, so it is not used in valuation. ROIC = EBIT x 0.79 over beginning invested capital (equity + debt - strict cash + 687 research asset), so it is flattered by netting all corporate cash.

## 3. Management
- Q3 revenue was a record $1.42B (+12%), but diluted EPS fell 16% to $0.51 on $67M of RVI mark-to-market losses and higher credit provisions. Net interest revenue fell 9% on lower rates and less securities lending (IR release via EDGAR: https://www.sec.gov/Archives/edgar/data/1783879/000178387926000164/q32026robinhoodexhibit991.htm).
- 2026 Adjusted Opex + SBC outlook: top end cut to $2.675-2.75B (was $2.775B), with the CFO transition noted (same link).
- October net deposits topped $13B month-to-date, including $6B from the Dell Trump Accounts contribution. Gold subscribers reached 5.2M (+34%) (same link; newsroom listing https://newsroom.aboutrobinhood.com/).

## 4. Pending deals, financing, legal and tax
| Item | Size | Status | Funding / cash still due | In valuation as | Source |
|---|---|---|---|---|---|
| 0.00% convertible notes due Oct 2029 | $2.2B principal (carrying $2.17B; fair value $2.241B) | Closed 2026-06-25 | $290M used to buy back 2.74M shares; $123M spent on capped calls (strike $174.42, cap $237.85) | Debt $2,200M. Proceeds sit in the $5,829M cash. Conversion is out of the money, so no share add | EDGAR 8-K 2026-06-25; 10-Q Note 11 |
| RHS 364-day secured revolver | $3.25B (up to $4.875B) | Renewed 2026-03-20; $0 drawn at 9/30 | Undrawn | Excluded (undrawn) | EDGAR 8-K 2026-03-24 |
| Credit Card Funding Trust borrowings (incl. $491M ABS) | $839M | Outstanding | Non-recourse, secured by $1.51B of card receivables | Excluded as operating funding; costs $0.93/share if counted as debt | 10-Q Note 11 |
| PT Buana Capital Sekuritas + PT Pedagang Aset Kripto (Indonesia) | Not disclosed | Announced Dec 2025; not mentioned in any 2026 10-Q | not assessed (no data) | Not included; each $1B of target net debt = $1.11/share | 10-K 2026-02-18 |
| $1.5B buyback program | $1.5B ($399M used 9M 2026) | Active | Cash | Not modeled | 8-K 2026-03-24 |

No 8-K with items 1.01/2.01/2.03/3.02 and no 424B prospectus was filed after the 10-Q (EDGAR submissions, checked 2026-11-20). WonderFi ($178M) and MIAXdx closed earlier. Legal and tax: none above the threshold ($583M). Aggregate accrued contingencies are $96M and are subtracted as other claims. The FINRA/NYAG/FDIC probes and the cash-sweep and IPO suits give no amounts. The tax note shows no disputes.

## 5. Valuation
| Input | Value | Source | As of |
|---|---|---|---|
| Risk-free rate | 5.07% | FRED DGS10 | 2026-11-18 |
| Equity risk premium | 4.41% (trailing 12-month, adjusted payout) | Damodaran implied ERP | 2026-11-01 |
| Bottom-up beta (relevered) | 1.89 (unlevered median 1.84) | scripts/peers.py | Yahoo chart prices, 2026-11-20 |
| Industry-table beta (relevered) | 0.60 (unlevered 0.58) | Damodaran, Brokerage & Investment Banking | Jan 2026 |
| Initial WACC -> stable | 13.11% -> 9.78% | scripts/dcf.py | 2026-11-20 |
| Terminal growth / ROC | 4.0% / 15% | Own assumption (g below rf) | 2026-11-20 |

**Peer betas:** SCHW 0.80/0.72, IBKR 1.75/1.75, COIN 2.36/1.96, SOFI 2.28/1.92 (raw/unlevered, 104 weeks). The two betas differ by 1.29 (more than 0.3). The crypto and fintech peers drive the gap; the base case is $43.45 on the bottom-up beta and $58.71 on the industry beta. Peers come from the 10-K's competitor classes (legacy brokers, fintech entrants) plus Coinbase, which it names.

**Revenue vs consensus ($M)**
| Fiscal year | Mine | Consensus avg | Low | High | Analysts |
|---|---|---|---|---|---|
| FY2026 | 5,300 | 5,320 | 5,210 | 5,450 | 28 |
| FY2027 | 6,360 | 6,880 | 6,510 | 7,750 | 28 |

Within 10% (-0.4% / -7.6%) (Yahoo consensus, 2026-11-20). Years 3-10 are my own; no consensus exists for them.

**Scenarios** (scripts/dcf.py, dcf_config.json)
| Case | Per share | Industry beta | TV share | Drivers |
|---|---|---|---|---|
| Bear | $19.74 | $25.65 | 52.8% | 10% growth fading to 3%; margin 32%; sales/capital 0.7; terminal ROC 10% |
| Base | $43.45 | $58.71 | 63.2% | 20% for 2 years fading to 4%; margin 44% to 42%; sales/capital 1.0; ROC 15% |
| Bull | $73.02 | $100.62 | 71.8% | 28% for 2 years fading to 4.5%; margin 48%; sales/capital 0.9; ROC 20% |

**Reverse DCF:** $65.80 requires 1.52x the base growth path (30.4% in year 1, 19.2% 10-year CAGR, $30.6B year-10 revenue) or a 62.4% operating margin.
**Growth-invariance test:** terminal g of 2/3/4/5% gives $39.88/$41.42/$43.45/$46.27; with ROC = WACC it is $38.46.
**Self-audit flags:** None. All cases pass. Not adjusted: I treat the $591M equity securities and RVI stakes as non-cash and leave them out of value, worth $0.66/share if added.

**Comps** (scripts/peers.py does not fit deposit- and customer-cash-funded firms, so P/S and P/E are by hand from SEC XBRL TTM and 2026-11-20 quotes)
| | EV/Sales | EV/EBIT | P/E | FCF yield |
|---|---|---|---|---|
| HOOD | 10.9x (P/S 11.7x) | 24.0x | 30.3x | n/m |
| SCHW | P/S 5.9x | n/m | 15.7x | n/m |
| IBKR | n/m | n/m | 27.9x | n/m |
| COIN | 4.5x (P/S 5.1x) | 127.5x | n/m (loss) | 4.9% |
| SOFI | P/S 3.6x | n/m | 23.7x | n/m |

Analysts (Robinhood, 2026-11-19): 29 buy / 7 hold / 1 sell, mean target $127.32.

## 6. Bull thesis
1. Asset gathering compounds: $71.0B of TTM net deposits is 21% of platform assets, and October alone brought more than $13B.
2. The margin is already elite at 45.7% TTM GAAP, and the opex guide was trimmed. Keeping 48% gives $73.
3. The shares are down 53% from the $139.75 high, and the price is near the bull case. Consensus FY2027 of $6.88B (+29%) sits above my $6.36B.

## 7. Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $65.80 | Robinhood quote | 2026-11-20 |
| Market cap | $59,252M | price x cover shares | 2026-11-20 |
| Shares outstanding | 900.49M (793.43M A + 107.07M B) | 10-Q cover | 2026-10-21 |
| Cash (strict) | $5,829M (matches the $5.8B in the release; no corporate marketable debt securities; segregated Treasuries excluded) | 10-Q balance sheet and fair-value note | 2026-09-30 |
| Debt | $2,200M (convert principal) | 10-Q Note 11 | 2026-09-30 |
| Net debt | -$3,629M | computed | 2026-09-30 |
| Enterprise value | $55,623M | computed | 2026-11-20 |
| Next earnings | 2027-02-09 (pm) | Robinhood (estimated) | 2026-11-20 |

Tool access: investors.robinhood.com failed (WebFetch DNS; curl Access Denied), so I used the 8-K Ex-99.1 and the company newsroom. finance.yahoo.com failed on WebFetch, so I used curl (Yahoo consensus). scripts/peers.py comps do not fit financials, so I did them by hand. Twelve Data was not needed.

## Data
```data
agent: equity
ticker: HOOD
date: 2026-11-20
price: 65.80
market_cap_m: 59252
shares_m: 900.49
cash_m: 5829
debt_m: 2200
net_debt_m: -3629
ev_m: 55623
rf: 0.0507
erp: 0.0441
beta_bottom_up: 1.89
beta_industry: 0.60
wacc_initial: 0.1311
terminal_g: 0.04
terminal_roc: 0.15
value_bear: 19.74
value_base: 43.45
value_bull: 73.02
value_base_industry_beta: 58.71
tv_share_base: 0.632
implied_growth: 1.52x base path (year-1 30.4%, 10-yr CAGR 19.2%)
implied_margin: 0.624
rev_cy_mine_m: 5300
rev_cy_consensus_m: 5320
rev_ny_mine_m: 6360
rev_ny_consensus_m: 6880
analyst_mean_target: 127.32
next_earnings: 2027-02-09 (estimated)
dcf_config: /home/user/investmentcommitee/runs/HOOD_2026-11-20/downloads/equity-analyst/dcf_config.json
```


## Short seller
# Short seller: HOOD, 2026-11-20
**Bear case price:** $38 (-42% vs $65.80) | **Thesis strength:** 2/5

## 1. Top 3 bear points
1. **Without event contracts, revenue was flat, and states are shutting those contracts down.** Q3 revenue was $1,424M including $173M of event contracts (about $29M a year ago), so about $1,251M vs $1,245M without them (EDGAR 8-K/A, 2026-10-28). The Q3 10-Q added appeals-court losses and state exits. It also says RHD has "not collected or remitted federal excise tax" on wagers. At 2% and a $0.50 average price (my assumption), that is about $164M a quarter (EDGAR 10-Q). Louisiana sued on Nov 12 (web only; no 8-K).
2. **Growth is falling fast.** Revenue growth went from +32% in Q2 to +12% in Q3. EPS fell 16% and crypto revenue fell 55% (EDGAR). November crypto app volume fell 51% (web).
3. **Credit risk is growing far faster than revenue.** Receivables from users rose 64% to $23.6B. Card loans rose 77% and provisions rose 173% (EDGAR 10-Q). Adjusted Net Income was reissued a day later over a tax sign error (EDGAR 8-K/A).

## 2. Weakest assumption
**Base case: 20% revenue growth for two years (FY2027 $6.36B).** Use about 6% ($5.6B), since growth without event contracts is about 0%.

## 3. Red flag checklist
| Item | Status | Evidence |
|---|---|---|
| Insider net buying/selling (6 months) | Watch | 112 sales, $200.5M, all 10b5-1. 3 buys, $55.3M, by director Malka (EDGAR) |
| Dilution | Clear | +1.8% over 3 years. SBC 7.3% of revenue (EDGAR) |
| Receivables / inventory vs revenue | Watch | Receivables +64% vs revenue +12%. No inventory (EDGAR) |
| Guidance cuts | Clear | Opex top end trimmed. No revenue guide (EDGAR) |
| Downgrades | Watch | Goldman and Evercore cut targets (web). 29/7/1 ratings (Robinhood) |
| Negative news trend | Red | Louisiana suit, Kalshi adding stocks, crypto slump (web) |
| New risk factors | Red | Event-contract losses, perpetual futures, agentic AI (EDGAR 10-Q) |
| Legal / tax cash still due | Watch | $96M accrued. Excise tax not accrued (EDGAR) |
| Institutions (13F) | not assessed (no data) | Only scattered, stale web reports |

## 4. Where the macro call is wrong
It is a Headwind. Net interest fell 9% anyway, and the new 10-Q text says higher rates pull cash into high-yield accounts and raise delinquencies. 61% of revenue is transactions, which follow risk appetite.

## 5. Bear case price
**$38.** $5.6B FY2027 revenue × 40% margin × (1 - 23% tax) ÷ 911M shares = $1.89 EPS. At 20x (peer average about 22x) that is $37.87.

## 6. Thesis strength
**2/5.** The price already sits above the analyst's own $43.45 base value.

Web sources: https://www.tikr.com/blog/robinhood-has-slumped-for-a-year-why-goldman-sachs-sees-41-upside-after-two-target-cuts ; https://www.tikr.com/blog/evercore-isis-100-target-says-robinhoods-selloff-went-too-far ; https://www.benzinga.com/trading-ideas/movers/26/11/63254460/robinhood-stock-falls-on-48-crypto-volume-drop-goldman-target-cut-bitcoin-slide ; https://theblock.co/news/regulation/2026-11-12-louisiana-sues-kalshi-robinhood-other-prediction-markets-escalating-regulatory-fight-439052 ; https://finviz.com/news/422249/robinhood-markets-inc-reports-october-2026-operating-data

Tool access: all assigned tools worked

## Data
```data
agent: short
ticker: HOOD
date: 2026-11-20
bear_price: 38
thesis_strength: 2
bear_point_1: Ex-event-contracts revenue flat y/y while event contracts face state bans and unaccrued excise tax
bear_point_2: Growth collapsing (Q2 +32% to Q3 +12%, EPS -16%) with weaker Q4 crypto and assets
bear_point_3: Credit and margin risk growing far faster than revenue (receivables +64%, card loans +77%, provisions +173%)
weakest_assumption: Base case 20% revenue growth for 2 years; underlying ex-event-contract growth is about 0%, use about 6%
red_flags: 2
watch_flags: 4
```


## Data flags
# Data flags: HOOD, 2026-11-20

## Price check
| | Price | Market cap | Source | Time |
|---|---|---|---|---|
| Reports | $65.80 | $59.3B (900.49M shares) | Equity and short reports | 2026-11-20 |
| Fresh quote | $65.08 | $58.6B (900.49M shares) | Robinhood | 2026-11-20 16:30 UTC |

**Difference:** -1.1%. No flag (under 2%).

## Conflicts between reports
| # | Item | Report A | Report B | Type |
|---|---|---|---|---|
| C1 | FY2027 revenue growth | Equity: 20% a year for 2 years (FY2027 $6,360M); Yahoo consensus FY2027 $6,880M | Short: about 6% ($5.6B), because revenue excluding event contracts is flat | Judgment. Inputs verified in V1 and V2. Consensus is above both |
| C2 | Macro call | Macro: Neutral (floating-rate interest income offsets a 5%+ 10Y) | Short: Headwind (net interest revenue fell 9% despite higher rates) | Judgment. The 9% fall is verified in V3 |
| C3 | Debt counted in valuation | Equity: $2,200M convertible only; excludes $839M of non-recourse credit-card trust borrowings ($0.93/share if counted) | — | Classification. 10-Q balance sheet long-term borrowings are $2,660M at 2026-09-30, which includes the $500M Series 2026-1 trust notes |
| C4 | Beta | Bottom-up 1.89 (crypto and fintech peers) | Industry table 0.60 (Brokerage & Investment Banking) | Gap 1.29. Base $43.45 vs $58.71. Not a factual conflict but the largest sensitivity in the equity report |

## Verification
| # | Claim | Status | Source |
|---|---|---|---|
| V1 | Q3 revenue $1,424M vs $1,274M (+12%); event contracts $173M vs $27M; so revenue excluding event contracts ≈$1,251M vs ≈$1,247M (flat) | Verified | 10-Q filed 2026-10-28, revenue disaggregation note and MD&A. The short report says $29M a year ago; the 10-Q says $27M. The conclusion (flat) holds |
| V2 | Crypto revenue -55%; diluted EPS -16% ($0.51 vs $0.61); net income -16% | Verified | 10-Q filed 2026-10-28 (MD&A: cryptocurrencies $268M to $120M; "diluted EPS decreased 16% to $0.51") |
| V3 | Net interest revenue fell 9% | Verified | 10-Q filed 2026-10-28: $456M (Q3 2025) to $415M (Q3 2026) |
| V4 | Not collecting or remitting federal excise tax on event contracts | Verified | 10-Q filed 2026-10-28: "We have not collected or remitted federal excise tax on event contracts offered through RHD because we do not believe these contracts are subject to such tax." The short seller's ≈$164M a quarter is its own estimate (assumed 2% rate and $0.50 average contract price, neither in the filing) |
| V5 | Receivables from users $23.6B, +64% | Partly verified | 10-Q balance sheet: $23,598M at 2026-09-30 vs $17,994M at 2025-12-31 (+31% year to date). The year-on-year +64% was not checked against a 2025-09-30 figure. Platform-asset table: receivables from customers (mainly margin) $22.1B vs $13.8B a year earlier (+60%) |
| V6 | Adjusted Net Income was reissued over a tax sign error | Partly verified | 8-K/A filed 2026-10-28, items 2.02/9.01: Exhibit 99.1 is a "Revised press release dated October 27, 2026". The reason for the revision was not located in the 8-K/A text |
| V7 | Louisiana sued Robinhood and other prediction-market operators on 2026-11-12 | Not found | Web only (The Block). No 8-K filed after 2026-10-28; the 10-Q predates the suit |
| V8 | Strict cash $5,829M; no corporate marketable debt securities | Verified | 10-Q cash-flow reconciliation: cash and cash equivalents at period end $5,829M (2026-09-30). The equity analyst reports it matches the $5.8B in the earnings release |
| V9 | $2.2B 0.00% convertible notes due 2029-10-01, conversion ≈$174.42 | Verified | 10-Q Note 11: "$ 2.2 billion aggregate principal amount of 0.00 % convertible senior notes due 2029"; initial conversion rate 5.7332 shares per $1,000 (= $174.42) |
| V10 | Revenue growth was +32% in Q2 2026 | Not checked | — |

Status is exactly one of: Verified / Partly verified / Contradicted / Not found / Not checked.

## Known gaps
- Robinhood's investor site (investors.robinhood.com) was unreachable, so the equity analyst used the 8-K earnings release and the company newsroom.
- bls.gov blocked both fetch methods; the macro strategist took BLS dates from web search.
- Revenue by region was not found, so the dollar exposure is not assessed.
- 13F holdings: not assessed (no data).
- Two Indonesian acquisitions (announced December 2025) have no disclosed size: not assessed. The equity analyst gives $1.11/share per $1B of target net debt.
- The DCF and comps scripts are built for non-financial companies; the equity analyst adapted the DCF and did the comps by hand.
- Next earnings date 2027-02-09 is an estimate (Robinhood).

## Data
```data
agent: data_flags
ticker: HOOD
date: 2026-11-20
fresh_price: 65.08
fresh_price_time: 2026-11-20T16:30:13Z
price_diff_pct: -0.011
verified: 6
partly_verified: 2
contradicted: 0
not_found: 1
not_checked: 1
```


