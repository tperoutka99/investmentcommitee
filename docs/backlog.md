# Backlog — gaps and ideas (not approved yet; Trey decides)

1. **Same-period rule for the fact check.** On MRVL the fact check put "receivables +1.5% since year-end" next to the short seller's "+53% vs a year ago," and the PM treated it as a rebuttal. Proposed rule: the fact check can only mark a claim Contradicted when it compares the same period.
2. **Almost every verdict is WATCH** (8 of 9 memos). Check whether the PM's rules push it toward WATCH by default, e.g. require it to say what would make it BUY *today* and why that isn't met.
3. **Institutional (13F) data** comes back "not assessed" most runs. No free structured source found yet.
4. **Multi-year revenue consensus** stops at 2 years (Yahoo). Years 3+ are the analyst's own.
5. **Track record.** Compare each memo's verdict and trigger prices against what the stock did 30/90 days later, to see if the committee is any good.
6. **WebFetch vs curl.** With the network set to all allowed, curl reaches federalreserve.gov and Yahoo but the agents' WebFetch still fails on them (ADBE/SPCX 2026-11-20). Proposed: tell agents in `reference/agent-rules.md` to retry a failed WebFetch with curl before marking data "not assessed".
7. **Orchestrator task notes.** The SPCX task note mislabeled the 2026-08-14 8-K as xAI (it was Cursor). Proposed: Step 0 notes about filings must quote the 8-K's own item text, or be left out.
