Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит функции для преобразования объекта `SimpleNamespace` в различные форматы: словарь (dict), JSON, CSV, XML и XLS.  Функции позволяют работать с вложенными структурами данных.  В частности, `ns2dict` рекурсивно преобразует `SimpleNamespace` в словарь, обрабатывая вложенные объекты `SimpleNamespace`, словари и списки.  Функции `ns2csv`, `ns2xml`, `ns2xls`  соответственно сохраняют данные в CSV, XML и XLS файлы.  Используется логирование для обработки ошибок.


Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**: Модули `json`, `csv`, `pathlib`, `typing`, `xml2dict` (из другого модуля), `save_csv_file`, `save_xls_file`, `logger` (из других модулей) импортируются для работы с различными форматами и логированием.

2. **Определение функции `ns2dict`**: Функция `ns2dict` преобразует объект `SimpleNamespace` в словарь. Внутри функции `convert` реализована рекурсия для обработки вложенных структур.

3. **Определение функции `ns2csv`**: Функция `ns2csv` принимает объект `SimpleNamespace` и путь к CSV файлу. Она преобразует объект в словарь с помощью `ns2dict`, затем сохраняет его в CSV файл с помощью `save_csv_file`. Обрабатывает возможные ошибки.

4. **Определение функции `ns2xml`**: Функция `ns2xml` принимает объект `SimpleNamespace` и имя тега корневого элемента (по умолчанию "root"). Она преобразует объект в словарь с помощью `ns2dict`, затем генерирует XML-представление данных с помощью `xml2dict` и возвращает его в виде строки.  Обрабатывает возможные ошибки.

5. **Определение функции `ns2xls`**: Функция `ns2xls` принимает объект `SimpleNamespace` и путь к XLS файлу. Она сохраняет данные в XLS файл с помощью функции `save_xls_file`. Возвращает True при успехе, False при ошибке. Обрабатывает возможные ошибки.


Пример использования
-------------------------
.. code-block:: python

    import os
    from types import SimpleNamespace
    from pathlib import Path
    from hypotez.src.utils.convertors.ns import ns2dict, ns2csv, ns2xml, ns2xls


    # Пример создания объекта SimpleNamespace
    ns_obj = SimpleNamespace(name="John Doe", age=30, city="New York")

    # Пример сохранения в CSV
    csv_file_path = Path("output.csv")
    success = ns2csv(ns_obj, csv_file_path)
    if success:
        print(f"Файл {csv_file_path} успешно создан.")
    else:
        print("Ошибка при создании CSV файла.")
        
    # Пример сохранения в XML
    xml_output = ns2xml(ns_obj)
    print(xml_output)


    #Пример сохранения в XLS (предполагается, что save_xls_file корректно обрабатывает данные)
    xls_file_path = Path("output.xls")
    success = ns2xls(ns_obj, xls_file_path)
    if success:
        print(f"Файл {xls_file_path} успешно создан.")
    else:
        print("Ошибка при создании XLS файла.")

    # Пример преобразования в словарь
    dict_representation = ns2dict(ns_obj)
    print(dict_representation)