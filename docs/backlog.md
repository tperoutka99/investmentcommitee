# Backlog — gaps and ideas (not approved yet; Trey decides)

1. **Same-period rule for the fact check.** On MRVL the fact check put "receivables +1.5% since year-end" next to the short seller's "+53% vs a year ago," and the PM treated it as a rebuttal. Proposed rule: the fact check can only mark a claim Contradicted when it compares the same period.
2. **Almost every verdict is WATCH** (8 of 9 memos). Check whether the PM's rules push it toward WATCH by default, e.g. require it to say what would make it BUY *today* and why that isn't met.
3. **Institutional (13F) data** comes back "not assessed" most runs. No free structured source found yet.
4. **Multi-year revenue consensus** stops at 2 years (Yahoo). Years 3+ are the analyst's own.
5. **Speed: fewer, bigger tool calls (other agents).** Added to the equity analyst in v1.2; not yet to macro or short seller. Each agent round trip costs ~10s of model time. Proposed rule in `reference/agent-rules.md`: batch fetches into one Bash call where possible, and write the report file once.
