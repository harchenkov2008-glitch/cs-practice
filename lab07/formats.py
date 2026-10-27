def csv_to_records(text: str) -> list[dict]:
    if not text:
        return []
    lines = [line.rstrip("\r") for line in text.split("\n") if line.strip()]
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        record = {}
        for i, header in enumerate(headers):
            record[header] = values[i] if i < len(values) else ""
        records.append(record)
    return records
def _convert(value: str):
    low = value.lower()
    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- "):
            if current_list_key is not None:
                item = line[2:].strip()
                result[current_list_key].append(_convert(item))
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "":
            result[key] = []
            current_list_key = key
        else:
            result[key] = _convert(value)
            current_list_key = None
    return result
def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        if key in row and str(row[key]) in extra:
            base = dict(extra[str(row[key])])
            base.update(row)
            merged.append(base)
        else:
            merged.append(row)
    return merged
import json


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
