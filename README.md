[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/h05meigames2/out-of-office-24nov26/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/h05meigames2/out-of-office-24nov26/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

An entry for the [make.fun bounty "The Funniest Out-of-Office"](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf): one line of out-of-office auto-reply, as funny as I could make it in 140 characters or fewer.

## The program

`main.py` (Python 3.13, standard library only, no network access) writes the single-line reply to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), validating that it is exactly one line of 1–140 characters before writing, and exits 0 on success. The reply itself lives in the `LINE` constant at the top of `main.py`, so the program is fully self-contained.

## The line

> I'm away until Monday — my inbox is guarded by my cat, who has already deleted three emails and shows no remorse.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py
cat /tmp/ooo-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
