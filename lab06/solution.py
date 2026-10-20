from pathlib import Path


def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        ext = Path(path).suffix.lower()
        if ext.startswith('.'):
            ext = ext[1:]
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    sorted_paths = sorted(paths, key=lambda p: (-p.count('/'), p))
    return sorted_paths[0]


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    
    for unit in units:
        size /= 1024.0
        if size < 1024 or unit == "ТБ":
            return f"{size:.1f} {unit}"