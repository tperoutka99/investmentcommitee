# Investment Committee — project notes for Claude

## What this is
A multi-agent "investment committee" that evaluates one stock ticker at a time, modeled on a hedge fund / investment bank. The skill is in `.claude/skills/investment-committee/SKILL.md`. It launches four isolated subagents — Macro strategist, Equity analyst + valuation, Short seller (red team), Portfolio manager — and the main session acts as orchestrator and fact-checker. The equity analyst also loads `.claude/skills/damodaran-dcf/SKILL.md`.

Run it with: "run the committee on <TICKER>" (or `/investment-committee <TICKER>`).

## How Trey wants to work (follow this)
- **Trey is the boss.** He decides every change to the skill. Explain options simply, recommend one, and wait for his call. Make **one change at a time** unless he says "do all of them."
- **Plain language.** He gets overwhelmed by too much at once. Short answers, simple words, tables over walls of text. Be direct, push back when something is wrong.
- **Before each run, ask for Trey's guess** (business good/bad, cheap/expensive, rough value). Never pass it to any agent. After the memo, compare the committee's answer to his guess.
- **Log every skill change** in the SKILL.md change log, bump the version, and mark it "(Trey's call)" when he decided it.
- After a run, say how it performed and list gaps honestly, ranked biggest first.

## Files
- `memos/` — the one-page PM memos, `IC_<TICKER>_<YYYY-MM-DD>.md` (same-day reruns get `_v<version>`).
- `audit/` — every agent report plus the Data flags fact check, `..._reports.md`. This is the audit trail.
- `docs/run-log.md` — every run, verdict, and Trey's guess.
- `docs/backlog.md` — known gaps and ideas not yet approved.
- Prior memos in `memos/` are given to the PM only (never to other agents).

## Data sources (all free)
- **SEC EDGAR data API** (curl with User-Agent `IC research tool research@example.com`): filings, XBRL company facts, ticker→CIK. browse-edgar is blocked; use data.sec.gov.
- **FRED** CSVs for macro and the 10Y risk-free rate.
- **Robinhood MCP** — read-only tools ONLY: `get_equity_quotes`, `get_equity_fundamentals`, `get_equity_analyst_ratings`, `get_earnings_results`. The connector also has trading tools; never call them.
- **Twelve Data MCP** — `get_quote`, `get_time_series` (peer betas, UUP dollar proxy), `get_company_news`.
- **Yahoo Finance analysis page** (WebFetch) for 2-year revenue consensus; StockAnalysis.com as backup.
- **Polymarket + Kalshi** public APIs for Fed rate-hike odds.
- **Damodaran's pages** (pages.stern.nyu.edu/~adamodar) for the implied ERP (home page; implpr.html is stale) and the industry beta table.

## Setup needed in Claude Code
- Connect the **Robinhood** and **Twelve Data** MCP servers (see README).
- Network access to sec.gov, data.sec.gov, fred.stlouisfed.org, finance.yahoo.com, pages.stern.nyu.edu, gamma-api.polymarket.com, api.elections.kalshi.com.

## Hard rules (also in SKILL.md)
- No trading, ever. Research only.
- Every number has a source and date. Gaps are written "not assessed (no data)", never guessed.
- Agents stay isolated and reports are passed verbatim.
