# X2 · Optional commit trailers (ES: metadatos opcionales del commit)

**State:** proposal only; no hook installed and no commit altered.

The Round 2 commission names `Agent`, `Model`, and `Run` as the de-facto fields and says `Status` has never been used. Propose an optional `prepare-commit-msg` hook for ordinary new commits: preserve supplied values, add each missing field once as `NO_DATA`, and remain idempotent. Do not add `Status`; skip merge, squash, rebase, and amend messages. No network access or history rewrite.

**Acceptance gate:** after FIRMO, test in a disposable repository; attach output showing one new commit with exactly one value for each field and `NO_DATA` where absent. This proposal installs nothing and creates no test commit.

## Receipt

source=study#61/R2-X2; hook_installed=0; commits_created=0; test_output=NO_DATA(cause: implementation awaits FIRMO); state=proposal
