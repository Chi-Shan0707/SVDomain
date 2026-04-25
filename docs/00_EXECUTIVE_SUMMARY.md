[English](00_EXECUTIVE_SUMMARY.md) | [中文](00_EXECUTIVE_SUMMARY.zh-CN.md)

# Executive Summary

`SVD_Domain` is a cleaned subset of the original `SVDomain` repository. The goal is not to preserve every branch of the old workspace. The goal is to keep the parts that still support a clear, defensible story.

## Core reading

The current subset supports five claims:

1. **Moderate low rank is already sufficient**
   - `math`: smallest sufficient rank `16`
   - `science`: smallest sufficient rank `24`
   - `ms`: smallest sufficient rank `24`

2. **Frozen-basis transfer is real**
   - at slot `100`, frozen-basis EarlyStop is nearly tied with task-specific retraining on math and science
   - on RL ranking, the frozen basis is the cleanest supporting win

3. **Cross-anchor transfer is domain-dependent**
   - math bases stay reusable across the trajectory
   - science bases are more maturity-sensitive, especially for early-to-late reuse

4. **The most reusable basis is often not the final anchor**
   - best dense source anchor is `30%` for math
   - best dense source anchor is `50%` for science

5. **Dense-anchor timing explains the transfer pattern**
   - math saturates early
   - science becomes useful early but keeps improving later

## What this repo does not claim

- it does not claim that one basis solves every downstream task
- it does not claim that low-rank beats no-SVD everywhere
- it does not use coding as the headline success case

## What is retained

- concise docs
- summary tables and a few figures
- lightweight public entry scripts
- a smaller repo layout that is easier to browse and cite

