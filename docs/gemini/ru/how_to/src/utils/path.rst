Как использовать функцию get_relative_path
========================================================================================

Описание
-------------------------
Функция `get_relative_path` извлекает относительный путь к файлу или каталогу, начиная с указанного сегмента пути. Она принимает полный путь и сегмент пути, с которого нужно начать извлечение, и возвращает относительный путь или None, если указанный сегмент не найден.

Шаги выполнения
-------------------------
1. Функция принимает на вход два аргумента: `full_path` (полный путь) и `relative_from` (сегмент пути, с которого нужно начать извлечение).
2. Преобразует входные строки `full_path` и `relative_from` в объекты `Path` для работы с путями.
3. Разбивает полный путь на составляющие (parts).
4. Определяет индекс сегмента `relative_from` в списке `parts`.
5. Если сегмент `relative_from` найден:
    - Создаёт новый объект `Path`, содержащий все части пути начиная с найденного сегмента.
    - Преобразует полученный объект `Path` в строку в формате POSIX.
    - Возвращает полученный относительный путь.
6. Если сегмент `relative_from` не найден:
    - Возвращает `None`.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.utils.path import get_relative_path

    full_path = "/home/user/project/data/file.txt"
    relative_from = "project"

    relative_path = get_relative_path(full_path, relative_from)

    if relative_path:
        print(f"Относительный путь: {relative_path}")  # Выведет: Относительный путь: data/file.txt
    else:
        print("Сегмент не найден.")


    full_path2 = "/home/user/project/other_folder/file.txt"
    relative_from2 = "data"

    relative_path2 = get_relative_path(full_path2, relative_from2)

    if relative_path2:
        print(f"Относительный путь: {relative_path2}")
    else:
        print("Сегмент не найден.") # Выведет: Сегмент не найден.