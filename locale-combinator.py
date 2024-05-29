import json, argparse
from dataclasses import dataclass

@dataclass
class op_counter:
    changes: int = 0

arg_parser = argparse.ArgumentParser(
    prog = "Locale Combinator", 
    description = "Программа для обновления существующих JSON-файлов локализации модов Minecraft",
)
arg_parser.add_argument("eng_source", type = str, help = "Оригинальный файл (английский язык)")
arg_parser.add_argument("locale_source", type = str, help = "Устаревший файл локализации")
arg_parser.add_argument("destination", type = str, help = "Объединенный файл (вывод)")
arg_parser.add_argument("--case", help = "Включить исправление регистра строк", action = "store_true")
args = arg_parser.parse_args()

with open(args.eng_source, encoding = "utf-8") as f:
    english_json = json.load(f)

with open(args.locale_source, encoding = "utf-8") as f:
    old_language_json = json.load(f)

for key, value in english_json.items():
    if(key in old_language_json):
        english_json[key] = old_language_json.get(key)
        op_counter.changes += 1
    
    if(args.case):
        english_json[key] = english_json[key].capitalize()

with open(args.destination, "w", encoding = "utf-8") as f:
    json.dump(english_json, f, ensure_ascii = False, indent = 2, sort_keys = True)

print(f"Всего строк: {len(english_json)}")
print(f"Существует перевод: {op_counter.changes}")
if(args.case):
    print("Выполнено исправление регистра.")