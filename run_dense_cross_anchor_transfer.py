#!/usr/bin/env python3
"""Standalone wrapper for the paper-facing dense cross-anchor transfer suite.

This public entrypoint keeps the standalone `SVDomain` repository tidy while
delegating the full dense all-to-all transfer logic to the canonical
implementation in the sibling `NAD_Next` checkout. It:

- resolves the local repository root for outputs
- bootstraps `NAD_NEXT_ROOT`
- imports the canonical dense cross-anchor implementation
- rewrites default outputs so artifacts land in this repo

Use it as the standalone runner for the `10 / 20 / ... / 100` dense
cross-anchor transfer analysis.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

LOCAL_REPO_ROOT = Path(__file__).resolve().parent
LOCAL_REPO_ROOT_STR = str(LOCAL_REPO_ROOT)
if LOCAL_REPO_ROOT_STR not in sys.path:
    sys.path.insert(0, LOCAL_REPO_ROOT_STR)

if "NAD_NEXT_ROOT" not in os.environ:
    sibling_nad_next = LOCAL_REPO_ROOT.parent / "NAD_Next"
    if sibling_nad_next.is_dir():
        os.environ["NAD_NEXT_ROOT"] = str(sibling_nad_next)

from svdomain.bootstrap_nad_next import ensure_nad_next_on_path

ensure_nad_next_on_path()

if LOCAL_REPO_ROOT_STR in sys.path:
    sys.path.remove(LOCAL_REPO_ROOT_STR)

from SVDomain.experiments import run_dense_cross_anchor_transfer as _impl

_impl.REPO_ROOT = LOCAL_REPO_ROOT
_impl.DEFAULT_OUT_MATRIX = "results/tables/dense_cross_anchor_transfer_matrix.csv"
_impl.DEFAULT_OUT_DELTAS = "results/tables/dense_cross_anchor_transfer_deltas.csv"
_impl.DEFAULT_OUT_SUMMARY = "results/tables/dense_cross_anchor_transfer_summary.csv"
_impl.DEFAULT_OUT_NOTE = "docs/17_DENSE_CROSS_ANCHOR_TRANSFER.md"
_impl.DEFAULT_PAPER_OUT_MATRIX = _impl.DEFAULT_OUT_MATRIX
_impl.DEFAULT_PAPER_OUT_DELTAS = _impl.DEFAULT_OUT_DELTAS
_impl.DEFAULT_PAPER_OUT_SUMMARY = _impl.DEFAULT_OUT_SUMMARY

for module_name in (
    "run_cross_anchor_transfer",
    "SVDomain.experiments.run_cross_anchor_transfer",
):
    module = sys.modules.get(module_name)
    if module is not None:
        module.REPO_ROOT = LOCAL_REPO_ROOT

_build_note_markdown = _impl.build_note_markdown


def _rewrite_note_paths(markdown: str) -> str:
    lines: list[str] = []
    replacements = {
        "**Experiment script**: `SVDomain/experiments/run_dense_cross_anchor_transfer.py`": (
            "**Experiment script**: `run_dense_cross_anchor_transfer.py`"
        ),
        "- Root matrix CSV:": "- Matrix CSV:",
        "- Root delta CSV:": "- Delta CSV:",
        "- Root summary CSV:": "- Summary CSV:",
    }
    for line in markdown.splitlines():
        if "Paper-package" in line:
            continue
        for old, new in replacements.items():
            line = line.replace(old, new)
        lines.append(line)
    return "\n".join(lines)


def _local_build_note_markdown(*args, **kwargs) -> str:
    return _rewrite_note_paths(_build_note_markdown(*args, **kwargs))


_impl.build_note_markdown = _local_build_note_markdown


def main() -> None:
    _impl.main()


if __name__ == "__main__":
    main()
