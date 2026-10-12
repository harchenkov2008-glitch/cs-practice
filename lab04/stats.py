def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {"city": city, "temp": float(temp), "date": date}

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temp"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    result = {}

    for city in total:
        result[city] = round(total[city] / count[city], 1)

    return result


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    best = ""

    for city in averages:
        if best == "":
            best = city
        elif averages[city] > averages[best]:
            best = city
        elif averages[city] == averages[best] and city < best:
            best = city

    return best