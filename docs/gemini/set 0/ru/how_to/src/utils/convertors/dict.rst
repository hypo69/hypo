Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот модуль (`hypotez/src/utils/convertors/dict.py`) предоставляет функции для преобразования между словарями (dict) и объектами `SimpleNamespace`, а также для экспорта данных в различные форматы (XML, CSV, JSON, XLS, HTML, PDF).  В нём определены функции для преобразования, обработки и сохранения данных.  Одной из ключевых функций является `replace_key_in_dict`, которая рекурсивно заменяет ключи в словарях и списках. Модуль также содержит функции для генерации XML, HTML, сохранения данных в CSV, XLS, PDF и JSON форматы.

Шаги выполнения
-------------------------
1. **Импортируйте необходимые модули:**
   Модуль импортирует необходимые библиотеки, включая `json`, `SimpleNamespace`, `pathlib`, `xml.dom.minidom`, `reportlab`, `src.utils.xls` и т.д. для работы с различными форматами.

2. **Определите функции преобразования:**
   Функции `dict2ns`, `dict2xml`, `dict2csv`, `dict2json`, `dict2xls`, `dict2html`, `dict2pdf` предназначены для преобразования и сохранения данных.

3. **Используйте функции для преобразования данных:**
   Например, для преобразования словаря в `SimpleNamespace` используйте `dict2ns(data)`. Для сохранения данных в CSV-файл используйте `dict2csv(data, file_path)`.
   Другие функции работают аналогично.

4. **Обработайте возвращаемые значения:**
   Функции могут возвращать различные типы данных (строки, файлы, булевы значения). Обработайте возвращаемые значения в соответствии с требуемым результатом.


Пример использования
-------------------------
.. code-block:: python

    import json
    from hypotez.src.utils.convertors.dict import dict2ns, dict2pdf

    # Пример словаря
    data = {"name": "John Doe", "age": 30, "city": "New York"}

    # Преобразуем словарь в SimpleNamespace
    ns_data = dict2ns(data)
    print(ns_data.name)  # Выведет "John Doe"

    # Сохраняем данные в PDF
    dict2pdf(data, "output.pdf")

    # Пример использования replace_key_in_dict
    data_with_replaced_key = replace_key_in_dict(data, 'name', 'full_name')
    print(data_with_replaced_key)
    # Ожидаемый результат: {'full_name': 'John Doe', 'age': 30, 'city': 'New York'}

    #Пример преобразования в XML:
    xml_data = dict2xml({"name": "User1", "address": {"street": "Main St", "city": "Anytown"}})