LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    text = line.rstrip("\r\n")
    parts = text.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError(f"bad line: {line!r}")

    time, level, message = parts

    if level not in LEVELS or not time or not message:
        raise ValueError(f"bad line: {line!r}")

    return {
        "time": time,
        "level": level,
        "message": message,
    }


def count_levels(lines) -> dict:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            key = "BROKEN"
        else:
            key = event["level"]

        counts[key] = counts.get(key, 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    if n <= 0:
        return []

    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            counts[message] = counts.get(message, 0) + 1

    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in result[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    parts = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        parts.append(f"{level}: {counts[level]}")

    parts.append("")
    parts.append("Частые ошибки:")

    for message, count in errors:
        parts.append(f"- {message} — {count}")

    return "\n".join(parts) + "\n"