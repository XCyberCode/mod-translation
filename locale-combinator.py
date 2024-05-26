import json, argparse

changes_amount = 0

arg_parser = argparse.ArgumentParser(
    prog = "Locale Combinator", 
    description = "Программа для обновления существующих JSON-файлов локализации модов Minecraft",
)
arg_parser.add_argument("eng_source", type = str, help = "Оригинальный файл (английский язык)")
arg_parser.add_argument("locale_source", type = str, help = "Устаревший файл локализации")
arg_parser.add_argument("destination", type = str, help = "Объединенный файл (вывод)")
args = arg_parser.parse_args()

with open(args.eng_source, encoding = "utf-8") as f:
    english_json = json.load(f)

with open(args.locale_source, encoding = "utf-8") as f:
    old_language_json = json.load(f)

for key, value in english_json.items():
    if(key in old_language_json):
        english_json[key] = old_language_json.get(key)
        changes_amount += 1

with open(args.destination, "w", encoding = "utf-8") as f:
    json.dump(english_json, f, ensure_ascii = False, indent = 2, sort_keys = True)

print(f"Всего: {len(english_json)}")
print(f"Изменено: {changes_amount}")