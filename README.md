# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/gibalers-rgb/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/gibalers-rgb/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world news of Wednesday, 25 November 2026: a
newspaper front page — masthead, a dawn globe ringed by the day's scenes,
and the six stories that defined the day. Ukraine hits Russian ships in
the Baltic and off Libya, with Putin vowing retaliation; COP31 collapses
in Antalya with no deal; a Houthi missile strikes Riyadh's tallest tower;
NATO sends early-warning planes to Poland; Trump awards Giuliani the Medal
of Freedom; and Anthropic shares slide below their $83 IPO price. The
image is composed once (AI illustration + sharp rendered text) and the
program copies it to the output, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB) — the whole entry.

## How the image was made

`compose.py` builds `entry.png`: it takes the AI-generated hero illustration
in `assets/` (a dawn globe with the day's themes, no text) and lays out the
masthead, date and six story cards with PIL, so every word is crisp and
legible. Rebuild it with `python3 compose.py`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
