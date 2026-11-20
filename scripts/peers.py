#!/usr/bin/env python3
"""Comps table and bottom-up beta for the equity analyst.

Usage:
  python3 -I scripts/peers.py --peers CRM,ADSK,HUBS,MSFT --prices CRM=240.1,ADSK=301.2,... \
      --target-de 0.078 --target-tax 0.21 [--target ADBE --target-price 221.63] [--out DIR]

--prices   today's price per peer (Robinhood get_equity_quotes or Twelve Data get_quote).
Prices for the beta: by default the script downloads 2 years of weekly closes for SPY and each
           peer from Yahoo Finance's chart data (query1.finance.yahoo.com) and saves them to
           <out>/closes_yahoo.json. Any symbol Yahoo fails on is reported; supply it with
           --closes, a JSON file keyed by symbol (Twelve Data get_time_series values list, or a
           plain list of closes newest-first), which takes priority over Yahoo. --no-beta skips it.
--target-de / --target-tax   the valued company's debt-to-equity (market) and marginal tax rate,
           used to relever the median unlevered beta.

Financials come from SEC XBRL company facts via edgar_facts.py (TTM). Each peer's D/E uses
its XBRL debt and market cap at --prices; tax = TTM tax / pretax income, clamped to 0-35%.
Beta = covariance of weekly returns with SPY / variance of SPY's weekly returns.
"""
import argparse, json, os, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edgar_facts as ef

def val(r, k):
    f = r["flows"].get(k) or {}
    t = f.get("ttm")
    return t["val"] if t else None

def stock(r, k):
    s = r["stocks"].get(k)
    return s["val"] if s and not s["stale"] else 0.0

def debt_of(r):
    d = stock(r, "debt_total") or stock(r, "debt_noncurrent")
    cur = stock(r, "debt_current")
    # LongTermDebt (debt_total) usually already includes the current portion; noncurrent does not
    if r["stocks"].get("debt_total") and not r["stocks"]["debt_total"]["stale"]:
        concept = r["stocks"]["debt_total"]["concept"]
        return d if concept == "LongTermDebt" and cur and cur < d else d + cur
    return d + cur

def yahoo_closes(sym, weeks=105):
    """2 years of weekly closes from Yahoo's chart endpoint, as {YYYY-MM-DD: close}."""
    import urllib.request
    from datetime import datetime, timezone
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=2y&interval=1wk"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for i in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)["chart"]["result"][0]
            break
        except Exception:
            if i:
                raise
    pts = {datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d"): c
           for ts, c in zip(d["timestamp"], d["indicators"]["quote"][0]["close"]) if c is not None}
    keep = sorted(pts)[-weeks:]
    return {k: pts[k] for k in keep}

def closes_of(x):
    if isinstance(x, dict) and "values" in x:
        x = x["values"]
    if x and isinstance(x[0], dict):
        pts = sorted(((p["datetime"], float(p["close"])) for p in x), reverse=True)
        return dict(pts)
    return {i: float(c) for i, c in enumerate(x)}  # positional, newest first

def beta(peer, spy):
    common = sorted(set(peer) & set(spy), reverse=True)
    if isinstance(common[0], int):
        common = sorted(common)
    p = [peer[k] for k in common]; s = [spy[k] for k in common]
    rp = [p[i] / p[i + 1] - 1 for i in range(len(p) - 1)]
    rs = [s[i] / s[i + 1] - 1 for i in range(len(s) - 1)]
    mp, ms = statistics.fmean(rp), statistics.fmean(rs)
    cov = sum((a - mp) * (b - ms) for a, b in zip(rp, rs)) / (len(rp) - 1)
    var = sum((b - ms) ** 2 for b in rs) / (len(rs) - 1)
    return cov / var, len(rp)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--peers", required=True)
    ap.add_argument("--prices", required=True)
    ap.add_argument("--closes")
    ap.add_argument("--no-beta", action="store_true")
    ap.add_argument("--target-de", type=float)
    ap.add_argument("--target-tax", type=float, default=0.21)
    ap.add_argument("--target")
    ap.add_argument("--target-price", type=float)
    ap.add_argument("--min-weeks", type=int, default=100)
    ap.add_argument("--shares", help="override shares, e.g. SPCX=13581.06,META=2520 (millions, from filing cover pages)")
    ap.add_argument("--out")
    a = ap.parse_args()
    prices = {k: float(v) for k, v in (x.split("=") for x in a.prices.split(","))}
    tickers = [t.strip().upper() for t in a.peers.split(",")]
    if a.target:
        prices[a.target.upper()] = a.target_price
    closes, src = None, {}
    if not a.no_beta:
        given = json.load(open(a.closes)) if a.closes else {}
        closes, fetched, failed = {}, {}, []
        for s in ["SPY"] + tickers:
            if s in given:
                closes[s] = closes_of(given[s]); src[s] = "file"
                continue
            try:
                fetched[s] = yahoo_closes(s); closes[s] = fetched[s]; src[s] = "Yahoo chart"
            except Exception as e:
                failed.append(f"{s} ({type(e).__name__})")
        if a.out and fetched:
            os.makedirs(a.out, exist_ok=True)
            json.dump(fetched, open(os.path.join(a.out, "closes_yahoo.json"), "w"))
        if failed:
            print("Price history not downloaded for: " + ", ".join(failed) +
                  ". Supply these with --closes (Twelve Data get_time_series) and rerun.")
        if "SPY" not in closes:
            print("No SPY prices: beta skipped.")
            closes = None
    spy = closes["SPY"] if closes else None
    overrides = {k.upper(): float(v) for k, v in (x.split("=") for x in a.shares.split(","))} if a.shares else {}
    notes = []
    rows = []
    for t in ([a.target.upper()] if a.target else []) + tickers:
        r = ef.build(t)
        sh = (r.get("shares_cover") or {}).get("val")
        if overrides.get(t):
            sh = overrides[t] * 1e6
        elif (r.get("shares_cover") or {}).get("fallback"):
            notes.append(f"{t}: shares = {r['shares_cover']['fallback']}")
        px = prices.get(t)
        mcap = px * sh if px and sh else None
        cash = stock(r, "cash") + stock(r, "st_investments")
        debt = debt_of(r)
        ev = mcap + debt - cash if mcap else None
        rev, ebit, ni = val(r, "revenue"), val(r, "operating_income"), val(r, "net_income")
        ocf, capex = val(r, "ocf"), val(r, "capex")
        fcf = ocf - capex if ocf is not None and capex is not None else None
        tax, pti = val(r, "income_tax"), val(r, "pretax_income")
        t_rate = min(max(tax / pti, 0.0), 0.35) if tax is not None and pti and pti > 0 else 0.0
        row = dict(ticker=t, price=px, shares_m=sh / 1e6 if sh else None, mcap_m=mcap / 1e6 if mcap else None,
                   debt_m=debt / 1e6, cash_m=cash / 1e6, ev_m=ev / 1e6 if ev else None,
                   ev_sales=ev / rev if ev and rev else None,
                   ev_ebit=ev / ebit if ev and ebit and ebit > 0 else None,
                   pe=mcap / ni if mcap and ni and ni > 0 else None,
                   fcf_yield=fcf / mcap if mcap and fcf is not None else None,
                   de=debt / mcap if mcap else None, tax=t_rate,
                   pb=mcap / stock(r, "equity") if mcap and stock(r, "equity") else None,
                   roe=ni / stock(r, "equity") if ni is not None and stock(r, "equity") else None,
                   ttm_basis=(r["flows"]["revenue"]["ttm"] or {}).get("basis"),
                   bs_date=r.get("balance_sheet_date"), is_target=(t == (a.target or "").upper()))
        if closes and t in closes and not row["is_target"]:
            b, n = beta(closes[t], spy)
            row.update(beta_raw=b, weeks=n, beta_unlev=b / (1 + (1 - t_rate) * row["de"]) if row["de"] is not None else None)
        rows.append(row)
    f = lambda v, d=1, s="x": "n/m" if v is None else f"{v:.{d}f}{s}"
    print("**Comps** (TTM; financials SEC XBRL company facts; prices as given)")
    print("For banks, brokers and insurers use P/E, P/B and ROE: EV, EV/Sales, EV/EBIT and D/E mix customer funding with corporate debt.")
    print("| | EV/Sales | EV/EBIT | P/E | P/B | ROE | FCF yield | D/E | Tax | Balance sheet | TTM basis |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        name = f"**{r['ticker']}**" if r["is_target"] else r["ticker"]
        print(f"| {name} | {f(r['ev_sales'])} | {f(r['ev_ebit'])} | {f(r['pe'])} | {f(r['pb'])} | "
              f"{f(r['roe']*100 if r['roe'] is not None else None, 1, '%')} | "
              f"{f(r['fcf_yield']*100 if r['fcf_yield'] is not None else None, 1, '%')} | {f(r['de'], 3, '')} | "
              f"{r['tax']*100:.0f}% | {r['bs_date']} | {r['ttm_basis'] or 'no TTM (new filer)'} |")
    for n in notes:
        print("Note: " + n)
    out = {"comps": rows}
    if closes:
        used = [r for r in rows if r.get("beta_unlev") is not None and r["weeks"] >= a.min_weeks]
        short = [r for r in rows if r.get("weeks") is not None and r["weeks"] < a.min_weeks]
        srcs = sorted(set(src.values()))
        print(f"\n**Bottom-up beta** (weekly returns vs SPY; prices: {', '.join(srcs)}"
              + (f", downloaded {__import__('datetime').date.today()}" if "Yahoo chart" in srcs else "") + ")")
        print("| Peer | Weeks | Raw beta | D/E | Tax | Unlevered |")
        print("|---|---|---|---|---|---|")
        for r in rows:
            if r.get("beta_raw") is not None:
                flag = "" if r["weeks"] >= a.min_weeks else " (excluded: under 2 years)"
                print(f"| {r['ticker']}{flag} | {r['weeks']} | {r['beta_raw']:.2f} | {f(r['de'], 3, '')} | {r['tax']*100:.0f}% | {f(r['beta_unlev'], 2, '')} |")
        if len(used) >= 3:
            med = statistics.median(r["beta_unlev"] for r in used)
            out["median_unlevered"] = med
            line = f"Median unlevered beta {med:.2f} from {len(used)} peers"
            if a.target_de is not None:
                lev = med * (1 + (1 - a.target_tax) * a.target_de)
                out["relevered"] = lev
                line += f"; relevered at D/E {a.target_de:.3f}, tax {a.target_tax*100:.0f}%: **{lev:.2f}**"
            print(line)
        else:
            out["median_unlevered"] = None
            print(f"Only {len(used)} peers have {a.min_weeks}+ weeks of prices: use the industry-table beta in the cases (agent rule).")
        if short:
            print("Excluded for short history: " + ", ".join(r["ticker"] for r in short))
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump(out, open(os.path.join(a.out, "peers_out.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
