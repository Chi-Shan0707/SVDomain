[English](16_DENSE_ANCHOR_EARLYSTOP.md) | [中文](16_DENSE_ANCHOR_EARLYSTOP.zh-CN.md)

# Dense-Anchor EarlyStop

这份说明把 dense-anchor EarlyStop 压缩成当前仓库真正需要的那几组数字。

## 主表

| Domain | AUC-of-AUROC | AUROC @ 10% | AUROC @ 100% | 95%-of-final anchor | Plateau | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `math` | `0.9677` | `0.9357` | `0.9817` | `10%` | `50%` | 很早饱和 |
| `science` | `0.8269` | `0.7673` | `0.8411` | `20%` | `40%` | 早期可用，后期继续 refinement |
| `coding` | `0.4321` | `0.4656` | `0.4068` | `10%*` | `100%` | 弱域 / 边界案例 |

## 当前读法

- `math`：很早就已经有强信号；
- `science`：早期已有信号，但后期仍会继续抬升；
- `coding`：在当前特征家族下仍然偏弱，不适合作为主线。

## 对应结果物

- `results/tables/dense_anchor_main_table.csv`
- `results/tables/dense_anchor_earlystop.csv`
- `results/tables/onset_of_signal.csv`
- `results/tables/plateau_of_signal.csv`
- `results/figures/dense_anchor_earlystop_main.png`

