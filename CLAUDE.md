@AGENTS.md

## Claude Code notes
- Run the committee with "run the committee on <TICKER>" or `/investment-committee <TICKER>`. Open Claude Code in this folder's root so the agents in `.claude/agents/` load.
- The four analysts are subagents: `macro-strategist`, `equity-analyst`, `short-seller`, `portfolio-manager`. Launch them only through the investment-committee skill, never one-off, so the isolation and fact-check steps aren't skipped.
- Before each run, ask Trey for his guess (business good/bad, cheap/expensive, rough value), keep it out of every agent, and compare it with the verdict at the end.
