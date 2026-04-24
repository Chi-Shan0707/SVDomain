# Docs Index

这个目录只保留当前公开版本最核心的几份说明文档。

## 包含哪些文档

- `00_EXECUTIVE_SUMMARY.md`
  - 一页式总览：这个精简仓库现在到底想讲什么。
- `07_LOWRANK_NECESSITY.md`
  - 低秩 bottleneck 是否真的有用，smallest sufficient rank 大约在哪里。
- `08_FROZEN_BASIS_TRANSFER.md`
  - slot-100 上，固定 basis + 新线性头是否足够。
- `11_CROSS_ANCHOR_TRANSFER.md`
  - sparse `10 / 40 / 70 / 100` anchor 上的迁移现象。
- `16_DENSE_ANCHOR_EARLYSTOP.md`
  - 什么时候信号开始可用，什么时候进入 plateau。
- `17_DENSE_CROSS_ANCHOR_TRANSFER.md`
  - dense `10 / 20 / ... / 100` 网格下 basis maturity 的更细解释。
- `20_RL_CHECKPOINT_RANKING.md`
  - RL checkpoint ranking 的支持性证据，包括 blind correlation 与线性头 sweep 摘要。

## 阅读顺序

建议按下面顺序读：

1. `00_EXECUTIVE_SUMMARY.md`
2. `07_LOWRANK_NECESSITY.md`
3. `08_FROZEN_BASIS_TRANSFER.md`
4. `11_CROSS_ANCHOR_TRANSFER.md`
5. `17_DENSE_CROSS_ANCHOR_TRANSFER.md`
6. `16_DENSE_ANCHOR_EARLYSTOP.md`
7. `20_RL_CHECKPOINT_RANKING.md`

## 当前策略

这个目录有意不再收录大量实验备忘录、battle history、workshop 草稿或 late-round exploratory notes。
