# Анализ кода модуля `scenario.py`

**Качество кода**
7
- Плюсы
    - Код имеет базовую структуру и логику для сбора товаров с сайта Amazon.
    - Используется логгер для отслеживания ошибок и предупреждений.
    - Есть комментарии, объясняющие назначение некоторых частей кода.
- Минусы
    - Не все комментарии соответствуют формату RST.
    - Отсутствуют docstring для модуля и функции.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не хватает обработки исключений с помощью `logger.error`.
    -  Используются магические значения (например, `'category'`, `'product_links'`).
    -  Отсутствует обработка исключений при работе с драйвером.
    -  Не все комментарии достаточно подробные.
    -  Код не соответствует pep8.
    -  Много пустых docstring.
    -  Нет проверки на прокрутку страниц.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить docstring в формате reStructuredText (RST) для модуля и функции `get_list_products_in_category`.
    - Дополнить комментарии после `#` подробными объяснениями.

2.  **Импорты**:
    - Добавить отсутствующие импорты, если это необходимо.
    - Проверить и, если нужно, отсортировать импорты.
    - Все импорты должны быть в одном месте

3.  **Обработка данных**:
    - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо.
    - Исключить использование `json.load`.

4.  **Логирование**:
    - Использовать `logger.error` для обработки исключений вместо `try-except`.
    - Улучшить сообщения логов, добавив больше контекста.

5.  **Рефакторинг**:
    - Улучшить читаемость кода, добавив пробелы между операторами и вокруг скобок.
    - Вынести повторяющиеся блоки кода в отдельные функции.
    -  Улучшить форматирование строк.
    -  Переименовать переменные для большей ясности.
    -  Добавить обработку исключений при работе с драйвером.
    -  Избавиться от магических значений.
    -  Добавить документацию ко всем полям классов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для сбора товаров со страницы категорий поставщика Amazon.
===============================================================

Этот модуль содержит функции для сбора списка товаров со страниц категорий Amazon.
Он включает в себя функции для извлечения URL товаров и проверки их наличия в базе данных.

Основные функции:
-----------------
- :func:`get_list_products_in_category`: Извлекает URL товаров со страницы категории.

Пример использования:
---------------------
.. code-block:: python

    from src.suppliers.amazon.scenario import get_list_products_in_category
    from src.suppliers.amazon.amazon_supplier import AmazonSupplier  # Assuming AmazonSupplier is defined
    
    supplier = AmazonSupplier()  # Initialize your supplier instance
    product_urls = get_list_products_in_category(supplier)
    if product_urls:
        for url in product_urls:
            print(url)
"""

from typing import List, Optional
from pathlib import Path

from src import gs
from src.logger.logger import logger


def get_list_products_in_category(s) -> Optional[List[str]]:
    """
    Извлекает список URL товаров со страницы категории.

    :param s: Экземпляр класса поставщика (Supplier).
    :type s: src.suppliers.amazon.amazon_supplier.AmazonSupplier
    :return: Список URL товаров или None в случае ошибки.
    :rtype: Optional[List[str]]

    :raises TypeError: Если `s` не является объектом поставщика.
    
    ..  note::
        Если локаторы не найдены, функция возвращает `None`.
        Если не найдено ссылок на товары, функция возвращает `None`.
        
    """
    if not hasattr(s, 'driver') or not hasattr(s, 'locators'):
         logger.error('Переданный объект не является объектом поставщика')
         return None

    d = s.driver
    l: dict = s.locators.get('category')

    if not l:
        logger.error(f'Локаторы не найдены: {l}')
        return None

    try:
        d.scroll()
        # TODO: Нет листалки
        list_products_in_category = d.execute_locator(l.get('product_links'))
    except Exception as e:
        logger.error(f"Ошибка при выполнении локатора: {e}")
        return None
    
    if not list_products_in_category:
        logger.warning('Не найдено ссылок на товары')
        return None
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category
    logger.info(f'Найдено {len(list_products_in_category)} товаров')
    return list_products_in_category
```