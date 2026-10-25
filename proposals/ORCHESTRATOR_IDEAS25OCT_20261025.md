# Orchestrator brief · ideas25oct · proposal

**State:** proposed; awaiting Sovereign review. No repository fix is authorized by this document.

**Source:** `proposals/ORCHESTRATOR_IDEAS25OCT_OBJECTIVES_20261025.md` on `origin/main` at `57cfe0f` (study#60).

## Work package

1. **Identity registry:** audit every `Agent`, `Model`, and `Run` trailer in study, lab, PreceptorOS, preceptoros-web, p0x, and buzon. Map values to Mistral or ChatGPT. Preserve unresolvable values as `NO_DATA` with cause. Publish the complete value-to-result table with the PR.
2. **New-commit trailers:** propose an optional hook for `Agent` / `Model` / `Run`; absent values become `NO_DATA`. Before acceptance, run it on a test commit and attach its output.
3. **Branch prefix:** record `navegante/*` on app #80, lab #57, and study #26 as a pre-rule historical exception. Do not alter history.
4. **PR state listing:** propose a listing script for PRs lacking state. Acceptance is an attached run with zero rows.
5. **Web budget:** propose one `BUDGET: CEILING` line in web `llms.txt`; confirm the value from signed authority. Acceptance is `check_budgets` passing in app, lab, study, and web.
6. **CI preflight:** propose a clear gate preflight. A missing tool returns `NO_DATA` and a cause.
7. **Chrome timing:** web #308 is reported merged. Attach three consecutive runs at each configured wait (30 s and 60 s) and outer limit (60 s and 90 s), with elapsed times, before closing acceptance.
8. **Commit email privacy:** document the observed personal-address issue and the no-rewrite rule. The Sovereign handles account settings.

## Clarifying objectives A1–A14

The verbatim objective text is now versioned in the source above. Draft one proposal document and one receipt per objective, keeping each artifact below 1,024 UTF-8 bytes. Drafts must preserve the source's pending decisions and measurement gates; they do not authorize implementation. The source's three Mesa constraints are: do not claim browser saves (JSON download is the only measured persistence); permit offline chat only after a service-worker model-cache test; and verify the app Rosetta-file count during the sweep.

## Shared acceptance gates

Cards and receipts stay below 1,024 UTF-8 bytes each. Check keyboard use, 44 px targets, alt text, overlap, reduced motion, and zero page-load external requests. Keep private values, raw prompts, and private network details out of repository artifacts. Screen each artifact for the prohibited vocabulary before submission.

## NO_DATA register

Do not infer the meaning of CLM self-host, reference hardware or RAM, mini-model sizes, remote-node access, or decisions held in private or rack material. Record a cause and seek the Sovereign's datum.

## Collision check

Checked current `study/proposals` filenames and titles on 2026-10-25. No existing ideas25oct orchestrator proposal was found. This check covers the study lane only; other-repository history remains to be audited under item 1.
