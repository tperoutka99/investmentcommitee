---
name: "investment-committee"
description: "Run a ticker through a 4-agent investment committee (macro, equity+valuation, short seller, PM) using isolated subagents with separate data sources; outputs a one-page Markdown IC memo."
---

# Investment Committee

**Version:** v1.4 (2026-11-20)
**Change log:**
- v1.4 (Trey's calls): Two changes. (1) Fixed templates: every report (macro, equity, short seller, data flags, memo) is now written by filling in its file in `templates/`, with the same headings, tables and row labels every run, plus a `data` block of key numbers at the end. `scripts/save_run.py --check` enforces it, and a report that fails goes back to its agent. Before this the layout changed from run to run. (2) Keep the data: `scripts/save_run.py` now does all of Step 5. It also archives each run to `archive/<run>/` (reports, record.json, DCF config and outputs, peer data, price history) and appends a row to `data/runs.csv`. `scripts/track_record.py` scores past calls against SPY in `docs/track-record.md`. The 11 earlier runs were backfilled into `data/runs.csv` from their memo headers; their valuation fields are blank because the old memos had no fixed format.
- v1.3 (Trey's call): Peer price history for the bottom-up beta now comes from Yahoo Finance's chart data, downloaded by `scripts/peers.py` itself, with Twelve Data as the backup for any symbol Yahoo misses. The analyst had been retyping about 500 weekly closes from Twelve Data's tool output, which can't be saved to a file. On the SPCX peers, Yahoo and Twelve Data betas differ by 0.02–0.07 and give the same relevered beta (1.45 vs 1.44).
- v1.2 (Trey's call): The equity analyst now runs three tested scripts instead of writing new code each run: `scripts/edgar_facts.py` (SEC statements, TTM, balance sheet, cover shares, research asset), `scripts/peers.py` (comps and bottom-up beta) and `scripts/dcf.py` (Damodaran DCF, cases, growth-invariance test, reverse DCF, self-audit). `scripts/test_dcf.py` checks the DCF engine against the skill's Amazon, Tata, 3M and Facebook figures (all within 1%). On ADBE and SPCX the analyst took 7–11 minutes, mostly writing these by hand; the DCF math also differed from run to run. It must also batch fetches and write its report once.
- v1.1 (Trey's calls, after the ADBE and SPCX v1.0 runs): Two rules. (1) Every agent now retries a failed WebFetch with curl before falling back to WebSearch or "not assessed" (`reference/agent-rules.md`). On both runs WebFetch failed on federalreserve.gov and Yahoo while curl reached them. (2) The orchestrator's notes in task messages may describe a filing only by quoting its own item text or title from EDGAR, never from memory. On SPCX the note called the 2026-08-14 8-K the xAI deal; it was Cursor.
- v1.0 (Trey's call): The analysts moved into code. Each one is now its own Claude Code agent file in `.claude/agents/` (macro-strategist, equity-analyst, short-seller, portfolio-manager) holding its mandate word for word, and each file's `tools:` list limits that agent to its own data sources, so the different-data rule is enforced by the setup and not just by instructions. Shared how-to sections (FRED, SEC EDGAR, rate-hike odds, agent rules) moved to `reference/`, so each lives in one place. Agents now pass reports as files in a run folder (`runs/<TICKER>_<date>/`) instead of the orchestrator retyping them, which keeps them verbatim and cuts cost. The analysis rules themselves did not change.
- v0.9 (Trey's calls, after the UBER v0.8 run): Five fixes. (1) Beta: the cases now use a bottom-up beta built from the comp peers' own 2-year weekly price moves against SPY (unlevered, median, relevered), and the industry-table beta is shown next to it. On UBER the industry-table beta (Transportation, 0.71) gave a $121 base, but a realistic beta gave about $62, and the PM had to fix it by hand. (2) The equity analyst must now read the legal and tax notes and subtract any large cash still owed; both analysts missed Uber's $1.5B UK VAT bill, which the fact check found only by chance. The short seller's checklist now covers it too. (3) The next earnings date now comes from Robinhood and must appear in the memo's catalysts; UBER's memo said "no date". (4) For an acquisition target that does not file with the SEC, the analyst reads the target's own investor site for its net debt, after Delivery Hero's debt went unknown two runs in a row. (5) The fact check can use about 10 fetches instead of 5, and the PM can no longer build a thesis point on an unchecked fact.
- v0.8 (Trey's calls): Data sources rebuilt around free, official sources. FMP and Alpha Vantage are removed. Price, market cap and sector now come from Robinhood (read-only tools only); the CIK comes from SEC's ticker list; financial statements come from SEC XBRL company facts; analyst ratings, price targets and EPS estimates come from Robinhood; insider trades come from SEC Form 4s; peers are picked from the competitors named in the 10-K, and their numbers come from their own SEC filings instead of a website. Rate-hike odds now come from Polymarket and Kalshi instead of secondhand news. The equity analyst now pulls Wall Street's revenue forecast for this fiscal year and next from Yahoo Finance (StockAnalysis.com as backup) and must show its own year 1 and 2 revenue next to it, explaining any gap over 10%. Step 0 now also checks 8-Ks filed after the latest 10-Q or 10-K for new debt, after the MSFT run missed $25B of new notes.
- v0.7 (Trey's call): The equity analyst can now read SEC filings about new money and deals (8-Ks for agreements, acquisitions, new debt and stock sales, plus stock-sale prospectuses) filed since the latest 10-Q or 10-K. On the last two runs it missed Microsoft's $25B of new notes and AAOI's $550M stock-sale program because those filings were outside its allowed scope. New stock-sale programs must now be shown in the per-share value. Risk factors, insider filings and other 8-K news still belong to the short seller.
- v0.6 (Trey's calls): Two changes. (1) The macro strategist now gets two company facts, pulled by the orchestrator in Step 0 from the latest 10-Q or 10-K: where revenue comes from by region, and how the debt is structured (fixed vs floating). Before this it only knew the industry, so it gave the same Headwind call on every company. It still never sees the full financials or the equity analyst's work. (2) The equity analyst must now follow the damodaran-dcf skill in full, including its input rules: the equity risk premium comes from Damodaran's current implied ERP and beta from his industry-average table, instead of the analyst's own guesses. Those two inputs set the discount rate and had been unsourced on every run.
- v0.5: The equity analyst must now look up what "marketable securities" actually hold in the latest 10-Q or 10-K fair-value note before classifying them, after the SPCX run left $38.6B of Treasuries out of cash and understated net cash by about $39B. If the note can't be found, the analyst reports net cash both ways and marks the classification "not assessed" instead of picking one. The equity analyst now gets the EDGAR instructions, limited to financial-statement notes. Step 3 checks the cash figure against the same note.
- v0.4: The St. Louis Fed's FRED is now the main source for macro data and for the equity analyst's risk-free rate. It is free, official, and has no daily cap. Alpha Vantage (25 calls a day on the free tier) is now kept for the short seller's insider and institutional data, with SEC Form 4 filings as the fallback. The equity analyst must define net cash strictly (cash, equivalents and marketable debt securities only) and check it against the latest earnings release, after the NVDA run overstated net cash by including equity securities.
- v0.3: SEC EDGAR is now read through its data API (submissions JSON plus Archives documents, via curl with a User-Agent header); the browse-edgar page blocks automated fetches. Step 0 records the company's CIK and passes it to the short seller. Dropped Twelve Data get_statistics (needs a pro plan); peers are picked with FMP's peers endpoint, priced with Twelve Data get_quote, and multiples come from the web. Added a "not assessed" rule so agents never fill a data gap with an assumption. Same-day reruns get a version suffix so files are not overwritten.
- v0.2: Rebuilt each agent's data sources around tools that worked on the UBER test run. Dropped Quartr (needs a subscription), FMP SEC filings and peer data (plan tier), and Alpha Vantage COMPANY_OVERVIEW, NEWS_SENTIMENT and INFLATION (premium or stale). Equity analyst now pulls the live 10Y yield itself as the DCF risk-free rate, and must list pending deals and financings. Short seller reads filings straight from SEC EDGAR. Step 3 now verifies material conflicts against primary sources. Added rate-limit rules and a required tool-access line.
- v0.1: Phase 1 build. Four agents: Macro strategist, Equity analyst + valuation, Short seller (red team), Portfolio manager. Different-data split between agents. Markdown memo output.

The user brings a ticker. Four separate subagents research it, argue it, and decide it. You are the **orchestrator**: you launch the agents, pass material between them exactly as specified, verify disputed facts, and save the output. You do not analyze the stock yourself.

## The agents

Each analyst is a Claude Code subagent defined in `.claude/agents/`. Its file holds its full mandate and its allowed tools. **To change how an analyst works, edit its agent file, not this one.**

| Agent (subagent_type) | File | Runs in |
|---|---|---|
| `macro-strategist` | `.claude/agents/macro-strategist.md` | Step 1 (background, parallel) |
| `equity-analyst` | `.claude/agents/equity-analyst.md` | Step 1 (background, parallel) |
| `short-seller` | `.claude/agents/short-seller.md` | Step 2 (foreground) |
| `portfolio-manager` | `.claude/agents/portfolio-manager.md` | Step 4 (foreground) |

Shared how-to files in `reference/`: `sec-edgar.md` (you read it before Step 0 and Step 3; equity analyst and short seller read it too), `fred.md`, `rate-hike-odds.md`, `agent-rules.md`.

If the Agent tool reports that a named subagent type does not exist, stop and tell the user the agent files are not loaded (Claude Code must be opened in this repo's root folder).

## Hard rules

1. **Isolation.** Each agent is a separate subagent launched with the Agent tool by its name, starting from a blank context. Give each agent only what its step below says it receives. Never pass one agent's report to another unless this file says to.
2. **Pass reports verbatim.** Reports move between agents as the files each agent writes in the run folder. Never edit, summarize, or comment on a report file. Do not add your own view anywhere.
3. **Do not pass the user's opinion.** If the user says they like or own the stock, or gives a guess, do not tell any agent. The only exception: a prior IC memo on the same ticker goes to the PM only (see Step 4).
4. **Different data per agent.** Each agent uses only its assigned sources; its agent file's `tools:` list enforces this. If an assigned tool fails, the agent may fall back to WebSearch and must label that figure "(web)".
5. **Every number has a source.** Every figure in every report carries its source and as-of date. The PM may only use numbers that appear in the reports or the Data flags note.
6. **No trading.** No agent and no step may call any order, cancel, exercise, alert, or watchlist-changing tool. This committee produces research only. The user makes every trade decision. The Robinhood connector also holds trading tools: agents may call only these four read-only ones, and only where their agent file names them: `get_equity_quotes`, `get_equity_fundamentals`, `get_equity_analyst_ratings`, `get_earnings_results`.

## Before Step 0: ask for the user's guess

Ask the user for their guess (business good or bad, cheap or expensive, rough value) in one line, and carry on without waiting. Never pass it to any agent. Compare it with the verdict in Step 5.

## Step 0: Resolve the ticker

Load `mcp__Robinhood__get_equity_quotes` and `mcp__Robinhood__get_equity_fundamentals` with ToolSearch. Confirm the company name, current price, market cap, sector, industry and headquarters. Get the CIK from SEC's ticker list (`reference/sec-edgar.md`, step 5). If the ticker is ambiguous or not found, ask the user before launching anything. Record today's date.

**Two company facts for the macro strategist.** From the latest 10-Q or 10-K on EDGAR (read as `reference/sec-edgar.md` describes), pull exactly these two facts and nothing else:

1. **Revenue by region:** the share of revenue from the US and from outside the US (or by named region, if that is how the filing splits it), with the period. Search the filing for "geographic", "United States", "International" and "revenue by".
2. **Debt structure:** total debt, and how much is fixed-rate vs floating-rate (floating = tied to SOFR, EURIBOR, prime or another benchmark), plus any large maturities in the next 2 years. Search for "Debt", "floating", "variable rate", "SOFR", "EURIBOR" and "fixed rate". Then check every 8-K filed after that 10-Q or 10-K whose items include 1.01 or 2.03, and add any new debt it describes, with its date.

Write each as one or two plain lines with the form type and filing date. If a fact can't be found in about 3 fetches, write "not found" for it. Do not add interpretation: these are facts handed over, not a view.

Tell the user in one line that the committee is starting on <TICKER>.

Create the run folder `runs/<TICKER>_<YYYY-MM-DD>/` (if it exists, add `_v<version>`). Below, `<run>` means this folder.

## Step 1: Macro strategist and Equity analyst (in parallel)

Launch both agents in the same turn, in the background, by name. Wait for both to finish before Step 2.

**Task message for `macro-strategist`** (fill in every field; give nothing else):
> Ticker: <TICKER>. Company: <Company>. Sector: <sector>. Industry: <industry>. Country: <country>. Date: <date>.
> Two facts about this company (from its filings):
> - Revenue by region: <fact 1, with source>
> - Debt structure: <fact 2, with source>
> Run folder: <run>. Write your report to <run>/macro.md.

**Task message for `equity-analyst`:**
> Ticker: <TICKER>. Company: <Company>. SEC CIK: <CIK> (10-digit: <CIK padded>). Date: <date>. <any useful note, such as when the fiscal year ends>.

**Rule for notes in any task message:** describe a filing only with what EDGAR itself says: form type, filing date, item numbers, and a quoted phrase from the filing (for example "8-K <date>, items 2.01/3.02: '<a phrase copied from the filing>'"). Never name what a filing is about from memory or inference. If you haven't read it, give only the form, date and items, or leave the note out.
> Run folder: <run>. Write your report to <run>/equity.md.

If an agent returns a report but did not write its file, write the returned text to that file exactly as returned.

**Template check (after every agent, Steps 1, 2 and 4):** run `python3 -I scripts/save_run.py <run> --check <macro|equity|short|memo>`. If it fails, send the agent the error lines with SendMessage and ask it to fix only the format (no new research), then check again. Do not edit an agent's report yourself, and do not move on until it passes.

## Step 2: Short seller (red team)

After both Step 1 agents finish, launch `short-seller` in the foreground (the next step depends on it).

**Task message:**
> Ticker: <TICKER>. Company: <Company>. SEC CIK: <CIK> (10-digit: <CIK padded>). Date: <date>.
> Macro strategist report: <run>/macro.md. Equity analyst report: <run>/equity.md.
> Run folder: <run>. Write your report to <run>/short.md.

## Step 3: Sanity check and verification (orchestrator)

1. **Price check.** Pull a fresh `mcp__Robinhood__get_equity_quotes`. Compare price and market cap against the figures in the reports. Flag any difference over 2%.
2. **List conflicts.** Note every case where two reports give different values or contradictory facts for the same thing. Also list any bear point the short seller ranked in its top 3 that rests only on a web source.
3. **Verify material items.** For each material conflict or web-only top-3 point (an acquisition or divestiture, a financing, debt or cash level, guidance, a management change, a partnership change, or anything a report calls decisive), check a primary source yourself: EDGAR, read as `reference/sec-edgar.md` describes, or the company's own IR press release. Always check the equity analyst's cash figure against the latest earnings release or CFO commentary, and check its classification of marketable securities against the fair-value note in the latest 10-Q or 10-K. Record each as **Verified** (with the filing or release and date), **Contradicted** (with what the source says), or **Not found** (with where you looked). Then, with any fetches left, check other facts either report gives as a reason to own the stock (for example insider buying) that do not come from a filing the analyst quoted. Spend no more than about 10 fetches total. Do not form or state any view on the stock.
4. Write the **Data flags** note to `<run>/data_flags.md` by filling in `templates/data_flags.md` (same headings, tables and rows every run, Data block included): the price check result, the conflicts, then each item with its verification status. Then run `python3 -I scripts/save_run.py <run> --check data_flags`. The PM must address every flag. This is the Phase 1 stand-in for a fact-checker.

## Step 4: Portfolio manager

Launch `portfolio-manager` in the foreground. Find the most recent prior memo on this ticker in `memos/` (or one the user attached or that exists in this conversation; save an attached one to `<run>/prior_memo.md`).

**Task message:**
> Ticker: <TICKER>. Company: <Company>. Date: <date>.
> Macro strategist report: <run>/macro.md. Equity analyst report: <run>/equity.md. Short seller report: <run>/short.md. Data flags note: <run>/data_flags.md.
> Prior memo: <path, or "none exists; omit the What changed section">.
> Write the memo to <run>/memo.md.

## Step 5: Save and deliver

1. Run `python3 -I scripts/save_run.py <run> --version <version> --guess "<the user's guess, or —>"`. It checks all five reports against `templates/` (and saves nothing if one fails), then writes:
   - `memos/IC_<TICKER>_<date>.md` (same-day rerun: `_<version>` added, never overwritten)
   - `audit/IC_<...>_reports.md` (title, skill version, then every report and the data flags, verbatim)
   - `archive/<run>/`: the five reports, `record.json` with every Data block, and the analysts' structured inputs (DCF config and outputs, peers_out.json, price history, facts JSON, FRED CSVs). Raw filings are not kept; they stay on EDGAR.
   - a row in `data/runs.csv` and in `docs/run-log.md`
2. Run `python3 -I scripts/track_record.py` to refresh `docs/track-record.md`.
3. Commit the new and changed files in `memos/`, `audit/`, `archive/`, `data/` and `docs/`.
4. If a file-sending tool (SendUserFile) is available, send the memo, and the reports file as an attachment. In Claude Code, just give both file paths.
5. In chat: the verdict with conviction, the biggest unresolved bear point, and a short comparison with the user's guess. Then, only if any agent's Tool access line reports a failure, add one line naming the failed tools.

## Cost note

One run launches four subagents, so it uses roughly four to five normal conversations' worth of usage. Every data source is now free with no daily cap a normal run should hit. Run the committee on tickers worth the cost.