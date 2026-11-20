# Equity: <TICKER>, <YYYY-MM-DD>
**Base value:** $<x> | **Bear / Base / Bull:** $<x> / $<x> / $<x> | **Price:** $<x> (<source>, <date>)

## 1. Business
<Three sentences: how it makes money and what drives it.>

## 2. Quality
| | <FY> | <FY> | <FY> | <FY> | TTM |
|---|---|---|---|---|---|
| Revenue growth | | | | | |
| Gross margin | | | | | |
| Operating margin (GAAP) | | | | | |
| FCF margin | | | | | |
| ROIC (R&D capitalized) | | | | | |
| Net debt / EBITDA | | | | | |
| Diluted share change | | | | | |

Source: <scripts/edgar_facts.py output, filings and dates>. <One line of footnotes, or "No adjustments.">

## 3. Management
- <Point 1, with link>
- <Point 2, with link>
- <Point 3 (optional), with link>

## 4. Pending deals, financing, legal and tax
| Item | Size | Status | Funding / cash still due | In valuation as | Source |
|---|---|---|---|---|---|

<Write "None found." under the table if empty. Legal and tax: list matters above the threshold, or "None above the threshold (<$x>)".>

## 5. Valuation
| Input | Value | Source | As of |
|---|---|---|---|
| Risk-free rate | | FRED DGS10 | |
| Equity risk premium | | Damodaran implied ERP | |
| Bottom-up beta (relevered) | | scripts/peers.py | |
| Industry-table beta (relevered) | | Damodaran, <row> | |
| Initial WACC -> stable | | scripts/dcf.py | |
| Terminal growth / ROC | | | |

**Peer betas:** <TICKER raw/unlevered, ...>. <Beta gap line if > 0.3.>

**Revenue vs consensus ($M)**
| Fiscal year | Mine | Consensus avg | Low | High | Analysts |
|---|---|---|---|---|---|
| <current FY> | | | | | |
| <next FY> | | | | | |

<Reason for any gap over 10%, or "Within 10%.">

**Scenarios** (scripts/dcf.py, <config file>)
| Case | Per share | Industry beta | TV share | Drivers |
|---|---|---|---|---|
| Bear | | | | |
| Base | | | | |
| Bull | | | | |

**Reverse DCF:** <what the price implies for growth and for margin>.
**Growth-invariance test:** <values across terminal g, and with ROC = WACC>.
**Self-audit flags:** <FLAG lines from dcf.py, or "None.">

**Comps** (scripts/peers.py)
| | EV/Sales | EV/EBIT | P/E | P/B | ROE | FCF yield |
|---|---|---|---|---|---|---|

Analysts (Robinhood, <date>): <buy / hold / sell>, mean target $<x>.

## 6. Bull thesis
1. <Reason, tied to a number above>
2. <Reason, tied to a number above>
3. <Reason, tied to a number above>

## 7. Key numbers
| Figure | Value | Source | As of |
|---|---|---|---|
| Price | | | |
| Market cap | | | |
| Shares outstanding | | | |
| Cash (strict) | | | |
| Debt | | | |
| Net debt | | | |
| Enterprise value | | | |
| Next earnings | | Robinhood (<confirmed/estimated>) | |

Tool access: <every assigned tool that failed and what you used instead, or "all assigned tools worked">

## Data
```data
agent: equity
ticker: <TICKER>
date: <YYYY-MM-DD>
price: <number>
market_cap_m: <number>
shares_m: <number>
cash_m: <number>
debt_m: <number>
net_debt_m: <number>
ev_m: <number>
rf: <decimal>
erp: <decimal>
beta_bottom_up: <number>
beta_industry: <number>
wacc_initial: <decimal>
terminal_g: <decimal>
terminal_roc: <decimal>
value_bear: <number>
value_base: <number>
value_bull: <number>
value_base_industry_beta: <number>
tv_share_base: <decimal>
implied_growth: <one line>
implied_margin: <decimal or one line>
rev_cy_mine_m: <number>
rev_cy_consensus_m: <number or "not assessed">
rev_ny_mine_m: <number>
rev_ny_consensus_m: <number or "not assessed">
analyst_mean_target: <number>
next_earnings: <YYYY-MM-DD> (<confirmed|estimated>)
dcf_config: <path to the config you ran>
```
