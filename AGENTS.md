# AGENTS.md

Instructions for any AI coding agent working in this repo (Claude Code, Codex, Cursor and others). Claude Code also reads `CLAUDE.md`, which imports this file.

## What this repo is
A multi-agent **investment committee** that researches one stock ticker and returns a one-page memo with a verdict of **BUY, PASS or WATCH**. It is modeled on a hedge fund investment committee: three analysts research independently, a portfolio manager decides, and the orchestrator fact-checks disputed claims against primary sources in between.

It is research only. No agent may place, cancel or change any trade, alert or watchlist.

## The committee

| Agent | File | Job | Data it may use | Writes |
|---|---|---|---|---|
| **Orchestrator** | `.claude/skills/investment-committee/SKILL.md` | Resolves the ticker, launches the agents, fact-checks, saves output. Never gives its own view. | Robinhood quotes and fundamentals, SEC EDGAR | `data_flags.md`, final files |
| **Macro strategist** | `.claude/agents/macro-strategist.md` | Tailwind / Neutral / Headwind for *this* company | FRED, UUP via Twelve Data, Fed statements, Polymarket + Kalshi, 2 company facts from the orchestrator | `macro.md` |
| **Equity analyst** | `.claude/agents/equity-analyst.md` | Business quality, Damodaran DCF, comps, consensus check | SEC EDGAR (statements, notes, deal 8-Ks), Robinhood (quotes, fundamentals, ratings, earnings), Yahoo consensus, FRED 10Y, company IR, peers' SEC data, Twelve Data peer prices | `equity.md` |
| **Short seller** | `.claude/agents/short-seller.md` | Strongest case against owning it | SEC EDGAR (10-K, 10-Qs, 8-Ks, risk factors, Form 4/144), Twelve Data news, Robinhood ratings, web | `short.md` |
| **Portfolio manager** | `.claude/agents/portfolio-manager.md` | Decides; writes the memo | Only the three reports, the Data flags note and the prior memo | `memo.md` |

Run order: Step 0 resolve ticker → Step 1 macro + equity in parallel → Step 2 short seller (reads both reports) → Step 3 fact check → Step 4 PM → Step 5 save.

Supporting skill: `.claude/skills/damodaran-dcf/SKILL.md` (the equity analyst must follow it, except where its agent file overrides the beta rule).

Shared how-tos in `reference/`: `sec-edgar.md`, `fred.md`, `rate-hike-odds.md`, `agent-rules.md`. Change a how-to there, once, not inside agent files.

## Rules that must not be broken
1. **Isolation:** each agent starts blank and sees only what its step passes it. The macro strategist never sees company financials, and nobody but the PM sees a prior memo.
2. **Different data per agent:** each agent file's `tools:` list is its allowed toolset. Don't widen it without the owner's approval.
3. **Every number has a source and an as-of date.** Data gaps are written "not assessed (no data)", never guessed.
4. **Reports pass verbatim** as files in `runs/<TICKER>_<date>/`. Never retype or summarize them.
5. **Never pass the user's opinion or guess to any agent.**
6. **No trading tools, ever.** Robinhood is read-only: `get_equity_quotes`, `get_equity_fundamentals`, `get_equity_analyst_ratings`, `get_earnings_results`.

## Working with the owner (Trey)
- Trey decides every change to how the committee works. Explain options in plain, simple language, recommend one, and wait for his call. **One change at a time** unless he says otherwise.
- Be direct and push back when something is wrong. Keep answers short; use tables.
- Every change to an agent or the skill: bump the version and add a change-log line at the top of `SKILL.md`, marked "(Trey's call)" when he decided it.
- After a run, report how it performed and list gaps honestly, biggest first. Add unapproved ideas to `docs/backlog.md`.

## Files and folders
| Path | What |
|---|---|
| `memos/` | Final one-page memos, `IC_<TICKER>_<YYYY-MM-DD>.md` (same-day reruns: `_v<version>`) |
| `audit/` | Every report + Data flags per run, `..._reports.md` |
| `runs/` | Scratch folder for live runs (git-ignored) |
| `docs/run-log.md` | One row per run, with Trey's guess |
| `docs/backlog.md` | Known gaps and ideas, not yet approved |
| `scripts/check_setup.sh` | Checks network access to the free data sources |
| `scripts/edgar_facts.py`, `scripts/peers.py`, `scripts/dcf.py` | The equity analyst's tested tools: SEC statements, comps + bottom-up beta, Damodaran DCF. Template: `scripts/dcf_template.json`. Tests: `python3 -I scripts/test_dcf.py` |

## Setup
- MCP servers named exactly **`Robinhood`** and **`Twelve_Data`** (agent `tools:` lines use `mcp__Robinhood__...` and `mcp__Twelve_Data__...`). If yours have other names, update the `tools:` lines.
- Network access to: sec.gov, data.sec.gov, fred.stlouisfed.org, finance.yahoo.com, stockanalysis.com, pages.stern.nyu.edu, gamma-api.polymarket.com, api.elections.kalshi.com. Run `bash scripts/check_setup.sh` to test.
