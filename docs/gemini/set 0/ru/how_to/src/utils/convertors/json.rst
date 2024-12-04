Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит функции для преобразования данных в формате JSON в различные форматы: CSV, SimpleNamespace, XML и XLS. Функции позволяют загружать данные из JSON-строки, JSON-файла или словаря Python и сохранять результаты в CSV, XML или XLS файл.  Также, одна функция преобразует JSON в объект SimpleNamespace.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:**  Код импортирует необходимые модули, такие как `json`, `csv`, `SimpleNamespace`, `Path` и другие, для работы с JSON, CSV, XML и XLS данными. Также импортируются вспомогательные функции для работы с файлами.

2. **Определение функций преобразования:**  Код определяет четыре функции: `json2csv`, `json2ns`, `json2xml`, и `json2xls`, каждая из которых предназначена для преобразования JSON в соответствующий формат.

3. **Функция `json2csv`:**
    - Принимает на вход JSON данные (`json_data`) и путь к CSV файлу (`csv_file_path`).
    - Проверяет тип входных данных и загружает JSON данные из строки, списка словарей, файла или словаря.
    - Сохраняет загруженные данные в указанный CSV файл с разделителем ",".
    - Возвращает `True`, если преобразование успешно, иначе `False`.
    - Обрабатывает исключения при работе с JSON и файлами.

4. **Функция `json2ns`:**
    - Принимает на вход JSON данные (`json_data`).
    - Проверяет тип входных данных и загружает JSON данные из строки, файла или словаря.
    - Преобразует загруженные данные в объект `SimpleNamespace`.
    - Возвращает объект `SimpleNamespace`.
    - Обрабатывает исключения при работе с JSON.

5. **Функция `json2xml`:**
    - Принимает на вход JSON данные (`json_data`) и необязательный параметр `root_tag`.
    - Использует функцию `dict2xml` для преобразования JSON в XML.
    - Возвращает строку XML.
    - Обрабатывает исключения при работе с JSON и преобразованием в XML.


6. **Функция `json2xls`:**
    - Принимает на вход JSON данные (`json_data`) и путь к XLS файлу (`xls_file_path`).
    - Использует функцию `save_xls_file` для сохранения данных в XLS файл.
    - Возвращает `True`, если преобразование успешно, иначе `False`.
    - Обрабатывает исключения при работе с JSON и записью в XLS.


Пример использования
-------------------------
.. code-block:: python

    import json
    from pathlib import Path
    from hypotez.src.utils.convertors.json import json2csv, json2ns, json2xml

    # Пример данных JSON
    json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

    # Путь к файлу CSV
    csv_file_path = 'output.csv'

    # Преобразование в CSV
    json2csv(json_data, csv_file_path)

    # Преобразование в SimpleNamespace
    ns_data = json2ns(json_data)
    print(ns_data.name)  # Вывод: John Doe

    # Преобразование в XML
    xml_data = json2xml(json_data)
    print(xml_data)

    # Пример с файлом JSON
    json_file_path = Path('data.json')
    with open(json_file_path, 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    csv_file_path = 'output2.csv'
    json2csv(json_file_path, csv_file_path)