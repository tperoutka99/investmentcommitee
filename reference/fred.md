# How to read FRED

FRED (the St. Louis Fed's economic database) serves any series as a CSV with no key and no daily cap:

`curl -sS "https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>"` (if curl is refused, use WebFetch on the same URL).

Parse it in Python. Label figures "(FRED <SERIES>)" with the observation date. Useful series: `DGS10` and `DGS2` (10Y and 2Y Treasury, daily), `DFF` (effective fed funds, daily), `CPIAUCNS` (CPI, not seasonally adjusted, for year-over-year), `CPIAUCSL` (CPI, seasonally adjusted, for 3-month annualized), `UNRATE` (unemployment), `PAYEMS` (payrolls; take the monthly change), `GDPC1` (real GDP; annualize the quarterly change), `RSAFS` (retail sales).
