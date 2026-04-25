<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a>
</p>

<h1 align="center">SVD_Domain</h1>

<p align="center">
  <em>Evidence-first notes and artifacts on low-rank basis reuse in reasoning traces.</em>
</p>

<p align="center">
  <img alt="Focus" src="https://img.shields.io/badge/focus-low--rank%20basis%20reuse-0F766E" />
  <img alt="Scope" src="https://img.shields.io/badge/scope-math%20%7C%20science%20%7C%20RL-1D4ED8" />
  <img alt="Style" src="https://img.shields.io/badge/repo-cleaned%20artifact%20pack-7C3AED" />
</p>

<p align="center">
  <a href="docs/00_EXECUTIVE_SUMMARY.md">Overview</a> ·
  <a href="docs/README.md">Docs</a> ·
  <a href="results/README.md">Results</a> ·
  <a href="results/comparison_tables.md">Comparison Tables</a>
</p>

`SVD_Domain` is a compact, cleaned subset of the original `SVDomain` workspace. It does not try to preserve every branch of the old repo. Instead, it keeps the notes, tables, figures, and lightweight entrypoints that still support a clear story:

- moderate low rank is already sufficient;
- basis reuse is real, but strongly domain-dependent;
- anchor maturity matters;
- the same latent object also carries checkpoint-order structure.

## Featured Results

<p align="center">
  <img src="results/figures/frozen_basis_transfer.png" width="94%" alt="Frozen-basis transfer" />
</p>

<p align="center">
  <sub><strong>Frozen-basis transfer at slot 100.</strong> The fixed basis stays near task-specific retraining on math and science, while RL ranking is the cleanest supporting win.</sub>
</p>

<p align="center">
  <img src="results/figures/dense_anchor_maturity.png" width="76%" alt="Dense-anchor maturity" />
</p>

<p align="center">
  <sub><strong>Dense-anchor timing.</strong> Math saturates early; science becomes useful early but still improves later.</sub>
</p>

## Core Findings

<table>
  <tr>
    <td valign="top" width="33%">
      <strong>Low-rank sufficiency</strong><br />
      <br />
      <code>math</code>: best rank <code>24</code>, smallest sufficient rank <code>16</code><br />
      <code>science</code>: smallest sufficient rank <code>24</code><br />
      <code>ms</code>: smallest sufficient rank <code>24</code>
    </td>
    <td valign="top" width="33%">
      <strong>Basis transfer</strong><br />
      <br />
      Slot-<code>100</code> frozen-basis transfer is nearly tied with task-specific retraining on math and science.<br />
      The strongest reusable dense source anchor is <code>30%</code> for math and <code>50%</code> for science.
    </td>
    <td valign="top" width="33%">
      <strong>Anchor maturity</strong><br />
      <br />
      <code>math 10→100</code>: gap <code>-0.19</code> pts<br />
      <code>science 10→100</code>: gap <code>-5.60</code> pts<br />
      The most reusable basis is often a mid-trajectory basis, not the final anchor.
    </td>
  </tr>
</table>

## What Is in This Repo

- `docs/`
  - compact research notes for low-rank necessity, basis transfer, anchor transfer, dense timing, and RL ranking
- `results/`
  - summary tables, a few stable figures, and small machine-readable summaries
- `run_*.py`
  - public entry wrappers for the retained experiment families
- `scripts/`
  - a small number of supporting scripts that still help explain the exported artifacts

## Scope

This is not a fully vendored training environment.

- Some experiment families still depend on the sibling `NAD_Next` workspace and local cache/model artifacts.
- The repo is intentionally selective: no workshop notes, no full cache dumps, no submission bundles, and no oversized exploratory branches.
- The public value here is the artifact contract: a clean path from claim → note → table → figure.

## Start Here

- `docs/00_EXECUTIVE_SUMMARY.md`
- `docs/07_LOWRANK_NECESSITY.md`
- `docs/11_CROSS_ANCHOR_TRANSFER.md`
- `results/comparison_tables.md`

