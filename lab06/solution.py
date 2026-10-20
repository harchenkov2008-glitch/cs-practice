def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    i = 0

    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1

    if i == 0:
        return f"{n_bytes} Б"

    return f"{size:.1f} {units[i]}"
