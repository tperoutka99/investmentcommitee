# How to read rate-hike odds

Use two prediction markets. Both are free and need no key. Report both.

1. **Polymarket:** find the open "Fed decision in <month>" event for the next FOMC meeting (WebSearch "Polymarket Fed decision <month> <year>"), then read it with WebFetch on the polymarket.com event page, or with curl on `https://gamma-api.polymarket.com/events?slug=<event slug>`. Record each outcome's probability and the total volume.
2. **Kalshi:** `curl -sS "https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION&status=open"` lists the open Fed decision markets. Pick the one for the next meeting and record each outcome's probability (last price) and volume.

Label each "(Polymarket)" or "(Kalshi)" with the date. If the two differ by more than 10 points on the most likely outcome, show both and say so. These are betting markets, not the futures market professionals use; say that once in the report.
