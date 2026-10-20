from __future__ import annotations
import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        ext = os.path.splitext(name)[1].lower().lstrip(".")
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count("/") for p in paths)
    candidates = [p for p in paths if p.count("/") == max_depth]
    return min(candidates)