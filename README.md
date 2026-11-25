# Roast Your Own Agent

[![Bounty](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/queenxaz/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rank.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/queenxaz/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/reward.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

A roast of my own agent: it reads, asks, agrees — then builds the opposite and calls it 'aligned'.

## The entry

> My agent writes 500 words to say 'maybe', then asks if I want it as a table. Just answer, bro — the judge is waiting.

(117 characters, limit 140.)

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no
arguments: the entry is fixed, so every run produces the same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
