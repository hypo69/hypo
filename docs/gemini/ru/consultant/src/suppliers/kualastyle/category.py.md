# Анализ кода модуля `category`

**Качество кода**
9
 - Плюсы
        - Код имеет docstring для модуля и функций, что улучшает читаемость.
        - Используется logger для записи ошибок и отладочной информации.
        - Код в целом структурирован и выполняет поставленные задачи.
 - Минусы
    -  Некоторые docstring требуют доработки.
    - Есть импорты, которые не используются.
    -  Используются `...` в коде.
    -  Не все переменные имеют аннотации типов.
    -  Использование `list[str, str, None]` не соответствует ожидаемому возвращаемому значению.
**Рекомендации по улучшению**
1. **Импорты**:
   - Удалить неиспользуемые импорты.
2. **Документация**:
   - Уточнить docstring для функций, добавив информацию о параметрах и возвращаемых значениях.
   - Добавить примеры использования в docstring для `get_list_products_in_category`.
3. **Обработка ошибок**:
   - Заменить `...` на `return` или `continue` или `pass`, где это необходимо.
4. **Типизация**:
    - Добавить аннотации типов для переменных, где это возможно.
5. **Форматирование**:
   -  Исправить аннотацию типов `list[str, str, None]` на `list[str]`.
6. **Логирование**:
    - Использовать f-строки для форматированного вывода в `logger.debug`.
7. **Общее**:
   - Заменить `while d.current_url != d.previous_url:` на более подходящий вариант, если это необходимо.
**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для сбора товаров со страницы категорий поставщика kualastyle через вебдрайвер.

У каждого поставщика свой сценарий обработки категорий.

- Модуль собирает список категорий со страниц продавца :func:`get_list_categories_from_site`.
  
  .. todo::
     Сделать проверку на изменение категорий на страницах продавца.
     Продавец может добавлять новые категории, переименовывать или удалять/скрывать уже существующие.
     По большому счету надо держать таблицу категории `PrestaShop.categories <-> aliexpress.shop.categories`

- Собирает список товаров со страницы категории :func:`get_list_products_in_category`.
- Итерируясь по списку, передает управление в :func:`grab_product_page`, отправляя функции текущий URL страницы.
  :func:`grab_product_page` обрабатывает поля товара и передает управление классу `Product`.
"""
from typing import List
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.suppliers import Supplier


def get_list_products_in_category(s: Supplier) -> List[str]:
    """
    Извлекает список URL товаров со страницы категории.

    Args:
        s (Supplier): Объект поставщика.

    Returns:
        List[str]: Список URL товаров или пустой список, если товары не найдены.

    Example:
        >>> supplier = Supplier(...)
        >>> product_urls = get_list_products_in_category(supplier)
        >>> if product_urls:
        >>>     for url in product_urls:
        >>>         print(url)
    """
    d: Driver = s.driver
    l: dict = s.locators['category']

    d.wait(1)
    d.execute_locator(s.locators['product']['close_banner'])
    d.scroll()

    list_products_in_category = d.execute_locator(l['product_links'])

    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        return []
    
    while d.current_url != d.previous_url:
        if paginator(d, l, list_products_in_category):
            new_products = d.execute_locator(l['product_links'])
            if new_products:
                if isinstance(new_products, str):
                    list_products_in_category.append(new_products)
                elif isinstance(new_products, list):
                    list_products_in_category.extend(new_products)
        else:
            break
    
    if isinstance(list_products_in_category, str):
        list_products_in_category = [list_products_in_category]
    
    logger.debug(f"Found {len(list_products_in_category)} items in category {s.current_scenario['name']}")

    return list_products_in_category


def paginator(d: Driver, locator: dict, list_products_in_category: list) -> bool:
    """
    Выполняет перелистывание страниц, если это необходимо.

    Args:
        d (Driver): Объект веб-драйвера.
        locator (dict): Локаторы элементов страницы.
        list_products_in_category (list): Текущий список URL товаров.

    Returns:
        bool: True, если перелистывание выполнено успешно, False в противном случае.
    """
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0):
        return False
    return True


def get_list_categories_from_site(s: Supplier) -> None:
    """Сборщик актуальных категорий с сайта."""
    ...