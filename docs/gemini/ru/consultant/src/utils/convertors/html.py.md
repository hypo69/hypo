### Анализ кода модуля `html`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код разбит на функции, что улучшает читаемость и поддержку.
    - Присутствует базовая документация для каждой функции.
    - Используются `HTMLParser` для разбора HTML, что является стандартным подходом.
- **Минусы**:
    - Не везде используется одинарный кавычки (`'`) в коде.
    - Стандартный `print` используется для ошибок, что не соответствует требованиям.
    - Отсутствует использование `j_loads` или `j_loads_ns`.
    - Не везде используется `from src.logger.logger import logger`.
    - Есть блоки `try-except` без обработки ошибок через `logger.error`.
    - Закомментированный код `html2pdf` с использованием `xhtml2pdf` необходимо удалить или доработать.

**Рекомендации по улучшению**:

- Использовать одинарные кавычки (`'`) в коде и двойные кавычки (`"`) только для вывода в консоль и логгирования.
- Заменить `print` на `logger.error` для вывода ошибок.
- Применять `from src.logger.logger import logger` для логирования.
- Избегать стандартных блоков `try-except` и использовать `logger.error` для обработки ошибок.
- Доработать или удалить закомментированный код с `xhtml2pdf`.
- Добавить RST-комментарии для модуля и всех функций.
- Использовать `j_loads` или `j_loads_ns`, если это необходимо (в данном коде не используется).
- Выравнивание импортов и названий в соответствии с PEP8.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с HTML
========================

Этот модуль содержит функции для преобразования HTML:
- в escape-последовательности,
- из escape-последовательностей в HTML,
- в словари,
- в объекты SimpleNamespace.
- конвертация в PDF

Пример использования
----------------------
.. code-block:: python

    from src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf

    html = '<p>Hello, world!</p>'
    escaped_html = html2escape(html)
    print(f"Escape HTML: {escaped_html}")

    unescaped_html = escape2html(escaped_html)
    print(f"Unescape HTML: {unescaped_html}")

    html_dict = html2dict('<p>Hello</p><a href=\'link\'>World</a>')
    print(f"HTML to dict: {html_dict}")

    html_ns = html2ns('<p>Hello</p><a href=\'link\'>World</a>')
    print(f"HTML to SimpleNamespace: {html_ns.p}, {html_ns.a}")

    pdf_file = 'example.pdf'
    html2pdf(html, pdf_file)
    print(f"PDF created: {pdf_file}")
"""
import re
from typing import Dict
from pathlib import Path
from types import SimpleNamespace
from html.parser import HTMLParser

from src.logger.logger import logger #  Используем импорт из src.logger
try:
    from weasyprint import HTML
except Exception as ex: #  Используем logger.error для обработки ошибок
    logger.error(f'Error import WeasyPrint: {ex}')
    ...

class StringFormatter:
    """
    Класс для форматирования строк, включая экранирование HTML-тегов.
    """
    @staticmethod
    def escape_html_tags(input_str: str) -> str:
        """
        Экранирует HTML-теги в строке, заменяя <, >, & на соответствующие escape-последовательности.

        :param input_str: Строка, содержащая HTML-теги.
        :type input_str: str
        :return: Строка с экранированными HTML-тегами.
        :rtype: str
        """
        return (
            input_str.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
        )

    @staticmethod
    def unescape_html_tags(input_str: str) -> str:
        """
        Деэкранирует HTML-теги в строке, заменяя escape-последовательности на <, >, &.

        :param input_str: Строка с экранированными HTML-тегами.
        :type input_str: str
        :return: Строка с деэкранированными HTML-тегами.
        :rtype: str
        """
        return (
            input_str.replace('&lt;', '<')
            .replace('&gt;', '>')
            .replace('&amp;', '&')
        )

def html2escape(input_str: str) -> str:
    """
    Преобразует HTML в escape-последовательности.

    :param input_str: HTML-код.
    :type input_str: str
    :return: HTML, преобразованный в escape-последовательности.
    :rtype: str

    Пример:
        >>> html = '<p>Hello, world!</p>'
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    return StringFormatter.escape_html_tags(input_str) # Используем класс StringFormatter

def escape2html(input_str: str) -> str:
    """
    Преобразует escape-последовательности обратно в HTML.

    :param input_str: Строка с escape-последовательностями.
    :type input_str: str
    :return: Escape-последовательности, преобразованные обратно в HTML.
    :rtype: str

    Пример:
        >>> escaped = '&lt;p&gt;Hello, world!&lt;/p&gt;'
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    return StringFormatter.unescape_html_tags(input_str) # Используем класс StringFormatter

def html2dict(html_str: str) -> Dict[str, str]:
    """
    Преобразует HTML в словарь, где теги являются ключами, а содержимое — значениями.

    :param html_str: HTML-строка для преобразования.
    :type html_str: str
    :return: Словарь с HTML-тегами в качестве ключей и их содержимым в качестве значений.
    :rtype: dict

    Пример:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        """
        Внутренний класс для разбора HTML и преобразования в словарь.
        """
        def __init__(self):
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            """Обрабатывает начальный тег HTML."""
            self.current_tag = tag

        def handle_endtag(self, tag):
            """Обрабатывает конечный тег HTML."""
            self.current_tag = None

        def handle_data(self, data):
            """Обрабатывает данные между тегами."""
            if self.current_tag:
                self.result[self.current_tag] = data.strip()

    parser = HTMLToDictParser()
    parser.feed(html_str)
    return parser.result

def html2ns(html_str: str) -> SimpleNamespace:
    """
    Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое — значениями.

    :param html_str: HTML-строка для преобразования.
    :type html_str: str
    :return: Объект SimpleNamespace с HTML-тегами в качестве атрибутов и их содержимым в качестве значений.
    :rtype: SimpleNamespace

    Пример:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
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
    Конвертирует HTML-содержимое в PDF-файл с использованием WeasyPrint.

    :param html_str: HTML-содержимое в виде строки.
    :type html_str: str
    :param pdf_file: Путь к выходному PDF-файлу.
    :type pdf_file: str | Path
    :return: True, если создание PDF прошло успешно; None в противном случае.
    :rtype: bool | None

    Пример:
        >>> html = '<p>Hello</p>'
        >>> pdf_file = 'example.pdf'
        >>> result = html2pdf(html, pdf_file)
        >>> print(result)
        True
    """
    try:
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        logger.error(f'Error during PDF generation: {e}') #  Используем logger.error для обработки ошибок
        return