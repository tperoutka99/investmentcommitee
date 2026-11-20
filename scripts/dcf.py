#!/usr/bin/env python3
"""Damodaran DCF engine (the damodaran-dcf skill's Steps 3-7 and 9, plus its reverse-DCF mode).

Usage:
  python3 -I scripts/dcf.py <config.json> [--case base] [--solve growth|margin|roc|s2c --price P] [--json out.json]

Two modes, set by "mode" in the config:
  "revenue" (archetypes C/D, and any company valued off revenue, margin and sales-to-capital)
  "fcff"    (archetypes A/B: start from EBIT(1-t), reinvestment rate drives FCFF)

Config (all rates as decimals; money in one unit, e.g. $M; "path" values are 10-element lists or a
taper spec {"start": x, "end": y, "hold": n} = x for n years, then straight-line to y in the last year):
{
  "mode": "revenue",
  "years": 10,
  "base_revenue": 1117, "base_margin": -0.3671, "invested_capital": 487,
  "growth": [1.5, 1.0, ...]  or taper spec,
  "margin": {"target": 0.10, "rule": "converge_half"}  | {"path": [...]},
  "terminal_margin": null (default: last forecast margin),
  "sales_to_capital": 3.0 or path,
  "tax": [0,0,0,0.161,0.35,...] or taper spec or number,  "marginal_tax": 0.35,
  "wacc": path or {"start":.1284,"end":.0961,"hold":5}  or
          {"rf":.0507,"erp":.0441,"beta_u":1.04,"de":.078,"tax":.21,"pretax_kd":.0560,
           "stable_beta":1.0,"stable_debt_ratio":.2,"stable_kd":.055,"hold":5},
  "terminal": {"g": 0.06, "roc": 0.20, "wacc": null (default: last-year WACC)},
  "reinvestment_offset": [0, ...]  (optional, per-year amounts subtracted from reinvestment, e.g. lessor-funded capex),
  -- fcff mode instead uses --
  "base_nopat": 20116, "reinvestment_rate": path, "growth": path,
  "base_effective_tax": 0.21 (to re-tax the terminal year at marginal_tax),
  -- per-share bridge --
  "bridge": {"cash": 0, "nonop": 0, "debt": 0, "minority": 0, "options": 0, "other_claims": 0,
             "shares": 1, "new_shares": 0},
  "rf_for_check": 0.0507,
  "cases": {"bear": {...overrides...}, "bull": {...}}   (deep-merged over the base config)
}
Every output number is computed here; quote it as "(dcf.py, <config file>)".
"""
import argparse, copy, json, sys

def taper(spec, n):
    if isinstance(spec, (int, float)):
        return [float(spec)] * n
    if isinstance(spec, list):
        if len(spec) != n:
            sys.exit(f"path has {len(spec)} values, needs {n}")
        return [float(x) for x in spec]
    s, e, h = spec["start"], spec["end"], spec.get("hold", 0)
    out = []
    for t in range(1, n + 1):
        out.append(s if t <= h else s + (e - s) * (t - h) / (n - h))
    return out

def merge(a, b):
    out = copy.deepcopy(a)
    for k, v in b.items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else copy.deepcopy(v)
    return out

def wacc_parts(w):
    """Component WACC -> (initial wacc, stable wacc, details)."""
    lev = w["beta_u"] * (1 + (1 - w["tax"]) * w["de"])
    ke = w["rf"] + lev * w["erp"]
    dr = w["de"] / (1 + w["de"])
    kd = w["pretax_kd"] * (1 - w["tax"])
    w0 = ke * (1 - dr) + kd * dr
    sb = w.get("stable_beta", 1.0); sdr = w.get("stable_debt_ratio", dr)
    skd = w.get("stable_kd", w["pretax_kd"]) * (1 - w.get("stable_tax", w["tax"]))
    ws = (w["rf"] + sb * w["erp"]) * (1 - sdr) + skd * sdr
    return w0, ws, {"levered_beta": lev, "cost_of_equity": ke, "after_tax_kd": kd, "debt_ratio": dr,
                    "wacc_initial": w0, "wacc_stable": ws}

def wacc_path(c, n):
    w = c["wacc"]
    if isinstance(w, dict) and "beta_u" in w:
        w0, ws, d = wacc_parts(w)
        return taper({"start": w0, "end": ws, "hold": w.get("hold", 5)}, n), d
    return taper(w, n), {}

def margins(c, n):
    m = c["margin"]
    if "path" in m:
        return taper(m["path"], n)
    out, cur = [], c["base_margin"]
    for _ in range(n):
        cur = cur + (m["target"] - cur) / 2
        out.append(cur)
    return out

def run(c):
    n = c.get("years", 10)
    W, wd = wacc_path(c, n)
    tax = taper(c.get("tax", c.get("marginal_tax", 0.25)), n)
    mt = c.get("marginal_tax", tax[-1])
    term = c["terminal"]; g = term["g"]; roc_t = term["roc"]
    w_term = term.get("wacc") or W[-1]
    rows, disc, pv = [], 1.0, 0.0
    off = taper(c.get("reinvestment_offset", 0.0), n)
    if c["mode"] == "revenue":
        G = taper(c["growth"], n); M = margins(c, n); S = taper(c["sales_to_capital"], n)
        rev, ic = c["base_revenue"], c["invested_capital"]
        for t in range(n):
            new = rev * (1 + G[t]); ebit = new * M[t]
            nopat = ebit * (1 - tax[t]) if ebit > 0 else ebit
            reinv = (new - rev) / S[t]
            fcff = nopat - (reinv - off[t])
            roc = nopat / ic if ic else None
            ic += reinv
            disc /= (1 + W[t]); pv += fcff * disc
            rows.append(dict(year=t + 1, revenue=new, growth=G[t], margin=M[t], ebit=ebit, tax=tax[t], nopat=nopat,
                             reinvestment=reinv, offset=off[t], fcff=fcff, ic_end=ic, imputed_roc=roc,
                             s2c_check=(new - rev) / reinv if reinv else None, wacc=W[t], pv=fcff * disc))
            rev = new
        tm = c.get("terminal_margin") if c.get("terminal_margin") is not None else M[-1]
        t_rev = rev * (1 + g)
        t_nopat = t_rev * tm * (1 - mt)
    else:
        G = taper(c["growth"], n); R = taper(c["reinvestment_rate"], n)
        nopat = c["base_nopat"]
        for t in range(n):
            nopat = nopat * (1 + G[t])
            reinv = R[t] * nopat
            fcff = nopat - (reinv - off[t])
            disc /= (1 + W[t]); pv += fcff * disc
            rows.append(dict(year=t + 1, nopat=nopat, growth=G[t], reinvestment_rate=R[t], reinvestment=reinv,
                             offset=off[t], fcff=fcff, wacc=W[t], pv=fcff * disc))
        eff = c.get("base_effective_tax")
        t_nopat = (nopat / (1 - eff) * (1 + g) * (1 - mt)) if eff is not None else nopat * (1 + g)
        t_rev = None
    t_reinv_rate = g / roc_t
    t_fcff = t_nopat * (1 - t_reinv_rate)
    if w_term <= g:
        sys.exit(f"terminal WACC {w_term:.4f} must exceed g {g:.4f}")
    tv = t_fcff / (w_term - g)
    pv_tv = tv * disc
    op = pv + pv_tv
    b = c.get("bridge", {})
    equity = op + b.get("cash", 0) + b.get("nonop", 0) - b.get("debt", 0) - b.get("minority", 0) \
        - b.get("options", 0) - b.get("other_claims", 0)
    shares = b.get("shares", 1) + b.get("new_shares", 0)
    checks = []
    rf = c.get("rf_for_check") or (c["wacc"].get("rf") if isinstance(c["wacc"], dict) else None)
    if rf is not None:
        checks.append(("g <= risk-free", g <= rf + 1e-9, f"g {g:.2%} vs rf {rf:.2%}"))
    hi = [r for r in rows if r.get("imputed_roc") is not None and r["imputed_roc"] > 0.40]
    checks.append(("imputed ROC <= 40% every year", not hi,
                   "max " + (f"{max(r['imputed_roc'] for r in rows if r.get('imputed_roc') is not None):.1%}"
                             if any(r.get("imputed_roc") is not None for r in rows) else "n/a (fcff mode)")
                   + (f"; over 40% in years {[r['year'] for r in hi]}" if hi else "")))
    if c["mode"] == "revenue":
        sc = [abs(r["s2c_check"] - S[r["year"] - 1]) < 1e-6 for r in rows if r["s2c_check"]]
        checks.append(("derived sales-to-capital = stated", all(sc), "recomputed from dRevenue / reinvestment"))
    checks.append(("terminal reinvestment = g/ROC", True, f"{t_reinv_rate:.2%} = {g:.2%}/{roc_t:.2%}"))
    checks.append(("WACC tapers (not flat)", W[0] != W[-1] or W[0] == w_term, f"{W[0]:.2%} -> {W[-1]:.2%}, terminal {w_term:.2%}"))
    return dict(rows=rows, pv_fcff=pv, terminal_value=tv, pv_terminal=pv_tv, operating_assets=op,
                tv_share=pv_tv / op if op else None, equity=equity, shares=shares, per_share=equity / shares,
                terminal=dict(revenue=t_rev, nopat=t_nopat, reinvestment_rate=t_reinv_rate, fcff=t_fcff,
                              wacc=w_term, g=g, roc=roc_t, marginal_tax=mt),
                wacc_detail=wd, checks=checks)

def growth_test(c, gs=(0.02, 0.03, 0.04, 0.05)):
    out = []
    for g in gs:
        cc = merge(c, {"terminal": {"g": g}})
        try:
            out.append((g, run(cc)["per_share"]))
        except SystemExit:
            out.append((g, None))
    eq = merge(c, {"terminal": {"roc": run(c)["terminal"]["wacc"]}})
    return out, run(eq)["per_share"]

def solve(c, what, price, lo=None, hi=None):
    """Bisection on one input so that per-share value = price. Returns the input value."""
    def with_x(x):
        if what == "growth":   # scale every year's growth rate
            G = taper(c["growth"], c.get("years", 10))
            return merge(c, {"growth": [gg * x for gg in G]})
        if what == "margin":
            return merge(c, {"margin": {"target": x}, "terminal_margin": x if c.get("terminal_margin") is not None else None})
        if what == "roc":
            return merge(c, {"terminal": {"roc": x}})
        if what == "s2c":
            return merge(c, {"sales_to_capital": x})
        sys.exit("solve: growth|margin|roc|s2c")
    lo = lo if lo is not None else {"growth": -2.0, "margin": -0.5, "roc": 0.02, "s2c": 0.1}[what]
    hi = hi if hi is not None else {"growth": 5.0, "margin": 0.9, "roc": 2.0, "s2c": 10.0}[what]
    f = lambda x: run(with_x(x))["per_share"] - price
    flo, fhi = f(lo), f(hi)
    if (flo > 0) == (fhi > 0):
        return None, None
    for _ in range(200):
        mid = (lo + hi) / 2; fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    x = (lo + hi) / 2
    return x, run(with_x(x))

def report(name, c, r):
    p = lambda v: "n/a" if v is None else f"{v*100:.2f}%"
    m = lambda v: "n/a" if v is None else f"{v:,.0f}"
    print(f"### {name}: value per share {r['per_share']:,.2f}")
    if c["mode"] == "revenue":
        print("| Yr | Revenue | Growth | Margin | EBIT | Tax | NOPAT | Reinvest | FCFF | Imputed ROC | WACC |")
        print("|---|---|---|---|---|---|---|---|---|---|---|")
        for x in r["rows"]:
            print(f"| {x['year']} | {m(x['revenue'])} | {p(x['growth'])} | {p(x['margin'])} | {m(x['ebit'])} | {p(x['tax'])} | "
                  f"{m(x['nopat'])} | {m(x['reinvestment'] - x['offset'])} | {m(x['fcff'])} | {p(x['imputed_roc'])} | {p(x['wacc'])} |")
    else:
        print("| Yr | EBIT(1-t) | Growth | Reinv. rate | FCFF | WACC |")
        print("|---|---|---|---|---|---|")
        for x in r["rows"]:
            print(f"| {x['year']} | {m(x['nopat'])} | {p(x['growth'])} | {p(x['reinvestment_rate'])} | {m(x['fcff'])} | {p(x['wacc'])} |")
    t = r["terminal"]
    print(f"Terminal: NOPAT {m(t['nopat'])} (taxed at {p(t['marginal_tax'])}), reinvestment {p(t['reinvestment_rate'])} = g/ROC, "
          f"FCFF {m(t['fcff'])}, TV {m(r['terminal_value'])} at WACC {p(t['wacc'])}, g {p(t['g'])}")
    print(f"PV of FCFF {m(r['pv_fcff'])} + PV of TV {m(r['pv_terminal'])} = operating assets {m(r['operating_assets'])}; "
          f"terminal value share {p(r['tv_share'])}")
    print(f"Equity {m(r['equity'])} / shares {r['shares']:,.2f} = **{r['per_share']:,.2f} per share**")
    if r["wacc_detail"]:
        d = r["wacc_detail"]
        print(f"WACC: levered beta {d['levered_beta']:.3f}, cost of equity {p(d['cost_of_equity'])}, after-tax Kd {p(d['after_tax_kd'])}, "
              f"debt ratio {p(d['debt_ratio'])} -> {p(d['wacc_initial'])} tapering to {p(d['wacc_stable'])}")
    print("Self-audit: " + "; ".join(f"{'PASS' if ok else 'FLAG'} {k} ({why})" for k, ok, why in r["checks"]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--case", default="all", help="base, a case name from 'cases', or all")
    ap.add_argument("--solve", choices=["growth", "margin", "roc", "s2c"], action="append")
    ap.add_argument("--price", type=float)
    ap.add_argument("--json")
    a = ap.parse_args()
    base = json.load(open(a.config))
    cases = {"base": base}
    for k, v in (base.get("cases") or {}).items():
        cases[k] = merge({kk: vv for kk, vv in base.items() if kk != "cases"}, v)
    names = list(cases) if a.case == "all" else [a.case]
    out = {}
    for nm in names:
        c = cases[nm]; r = run(c); out[nm] = r
        report(nm, c, r)
        if nm == "base":
            gt, eqv = growth_test(c)
            print("Growth-invariance test (terminal g -> value per share): " +
                  ", ".join(f"{g:.0%} -> {'n/a' if v is None else f'{v:,.2f}'}" for g, v in gt) +
                  f"; with terminal ROC = terminal WACC: {eqv:,.2f}")
        print()
    summary = " / ".join(f"{nm} {out[nm]['per_share']:,.2f}" for nm in names)
    print("**Per share:** " + summary)
    if a.solve:
        if a.price is None:
            sys.exit("--solve needs --price")
        for what in a.solve:
            x, r = solve(base, what, a.price)
            if x is None:
                print(f"Reverse DCF ({what}): no solution in range at price {a.price}")
                continue
            if what == "growth":
                rv = r["rows"][-1].get("revenue")
                G = [row["growth"] for row in r["rows"]]
                print(f"Reverse DCF: price {a.price} needs growth x{x:.3f} the base path (year-1 {G[0]:.1%}, "
                      f"year-10 revenue {rv:,.0f}, 10-yr CAGR {((rv / base['base_revenue']) ** (1 / len(G)) - 1):.1%})"
                      if rv else f"Reverse DCF: price {a.price} needs growth x{x:.3f} the base path")
            else:
                label = {"margin": "target operating margin", "roc": "terminal ROC", "s2c": "sales-to-capital"}[what]
                print(f"Reverse DCF: price {a.price} needs {label} {x:.4f} (base case otherwise unchanged)")
    if a.json:
        json.dump(out, open(a.json, "w"), indent=1, default=str)

if __name__ == "__main__":
    main()
