[![make.fun · u-deysumbrella-the-3am-fridge-text-4c3e721d](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/imnotripper/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/imnotripper/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)

# The 3AM Fridge Text

One-line text message for the [make.fun bounty](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d): the program writes a single
message — the text a smart fridge sends its owner at 3am — to
`/output/entry.txt`, one line, under 140 characters, nothing else.

## The text

> 3am check-in: the pickles have unionised and the cheese has filed a formal complaint.

85 characters (55 to spare of the 140 allowed). Chosen from a scored
pool of 10 candidates in [`selection.md`](selection.md): the fridge
speaking as a night-shift manager filing a report on its contents,
two jokes stacked in one line, complete on a lock screen — and nothing
in it about milk, ice, or a door left open.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib only, no network, no clock, no randomness — the
same fixed text on every run.

## Tests

```sh
python3 test.py
```

Asserts the gate (1–140 characters, exactly one line, valid UTF-8,
not only whitespace), determinism (two runs byte-identical), the
output file mode (0644), and that the output is the chosen text.

Verified output: 85 characters, no trailing newline, mode 0644.
