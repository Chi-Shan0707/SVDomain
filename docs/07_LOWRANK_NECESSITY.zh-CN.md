[English](07_LOWRANK_NECESSITY.md) | [中文](07_LOWRANK_NECESSITY.zh-CN.md)

# Low-Rank Necessity

这份说明只回答一个问题：收益到底来自 low-rank bottleneck，还是只是来自同一套 feature bank。

## 主表

| Domain | Best rank | Smallest sufficient rank | Best AUC-of-AUROC | No-SVD AUC-of-AUROC |
| --- | ---: | ---: | ---: | ---: |
| `math` | `24` | `16` | `0.9595` | `0.9593` |
| `science` | `24` | `24` | `0.8367` | `0.8348` |
| `ms` | `24` | `24` | `0.9322` | `0.9316` |

## 当前更稳的读法

- bottleneck 本身是有用的，但优势并不夸张。
- 真正有用的区间已经集中在 `16–24`。
- 这部分最适合写成 **compact and sufficient**, 而不是“低秩全面压制所有 baseline”。

## 对应结果物

- `results/tables/lowrank_necessity_ablation.csv`
- `results/tables/lowrank_smallest_sufficient_rank.csv`
- `results/scans/lowrank_necessity/lowrank_necessity_summary.json`

