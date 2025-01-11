# Анализ кода модуля `html.py`

**Качество кода**
7
-  Плюсы
    - Код содержит docstring для функций, что облегчает понимание их назначения и использования.
    - Присутствуют примеры использования функций в docstring.
    - Используется `HTMLParser` для разбора HTML, что является подходящим решением для поставленной задачи.
    - Есть обработка ошибок при импорте `weasyprint`.
    -  Функции разделены по логическому назначению: `html2escape`, `escape2html`, `html2dict`, `html2ns`, `html2pdf`
-  Минусы
    - Отсутствует описание модуля в начале файла.
    -  В коде используется импорт `from venv import logger`, который не является корректным. Нужно использовать `from src.logger.logger import logger`.
    -  Используется `print` для вывода ошибок, что не соответствует стандартам логирования, необходимо использовать `logger.error`.
    -  Не везде используется `logger.error` для обработки исключений.
    -  Не все комментарии достаточно подробные.
    - Использование `try-except` с `print` для `weasyprint` не соответствует стандартам логирования.
    -  В функции `html2pdf` необходимо использовать `logger.error` для логирования ошибок.
    - Не используется  `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, но в данном случае это не нужно.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате RST.
2.  Исправить импорт `logger` на `from src.logger.logger import logger`.
3.  Заменить `print` на `logger.error` при обработке ошибок.
4.  Добавить более подробные комментарии к блокам кода.
5.  В функции `html2pdf` использовать `logger.error` для логирования ошибок и заменить общий `try except` на более конкретный
6.  Соблюдать PEP8 в оформлении кода.
7.  Использовать одинарные кавычки в коде, двойные только в `print` и `logger`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с HTML
=========================================================================================

Этот модуль содержит функции для преобразования HTML в различные форматы, включая:
- преобразование HTML в escape-последовательности
- преобразование escape-последовательностей обратно в HTML
- преобразование HTML в словарь
- преобразование HTML в объект SimpleNamespace
- преобразование HTML в PDF

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf

    html_string = "<p>Hello, world!</p><a href='https://example.com'>Link</a>"
    escaped_html = html2escape(html_string)
    print(f"Escaped HTML: {escaped_html}")
    unescaped_html = escape2html(escaped_html)
    print(f"Unescaped HTML: {unescaped_html}")

    html_dict = html2dict(html_string)
    print(f"HTML to dict: {html_dict}")
    
    html_ns = html2ns(html_string)
    print(f"HTML to SimpleNamespace: {html_ns.p}, {html_ns.a}")
    
    pdf_file = Path("output.pdf")
    if html2pdf(html_string, pdf_file):
        print(f"PDF created successfully at {pdf_file}")
    else:
        print("PDF creation failed")
"""
import re
from typing import Dict
from pathlib import Path
from types import SimpleNamespace
from html.parser import HTMLParser

from src.logger.logger import logger
from xhtml2pdf import pisa
try:
    from weasyprint import HTML
except Exception as ex:
    logger.error(f'Ошибка при импорте weasyprint: {ex}')
    ...

class StringFormatter:
    """
    Класс для форматирования строк, включая HTML escape и unescape.
    """
    @staticmethod
    def escape_html_tags(text: str) -> str:
        """
        Преобразует HTML теги в escape-последовательности.

        Args:
            text (str): Строка с HTML тегами.
        Returns:
            str: Строка с HTML тегами, преобразованными в escape-последовательности.
        """
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#39;')
        return text

    @staticmethod
    def unescape_html_tags(text: str) -> str:
        """
        Преобразует escape-последовательности обратно в HTML теги.
        
        Args:
            text (str): Строка с escape-последовательностями.
        Returns:
            str: Строка с escape-последовательностями, преобразованными в HTML теги.
        """
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&quot;', '"')
        text = text.replace('&#39;', "'")
        return text

def html2escape(input_str: str) -> str:
    """
    Преобразует HTML в escape-последовательности.
    
    Args:
        input_str (str): HTML код.
    
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
    Преобразует escape-последовательности в HTML.
    
    Args:
        input_str (str): Строка с escape-последовательностями.
    
    Returns:
        str: Escape-последовательности, преобразованные в HTML.
        
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
        html_str (str): HTML строка для преобразования.
    
    Returns:
        dict: Словарь, где HTML теги являются ключами, а их содержимое - значениями.
        
    Example:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        """
        Вспомогательный класс для разбора HTML и преобразования его в словарь.
        """
        def __init__(self):
            """
            Инициализация парсера HTML.
            """
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            """
            Обрабатывает начальный тег HTML.

            Args:
                tag (str): Имя тега.
                attrs (list): Список атрибутов тега.
            """
            self.current_tag = tag

        def handle_endtag(self, tag):
            """
            Обрабатывает конечный тег HTML.

            Args:
                tag (str): Имя тега.
            """
            self.current_tag = None

        def handle_data(self, data):
            """
            Обрабатывает текстовые данные внутри тегов.

            Args:
                data (str): Текстовые данные.
            """
            if self.current_tag:
                self.result[self.current_tag] = data.strip()
    
    # Создание экземпляра парсера
    parser = HTMLToDictParser()
    # Передача HTML строки в парсер
    parser.feed(html_str)
    # Возврат результата
    return parser.result

def html2ns(html_str: str) -> SimpleNamespace:
    """
    Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.
    
    Args:
        html_str (str): HTML строка для преобразования.
    
    Returns:
        SimpleNamespace: Объект SimpleNamespace, где HTML теги являются атрибутами, а их содержимое - значениями.
        
    Example:
        >>> html = '<p>Hello</p><a href=\'link\'>World</a>'
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    # Преобразование HTML в словарь
    html_dict = html2dict(html_str)
    # Возврат объекта SimpleNamespace из словаря
    return SimpleNamespace(**html_dict)

def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Преобразует HTML в PDF файл, используя WeasyPrint.
    
    Args:
        html_str (str): HTML содержимое в виде строки.
        pdf_file (str | Path): Путь к выходному PDF файлу.
    
    Returns:
        bool | None: Возвращает `True`, если PDF был успешно создан, `None` в противном случае.
    """
    try:
        # Создание PDF из HTML строки
        HTML(string=html_str).write_pdf(pdf_file)
        # Возврат True при успешном создании
        return True
    except Exception as e:
        # Логирование ошибки при возникновении исключения
        logger.error(f'Ошибка при создании PDF: {e}')
        return
```