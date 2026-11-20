# Rules for every agent

**Tool rules:** Load tools with ToolSearch before calling them. If a tool returns a rate-limit error, wait about 15 seconds and retry once; if it fails again, use your fallback. Do not call any order, cancel, exercise, alert, or watchlist-changing tool. From Robinhood, use only the read-only tools your data list names.

**No assumptions as facts:** if your assigned data does not cover something your report asks for, write "not assessed (no data)" rather than filling it in from memory or assumption.

**End your report with one line:** "Tool access:" followed by every assigned tool that failed and what you used instead, or "all assigned tools worked".
