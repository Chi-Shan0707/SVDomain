# Results Index

这个目录只保留 README 与核心文档已经直接引用到的结果物。

## 子目录

- `tables/`
  - 论文主结论对应的 summary tables。
- `figures/`
  - 少量可直接在 README / 文档中展示的图。
- `scans/`
  - 当前仅保留 low-rank necessity 对应的机器可读摘要。
- `summary_metrics.json`
  - 一个更小、更聚焦的 headline metrics 摘要。
- `comparison_tables.md`
  - 当前 clean repo 的跨主题摘要表，适合快速浏览。

## 当前分组

### Low-rank

- `tables/lowrank_necessity_ablation.csv`
- `tables/lowrank_smallest_sufficient_rank.csv`
- `figures/lowrank_necessity.png`

### Slot-100 frozen basis transfer

- `tables/frozen_basis_transfer_matrix.csv`
- `tables/frozen_basis_transfer_deltas.csv`
- `figures/frozen_basis_transfer.png`

### Sparse cross-anchor transfer

- `tables/cross_anchor_transfer_matrix.csv`
- `tables/cross_anchor_transfer_deltas.csv`
- `tables/cross_anchor_transfer_summary.csv`
- `figures/sparse_cross_anchor.png`

### Dense-anchor timing

- `tables/dense_anchor_main_table.csv`
- `tables/dense_anchor_earlystop.csv`
- `tables/onset_of_signal.csv`
- `tables/plateau_of_signal.csv`
- `tables/dense_anchor_neuron_vs_legacy.csv`
- `figures/dense_anchor_earlystop_main.png`

### Dense cross-anchor transfer

- `tables/dense_cross_anchor_transfer_matrix.csv`
- `tables/dense_cross_anchor_transfer_deltas.csv`
- `tables/dense_cross_anchor_transfer_summary.csv`

### RL checkpoint ranking

- `tables/checkpoint_correlation_summary.csv`
- `tables/checkpoint_ranking_summary.csv`
- `tables/rl_linear_head_summary.csv`

## 推荐浏览顺序

如果只想快速抓重点，建议：

1. `summary_metrics.json`
2. `comparison_tables.md`
3. 需要展开时再进入 `tables/` 和 `figures/`

## 当前原则

- 只保留正文叙事真正需要的结果；
- 不保留大体积 submission / cache / exploratory tables；
- 后续若继续扩充，优先补“已经在 README 里被提到但尚未收录的最小证据”。
