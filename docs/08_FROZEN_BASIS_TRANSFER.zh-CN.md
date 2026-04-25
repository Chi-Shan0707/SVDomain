[English](08_FROZEN_BASIS_TRANSFER.md) | [中文](08_FROZEN_BASIS_TRANSFER.zh-CN.md)

# Frozen-Basis Transfer

这份说明总结的是 slot `100` 上的 frozen-basis 实验：basis 固定，只重训最后一层线性头。

## 核心对比

| Task | Domain | Frozen basis | Task-specific | No-SVD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| EarlyStop | `math` | `0.9655` | `0.9658` | `0.9668` | 基本持平 |
| EarlyStop | `science` | `0.7711` | `0.7731` | `0.7798` | 仍然接近 |
| BestOfN | `math` | `0.7917` | `0.8000` | `0.8000` | 小幅落后 |
| RL ranking | `math` | `0.5818` | `0.5545` | `0.2636` | 最干净的支持性胜出 |

## 当前更合适的口径

- math / science 的 EarlyStop 可以支持 shared-basis reuse；
- RL ranking 是这里最漂亮的一项 supporting evidence；
- coding 不适合在这一页被当成主卖点。

## 对应结果物

- `results/tables/frozen_basis_transfer_matrix.csv`
- `results/tables/frozen_basis_transfer_deltas.csv`
- `results/figures/frozen_basis_transfer.png`

