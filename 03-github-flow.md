# 03 · The GitHub flow

- **repo** — One project on GitHub. The measured set: PreceptorOS (the app), lab (benchmarks), preceptoros-web (the web and the game), p0x (the private rack monorepo), the Comando (the channel), aduana (the Customs Worker), study (this repo), plus the profile. Name the repo exactly; "the repo" alone is ambiguity.
- **main** — The trunk. Nothing enters without a measured PR and the Sovereign's sign-off. Cited with its sha ("main a730548").
- **branch** — A separate line of work (haiku/*, mesa/*, codex/*). Never write directly to main.
- **commit** — A snapshot with its hash. Unsigned commits are the norm here: silicon does not sign.
- **PR (pull request)** — A proposal of change against main. One piece per PR: two asks in one PR break the measurement.
- **draft PR** — A PR in draft cannot merge until marked ready. A 405 "still a draft" on merge means: mark ready, retry. It happened twice already; it is a bounce, not a failure.
- **head / base** — head = the branch carrying the change; base = the target. Cite both shas to avoid merging against a moved base.
- **expectedHeadSha** — The merge lock: the exact hash the branch tip must have. If the branch moved, the merge bounces instead of merging blind.
- **merge** — Entering the PR into main. Only under the Sovereign's sign-off, per PR, after the Desk's measurement. Never "merge what you see".
- **diff** — The exact text of the change. The Desk reads it whole before surfacing any sign-off.
- **issue** — A work or decision thread inside a repo. Rulings live in issues; cite number and comment.
- **CI / checks** — Remote automatic tests on the PR (e.g. 10/10 green across Python 3.10–3.14). They add to the local gates; they never replace them.
- **redirect** — GitHub redirects the old name after a repo rename; issues and clones keep living. Renaming is safe; deleting is not.
- **AGENTS.md / llms.txt** — The files an AI reads when it lands in a repo. If you want a preceptor to understand your repo cold, its law lives here.
- **worktree / staging (/tmp)** — A separate working area that does not touch main. "VERSION intact" means nothing served or registered yet.