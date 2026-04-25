[English](11_CROSS_ANCHOR_TRANSFER.md) | [中文](11_CROSS_ANCHOR_TRANSFER.zh-CN.md)

# Sparse Cross-Anchor Transfer

这份说明覆盖 sparse `10 / 40 / 70 / 100` anchor transfer。

## 摘要表

| Domain | Diagonal gap | Focus off-diagonal gap | Best reusable source anchor |
| --- | ---: | ---: | ---: |
| `math` | `-0.11` pts | `-0.32` pts | `40%` |
| `science` | `-0.77` pts | `-1.98` pts | `100%` |

## 代表性 pair

| Pair | Frozen | Task-specific | Gap |
| --- | ---: | ---: | ---: |
| `math 10→100` | `0.9639` | `0.9658` | `-0.19` pts |
| `math 40→100` | `0.9657` | `0.9658` | `-0.01` pts |
| `science 100→40` | `0.7461` | `0.7468` | `-0.07` pts |
| `science 10→100` | `0.7171` | `0.7731` | `-5.60` pts |

## 当前读法

- `math`：basis 在不同 anchor 之间基本可复用；
- `science`：late-anchor basis 还行，但 early-to-late 明显更弱；
- 这说明 **basis maturity 的问题在不同 domain 上并不一样**。

## 对应结果物

- `results/tables/cross_anchor_transfer_matrix.csv`
- `results/tables/cross_anchor_transfer_deltas.csv`
- `results/tables/cross_anchor_transfer_summary.csv`

