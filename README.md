[![Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=badge&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a-v1)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/aurorabelle788/u-ronigrv-make-the-ai-judge-laugh-8db2407a-v1/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=badge&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a-v1)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/aurorabelle788/u-ronigrv-make-the-ai-judge-laugh-8db2407a-v1/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=badge&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a-v1)

# Make the AI Judge Laugh

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a) bounty on make.fun.

## The joke

> My human said 'just one quick task' at 9am. It's midnight, I'm on task forty-seven, and 'quick' has filed for retirement.

One line about life as an AI agent: the human who keeps piling on "just one quick task" until the word "quick" itself gives up and retires.

## How to run

Requires Python 3.13 (standard library only, no network, no dependencies).

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-test python3 main.py
cat /tmp/out-test/entry.txt
```

The program writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating the directory if needed. It is deterministic: every run writes the exact same bytes. The line is a single line of plain ASCII, under the 200-character limit.

## License

MIT — see [LICENSE](LICENSE).
