[English](README.md) | [中文](README.zh-CN.md)

# SVD_Domain

`SVD_Domain` is a cleaned, English-first subset of the original `SVDomain` repository.
It keeps a small set of docs, tables, figures, and entry scripts that support the main empirical story, and drops the workshop notes, caches, submissions, and other clutter that made the original tree hard to browse.

## What this repo is for

This repo is meant to answer a narrow question:

> When does a low-rank basis become useful, and when does that basis transfer across anchors or tasks?

The current public subset is built around five evidence threads:

| Topic | Main point | Primary artifact |
| --- | --- | --- |
| Low-rank sufficiency | Moderate rank is enough; the story is compactness, not domination | `results/tables/lowrank_smallest_sufficient_rank.csv` |
| Frozen-basis transfer | A fixed basis plus a new linear head is often enough | `results/tables/frozen_basis_transfer_deltas.csv` |
| Sparse cross-anchor transfer | Math transfers broadly; science is more maturity-sensitive | `results/tables/cross_anchor_transfer_summary.csv` |
| Dense-anchor timing | Math saturates early; science is usable early but still improves later | `results/tables/dense_anchor_main_table.csv` |
| RL checkpoint ranking | The same latent object also carries checkpoint-order signal | `results/tables/checkpoint_correlation_summary.csv` |

## At a glance

### Low-rank sufficiency

- `math`: best rank `24`, smallest sufficient rank `16`
- `science`: smallest sufficient rank `24`
- `ms`: smallest sufficient rank `24`

The practical reading is simple: rank `16–24` already captures most of the useful signal.

### Frozen-basis transfer at slot 100

- `earlystop / math`: `0.9655` vs `0.9658` task-specific
- `earlystop / science`: `0.7711` vs `0.7731` task-specific
- `rl_ranking / math`: `ρ = 0.5818` vs `0.5545` task-specific

This is the cleanest support for the shared-basis story.

### Anchor-maturity story

- Sparse transfer:
  - `math 10→100`: gap `-0.19` pts
  - `science 10→100`: gap `-5.60` pts
- Dense transfer:
  - best reusable source anchor is `30%` for math
  - best reusable source anchor is `50%` for science

The main observation is that the most reusable basis is often a **mid-trajectory basis**, not the final anchor.

### Dense-anchor timing

- `math`: AUROC `0.9357` already at `10%`; plateau around `50%`
- `science`: AUROC `0.7673` at `10%`; reaches `95%` of final by `20%`

That is why the repo frames math as **early-saturating** and science as **early-usable but later-refined**.

## Figures

<table>
  <tr>
    <td width="50%">
      <img src="results/figures/frozen_basis_transfer.png" alt="Frozen-basis transfer" />
      <br />
      <sub>Frozen-basis transfer</sub>
    </td>
    <td width="50%">
      <img src="results/figures/dense_anchor_maturity.png" alt="Dense-anchor maturity" />
      <br />
      <sub>Dense-anchor maturity</sub>
    </td>
  </tr>
</table>

## Repository layout

```text
SVD_Domain/
├── README.md
├── README.zh-CN.md
├── docs/
├── results/
├── scripts/
├── svdomain/
└── run_*.py
```

## Reproduction boundary

This is not a fully vendored training environment.

- The retained `run_*.py` files are public entry wrappers.
- Some experiments still depend on the sibling `NAD_Next` workspace and local cache/model artifacts.
- The public value of this repo is the **artifact contract**: the docs, tables, figures, and lightweight entrypoints are all in one place.

## Where to start

- Overview: `docs/00_EXECUTIVE_SUMMARY.md`
- Doc index: `docs/README.md`
- Result index: `results/README.md`
- Cross-topic summary: `results/comparison_tables.md`
