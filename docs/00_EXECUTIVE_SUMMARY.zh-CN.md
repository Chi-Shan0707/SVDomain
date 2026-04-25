[English](00_EXECUTIVE_SUMMARY.md) | [中文](00_EXECUTIVE_SUMMARY.zh-CN.md)

# 执行摘要

`SVD_Domain` 是从原始 `SVDomain` 中整理出来的一个精简版本。它不再试图保留所有旧分支，而是只保留还能支撑清晰结论的那部分材料。

## 当前主线

现在这个仓库主要支持五个判断：

1. **中等 rank 已经足够**
   - `math`：smallest sufficient rank 是 `16`
   - `science`：是 `24`
   - `ms`：也是 `24`

2. **Frozen-basis transfer 是成立的**
   - slot `100` 上，math / science 的 EarlyStop 基本接近 task-specific 重训
   - RL ranking 是更干净的一条 supporting win

3. **Cross-anchor transfer 有明显 domain 差异**
   - `math` 的 basis 更容易贯穿整条 trajectory
   - `science` 更依赖 basis 成熟度，尤其 early-to-late 更容易掉

4. **最可迁移的 basis 往往不是最后一个 anchor**
   - dense transfer 里，`math` 最优 source anchor 是 `30%`
   - `science` 最优 source anchor 是 `50%`

5. **Dense-anchor timing 可以解释这种差异**
   - `math` 很早就趋于饱和
   - `science` 早期就有信号，但后面仍会继续 refinement

## 这个仓库不主张什么

- 不主张一个 basis 解决所有问题
- 不主张 low-rank 在所有设置上都严格优于 no-SVD
- 不把 coding 当作主成功案例

## 当前保留的东西

- 简洁文档
- 核心 summary tables 和少量图
- 公开入口脚本
- 一个更容易浏览和引用的目录结构

