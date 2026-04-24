# Comparison Tables

这份文件是当前 clean repo 的**跨主题速查表**。

它不试图覆盖原始仓库的所有分支，而只浓缩现在 README 主线真正依赖的几类结果。

## 1. Low-rank sufficiency

| Domain | Best rank | Smallest sufficient rank | Best AUC-of-AUROC | No-SVD AUC-of-AUROC | Reading |
|---|---:|---:|---:|---:|---|
| `math` | `24` | `16` | `0.9595` | `0.9593` | rank `16` 已经基本吃满收益 |
| `science` | `24` | `24` | `0.8367` | `0.8348` | low-rank 有用，但优势温和 |
| `ms` | `24` | `24` | `0.9322` | `0.9316` | 最稳妥的口径是“compact bottleneck” |

## 2. Frozen-basis transfer at slot-100

| Task | Domain | Frozen basis | Task-specific | No-SVD | Reading |
|---|---|---:|---:|---:|---|
| EarlyStop | `math` | `0.9655` | `0.9658` | `0.9668` | near-tie |
| EarlyStop | `science` | `0.7711` | `0.7731` | `0.7798` | still competitive |
| BestOfN | `math` | `0.7917` | `0.8000` | `0.8000` | small gap |
| RL ranking | `math` | `0.5818` | `0.5545` | `0.2636` | cleanest supporting win |

## 3. Sparse cross-anchor transfer

| Domain | Diagonal gap | Focus off-diagonal gap | Best reusable source anchor | Reading |
|---|---:|---:|---:|---|
| `math` | `-0.11` pts | `-0.32` pts | `40%` | broadly reusable across trajectory |
| `science` | `-0.77` pts | `-1.98` pts | `100%` | late-anchor basis is much safer |

Highlighted pairs:

| Pair | Frozen | Task-specific | Gap |
|---|---:|---:|---:|
| `math 10→100` | `0.9639` | `0.9658` | `-0.19` pts |
| `math 40→100` | `0.9657` | `0.9658` | `-0.01` pts |
| `science 100→40` | `0.7461` | `0.7468` | `-0.07` pts |
| `science 10→100` | `0.7171` | `0.7731` | `-5.60` pts |

## 4. Dense cross-anchor transfer

| Domain | Diagonal gap | Offdiag-all gap | Near-gap | Far-gap | Best source anchor |
|---|---:|---:|---:|---:|---:|
| `math` | `-0.13` pts | `-0.34` pts | `-0.16` pts | `-0.62` pts | `30%` |
| `science` | `-0.09` pts | `-0.54` pts | `-0.23` pts | `-0.97` pts | `50%` |

Current reading:

- `math`：shared basis 几乎贯穿全 trajectory；
- `science`：shared basis 存在，但更依赖 basis maturity；
- 最有意思的一点是：**最可迁移 basis 往往在中段，而不是最后一个 anchor。**

## 5. Dense-anchor timing

| Domain | AUC-of-AUROC | AUROC@10% | AUROC@100% | Onset 95%-of-final | Plateau | Reading |
|---|---:|---:|---:|---:|---:|---|
| `math` | `0.9677` | `0.9357` | `0.9817` | `10%` | `50%` | early-saturating |
| `science` | `0.8269` | `0.7673` | `0.8411` | `20%` | `40%` | early-usable, later-refined |
| `coding` | `0.4321` | `0.4656` | `0.4068` | `10%*` | `100%` | boundary-case / weak curve |

## 6. RL ranking snapshot

### Blind / offline summary

| Split | Spearman ρ | Pearson r | Kendall τ |
|---|---:|---:|---:|
| `offline_local` | `0.5727` | `0.7633` | `0.4182` |
| `blind_eval` | `0.7364` | `0.8398` | `0.6000` |

### Linear-head sweep winner

| Head | Family | Spearman ρ | Kendall τ | Pearson r | RMSE | ECE |
|---|---|---:|---:|---:|---:|---:|
| `smoothness_regularized_linear` | trajectory | `0.5909` | `0.4909` | `0.8347` | `0.3270` | `0.0175` |

## Reading note

如果只保留一句总括，那就是：

> `SVD_Domain` 当前最干净的故事，不是“one basis solves everything”，而是“moderate low rank yields a compact latent object whose reuse depends strongly on domain and anchor maturity, while still remaining useful beyond EarlyStop in supporting tasks such as checkpoint ranking.”

