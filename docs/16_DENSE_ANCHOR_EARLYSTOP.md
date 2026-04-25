[English](16_DENSE_ANCHOR_EARLYSTOP.md) | [中文](16_DENSE_ANCHOR_EARLYSTOP.zh-CN.md)

# Dense-Anchor EarlyStop

This note compresses the dense-anchor EarlyStop results into the small set of numbers that matter for the cleaned repo.

## Main table

| Domain | AUC-of-AUROC | AUROC @ 10% | AUROC @ 100% | 95%-of-final anchor | Plateau | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `math` | `0.9677` | `0.9357` | `0.9817` | `10%` | `50%` | early-saturating |
| `science` | `0.8269` | `0.7673` | `0.8411` | `20%` | `40%` | early-usable, later-refined |
| `coding` | `0.4321` | `0.4656` | `0.4068` | `10%*` | `100%` | weak boundary case |

## Reading

- Math already contains strong signal very early.
- Science has useful early signal, but late anchors still refine the decision boundary.
- Coding remains weak under the current feature family and is not the headline branch in this repo.

## Artifacts

- `results/tables/dense_anchor_main_table.csv`
- `results/tables/dense_anchor_earlystop.csv`
- `results/tables/onset_of_signal.csv`
- `results/tables/plateau_of_signal.csv`
- `results/figures/dense_anchor_earlystop_main.png`

