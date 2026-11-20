# Backlog — gaps and ideas (not approved yet; Trey decides)

1. **Same-period rule for the fact check.** On MRVL the fact check put "receivables +1.5% since year-end" next to the short seller's "+53% vs a year ago," and the PM treated it as a rebuttal. Proposed rule: the fact check can only mark a claim Contradicted when it compares the same period.
2. **Almost every verdict is WATCH** (8 of 9 memos). Check whether the PM's rules push it toward WATCH by default, e.g. require it to say what would make it BUY *today* and why that isn't met.
3. **Institutional (13F) data** comes back "not assessed" most runs. No free structured source found yet.
4. **Multi-year revenue consensus** stops at 2 years (Yahoo). Years 3+ are the analyst's own.
5. **Track record.** Compare each memo's verdict and trigger prices against what the stock did 30/90 days later, to see if the committee is any good.
6. **Speed: reusable equity scripts.** On ADBE/SPCX the equity analyst took 7.5 and 10.8 min. Its data calls took only ~30-40s; the rest was the model writing new DCF, beta and peer scripts and running 46-63 small commands. Proposed: commit tested scripts (`scripts/edgar_facts.py`, `scripts/peer_beta.py`, `scripts/dcf.py`) that the analyst runs with its inputs.
7. **Speed: fewer, bigger tool calls.** Each agent round trip costs ~10s of model time. Proposed rule in `reference/agent-rules.md`: batch fetches into one Bash call where possible, and write the report file once.
