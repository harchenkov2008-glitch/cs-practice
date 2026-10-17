def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("В строке должно быть ровно три поля")

    city, temperature, date = parts

    if city == "" or date == "":
        raise ValueError("Город и дата не должны быть пустыми")

    try:
        temperature_value = float(temperature)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {"city": city, "temperature": temperature_value, "date": date}
def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        total[city] = total.get(city, 0) + temperature
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

def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if line == "":
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records