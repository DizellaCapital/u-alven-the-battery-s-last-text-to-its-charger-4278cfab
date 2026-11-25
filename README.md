# The Battery's Last Text to Its Charger

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/DizellaCapital/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/DizellaCapital/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A [make.fun](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) bounty entry: the phone battery's last text message to the charger it waited for all day — one line of plain text, at most 200 characters.

## The line

> 1% left, and I spent it on this text instead of your 7 a.m. alarm. All day you charged the tablet. It doesn't even make calls. Enjoy waking up late.

148 characters. The battery burns its final percent on the text itself instead of saving it for the 7 a.m. alarm — so the alarm never rings.

## How it works

`main.py` (Python 3, standard library only) validates the line — 1–200 characters, a single line, valid UTF-8, not only whitespace — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`) with no trailing newline, then reads the file back and verifies it byte-for-byte before reporting success.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

[The Battery's Last Text to Its Charger — make.fun](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
