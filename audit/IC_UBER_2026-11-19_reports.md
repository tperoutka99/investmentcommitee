# IC Reports: UBER (Uber Technologies, Inc.), 2026-11-19
Audit trail for IC_UBER_2026-11-19.md. Skill version: investment-committee v0.1. Each report is verbatim as returned by its agent.

---

## 1. Macro strategist

**UBER macro view, as of 2026-11-19** (Sector: Industrials / Transportation (web, Simply Wall St). AV = Alpha Vantage tool.)

**1. Regime:** The economy is growing and inflation is heating up again. CPI is about 3.7% and unemployment is falling to 4.1%. The Fed held at 3.75–4.00% on Oct 28, with two dissenters who wanted a hike. Futures price a more than 90% chance of a 25bp hike on Dec 9 and three hikes by July 2027 (web: Fed statement; Trading Economics, 11/17).

**2. Data table**
| Indicator | Latest | Prior | As-of | Source |
|---|---|---|---|---|
| Effective fed funds rate | 3.88% | 3.75% | Oct / Sep 2026 | AV FEDERAL_FUNDS_RATE |
| 2Y Treasury | 4.80% | 4.83% | 11/17 / 11/16 | AV TREASURY_YIELD |
| 10Y Treasury | 5.10% | 5.12% | 11/17 / 11/16 | AV TREASURY_YIELD |
| CPI index | 337.511 | 336.940 (Sep 2026 YoY +3.7%) | Oct / Sep 2026 | AV CPI |
| Unemployment rate | 4.1% | 4.2% | Oct / Sep 2026 | AV UNEMPLOYMENT |
| Nonfarm payrolls (not seasonally adjusted) | 160,277k (YoY +0.6%) | 159,254k | Oct / Sep 2026 | AV NONFARM_PAYROLL |
| Real GDP YoY | +2.2% | +2.4% | Q3 / Q2 2026 | AV REAL_GDP |
| Retail sales YoY (nominal) | +6.7% | +7.0% | Oct / Sep 2026 | AV RETAIL_SALES |

**3. Sensitivity**
- **Rates:** Uber's value rests on cash flow years out, so the main way rates hurt is a lower valuation multiple, not interest expense. Higher rates also make car loans and leases cost more for drivers, which shrinks the pool of drivers. Capital-heavy autonomous-vehicle fleet plans also get pricier to fund.
- **Growth:** Rides follow jobs, commuting, travel and nightlife, so strong employment helps demand. The catch is that a tight job market leaves fewer people willing to drive, so Uber has to pay higher driver incentives. Delivery holds up better in a slowdown.
- **Inflation:** Uber takes a cut of each fare or order, so rising prices push revenue up in dollar terms. The pressure is on costs: auto insurance and fuel. Consumers who keep paying more also start to trade down.
- **Dollar:** A big share of bookings is outside the US. If the Fed hikes while other central banks don't, a stronger dollar shrinks those bookings when they're reported in dollars. No dollar data was assigned, so I have no figure for this.

**4. Call: Headwind, Medium confidence.** The Fed is starting to hike again with the 10Y above 5% and CPI near 3.7%, which squeezes the valuation multiple and driver costs. Healthy demand is real but already expected.

**5. Next 30 days**
- Dec 1: JOLTS (Oct)
- Dec 4: November jobs report
- Dec 8–9: FOMC meeting (decision Dec 9, 2:00pm ET; press conference 2:30pm)
- Dec 10: November CPI (most important)
- Dec 15: November PPI
- Dec 16: November retail sales

Dates are from the BLS and Fed calendars (web).

**6. What would flip the call:** the 10Y closing below 4.75% for 5 straight sessions, which would mean the market has priced out the hiking cycle. That moves the call to Neutral.

**Tool access:** COMPANY_OVERVIEW failed (premium endpoint), so the sector came from the web. FMP economics has no calendar endpoint, so the calendar came from the web. INFLATION only runs to 2024 and wasn't used. Several AV calls hit rate limits at first but worked on retry.

---

## 2. Equity analyst + valuation

**UBER — Equity Analyst (as of 2026-11-19)**

**1. Business**
Uber makes most of its money by taking a cut of each Mobility ride and Delivery order on its platform: $59.8B of gross bookings in Q3'26, with revenue of $14.8B. Two things drive it: more users and more use (215M monthly active users; 4.1B trips, up 16%), and the Uber One subscription (~55M members) that ties rides and delivery together. Recently, revenue (+9.6% YoY in Q3) has grown about half as fast as bookings (+20%). Grocery and retail (a $15B run rate, +40%) and autonomous vehicles (AVs) are the newer growth bets. *(Uber press release and transcript, 2026-11-04, web; FMP income statement)*

**2. Quality** *(FMP statements, FY to 2025-12-31; TTM to 2026-09-30. ROIC = op. income×(1−21%) ÷ operating invested capital; "adj" adds 3-yr capitalized R&D)*

| | 2021 | 2022 | 2023 | 2024 | 2025 | TTM |
|---|---|---|---|---|---|---|
| Rev growth | – | 82.6% | 17.0% | 18.0% | 18.3% | 9M: 12.0% |
| Gross margin | 46.4% | 38.3% | 39.8% | 39.4% | 39.8% | 43.2% |
| Op margin | −22.0% | −5.7% | 3.0% | 6.4% | 10.7% | 12.4% |
| FCF margin | −4.3% | 1.2% | 9.0% | 15.7% | 18.8% | 18.4% |
| FCF−SBC margin | −10.9% | −4.4% | 3.8% | 11.6% | 15.3% | 14.8% |
| ROIC (adj) | neg | neg | 6.0% | 16.8% | 32.0% | 38.5% |
| Net debt/EBITDA | n.m. | n.m. | 2.9x | 1.1x | 0.7x | 1.0x |
| Diluted shares | – | +4.4% | +5.9% | +2.8% | −1.4% | −3.5% YoY |

GAAP net income is distorted by valuation-allowance releases and gains or losses on equity stakes, so I don't use it for quality.

**3. Management (Q3'26 call, 2026-11-04)**
- **Guidance:** Q4 gross bookings $63.25–65.25B (+18–22% in constant currency). Adj. EBITDA $3.13–3.23B. Non-GAAP EPS $0.95–0.99 (+34–39%). Adj. EBITDA is being retired as a key metric. [Uber IR transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Nov/04/Uber-Q3-Earnings-Call-Transcript.pdf) (web); [Quartr event](https://quartr.com/events/uber-technologies-inc-uber-q3-2026_3PkH0eTw) (link found by web search; the Quartr tool was unavailable)
- **Tone:** The CEO said Mobility "came in below our expectations" because of driver shortages in Brazil, India and Canada. The CFO said there are no "meaningful changes in the margin trajectory." Q4 driver incentives will hit take rate rather than margin. [transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Nov/04/Uber-Q3-Earnings-Call-Transcript.pdf) (web)
- **Capital allocation:** Uber is pulling back on M&A after ~$1.55B of acquisitions in Q2–Q3 (FMP cash flow), shifting to organic growth plus buybacks. Early AVs will sit on Uber's balance sheet: a $10B AV commitment, ~700 driverless vehicles by end-2026 and >2,000 by end-2027. [transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Nov/04/Uber-Q3-Earnings-Call-Transcript.pdf) (web)

**4. Valuation** *(Damodaran-style DCF run in Python. Assumptions: 10-yr Treasury 4.25%, equity risk premium 4.5%, unlevered beta 1.20 → WACC 9.46%, falling to 8.19%; tax 18% rising to 25%; terminal growth 4%. Stock-based comp is treated as a cost.)*

**What the price implies:** At $65.60 the market is pricing either:
- ~8.4% revenue growth for 5 years with margins frozen at today's 12.4%, or
- consensus-like 13% growth with the operating margin falling to 10.2%.

Consensus revenue goes from $57.8B in 2026 to $94.2B in 2030, a ~13% CAGR (FMP analyst estimates).

| Case | Rev growth yrs 1–5 | Target op margin | Sales/capital | Terminal ROC | **$/share** |
|---|---|---|---|---|---|
| Bear | 7% | 12% | 2.0 | = WACC | **$47** |
| Base | 13% | 18% | 3.0 | 15% | **$116** |
| Bull | 16% | 22% | 4.0 | 25% | **$185** |

- **Terminal value:** 69% of the base value.
- **Discount rate:** ±1pt WACC moves the base to $95 / $152.
- **Terminal growth:** going from 4% to 2% moves the base to $97, so the base assumes a lasting competitive edge.
- **Return on capital:** year-1 ROC in the base case is 49%, above the 40% flag. That is plausible for a business that runs on negative working capital, but AV capex could cut it.
- **Equity stakes:** $22.2B carried at book, ~$10.9/share, is a separate uncertainty.

**Comps** (peers from stockanalysis.com, web, closes 10/26–11/13/26; UBER from FMP, 11/19)

| | EV/Sales | EV/EBIT | Fwd P/E | FCF yield |
|---|---|---|---|---|
| UBER | 2.5x | 20.1x (17.2x ex-stakes) | 15.0x ('27) | 7.8% |
| DASH | 4.2x | 68.3x | 24.8x | 3.6% |
| CART | 3.3x | 22.3x | 23.6x | 8.3% |
| GRAB | 1.8x | 47.5x | 15.7x | −1.5% |
| LYFT | 0.9x | n.m. | 7.8x | 17.5% |

**5. Bull thesis**
1. **The price assumes little growth.** The market is pricing ~8% growth at flat margins, against 20% bookings growth and a 13% consensus revenue CAGR. The FCF yield is 7.8% (6.2% after stock comp).
2. **Margins keep climbing.** Operating margin went from −22% in 2021 to 12.4% TTM, gross margin is up to 43.2%, and R&D-adjusted ROIC is 38.5%.
3. **Buybacks are shrinking the share count.** Diluted shares are down 3.5% YoY, after $6.5B of buybacks in 2025 and $4.3B in the first nine months of 2026. Leverage is low at ~1.0x net debt/EBITDA.

The main risks are revenue growing more slowly than bookings, and AV economics.

**6. Key numbers** (FMP quote, close 2026-11-19)
- **Price:** $65.60 (52-week range $64.04–92.78)
- **Market cap:** $133.95B
- **Shares outstanding:** 2,041.9M, implied from market cap ÷ price (Q3 weighted basic 2,038.4M, FMP). Not checked against the 10-Q cover page.
- **EV:** $141.6B = market cap + debt including leases $17.74B − cash and short-term investments $10.07B (FMP balance sheet, 2026-09-30). FMP's key-metrics EV is $142.1B. Adding minority interest and removing equity stakes gives $120.7B.

**Tool access:** Every Quartr tool failed (subscription required), so management and transcript data come from Uber IR via WebFetch, labeled (web). FMP quote and statements were denied for peer tickers (plan tier), so the peer comps are from the web.

---

## 3. Short seller (red team)

**UBER: Short-seller case (as of 2026-11-19)**

**Sources:** FS = FMP statements (Q3'26 filed 11/4/26; FY25 filed 2/13/26). INS = AV INSIDER_TRANSACTIONS (6/2–11/12/26). INST = AV INSTITUTIONAL_HOLDINGS (13Fs to 9/30/26). AN = FMP analyst (11/19/26). (web) = fallback.

**1. Top 3 bear points**
1. **Revenue and margins are slowing, not compounding at 13%.**
   - Q3 revenue grew 9.6% YoY. Operating margin fell to 9.8% (11.1% excluding $186M of restructuring), down from 14.6% in Q1 (FS).
   - R&D rose 48% and stock comp rose 27%, against revenue up 9.6% (FS).
   - Take rate was 24.7%, down from 27.1%. Mobility revenue fell 2% while Mobility bookings rose 18%. Non-GAAP EPS of $0.88 missed consensus (web: sec-api, Finviz, 11/4/26).
   - Caveat: a change to the UK business model explains part of the take-rate drop.
2. **Autonomous vehicles turn Uber from a toll-collector into a fleet owner, and its best partner is leaving.**
   - Waymo will run Austin and Atlanta on its own from Jan 2028. The stock fell 9% on the news (web: Simply Wall St, 7/25/26).
   - The risk factors in the Q2 10-Q now say Uber may need more debt to buy AVs (web: sec-api, 11/4/26).
   - The analyst's 38.5% ROIC and 3.0 sales-to-capital assume an asset-light model that is ending.
3. **The balance sheet is taking on debt again, and buybacks only offset dilution.**
   - In nine months, debt rose from $12.08B to $17.74B and net debt from $4.98B to $8.18B (FS, 12/31/25 to 9/30/26).
   - The $14.8B Delivery Hero deal, backed by a ~€14B bridge loan, contradicts the analyst's "pulling back on M&A" (web: Bloomberg Law, Cooley, 7/16/26).
   - Buying the ~75% Uber doesn't own takes pro forma net debt to ~$19B, about 2.5x EBITDA before adding Delivery Hero's own debt.
   - Basic shares are up 0.1% versus FY23, despite $12.05B of buybacks since 2024 (FS).
   - The analyst's $22.2B of "equity stakes" appears to include ~$8.8B of restricted investments that back $13.7B of insurance reserves (web: sec-api). That overstates value by ~$4.3/share.

**2. The weakest assumption:** the 13% revenue growth rate for years 1–5. It should be 8–9%:
- Q3 growth is 9.6% and falling.
- Take rate is compressing.
- Q4 incentives move to drivers.

The analyst's own reverse DCF shows that 8.4% growth at a 12.4% margin gives $65.60, which is today's price and leaves no upside. A second problem: the model uses a 4.25% risk-free rate, but the 10Y is at 5.10% (macro report, AV 11/17).

**3. Red flag checklist**
- **Insiders: Clear.** Net open-market buying of +$10.8M. The CEO bought $10.0M at $70.96 on 9/10 and the COO bought $5.3M on 9/4; sales were $4.5M (INS).
- **Dilution: Watch.** Basic shares are flat over 3 years despite buybacks. Stock comp is 4.0% of Q3 revenue, up from 3.5% in FY25 (FS).
- **Receivables/inventory: Watch.** Receivables rose 17.3% against revenue up 9.6%, and days sales outstanding went from 25.8 to 27.6 (FS). Uber holds no inventory.
- **Guidance: Watch.** There was no formal cut. But Q3 EPS missed, and management said Mobility came in "below expectations" (web).
- **Downgrades: Watch.** No downgrade since 6/27/25. The average price target was $97 last quarter, versus $102.54 over the trailing year (AN).
- **News trend: Red.** Waymo's exit, the Q3 miss, and a 52-week low of $64.04 on 10/29 (web). Ownership is crowded at 94% institutional (INST).

**4. Where the macro call is wrong:** The Headwind call is right. Two parts of the reasoning are wrong:
- The report says rates hurt Uber through the valuation multiple, not interest expense. That no longer holds. Euro notes, a $3B term loan and the Delivery Hero bridge make Uber a borrower going into a hiking cycle.
- The driver shortages are in Brazil, India and Canada. They are not caused by tight US labor.

**5. Bear case price: $50 (24% below $65.60).**
- Start with trailing free cash flow of $10.42B (FS).
- Subtract stock comp of $2.07B and a $1.49B working-capital and insurance-float tailwind. That leaves $6.86B of owner free cash flow.
- At 15x (a 6.7% yield, ~160bp over the 5.10% 10Y), that is $103B, or about $50 per share on 2,041.9M shares.
- This assumes Delivery Hero creates no value. Cross-check: the analyst's bear DCF gives $47.

**6. Thesis strength: 3/5.** At a ~12% owner-cash-flow margin, with insiders buying, the stock already prices in a lot of the slowdown. The bear case is real but not a knockout.

**Tool access:**
- FMP secFilings was denied (plan tier), so the risk-factor changes come from sec-api (web).
- AV NEWS_SENTIMENT failed (premium endpoint), so the news is from WebSearch.
- AV INSTITUTIONAL_HOLDINGS hit a rate limit, then worked on retry.
- FMP statements were denied at limit=16 and worked at limit=5.

---

## 4. Data flags (orchestrator sanity check)

Fresh FMP quote (2026-11-19): price $65.60, market cap $133.95B. Both match the reports. No price or market-cap flag.

Conflicts between reports (not resolved by the orchestrator):
1. **Risk-free rate.** The equity DCF uses a 10Y Treasury of 4.25%. The macro report shows the 10Y at 5.10% (AV TREASURY_YIELD, 11/17). Per the equity analyst's own sensitivity, +1pt WACC moves the base value from $116 to $95.
2. **Net debt at 9/30/26.** The equity report's figures imply $7.67B (debt incl. leases $17.74B − cash and ST investments $10.07B). The short seller states $8.18B.
3. **M&A.** The equity report says Uber is pulling back on M&A (~$1.55B of acquisitions in Q2–Q3). The short seller cites a $14.8B Delivery Hero deal backed by a ~€14B bridge loan (web, 7/16/26). Neither figure was verified against a filing.
4. **Equity stakes.** The equity report carries $22.2B (~$10.9/share). The short seller says ~$8.8B of that is restricted investments backing insurance reserves, overstating value by ~$4.3/share (web).
5. **Share count trend.** The equity report shows diluted shares −3.5% YoY. The short seller shows basic shares +0.1% vs FY23. These are different measures and periods, not necessarily contradictory.
