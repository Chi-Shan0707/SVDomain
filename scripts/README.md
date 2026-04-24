# Scripts

这个目录在第一轮清洗里先作为**骨架目录**保留。

当前策略是：

- 先保留根目录的 `run_*.py` 作为最小公开入口；
- 复杂、依赖较重、需要更多外部私有环境的脚本，后续再按需挑选加入；
- 避免一开始就把大量脚本与隐藏依赖一起推上去。

## 当前公开入口

- `../run_lowrank_necessity_ablation.py`
- `../run_cross_anchor_transfer.py`
- `../run_dense_anchor_earlystop.py`
- `../run_dense_cross_anchor_transfer.py`
- `run_rl_checkpoint_ranking_linear_heads.py`

这些脚本更多是**方法入口与输出协议说明**，而不是“开箱即用的完整复现环境”。

## 额外保留的代表性脚本

- `run_rl_checkpoint_ranking_linear_heads.py`
  - 当前保留下来的少数较完整脚本之一；
  - 它对应 `docs/20_RL_CHECKPOINT_RANKING.md` 里的 linear-head sweep；
  - 保留它，是因为它相对自洽，且确实有助于别人理解 RL ranking 这条 supporting branch。
