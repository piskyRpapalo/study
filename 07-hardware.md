# 07 · Hardware — the machines

- **the Rack** *(ES: el rack)* — The lab machine (a beelink): home of the local loops, the Register, the local brains. Everything private lives inside it.
- **the S110** — The Sovereign's phone; the visual half of the Eye. Viewed and measured via scrcpy / adb reverse over loopback; serial numbers never appear in public.
- **jetson** — A machine of the fleet under a permanent push embargo. Nothing is ever pushed there.
- **loopback discipline** — Serving and measuring happen on 127.0.0.1; a public deployment is a separate, signed act.
- **local inference hardware** — The rack runs local model inference; the app pairs with local memory and local inference — zero cloud. Figures (models, benchmarks) live in the lab repo.
- **keys** — Ed25519 keys for charters live in the rack; the Register is signed with a rotating key with real deadlines — expiry dates are tracked, never ignored.