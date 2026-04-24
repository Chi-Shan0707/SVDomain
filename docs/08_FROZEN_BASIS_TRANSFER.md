# 08 — Frozen-Basis Transfer

**Compact-repo status**: artifact note  
**What is kept here**:
  - `results/tables/frozen_basis_transfer_matrix.csv`
  - `results/tables/frozen_basis_transfer_deltas.csv`
  - `results/figures/frozen_basis_transfer.png`
**Provenance note**: 原始实验依赖内部 bundle / cache；本仓库当前保留的是可公开引用的结果物与说明。  
**Date**: 2026-04-11

---

## 1. Claim Under Test

> *A shared low-rank basis + lightweight task head replaces task-specific SVD pipelines.*

The SVDomain paper asserts that a single scaler+SVD trained on math reasoning runs
provides a **transferable** low-rank feature space for downstream tasks (EarlyStop,
Best-of-N, RL checkpoint ranking).  This experiment operationalises that claim with a
controlled 3-way ablation.

---

## 2. Experimental Protocol

### Three Conditions (per task × domain)

| Condition | Scaler+SVD | LR head | Description |
|-----------|------------|---------|-------------|
| `frozen_basis` | **frozen** (math route, slot-100) | retrained per CV fold | Core claim: only the head adapts |
| `task_specific` | **retrained** per fold | retrained per fold | Upper bound |
| `no_svd` | — | retrained per fold (no dim-red) | Lower bound |

### Cross-Validation
- EarlyStop / BestofN: GroupKFold, `n_splits=5`, groups = `cache_key::problem_id`
- RL ranking: 11-fold leave-one-checkpoint-out; Spearman ρ across all 11 checkpoints

### Frozen Basis Configuration
- Source: math route of `es_svd_ms_rr_r1`, slot-9 (100%)
- Feature family: `token_plus_traj` (22 features), representation: `raw+rank` → 44-dim input
- Rank: 16 components, whiten: False
- Source route CV-AUROC: **0.9567** (trained on math+science combined)

### Tasks and Metrics

| Task | Domain | n_samples | n_groups | Metric |
|------|--------|-----------|----------|--------|
| `earlystop` | math | 7 680 | 120 | AUROC |
| `earlystop` | science | 12 672 | 198 | AUROC |
| `earlystop` | coding | 10 688 | 167 | AUROC |
| `bestofn` | math | 7 680 | 120 | hit@1 |
| `rl_ranking` | math | 70 400 | 11 ckpts | Spearman ρ |

---

## 3. Transfer Matrix

| task | domain | frozen_basis | task_specific | no_svd | n_folds |
|------|--------|:------------:|:-------------:|:------:|:-------:|
| earlystop | math | **0.9655** | 0.9658 | 0.9668 | 5 |
| earlystop | science | **0.7711** | 0.7731 | 0.7798 | 5 |
| earlystop | coding | **0.4982** | 0.4915 | 0.4910 | 5 |
| bestofn | math | **0.7917** | 0.8000 | 0.8000 | 5 |
| rl_ranking | math | **0.5818** | 0.5545 | 0.2636 | 11 |

*std values: earlystop/math ≈0.011, earlystop/science ≈0.058, earlystop/coding ≈0.082, bestofn/math ≈0.026–0.031*

---

## 4. Delta Summary

| task | domain | metric | Δ (fb − task_specific) | Δ (fb − no_svd) | verdict |
|------|--------|--------|------------------------|-----------------|---------|
| earlystop | math | auroc | **−0.0003** | −0.0013 | **tie** |
| earlystop | science | auroc | **−0.0020** | −0.0087 | **tie** |
| earlystop | coding | auroc | **+0.0067** | +0.0073 | **win** |
| bestofn | math | hit@1 | **−0.0083** | −0.0083 | **tie** |
| rl_ranking | math | spearman_ρ | **+0.0273** | +0.3182 | **win** |

*Verdict thresholds: win ≥ 0, tie ≥ −0.02, loss < −0.02.*

---

## 5. Verdict

### 5.1 Summary

**4 out of 5 tasks are win or tie; 0 losses.**

| Task | Verdict | Interpretation |
|------|---------|----------------|
| earlystop/math | **tie** (−0.0003) | Frozen basis is essentially indistinguishable from retrained; within-distribution, the shared representation is all you need |
| earlystop/science | **tie** (−0.0020) | Science is in-distribution for the source bundle (math+science training). Frozen basis retains 98.9% of task_specific performance |
| earlystop/coding | **win** (+0.0067) | Cross-domain: the math-derived basis generalises better than a fresh per-fold refit, likely because coding data is too sparse per fold for SVD to converge well |
| bestofn/math | **tie** (−0.0083) | Near-tie; frozen basis is only 0.83 pp below the task-specific refit on hit@1 |
| rl_ranking/math | **win** (+0.0273) | The frozen basis outperforms a fresh SVD refit on Spearman ρ (0.582 vs 0.555); the LOO training set is small (10 checkpoints × 6 400 samples = 64 000 samples) — frozen pre-compression helps regularise |

### 5.2 Headline Claim Assessment

更稳妥的结论是：**shared-basis transfer 在 math / science EarlyStop 上基本成立，在 RL ranking 上给出最干净的支持性证据。**

1. **Within-distribution transfer** (math → math, math+science → science):
   Frozen basis 与 task-specific 几乎重合，说明在这些设置里“固定 basis + 新线性头”是可信的压缩口径。

2. **Cross-domain transfer** (math → coding):
   frozen basis 数值上略优于 task-specific，但两者都接近 chance，因此不适合被当成强 claim。

3. **Task transfer** (classification → ordinal ranking):
   RL checkpoint ranking 上，frozen basis 优于 task_specific 和 no_svd；这一项更适合作为共享 latent object 的支持性证据。

### 5.3 Paper Recommendation

推荐口径不是“强 transfer 统一成立”，而是：

- EarlyStop / math 与 science：**near-lossless reuse**
- BestOfN / math：**small gap, still competitive**
- RL ranking：**supporting win**
- coding：**do not headline**

### 5.4 Caveats

- **RL LOO with 11 points**: Spearman on 11 data points has large sampling
  variance (SE ≈ 0.3 / √11 ≈ 0.09). The 2.7 pp advantage of frozen over
  task_specific is directionally consistent but not statistically decisive.
  The large gap over no_svd (+31.8 pp) is more robust.

- **Coding near chance (AUROC ≈ 0.50)**: The coding EarlyStop signal from
  math-derived features is weak in absolute terms. The "win" is meaningful
  only in the context of frozen_basis slightly beating task_specific (both
  near random). Future work should use coding-trained features.

- **Single anchor (100%)**: Results are for slot-9 (100% of generation
  complete). The frozen basis may transfer differently at earlier anchors
  (10%, 40%, 70%) where less trajectory information is available.
  Re-run with `--anchor-pct 40` to check mid-trajectory transfer.

- **Science in-distribution**: `es_svd_ms_rr_r1` was trained on math+science
  combined. The science result is thus within-distribution and the "tie" is
  expected. Coding is the true cross-domain test.

---

## 6. Reproduction boundary

完整复现实验仍依赖外部 `NAD_Next` 代码栈与内部 bundle / cache。

因此在这个 compact repo 里，这一节更适合被理解为：

- 结果物已经保留；
- 方法假设已经保留；
- 但训练与导出环境没有被完整 vendored 进来。
