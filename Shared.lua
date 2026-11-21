-- EverlookDB Auctions: Price Feed. This is the empty copy: it holds no prices.
--
-- The EverlookDB App (everlookdb.com) fills this folder with other players' newest auction scans of the auction
-- houses you play on: it writes its own Shared.lua over this one, a .lua file per auction house, and the .toc that
-- lists them. EverlookDB Auctions reads them at login and /reload. Without the app this stays empty, and EverlookDB
-- Auctions says "Price Feed: no data yet".
--
-- written = 0 marks this empty copy (the app writes the time it wrote the data).
EverlookDBAuctionsShared = { version = 1, written = 0, houses = {} }