# Анализ кода модуля `extract_product_id`

**Качество кода**
8
- Плюсы
    -  Код соответствует PEP 8, за исключением использования двойных кавычек в docstring
    -  Функция `extract_prod_ids` и вложенная `extract_id` имеют docstring, который соответствует стандарту RST
    -  Логика извлечения ID из URL-адресов реализована корректно
    -  Используется `re.compile` для оптимизации регулярного выражения
- Минусы
    - Отсутствует описание модуля.
    - Не все docstring используют одинарные кавычки.
    - В функции `extract_id` используется `return` без возвращаемого значения.
    - В функции `extract_prod_ids` не обрабатывается исключение `TypeError` при передаче неправильного типа данных в качестве аргумента `urls`.

**Рекомендации по улучшению**

1. Добавить описание модуля.
2. В `docstring` использовать только одинарные кавычки.
3. Изменить `return` на `return None` в функции `extract_id`.
4. Обработать исключение `TypeError` в функции `extract_prod_ids`.
5.  Удалить избыточное `if extract_id(url) is not None`
6.  Добавить комментарии к коду для пояснения логики.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для извлечения идентификаторов продуктов из URL-адресов AliExpress.
=========================================================================

Этот модуль предоставляет функции для извлечения идентификаторов продуктов из URL-адресов AliExpress.
Использует регулярные выражения для поиска идентификаторов в строке.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids

    url = 'https://www.aliexpress.com/item/123456.html'
    product_id = extract_prod_ids(url)
    print(product_id)

    urls = ['https://www.aliexpress.com/item/123456.html', 'https://www.aliexpress.com/item/789012.html']
    product_ids = extract_prod_ids(urls)
    print(product_ids)
"""

import re
from src.logger.logger import logger


def extract_prod_ids(urls: str | list[str]) -> str | list[str] | None:
    """Извлекает идентификаторы товаров из списка URL-адресов или возвращает их, если они были переданы напрямую.

    Args:
        urls (str | list[str]): URL-адрес, список URL-адресов или идентификаторы товаров.

    Returns:
        str | list[str] | None: Список извлеченных идентификаторов товаров, единичный идентификатор или `None`, если не найдено ни одного корректного идентификатора.

    Examples:
        >>> extract_prod_ids('https://www.aliexpress.com/item/123456.html')
        '123456'

        >>> extract_prod_ids(['https://www.aliexpress.com/item/123456.html', '7891011.html'])
        ['123456', '7891011']

        >>> extract_prod_ids(['https://www.example.com/item/123456.html', 'https://www.example.com/item/abcdef.html'])
        ['123456']

        >>> extract_prod_ids('7891011')
        '7891011'

        >>> extract_prod_ids('https://www.example.com/item/abcdef.html')
        None
    """
    # Регулярное выражение для поиска идентификаторов продуктов.
    pattern = re.compile(r'(?:item/|/)?(\d+)\.html')

    def extract_id(url: str) -> str | None:
        """Извлекает идентификатор продукта из заданного URL-адреса или проверяет идентификатор продукта.

        Args:
            url (str): URL-адрес или идентификатор продукта.

        Returns:
            str | None: Извлеченный идентификатор продукта или входные данные, если они являются допустимым идентификатором, или `None`, если не найдено ни одного допустимого идентификатора.

        Examples:
            >>> extract_id('https://www.aliexpress.com/item/123456.html')
            '123456'

            >>> extract_id('7891011')
            '7891011'

            >>> extract_id('https://www.example.com/item/abcdef.html')
            None
        """
        # Проверка, является ли входная строка допустимым идентификатором продукта.
        if url.isdigit():
            return url

        # Попытка извлечь идентификатор из URL-адреса.
        match = pattern.search(url)
        if match:
            return match.group(1)
        return None

    # Код обрабатывает список URL-адресов
    if isinstance(urls, list):
        extracted_ids = [extract_id(url) for url in urls if extract_id(url)]
        return extracted_ids if extracted_ids else None
    # Код обрабатывает один URL-адрес или ID
    else:
        return extract_id(urls)
```