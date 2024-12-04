Как использовать функцию get_relative_path
========================================================================================

Описание
-------------------------
Функция `get_relative_path` из модуля `src.utils.path` возвращает часть пути, начиная с указанного сегмента.  Она принимает полный путь и сегмент, с которого нужно начать извлечение, и возвращает относительный путь, или None, если сегмент не найден. Функция преобразует входные строки в объекты `Path` для работы с путями.

Шаги выполнения
-------------------------
1. Функция принимает полный путь (`full_path`) и сегмент пути (`relative_from`) как аргументы.
2. Преобразует `full_path` в объект `Path`.
3. Разбивает путь `full_path` на части (`parts`).
4. Ищет индекс сегмента `relative_from` в списка `parts`.
5. Если сегмент найден:
    - Находит индекс (`start_index`) сегмента.
    - Создает новый объект `Path`, используя части пути начиная с `start_index` (`parts[start_index:]`).
    - Возвращает строковое представление относительного пути, используя метод `as_posix()`.
6. Если сегмент не найден:
    - Возвращает `None`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.path import get_relative_path
    
    full_path = "/home/user/project/data/file.txt"
    relative_from = "project"
    
    relative_path = get_relative_path(full_path, relative_from)
    
    if relative_path:
        print(f"Относительный путь: {relative_path}")  # Вывод: Относительный путь: data/file.txt
    else:
        print("Сегмент не найден")
        
    full_path = "/home/user/other_project/data/file.txt"
    relative_from = "project"
    
    relative_path = get_relative_path(full_path, relative_from)
    
    if relative_path:
        print(f"Относительный путь: {relative_path}")
    else:
        print("Сегмент не найден") # Вывод: Сегмент не найден