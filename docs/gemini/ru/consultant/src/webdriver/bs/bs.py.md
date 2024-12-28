# Анализ кода модуля `bs.py`

**Качество кода**

8
-   Плюсы
    -   Код имеет docstring для модуля, класса и методов.
    -   Используется `logger` для обработки ошибок.
    -   Применяется `j_loads_ns` для чтения JSON данных.
    -   Код достаточно структурирован и понятен.
    -   Используются типы для параметров и возвращаемых значений.
-   Минусы
    -   Используется  `try-except`  с общим `Exception` без конкретизации, что затрудняет отладку.
    -   Не все комментарии соответствуют формату reStructuredText (RST).
    -   В `execute_locator`  используется жесткое кодирование XPath запросов, что снижает гибкость.
    -   Отсутствуют проверки валидности `locator`.

**Рекомендации по улучшению**

1.  **Формат документации**:
    -   Привести все комментарии и docstring в формат reStructuredText (RST).
2.  **Обработка ошибок**:
    -   Избегать общих исключений `Exception` и использовать конкретные типы исключений.
    -   Улучшить логирование ошибок, добавить контекст к сообщениям.
3.  **Структура кода**:
    -   Улучшить обработку локаторов, предусмотреть больше вариантов `by`.
    -   Добавить валидацию `locator` перед использованием.
4.  **Комментарии**:
    -   Улучшить комментарии в коде, сделав их более информативными.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц с использованием `BeautifulSoup` и XPath
=========================================================================================

Этот модуль предоставляет пользовательскую реализацию для парсинга HTML контента,
используя `BeautifulSoup` и XPath.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        parser = BS()
        parser.get_url('https://example.com')
        locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
        elements = parser.execute_locator(locator)
        print(elements)
"""

MODE = 'dev'

import re
from pathlib import Path
from typing import Optional, Union, List, Any
from types import SimpleNamespace
from bs4 import BeautifulSoup
from lxml import etree
import requests
# from src import gs  #  Импорт не используется, удалён
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class BS:
    """
    Класс для парсинга HTML контента с использованием `BeautifulSoup` и XPath.

    :ivar html_content: HTML контент для парсинга.
    :vartype html_content: str
    """

    html_content: str = None

    def __init__(self, url: Optional[str] = None):
        """
        Инициализирует парсер BS с необязательным URL.

        :param url: URL или путь к файлу для получения HTML контента.
        :type url: Optional[str]
        """
        if url:
            self.get_url(url)

    def get_url(self, url: str) -> bool:
        """
        Получает HTML контент из файла или URL и парсит его с помощью BeautifulSoup и XPath.

        :param url: Путь к файлу или URL для получения HTML контента.
        :type url: str
        :return: True, если контент был успешно получен, иначе False.
        :rtype: bool
        """
        if url.startswith('file://'):
            # Удаляет префикс 'file://' и очищает путь
            cleaned_url = url.replace(r'file:///', '')

            # Извлекает Windows путь, если он имеет вид 'c:/...' или 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        #  Код читает содержимое файла
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except FileNotFoundError as ex:
                        # Логирование ошибки при чтении файла
                        logger.error(f'Файл не найден: {file_path}', exc_info=ex)
                        return False
                    except Exception as ex:
                        #  Логирование общей ошибки при чтении файла
                        logger.error(f'Исключение при чтении файла: {file_path}', exc_info=ex)
                        return False
                else:
                    #  Логирование ошибки, если локальный файл не найден
                    logger.error(f'Локальный файл не найден: {file_path}')
                    return False
            else:
                #  Логирование ошибки, если путь к файлу невалидный
                logger.error(f'Невалидный путь к файлу: {cleaned_url}')
                return False
        elif url.startswith('https://'):
            # Обрабатывает веб-URL
            try:
                response = requests.get(url)
                response.raise_for_status()  # Проверяет HTTP ошибки запроса
                # Код присваивает полученный HTML-контент
                self.html_content = response.text
                return True
            except requests.RequestException as ex:
                 #  Логирование ошибки при получении URL
                logger.error(f"Ошибка при получении {url}:", exc_info=ex)
                return False
        else:
            #  Логирование ошибки, если URL или путь к файлу невалиден
            logger.error(f'Невалидный URL или путь к файлу: {url}')
            return False

    def execute_locator(self, locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]:
        """
        Выполняет XPath локатор на HTML контенте.

        :param locator: Объект локатора, содержащий селектор и атрибут.
        :type locator: Union[SimpleNamespace, dict]
        :param url: Необязательный URL или путь к файлу для получения HTML контента.
        :type url: Optional[str]
        :return: Список элементов, соответствующих локатору.
        :rtype: List[etree._Element]
        """
        if url:
            self.get_url(url)

        if not self.html_content:
            #  Логирование ошибки, если нет HTML контента
            logger.error('Нет HTML контента для парсинга.')
            return []

        soup = BeautifulSoup(self.html_content, 'lxml')
        tree = etree.HTML(str(soup))  # Преобразует объект BeautifulSoup в lxml дерево

        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        if not hasattr(locator, 'attribute') or not hasattr(locator, 'by') or not hasattr(locator, 'selector'):
            #  Логирование ошибки, если локатор невалиден
            logger.error(f'Невалидный локатор: {locator}')
            return []

        attribute = locator.attribute
        by = locator.by.upper()
        selector = locator.selector
        elements = None

        if by == 'ID':
            #  Код выполняет поиск элемента по ID
            elements = tree.xpath(f'//*[@id="{attribute}"]')
        elif by == 'CSS':
            #  Код выполняет поиск элемента по CSS классу
            elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
        elif by == 'TEXT':
             #  Код выполняет поиск элемента по типу input
            elements = tree.xpath(f'//input[@type="{attribute}"]')
        elif by == 'XPATH':
            #  Код выполняет поиск элемента по XPath
            elements = tree.xpath(selector)
        else:
            # Логирование ошибки, если тип локатора не поддерживается
            logger.error(f'Тип локатора "{by}" не поддерживается.')
            return []


        return elements


if __name__ == "__main__":
    parser = BS()
    parser.get_url('https://example.com')
    locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
    elements = parser.execute_locator(locator)
    print(elements)
```