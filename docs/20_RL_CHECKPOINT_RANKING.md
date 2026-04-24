# RL Checkpoint Ranking

这部分在当前仓库里是**支持性证据**，不是主故事。

它的重要性在于：同一类 low-rank latent object，不仅能支持 EarlyStop / transfer 分析，也能对 checkpoint 顺序结构给出可用信号。

## Headline numbers

来自 `results/tables/checkpoint_correlation_summary.csv`：

| Eval split | Spearman ρ | Pearson r | Kendall τ | Top1 | Top3 |
|---|---:|---:|---:|---:|---:|
| `offline_local` | `0.5727` | `0.7633` | `0.4182` | `0` | `0` |
| `blind_eval` | `0.7364` | `0.8398` | `0.6000` | `0` | `0` |

## 当前更稳的读法

- 这组结果说明：低秩表示至少捕捉到了**checkpoint-quality ordering** 的一部分结构。
- 它更适合被写成 supporting evidence，而不是主贡献。
- 当前最可取的口径是：

> The same low-rank object appears to capture checkpoint-order structure, not just early-stop predictability.

## Linear-head sweep

为了让这部分不只停留在“一条相关性摘要”，当前版本还补了一张压缩后的线性头对比表：

- `results/tables/rl_linear_head_summary.csv`
- 代表性脚本：`scripts/run_rl_checkpoint_ranking_linear_heads.py`

### Top heads

| Head | Family | Spearman ρ | Kendall τ | Pearson r | RMSE | ECE |
|---|---|---:|---:|---:|---:|---:|
| `smoothness_regularized_linear` | trajectory | `0.5909` | `0.4909` | `0.8347` | `0.3270` | `0.0175` |
| `fused_lasso_tv_linear` | trajectory | `0.5818` | `0.4545` | `0.8359` | `0.3285` | `0.0196` |
| `elastic_net` | pointwise | `0.5818` | `0.4545` | `0.8316` | `0.3239` | `0.0250` |
| `weak_monotone_linear` | trajectory | `0.5818` | `0.4545` | `0.8263` | `0.3241` | `0.0244` |

### 当前更稳的解释

- 最好的头不是更复杂的黑箱，而仍然是**线性或近线性**结构。
- `smoothness_regularized_linear` 的意义，不在于“绝对领先很多”，而在于：
  - 排序指标最好；
  - calibration 没明显崩；
  - 仍然维持了轻量、可解释的线性头风格。

## 为什么这里现在值得保留

- blind correlation 摘要说明：这个 slice 在线评侧面是成立的；
- linear-head sweep 说明：这个 slice 不是偶然碰出来的一条 baseline，而是经过了一轮 head-space 对照；
- 两者合起来，足够支撑“RL ranking 是 supporting evidence”这个更稳的定位。

## 为什么这里只保留简版

- 原始仓库里 RL 还有更长的 head sweep 与 calibration 分析；
- 这次已经补进了一个**压缩后的线性头摘要表**和代表性脚本；
- 但依然没有把完整 cache / 中间产物一起 vendored 进来。
