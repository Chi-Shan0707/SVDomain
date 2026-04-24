# Executive Summary

`SVD_Domain` 是从原始 `SVDomain` 中整理出来的一个**精简证据仓库**。

它当前更合适的定位，不是“已经完成全部主张的完整论文代码仓”，而是：

> 一个围绕 low-rank basis、basis transfer、anchor maturity 与 checkpoint-order structure 的公开 evidence pack。

## 当前最稳的结论

### 1. Moderate low rank is already sufficient

- `math` 的 smallest sufficient rank 是 `16`；
- `science` 和 `ms` 的 smallest sufficient rank 都是 `24`；
- 所以更稳的说法是：**rank `16–24` 已经足够**。

### 2. Frozen basis transfer is real

- `math` 与 `science` 的 slot-100 EarlyStop 上，frozen basis 与 task-specific 基本接近；
- `RL ranking / math` 上，frozen basis 反而更强：`ρ = 0.5818` vs `0.5545`。

### 3. Cross-anchor transfer has domain asymmetry

- `math` 的 basis 在整条 trajectory 上更可复用；
- `science` 的 basis 更依赖成熟度，尤其 early-to-late 的迁移更容易退化。

### 4. The best transferable basis is often mid-trajectory

- dense 网格里，`math` 最优 source anchor 是 `30%`；
- `science` 最优 source anchor 是 `50%`。

这说明 basis transfer 不是“最终 anchor 独有的现象”。

### 5. Dense-anchor timing tells a clean story

- `math`：早期强信号，`10%` 就达到 final AUROC 的 `95%`，`50%` 左右 plateau；
- `science`：`10%` 已可用，但后期继续 refinement，`20%` 达到 `95% final`，`40%` 左右 plateau。

## 当前不主打什么

- 不主打 coding。
- 不主打“单一 basis 解决一切”。
- 不主打“low-rank 在所有指标上严格优于 no-SVD”。

## 这个仓库保留什么

- 可直接引用的说明文档；
- 少量 summary tables / figures；
- 少量公开 wrapper 脚本；
- 一个更干净的目录骨架，便于后续继续增量清洗。

