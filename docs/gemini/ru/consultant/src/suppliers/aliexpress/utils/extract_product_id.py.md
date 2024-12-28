# Анализ кода модуля `extract_product_id`

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован и логически понятен.
    -  Используются `docstring` для описания функций и модуля.
    -  Код обрабатывает как отдельные URL, так и списки URL.
    -  Есть примеры использования функций в docstring.
-  Минусы
    -  Отсутствует обработка ошибок с использованием `logger`.
    -  Не все комментарии соответствуют формату reStructuredText.
    -  Некоторые docstring можно улучшить для большей ясности.

**Рекомендации по улучшению**
1. Добавить обработку ошибок с помощью `logger.error` в функции `extract_id`, для записи в журнал, если не удалось извлечь идентификатор.
2.  Переписать все комментарии и `docstring` в соответствии с форматом reStructuredText.
3.  Улучшить `docstring` для более точного описания параметров и возвращаемых значений.
4.  Добавить проверку входных данных, чтобы избежать ошибок при использовании.
5.  Импортировать `logger` из `src.logger.logger` как рекомендовано в инструкции.
6.  Использовать `isinstance(urls, str)` вместо `else`, для более явной проверки, что `urls` является строкой.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для извлечения идентификаторов товаров из URL-адресов AliExpress.
=========================================================================

Этот модуль содержит функции для извлечения идентификаторов товаров из URL-адресов AliExpress.
Он поддерживает как отдельные URL-адреса, так и списки URL-адресов.

Пример использования
--------------------

Пример извлечения идентификатора товара из URL-адреса:

.. code-block:: python

    from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids

    url = "https://www.aliexpress.com/item/123456.html"
    product_id = extract_prod_ids(url)
    print(product_id)

Пример извлечения идентификаторов товаров из списка URL-адресов:

.. code-block:: python

    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/789012.html"]
    product_ids = extract_prod_ids(urls)
    print(product_ids)
"""


import re
from src.logger.logger import logger # Импортируем logger

def extract_prod_ids(urls: str | list[str]) -> str | list[str] | None:
    """
    Извлекает идентификаторы товаров из списка URL-адресов или возвращает идентификаторы, если они переданы напрямую.

    :param urls: URL-адрес, список URL-адресов или идентификаторы товаров.
    :type urls: str | list[str]
    :return: Список извлеченных идентификаторов товаров, одиночный идентификатор или None, если не найден допустимый идентификатор.
    :rtype: str | list[str] | None

    :Examples:

    .. code-block:: python

        >>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
        '123456'

        >>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
        ['123456', '7891011']

        >>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
        ['123456']

        >>> extract_prod_ids("7891011")
        '7891011'

        >>> extract_prod_ids("https://www.example.com/item/abcdef.html")
        None
    """
    # Регулярное выражение для поиска идентификаторов товаров
    pattern = re.compile(r"(?:item/|/)?(\d+)\.html")

    def extract_id(url: str) -> str | None:
        """
        Извлекает идентификатор товара из заданного URL-адреса или проверяет его валидность.

        :param url: URL-адрес или идентификатор товара.
        :type url: str
        :return: Извлеченный идентификатор товара или сам ввод, если это допустимый идентификатор, или None, если не найден допустимый идентификатор.
        :rtype: str | None

        :Examples:

        .. code-block:: python

            >>> extract_id("https://www.aliexpress.com/item/123456.html")
            '123456'

            >>> extract_id("7891011")
            '7891011'

            >>> extract_id("https://www.example.com/item/abcdef.html")
            None
        """
        # Проверяет, является ли ввод допустимым идентификатором товара
        if url.isdigit():
            return url

        # Пытается извлечь идентификатор из URL-адреса
        match = pattern.search(url)
        if match:
            return match.group(1)
        # Если извлечение не удалось, записываем ошибку в журнал и возвращает None
        logger.error(f'Не удалось извлечь ID из url: {url}')
        return None

    # Проверяем, является ли urls списком
    if isinstance(urls, list):
        # Извлекает идентификаторы из списка URL, если они есть
        extracted_ids = [extract_id(url) for url in urls if extract_id(url) is not None]
        # Возвращает список извлеченных идентификаторов или None, если список пуст
        return extracted_ids if extracted_ids else None
    # Если urls не список, то это строка
    if isinstance(urls, str):
       # Извлекает идентификатор из одной строки
        return extract_id(urls)
    # Если тип входных данных не распознан, то логируем ошибку и возвращаем None
    logger.error(f'Неверный тип данных {type(urls)=}')
    return None
```