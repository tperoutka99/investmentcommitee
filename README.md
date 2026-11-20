# Investment Committee

Four AI analysts research a stock, argue about it, and a portfolio manager makes the call: **BUY, PASS or WATCH**. Built as a Claude Code skill.

| Agent | Job | Sees |
|---|---|---|
| Macro strategist | Is the economy a tailwind or headwind for *this* company? | FRED data, Fed odds, 2 facts about the company |
| Equity analyst | Business quality + DCF valuation (Damodaran method) | SEC filings, Robinhood, Yahoo consensus, peers |
| Short seller | Strongest case *against* owning it | SEC filings, insider trades, news, both reports above |
| Portfolio manager | Makes the decision | All reports + the fact check + the last memo |

The orchestrator (main Claude session) fact-checks disputed claims against primary sources before the PM decides.

## Run it
```
claude
> run the committee on UBER
```
Output: `memos/IC_UBER_<date>.md` (one-page memo) and `audit/IC_UBER_<date>_reports.md` (every report + fact check).

## Setup
1. Install Claude Code and open this folder.
2. Connect the MCP servers the agents use:
   - **Robinhood** (read-only use: quotes, fundamentals, analyst ratings, earnings dates)
   - **Twelve Data** (quotes, weekly price history, company news)
3. Everything else is free and needs no key: SEC EDGAR, FRED, Yahoo Finance, Polymarket, Kalshi, Damodaran's data pages.

## Current version
v0.9 — see the change log at the top of `.claude/skills/investment-committee/SKILL.md`.

Research only. Nothing here is financial advice, and no agent may place trades.
