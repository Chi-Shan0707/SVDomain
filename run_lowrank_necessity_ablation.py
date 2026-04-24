#!/usr/bin/env python3
"""Standalone wrapper for the paper-facing low-rank necessity ablation.

This thin wrapper keeps the public entrypoint at the root of `SVDomain` while
reusing the canonical implementation logic from the shared training workspace.
Its responsibilities are:

- resolve the local repository root
- discover `NAD_NEXT_ROOT` automatically when a sibling checkout exists
- import the canonical implementation
- redirect output paths so generated artifacts land in this repository

The script is intentionally complete and auditable, but reproducing the
original numbers still requires the shared `NAD_Next` stack plus the expected
cache/model artifacts.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

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

from SVDomain import run_lowrank_necessity_ablation as _impl

_impl.REPO_ROOT = LOCAL_REPO_ROOT


def write_outputs_from_summary(*args: Any, **kwargs: Any):
    return _impl.write_outputs_from_summary(*args, **kwargs)


def main() -> None:
    _impl.main()


if __name__ == "__main__":
    main()
