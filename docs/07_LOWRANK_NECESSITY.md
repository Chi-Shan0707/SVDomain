[English](07_LOWRANK_NECESSITY.md) | [中文](07_LOWRANK_NECESSITY.zh-CN.md)

# Low-Rank Necessity

This note asks one question: does the gain come from the low-rank bottleneck itself, or only from the feature bank?

## Main table

| Domain | Best rank | Smallest sufficient rank | Best AUC-of-AUROC | No-SVD AUC-of-AUROC |
| --- | ---: | ---: | ---: | ---: |
| `math` | `24` | `16` | `0.9595` | `0.9593` |
| `science` | `24` | `24` | `0.8367` | `0.8348` |
| `ms` | `24` | `24` | `0.9322` | `0.9316` |

## Practical reading

- The bottleneck helps, but the gain is modest.
- The useful regime is already visible by rank `16–24`.
- The right takeaway is **compactness and sufficiency**, not “SVD dominates every baseline”.

## Why this matters

- Very low rank (`r2 / r4 / r8`) is clearly too small.
- Very high rank is not necessary for the main effect.
- For the cleaned repo, this is one of the most stable pieces of evidence.

## Artifacts

- `results/tables/lowrank_necessity_ablation.csv`
- `results/tables/lowrank_smallest_sufficient_rank.csv`
- `results/scans/lowrank_necessity/lowrank_necessity_summary.json`

