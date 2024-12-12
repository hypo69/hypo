# Анализ кода модуля `ensure_https.py`

**Качество кода**
8
- Плюсы
    - Код выполняет поставленную задачу, обеспечивает добавление `https://` к URL или создание полного URL из ID продукта.
    - Присутствуют docstring для модуля и функций, соответствующие стандарту.
    - Используется `logger` для записи ошибок.
- Минусы
    - Код содержит точки остановки `...`, которые должны быть убраны.
    - Отсутствует обработка исключения `ValueError`.
    - В docstring модуля присутствует пример кода, который не является частью документации reStructuredText (RST) и должен быть оформлен корректно.
    - Внутренняя функция `ensure_https_single` не имеет  проверку на `WindowsPath`.

**Рекомендации по улучшению**
1. **Удалить точки остановки**: Убрать все `...` из кода.
2. **Обработка `ValueError`**:  Добавить проверку на `WindowsPath` в `ensure_https_single`  и  `ensure_https` и вызов `logger.error` если условие соблюдено
3. **Форматирование docstring**: Привести примеры кода в docstring модуля в соответствие с RST.
4. **Логирование**: Добавить обработку ошибки `ValueError` с помощью `logger.error` в функции `ensure_https`.
5. **Переименования**:
    - Переименовать `prod_ids` в `url` или `urls` для соответствия с логикой кода.
    - Переименовать `_prod_id` в `product_id`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для обеспечения наличия https:// префикса в URL
======================================================

Этот модуль предоставляет функцию :func:`ensure_https`, которая проверяет,
содержит ли предоставленная строка URL или список URL-строк префикс `https://`.
Если входные данные являются идентификатором продукта,
функция создает полный URL с префиксом `https://`.

Примеры использования
--------------------

Пример использования функции ``ensure_https``:

.. code-block:: python

    url = "example_product_id"
    url_with_https = ensure_https(url)
    print(url_with_https)  # Вывод: https://www.aliexpress.com/item/example_product_id.html

    urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
    urls_with_https = ensure_https(urls)
    print(urls_with_https)  # Вывод: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

"""
MODE = 'dev'

from src.logger.logger import logger
from .extract_product_id import extract_prod_ids
from pathlib import WindowsPath


def ensure_https(urls: str | list[str]) -> str | list[str]:
    """
    Обеспечивает наличие префикса https:// в URL или создает полный URL из ID продукта.

    :param urls: URL-адрес или список URL-адресов для проверки и изменения при необходимости.
    :type urls: str | list[str]
    :raises ValueError: Если `urls` является экземпляром `WindowsPath`.
    :return: URL-адрес или список URL-адресов с префиксом https://.
    :rtype: str | list[str]

    Примеры:

    >>> ensure_https("example_product_id")
    'https://www.aliexpress.com/item/example_product_id.html'

    >>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
    ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

    >>> ensure_https("https://www.example.com/item/example_product_id")
    'https://www.example.com/item/example_product_id'
    """
    def ensure_https_single(url: str) -> str:
        """
        Обеспечивает наличие префикса https:// в одном URL-адресе или строке ID продукта.

        :param url: URL-адрес или строка ID продукта.
        :type url: str
        :raises ValueError: Если `url` является экземпляром `WindowsPath`.
        :return: URL-адрес с префиксом https://.
        :rtype: str

        Примеры:
            >>> ensure_https_single("example_product_id")
            'https://www.aliexpress.com/item/example_product_id.html'

            >>> ensure_https_single("https://www.example.com/item/example_product_id")
            'https://www.example.com/item/example_product_id'
        """
        # Проверяет, является ли `url` экземпляром `WindowsPath`.
        if isinstance(url, WindowsPath):
            logger.error(f"Обнаружен недопустимый тип данных: {url=}. Ожидалась строка URL или ID продукта.", exc_info=True)
            raise ValueError(f"Недопустимый тип данных: {url=}. Ожидалась строка URL или ID продукта.")

        # Извлекает ID продукта из URL.
        product_id = extract_prod_ids(url)
        # Если ID продукта найден, код формирует URL с использованием ID продукта.
        if product_id:
            return f"https://www.aliexpress.com/item/{product_id}.html"
        # Если ID продукта не найден, код выводит сообщение об ошибке и возвращает исходный URL.
        else:
            logger.error(f"Некорректный ID продукта или URL: {url=}", exc_info=False)
            return url

    # Проверяет, является ли `urls` списком.
    if isinstance(urls, list):
        # Код обрабатывает каждый URL из списка с помощью функции `ensure_https_single`.
        return [ensure_https_single(url) for url in urls]
    # Если `urls` не список, код обрабатывает `urls` как отдельный URL.
    else:
        return ensure_https_single(urls)
```