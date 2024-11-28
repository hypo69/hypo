Как использовать функцию get_relative_path
========================================================================================

Описание
-------------------------
Функция `get_relative_path` извлекает относительный путь к файлу или директории, начиная с указанного сегмента пути. Она принимает полный путь и сегмент пути в качестве входных данных и возвращает относительный путь, если указанный сегмент найден, иначе возвращает `None`.

Шаги выполнения
-------------------------
1. Принимает на вход полный путь (`full_path`) и сегмент пути (`relative_from`).
2. Преобразует входные строки в объекты `Path`.
3. Разбивает полный путь на составляющие (сегменты) с помощью метода `parts`.
4. Ищет указанный сегмент (`relative_from`) среди сегментов пути.
5. Если сегмент найден, определяет его индекс (`start_index`).
6. Формирует относительный путь, начиная с найденного сегмента, используя `parts[start_index:]` и объединяя сегменты в объект `Path`.
7. Преобразует объект `Path` в строку с помощью метода `as_posix()`.
8. Возвращает сформированный относительный путь.
9. Если сегмент не найден, возвращает `None`.


Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.utils.path import get_relative_path

    full_path = "/home/user/project/data/files/report.txt"
    relative_from = "data"
    relative_path = get_relative_path(full_path, relative_from)

    if relative_path:
        print(f"Относительный путь: {relative_path}")
    else:
        print("Сегмент пути не найден.")


    full_path2 = "/home/user/project/images/image.jpg"
    relative_from2 = "data"
    relative_path2 = get_relative_path(full_path2, relative_from2)

    if relative_path2:
        print(f"Относительный путь: {relative_path2}")
    else:
        print("Сегмент пути не найден.")