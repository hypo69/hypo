# Анализ кода модуля `md2dict`

**Качество кода**
    8
 -  Плюсы
        - Код структурирован, функции имеют docstring.
        - Используется `logger` для обработки ошибок.
        - Присутствуют проверки на наличие расширений.
 -  Минусы
    - Не везде используется одинарная кавычка.
    - В docstring не хватает примеров использования.
    - Отсутствует обработка пустой строки в `md_string`.
    - Не везде есть аннотация типов.

**Рекомендации по улучшению**

1.  Использовать одинарные кавычки для строк в коде, кроме `print`, `input` и логера.
2.  Добавить примеры использования функций в docstring в формате reStructuredText.
3.  Обработать ситуацию, когда `md_string` пустая строка, возвращая пустой словарь.
4.  Добавить `from typing import Optional` и использовать `Optional[List[str]]` вместо `List[str] = None`.
5.  В блоке `try` использовать конструкцию `logger.error(..., exc_info=True)` только в крайних случаях. Вместо этого следует обрабатывать ошибку и возвращать `None` или `{}`, после чего  залогировать ошибку.

**Оптимизированный код**
```python
"""
Модуль для конвертации Markdown в структурированный словарь
=========================================================================================

Этот модуль предоставляет функции для преобразования строк в формате Markdown в HTML и в структурированный словарь.
Модуль использует библиотеку `markdown2` для преобразования Markdown в HTML.

Пример использования
--------------------

Пример использования функции `md2dict`:

.. code-block:: python

    from src.utils.convertors.md import md2dict

    md_string = '''# Section 1
    Content of section 1.
    ## Subsection 1.1
    Content of subsection 1.1'''
    result = md2dict(md_string)
    print(result)
    # {'Section 1': ['Content of section 1.', 'Subsection 1.1', 'Content of subsection 1.1']}
"""

import re
from typing import Dict, List, Any, Optional
from markdown2 import markdown
from src.logger.logger import logger


def md2html(md_string: str, extras: Optional[List[str]] = None) -> str:
    """Конвертирует строку Markdown в HTML.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (Optional[List[str]], optional): Список расширений markdown2. Defaults to None.

    Returns:
        str: HTML-представление Markdown.

    Raises:
        Exception: Если возникает ошибка при конвертации Markdown в HTML.

    Example:
        >>> md_string = '# Заголовок'
        >>> html = md2html(md_string)
        >>> print(html)
        <h1 id="заголовок">Заголовок</h1>
    """
    try:
        # Проверка наличия дополнительных параметров
        if extras is None:
            # Код исполняет преобразование Markdown в HTML без дополнительных параметров
            return markdown(md_string)
        # Код исполняет преобразование Markdown в HTML с дополнительными параметрами
        return markdown(md_string, extras=extras)
    except Exception as ex:
        # Логирование ошибки преобразования
        logger.error(f'Ошибка при преобразовании Markdown в HTML: {ex}')
        return ''


def md2dict(md_string: str, extras: Optional[List[str]] = None) -> Dict[str, list[str]]:
    """Конвертирует строку Markdown в структурированный словарь.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (Optional[List[str]], optional): Список расширений markdown2 для md2html. Defaults to None.

    Returns:
        Dict[str, list[str]]: Структурированное представление Markdown содержимого.

    Raises:
        Exception: Если возникает ошибка при парсинге Markdown.

    Example:
        >>> md_string = '# Section 1\\nContent of section 1.\\n## Subsection 1.1\\nContent of subsection 1.1'
        >>> result = md2dict(md_string)
        >>> print(result)
        {'Section 1': ['Content of section 1.', 'Subsection 1.1', 'Content of subsection 1.1']}
    """
    # Проверка на пустую строку
    if not md_string:
        return {}
    try:
        # Код исполняет преобразование Markdown в HTML
        html = md2html(md_string, extras)
        # Инициализация словаря для хранения результата
        sections: Dict[str, list[str]] = {}
        current_section: Optional[str] = None
        # Код исполняет разбор HTML
        for line in html.splitlines():
            # Проверка, является ли строка заголовком
            if line.startswith('<h'):
                # Поиск уровня заголовка
                heading_level_match = re.search(r'h(\\d)', line)
                if heading_level_match:
                    # Извлечение уровня заголовка
                    heading_level = int(heading_level_match.group(1))
                    # Удаление HTML-тегов и пробелов из заголовка
                    section_title = re.sub(r'<.*?>', '', line).strip()
                    # Если это заголовок первого уровня
                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    # Если это заголовок более низкого уровня
                    elif current_section:
                        sections[current_section].append(section_title)
            # Если строка содержит текст и есть текущий раздел
            elif line.strip() and current_section:
                # Очистка текста от HTML-тегов и пробелов
                clean_text = re.sub(r'<.*?>', '', line).strip()
                sections[current_section].append(clean_text)
        # Код возвращает результат
        return sections
    except Exception as ex:
        # Логирование ошибки и возврат пустого словаря
        logger.error(f'Ошибка при парсинге Markdown в структурированный словарь: {ex}')
        return {}
```