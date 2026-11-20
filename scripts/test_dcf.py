#!/usr/bin/env python3
"""Check dcf.py against the damodaran-dcf skill's verified worked examples.

Run: python3 -I scripts/test_dcf.py     (prints PASS/FAIL per check; exit code 1 on any failure)
Reference figures are the ones the skill states it recomputed from the source paper.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dcf

fails = 0
def check(name, got, want, tol):
    global fails
    ok = abs(got - want) <= tol * abs(want)
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got:,.4f}, want {want:,.4f} (tolerance {tol:.1%})")

# Amazon (archetype C, revenue mode)
amzn = {
    "mode": "revenue", "years": 10,
    "base_revenue": 1117, "base_margin": -0.3671, "invested_capital": 487,
    "growth": [1.5, 1.0, 0.75, 0.5, 0.3, 0.252, 0.204, 0.156, 0.108, 0.06],
    "margin": {"target": 0.10, "rule": "converge_half"},
    "sales_to_capital": 3.0,
    "tax": [0, 0, 0, 0.161, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35], "marginal_tax": 0.35,
    "wacc": {"start": 0.1284, "end": 0.0961, "hold": 5},
    "terminal": {"g": 0.06, "roc": 0.20, "wacc": 0.0961},
    "bridge": {"cash": 26, "debt": 349, "options": 2892, "shares": 341},
}
r = dcf.run(amzn)
want_m = [-13.36, -1.68, 4.16, 7.08, 8.54, 9.27, 9.64, 9.82, 9.91, 9.95]
for i, w in enumerate(want_m):
    check(f"Amazon margin year {i+1}", r["rows"][i]["margin"] * 100, w, 0.005 if abs(w) > 1 else 0.02)
want_roc = [-76.59, -8.99, 20.59, 25.83, 21.15, 22.23, 22.30, 21.87, 21.19, 20.39]
for i, w in enumerate(want_roc):
    check(f"Amazon imputed ROC year {i+1} (beginning-of-year capital)", r["rows"][i]["imputed_roc"] * 100, w, 0.01)
check("Amazon terminal value (skill recompute 52,105)", r["terminal_value"], 52105, 0.01)
check("Amazon operating assets (published 15,170)", r["operating_assets"], 15170, 0.01)
check("Amazon value per share (published $35.08)", r["per_share"], 35.08, 0.01)

# Tata Motors (archetype B, FCFF mode, terminal re-taxed at the marginal rate)
tata = {
    "mode": "fcff", "years": 10, "base_nopat": 20116,
    "growth": [0.1201] * 5 + [0.106, 0.092, 0.078, 0.064, 0.05],
    "reinvestment_rate": {"start": 0.70, "end": 0.4167, "hold": 5},
    "wacc": {"start": 0.125, "end": 0.1039, "hold": 5},
    "base_effective_tax": 0.21, "marginal_tax": 0.3399,
    "terminal": {"g": 0.05, "roc": 0.12, "wacc": 0.1039},
}
r = dcf.run(tata)
check("Tata year-10 EBIT(1-t) (skill 51,607)", r["rows"][-1]["nopat"], 51607, 0.002)
check("Tata terminal EBIT(1-t) re-taxed (skill 45,277)", r["terminal"]["nopat"], 45277, 0.002)
check("Tata terminal FCFF (skill 26,412)", r["terminal"]["fcff"], 26412, 0.002)
check("Tata operating assets, tapering WACC (skill 232,043; published 231,914)", r["operating_assets"], 232043, 0.005)
flat = dcf.merge(tata, {"wacc": 0.125})
check("Tata operating assets, flat 12.5% WACC (skill 222,054)", dcf.run(flat)["operating_assets"], 222054, 0.01)

# 3M (archetype A): terminal value invariant to growth when ROC = cost of capital
mmm = {
    "mode": "fcff", "years": 5, "base_nopat": 3474,
    "growth": [0.075, 0.075, 0.066, 0.048, 0.03],
    "reinvestment_rate": {"start": 0.2997, "end": 0.4438, "hold": 2},
    "wacc": {"start": 0.0789, "end": 0.0676, "hold": 2},
    "terminal": {"g": 0.03, "roc": 0.0676, "wacc": 0.0676},
}
r = dcf.run(mmm)
check("3M terminal value (published 70,409)", r["terminal_value"], 70409, 0.005)
check("3M operating assets (skill recompute 59,745; published 60,607)", r["operating_assets"], 59745, 0.02)
tvs = [dcf.run(dcf.merge(mmm, {"terminal": {"g": g}}))["terminal_value"] / (1 + g) for g in (0.0, 0.01, 0.02, 0.03)]
# with ROC = WACC, TV/(1+g) is constant in g: NOPAT x (1 - g/r) x (1+g)/(r-g) = NOPAT x (1+g)/r
check("3M growth invariance: TV/(1+g) at g=0% vs g=3%", tvs[0], tvs[3], 1e-9)

# Discount-rate formulas (Step 4)
_, _, d = dcf.wacc_parts({"rf": 0.0372, "erp": 0.04, "beta_u": 1.09, "de": 0.088, "tax": 0.35, "pretax_kd": 0.0447})
check("3M levered beta (1.1523)", d["levered_beta"], 1.1523, 0.0005)
check("3M WACC (7.89%)", d["wacc_initial"] * 100, 7.89, 0.003)
_, _, d = dcf.wacc_parts({"rf": 0.02, "erp": 0.06, "beta_u": 1.52, "de": 0.0121, "tax": 0.40, "pretax_kd": 0.0265})
check("Facebook levered beta (1.5310)", d["levered_beta"], 1.5310, 0.0005)
check("Facebook cost of equity (11.18%)", d["cost_of_equity"] * 100, 11.18, 0.002)
check("Facebook WACC (11.07%)", d["wacc_initial"] * 100, 11.07, 0.002)

# Reverse DCF returns the input that reproduces a given price
x, rr = dcf.solve(amzn, "margin", 35.08)
check("Reverse DCF: Amazon target margin that gives $35.08 (10%)", x, 0.10, 0.02)

print("\nALL PASS" if not fails else f"\n{fails} FAILED")
sys.exit(1 if fails else 0)
