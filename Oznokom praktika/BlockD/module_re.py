import json
import re

def csv_to_json(json_data):
# загрузка данных из JSON
    data = json.loads(json_data)

    # регулярное выражение для поиска ключей и значений
    pattern = re.compile(r'"(.+?)":\s*"(.+?)"')

    # преобразование данных в формат CSV
    for item in data:
        # поиск ключей и значений
        matches = pattern.findall(json.dumps(item))
        # объединение ключей и значений в строку
        csv_string = ';'.join(['"{}"'.format(match[1]) for match in matches])
        print(csv_string)

json_data = '''[
    {"en": "Male", "es": "Macho"},
    {"en": "Female", "es": "Hembra"},
    {"en":"Population","es":"Poblacion"}
]'''

csv_to_json(json_data)