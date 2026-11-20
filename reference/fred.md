# How to read FRED

FRED (the St. Louis Fed's economic database) serves any series as a CSV with no key and no daily cap:

`curl -sS "https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>"` (if curl is refused, use WebFetch on the same URL).

Parse it in Python.

**Check for gaps before computing any change.** FRED leaves a blank value (an empty cell after the comma, or ".") for a month with no release; October 2025 is blank for the CPI series because of the 2025 government shutdown. Never skip over a blank, interpolate it, or compare against the nearest month instead. If the latest value, or the value a year (or 3 months) earlier, is blank, report the latest change you can compute exactly, label its period (for example "CPI y/y 3.74% (Sep 2026)"), and add one line to your Notes naming the missing month. State the exact two observations behind every change you report. Label figures "(FRED <SERIES>)" with the observation date. Useful series: `DGS10` and `DGS2` (10Y and 2Y Treasury, daily), `DFF` (effective fed funds, daily), `CPIAUCNS` (CPI, not seasonally adjusted, for year-over-year), `CPIAUCSL` (CPI, seasonally adjusted, for 3-month annualized), `UNRATE` (unemployment), `PAYEMS` (payrolls; take the monthly change), `GDPC1` (real GDP; annualize the quarterly change), `RSAFS` (retail sales).
