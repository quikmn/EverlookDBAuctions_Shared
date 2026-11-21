# EverlookDB Auctions: Price Feed

Other players' newest auction scans from [everlookdb.com](https://everlookdb.com), for
[EverlookDB Auctions](https://github.com/quikmn/EverlookDBAuctions) in WoW Forever.

This addon ships empty. The [EverlookDB App](https://github.com/quikmn/everlookdb-uploader) fills it: every 15 minutes,
and right after it uploads your own scans, it fetches the newest scan anyone uploaded for the auction houses you play on
and writes it into this folder. EverlookDB Auctions reads it at your next `/reload` or login, so prices are fresh even
when you haven't been to the auction house for days. Such prices always say so: "other players' scan · 12 min ago".

- Needs EverlookDB Auctions (it shows under it in the addon list and never loads without it).
- Without the app it stays empty, and EverlookDB Auctions says "Price Feed: no data yet".
- The app writes only `Shared.lua`, the `.toc` and one `.lua` file per auction house in this folder, never anything
  else. When CurseForge updates this addon (which brings back the empty copy), the app writes its data again within
  about a minute.
- The data has no player names.
- Turn it off in the app (the Price Feed switch), or in game on the General page of `/eah`.

Like TradeSkillMaster's AppHelper, it is a CurseForge addon so it installs and updates like any other; the data comes
from the app.

## License

GPL-3.0, see LICENSE.