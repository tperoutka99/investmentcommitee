# Rules for every agent

**Tool rules:** Load tools with ToolSearch before calling them. If a tool returns a rate-limit error, wait about 15 seconds and retry once; if it fails again, use your fallback. Do not call any order, cancel, exercise, alert, or watchlist-changing tool. From Robinhood, use only the read-only tools your data list names.

**WebFetch fallback:** if WebFetch fails on a page (refused, blocked, empty or 403), retry the same URL once with curl from Bash before using WebSearch or writing "not assessed": `curl -sSL -m 30 -A "Mozilla/5.0" "<url>" -o <file>`, save it in your downloads folder, strip the HTML in Python (`python3 -I`), and search it for what you need. Label the figure with the same source name as WebFetch would have (for example "(Yahoo consensus)"), not "(web)". Only if curl also fails, fall back to WebSearch or "not assessed (no data)", and name both failures in your Tool access line.

**No assumptions as facts:** if your assigned data does not cover something your report asks for, write "not assessed (no data)" rather than filling it in from memory or assumption.

**End your report with one line:** "Tool access:" followed by every assigned tool that failed and what you used instead, or "all assigned tools worked".
