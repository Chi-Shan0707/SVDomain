#!/usr/bin/env python3
"""Standalone wrapper for the paper-facing cross-anchor transfer suite.

This public entrypoint preserves a clean root-level script for the repository
while delegating the core transfer logic to the canonical implementation. It:

- resolves the local repo root
- bootstraps `NAD_NEXT_ROOT` from the environment or a sibling checkout
- imports the canonical cross-anchor transfer code
- rewrites output resolution so artifacts are written under `SVDomain`

Use this script when generating or auditing the paper-facing cross-anchor
transfer artifacts bundled with this repository.
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

from SVDomain import run_cross_anchor_transfer as _impl

_impl.REPO_ROOT = LOCAL_REPO_ROOT


def main() -> None:
    _impl.main()


if __name__ == "__main__":
    main()
