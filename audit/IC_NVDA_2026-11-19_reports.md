# IC Reports: NVDA (NVIDIA Corporation), 2026-11-19
Audit trail for IC_NVDA_2026-11-19.md. Skill version: investment-committee v0.3. Each report is verbatim as returned by its agent.

---

## 1. Macro strategist

**1. Regime:** Growth is strong (Q3 real GDP 3.4% annualized) and inflation is speeding up again. The Fed held at 3.75–4.00% on Oct 28, but two members dissented in favor of a hike. Futures price a December hike at more than 90%.

**2. Data table**

| Indicator | Latest | Prior | As of | Source |
|---|---|---|---|---|
| Effective fed funds (monthly) | 3.88% | 3.75% | Oct / Sep 2026 | AV FEDERAL_FUNDS_RATE |
| 10Y Treasury | 5.10% | 5.15% (4.12% a year ago) | 11/17 vs 10/19 | AV TREASURY_YIELD |
| 2Y Treasury | 4.80% | 4.77% | 11/18 vs 10/19 | FRED DGS2 (fallback) |
| CPI YoY (NSA index, my calc) | 3.7% (3-month annualized SA: 5.7%) | 3.4% | Sep / Aug 2026 | FRED CPIAUCNS / CPIAUCSL (fallback) |
| Unemployment | 4.1% | 4.2% | Oct / Sep | BLS release, FRED UNRATE (fallback) |
| Nonfarm payrolls | +165k | +60k (revised) | Oct / Sep | BLS release (fallback) |
| Real GDP (annualized, my calc) | 3.4% | 2.2% | Q3 / Q2 2026 | FRED GDPC1 (fallback) |
| Retail sales m/m | +0.2% | +0.8% | Oct / Sep | FRED RSXFS (fallback) |
| Dollar (UUP) | 29.64 | 29.00 | 11/19 vs 10/19 | Twelve Data |

I can't compute October CPI YoY: BLS did not collect October 2025 data.

**3. Sensitivity**
- **Rates:** Most of NVDA's value sits in far-future AI cash flows, so a 10Y above 5% and a hiking cycle push the multiple down. A second channel is customer financing: higher borrowing costs raise the price of debt-funded data-center builds. How much of that demand is debt-funded is not assessed (no data).
- **Growth:** Demand comes from corporate and hyperscaler capex, not consumers. The Fed itself says capital investment is "robust," which supports demand.
- **Inflation:** Mostly hurts through rates, not costs. Input-cost and pricing-power effects: not assessed (no data).
- **Dollar:** UUP is up about 2% in a month, which makes USD-priced hardware dearer for foreign buyers. Revenue mix by geography: not assessed (no data).
- **Company debt structure and borrowing exposure:** not assessed (no data).

**4. Call: Headwind, Medium confidence.** Rising policy rates, a 10Y above 5%, inflation re-accelerating and a firmer dollar all pressure a long-duration growth multiple, even though strong capex growth supports demand.

**5. Next 30 days**
- Nov 25: Q3 GDP second estimate and October PCE (BEA)
- Dec 4: November jobs report (BLS)
- Dec 8–9: FOMC meeting, with projections and dot plot
- Dec 10: November CPI (BLS)
- Dec 16: November retail sales (Census)

**6. What would flip the call:** the 10Y closing below 4.70% (its August level) for 5 straight sessions. That would mean the market has stopped pricing the hiking cycle.

**Sources:** the [Oct 28 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm), the [FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), and the BLS [CPI](https://www.bls.gov/news.release/cpi.nr0.htm) and [jobs](https://www.bls.gov/news.release/empsit.nr0.htm) releases. The rate-path figure comes from a single non-official source, [Trading Economics, Nov 17](https://tradingeconomics.com/united-states/implied-rates/news/602003), which also prices three hikes by July 2027. Release dates are from the [BEA](https://www.bea.gov/news/schedule) and [Census](https://www.census.gov/retail/release_schedule.html) schedules.

Tool access: Alpha Vantage hit its 25-calls-per-day limit after the FEDERAL_FUNDS_RATE and 10Y TREASURY_YIELD calls. The 2Y TREASURY_YIELD, CPI, UNEMPLOYMENT, NONFARM_PAYROLL, REAL_GDP and RETAIL_SALES calls all failed, including on retry. In their place I used St. Louis Fed FRED CSVs (DGS2, CPIAUCNS, CPIAUCSL, UNRATE, PAYEMS, GDPC1, RSXFS), checked against the BLS release pages. The BLS API was also over its daily limit. Twelve Data (UUP) worked.

---

## 2. Equity analyst + valuation

**NVDA equity analyst report, as of 2026-11-19**

**1. Business**
NVIDIA sells accelerated-computing platforms: GPUs, CPUs (Vera), networking and full rack systems such as Vera Rubin NVL72. Most of these go to hyperscalers, AI labs and sovereign buyers. Data Center was $107.6B of Q3 FY27's $115.8B revenue (93%) (IR). Results are driven by AI infrastructure capex budgets, product cadence and supply capacity (CoWoS, substrates).

**2. Quality table** (FMP statements; ROIC = after-tax operating income / operating invested capital, which excludes cash and investments)

| | FY23 | FY24 | FY25 | FY26 | TTM Q3 FY27 |
|---|---|---|---|---|---|
| Revenue growth | 0% | 126% | 114% | 65% | Q3 +103% YoY |
| Gross margin | 56.9% | 72.7% | 75.0% | 71.1% | 74.9% |
| Operating margin | 15.7% | 54.1% | 62.4% | 60.4% | 66.1% |
| FCF margin | 14.1% | 44.4% | 46.6% | 44.8% | 41.1% |
| ROIC | 21% | 109% | 164% | 132% | 141% (109% with R&D capitalized) |
| Net debt/EBITDA | -0.22x | -0.43x | -0.40x | -0.38x | -0.24x |
| Diluted share change | -1.1% | -0.5% | -0.5% | -1.2% | Q3 diluted 24.19B vs FY26 24.51B |

**3. Management**
- **CEO resignation.** Jensen Huang resigned on Nov 12, effective immediately, and the release gave no reason. CFO Colette Kress is interim CEO and stays CFO; Harvey Jones is the first Board Chair. This followed a Nov 8 board statement on reports that Huang was "the target of a foreign intelligence effort", with an independent investigation launched. https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/ (IR); https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors (IR)
- **Q4 guidance.** Revenue $130B ±3% (the quarter has an extra week), with no China Data Center revenue assumed. Gross margin is guided down to 71–72% from 74.8%. Kress: "Vera Rubin is off to an explosive start." https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027 (IR)
- **Capital return.** The buyback authorization rose by $150B, leaving $227.3B remaining (6.5% of market cap). $28.1B was returned in Q3. (same link, IR)

**4. Pending deals and financing**
- **Hugging Face acquisition:** $12.93B, announced Sep 3, 2026. Funding and close timing not disclosed (company blog, blogs.nvidia.com). I modeled it as cash.
- **Meta equity offering:** $3B investment, subject to closing conditions; status not stated (IR, Oct 27). I modeled it as cash.
- **Supply-chain prepayments:** Amkor about $3B, KYEC $1.1B, and "multibillion" amounts for IBIDEN and SPIL (IR, Oct 21 and Nov 17). I left these out of the valuation because they are operating advances with mostly unspecified size.
- **$25B senior notes:** already closed in Q2 and on the balance sheet.

The two deals I included cut value by $0.66/share. The IR RSS feed only covered Oct 21 to Nov 19, so the 12-month scan may be incomplete.

**5. Valuation**
- **Discount rate.** Risk-free rate is **5.04% (10Y, 2026-11-19)**. Two inputs are my own assumptions, not data: ERP 4.5% and unlevered beta 1.40. That gives a WACC of 11.3%, tapering to 9.3%. Terminal growth is 4%, terminal ROC is 20%, and the terminal year is taxed at 21%.
- **Reverse DCF.** At a 50% target margin, $145.98 implies only **~11.9% a year revenue growth for 5 years** (year-5 revenue $636B). If revenue instead follows the consensus path (FY27–31 growth of 72%, 29%, 17%, 12%), the price implies operating margin collapsing to **~28%**.

| Scenario | Value/share | Main drivers |
|---|---|---|
| Bear | **$51** | Revenue +30% in year 1, then -30% and -15% (capex bust); margin falls to 35%; sales-to-capital 2.0 |
| Base | **$146** | Revenue +60%, +15%, +5%, then flat; margin falls to 50%; sales-to-capital 2.5 |
| Bull | **$300** | Revenue +80%, +30%, +15%, +10% (near consensus); margin 60%; sales-to-capital 3.0 |

- Terminal value is 45–59% of operating value across scenarios.
- Growth-invariance test: base value moves from $131 to $146 as terminal growth goes from 2% to 4%, so the model assumes excess returns.
- Imputed ROC stays above 100% in the base case, well above the method's ~40% flag. That matches NVDA's history, but it is an aggressive assumption to carry for a decade.

**Comps** (peer prices from Twelve Data on 11/19; financials from stockanalysis.com (web) dated 11/6–11/18, rescaled to those prices)

| | EV/Sales | EV/EBIT | P/E TTM | FCF yield |
|---|---|---|---|---|
| **NVDA** | 9.6x | 14.5x | 15.7x | 4.2% |
| AMD | 17.5x | 98x | 106x | 0.9% |
| AVGO | 19.0x | 39x | 44x | 2.4% |
| MRVL | 13.0x | 77x | 46x | 1.4% |
| QCOM | 4.2x | 20x | 13x | 5.0% |

**6. Bull thesis**
1. **The price implies a steep slowdown.** It requires only ~12% a year growth, while Q3 grew 103% and the Q4 guide annualizes to $520B against $362B of TTM revenue.
2. **Returns are exceptional.** ROIC is 141% (109% with R&D capitalized), FCF margin is 41%, and TTM FCF is $148.7B.
3. **It is cheap against peers and consensus.** It trades at 14.5x EV/EBIT versus 20–98x for peers and 8.8x the FY28 consensus EPS of $16.56. It also has $59.6B of net cash, $65.5B of non-marketable investments, and $227B of buyback capacity.

**7. Key numbers** (FMP quote and statements, 2026-11-19 close; balance sheet as of 2026-10-25)
- Price: $145.98 (-3.3% on the day; 52-week high $243.37)
- Market cap: $3,518B
- Shares: 24.10B basic (implied by market cap), 24.19B diluted. Filing cover-page share count not assessed (no data).
- Debt including leases: $38.1B. Cash and short-term investments: $97.7B. Net debt: **-$59.6B** (net cash); pro forma for the two pending deals, -$43.7B.
- EV: **$3,459B** ($3,393B excluding non-marketable investments).

Tool access: Alpha Vantage TREASURY_YIELD hit its rate limit twice (the second time the daily cap), so I used FMP economics treasury-rates for the 10Y. The Hugging Face deal terms came from NVIDIA's own blog, not an IR page.

---

## 3. Short seller (red team)

**NVDA short-seller report, 2026-11-19**

**1. Top 3 bear points**
1. **NVIDIA is paying for its own demand.** It has up to $118B of guarantees outstanding. $105B of that backs OpenAI's leases at the Ohio PORTS campus. It also has $32B of neocloud agreements, and total commitments of $518B. Supply commitments alone rose from $279B to $390B in one quarter (8-K 11/17/26, EDGAR). The 10-Q filed 8/26/26 added two lines: "if AI clouds do not successfully sell committed capacity… we have agreed to purchase that capacity", and AI clouds and model makers "lack… investment-grade financing capacity" (EDGAR). NVIDIA now gives some customers up to one year to pay, and days sales outstanding (DSO) rose from 45 to 64 in two quarters. Long-term investments went from $8.2B to $65.5B in a year (FMP). If customer credit breaks, lost revenue and guarantee payments arrive together.
2. **Governance and export-control risk.** Huang resigned and the 8-K gave no reason (8-K 11/12/26, EDGAR). The DOJ and Commerce have confirmed a criminal export probe of Megaspeed (web). The NYT reports that General Counsel Teter contacted the Commerce export agency (BIS) about that probe (web only). No 8-K or 10-Q says anything about this yet, and the Q3 10-Q has not been filed. Teter filed a Form 144 today to sell 30,000 shares (EDGAR). There is also a securities class action, *Kistenmacher v. NVIDIA*, covering purchases from 10/9/25 to 11/8/26 (Twelve Data).
3. **Earnings quality is peaking.** Nine-month GAAP net income includes $25.5B of equity-security gains, and Q3 also took a $1.8B impairment (8-K 11/17/26, EDGAR). TTM free cash flow is only 0.66x net income. Gross margin is guided down from 74.8% to 71–72%. The 25% tariff on H200 sales to China is not being passed on to customers (10-Q, EDGAR).

**2. The weakest assumption:** the 50% operating margin held for a decade. It should be about 35%. Gross margin is already guided down about 3 points. The guarantees, the promise to buy unsold capacity and the long payment terms act like price cuts that reported margins do not show yet. Custom chips from AVGO and AMD cap pricing. I rebuilt the analyst's model (it gives $153 against his $146). At 35% margin it gives about $114.

**3. Red flag checklist**
- **Insiders (6 months): Watch.** No open-market buys. 6.23M shares ($1.38B) sold, $1.35B of it by director Mark Stevens. Teter filed a Form 144 today (EDGAR Form 4/144).
- **Dilution: Clear.** Diluted shares are down 3.5% since FY23. Stock-based comp is 2.1% of revenue.
- **Receivables vs revenue: Red.** Receivables grew 143% YoY against revenue growth of 103%.
- **Inventory vs revenue: Watch.** Inventory grew 26% QoQ against revenue growth of 20%.
- **Guidance cuts: Watch.** The revenue guide went up, but the gross-margin guide went down.
- **Downgrades: Red.** Nine downgrades on Nov 11–12, including Bernstein, Evercore, KeyBanc and Oppenheimer. The average price target fell to $229.6 last month from $281 last quarter (FMP).
- **News trend: Red.** 7 of the 10 latest items are class-action notices (Twelve Data).
- **New risk factors: Red.** These are new in the 8/26 10-Q versus the 5/20 10-Q: guarantees and credit support, the promise to buy unsold capacity, the OpenAI guarantee, financing-platform memoranda of understanding, $33.5B of debt, and a Chinese regulator inquiry into the Mellanox commitments (EDGAR).
- **Institutional: Watch (web).** In Q3 13F filings, Renaissance sold nearly all its stake and Soros cut 19%.

**4. Where the macro call is wrong:** the direction is right, but the channel is wrong. At 14.5x EV/EBIT, NVDA's value is not mostly far-off cash flows, so the rates-hit-the-multiple argument is overstated. The real channel is credit. The macro report marked debt-funded demand "not assessed", but EDGAR shows NVIDIA itself backing about $150B of it. Rate hikes with a 10Y above 5% hit customer financing first, then NVIDIA's guarantees. The dollar point barely matters, because the Q4 guide already excludes China data-center revenue.

**5. Bear case price: about $68.** I used the analyst's model structure with these inputs:
- **Revenue:** +45% over the next 12 months (about the Q4 run-rate), then −25% and −10% as financing dries up, then flat, then +3%.
- **Margin and capital:** margin falls to 35%, and sales-to-capital is 2.0.
- **Adjustments:** a 30% haircut on the $65.5B of private stakes, and a $30B expected loss on the guarantees.

That gives $65–73. Cross-check: trough revenue of about $355B at 35% margin and 79% after tax is about $98B of after-tax operating profit. At 16x that, plus about $105B of cash and investments, the stock is worth about $69.

**6. Thesis strength: 3/5.** At 15.7x trailing earnings with net cash and Q4 guided up 12% QoQ, valuation alone does not kill the bull case. It dies only if the loop of NVIDIA financing its own customers breaks. That is plausible within 12–24 months but has not happened yet.

Note: the Q3 FY27 10-Q is not filed yet, so the two 10-Qs compared are those filed 5/20/26 and 8/26/26.

Tool access: Alpha Vantage INSIDER_TRANSACTIONS and INSTITUTIONAL_HOLDINGS failed twice on the rate limit. I used 38 Form 4s and a Form 144 from EDGAR for insiders, and WebSearch for institutions. Two web pages would not fetch (cryptobriefing, tech-insider), so they are not used.

---

## 4. Data flags (orchestrator sanity check and verification)

**Price check:** fresh FMP quote (2026-11-19) shows price $145.98 and market cap $3,518B. Both match the reports. No flag. (The quote also shows a 52-week low of $145.71, set today, and a 50-day average of $210.30.)

**Items and verification status:**
1. **CEO resignation.** Equity analyst (IR) and short seller (EDGAR) both report it.
   **Verified:** NVIDIA 8-K filed 11/12/26, Item 5.02. On 11/11/26 the board accepted Jen-Hsun Huang's resignation as President, CEO and director, effective immediately. Colette M. Kress was appointed interim CEO and remains CFO while the board searches for a new CEO. Harvey C. Jones was appointed Chair. The 8-K gives no reason for the resignation. The Nov 8 board statement about a "foreign intelligence effort" (equity analyst, IR) is not in any 8-K; NVIDIA has filed no 8-K since Oct 1 other than 11/12 and 11/17. Not checked further.
2. **Guarantees and commitments (short seller's #1 point).**
   **Verified** (8-K filed 11/17/26, CFO commentary exhibit):
   - Maximum gross guarantee exposure is $118.0B: $105.0B SB Energy credit support, $9.5B power and systems credit support, and $3.5B land, power and shell guarantees for neoclouds.
   - The $105B backs 20-year leases to OpenAI at the PORTS-Pike campus in Ohio. It takes effect building by building, with the first expected in fiscal 2029, builds to that maximum over time, then declines as OpenAI pays its leases.
   - Neocloud agreements total $32B. They take effect only if the neoclouds secure financing and the capacity is deployed and accepted by NVIDIA.
   - Total commitments are $518B. Supply commitments rose from $279B to $390B, primarily for multi-year memory supply.
   - The same document says neoclouds and frontier labs are "growing faster than their balance sheets and long-term credit profiles can support."
3. **Receivables and payment terms.** The short seller says NVIDIA gives some customers up to one year to pay.
   **Partly verified** (8-K 11/17/26, CFO commentary): receivables are $81.0B with DSO of 64 days, up from 60 sequentially. NVIDIA attributes this to Rubin shipment timing and to extended payment terms on large multi-quarter agreements with certain **investment-grade** customers. The "up to one year" figure was not found in this document.
4. **Cash balance / net cash.** The equity analyst reports cash and short-term investments of $97.7B and net cash of $59.6B (FMP).
   **Contradicted on definition** (8-K 11/17/26, CFO commentary): cash, cash equivalents and marketable debt securities were $53.5B at quarter end, down from $56.6B a quarter ago. Against the analyst's $38.1B of debt including leases, that is about $15.4B of net cash on this definition. The FMP figure likely includes other investments, such as publicly held equity securities, which are not cash. Treat the $59.6B net cash figure as overstated.
5. **Equity-security gains and impairment (short seller's #3 point).**
   **Verified in part** (8-K 11/17/26, CFO commentary): Q3 net gains from equity securities were $1.8B, made up of $2.8B of gains on publicly held securities and a $1.0B net loss on non-marketable securities, including a $1.8B impairment. The nine-month $25.5B gain figure was not checked.
6. **Export probe and General Counsel contact with BIS (part of the short seller's #2 point).** This rests only on web sources.
   **Not found:** no mention of Megaspeed or export matters in the 11/12/26 8-K, the 11/17/26 earnings release, or the CFO commentary. The Q3 10-Q has not been filed. Not contradicted.
7. **Hugging Face acquisition.** Verified as pending: the 11/17/26 CFO commentary refers to "our pending acquisition of Hugging Face." Price was not checked.
