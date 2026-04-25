# Comparison Tables

This file is the quickest way to scan the current public subset.

## 1. Low-rank sufficiency

| Domain | Best rank | Smallest sufficient rank | Best AUC-of-AUROC | No-SVD AUC-of-AUROC |
| --- | ---: | ---: | ---: | ---: |
| `math` | `24` | `16` | `0.9595` | `0.9593` |
| `science` | `24` | `24` | `0.8367` | `0.8348` |
| `ms` | `24` | `24` | `0.9322` | `0.9316` |

## 2. Frozen-basis transfer at slot 100

| Task | Domain | Frozen basis | Task-specific | No-SVD |
| --- | --- | ---: | ---: | ---: |
| EarlyStop | `math` | `0.9655` | `0.9658` | `0.9668` |
| EarlyStop | `science` | `0.7711` | `0.7731` | `0.7798` |
| BestOfN | `math` | `0.7917` | `0.8000` | `0.8000` |
| RL ranking | `math` | `0.5818` | `0.5545` | `0.2636` |

## 3. Sparse cross-anchor transfer

| Domain | Diagonal gap | Focus off-diagonal gap | Best reusable source anchor |
| --- | ---: | ---: | ---: |
| `math` | `-0.11` pts | `-0.32` pts | `40%` |
| `science` | `-0.77` pts | `-1.98` pts | `100%` |

## 4. Dense cross-anchor transfer

| Domain | Diagonal gap | Off-diagonal gap | Near-gap | Far-gap | Best source anchor |
| --- | ---: | ---: | ---: | ---: | ---: |
| `math` | `-0.13` pts | `-0.34` pts | `-0.16` pts | `-0.62` pts | `30%` |
| `science` | `-0.09` pts | `-0.54` pts | `-0.23` pts | `-0.97` pts | `50%` |

## 5. Dense-anchor timing

| Domain | AUC-of-AUROC | AUROC @ 10% | AUROC @ 100% | 95%-of-final anchor | Plateau |
| --- | ---: | ---: | ---: | ---: | ---: |
| `math` | `0.9677` | `0.9357` | `0.9817` | `10%` | `50%` |
| `science` | `0.8269` | `0.7673` | `0.8411` | `20%` | `40%` |
| `coding` | `0.4321` | `0.4656` | `0.4068` | `10%*` | `100%` |

## 6. RL checkpoint ranking

| Split | Spearman ρ | Pearson r | Kendall τ |
| --- | ---: | ---: | ---: |
| `offline_local` | `0.5727` | `0.7633` | `0.4182` |
| `blind_eval` | `0.7364` | `0.8398` | `0.6000` |

| Head | Family | Spearman ρ | Kendall τ | Pearson r | RMSE | ECE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `smoothness_regularized_linear` | trajectory | `0.5909` | `0.4909` | `0.8347` | `0.3270` | `0.0175` |

## One-line reading

The clean story is not “one basis solves everything.” The clean story is that a moderate low-rank basis becomes reusable in a way that depends strongly on domain and anchor maturity.

