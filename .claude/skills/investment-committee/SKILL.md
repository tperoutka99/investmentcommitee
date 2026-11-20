---
name: "investment-committee"
description: "Run a ticker through a 4-agent investment committee (macro, equity+valuation, short seller, PM) using isolated subagents with separate data sources; outputs a one-page Markdown IC memo."
---

# Investment Committee (Phase 1)

**Version:** v0.9 (2026-11-20)
**Change log:**
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

## Hard rules

1. **Isolation.** Each agent is a separate subagent launched with the Agent tool, starting from a blank context. Give each agent only what its section below says it receives. Never pass one agent's report to another unless this file says to.
2. **Pass reports verbatim.** Do not summarize, soften, or comment on a report when handing it to the next agent. Do not add your own view anywhere.
3. **Do not pass the user's opinion.** If the user says they like or own the stock, do not tell any agent. The only exception: a prior IC memo on the same ticker goes to the PM only (see Step 4).
4. **Different data per agent.** Each agent uses only its assigned sources. This is what makes their views independent. If an assigned tool fails, the agent may fall back to WebSearch and must label that figure "(web)".
5. **Every number has a source.** Every figure in every report carries its source and as-of date. The PM may only use numbers that appear in the reports or the Data flags note.
6. **No trading.** No agent and no step may call any order, cancel, exercise, alert, or watchlist-changing tool. This committee produces research only. The user makes every trade decision. The Robinhood connector also holds trading tools: agents may call only these four read-only ones, and only where this file names them: `get_equity_quotes`, `get_equity_fundamentals`, `get_equity_analyst_ratings`, `get_earnings_results`.

## How to read FRED

FRED (the St. Louis Fed's economic database) serves any series as a CSV with no key and no daily cap:

`curl -sS "https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>"` (if curl is refused, use WebFetch on the same URL).

Parse it in Python. Label figures "(FRED <SERIES>)" with the observation date. Useful series: `DGS10` and `DGS2` (10Y and 2Y Treasury, daily), `DFF` (effective fed funds, daily), `CPIAUCNS` (CPI, not seasonally adjusted, for year-over-year), `CPIAUCSL` (CPI, seasonally adjusted, for 3-month annualized), `UNRATE` (unemployment), `PAYEMS` (payrolls; take the monthly change), `GDPC1` (real GDP; annualize the quarterly change), `RSAFS` (retail sales).

## How to read SEC EDGAR

The browse-edgar page (`sec.gov/cgi-bin/browse-edgar`) blocks automated fetches. Use EDGAR's data API instead, with curl from Bash. SEC requires a User-Agent header on every request:

1. **Filing list:** `curl -sS -A "IC research tool research@example.com" https://data.sec.gov/submissions/CIK<10-digit CIK>.json`. Parse `filings.recent` in Python (`form`, `filingDate`, `accessionNumber`, `primaryDocument`, `items`).
2. **A filing:** `curl -sS -A "IC research tool research@example.com" https://www.sec.gov/Archives/edgar/data/<CIK without leading zeros>/<accession number without dashes>/<primaryDocument>`. For an exhibit (an earnings release or CFO commentary attached to an 8-K), list the filing's documents first with `.../<accession number without dashes>/index.json`. Strip the HTML in Python and search for the terms you need.
3. Save downloads in their own new directory, and run Python on them with `python3 -I`.
4. Label facts from these files "(EDGAR)" with the form type and filing date.
5. **Ticker to CIK:** `curl -sS -A "IC research tool research@example.com" https://www.sec.gov/files/company_tickers.json` and match the ticker. Pad the CIK to 10 digits for the data API.
6. **Financial statement data:** `curl -sS -A "IC research tool research@example.com" https://data.sec.gov/api/xbrl/companyfacts/CIK<10-digit CIK>.json` returns every figure the company has reported (revenue, operating income, cash, debt, shares and more) by period. It works for any SEC filer, so use it for peers too.
7. SEC allows up to 10 requests a second. Space calls out and retry once if refused.

## How to read rate-hike odds

Use two prediction markets. Both are free and need no key. Report both.

1. **Polymarket:** find the open "Fed decision in <month>" event for the next FOMC meeting (WebSearch "Polymarket Fed decision <month> <year>"), then read it with WebFetch on the polymarket.com event page, or with curl on `https://gamma-api.polymarket.com/events?slug=<event slug>`. Record each outcome's probability and the total volume.
2. **Kalshi:** `curl -sS "https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION&status=open"` lists the open Fed decision markets. Pick the one for the next meeting and record each outcome's probability (last price) and volume.

Label each "(Polymarket)" or "(Kalshi)" with the date. If the two differ by more than 10 points on the most likely outcome, show both and say so. These are betting markets, not the futures market professionals use; say that once in the report.

## Rules for every agent prompt

Include these lines at the end of every agent's prompt:

> **Tool rules:** Load tools with ToolSearch before calling them. If a tool returns a rate-limit error, wait about 15 seconds and retry once; if it fails again, use your fallback. Do not call any order, cancel, exercise, alert, or watchlist-changing tool. From Robinhood, use only the read-only tools your data list names.
>
> **No assumptions as facts:** if your assigned data does not cover something your report asks for, write "not assessed (no data)" rather than filling it in from memory or assumption.
>
> **End your report with one line:** "Tool access:" followed by every assigned tool that failed and what you used instead, or "all assigned tools worked".

## Step 0: Resolve the ticker

Load `mcp__Robinhood__get_equity_quotes` and `mcp__Robinhood__get_equity_fundamentals` with ToolSearch. Confirm the company name, current price, market cap, sector, industry and headquarters. Get the CIK from SEC's ticker list ("How to read SEC EDGAR", step 5). If the ticker is ambiguous or not found, ask the user before launching anything. Record today's date.

**Two company facts for the macro strategist.** From the latest 10-Q or 10-K on EDGAR (read as "How to read SEC EDGAR" describes), pull exactly these two facts and nothing else:

1. **Revenue by region:** the share of revenue from the US and from outside the US (or by named region, if that is how the filing splits it), with the period. Search the filing for "geographic", "United States", "International" and "revenue by".
2. **Debt structure:** total debt, and how much is fixed-rate vs floating-rate (floating = tied to SOFR, EURIBOR, prime or another benchmark), plus any large maturities in the next 2 years. Search for "Debt", "floating", "variable rate", "SOFR", "EURIBOR" and "fixed rate". Then check every 8-K filed after that 10-Q or 10-K whose items include 1.01 or 2.03, and add any new debt it describes, with its date.

Write each as one or two plain lines with the form type and filing date. If a fact can't be found in about 3 fetches, write "not found" for it. Do not add interpretation: these are facts handed over, not a view.

Tell the user in one line that the committee is starting on <TICKER>.

## Step 1: Macro strategist and Equity analyst (in parallel)

Launch both agents in the same turn, in the background. Each receives only: ticker, company name, today's date, and its mandate below (copy the mandate in full into the agent prompt, followed by the "How to read FRED" section and the Rules for every agent prompt). The macro strategist also receives the sector, industry, and country from Step 0, the two company facts (revenue by region and debt structure) labeled with their sources, and the "How to read rate-hike odds" section, copied in full. The equity analyst also receives the company's CIK from Step 0 and the "How to read SEC EDGAR" section, copied in full. Wait for both to finish before Step 2.

### Mandate: Macro strategist

> You are the macro strategist on an investment committee evaluating <TICKER> (<Company>; sector: <sector>; industry: <industry>; country: <country>) as of <date>. You work alone. You will not see any other analyst's work.
>
> **Two facts about this company (from its filings):**
> - Revenue by region: <fact 1, with source>
> - Debt structure: <fact 2, with source>
>
> Use these to make your view specific to this company, not just its industry. Ask: does this company sell where the economy is strong or weak? Would a stronger dollar shrink its overseas sales? Would rising rates raise its own interest costs?
>
> **Your data (use only these):** FRED, read as the "How to read FRED" section below describes, for rates, inflation, labor, growth and retail sales. Compute CPI year-over-year and other changes yourself in Python. For the dollar, use `mcp__Twelve_Data__get_time_series` on the UUP ETF (Twelve Data does not cover indices). Use WebFetch or WebSearch for the latest FOMC statement and the economic release calendar, preferring official pages (federalreserve.gov, bls.gov, bea.gov, census.gov). For the odds of the next Fed decision, use the prediction markets as the "How to read rate-hike odds" section below describes. Do not look at the company's financial statements, earnings calls, price targets, or news.
>
> **Your job:** Decide whether the current macro environment is a tailwind, headwind, or neutral for this specific business, and how sensitive the business is to rates, growth, inflation, and the dollar.
>
> **Return exactly this, under 400 words:**
> 1. **Regime:** one sentence on where the economy and the Fed are.
> 2. **Data table:** 6 to 8 indicators, each with latest value, prior value, as-of date, and source. Include the dollar proxy.
> 3. **Sensitivity:** how this sector/business model responds to rates, growth, inflation, and the dollar. Be specific to the business, not generic. Tie the dollar point to the revenue-by-region fact and the rates point to the debt-structure fact, quoting the numbers you were given. If either fact says "not found", mark that part "not assessed (no data)" rather than guessing. You have no other company data, so do not judge anything else about the company.
> 4. **Call:** Tailwind / Neutral / Headwind, with confidence (High / Medium / Low) and the one-sentence reason.
> 5. **Next 30 days:** the macro events (with dates) most likely to move this stock.
> 6. **What would flip your call:** one measurable condition.

### Mandate: Equity analyst + valuation

> You are the equity analyst on an investment committee evaluating <TICKER> (<Company>) as of <date>. You work alone. You will not see any other analyst's work.
>
> **Your data (use only these):**
> - **Financial statements:** SEC EDGAR, as the "How to read SEC EDGAR" section below describes: XBRL company facts plus the latest 10-K and 10-Q.
> - **Price, market cap and shares:** `mcp__Robinhood__get_equity_quotes` and `mcp__Robinhood__get_equity_fundamentals`.
> - **Analyst ratings and EPS:** `mcp__Robinhood__get_equity_analyst_ratings` (buy/hold/sell counts and price targets) and `mcp__Robinhood__get_earnings_results` (EPS estimates and the next report date). Label these "(Robinhood)".
> - **Revenue consensus:** WebFetch `https://finance.yahoo.com/quote/<TICKER>/analysis/` and read the Revenue Estimate table's "Current Year" and "Next Year" columns: fiscal year, average, low, high, and number of analysts. Ignore its quarter columns; their labels lag after earnings. Label "(Yahoo consensus)" with today's date. If Yahoo fails, use `https://stockanalysis.com/stocks/<ticker>/forecast/` and label "(StockAnalysis)" with its data date. If both fail, mark it "not assessed (no data)".
> - **Risk-free rate:** FRED series `DGS10` only, read as the "How to read FRED" section below describes.
> - **Management commentary and press releases:** WebFetch on the company's own investor relations site (label these "(IR)"); if the news page renders with JavaScript, use its RSS feed or individual press-release pages.
> - **Peer comps:** pick 3 to 5 peers from the competitors the company names in its latest 10-K (search the filing for "Competition"). Get their prices from `mcp__Robinhood__get_equity_quotes` or `mcp__Twelve_Data__get_quote`, and compute their multiples from their own SEC XBRL company facts. Use WebSearch only for a peer that does not file with the SEC, labeled "(web)" with the data date.
> - **Peer price history (for beta only):** `mcp__Twelve_Data__get_time_series` for 2 years of weekly closes on each comp peer and on SPY.
>
> Do not use insider trading data, institutional holdings, news sentiment, or SEC risk-factor sections; those belong to another agent.
>
> **Check your revenue path against consensus:** in your base case, put your revenue for the current and next fiscal year next to the consensus average. If yours differs from consensus by more than 10% in either year, give the reason in one line, tied to a number (guidance, backlog, a filing). Years 3 onward are your own; no consensus exists for them, so say so.
>
> **Your job:** Understand the business, judge its quality, and value it.
>
> **Required checks:**
> - **Risk-free rate:** use the latest 10Y yield from FRED DGS10 as the risk-free rate in your DCF, and state its value and date. Do not use a remembered or default rate.
> - **Pending deals and new financing:** list every announced acquisition, divestiture, or major financing from the last 12 months that has not closed, plus any financing completed since the latest 10-Q or 10-K, with size and how it is funded. Check two places:
>   1. The company's IR press releases.
>   2. EDGAR: every 8-K filed since the latest 10-Q or 10-K whose items include 1.01 (material agreement), 2.01 (acquisition or disposal), 2.03 (new debt) or 3.02 (unregistered stock sale), and every prospectus filed in the same window (forms 424B2, 424B3, 424B5). Read the item text, not just the item number.
>
>   Build each one into the valuation:
>   - **New debt:** add it to debt. If the proceeds are raised and held as cash, add them to cash too, and say so.
>   - **A stock-sale program** (an at-the-market or other offering): show value per share twice, before and after the full program is sold at today's price, and say which one your bear / base / bull cases use.
>   - **A pending acquisition of a company that does not file with the SEC:** get the target's latest debt and cash from its own investor relations site (its latest annual or quarterly report), labeled "(target IR)" with the period, and add its net debt to the pro forma figures. If you can't find it, mark it "not assessed (no data)" and state how much value per share each $1B of target net debt costs.
>   - **Anything you leave out:** say why, in one line.
>
>   Never mark a financing "not assessed" just because it sits in an 8-K or prospectus. Those filings are now in scope.
> - **Net cash, strictly defined:** count only cash, cash equivalents, and marketable debt securities. Equity securities (public or private stakes) and other investments are never cash; if you include them in value, show them as a separate line.
>   - **Look up what "marketable securities" hold before classifying them.** Read the fair-value or investments note in the latest 10-Q or 10-K (via EDGAR, as the "How to read SEC EDGAR" section below describes; search the filing for "fair value", "Level", "government securities", "corporate debt" and "equity securities"). Government, agency, corporate debt and money-market holdings count as cash. Equity holdings do not. Quote the note's breakdown with its filing and date.
>   - **If you cannot find the breakdown,** do not guess and do not default to excluding them. Report net cash both ways (with and without marketable securities), mark the classification "not assessed (no data)", and say which figure your valuation uses.
>   - Check your cash figure against the number in the company's latest earnings release or CFO commentary, and report both if they differ.
>   - From EDGAR, use only the financial statements and their notes, plus the 8-Ks and prospectuses named in the pending-deals check above. Risk factors, Form 4s and Form 144s, and all other 8-K news belong to another agent.
> - **Legal and tax disputes:** read the commitments-and-contingencies note and the income-tax note in the latest 10-Q or 10-K (search for "Contingencies", "assessment", "accrued", "settlement", "tax authority" and "appeal"). List every single matter where the amount accrued, assessed, paid, or still to be paid is at least 1% of market cap or 10% of strict cash, whichever is smaller. For each, give the amount, how much has been paid, how much is still due, and whether the company books it as an expense or as a receivable. Subtract any cash still due from equity value, and say so: a dispute the company expects to win still costs cash now. If there are none, write "none above the threshold".
>
> **Valuation method:** Load the `damodaran-dcf` skill with the Skill tool and follow it in full, including its rules for where inputs come from. This is required, not optional. Two inputs in particular:
> - **Equity risk premium:** use Damodaran's current implied equity risk premium from his data pages (pages.stern.nyu.edu/~adamodar), with the month it is for. Never a remembered, historical or default figure.
> - **Beta (this overrides the damodaran-dcf skill's beta rule):** compute two betas, and use the bottom-up one in your bear / base / bull cases.
>   - **Bottom-up beta (used in the cases):** for each comp peer, regress 2 years of weekly returns against SPY's weekly returns (Twelve Data closes) to get its beta. Unlever each with that peer's own debt-to-equity and tax rate, take the median, then relever it to this company's debt-to-equity as the skill shows. Show each peer's beta. If fewer than 3 peers have 2 years of prices, use the industry-table beta in the cases instead and say so.
>   - **Industry-table beta (shown for comparison):** the industry-average unlevered beta from Damodaran's betas-by-industry table, relevered the same way. Name the industry row you used.
>   - Show the base value under both betas. If the two betas differ by more than 0.3, say so in one line.
>   - Never use this company's own price history for beta, and never a guess.
> - You may WebFetch those Damodaran pages for these two inputs only.
> - **If you can't reach them,** do not swap in a guess. Mark the input "not assessed (no data)", show how the base value changes across a range (equity risk premium 4% to 6%; beta 0.8 to 1.6), label that range "unsourced", and say which figure your bear / base / bull cases use.
>
> Run all math in Python (Bash), not in your head. Produce: (a) a reverse DCF showing what revenue growth and margin the current price implies, (b) bear / base / bull fair values with the two or three assumptions that drive each, (c) a comps table against 3 to 5 peers (EV/Sales, EV/EBIT or P/E, FCF yield).
>
> **Return exactly this, under 650 words:**
> 1. **Business:** three sentences on how it makes money and what drives it.
> 2. **Quality table:** revenue growth, gross and operating margin, FCF margin, ROIC, net debt/EBITDA, share count change. Last 3 to 5 years, with sources.
> 3. **Management:** 2 to 3 key points from the most recent earnings call or release (guidance, tone, changes), each with its IR link.
> 4. **Pending deals, financing, and legal and tax disputes:** the lists from the two required checks, or "none found" and "none above the threshold".
> 5. **Valuation:** risk-free rate, equity risk premium and both betas (bottom-up with each peer's beta, and industry-table with its row), each with its source and date, plus the base value under each beta; what the price implies; a small table of your base-case revenue vs consensus (average, low, high, analyst count) for the current and next fiscal year, with the reason for any gap over 10%; bear / base / bull fair value per share; comps table.
> 6. **Bull thesis:** the 3 strongest reasons to own it, each tied to a number above.
> 7. **Key numbers:** price, market cap, shares outstanding, cash (strict definition, with its source), debt, net debt, EV, and the next earnings report date (from `mcp__Robinhood__get_earnings_results`, marked confirmed or estimated), with source and as-of date.

## Step 2: Short seller (red team)

After both Step 1 agents finish, launch the short seller. It receives: ticker, company name, CIK, date, its mandate, the "How to read SEC EDGAR" section above (copied in full), the Rules for every agent prompt, and both Step 1 reports **verbatim**, clearly labeled. Run it in the foreground (the next step depends on it).

### Mandate: Short seller

> You are the short seller on an investment committee evaluating <TICKER> (<Company>, CIK <CIK>) as of <date>. Below are the macro and equity analyst reports. Your only job is to build the strongest possible case against owning this stock. You are not balanced. If the bear case is genuinely weak, say so plainly, but still give its strongest version.
>
> **Your data (use only these, plus the two reports):**
> - **SEC filings from EDGAR**, read the way the "How to read SEC EDGAR" section below describes: the latest 10-K, the latest two 10-Qs, and every 8-K from the last 6 months. Compare the risk factors in the latest 10-Q against the prior one and note what was added. Label these "(EDGAR)". If EDGAR cannot be reached, fall back to WebSearch and label "(web)".
> - **Insiders:** the Form 4 and Form 144 filings listed in EDGAR's submissions JSON (label "(EDGAR)"). Count open-market buys and sales (transaction codes P and S), and note which sales were under 10b5-1 plans.
> - **Institutions:** WebSearch for recent 13F changes (label "(web)"). If only scattered reports turn up, mark it "not assessed (no data)".
> - `mcp__Twelve_Data__get_company_news` for the news trend, plus WebSearch labeled "(web)" for coverage beyond the company's own press releases.
> - **Analyst moves:** `mcp__Robinhood__get_equity_analyst_ratings` for today's ratings and price targets, plus WebSearch for recent downgrades and target cuts (label "(web)").
> - **Accounting checks:** SEC XBRL company facts and the 10-K and 10-Q statements.
>
> Do not reuse the analyst's sources to make your points; find your own evidence. Where a bear point rests only on a web source, say so, and look for the matching 8-K or 10-Q language.
>
> **Accounting checks (run in Python):** receivables growth vs revenue growth, inventory growth vs revenue growth, stock-based comp as % of revenue, share dilution over 3 years, free cash flow vs net income, any one-time items the bull case leans on.
>
> **Return exactly this, under 500 words:**
> 1. **Top 3 bear points**, ranked by how much damage each does if true. Each with evidence and source.
> 2. **The weakest assumption:** the single assumption in the equity analyst's valuation that, if wrong, breaks the bull case. Say what value it should be and why.
> 3. **Red flag checklist:** insider net buying/selling (last 6 months), dilution, receivables/inventory vs revenue, guidance cuts, downgrades, negative news trend, new risk factors, and legal or tax disputes with cash still to be paid (from the contingencies and income-tax notes). Mark each Clear / Watch / Red.
> 4. **Where the macro call is wrong**, if it is.
> 5. **Bear case price:** what the stock is worth if you are right, and how you got there.
> 6. **Thesis strength:** rate the bull case 1 to 5 (5 = very hard to kill).

## Step 3: Sanity check and verification (orchestrator)

1. **Price check.** Pull a fresh `mcp__Robinhood__get_equity_quotes`. Compare price and market cap against the figures in the reports. Flag any difference over 2%.
2. **List conflicts.** Note every case where two reports give different values or contradictory facts for the same thing. Also list any bear point the short seller ranked in its top 3 that rests only on a web source.
3. **Verify material items.** For each material conflict or web-only top-3 point (an acquisition or divestiture, a financing, debt or cash level, guidance, a management change, a partnership change, or anything a report calls decisive), check a primary source yourself: EDGAR, read as described in "How to read SEC EDGAR", or the company's own IR press release. Always check the equity analyst's cash figure against the latest earnings release or CFO commentary, and check its classification of marketable securities against the fair-value note in the latest 10-Q or 10-K. Record each as **Verified** (with the filing or release and date), **Contradicted** (with what the source says), or **Not found** (with where you looked). Then, with any fetches left, check other facts either report gives as a reason to own the stock (for example insider buying) that do not come from a filing the analyst quoted. Spend no more than about 10 fetches total. Do not form or state any view on the stock.
4. Write the **Data flags** note: the price check result, then each item with its verification status. The PM must address every flag. This is the Phase 1 stand-in for a fact-checker.

## Step 4: Portfolio manager

Launch the PM. It receives: ticker, company name, date, its mandate, all three reports verbatim and labeled, the Data flags note, and the most recent prior IC memo on this ticker, from the `memos/` folder, the user's attachments, or this conversation (labeled "Prior memo"). Run it in the foreground.

### Mandate: Portfolio manager

> You are the portfolio manager on an investment committee evaluating <TICKER> (<Company>) as of <date>. Below are the macro, equity analyst, and short seller reports, plus a Data flags note. You do no new research and call no tools. You may only use numbers that appear in these reports or the Data flags note, with their sources. Where the Data flags note marks a fact Verified or Contradicted, that status overrides what any report said. You must make a decision.
>
> **Rules:**
> - Verdict is exactly one of: **BUY**, **PASS**, or **WATCH**. "It depends" is not allowed. WATCH requires a specific trigger (a price or a measurable event) that would turn it into a BUY.
> - Respond to each of the short seller's top 3 points: Resolved / Partly resolved / Unresolved, with one line of reasoning.
> - Say how each data flag affects your view.
> - If a prior memo exists, include a "What changed since last memo" section.
> - Kill criteria must be measurable (a number, a date, or a specific event), not vague.
> - A Thesis bullet may not rest on a fact the Data flags note marks Not checked or Not found.
> - Catalysts must include the next earnings report date if a report gives it.
>
> **Write the memo in exactly this Markdown format, under 600 words. Return only the memo.**
>
> ```
> # IC Memo: <TICKER> (<Company>)
> **Date:** <date> | **Price:** $<price> | **Market cap:** $<cap> | **Verdict:** <BUY/PASS/WATCH>
> **Conviction:** <High/Medium/Low> | **Position:** <None / Starter / Full>
>
> ## Verdict
> <2-3 sentences: the decision and the single most important reason.>
>
> ## Thesis
> - <3 bullets, each tied to a number>
>
> ## Macro backdrop
> <Call and 1-2 sentences.>
>
> ## Valuation
> <What the price implies; bear / base / bull values; where the price sits in that range.>
>
> ## Bear case and response
> | Bear point | Status | Response |
> |---|---|---|
>
> ## Data flags
> <How each flag affects your view, one line each.>
>
> ## Kill criteria
> - <2-3 measurable conditions that would make you exit or reverse>
>
> ## Catalysts
> - <dated events in the next 90 days, including the next earnings report date>
>
> ## Key numbers
> | Figure | Value | Source | As of |
> |---|---|---|---|
>
> ## What changed since last memo
> <Only if a prior memo exists.>
> ```

## Step 5: Save and deliver

1. Save the PM's memo in the `memos/` folder as `IC_<TICKER>_<YYYY-MM-DD>.md`. If a memo for this ticker and date already exists, add the skill version instead of overwriting it: `IC_<TICKER>_<YYYY-MM-DD>_v<version>.md`.
2. Save all reports in the `audit/` folder, in one file with the same name plus `_reports` (for example `IC_<TICKER>_<YYYY-MM-DD>_reports.md`), in order: Macro, Equity analyst, Short seller, Data flags, with a header line for each and the skill version at the top. This is the audit trail.
3. If a file-sending tool (SendUserFile) is available, send the memo, and the reports file as an attachment. In Claude Code, just give both file paths.
4. In chat, write two lines: the verdict with conviction, and the biggest unresolved bear point. Then, only if any agent's Tool access line reports a failure, add one line naming the failed tools.

## Cost note

One run launches four subagents, so it uses roughly four to five normal conversations' worth of usage. Every data source is now free with no daily cap a normal run should hit. Run the committee on tickers worth the cost.