# SVD_Domain

一个从原始 `SVDomain` 中**选择性整理**出来的、以证据为中心的精简仓库。

这个版本不再追求“把所有实验痕迹都公开出来”，而是优先保留：
- 能直接支撑主要结论的文档与结果表；
- 少量能说明方法入口的公开脚本；
- 一套更干净、更容易浏览的目录骨架。

## 这个仓库现在讲什么

当前公开版本主要聚焦 **math / science** 上比较稳的几条结论：

| 主题 | 当前更稳妥的说法 | 对应证据 |
|---|---|---|
| Low-rank sufficiency | 低秩有用，但更准确的表述是“中等 rank 已经足够”，不是“无条件大胜” | `results/tables/lowrank_smallest_sufficient_rank.csv` |
| Frozen basis transfer | 一个固定 basis 往往只需换线性头就能复用；math 几乎无损，science 仍然接近 | `results/tables/frozen_basis_transfer_deltas.csv` |
| Sparse cross-anchor transfer | `math` 的 basis 基本贯穿整条 trajectory 可复用；`science` 更依赖 basis 成熟度 | `results/tables/cross_anchor_transfer_summary.csv` |
| Dense cross-anchor transfer | 最可迁移的 basis 往往不是最后一个 anchor，而是中段 anchor | `results/tables/dense_cross_anchor_transfer_summary.csv` |
| Dense-anchor timing | `math` 很早就趋于饱和；`science` 则是“早期已有信号，后期继续 refinement” | `results/tables/dense_anchor_main_table.csv` |
| RL checkpoint ranking | 这是支持性证据，不是主故事，但它说明同一 latent object 也能刻画 checkpoint 顺序结构 | `results/tables/checkpoint_correlation_summary.csv` |

## README 级别的核心发现

### 1. 低秩更像“紧凑瓶颈”，而不是神奇替代

- `math`：best rank = `24`，但 smallest sufficient rank 已经是 `16`。
- `science`：smallest sufficient rank = `24`。
- `ms`：smallest sufficient rank = `24`。
- 更诚实的说法是：**rank `16–24` 已经吃到了主要收益**，低秩的价值更体现在紧凑、可迁移、可解释。

### 2. Slot-100 的 frozen basis transfer 是成立的

- `earlystop / math`：frozen basis `0.9655`，task-specific `0.9658`，基本可视为 near-tie。
- `earlystop / science`：`0.7711` vs `0.7731`，仍然很接近。
- `rl_ranking / math`：frozen basis `ρ = 0.5818`，优于 task-specific `0.5545`，也显著高于 `no_svd = 0.2636`。

### 3. Basis transfer 不是只出现在最终 anchor

- sparse 版本里：
  - `math` diagonal mean gap 只有 `-0.11` pts；
  - `science` diagonal mean gap 是 `-0.77` pts；
  - `math 10→100` 仍只有 `-0.19` pts；
  - `science 10→100` 会掉到 `-5.60` pts。
- dense 版本里：
  - `math` 最可迁移 source anchor 是 `30%`；
  - `science` 最可迁移 source anchor 是 `50%`。

最值得保留的一句总结是：

> 最可迁移的 basis 往往不是最后一个 anchor，而是已经成熟、但尚未被 completion-specific 信息过度塑形的中段 basis。

### 4. Dense-anchor timing 给出了一个很干净的对照

- `math`：
  - `AUC-of-AUROC = 0.9677`
  - `10%` 时 AUROC 已有 `0.9357`
  - `10%` 就达到 final AUROC 的 `95%`
  - `50%` 左右进入 plateau
- `science`：
  - `AUC-of-AUROC = 0.8269`
  - `10%` 时 AUROC 为 `0.7673`
  - `20%` 达到 final AUROC 的 `95%`
  - `40%` 左右进入 plateau

这组结果最适合被表述为：
- `math` 是 **early-saturating**
- `science` 是 **early-usable but later-refined**

## 仓库骨架

```text
SVD_Domain/
├── README.md
├── docs/
│   ├── README.md
│   ├── 00_EXECUTIVE_SUMMARY.md
│   ├── 07_LOWRANK_NECESSITY.md
│   ├── 08_FROZEN_BASIS_TRANSFER.md
│   ├── 11_CROSS_ANCHOR_TRANSFER.md
│   ├── 16_DENSE_ANCHOR_EARLYSTOP.md
│   ├── 17_DENSE_CROSS_ANCHOR_TRANSFER.md
│   └── 20_RL_CHECKPOINT_RANKING.md
├── results/
│   ├── README.md
│   ├── tables/
│   ├── figures/
│   └── scans/
├── scripts/
│   └── README.md
├── svdomain/
│   └── README.md
└── run_*.py
```

## 这次清洗的边界

- **保留**：论文叙事里最稳定、最能被现有表格直接支撑的证据。
- **暂不强调**：coding 分支。原始材料里这部分结论还不够稳定，不适合作为当前 README 主线。
- **不内置**：完整 cache、submission 文件、viewer、workshop 草稿、大量 exploratory notes。

## 复现边界

根目录下保留的 `run_*.py` 是**公开入口包装器**，便于说明方法和输出协议；但完整复现仍依赖外部 `NAD_Next` 代码栈与本地 cache / model artifacts。

因此，这个仓库更准确的定位是：

> 一个可浏览、可引用、可继续清洗扩展的 evidence pack，而不是一次性 vendored 完整训练环境。

## 导航

- 文档索引：`docs/README.md`
- 结果索引：`results/README.md`
- 本地 bootstrap 说明：`svdomain/README.md`

