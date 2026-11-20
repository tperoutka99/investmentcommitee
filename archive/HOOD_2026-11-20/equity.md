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
