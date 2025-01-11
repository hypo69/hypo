# Анализ кода модуля `bs`

**Качество кода**
6
-  Плюсы
    -  Код модуля содержит docstring для модуля и класса `BS`, что соответствует требованиям к документированию.
    -  Используются `logger.error` для обработки ошибок, что способствует логированию и отслеживанию проблем.
    -  Импортированы необходимые библиотеки для работы с HTML, такие как `BeautifulSoup` и `lxml`.
-  Минусы
    -  Не все функции и методы имеют подробные docstring с описанием аргументов и возвращаемых значений.
    -  Используется конструкция `try-except` без необходимости, `logger.error` вполне достаточно.
    -  В коде отсутствуют примеры использования для методов, что затрудняет понимание их работы.
    -  Смешаны стили оформления, в том числе и docstring, что делает код менее читаемым.
    -  Не используются `j_loads` или `j_loads_ns` для работы с json (это касается чтения файлов, но в данном случае json не используется).

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить подробные docstring для всех функций и методов, включая описание параметров и возвращаемых значений.
    - Использовать формат RST для документации, чтобы она была совместима со Sphinx.
    - Добавить примеры использования для методов в формате docstring.

2.  **Обработка ошибок:**
    -  Избегать избыточного использования `try-except` блоков, так как `logger.error` уже логирует ошибки.

3.  **Структура кода:**
    -  Унифицировать стиль оформления кода, особенно docstring.
    -  Использовать более конкретные сообщения об ошибках в `logger.error`.

4.  **Улучшения:**
   -   Удалить неиспользуемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц с использованием `BeautifulSoup` и XPath.
=========================================================================================

Этот модуль предоставляет класс :class:`BS`, который используется для парсинга HTML контента с помощью
`BeautifulSoup` и XPath. Он поддерживает получение контента как с веб-страниц, так и из локальных файлов.

Пример использования
--------------------

Пример использования класса `BS`:

.. code-block:: python

    if __name__ == "__main__":
        parser = BS()
        parser.get_url('https://example.com')
        locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
        elements = parser.execute_locator(locator)
        print(elements)
"""

import re
from pathlib import Path
from typing import Optional, Union, List
from types import SimpleNamespace
from bs4 import BeautifulSoup
from lxml import etree
import requests
from src.logger.logger import logger #  Импортируем логгер
# from src.utils.jjson import j_loads_ns  # не используется


class BS:
    """
    Класс для парсинга HTML контента с использованием BeautifulSoup и XPath.

    :ivar html_content: HTML контент для парсинга.
    :vartype html_content: str
    """

    html_content: str = None

    def __init__(self, url: Optional[str] = None):
        """
        Инициализирует парсер BS с опциональным URL.

        :param url: URL или путь к файлу для получения HTML контента.
        :type url: Optional[str]

        :Example:
        >>> parser = BS(url="https://example.com")
        >>> parser.html_content is not None
        True
        """
        if url:
            self.get_url(url)

    def get_url(self, url: str) -> bool:
        """
        Получает HTML контент из файла или URL и парсит его с помощью BeautifulSoup и XPath.

        :param url: Путь к файлу или URL для получения HTML контента.
        :type url: str
        :return: True, если контент был успешно получен, False в противном случае.
        :rtype: bool

        :Example:
        >>> parser = BS()
        >>> parser.get_url("https://example.com")
        True
        >>> parser.get_url("file://example.html") # doctest: +SKIP
        False
        """
        if url.startswith('file://'):
            #  Удаляет префикс 'file:///' и очищает путь
            cleaned_url = url.replace(r'file:///', '')
            #  Извлекает Windows путь, если он в формате 'c:/...' или 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Ошибка при чтении файла:', ex)
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path)
                    return False
            else:
                logger.error('Неверный путь к файлу:', cleaned_url)
                return False
        elif url.startswith('https://'):
            #  Обрабатывает веб-URL
            try:
                response = requests.get(url)
                response.raise_for_status()  #  Проверяет HTTP ошибки
                self.html_content = response.text
                return True
            except requests.RequestException as ex:
                logger.error(f'Ошибка при получении {url}:', ex)
                return False
        else:
            logger.error('Неверный URL или путь к файлу:', url)
            return False

    def execute_locator(self, locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]:
        """
        Выполняет XPath локатор на HTML контенте.

        :param locator: Объект локатора, содержащий селектор и атрибут.
        :type locator: Union[SimpleNamespace, dict]
        :param url: Опциональный URL или путь к файлу для получения HTML контента.
        :type url: Optional[str]
        :return: Список элементов, соответствующих локатору.
        :rtype: List[etree._Element]

        :Example:
        >>> parser = BS()
        >>> parser.get_url("https://example.com")
        True
        >>> locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
        >>> elements = parser.execute_locator(locator)
        >>> print(elements) # doctest: +SKIP
        []
        """
        if url:
            self.get_url(url)

        if not self.html_content:
            logger.error('Нет HTML контента для парсинга.')
            return []

        soup = BeautifulSoup(self.html_content, 'lxml')
        tree = etree.HTML(str(soup))  #  Преобразует BeautifulSoup объект в lxml дерево

        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        attribute = locator.attribute
        by = locator.by.upper()
        selector = locator.selector
        elements = None

        if by == 'ID':
            elements = tree.xpath(f'//*[@id="{attribute}"]')
        elif by == 'CSS':
            elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
        elif by == 'TEXT':
            elements = tree.xpath(f'//input[@type="{attribute}"]')
        else:
            elements = tree.xpath(selector)

        return elements


if __name__ == "__main__":
    parser = BS()
    parser.get_url('https://example.com')
    locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
    elements = parser.execute_locator(locator)
    print(elements)
```