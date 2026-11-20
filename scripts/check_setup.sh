#!/usr/bin/env bash
# Checks that the free data sources the committee uses are reachable.
# Usage: bash scripts/check_setup.sh
UA="IC research tool research@example.com"
ok=0; bad=0
check() {
  local name="$1" url="$2" ua="$3"
  local code
  if [ -n "$ua" ]; then code=$(curl -s -o /dev/null -w '%{http_code}' -A "$ua" --max-time 20 "$url")
  else code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$url"); fi
  if [ "$code" = "200" ]; then echo "OK    $name"; ok=$((ok+1)); else echo "FAIL  $name (HTTP $code)"; bad=$((bad+1)); fi
}
check "SEC ticker list"        "https://www.sec.gov/files/company_tickers.json" "$UA"
check "SEC data API"           "https://data.sec.gov/submissions/CIK0000320193.json" "$UA"
check "FRED (10Y yield)"       "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10"
check "Kalshi Fed markets"     "https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION&status=open"
check "Polymarket API"         "https://gamma-api.polymarket.com/events?limit=1"
check "Damodaran data pages"   "https://pages.stern.nyu.edu/~adamodar/"
echo
echo "$ok reachable, $bad failed."
echo "Also connect the Robinhood and Twelve_Data MCP servers in Claude Code (see AGENTS.md)."
echo "Yahoo Finance and StockAnalysis are read with WebFetch, not curl, so they aren't tested here."
