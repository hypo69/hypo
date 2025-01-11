# Анализ кода модуля `md2dict`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
  - Код выполняет поставленную задачу по преобразованию Markdown в HTML и структурированный словарь.
  - Используется библиотека `markdown2` для преобразования Markdown.
  - Присутствует обработка ошибок с логированием через `logger.error`.
- **Минусы**:
  - Не используются одинарные кавычки в Python коде.
  - Отсутствует RST-документация для модуля и функций.
  - Исключения обрабатываются слишком общим образом.
  - Не все импорты выровнены.

**Рекомендации по улучшению**:
-   Используйте одинарные кавычки для строковых литералов в Python, кроме случаев, когда это вывод в консоль или лог.
-   Добавьте RST-документацию для модуля и функций, чтобы улучшить читаемость и поддержку кода.
-   Используйте более специфические блоки `try-except` для обработки конкретных исключений, если это возможно.
-   Выровняйте импорты, переменные и названия функций.
-   Измените обработку ошибок, чтобы логировать через `logger.error`.
-   Улучшите регулярные выражения для парсинга HTML-тегов.

**Оптимизированный код**:
```python
"""
Модуль для конвертации Markdown в структурированный словарь
===========================================================

Этот модуль предоставляет функции для преобразования строк Markdown в HTML
и структурированные словари, включая извлечение заголовков и текста.

Пример использования
----------------------
.. code-block:: python

    from src.utils.convertors.md import md2dict

    md_string = '''# Заголовок 1
    ## Заголовок 2
    Текст 1
    ## Заголовок 3
    Текст 2'''
    result = md2dict(md_string)
    print(result)
    # {'Заголовок 1': ['Заголовок 2', 'Текст 1', 'Заголовок 3', 'Текст 2']}
"""
import re
from typing import Dict, List
from markdown2 import markdown  # type: ignore
from src.logger.logger import logger # Изменен импорт

def md2html(md_string: str, extras: List[str] = None) -> str:
    """
    Конвертирует строку Markdown в HTML.

    :param md_string: Строка Markdown для конвертации.
    :type md_string: str
    :param extras: Список расширений markdown2.
    :type extras: List[str], optional
    :return: HTML-представление Markdown.
    :rtype: str
    :raises Exception: В случае ошибки при преобразовании Markdown в HTML.

    Пример:
    >>> md2html('# Заголовок')
    '<h1>Заголовок</h1>\\n'
    """
    try:
        if extras is None:
            return markdown(md_string)
        return markdown(md_string, extras=extras)
    except Exception as ex:
        logger.error(f"Ошибка при преобразовании Markdown в HTML: {ex}", exc_info=True) #  Изменено логирование ошибки
        return ""


def md2dict(md_string: str, extras: List[str] = None) -> Dict[str, list[str]]:
    """
    Конвертирует строку Markdown в структурированный словарь.

    :param md_string: Строка Markdown для конвертации.
    :type md_string: str
    :param extras: Список расширений markdown2 для md2html.
    :type extras: List[str], optional
    :return: Структурированное представление Markdown содержимого.
    :rtype: Dict[str, list[str]]
    :raises Exception: В случае ошибки при парсинге Markdown в структурированный словарь.

    Пример:
        >>> md_string = '# Заголовок 1\\n## Заголовок 2\\nТекст 1\\n## Заголовок 3\\nТекст 2'
        >>> md2dict(md_string)
        {'Заголовок 1': ['Заголовок 2', 'Текст 1', 'Заголовок 3', 'Текст 2']}
    """
    try:
        html = md2html(md_string, extras)
        sections: Dict[str, list[str]] = {}
        current_section: str | None = None

        for line in html.splitlines():
            if line.startswith('<h'):
                heading_level_match = re.search(r'h(\d)', line) #  Улучшено регулярное выражение
                if heading_level_match:
                    heading_level = int(heading_level_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip() # Улучшено регулярное выражение
                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    elif current_section:
                        sections[current_section].append(section_title)

            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip() # Улучшено регулярное выражение
                sections[current_section].append(clean_text)

        return sections

    except Exception as ex:
        logger.error(f"Ошибка при парсинге Markdown в структурированный словарь: {ex}", exc_info=True)  # Изменено логирование ошибки
        return {}
```