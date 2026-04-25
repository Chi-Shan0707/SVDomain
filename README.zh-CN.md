<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a>
</p>

<h1 align="center">SVD_Domain</h1>

<p align="center">
  <em>一个以英文为主、中文可切换的精简研究仓库。</em>
</p>

<p align="center">
  <a href="docs/00_EXECUTIVE_SUMMARY.md">English Overview</a> ·
  <a href="docs/00_EXECUTIVE_SUMMARY.zh-CN.md">中文总览</a> ·
  <a href="results/comparison_tables.md">结果总表</a>
</p>

这个仓库现在的定位很明确：它不是原始大仓库的完整镜像，而是一个**保留关键证据、去掉杂乱枝叶**的公开版本。

## 现在保留的主线

- **Low-rank sufficiency**：中等 rank 已经足够，重点是紧凑性而不是“全面碾压”
- **Frozen-basis transfer**：固定 basis + 新线性头，在 math / science 上已经相当接近
- **Cross-anchor transfer**：`math` 更稳，`science` 更依赖 basis 成熟度
- **Dense-anchor timing**：`math` 很早饱和，`science` 早期可用但后期仍会 refinement
- **RL checkpoint ranking**：同一 latent object 对 checkpoint 顺序结构也有解释力

## 图

<p align="center">
  <img src="results/figures/frozen_basis_transfer.png" width="94%" alt="Frozen-basis transfer" />
</p>

<p align="center">
  <sub><strong>Frozen-basis transfer.</strong> 这是当前最适合拿来讲 shared-basis reuse 的图。</sub>
</p>

<p align="center">
  <img src="results/figures/dense_anchor_maturity.png" width="76%" alt="Dense-anchor maturity" />
</p>

<p align="center">
  <sub><strong>Dense-anchor maturity.</strong> 这张图最适合解释为什么 math 和 science 的 transfer 口径不一样。</sub>
</p>

## 一句话总结

> 这个仓库最适合讲的，不是“一个 basis 解决一切”，而是“low-rank basis 的可复用性强烈依赖 domain 和 anchor maturity”。

## 建议怎么读

- 英文首页：`README.md`
- 中文总览：`docs/00_EXECUTIVE_SUMMARY.zh-CN.md`
- 文档索引：`docs/README.md`
- 结果索引：`results/README.md`
- 结果总表：`results/comparison_tables.md`

## 复现边界

- 根目录 `run_*.py` 是公开入口包装器；
- 一部分实验仍依赖外部 `NAD_Next` 与本地 cache / model artifacts；
- 当前版本更像一个干净的 artifact pack，而不是完整训练环境。

