#!/usr/bin/env python3
"""Check a run's reports against templates/, then save the run.

Check only (Step 3/4, before moving on):
  python3 -I scripts/save_run.py runs/<RUN> --check [macro|equity|short|data_flags|memo ...]

Save (Step 5):
  python3 -I scripts/save_run.py runs/<RUN> --version v1.4 --guess "Trey's guess or —"

Saving does all of Step 5 in one go:
  memos/IC_<TICKER>_<date>[_<version>].md        the memo
  audit/IC_<...>_reports.md                       title + version + every report + data flags
  archive/<RUN>/                                  the reports, record.json (all Data blocks),
                                                  the DCF config and outputs, peers_out.json,
                                                  price history and the analyst's facts JSON
  data/runs.csv                                   one row per run (the committee's history)
  docs/run-log.md                                 one row per run
A report that fails its template check stops the save.
"""
import argparse, csv, glob, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = ["macro", "equity", "short", "data_flags", "memo"]
PLACEHOLDER = re.compile(r"<[^<>\s][^<>\n]{0,300}>")
CSV_FIELDS = ["run", "date", "ticker", "skill_version", "verdict", "conviction", "position", "price",
              "value_bear", "value_base", "value_bull", "short_bear_price", "macro_call", "macro_confidence",
              "beta_bottom_up", "wacc_initial", "rf", "erp", "tv_share_base", "thesis_strength",
              "buy_below", "exit_below", "exit_above", "watch_trigger", "kill_events", "review_by",
              "next_earnings", "rev_ny_mine_m", "rev_ny_consensus_m", "contradicted", "not_found",
              "trey_guess", "memo", "archive"]

def data_block(text):
    m = re.search(r"```data\n(.*?)```", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out

def headings(text):
    return [l.strip() for l in text.splitlines() if l.startswith("## ")]

def fixed_rows(tpl):
    """First-column labels of template table rows that already have a label (fixed rows)."""
    rows = []
    lines = tpl.splitlines()
    for i, l in enumerate(lines):
        if l.startswith("| ") and i > 1 and lines[i - 1].startswith("|---"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                lab = lines[j].split("|")[1].strip()
                if lab and not PLACEHOLDER.fullmatch(lab):
                    rows.append(lab)
                j += 1
    return rows

def check(name, path):
    errs = []
    tpl = open(os.path.join(ROOT, "templates", f"{name}.md")).read()
    if not os.path.exists(path):
        return [f"{name}: file missing ({path})"]
    txt = open(path).read()
    th, rh = headings(tpl), headings(txt)
    if th != rh:
        missing = [h for h in th if h not in rh]
        extra = [h for h in rh if h not in th]
        errs.append(f"{name}: section headings differ from the template"
                    + (f"; missing {missing}" if missing else "") + (f"; extra {extra}" if extra else "")
                    + ("; order differs" if not missing and not extra else ""))
    t1 = tpl.splitlines()[0].split(":")[0]; r1 = txt.splitlines()[0].split(":")[0] if txt else ""
    if t1 != r1:
        errs.append(f"{name}: title must start '{t1}:' (got '{r1}')")
    # table headers: placeholder-free ones must appear verbatim; others must keep their column count
    rlines = txt.splitlines()
    rheads = [rlines[i].strip() for i in range(len(rlines) - 1) if rlines[i].startswith("|") and rlines[i + 1].startswith("|---")]
    for h in header_lines(tpl):
        if not PLACEHOLDER.search(h):
            if h not in rheads:
                errs.append(f"{name}: table header missing or changed: {h}")
        else:
            ncol = h.count("|")
            if not any(r.count("|") == ncol and r.split("|")[-2].strip() == h.split("|")[-2].strip() for r in rheads):
                errs.append(f"{name}: table missing or its columns changed: {h}")
    for lab in fixed_rows(tpl):
        if not re.search(r"^\| " + re.escape(lab) + r" \|", txt, re.M):
            errs.append(f"{name}: fixed table row missing or renamed: '{lab}'")
    left = sorted(set(PLACEHOLDER.findall(txt)))
    if left:
        errs.append(f"{name}: unfilled placeholders: {left[:6]}")
    tb, rb = data_block(tpl), data_block(txt)
    if rb is None:
        errs.append(f"{name}: no ```data block at the end")
    else:
        miss = [k for k in tb if k not in rb]
        empty = [k for k in tb if k in rb and rb[k] == ""]
        if miss:
            errs.append(f"{name}: data block missing keys {miss}")
        if empty:
            errs.append(f"{name}: data block empty values {empty}")
    return errs

def header_lines(text):
    l = text.splitlines()
    return [l[i].strip() for i in range(len(l) - 1) if l[i].startswith("|") and l[i + 1].startswith("|---")]

def num(v):
    try:
        return float(str(v).replace("$", "").replace(",", "").split()[0])
    except Exception:
        return v

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--check", nargs="*")
    ap.add_argument("--version")
    ap.add_argument("--guess", default="—")
    a = ap.parse_args()
    run = a.run.rstrip("/")
    name = os.path.basename(run)
    if a.check is not None:
        which = a.check or REPORTS
        errs = [e for r in which for e in check(r, os.path.join(run, f"{r}.md"))]
        print("\n".join(errs) if errs else "Template check: PASS (" + ", ".join(which) + ")")
        sys.exit(1 if errs else 0)
    if not a.version:
        sys.exit("--version is required to save")
    errs = [e for r in REPORTS for e in check(r, os.path.join(run, f"{r}.md"))]
    if errs:
        print("Not saved. Fix these first:\n" + "\n".join(errs)); sys.exit(1)
    blocks = {r: data_block(open(os.path.join(run, f"{r}.md")).read()) for r in REPORTS}
    m = blocks["memo"]; ticker, date = m["ticker"], m["date"]
    base = f"IC_{ticker}_{date}"
    memo_path = os.path.join("memos", base + ".md")
    if os.path.exists(os.path.join(ROOT, memo_path)):
        base = f"{base}_{a.version}"; memo_path = os.path.join("memos", base + ".md")
    shutil.copy(os.path.join(run, "memo.md"), os.path.join(ROOT, memo_path))
    audit_path = os.path.join("audit", base + "_reports.md")
    with open(os.path.join(ROOT, audit_path), "w") as f:
        f.write(f"# {base}: analyst reports\n\n**Skill version:** {a.version}\n\n")
        for r, title in (("macro", "Macro strategist"), ("equity", "Equity analyst + valuation"),
                         ("short", "Short seller"), ("data_flags", "Data flags")):
            f.write(f"## {title}\n" + open(os.path.join(run, f"{r}.md")).read() + "\n\n")
    arch = os.path.join(ROOT, "archive", name if not os.path.exists(os.path.join(ROOT, "archive", name)) else f"{name}_{a.version}")
    os.makedirs(arch, exist_ok=True)
    for r in REPORTS:
        shutil.copy(os.path.join(run, f"{r}.md"), arch)
    # keep the analyst's structured inputs and outputs; skip raw filings (they stay on EDGAR)
    keep = []
    for pat in ("downloads/equity-analyst/*_facts.json", "downloads/equity-analyst/peers_out.json",
                "downloads/equity-analyst/closes*.json", "downloads/equity-analyst/dcf*.json",
                "downloads/macro-strategist/*.csv", "downloads/macro-strategist/kalshi*.json",
                "downloads/macro-strategist/polymarket*.json"):
        keep += glob.glob(os.path.join(run, pat), recursive=True)
    for p in sorted(set(keep)):
        if os.path.getsize(p) > 1_000_000:
            continue
        rel = os.path.relpath(p, os.path.join(run, "downloads"))
        os.makedirs(os.path.join(arch, "inputs", os.path.dirname(rel)), exist_ok=True)
        shutil.copy(p, os.path.join(arch, "inputs", rel))
    record = {"run": name, "skill_version": a.version, "trey_guess": a.guess, "memo": memo_path,
              "audit": audit_path, "reports": blocks}
    json.dump(record, open(os.path.join(arch, "record.json"), "w"), indent=1)
    e, s, mc, df = blocks["equity"], blocks["short"], blocks["macro"], blocks["data_flags"]
    row = {"run": name, "date": date, "ticker": ticker, "skill_version": a.version, "verdict": m["verdict"],
           "conviction": m["conviction"], "position": m["position"], "price": num(m["price"]),
           "value_bear": num(m["value_bear"]), "value_base": num(m["value_base"]), "value_bull": num(m["value_bull"]),
           "short_bear_price": num(m["short_bear_price"]), "macro_call": mc["call"], "macro_confidence": mc["confidence"],
           "beta_bottom_up": num(e["beta_bottom_up"]), "wacc_initial": num(e["wacc_initial"]), "rf": num(e["rf"]),
           "erp": num(e["erp"]), "tv_share_base": num(e["tv_share_base"]), "thesis_strength": num(s["thesis_strength"]),
           "buy_below": num(m["buy_below"]), "exit_below": num(m["exit_below"]), "exit_above": num(m["exit_above"]),
           "watch_trigger": m["watch_trigger"], "kill_events": m["kill_events"], "review_by": m["review_by"],
           "next_earnings": e["next_earnings"], "rev_ny_mine_m": num(e["rev_ny_mine_m"]),
           "rev_ny_consensus_m": num(e["rev_ny_consensus_m"]), "contradicted": num(df["contradicted"]),
           "not_found": num(df["not_found"]), "trey_guess": a.guess, "memo": memo_path,
           "archive": os.path.relpath(arch, ROOT)}
    csv_path = os.path.join(ROOT, "data", "runs.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    new = not os.path.exists(csv_path)
    with open(csv_path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    with open(os.path.join(ROOT, "docs", "run-log.md"), "a") as f:
        f.write(f"| {date} | {ticker} | {a.version} | ${num(m['price']):,.2f} | {m['verdict']} | {m['conviction']} | {a.guess} | {memo_path} |\n")
    print(f"Saved: {memo_path}, {audit_path}, {os.path.relpath(arch, ROOT)}/, data/runs.csv, docs/run-log.md")

if __name__ == "__main__":
    main()
