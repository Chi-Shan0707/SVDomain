[English](08_FROZEN_BASIS_TRANSFER.md) | [中文](08_FROZEN_BASIS_TRANSFER.zh-CN.md)

# Frozen-Basis Transfer

This note summarizes the slot-`100` experiment where the basis is frozen and only the linear head is retrained.

## Core comparison

| Task | Domain | Frozen basis | Task-specific | No-SVD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| EarlyStop | `math` | `0.9655` | `0.9658` | `0.9668` | near-tie |
| EarlyStop | `science` | `0.7711` | `0.7731` | `0.7798` | still competitive |
| BestOfN | `math` | `0.7917` | `0.8000` | `0.8000` | small gap |
| RL ranking | `math` | `0.5818` | `0.5545` | `0.2636` | cleanest win |

## Recommended interpretation

- For math and science EarlyStop, the fixed basis is close enough to task-specific retraining to support the shared-basis claim.
- RL checkpoint ranking is the strongest transfer result in this table.
- Coding should not be the headline here: the numbers are too close to chance to carry a broad claim.

## Artifacts

- `results/tables/frozen_basis_transfer_matrix.csv`
- `results/tables/frozen_basis_transfer_deltas.csv`
- `results/figures/frozen_basis_transfer.png`

## Reproduction boundary

The cleaned repo keeps the note and the exported artifacts. Full reruns still depend on the sibling `NAD_Next` workspace and local internal caches.

