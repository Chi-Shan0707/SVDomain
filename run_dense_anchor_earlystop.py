#!/usr/bin/env python3
"""Standalone wrapper for the paper-facing dense-anchor EarlyStop suite.

The underlying evaluation logic still depends on the shared training stack, but
this wrapper keeps the public artifact entrypoint local to `SVDomain`. It:

- resolves the repository root used for outputs
- bootstraps `NAD_NEXT_ROOT`
- imports the canonical dense-anchor implementation
- ensures generated tables and notes are written back into this repo

Use it as the clean public runner for the dense-anchor timing analysis shipped
with the paper repository.
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

from SVDomain import run_dense_anchor_earlystop as _impl

_impl.REPO_ROOT = LOCAL_REPO_ROOT


def main() -> None:
    _impl.main()


if __name__ == "__main__":
    main()
