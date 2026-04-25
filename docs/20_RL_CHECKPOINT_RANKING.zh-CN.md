[English](20_RL_CHECKPOINT_RANKING.md) | [中文](20_RL_CHECKPOINT_RANKING.zh-CN.md)

# RL Checkpoint Ranking

这是一条 supporting branch，不是主标题。它的价值在于：同一类 low-rank object 不只对 EarlyStop 有用，对 checkpoint 顺序结构也有可用信号。

## 相关性摘要

| Split | Spearman ρ | Pearson r | Kendall τ |
| --- | ---: | ---: | ---: |
| `offline_local` | `0.5727` | `0.7633` | `0.4182` |
| `blind_eval` | `0.7364` | `0.8398` | `0.6000` |

## 线性头 sweep

| Head | Family | Spearman ρ | Kendall τ | Pearson r | RMSE | ECE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `smoothness_regularized_linear` | trajectory | `0.5909` | `0.4909` | `0.8347` | `0.3270` | `0.0175` |
| `fused_lasso_tv_linear` | trajectory | `0.5818` | `0.4545` | `0.8359` | `0.3285` | `0.0196` |
| `elastic_net` | pointwise | `0.5818` | `0.4545` | `0.8316` | `0.3239` | `0.0250` |

## 当前读法

- 最好的结果依然来自线性或近线性头；
- 这里最重要的不是“某个 head 遥遥领先”；
- 而是 checkpoint-order signal 在紧凑、可解释的设定下仍然存在。

## 对应结果物

- `results/tables/checkpoint_correlation_summary.csv`
- `results/tables/checkpoint_ranking_summary.csv`
- `results/tables/rl_linear_head_summary.csv`
- `scripts/run_rl_checkpoint_ranking_linear_heads.py`

