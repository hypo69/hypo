# Анализ кода модуля `html.py`

**Качество кода**
9
- Плюсы
    - Код содержит docstring для каждой функции, что облегчает понимание его назначения и использования.
    - Используются typing для обозначения типов переменных, что повышает читаемость и облегчает отладку.
    - Код разбит на функции, что улучшает его структуру и повторное использование.
    - Присутствует обработка ошибок с помощью `try-except`.

- Минусы
    -   Импорт `logger` из `venv` выглядит некорректно.
    -   Некоторые комментарии `#` не соответствуют стандарту reStructuredText (RST).
    -   Обработка ошибок не использует `logger.error` для логирования.
    -   Импорт `SimpleNamespace` дублируется.
    -   Не все импорты используются, например, `Path` и `Dict`.
    -   Используется `print` для вывода ошибок, что не подходит для продакшн-кода, где обычно используется логирование.
    -   В коде присутствуют закомментированные участки кода, что может затруднять его понимание.
    -   Отсутствует обработка ошибок при импорте `weasyprint`.

**Рекомендации по улучшению**

1.  Заменить импорт `logger` из `venv` на `from src.logger.logger import logger`.
2.  Удалить дублирующийся импорт `SimpleNamespace`.
3.  Использовать `logger.error` для логирования ошибок вместо `print`.
4.  Удалить неиспользуемые импорты `Path` и `Dict`.
5.  Преобразовать все комментарии и docstring в формат RST.
6.  Удалить или раскомментировать неиспользуемый код, например, `html2pdf` с использованием `pisa`.
7.  Улучшить обработку ошибок в `html2pdf`, используя `logger.error` для логирования.
8.  Использовать одинарные кавычки в коде.

**Оптимизированный код**

```python
"""
Модуль для работы с HTML
=========================================================================================

Этот модуль содержит утилиты для преобразования HTML в различные форматы,
такие как escape-последовательности, словари и объекты SimpleNamespace,
а также для конвертации HTML в PDF.

Функции:
    - :func:`html2escape`: Преобразует HTML в escape-последовательности.
    - :func:`escape2html`: Преобразует escape-последовательности обратно в HTML.
    - :func:`html2dict`: Преобразует HTML в словарь.
    - :func:`html2ns`: Преобразует HTML в объект SimpleNamespace.
    - :func:`html2pdf`: Преобразует HTML в PDF-файл.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    html = '<p>Hello, world!</p>'
    escaped_html = html2escape(html)
    print(escaped_html)

    unescaped_html = escape2html(escaped_html)
    print(unescaped_html)

    html_dict = html2dict('<p>Hello</p><a>World</a>')
    print(html_dict)

    html_ns = html2ns('<p>Hello</p><a>World</a>')
    print(html_ns.p)
    print(html_ns.a)
"""
# -*- coding: utf-8 -*-
import re
from types import SimpleNamespace
from html.parser import HTMLParser
from xhtml2pdf import pisa
#from pathlib import Path # Удален неиспользуемый импорт
#from typing import Dict # Удален неиспользуемый импорт
from src.utils.string_format import StringFormatter # Добавлен импорт StringFormatter
from src.logger.logger import logger # Исправлен импорт логгера

try:
    from weasyprint import HTML
except Exception as ex:
    logger.error(f'Ошибка импорта weasyprint: {ex}') # Логируем ошибку импорта
    ...


def html2escape(input_str: str) -> str:
    """
    Преобразует HTML в escape-последовательности.

    :param input_str: HTML код для преобразования.
    :type input_str: str
    :return: HTML, преобразованный в escape-последовательности.
    :rtype: str

    :Example:
        >>> html = '<p>Hello, world!</p>'
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    # Код вызывает метод для преобразования html тегов в escape последовательности
    return StringFormatter.escape_html_tags(input_str)


def escape2html(input_str: str) -> str:
    """
    Преобразует escape-последовательности обратно в HTML.

    :param input_str: Строка с escape-последовательностями.
    :type input_str: str
    :return: Строка с преобразованными escape-последовательностями в HTML.
    :rtype: str

    :Example:
        >>> escaped = '&lt;p&gt;Hello, world!&lt;/p&gt;'
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    # Код вызывает метод для преобразования escape последовательностей обратно в html теги
    return StringFormatter.unescape_html_tags(input_str)


def html2dict(html_str: str) -> dict[str, str]:
    """
    Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

    :param html_str: HTML строка для преобразования.
    :type html_str: str
    :return: Словарь с HTML тегами в качестве ключей и их содержимым в качестве значений.
    :rtype: dict

    :Example:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        """
        Вспомогательный класс для парсинга HTML и преобразования его в словарь.
        """
        def __init__(self):
            """
            Инициализирует парсер.
            """
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            """
            Обрабатывает открытие тега.
            """
            # Код сохраняет текущий открытый тег
            self.current_tag = tag

        def handle_endtag(self, tag):
            """
            Обрабатывает закрытие тега.
            """
            # Код сбрасывает текущий открытый тег
            self.current_tag = None

        def handle_data(self, data):
            """
            Обрабатывает текстовые данные.
            """
            # Код добавляет данные в словарь, если есть текущий открытый тег
            if self.current_tag:
                self.result[self.current_tag] = data.strip()

    # Код создает экземпляр парсера и передает ему html строку
    parser = HTMLToDictParser()
    parser.feed(html_str)
    # Код возвращает словарь с результатами
    return parser.result


def html2ns(html_str: str) -> SimpleNamespace:
    """
    Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

    :param html_str: HTML строка для преобразования.
    :type html_str: str
    :return: Объект SimpleNamespace с HTML тегами в качестве атрибутов и их содержимым в качестве значений.
    :rtype: SimpleNamespace

    :Example:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    # Код преобразует html строку в словарь
    html_dict = html2dict(html_str)
    # Код возвращает SimpleNamespace объект на основе словаря
    return SimpleNamespace(**html_dict)


def html2pdf(html_str: str, pdf_file: str) -> bool | None:
    """
    Преобразует HTML контент в PDF-файл с использованием WeasyPrint.

    :param html_str: HTML контент в виде строки.
    :type html_str: str
    :param pdf_file: Путь к выходному PDF-файлу.
    :type pdf_file: str
    :return: Возвращает `True`, если генерация PDF прошла успешно, иначе `None`.
    :rtype: bool | None
    """
    try:
        # Код пытается сгенерировать pdf файл из html строки
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        # Код логгирует ошибку при генерации pdf файла
        logger.error(f'Ошибка во время генерации PDF: {e}')
        return None
```