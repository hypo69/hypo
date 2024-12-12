# Анализ кода модуля `extract_product_id.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и соответствует PEP 8.
    - Присутствует подробная документация в формате reStructuredText (RST) для модуля и функций, включая примеры использования.
    - Код содержит type hints, что облегчает понимание и отладку.
    - Используются регулярные выражения для извлечения ID, что является эффективным подходом.
    - Код обрабатывает как одиночные URL, так и списки URL.
    - Есть валидация и обработка ошибок: при отсутствии ID в URL или невалидном ID возвращается `None`.
-  Минусы
    - Отсутствует импорт `Any` из модуля `typing`, что не позволяет использовать этот тип в аннотации.
    - Нет обработки исключений (try-except) с использованием `logger.error` при поиске и извлечении ID, что может привести к неопределенному поведению при непредвиденных ошибках.
    - В некоторых местах код можно сделать более лаконичным (например, объединить проверки)
    - Отсутствует явное логирование.

**Рекомендации по улучшению**
1. **Добавить импорт `Any`**:
   - В начале файла добавить `from typing import Any` для корректной работы аннотаций типов.
2. **Обработка ошибок с использованием `logger.error`**:
   - Обновить функцию `extract_id` так, чтобы в случае ошибки при поиске ID с помощью регулярного выражения, ошибка логировалась, а функция возвращала `None`.
3. **Упростить логику проверки и возврата значений**:
   - Код `return extracted_ids if extracted_ids else None` в функции `extract_prod_ids` можно упростить, вернув `extracted_ids or None`.
4. **Добавить логирование**
   - Логировать начало и завершение функции а так же все ошибки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для извлечения идентификаторов продуктов из URL-адресов.
=============================================================

Этот модуль содержит функции для извлечения идентификаторов продуктов
из URL-адресов, используемых на сайте AliExpress. Он обрабатывает как
одиночные URL-адреса, так и списки URL-адресов, возвращая извлеченные
идентификаторы в виде строк или списков строк.

Примеры использования
--------------------

.. code-block:: python

   from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids

   # Извлечение ID из одиночного URL
   url = "https://www.aliexpress.com/item/123456.html"
   product_id = extract_prod_ids(url)
   print(product_id)  # Вывод: '123456'

   # Извлечение ID из списка URL
   urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/789012.html"]
   product_ids = extract_prod_ids(urls)
   print(product_ids)  # Вывод: ['123456', '789012']

   # Обработка невалидного URL или ID
   invalid_url = "https://www.example.com/item/abcdef.html"
   invalid_id = extract_prod_ids(invalid_url)
   print(invalid_id)  # Вывод: None

   # Обработка ID напрямую
   direct_id = extract_prod_ids("1234567")
   print(direct_id) # Вывод: '1234567'
"""

import re
from typing import List, Union, Optional, Any
from src.logger.logger import logger


def extract_prod_ids(urls: Union[str, List[str]]) -> Optional[Union[str, List[str]]]:
    """Извлекает идентификаторы продуктов из списка URL-адресов или возвращает ID напрямую, если они были переданы.

    :param urls: URL-адрес, список URL-адресов или идентификаторы продуктов.
    :type urls: str | list[str]
    :return: Список извлеченных идентификаторов продуктов, один ID или None, если не найдено ни одного допустимого ID.
    :rtype: str | list[str] | None

    :Example:
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
    logger.info(f'Начало извлечения ID из {urls=}')
    # Регулярное выражение для поиска идентификаторов продуктов
    pattern = re.compile(r"(?:item/|/)?(\d+)\.html")


    def extract_id(url: str) -> Optional[str]:
        """Извлекает идентификатор продукта из заданного URL-адреса или проверяет идентификатор продукта.

        :param url: URL-адрес или идентификатор продукта.
        :type url: str
        :return: Извлеченный идентификатор продукта или сам ввод, если это допустимый ID, или None, если допустимый ID не найден.
        :rtype: str | None

        :Example:
            >>> extract_id("https://www.aliexpress.com/item/123456.html")
            '123456'

            >>> extract_id("7891011")
            '7891011'

            >>> extract_id("https://www.example.com/item/abcdef.html")
            None
        """
        # Проверка, является ли ввод допустимым идентификатором продукта
        if url.isdigit():
            return url
        
        # Пытаемся извлечь ID из URL-адреса
        try:
            match = pattern.search(url)
            if match:
                return match.group(1)
            return None
        except Exception as ex:
            logger.error(f'Ошибка при извлечении ID из {url=}', exc_info=ex)
            return None

    if isinstance(urls, list):
        # Извлекаем ID из каждого URL, если ID не `None`
        extracted_ids = [extract_id(url) for url in urls if extract_id(url) is not None]
        logger.info(f'Извлеченные ID {extracted_ids=}')
        return extracted_ids or None
    else:
        result = extract_id(urls)
        logger.info(f'Извлеченный ID {result=}')
        return result
```