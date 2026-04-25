[English](17_DENSE_CROSS_ANCHOR_TRANSFER.md) | [中文](17_DENSE_CROSS_ANCHOR_TRANSFER.zh-CN.md)

# Dense Cross-Anchor Transfer

这份说明把 sparse `10 / 40 / 70 / 100` 的迁移故事扩展到 dense `10 / 20 / ... / 100` 网格。

## 主表

| Domain | Diagonal gap | Off-diagonal gap | Near-gap | Far-gap | Best source anchor |
| --- | ---: | ---: | ---: | ---: | ---: |
| `math` | `-0.13` pts | `-0.34` pts | `-0.16` pts | `-0.62` pts | `30%` |
| `science` | `-0.09` pts | `-0.54` pts | `-0.23` pts | `-0.97` pts | `50%` |

## 当前读法

- `math`：basis 在大部分 trajectory 上都还能复用；
- `science`：late-to-earlier 更稳，early-to-late 更容易退化；
- dense 网格最有价值的地方在于：**最可迁移的 anchor 往往在中段，而不是 `100%`。**

## 最好 / 最差 pair

| Domain | Best pair | Worst pair |
| --- | --- | --- |
| `math` | `60→100` (`+0.01`) | `100→10` (`-2.51`) |
| `science` | `100→90` (`+0.26`) | `10→50` (`-4.17`) |

## 对应结果物

- `results/tables/dense_cross_anchor_transfer_matrix.csv`
- `results/tables/dense_cross_anchor_transfer_deltas.csv`
- `results/tables/dense_cross_anchor_transfer_summary.csv`

