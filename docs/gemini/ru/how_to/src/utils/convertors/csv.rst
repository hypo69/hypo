Как использовать функции для преобразования CSV в другие форматы
================================================================================

Описание
-------------------------
Этот код содержит функции для преобразования данных из CSV-файлов в словари Python и объекты SimpleNamespace, а также для преобразования в JSON. Он использует библиотеки `csv`, `json`, `pathlib`, `typing` и `src.logger`.  Функции `csv2dict` и `csv2ns` выполняют преобразование из CSV в словарь и SimpleNamespace соответственно.  `csv_to_json` преобразует CSV в JSON и сохраняет его в файл.


Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует необходимые модули (`json`, `csv`, `pathlib`, `typing`, `SimpleNamespace`,  `logger`,  `read_csv_as_dict`, `read_csv_as_ns`, `save_csv_file`, `read_csv_file` ).

2. **Определение функции `csv2dict`:** Функция `csv2dict` принимает путь к CSV-файлу в качестве аргумента и использует функцию `read_csv_as_dict` для чтения данных из CSV и возвращает их в виде словаря. Возвращает `None` при ошибке.

3. **Определение функции `csv2ns`:** Функция `csv2ns` аналогична `csv2dict`, но возвращает данные в формате `SimpleNamespace`.

4. **Определение функции `csv_to_json`:** Функция `csv_to_json` принимает пути к CSV и JSON файлам. Она считывает данные из CSV с помощью `read_csv_file`. Если чтение прошло успешно, сохраняет данные в JSON-файл. В случае ошибки записывает сообщение об ошибке в лог с подробным отчетом.

5. **Обработка ошибок:** Все функции содержат обработку исключений (`try...except`), чтобы справиться с возможными ошибками при чтении или записи данных.


Пример использования
-------------------------
.. code-block:: python

    import os
    from pathlib import Path

    # Создаем временный CSV файл для примера
    csv_data = [['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]
    csv_file_path = 'temp_data.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

    # путь к выходному json файлу
    json_file_path = 'temp_data.json'


    # Преобразование CSV в JSON и сохранение в файл
    json_data = csv_to_json(csv_file_path, json_file_path)

    if json_data:
        print("Преобразованные данные в JSON формате:")
        print(json_data)


    # Удаление временного файла (важно!)
    os.remove(csv_file_path)