from formats import csv_to_records, parse_settings, merge_by_key, records_to_json

print("--- csv_to_records ---")
print(csv_to_records("id,город\n1,Азов\n2,Шахты\n"))
print(csv_to_records("город, цена \n Азов , 100"))
print(csv_to_records(""))

print("--- parse_settings ---")
print(parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1",
                      "active: true", "columns:", "  - город", "  - цена"]))
print(parse_settings(["# только комментарий"]))
print(parse_settings(["rate: 3,5 # с запятой"]))
print(parse_settings([]))

print("--- merge_by_key ---")
print(merge_by_key([{"id": "1", "город": "Азов"}],
                   {"1": {"регион": "Ростовская"}}, "id"))
print(merge_by_key([{"id": "9", "город": "Азов"}],
                   {"1": {"регион": "Ростовская"}}, "id"))
print(merge_by_key([{"id": "1", "регион": "своё"}],
                   {"1": {"регион": "из справочника"}}, "id"))

print("--- records_to_json ---")
print(records_to_json([{"б": 2, "а": 1}]))
print(records_to_json([]))