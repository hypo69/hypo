## Анализ кода модуля `html`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код содержит docstring для каждой функции, что облегчает понимание назначения каждой функции.
    - Присутствуют примеры использования функций.
    - Используются аннотации типов.
- **Минусы**:
    - Не все функции содержат подробное описание обработки ошибок и граничных случаев.
    - В коде используется `print` для логирования ошибок, рекомендуется использовать `logger.error`.
    - Используются смешанные стили кавычек (как двойные, так и одинарные).

**Рекомендации по улучшению:**

1.  **Импорты**:
    *   Убедитесь, что все необходимые импорты присутствуют и не содержат лишних.

2.  **Обработка ошибок**:
    *   Добавьте обработку исключений в функции `html2pdf` и используйте `logger.error` для логирования ошибок.

3.  **Использование кавычек**:
    *   Приведите все строки к использованию одинарных кавычек для соответствия стандартам кодирования.

4.  **Документация**:
    *   Улучшите документацию, добавив информацию о возможных исключениях и граничных случаях.

5.  **Логирование**:
    *   Замените `print` на `logger.error` для логирования ошибок, чтобы соответствовать стандартам проекта.

**Оптимизированный код:**

```python
## \file /src/utils/convertors/html.py
# -*- coding: utf-8 -*-

"""
Модуль для работы с HTML.
=================================================

Модуль содержит функции для преобразования HTML в различные форматы, такие как escape-последовательности, словари и объекты SimpleNamespace.

Функции:
    - `html2escape`: Преобразует HTML в escape-последовательности.
    - `escape2html`: Преобразует escape-последовательности обратно в HTML.
    - `html2dict`: Преобразует HTML в словарь.
    - `html2ns`: Преобразует HTML в объекты SimpleNamespace.

Пример использования:
----------------------

>>> from src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns
>>> html = '<p>Hello, world!</p>'
>>> escaped_html = html2escape(html)
>>> print(escaped_html)
&lt;p&gt;Hello, world!&lt;/p&gt;
>>> original_html = escape2html(escaped_html)
>>> print(original_html)
<p>Hello, world!</p>
>>> html_dict = html2dict(html)
>>> print(html_dict)
{'p': 'Hello, world!'}
>>> html_ns = html2ns(html)
>>> print(html_ns.p)
Hello, world!

Источники:
    - https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
    - https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""

import re
from typing import Dict
from pathlib import Path
from types import SimpleNamespace
from html.parser import HTMLParser

from src.logger.logger import logger

try:
    from weasyprint import HTML
except Exception as ex:
    logger.error('Ошибка при импорте weasyprint', ex, exc_info=True)
    ...


def html2escape(input_str: str) -> str:
    """
    Преобразует HTML в escape-последовательности.

    Args:
        input_str (str): HTML-код для преобразования.

    Returns:
        str: HTML, преобразованный в escape-последовательности.

    Example:
        >>> html = '<p>Hello, world!</p>'
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    return StringFormatter.escape_html_tags(input_str)


def escape2html(input_str: str) -> str:
    """
    Преобразует escape-последовательности обратно в HTML.

    Args:
        input_str (str): Строка с escape-последовательностями.

    Returns:
        str: HTML, полученный из escape-последовательностей.

    Example:
        >>> escaped = '&lt;p&gt;Hello, world!&lt;/p&gt;'
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    return StringFormatter.unescape_html_tags(input_str)


def html2dict(html_str: str) -> Dict[str, str]:
    """
    Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

    Args:
        html_str (str): HTML-строка для преобразования.

    Returns:
        dict: Словарь, где ключи - HTML-теги, а значения - их содержимое.

    Example:
        >>> html = '<p>Hello</p><a href='link'>World</a>'
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """

    class HTMLToDictParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            self.current_tag = tag

        def handle_endtag(self, tag):
            self.current_tag = None

        def handle_data(self, data):
            if self.current_tag:
                self.result[self.current_tag] = data.strip()

    parser = HTMLToDictParser()
    parser.feed(html_str)
    return parser.result


def html2ns(html_str: str) -> SimpleNamespace:
    """
    Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

    Args:
        html_str (str): HTML-строка для преобразования.

    Returns:
        SimpleNamespace: Объект SimpleNamespace с атрибутами, соответствующими HTML-тегам, и их содержимым в качестве значений.

    Example:
        >>> html = '<p>Hello</p><a href='link'>World</a>'
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)


def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """
    Преобразует HTML-контент в PDF-файл, используя WeasyPrint.

    Args:
        html_str (str): HTML-контент в виде строки.
        pdf_file (str | Path): Путь к выходному PDF-файлу.

    Returns:
        bool | None: Возвращает `True`, если генерация PDF прошла успешно, `None` в случае ошибки.
    """
    try:
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        logger.error(f'Ошибка при генерации PDF: {e}', exc_info=True)
        return None