# Equity: HOOD, 2026-11-20
**Base value:** $28.65 | **Bear / Base / Bull:** $11.87 / $28.65 / $51.53 | **Price:** $64.77 (Robinhood quote, 2026-11-20 16:40 UTC)

## 1. Business
Robinhood earns trading revenue on options, event contracts, equities and crypto ($867M in Q3). It earns net interest ($415M) and subscription fees ($142M) (8-K Ex.99.1, 2026-10-27). Drivers: net deposits, volumes, short rates, crypto.

## 2. Quality
| | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Revenue growth | -25.2% | 37.3% | 58.2% | 51.6% | 20.9% |
| Gross margin | n/m | n/m | n/m | n/m | n/m |
| Operating margin (GAAP) | -74.4% | -28.7% | 35.7% | 46.8% | 45.7% |
| FCF margin | -64.8% | 62.2% | -7.0% | 35.4% | 58.4% |
| ROIC (R&D capitalized) | -11.2% | -4.8% | 9.7% | 17.9% | 14.1% |
| Net debt / EBITDA | n/m | n/m | -3.83x | -1.95x | -1.30x |
| Diluted share change | +78.7% (IPO) | +1.4% | +1.7% | +1.4% | -0.7% |

Source: scripts/edgar_facts.py (EDGAR XBRL), 10-K 2026-02-18, 10-Q 2026-10-28. Broker: no COGS; FCF swings with customer balances; ROIC = EBIT×0.79 / (equity + debt + research asset).

## 3. Management
- Q3 revenue was a record $1.42B (+12%), but EPS fell 16% to $0.51. October net deposits passed $13B (https://investors.robinhood.com; read via 8-K Ex.99.1).
- 2026 opex + SBC guidance was trimmed to $2.675–2.75B; it excludes "pending acquisitions" costs (https://investors.robinhood.com).
- Net interest fell 9% and crypto fell 55%; event contracts grew more than 6x (https://investors.robinhood.com).

## 4. Pending deals, financing, legal and tax
| Item | Size | Status | Funding / cash still due | In valuation as | Source |
|---|---|---|---|---|---|
| 0% convert due 2029 | $2,200M | Closed 2026-06-25 | $290M buyback, $123M capped call (cap $237.85) | Debt; $174.42 conversion price is out of the money, so 0 new shares | 8-K 2026-06-25 |
| Card ABS 2026-1 | $500M | Outstanding | Card receivables | Debt | 10-Q Note 11 |
| RHS revolver | $3,250M | Undrawn | n/a | Excluded: undrawn | 8-K 2026-03-24 |
| "Pending acquisitions" | not assessed (no data) | Unidentified | not assessed (no data) | -$1.11/share per $1B net debt | 8-K Ex.99.1 |

No deal 8-K or 424B since the 10-Q. Legal and tax: none above the threshold ($583M); accruals total $96M (Note 16).

## 5. Valuation
| Input | Value | Source | As of |
|---|---|---|---|
| Risk-free rate | 5.07% | FRED DGS10 | 2026-11-18 |
| Equity risk premium | 4.41% | Damodaran implied ERP | 2026-11-01 |
| Bottom-up beta (relevered) | 1.90 | scripts/peers.py | 2026-11-20 |
| Industry-table beta (relevered) | 0.60 | Damodaran, Brokerage & Investment Banking | Jan 2026 |
| Initial WACC -> stable | Ke 13.45% -> 10.23% | scripts/dcf.py | 2026-11-20 |
| Terminal growth / ROC | 4.5% / ROE 16% | Own; g < rf | 2026-11-20 |

**Peer betas:** SCHW 0.80/0.72, IBKR 1.75/1.75, COIN 2.36/1.95, SOFI 2.28/1.92 (raw/unlevered). The betas differ by 1.30, more than 0.3. Base value: $28.65 (bottom-up beta) vs $40.31 (industry beta).

**Revenue vs consensus ($M)**
| Fiscal year | Mine | Consensus avg | Low | High | Analysts |
|---|---|---|---|---|---|
| FY2026 | 5,299 | 5,320 | 5,210 | 5,450 | 28 |
| FY2027 | 6,359 | 6,880 | 6,510 | 7,750 | 28 |

Within 10% (Yahoo consensus, 2026-11-20). Years 3+: no consensus.

**Scenarios** (scripts/dcf.py, dcf_config.json)
| Case | Per share | Industry beta | TV share | Drivers |
|---|---|---|---|---|
| Bear | $11.87 | $16.32 | 47% | ROE 14%; growth 8%; terminal ROE 10% |
| Base | $28.65 | $40.31 | 62% | ROE 22%; growth 15%; terminal ROE 16% |
| Bull | $51.53 | $73.13 | 69% | ROE 28%; growth 20%; terminal ROE 20% |

**Reverse DCF:** $64.77 needs ROE of 32.8% forever, or book growth at 2.52x the base path.
**Growth-invariance test:** g 2–5%: $25.85–$29.53; with ROE = cost of equity: $19.45.
**Self-audit flags:** None.

**Comps** (scripts/peers.py)
| | EV/Sales | EV/EBIT | P/E | FCF yield |
|---|---|---|---|---|
| HOOD | 10.8x | n/m | 29.3x | 5.2% |
| SCHW | 5.4x | n/m | 14.9x | 7.4% |
| IBKR | 3.7x | n/m | 27.6x | n/m |
| COIN | 4.5x | 125.5x | n/m | 5.0% |
| SOFI | 3.8x | n/m | 22.6x | n/m |

Analysts (Robinhood, 2026-11-19): 29 / 7 / 1, mean target $127.32.

## 6. Bull thesis
1. TTM net deposits of $71B equal 21% growth in platform assets.
2. TTM operating margin is 45.7% and the share count fell 0.7%.
3. $3.1B of net cash; the 0% convert is capped against dilution up to $237.85.

## 7. Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | $64.77 | Robinhood quote | 2026-11-20 |
| Market cap | $58,325M | cover shares × price | 2026-11-20 |
| Shares outstanding | 900.49M | 10-Q cover | 2026-10-28 |
| Cash (strict) | $5,829M (release: $5.8B) | 10-Q; Note 8: $591M equity securities excluded | 2026-09-30 |
| Debt | $2,700M | 10-Q | 2026-09-30 |
| Net debt | -$3,129M | computed | 2026-09-30 |
| Enterprise value | $55,196M | computed | 2026-11-20 |
| Next earnings | 2027-02-09 (pm) | Robinhood (estimated) | 2026-11-20 |

Tool access: investors.robinhood.com failed (curl 403; WebFetch could not resolve the host); I used 8-K Ex.99.1 instead.

## Data
```data
agent: equity
ticker: HOOD
date: 2026-11-20
price: 64.77
market_cap_m: 58325
shares_m: 900.49
cash_m: 5829
debt_m: 2700
net_debt_m: -3129
ev_m: 55196
rf: 0.0507
erp: 0.0441
beta_bottom_up: 1.90
beta_industry: 0.60
wacc_initial: 0.1345
terminal_g: 0.045
terminal_roc: 0.16
value_bear: 11.87
value_base: 28.65
value_bull: 51.53
value_base_industry_beta: 40.31
tv_share_base: 0.624
implied_growth: book-equity growth 2.52x base path (about 38% in years 1-2)
implied_margin: ROE 0.328 forecast and terminal (equity mode)
rev_cy_mine_m: 5299
rev_cy_consensus_m: 5320
rev_ny_mine_m: 6359
rev_ny_consensus_m: 6880
analyst_mean_target: 127.32
next_earnings: 2027-02-09 (estimated)
dcf_config: /home/user/investmentcommitee/runs/HOOD_2026-11-20_v1.6/downloads/equity-analyst/dcf_config.json
```
