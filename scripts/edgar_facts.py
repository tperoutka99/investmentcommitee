#!/usr/bin/env python3
"""Pull a company's financial statements from SEC XBRL company facts.

Usage:
  python3 -I scripts/edgar_facts.py <TICKER or CIK> [--out DIR] [--years 5] [--rd-life 3]

Prints a markdown table (last N fiscal years + TTM) and writes <DIR>/<TICKER>_facts.json
with every figure, its XBRL concept, period and filing form, so each number can be cited
"(EDGAR XBRL, <form> <filed>)".

TTM = latest fiscal year + current year-to-date - prior-year year-to-date.
Balance-sheet items are the latest reported instant. Shares outstanding come from the
10-Q/10-K cover page (dei:EntityCommonStockSharesOutstanding), as the DCF skill requires.
"""
import argparse, json, os, sys, time, urllib.request
from datetime import date

UA = os.environ.get("SEC_USER_AGENT") or "IC research tool research@example.com"

FLOWS = {  # name: candidate us-gaap concepts, first match with data wins
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "RevenuesNetOfInterestExpense",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"],
    "cost_of_revenue": ["CostOfRevenue", "CostOfGoodsAndServicesSold"],
    "gross_profit": ["GrossProfit"],
    "rd": ["ResearchAndDevelopmentExpense",
           "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
           "ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost"],
    "operating_income": ["OperatingIncomeLoss"],
    "pretax_income": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                      "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "income_tax": ["IncomeTaxExpenseBenefit"],
    "net_income": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    "interest_expense": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "diluted_shares_avg": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}
STOCKS = {
    "cash": ["CashAndCashEquivalentsAtCarryingValue",
             "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "st_investments": ["ShortTermInvestments", "MarketableSecuritiesCurrent",
                       "AvailableForSaleSecuritiesDebtSecuritiesCurrent"],
    "lt_investments": ["MarketableSecuritiesNoncurrent", "AvailableForSaleSecuritiesDebtSecuritiesNoncurrent",
                       "LongTermInvestments"],
    "debt_current": ["LongTermDebtCurrent", "DebtCurrent", "CommercialPaper",
                     "LongTermDebtAndCapitalLeaseObligationsCurrent", "NotesPayableCurrent",
                     "ShortTermBorrowings"],
    "debt_noncurrent": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations",
                        "LongTermNotesAndLoans", "LongTermNotesPayable"],
    "debt_total": ["LongTermDebt", "DebtInstrumentCarryingAmount"],
    "op_lease_liab": ["OperatingLeaseLiability"],
    "fin_lease_liab": ["FinanceLeaseLiability"],
    "equity": ["StockholdersEquity",
               "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "minority_interest": ["MinorityInterest"],
    "total_assets": ["Assets"],
    "goodwill": ["Goodwill"],
}

def get(url, retries=2):
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:
            if i == retries:
                raise
            time.sleep(1.5)

def resolve(ident):
    """Ticker or CIK -> (cik_int, ticker, name)."""
    if ident.isdigit():
        return int(ident), ident, ""
    data = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
    for v in data.values():
        if v["ticker"].upper() == ident.upper():
            return int(v["cik_str"]), v["ticker"], v["title"]
    sys.exit(f"ticker {ident} not in SEC ticker list")

def dur(s, e):
    return (date.fromisoformat(e) - date.fromisoformat(s)).days

PERIODIC = ("10-K", "10-Q", "10-KT", "20-F", "40-F", "10-K/A", "10-Q/A", "20-F/A")

def units_of(facts, concept, any_form=False):
    """Facts for a concept, from periodic reports only (proxies and 8-Ks can tag the same concept in other scales)."""
    for ns in ("us-gaap", "ifrs-full", "dei"):
        c = facts.get(ns, {}).get(concept)
        if c:
            u = c["units"]
            u = u.get("USD") or u.get("shares") or next(iter(u.values()))
            return u if any_form else [x for x in u if x.get("form") in PERIODIC]
    return None

def flow_series(facts, names, prefer_larger=False):
    """Return (concept, {fy_end: val} annual, ttm dict) for the first concept with data."""
    best = None
    for n in names:
        u = units_of(facts, n)
        if not u:
            continue
        rows = {}
        for x in u:
            if "start" in x:
                k = (x["start"], x["end"])
                if k not in rows or x["filed"] > rows[k]["filed"]:
                    rows[k] = x
        if not rows:
            continue
        latest_end = max(k[1] for k in rows)
        if best is None or latest_end > best[3]:
            best = (n, rows, None, latest_end)
        elif prefer_larger and latest_end == best[3]:
            cur = max((v["val"] for k, v in rows.items() if k[1] == latest_end), default=0)
            old = max((v["val"] for k, v in best[1].items() if k[1] == latest_end), default=0)
            if cur > old:
                best = (n, rows, None, latest_end)
    if not best:
        return None, {}, None, None
    n, rows, _, latest_end = best
    annual = {}
    for (s, e), x in rows.items():
        if 350 <= dur(s, e) <= 380:
            annual[e] = x
    ttm = None
    if annual:
        fy_end = max(annual)
        if fy_end == latest_end:
            x = annual[fy_end]
            ttm = {"val": x["val"], "end": fy_end, "basis": "FY", "form": x.get("form"), "filed": x["filed"]}
        else:
            ytd = [k for k in rows if k[1] == latest_end and dur(*k) > 80 and dur(*k) < 350]
            if ytd:
                y = max(ytd, key=lambda k: dur(*k))
                py = [k for k in rows if abs(dur(k[1], latest_end) - 365) <= 8 and abs(dur(*k) - dur(*y)) <= 8]
                if py:
                    v = annual[fy_end]["val"] + rows[y]["val"] - rows[py[0]]["val"]
                    ttm = {"val": v, "end": latest_end, "basis": f"FY{fy_end[:4]} + YTD to {latest_end} - prior YTD",
                           "form": rows[y].get("form"), "filed": rows[y]["filed"]}
    return n, annual, ttm, ytd_info(rows, latest_end)

def ytd_info(rows, latest_end):
    """Latest year-to-date (longest period ending on the latest date, under a year) and the same period a year earlier."""
    ytd = [k for k in rows if k[1] == latest_end and 80 < dur(*k) < 350]
    if not ytd:
        return None
    y = max(ytd, key=lambda k: dur(*k))
    py = [k for k in rows if abs(dur(k[1], latest_end) - 365) <= 8 and abs(dur(*k) - dur(*y)) <= 8]
    q = [k for k in rows if k[1] == latest_end and 80 < dur(*k) < 100]
    return {"start": y[0], "end": y[1], "val": rows[y]["val"], "form": rows[y].get("form"), "filed": rows[y]["filed"],
            "prior_val": rows[py[0]]["val"] if py else None,
            "quarter_val": rows[q[0]]["val"] if q else None}

def stock_latest(facts, names, at=None):
    best = None
    for n in names:
        u = units_of(facts, n)
        if not u:
            continue
        pts = [x for x in u if "start" not in x and (at is None or x["end"] == at)]
        if not pts:
            continue
        x = max(pts, key=lambda x: (x["end"], x["filed"]))
        if best is None or x["end"] > best[1]["end"]:
            best = (n, x)
    return best

def stock_at(facts, names, end):
    b = stock_latest(facts, names, at=end)
    return b[1]["val"] if b else None

def build(ident, years=5, rd_life=None, out=None):
    cik, ticker, name = resolve(ident)
    raw = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
    cf = json.loads(raw)
    facts = cf["facts"]
    res = {"ticker": ticker, "cik": cik, "name": cf.get("entityName", name), "source": "SEC XBRL company facts",
           "flows": {}, "stocks": {}, "annual": {}}
    fy_ends = set()
    for key, names in FLOWS.items():
        n, annual, ttm, ytd = flow_series(facts, names, prefer_larger=(key == "revenue"))
        res["flows"][key] = {"concept": n, "ttm": ttm, "ytd": ytd,
                             "annual": {e: {"val": x["val"], "form": x.get("form"), "filed": x["filed"]} for e, x in annual.items()}}
        if key == "revenue":
            fy_ends = sorted(annual)[-years:]
    bs = stock_latest(facts, STOCKS["total_assets"])
    bs_date = bs[1]["end"] if bs else None
    res["balance_sheet_date"] = bs_date
    for key, names in STOCKS.items():
        b = stock_latest(facts, names, at=bs_date) or stock_latest(facts, names)
        res["stocks"][key] = None if not b else {"concept": b[0], "val": b[1]["val"], "end": b[1]["end"],
                                                  "form": b[1].get("form"), "filed": b[1]["filed"],
                                                  "stale": b[1]["end"] != bs_date}
    # cover-page shares (sum of classes on the latest date)
    dei = facts.get("dei", {}).get("EntityCommonStockSharesOutstanding", {}).get("units", {}).get("shares", [])
    if dei and bs_date and (date.fromisoformat(bs_date) - date.fromisoformat(max(x["end"] for x in dei))).days > 120:
        dei = []   # cover-page count is stale (older than the latest balance sheet); use the fallback below
    if dei:
        last = max(x["end"] for x in dei)
        latest_filed = max(x["filed"] for x in dei if x["end"] == last)
        res["shares_cover"] = {"val": sum(x["val"] for x in dei if x["end"] == last and x["filed"] == latest_filed),
                               "date": last, "form": next(x.get("form") for x in dei if x["end"] == last)}
    if not res.get("shares_cover"):
        # multi-class filers often report cover shares only by class (not in company facts)
        for concept, label in (("CommonStockSharesOutstanding", "balance-sheet shares outstanding"),
                               ("WeightedAverageNumberOfSharesOutstandingBasic", "basic weighted-average shares, latest period")):
            u = units_of(facts, concept)
            if u:
                x = max(u, key=lambda x: (x["end"], x["filed"]))
                if bs_date and (date.fromisoformat(bs_date) - date.fromisoformat(x["end"])).days > 120:
                    continue   # stale
                res["shares_cover"] = {"val": x["val"], "date": x["end"], "form": x.get("form"),
                                       "fallback": f"{label} ({concept}); not the cover page: use the filing's cover count if it differs"}
                break
    # annual table with derived ratios
    for e in fy_ends:
        row = {k: v["annual"].get(e, {}).get("val") for k, v in res["flows"].items()}
        row["cash"] = stock_at(facts, STOCKS["cash"], e)
        row["st_investments"] = stock_at(facts, STOCKS["st_investments"], e)
        row["equity"] = stock_at(facts, STOCKS["equity"], e)
        res["annual"][e] = row
    # research asset (DCF skill Step 0) from annual R&D
    if rd_life:
        rd = res["flows"]["rd"]["annual"]
        ends = sorted(rd)
        if len(ends) >= rd_life:
            vals = [rd[e]["val"] for e in ends][::-1]  # newest first
            asset = sum(vals[n] * (1 - n / rd_life) for n in range(rd_life))
            amort = sum(vals[n] / rd_life for n in range(1, rd_life + 1) if n < len(vals))
            res["research_asset"] = {"life": rd_life, "asset": asset, "amortization": amort,
                                     "current_rd": vals[0], "ebit_adjustment": vals[0] - amort,
                                     "fiscal_year": ends[-1]}
        else:
            res["research_asset"] = {"life": rd_life, "note": f"only {len(ends)} years of R&D; not assessed"}
    if out:
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, f"{ticker}_facts.json"), "w") as f:
            json.dump(res, f, indent=1)
    return res

def fmt(v, pct=False):
    if v is None:
        return "n/a"
    return f"{v*100:.1f}%" if pct else f"{v/1e6:,.0f}"

def table(res):
    a = res["annual"]
    ends = sorted(a)
    t = {k: (v["ttm"] or {}).get("val") for k, v in res["flows"].items()}
    cols = [f"FY{e[:4]}" for e in ends] + ["TTM"]
    rows = [a[e] for e in ends] + [t]
    y = res["flows"]["revenue"].get("ytd")
    if y:
        cur = {k: (v.get("ytd") or {}).get("val") if (v.get("ytd") or {}).get("end") == y["end"] else None for k, v in res["flows"].items()}
        pri = {k: (v.get("ytd") or {}).get("prior_val") if (v.get("ytd") or {}).get("end") == y["end"] else None for k, v in res["flows"].items()}
        cols += [f"YTD to {y['end']}", "Prior-year YTD"]
        rows += [cur, pri]
    def ratio(r, n, d):
        return (r.get(n) / r.get(d)) if r.get(n) is not None and r.get(d) else None
    lines = [f"**{res['name']} ({res['ticker']})**, $M, SEC XBRL company facts",
             "| | " + " | ".join(cols) + " |", "|---" * (len(cols) + 1) + "|"]
    def line(label, f):
        lines.append(f"| {label} | " + " | ".join(f(r) for r in rows) + " |")
    line("Revenue", lambda r: fmt(r.get("revenue")))
    prev = [None] + rows[:-1]
    nfy = len(ends)
    def growth(i):
        r = rows[i]
        if i < nfy and i > 0 and r.get("revenue") and rows[i-1].get("revenue"):
            return f"{(r['revenue']/rows[i-1]['revenue']-1)*100:.1f}%"
        if i == nfy + 1 and r.get("revenue") and rows[i+1].get("revenue"):
            return f"{(r['revenue']/rows[i+1]['revenue']-1)*100:.1f}% y/y"
        return "n/a"
    lines.append("| Revenue growth | " + " | ".join(growth(i) for i in range(len(rows))) + " |")
    line("Gross margin", lambda r: fmt(ratio(r, "gross_profit", "revenue") if r.get("gross_profit") else
                                       ((r["revenue"] - r["cost_of_revenue"]) / r["revenue"] if r.get("revenue") and r.get("cost_of_revenue") else None), True))
    line("Operating income", lambda r: fmt(r.get("operating_income")))
    line("Operating margin", lambda r: fmt(ratio(r, "operating_income", "revenue"), True))
    line("Net income", lambda r: fmt(r.get("net_income")))
    line("R&D", lambda r: fmt(r.get("rd")))
    line("SBC", lambda r: fmt(r.get("sbc")))
    line("Operating cash flow", lambda r: fmt(r.get("ocf")))
    line("Capex", lambda r: fmt(r.get("capex")))
    line("FCF", lambda r: fmt(r["ocf"] - r["capex"]) if r.get("ocf") is not None and r.get("capex") is not None else "n/a")
    line("FCF margin", lambda r: fmt((r["ocf"] - r["capex"]) / r["revenue"], True) if r.get("ocf") is not None and r.get("capex") is not None and r.get("revenue") else "n/a")
    line("Effective tax rate", lambda r: fmt(ratio(r, "income_tax", "pretax_income"), True))
    line("Diluted shares (M)", lambda r: fmt(r.get("diluted_shares_avg")))
    lines.append("")
    ttm_basis = (res["flows"]["revenue"]["ttm"] or {}).get("basis")
    lines.append("TTM basis: " + (ttm_basis or "not available: no annual XBRL figures (new filer). Take annual history from the 10-K or IPO prospectus (424B4) text."))
    s = res["stocks"]
    lines.append(f"Latest balance sheet ({res.get('balance_sheet_date')}, $M): " + ", ".join(
        f"{k} {fmt(v['val'])} ({v['concept']})" for k, v in s.items() if v and not v["stale"]))
    stale = [f"{k} {fmt(v['val'])} as of {v['end']} ({v['concept']})" for k, v in s.items() if v and v["stale"]]
    if stale:
        lines.append("Older-dated (not on the latest balance sheet; read the filing instead): " + ", ".join(stale))
    if res.get("shares_cover"):
        sc = res["shares_cover"]
        lines.append(f"Cover-page shares: {sc['val']/1e6:,.1f}M as of {sc['date']} ({sc['form']})" if not sc.get("fallback")
                     else f"Shares: {sc['val']/1e6:,.1f}M as of {sc['date']} = {sc['fallback']}")
    if res.get("research_asset"):
        ra = res["research_asset"]
        if "asset" in ra:
            lines.append(f"Research asset ({ra['life']}-yr life, FY{ra['fiscal_year'][:4]}): {fmt(ra['asset'])}; "
                         f"EBIT adjustment +{fmt(ra['ebit_adjustment'])} (R&D {fmt(ra['current_rd'])} - amortization {fmt(ra['amortization'])})")
        else:
            lines.append("Research asset: " + ra["note"])
    lines.append("Check every figure against the filing before relying on it: XBRL concept choice can differ by company.")
    return "\n".join(lines)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("ident")
    ap.add_argument("--out")
    ap.add_argument("--years", type=int, default=5)
    ap.add_argument("--rd-life", type=int)
    a = ap.parse_args()
    r = build(a.ident, a.years, a.rd_life, a.out)
    print(table(r))
