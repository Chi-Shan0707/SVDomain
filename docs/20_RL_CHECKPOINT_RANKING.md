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

## 为什么这里只保留简版

- 原始仓库里 RL 还有更长的 head sweep 与 calibration 分析；
- 但在这次精简版里，先保留最容易引用的相关性摘要；
- 更长的 head benchmark 可以在后续提交中再补回。

