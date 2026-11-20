# IC MRVL 2026-11-20: Reports (audit trail)
**Skill version:** v0.9 rules (approved by Trey 2026-11-20; proposal not yet saved to the skill file at run time)

## Macro strategist
**MRVL – Macro Strategist View (as of 2026-11-20)**

**1. Regime:** Growth is strong and inflation is speeding up again, and the Fed has started hiking. It raised 25bp in Sept 2026, held at 3.75–4.00% on Oct 28 with two members voting for a hike, and betting markets put a December hike at about 92%.

**2. Data table**
| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| Fed funds (effective) | 3.88% | 3.63% (pre-hike) | 2026-11-18 | FRED DFF |
| 10Y / 2Y Treasury | 5.07% / 4.80% | 5.15% / 4.77% (10-19) | 2026-11-18 | FRED DGS10, DGS2 |
| CPI YoY (3m annualized) | 3.91% (5.72%) | 4.00% (4.56%) | Oct 2026 | FRED CPIAUCNS, CPIAUCSL |
| Unemployment | 4.1% | 4.2% | Oct 2026 | FRED UNRATE |
| Payrolls, monthly change | +165k | +60k | Oct 2026 | FRED PAYEMS |
| Real GDP, annualized | 3.37% | 2.22% | Q3 2026 | FRED GDPC1 |
| Retail sales MoM (YoY) | +0.21% (+6.8%) | +0.83% | Oct 2026 | FRED RSAFS |
| Dollar proxy, UUP ETF | $29.63 | $28.90 (10-20); $27.88 (08-19) | 2026-11-19 | Twelve Data |

The UUP ETF is up 2.5% in 1 month and 6.3% in 3 months.

Odds for the Dec 9 Fed decision:
- **Polymarket (11-20):** +25bp 92.5%, hold 3.2%, +50bp or more 3.9%, any cut under 0.3%. Total volume $44.4M.
- **Kalshi (11-20):** +25bp 92%, more than +25bp 6%, hold 3%, any cut 2%. Total volume about 17.7M contracts.

The two markets agree. These are betting markets, not the fed funds futures professionals use.

**3. Sensitivity**
- **Rates:** The direct interest-cost risk is low. All $4,999.9M of debt is fixed-rate notes (2.45%–5.95%), nothing floating is drawn, and the new $3.0B SOFR revolver has no loans on it. The real exposure is refinancing $1,249.9M due in 2028: $499.9M at 4.875% and $750.0M at 2.45%. If the 2.45% notes were refinanced near the 5.30% rate of the new 2036 notes, interest would rise about $21M a year (my rough estimate). The bigger rate channel is the stock's valuation: a high-multiple chip stock with the 10Y above 5% means a higher discount rate.
- **Growth:** Demand for these chips follows business capital spending (capex). The Fed's own statement cites "robust capital investment," and Q3 GDP grew 3.4%, so this channel is supportive.
- **Dollar:** There is no currency-translation loss because all sales are priced in U.S. dollars. The risk is price competitiveness: China 42%, Taiwan 17% and Singapore 12% of shipments ($1,955.6M of $2,739.3M). Most "China" shipments go to factories of customers based outside China, so that figure measures manufacturing location, not Chinese demand. A 6% stronger dollar over 3 months gives a mild headwind.
- **Inflation:** Matters mostly by pushing the Fed to hike. Input-cost effects: not assessed (no data).

**4. Call:** **Headwind, Medium confidence.** The business's own exposure is small (fixed-rate debt, dollar sales) and strong capex demand helps. That is outweighed by speeding-up inflation, a hiking Fed, a 10Y above 5% and a rising dollar, which squeeze valuations of long-duration chip stocks.

**5. Next 30 days**
- Nov 25: Q3 GDP second estimate and October PCE inflation (BEA)
- Dec 1: JOLTS job openings (BLS)
- Dec 4: November jobs report (BLS)
- **Dec 8–9: FOMC meeting with new projections (SEP) and dot plot**
- Dec 10: November CPI (BLS), the day after the Fed decision
- Dec 15: PPI (BLS)

**6. What would flip my call:** The November CPI (Dec 10) shows 3-month annualized inflation (CPIAUCSL) below 3.5%, and the 10Y (DGS10) closes below 4.75% for 5 straight trading days. That would move the call to Neutral.

Tool access: all assigned tools worked.

## Equity analyst + valuation
**MRVL equity analyst report, as of 2026-11-20**

**1. Business**
Marvell designs chips for data infrastructure: electro-optics DSPs, custom AI accelerators (XPU) and attach chips, switching and storage. Its fabs are outsourced. Data center revenue grew 46% y/y in Q2 FY27, and total revenue grew 37% to $2.739B. The business is driven by hyperscaler AI capex, the ramp of custom programs (Google, and an NVIDIA partnership) and the shift from copper to optical links.

**2. Quality** (EDGAR XBRL, 10-K/10-Q; ROIC = GAAP EBIT×0.85 ÷ average of debt + equity − cash; goodwill-heavy)

| | FY22 | FY23 | FY24 | FY25 | FY26 | TTM Aug-26 |
|---|---|---|---|---|---|---|
| Revenue growth | 50.3% | 32.7% | −7.0% | 4.7% | 42.1% | 30.6% |
| Gross / operating margin | 46/−8% | 51/4% | 42/−10% | 41/−13% | 51/16% | 52/16.5% |
| FCF margin | 14.6% | 18.3% | 18.8% | 24.2% | 17.0% | 18.3% |
| ROIC | −2% | 1% | −3% | −4% | 7% | 7% |
| Net debt/EBITDA | 4.4x | 2.2x | 3.9x | 4.9x | 0.7x | 0.36x |
| Diluted share change | +19% | +7% | +1% | +0.5% | +0.5% | +5.8% |

**3. Management**
- **Q2 FY27 release (Aug 27):** Management "again" raised its FY27 and FY28 revenue outlook but gave no figures. Q3 guide is $3.15B ±5%, which would be +52% y/y. Non-GAAP gross margin guide is 57.5–58.5%. (IR) https://investor.marvell.com/news-events/press-releases/detail/1031/marvell-technology-inc-reports-second-quarter-of-fiscal-year-2027-financial-results
- **Nov 2:** Agreed to buy Lumentum in an all-stock deal. Preliminary Q3 revenue is at the guidance midpoint, with the range narrowed to ±2%. Management cites more than $1B of run-rate cost synergies. (IR) https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity
- **New CFO:** Dan Durn (former Adobe CFO) started June 15, 2026. (IR) https://investor.marvell.com/news-events/press-releases/detail/1025/marvell-announces-cfo-transition

**4. Pending deals, financing, and legal and tax disputes**
- **Lumentum (pending, close expected 1H CY2028):** 4.5 MRVL shares per LITE share. That is about 457.7M new shares (101.7M LITE diluted shares; EDGAR 10-Q, 9/26/26).
  - LITE debt is $1,399.6M, cash $1,272.2M and short-term investments $707.4M (holdings not verified). Strict net debt is $127M.
  - Termination fees: $5.8B, or $3.2B regulatory ($3.47/share).
  - Built in as a separate pro forma line (section 5). LITE trades at $535.15 against $623.1 implied by the ratio, a 16.4% spread.
- **Google warrant (8-K 1.01/3.02, Aug 18):** 58.97M shares at $206.58. They vest per $500M of custom revenue through FY33. Black-Scholes value is $4.16B (vol 55.83%, Damodaran semiconductor std dev). I deduct 25%, 50% and 100% of it in bear, base and bull.
- **Celestial earnout:** fair value $749.5M (10-Q; up to 22.4M shares plus $233M cash), treated as debt. The $131M forward-contract asset is added back.
- **Revolver:** upsized to $3B on Oct 22 (8-K 1.01) and undrawn, so no debt added.
- **Closed within 12 months:** $1B 5.30% notes due 2036 (in debt), NVIDIA $2B preferred (21.8M shares in the count), Celestial and XConn.
- **No stock-sale program:** the 424B7s are resales by holders with no proceeds to Marvell, so there is one per-share value.
- **Legal and tax:** none above the threshold ($393M). Gross unrecognized tax benefits are $594.6M (10-K), but that is an aggregate of positions, not a single dispute.

**5. Valuation**

**Inputs**
- **Risk-free rate:** 5.07% (FRED DGS10, 2026-11-18).
- **Equity risk premium:** 4.41%, Damodaran implied ERP for Nov 1, 2026 (home page).
- **Bottom-up beta (used in the cases):** peer raw (unlevered) betas are AVGO 2.25 (2.17), CRDO 3.58, ALAB 2.64, MTSI 1.56 (1.54) and RMBS 2.15. Source: Twelve Data, 104 weekly returns vs SPY. Median unlevered 2.17, relevered to Marvell's 4.3% D/E gives **2.25**.
- **Industry-table beta:** Damodaran "Semiconductor" row (US, Jan 2026), 1.50 corrected for cash, relevered to **1.55**.
- **The two betas differ by 0.70, more than 0.3.**
- **Cost of capital:** cost of debt 6.14% (spread on the 2036 notes at issue). WACC is 14.56% in years 1–5, falling to 9.81% in the stable period.

**Base value:** $103.3 with the bottom-up beta, $122.3 with the industry beta. Terminal value is 61% of the total. Value rises with terminal growth ($88 at 2% to $115 at 5%) because terminal ROC of 20% is above WACC.

**What $138.47 implies (reverse DCF, bottom-up beta):** either a 10-year revenue CAGR of 20.5% (FY37 revenue $77B) at a 33% margin, or a 43.5% target margin at my base growth. With the industry beta: 18.1% CAGR or a 37.1% margin.

**Base revenue vs consensus** (Yahoo consensus, 2026-11-20)

| Fiscal year | Base | Average | Low | High | Analysts | Gap |
|---|---|---|---|---|---|---|
| FY27 (Jan 2027) | $12.0B | $12.07B | $11.94B | $12.4B | 41 | −0.6% |
| FY28 | $18.6B | $19.71B | $18.05B | $22.05B | 38 | −5.6% |

Neither gap is over 10%. Years 3 onward are my own; no consensus exists for them.

**Fair value per share** (bottom-up beta; industry beta in brackets)

| Case | Value | Main assumptions | Lumentum pro forma (no / with $11.6B synergy PV) |
|---|---|---|---|
| Bear | **$41** ($48) | FY28 +40%, 26% margin, sales-to-capital 1.5, terminal ROC 10% | $66.8 / $75.2 |
| Base | **$103** ($122) | FY28 +55%, then 30/20/15%, 33% margin, sales-to-capital 2.0 | $108.5 / $116.9 |
| Bull | **$158** ($187) | FY28 +65%, 38% margin, sales-to-capital 2.5 (imputed ROC reaches 46%, flagged) | $145.0 / $153.4 |

The deal raises value per share only if standalone Marvell is worth less than $118.9.

**Comps** (TTM, SEC XBRL; prices are Robinhood closes on 11/19)

| | EV/Sales | EV/EBIT | P/E | FCF yield |
|---|---|---|---|---|
| MRVL | 13.3x | 80x (51x ex-amortization) | 47x (includes divestiture gain) | 1.4% |
| AVGO | 19.0x | 39.5x | 43.2x | 2.4% |
| CRDO | 13.4x | 42.3x | 41.1x | 2.0% |
| ALAB | 22.9x | 89.7x | 80.2x | 0.9% |
| MTSI | 12.2x | 53.1x | 50.1x | 1.7% |
| RMBS | 9.3x | 25.5x | 30.7x | 3.8% |

On consensus, Marvell trades at 6.4x FY28 EV/Sales and 18.9x FY28 EPS.

Robinhood analyst ratings: 40 buy, 5 hold, 0 sell; mean price target $314 (range $175–450).

**6. Bull thesis**
1. **Growth is locked in near term:** Q3 is guided at +52% y/y and consensus FY28 is +63%, yet the stock trades at only 18.9x FY28 EPS.
2. **Margin leverage:** operating margin swung from −12.5% (FY25) to 16.5% TTM. Reaching a 37% margin justifies today's price under the industry beta.
3. **Strategic validation and a clean balance sheet:** NVIDIA bought $2B of preferred convertible at $91.84, Google's warrant is tied to up to $120B of custom revenue, and net debt/EBITDA is 0.36x.

**7. Key numbers**
- **Price:** $138.47, official close 2026-11-19 (Robinhood); pre-market $133.16 at 09:16 UTC on 11/20.
- **Market cap:** $121.4B (Robinhood), or $124.4B including the NVIDIA preferred.
- **Shares:** 876.9M on the 10-Q cover (Aug 21, 2026); 922.5M diluted used in the valuation.
- **Cash (strict):** $3,932.8M. The note shows no marketable debt securities; $194M of time deposits sit inside cash equivalents. Equity stakes of $181.7M are shown separately. This matches the Q2 release (10-Q, 8/1/26).
- **Debt:** $4,999.9M face, plus $323M of leases.
- **Net debt:** $1,067M.
- **EV:** $125.5B.
- **Next earnings report:** 2026-12-01 after market close, confirmed (Robinhood).

Tool access: all assigned tools worked.

## Short seller
**MRVL short-seller report (as of 2026-11-20)**

**1. Top 3 bear points**

1. **The Lumentum deal hands away a third of the company at peak optics prices.** The deal values Lumentum at a $115B enterprise value, close to Marvell's own $121B market cap. It issues about 457.7M shares, 52% of the 876.9M on the cover. Closing is not expected until 1H CY2028, with outside dates running to Aug 1, 2028. If regulators block it, Marvell owes a $3.2B cash fee (8-K 1.01, 11/2/26, EDGAR). The market's verdict: the stock went from $251.65 (Oct 28) to $138.47, down 45% (web). TD Cowen downgraded and cut its target from $350 to $175, calling the deal dilutive to year-one EPS (web). Management claims it is accretive on a non-GAAP basis (EDGAR).
2. **The AI capex bet is concentrated and locked in at high fixed cost.** The ten largest customers were 82% of FY26 revenue (10-Q 8/28/26, EDGAR). Marvell has $8.52B of unconditional purchase commitments, 6.3x inventory and 90% of TTM revenue, plus a TSMC capacity deal under which advance payments are forfeited if volumes fall short (EDGAR). New risk factors in the Q2 10-Q: local opposition to data center siting, a bipartisan AI oversight bill from July 2026, and a BIS semiconductor tariff report. Democrats won both chambers on Nov 3, and the stock fell 7% and then 16% (web). The last downturn, FY24–25, brought a -10% to -13% operating margin.
3. **Earnings quality is getting worse.**
   - Stock-based comp doubled to $326M in Q2, 11.9% of revenue. FCF minus SBC over six months was only $428M (8.3% of revenue).
   - Receivables rose 53% y/y against 37% revenue growth. Days sales outstanding went from 66 to 74 days, even after factoring $412M of receivables in the first half.
   - Accruals for distributor price claims rose from $518M (FY25) to $778M, and the 10-K notes rising distributor inventory.
   - Non-GAAP gross margin is drifting down: 59.4% a year ago, 58.9% in Q2, 57.5–58.5% guided for Q3 (EDGAR).

**2. Weakest assumption**
The 33–38% steady-state operating margin (bull point 2: "37% justifies the price"). The Q3 guide implies only 21% GAAP margin, or 28% excluding amortization but still counting SBC. Gross margin is falling as lower-margin custom chips grow, and Lumentum's optics will dilute mix further. A realistic figure is **about 26%**. That is the analyst's own bear margin, which gives $41–48 standalone, or $67–75 pro forma.

**3. Red flag checklist**

| Item | Rating | Detail |
|---|---|---|
| Insider net buying/selling (6 months) | **Red** | 0 open-market buys, 17 sales (123,279 shares, $27.6M). 15 were under 10b5-1 plans. The CFO (Jun 23) and the chief accounting officer (Oct 8) sold without a plan. The CEO was still selling at $146.54 on Nov 16. |
| Dilution | **Red** | Diluted shares +8.2% over 3 years. Potential count is about 1.46B (Lumentum, Google warrant, Celestial earnout), +67%. |
| Receivables vs revenue | **Red** | +53% vs +37%. |
| Inventory vs revenue | **Clear** | +29% vs +37%. |
| Guidance cuts | **Clear** | Q3 held at the midpoint. |
| Downgrades | **Red** | TD Cowen to Hold; B. Riley cut its target twice (web). The Robinhood mean target of $314 is stale; it was last updated Nov 7. |
| Negative news trend | **Red** | Twelve Data feed shows a shareholder law-firm probe of the deal and the AI selloff. |
| New risk factors | **Watch** | Data center siting opposition, the AI oversight bill and tariffs. |
| Legal/tax with cash to pay | **Watch** | $249M of income tax payable, partly from tax on the divestiture gain. No specific legal or tax dispute is disclosed. |
| Other | **Watch** | The CFO resigned on 5 days' notice in June; the audit chair became CFO. |
| Institutions (13F) | Not assessed (no data) | Only scattered reports found. |

**4. Where the macro call is wrong**
The macro report calls capex "supportive" and treats it as broad business investment. It is not. About ten hyperscalers drive the revenue, and their buildout now faces political and permitting risk that the report leaves out: the election result and the new risk factors above. The FX point is minor. Revenue shipped to Asia rose to 84% (from 76% a year ago), and tariff exposure matters more than the dollar.

**5. Bear case price: about $70 (-49%)**
- Start from implied FY28 consensus EPS: $138.47 ÷ 18.9x = $7.33.
- Subtract SBC (about $1.25/share after tax): about $6.10.
- Cut revenue to the $18.05B low estimate: about $5.30.
- Apply 13x, a cyclical multiple with the 10Y above 5%: about $69.
- This matches the analyst's own pro forma bear range of $67–75.

**6. Thesis strength: 2/5.** Near-term growth is real: Q3 is tracking +52% y/y. But the deal, the concentration and the gap between GAAP and non-GAAP margins leave the bull case exposed.

Tool access: all assigned tools worked. One WebFetch, a Trefis article, failed; I used letsdatascience.com and tikr.com instead. No price-history tool was used.

## Data flags
**Price check: FLAG.** The fresh Robinhood quote on 2026-11-20 at 09:29 UTC (pre-market) is **$132.63**, which is **4.2% below** the $138.47 close (11/19) that all reports use. Pre-market volume is thin, so the regular-session open may differ. Lumentum is also lower pre-market, at $505.51 against a $535.15 close. At $132.63, market cap is about $116.3B (876.9M shares). Every report figure is still stated at $138.47.

**Verified items**

1. **Lumentum deal terms: Verified.** It is an all-stock deal at 4.500 Marvell shares per Lumentum share. Termination fees: Marvell pays $5.8B (change of recommendation or a superior proposal) or **$3.2B** (regulatory failure or the outside date); Lumentum pays $2.9B in matching cases. (EDGAR 8-K, 2026-11-02)
2. **Share-price path around the deal: Verified, with a correction to the short seller.**
   - Closes: Oct 28 $251.65, Oct 29 $218.34, Oct 30 $196.40. The deal was announced Nov 1, and the stock closed at $171.41 on Nov 2. It closed at $133.55 on Nov 5 and $138.47 on Nov 19. (Twelve Data daily series)
   - The 45% fall is right, but **about 22% of it came on Oct 29–30, before the deal was announced.** The announcement day itself was −12.7%. The deal is not the whole "market verdict."
   - The short seller's $115B deal value matches the Oct 28 price (4.5 × $251.65 × 101.7M = about $115B). At $138.47 it is about $63B.
3. **Google warrant: Verified.** 58,970,907 shares at $206.58. Of these, 1,360,867 vest over time in year one. The rest vest in 240 equal tranches, one per $500M of Custom Products revenue from Q3 FY27 through FY33 (= $120B). Exercisable until Aug 18, 2033. (EDGAR 8-K, 2026-08-19)
4. **Cash: Verified.** Cash and cash equivalents were $3,932.8M at 2026-08-01, and there are no separate short-term investments on the balance sheet. (EDGAR 10-Q, 2026-08-28)
5. **Purchase commitments and TSMC: Verified.** Unconditional purchase commitments to foundries and test/assembly partners total $8,518.9M, plus $666.3M of technology/license fees and $351.6M of capex commitments. The risk factor confirms advance payments for wafer capacity, which "we may forfeit" in part if target quantities are missed. (EDGAR 10-Q, 2026-08-28)
6. **Distributor price-claim accrual: Verified for the latest period.** Variable consideration estimates were $777.7M at 2026-08-01, against $713.8M at 2026-01-31. The FY25 figure of $518M was not checked. (EDGAR 10-Q)
7. **CFO change: Verified, which reconciles the two reports.** CFO Willem Meintjes gave notice on June 10, 2026, effective June 15 (5 days). Dan Durn, then a Marvell director and Audit Committee chair and formerly CFO of Adobe, resigned from the board and became CFO on June 15. Both reports are right. (EDGAR 8-K, 2026-06-11)
8. **Board change: Verified, not in either report.** On Nov 11, 2026 the board expanded from 7 to 10 members, adding Donna Morris, Douglas Bettinger (Audit Committee) and Sasan Goodarzi. (EDGAR 8-K, 2026-11-12)
9. **Insider sales: Verified for the latest filings.** The CEO (Matthew Murphy) sold 7,500 shares at $146.54 on 2026-11-16; the Form 4 references a 10b5-1 plan. The Chief Accounting Officer's 11/15 Form 4 is a tax-withholding share disposal (code F, 393 shares at $156.76), not a market sale. The three new directors' Form 4s report no transactions. The short seller's 6-month totals (17 sales, $27.6M, 0 buys) were not fully re-counted. (EDGAR Form 4s, 2026-11-16/17)

**Partly verified or not checked**

10. **TD Cowen downgrade: Partly verified (web).** Several reports say TD Cowen downgraded to Hold and halved its target after the Lumentum deal: Stocktwits, Börse-Global, Goldesel and Stock-World. Goldesel and Stock-World also say Bank of America downgraded. The exact $350→$175 figures were not confirmed. The TipRanks page found describes an older (Sept 2025) TD Cowen downgrade, so don't confuse the two.
11. **Robinhood mean target of $314 "stale": Not checked.** The short seller says it was last updated Nov 7. Treat it as partly pre-deal.
12. **Election (Nov 3) and the 7%/16% fall: Not checked (web-only).** The Nov 5 close was −16.4% on the day ($159.80→$133.55). The cause is not verified.
13. **Lumentum diluted share count (101.7M → 457.7M new Marvell shares): Not checked.** This is from the equity analyst's read of Lumentum's 10-Q.
14. **Receivables +53% y/y and SBC $326M in Q2: Not checked.** These are from the short seller's XBRL work. Receivables were $2,218.4M at 2026-08-01 against $2,186.6M at 2026-01-31 (+1.5% since year-end).
15. **Next earnings date, 2026-12-01: Not checked** beyond Robinhood ("confirmed").
16. **Beta (method): no source check needed.** The bottom-up beta is 2.25 against 1.55 from the industry table, a 0.70 gap, which the analyst flagged. Base value is $103 against $122.
