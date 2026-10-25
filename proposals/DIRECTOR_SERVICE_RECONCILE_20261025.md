# director.service reconcile plan (ES: plan de reconciliación)

**State:** proposal only; no p0x file or service changed.

Observed divergence: local p0x `HEAD` is 406 commits ahead and 345 behind GitHub `origin/master`. Its working checkout has 2 modified tracked files, 916 untracked items, and 556 ignored items. Preserve all of them; keep the path-and-hash inventory local. The local `HEAD`, GitHub unit, and installed user unit have identical bytes (1,509 B; SHA-256 recorded in the receipt), though the repository paths differ. No unit content edit is currently justified.

**Proposed sequence:** freeze the checkout; do not reset, clean, pull, rebase, or merge it. Ask the owner to select the canonical lineage and unit path. After that decision, use an isolated worktree from the selected base and transfer only the approved unit/path change. Review the staged diff, run the p0x hygiene hook and a unit syntax check, then return the result for per-PR FIRMO. No service reload or deployment before sign-off. Preserve the original checkout throughout.

## Receipt

source=study#61/R3; p0x_head=2d44943; origin_master=9656ff3; ahead=406; behind=345; tracked_modified=2; untracked=916; ignored=556; unit_bytes=1509; unit_sha256=390ee744b37215dff623c94d839be0bd2ef1553166e605a30c01a789b83ef4b4; repo_path_match=0; user_unit=loaded/failed; dropins=0; failure_cause=NO_DATA; p0x_changes=0; state=proposal
