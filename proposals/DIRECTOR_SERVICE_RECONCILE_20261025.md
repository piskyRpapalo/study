# director.service reconcile plan (ES: plan de reconciliación)

**State:** proposal only; no p0x file or service changed.

Observed: p0x `HEAD` is 406 ahead and 345 behind GitHub `origin/master`; checkout status is 2 modified tracked, 916 untracked, and 556 ignored items. Preserve all; keep the path-and-hash inventory local. Local `HEAD`, GitHub, and installed user unit are byte-identical (1,509 B; hash in receipt) but repository paths differ. No content edit is justified.

**Proposed sequence:** freeze; do not reset, clean, pull, rebase, or merge. The owner selects canonical lineage and unit path. After approval, use an isolated worktree from that base; transfer only the approved unit/path change. Review the staged diff; run the p0x hygiene hook and unit syntax check; submit for per-PR FIRMO. No reload or deployment before sign-off. Preserve the original checkout.

## Receipt

source=study#61/R3; p0x_head=2d44943; origin_master=9656ff3; ahead=406; behind=345; tracked_modified=2; untracked=916; ignored=556; unit_bytes=1509; unit_sha256=390ee744b37215dff623c94d839be0bd2ef1553166e605a30c01a789b83ef4b4; repo_path_match=0; user_unit=loaded/failed; dropins=0; failure_cause=NO_DATA; p0x_changes=0; state=proposal
