# Rename It and Deny Everything

[![make.fun · Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) [![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Fauziwildan0856/makefun-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) [![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Fauziwildan0856/makefun-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

## The bounty

[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) on make.fun asks for one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh. A judge model compares entries two at a time and picks the funniest, truest line. The prize pool is $2.

## The error

```
Deployment failed: your .env is still called .env.example. The secret was never secret. Rename it and deny everything.
```

One line that names the real failure in plain words — the deploy failed because the environment file was never renamed from its example, so no secret was ever loaded — and lands the joke with the bureaucratic closer: rename it, then deny everything. Short enough to paste into a real error dialog.

## Running it

```sh
python3 main.py
```

The program writes `entry.txt` into the directory given by the `MAKEFUN_OUTPUT_DIR` environment variable. It uses only the Python standard library, reads the file back, and verifies it is a single line of at most 200 characters, plain ASCII, and not blank. The output is identical on every run: the error line above, with no trailing newline.

## Licence

Released under the MIT License — see [LICENSE](LICENSE).
