import sys

from stats import average_by_city, read_valid, warmest_city


lines = sys.stdin.read().splitlines()
records = read_valid(lines)

empty_count = 0
for line in lines:
    if line == "":
        empty_count += 1

errors_count = len(lines) - len(records) - empty_count

print(len(records))
print(errors_count)

if records:
    best = warmest_city(records)
    averages = average_by_city(records)
    print(f"{averages[best]:.1f}")
else:
    print("0.0")