# Анализ кода модуля `path`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код относительно прост и понятен.
    - Использует `pathlib` для работы с путями.
    - Есть документация к функции.
- **Минусы**:
    - Отсутствует  RST  документация.
    - Не хватает обработки ошибок.
    - Нет импорта `logger`.
    - Используются двойные кавычки в строке документации.
    - Комментарии `Args:` и `Returns:` не соответствуют RST.
    - Есть лишние комментарии и символы вначале кода

## Рекомендации по улучшению:

1.  **Документация**:
    - Необходимо добавить  RST  документацию для модуля.
    - Переделать  документацию функции в формате  RST.
2.  **Импорты**:
    - Добавить импорт `logger` из `src.logger`.
3.  **Обработка ошибок**:
    - Добавить обработку ошибок с помощью `logger.error`.
4.  **Комментарии**:
    - Привести комментарии в соответствие  RST  и убрать лишние.
5.  **Форматирование**:
    - Использовать одинарные кавычки в коде, двойные только для вывода.
    - Убрать лишние символы в начале файла
    - Добавить docstring модуля.
6.  **Улучшение кода**:
    - Добавить проверку на пустые пути.

## Оптимизированный код:

```python
"""
Модуль для работы с путями в проекте
=====================================

Этот модуль содержит функции для обработки путей, в частности,
для получения относительных путей от заданного сегмента.

Пример использования
--------------------
.. code-block:: python

    from pathlib import Path
    from src.utils.path import get_relative_path

    full_path = "/home/user/project/src/module/file.py"
    relative_from = "src"
    relative_path = get_relative_path(full_path, relative_from)
    print(relative_path)  # Вывод: src/module/file.py
"""
from pathlib import Path
from typing import Optional
from src.logger import logger  # импорт logger


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    :param full_path: Полный путь.
    :type full_path: str
    :param relative_from: Сегмент пути, с которого нужно начать извлечение.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    :rtype: Optional[str]

    :raises ValueError: Если `full_path` или `relative_from` пустые.

    Пример:
        >>> get_relative_path('/home/user/project/src/utils/file.py', 'src')
        'src/utils/file.py'
        >>> get_relative_path('/home/user/project/src/utils/file.py', 'project')
        'project/src/utils/file.py'
        >>> get_relative_path('/home/user/project/src/utils/file.py', 'test')
        None
    """
    if not full_path or not relative_from:  # проверка на пустой путь
        logger.error('Путь или сегмент не могут быть пустыми.')  # логируем ошибку
        raise ValueError('Путь или сегмент не могут быть пустыми.')

    try:  # обрабатываем ошибку преобразования строки в Path
        path = Path(full_path)  # Преобразуем строки в объекты Path
        parts = path.parts
    except Exception as e:
        logger.error(f'Ошибка при обработке пути: {e}') # логируем ошибку
        return None

    if relative_from in parts: # Находим индекс сегмента relative_from
        start_index = parts.index(relative_from)
        relative_path = Path(*parts[start_index:]) # Формируем путь начиная с указанного сегмента
        return relative_path.as_posix() # Возвращаем путь
    else:
        return None # возвращаем None, если сегмент не найден