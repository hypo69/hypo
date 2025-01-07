# Анализ кода модуля `html.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код содержит docstring для всех функций, что облегчает понимание их назначения и использования.
    *   Используются `HTMLParser` для парсинга HTML и `SimpleNamespace` для создания объектов с атрибутами, что соответствует задаче.
    *   Присутствуют примеры использования в docstring.
    *   Код разбит на функции, каждая из которых выполняет определенную задачу.

*   **Минусы:**
    *   Импорт `logger` из `venv` является некорректным и должен быть исправлен на `src.logger.logger`.
    *   Отсутствует обработка ошибок в функциях `html2dict` и `html2ns`.
    *   Функция `html2pdf` использует `print` для логирования ошибок, что не соответствует стандартам логирования.
    *   Использование `try-except` без конкретной обработки ошибок.
    *   В функции `html2pdf` используется `print` вместо `logger.error`.
    *   В коде присутствуют закомментированные блоки.

**Рекомендации по улучшению:**

1.  **Исправить импорты**: Заменить некорректный импорт `logger` из `venv` на `from src.logger.logger import logger`.
2.  **Добавить обработку ошибок**: В функциях `html2dict` и `html2ns` добавить `try-except` блоки для обработки возможных ошибок и логирования с помощью `logger.error`.
3.  **Улучшить логирование**: Заменить `print` на `logger.error` в функции `html2pdf`.
4.  **Убрать лишний try-except**: Убрать неинформативный try-except при импорте weasyprint и использовать logger.error.
5.  **Удалить закомментированный код**: Удалить закомментированный код, который не используется.
6.  **Унифицировать ковычки**: Использовать одинарные ковычки.
7.  **Добавить rst документацию**: Переписать комментарии в формате reStructuredText (RST).

**Оптимизированный код:**

```python
"""
Модуль для работы с HTML.
=========================================================================================

Этот модуль содержит функции для конвертации HTML в различные форматы,
а также для преобразования HTML в escape-последовательности и обратно.

Функции:
    - `html2escape`: Преобразует HTML в escape-последовательности.
    - `escape2html`: Преобразует escape-последовательности в HTML.
    - `html2dict`: Преобразует HTML в словарь.
    - `html2ns`: Преобразует HTML в объект SimpleNamespace.
    - `html2pdf`: Преобразует HTML в PDF файл.

Примеры использования
--------------------

Пример использования функций:

.. code-block:: python

    html = "<p>Hello</p><a href='link'>World</a>"
    escaped_html = html2escape(html)
    print(f"Escaped HTML: {escaped_html}")

    unescaped_html = escape2html(escaped_html)
    print(f"Unescaped HTML: {unescaped_html}")

    html_dict = html2dict(html)
    print(f"HTML as dictionary: {html_dict}")

    html_ns = html2ns(html)
    print(f"HTML as SimpleNamespace: {html_ns.p}, {html_ns.a}")

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import re
from typing import Dict
from pathlib import Path
# from venv import logger # некорректный импорт
from src.logger.logger import logger # исправленный импорт
from types import SimpleNamespace
from html.parser import HTMLParser
from xhtml2pdf import pisa

try:
    from weasyprint import HTML
except Exception as ex:
    #  Код логирует ошибку импорта weasyprint
    logger.error(f'Ошибка импорта weasyprint: {ex}')
    ...





class StringFormatter:
    """
    Утилитарный класс для форматирования строк.
    """
    @staticmethod
    def escape_html_tags(input_str: str) -> str:
        """
        Преобразует HTML в escape-последовательности.

        :param input_str: HTML код.
        :return: HTML, преобразованный в escape-последовательности.

        Пример:
            >>> html = "<p>Hello, world!</p>"
            >>> result = StringFormatter.escape_html_tags(html)
            >>> print(result)
            &lt;p&gt;Hello, world!&lt;/p&gt;
        """
        return (
            input_str.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;')
        )

    @staticmethod
    def unescape_html_tags(input_str: str) -> str:
        """
        Преобразует escape-последовательности в HTML.

        :param input_str: Строка с escape-последовательностями.
        :return: Escape-последовательности, преобразованные обратно в HTML.

         Пример:
            >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
            >>> result = StringFormatter.unescape_html_tags(escaped)
            >>> print(result)
            <p>Hello, world!</p>
        """
        return (
            input_str.replace('&amp;', '&')
            .replace('&lt;', '<')
            .replace('&gt;', '>')
            .replace('&quot;', '"')
            .replace('&#39;', "'")
        )


def html2escape(input_str: str) -> str:
    """
    Преобразует HTML в escape-последовательности.

    :param input_str: HTML код.
    :return: HTML, преобразованный в escape-последовательности.

    Пример:
        >>> html = "<p>Hello, world!</p>"
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    return StringFormatter.escape_html_tags(input_str)


def escape2html(input_str: str) -> str:
    """
    Преобразует escape-последовательности в HTML.

    :param input_str: Строка с escape-последовательностями.
    :return: Escape-последовательности, преобразованные обратно в HTML.

    Пример:
        >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    return StringFormatter.unescape_html_tags(input_str)


def html2dict(html_str: str) -> Dict[str, str]:
    """
    Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

    :param html_str: HTML строка для преобразования.
    :return: Словарь с HTML тегами в качестве ключей и их содержимым в качестве значений.

    Пример:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        """
        Класс для парсинга HTML в словарь.
        """
        def __init__(self):
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            """
            Код исполняет обработку начала тега.
            """
            self.current_tag = tag

        def handle_endtag(self, tag):
            """
            Код исполняет обработку закрытия тега.
            """
            self.current_tag = None

        def handle_data(self, data):
            """
            Код исполняет обработку данных внутри тега.
            """
            if self.current_tag:
                self.result[self.current_tag] = data.strip()
    try:
        parser = HTMLToDictParser()
        parser.feed(html_str)
        return parser.result
    except Exception as ex:
        #  Код логирует ошибку парсинга html
        logger.error(f'Ошибка парсинга html в словарь: {ex}')
        return {}

def html2ns(html_str: str) -> SimpleNamespace:
    """
    Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

    :param html_str: HTML строка для преобразования.
    :return: Объект SimpleNamespace с HTML тегами в качестве атрибутов и их содержимым в качестве значений.

    Пример:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    try:
        html_dict = html2dict(html_str)
        return SimpleNamespace(**html_dict)
    except Exception as ex:
        #  Код логирует ошибку преобразования в SimpleNamespace
        logger.error(f'Ошибка преобразования html в SimpleNamespace: {ex}')
        return SimpleNamespace()



def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """
    Преобразует HTML контент в PDF файл, используя WeasyPrint.

    :param html_str: HTML контент в виде строки.
    :param pdf_file: Путь к выходному PDF файлу.
    :return: `True`, если генерация PDF прошла успешно, `None` в противном случае.
    """
    try:
        #  Код исполняет запись pdf файла
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        #  Код логирует ошибку генерации pdf файла
        logger.error(f"Ошибка во время генерации PDF: {e}")
        return None
```