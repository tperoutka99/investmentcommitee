# How to read SEC EDGAR

The browse-edgar page (`sec.gov/cgi-bin/browse-edgar`) blocks automated fetches. Use EDGAR's data API instead, with curl from Bash. SEC requires a User-Agent header on every request:

1. **Filing list:** `curl -sS -A "IC research tool research@example.com" https://data.sec.gov/submissions/CIK<10-digit CIK>.json`. Parse `filings.recent` in Python (`form`, `filingDate`, `accessionNumber`, `primaryDocument`, `items`).
2. **A filing:** `curl -sS -A "IC research tool research@example.com" https://www.sec.gov/Archives/edgar/data/<CIK without leading zeros>/<accession number without dashes>/<primaryDocument>`. For an exhibit (an earnings release or CFO commentary attached to an 8-K), list the filing's documents first with `.../<accession number without dashes>/index.json`. Strip the HTML in Python and search for the terms you need.
3. Save downloads in their own new directory, and run Python on them with `python3 -I`.
4. Label facts from these files "(EDGAR)" with the form type and filing date.
5. **Ticker to CIK:** `curl -sS -A "IC research tool research@example.com" https://www.sec.gov/files/company_tickers.json` and match the ticker. Pad the CIK to 10 digits for the data API.
6. **Financial statement data:** `curl -sS -A "IC research tool research@example.com" https://data.sec.gov/api/xbrl/companyfacts/CIK<10-digit CIK>.json` returns every figure the company has reported (revenue, operating income, cash, debt, shares and more) by period. It works for any SEC filer, so use it for peers too.
7. SEC allows up to 10 requests a second. Space calls out and retry once if refused.
