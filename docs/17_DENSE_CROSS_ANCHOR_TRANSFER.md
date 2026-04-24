# Dense Cross-Anchor Transfer

This note upgrades the earlier sparse `10 / 40 / 70 / 100` cross-anchor analysis into a dense all-to-all `10 / 20 / ... / 100` transfer grid for `es_svd_ms_rr_r2`. The purpose is to answer a sharper paper question: is reusable basis transfer only a slot-100 phenomenon, or does it remain visible across the full reasoning trajectory?

## 1. Paper-facing assets

- Main note: `docs/17_DENSE_CROSS_ANCHOR_TRANSFER.md`
- Standalone runner: `run_dense_cross_anchor_transfer.py`
- Canonical implementation: sibling `NAD_Next/SVDomain/experiments/run_dense_cross_anchor_transfer.py`
- Tables:
  - `results/tables/dense_cross_anchor_transfer_matrix.csv`
  - `results/tables/dense_cross_anchor_transfer_deltas.csv`
  - `results/tables/dense_cross_anchor_transfer_summary.csv`

The standalone runner preserves the public `SVDomain` entrypoint while delegating to the canonical implementation through `NAD_NEXT_ROOT`.

## 2. Headline summary

| Domain | Diagonal mean Δ(frozen − task-specific) | All off-diagonal mean Δ | Near-gap Δ (`10 / 20`) | Far-gap Δ (`50–90`) | Best reusable source anchor |
|---|---:|---:|---:|---:|---:|
| `math` | `-0.13` AUC-pts | `-0.34` AUC-pts | `-0.16` AUC-pts | `-0.62` AUC-pts | `30%` |
| `science` | `-0.09` AUC-pts | `-0.54` AUC-pts | `-0.23` AUC-pts | `-0.97` AUC-pts | `50%` |

Main reading:

- In `math`, the frozen basis remains close to the task-specific one even under dense all-to-all transfer.
- In `science`, transfer is still real and clearly not limited to `100%`, but degradation grows faster with anchor distance and is much more directional.
- The cleanest paper sentence is therefore **not** “transfer only appears at slot-100,” but rather **math = broadly reusable across trajectory; science = shared but maturity-sensitive reusable basis**.

## 3. Direction and distance

| Domain | Forward all mean gap | Backward all mean gap | Best off-diagonal pair | Worst off-diagonal pair |
|---|---:|---:|---|---|
| `math` | `-0.11` AUC-pts | `-0.56` AUC-pts | `60→100` (`+0.01`) | `100→10` (`-2.51`) |
| `science` | `-0.98` AUC-pts | `-0.10` AUC-pts | `100→90` (`+0.26`) | `10→50` (`-4.17`) |

Interpretation:

- `math` transfer is stable when moving forward to later targets; most of the loss appears in long-range late-to-early reuse.
- `science` transfer is strongly asymmetric: late-to-earlier reuse stays fairly stable, but early-to-later reuse degrades rapidly.
- This asymmetry is the key dense result. It shows that early science anchors already contain meaningful signal, but their basis has not yet matured into a representation that can be reused without noticeable loss at later anchors.

## 4. Source-anchor ranking

### Math source-anchor ranking by mean off-diagonal Δ(frozen − task-specific)

`30% (-0.14)` > `40% (-0.17)` > `20% (-0.18)` > `50% (-0.22)` > `60% (-0.26)` > `10% (-0.27)` > `70% (-0.34)` > `80% (-0.41)` > `90% (-0.52)` > `100% (-0.87)`

### Science source-anchor ranking by mean off-diagonal Δ(frozen − task-specific)

`50% (-0.02)` > `60% (-0.02)` > `70% (-0.03)` > `40% (-0.03)` > `80% (-0.05)` > `100% (-0.09)` > `90% (-0.10)` > `30% (-0.10)` > `20% (-1.37)` > `10% (-3.60)`

Interpretation:

- In `math`, the best reusable source anchor sits in the early-middle regime (`30–40%`), not at the latest `100%` anchor.
- In `science`, the best reusable source anchor is no longer the isolated `100%` anchor seen in the sparse four-anchor study, but a cluster of mid/late-middle anchors around `50–80%`.
- The dense grid therefore sharpens the sparse story: the most transferable basis is often **not** the final anchor, but a mature mid-trajectory anchor that has not yet been overly shaped by completion-specific information.

## 5. Recommended paper sentence

> Dense cross-anchor transfer shows that reuse is not a slot-100-only effect. In math, the frozen basis remains close to the task-specific one across the full `10 / 20 / ... / 100` trajectory, with a diagonal mean gap of only `-0.13` AUC points and an all off-diagonal mean gap of `-0.34`; the best reusable source anchor is `30%`. In science, transfer remains real but more direction-sensitive: the diagonal mean gap is `-0.09`, the all off-diagonal mean gap is `-0.54`, and early-to-late transfer degrades much more than late-to-early transfer, with the best source anchors concentrated around `50–70%`.

## 6. Link to dense timing

This result should be read together with `docs/16_DENSE_ANCHOR_EARLYSTOP.md`:

- `math` reaches 95%-of-final AUROC at `10%` and plateaus around `50%`, which matches the weak distance-decay seen under dense transfer.
- `science` reaches 95%-of-final AUROC at `20%` and plateaus around `40%`, which matches the picture of early coarse signal plus late basis refinement.

The combined reading is:

> Dense anchors show that math saturates early and remains cross-anchor reusable throughout the trajectory, whereas science exhibits early usable signal but a more maturity-dependent reusable basis.
