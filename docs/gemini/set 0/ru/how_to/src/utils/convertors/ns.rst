Как использовать модуль ns для преобразования SimpleNamespace в различные форматы
==================================================================================

Описание
-------------------------
Этот модуль `hypotez/src/utils/convertors/ns.py` предоставляет функции для преобразования объектов `SimpleNamespace` в различные форматы, включая `dict`, `JSON`, `CSV`, `XML` и `XLS`.  Он обрабатывает вложенные структуры данных и обеспечивает удобный способ сохранения данных в разных форматах.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Модуль импортирует необходимые библиотеки, такие как `json`, `csv`, `pathlib`, `SimpleNamespace`, функции из модулей `src.utils.convertors`, `src.utils.csv`, `src.utils.xls` и `src.logger`, а также тип `SimpleNamespace` и типы данных `Any`, `Dict`.
2. **Определение функций преобразования:** Функции `ns2dict`, `ns2csv`, `ns2xml`, `ns2xls` определяют алгоритмы преобразования.
3. **Функция `ns2dict`:**  Рекурсивно преобразует объект `SimpleNamespace` в словарь (`dict`). Обрабатывает вложенные `SimpleNamespace`, `dict` и `list`.
4. **Функция `ns2csv`:** Преобразует объект `SimpleNamespace` в формат CSV. Принимает объект `SimpleNamespace` и путь к файлу CSV в качестве аргументов. Использует функцию `ns2dict` для преобразования объекта в словарь и функцию `save_csv_file` для сохранения данных в файл CSV. Логирует ошибки при возникновении проблем.
5. **Функция `ns2xml`:** Преобразует объект `SimpleNamespace` в XML-строку. Принимает объект `SimpleNamespace` и необязательный тег корня для XML. Использует функцию `ns2dict` для преобразования объекта в словарь и функцию `xml2dict` для генерации XML-строки. Логирует ошибки при возникновении проблем.
6. **Функция `ns2xls`:** Преобразует объект `SimpleNamespace` в формат XLS. Принимает объект `SimpleNamespace` и путь к файлу XLS в качестве аргументов. Использует функцию `save_xls_file` для сохранения данных в файл XLS. Возвращает `True` в случае успеха и `False` при ошибке.

Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from pathlib import Path
    import hypotez.src.utils.convertors.ns as ns

    # Создание объекта SimpleNamespace
    ns_object = SimpleNamespace(name="John Doe", age=30, city="New York")

    # Преобразование в словарь
    dict_representation = ns.ns2dict(ns_object)
    print(dict_representation)

    # Преобразование в CSV
    csv_file_path = Path("output.csv")
    ns.ns2csv(ns_object, csv_file_path)  # Сохранит данные в output.csv

    # Преобразование в XML
    xml_representation = ns.ns2xml(ns_object)
    print(xml_representation)  # Выведет XML-представление

    # Преобразование в XLS
    xls_file_path = Path("output.xls")
    success = ns.ns2xls(ns_object, xls_file_path)  # Сохранит данные в output.xls
    if success:
        print("Файл XLS успешно сохранен.")
    else:
        print("Ошибка при сохранении файла XLS.")