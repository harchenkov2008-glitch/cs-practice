from pathlib import Path

from logstats import count_levels, top_errors, format_report


def main():
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    report_path = Path(__file__).with_name("report.txt")
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()