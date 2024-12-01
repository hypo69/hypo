Как использовать функции конвертирования JSON в другие форматы
============================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для конвертирования данных в формате JSON в различные форматы: CSV, SimpleNamespace, XML и XLS.  Модуль содержит функции `json2csv`, `json2ns`, `json2xml` и `json2xls` для выполнения этих преобразований.  Каждая функция обрабатывает различные типы входных данных (строка JSON, словарь, список словарей, путь к файлу JSON) и возвращает соответствующий результат (CSV-строка, объект SimpleNamespace, XML-строка, успех/неудача преобразования в XLS).

Шаги выполнения
-------------------------
1. **Импортирование модуля:**  Импортируйте необходимый модуль.  При использовании функций из этого модуля, нужно импортировать `hypotez.src.utils.convertors.json`.

2. **Подготовка входных данных:** Подготовьте данные в формате JSON.  Это может быть строка, список словарей, словарь или путь к файлу JSON.

3. **Вызов соответствующей функции:** Вызовите функцию, соответствующую желаемому формату вывода:
    - `json2csv`: для преобразования в CSV. Не забудьте указать путь к файлу CSV.
    - `json2ns`: для преобразования в объект SimpleNamespace.
    - `json2xml`: для преобразования в XML. Укажите опциональный тег корня.
    - `json2xls`: для преобразования в XLS. Не забудьте указать путь к файлу XLS.

4. **Обработка результатов:**
    - `json2csv` и `json2xls`: функция возвращает `True` при успешном преобразовании и сохранении файла, `False` в случае ошибок. Обратите внимание на потенциальные исключения, указанные в документации к функции, особенно ValueError для неправильного типа данных входных данных.
    - `json2ns`: функция возвращает объект `SimpleNamespace` при успешном преобразовании.
    - `json2xml`: функция возвращает строку XML.

Пример использования
-------------------------
.. code-block:: python

    import json
    from pathlib import Path

    from hypotez.src.utils.convertors.json import json2csv, json2ns, json2xml, json2xls

    # Пример данных JSON
    json_data = '{"name": "John Doe", "age": 30}'

    # Преобразование в CSV
    csv_file_path = "output.csv"
    success = json2csv(json_data, csv_file_path)
    if success:
        print(f"CSV файл '{csv_file_path}' успешно создан.")
    else:
        print("Ошибка при создании CSV файла.")

    # Преобразование в SimpleNamespace
    ns_data = json2ns(json_data)
    if ns_data:
        print(f"Данные в SimpleNamespace: {ns_data.name}, {ns_data.age}")


    # Преобразование в XML
    xml_data = json2xml(json_data)
    print(f"Данные в XML:\n{xml_data}")

    # Преобразование в XLS (пример с файлом)
    json_file_path = Path("data.json")
    xls_file_path = "output.xls"

    with open(json_file_path, 'w') as f:
        json.dump({"name": "Jane Doe", "age": 25}, f)

    success = json2xls(json_file_path, xls_file_path)
    if success:
        print(f"XLSX файл '{xls_file_path}' успешно создан.")
    else:
        print("Ошибка при создании XLSX файла.")