#!/usr/bin/env python3
"""Resolve shared paths for the standalone SVDomain repository."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def local_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _looks_like_nad_next(path: Path) -> bool:
    return (path / "nad").is_dir() and (path / "scripts").is_dir()


def resolve_nad_next_root() -> Path:
    here = Path(__file__).resolve().parent
    repo_root = local_repo_root()
    candidates: list[Path] = []

    env_root = os.getenv("NAD_NEXT_ROOT")
    if env_root:
        candidates.append(Path(env_root).expanduser())

    candidates.extend(
        [
            here.parent,
            here.parent / "NAD_Next",
            repo_root.parent / "NAD_Next",
            Path.cwd(),
            Path.cwd() / "NAD_Next",
        ]
    )

    seen: set[str] = set()
    for candidate in candidates:
        candidate = candidate.resolve()
        key = str(candidate)
        if key in seen:
            continue
        seen.add(key)
        if _looks_like_nad_next(candidate):
            return candidate

    raise RuntimeError(
        "Could not locate the sibling NAD_Next repository. "
        "Set NAD_NEXT_ROOT=/path/to/NAD_Next before running this script."
    )


def ensure_nad_next_on_path() -> Path:
    repo_root = resolve_nad_next_root()
    repo_str = str(repo_root)
    if repo_str not in sys.path:
        sys.path.insert(0, repo_str)
    return repo_root


def prefer_local_artifact(relative_path: str | Path) -> Path:
    rel = Path(relative_path)
    local_path = local_repo_root() / rel
    if local_path.exists():
        return local_path
    return resolve_nad_next_root() / rel
