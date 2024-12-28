# Анализ кода модуля `__morlevi__.py`

**Качество кода: 6/10**

- **Плюсы**
    - Код структурирован в функции, что облегчает понимание и поддержку.
    - Используется logging для отслеживания ошибок и отладки.
    - Присутствуют docstring для некоторых функций, но они не соответствуют стандарту reStructuredText.
    - Код использует `execute_locator` для взаимодействия с веб-элементами, что делает его более гибким.
- **Минусы**
    - Комментарии не соответствуют формату reStructuredText.
    - Используются стандартные `try-except` блоки вместо `logger.error` для обработки ошибок.
    - Есть повторения кода, например, в обработке `_product_list_from_page` в `list_products_in_category_from_pagination`.
    - Не все функции и переменные имеют docstring.
    - Не используются импорты `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Есть неиспользуемый код.
    - Встречаются конструкции типа `if str(type(close_pop_up_btn)).execute_locator("class \'list\'") >-1`, которые выглядят неоптимально и трудночитаемы.
    - Используется eval для вычисления цены, что небезопасно.
    - Есть `...`  в коде.
    - Отсутствует обработка ошибок в функциях `set_images`, `set_combinations` и других.
    - Не везде соблюдается консистентность в именовании переменных (иногда с `_` в начале, иногда без)

**Рекомендации по улучшению**

1.  **Формат документации**:
    -   Переписать все комментарии в формате reStructuredText.
    -   Добавить docstring для всех функций, классов и методов.
2.  **Обработка ошибок**:
    -   Использовать `logger.error` вместо `try-except` для обработки ошибок.
    -   Добавить проверку на корректность данных перед их использованием.
3.  **Импорты**:
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов (если это требуется).
    -   Добавить отсутствующие импорты.
4.  **Рефакторинг**:
    -   Упростить и переписать конструкции типа `if str(type(close_pop_up_btn)).execute_locator("class \'list\'") >-1`.
    -   Вынести повторяющийся код в отдельные функции.
    -   Избегать использования `eval`. Применять более безопасные способы вычисления цены.
    -   Улучшить логику обработки списка товаров в категории и пагинации.
    -   Удалить неиспользуемый код и `...`  в коде.
5.  **Безопасность**:
    -   Заменить `eval` на безопасный способ вычисления цены, например, с использованием `ast.literal_eval` или более явно написанной логики.
6. **Консистентность**:
    - Привести к единообразию именование переменных.
7.  **Дополнительные улучшения**:
    -   Добавить type hints для параметров и возвращаемых значений функций.
    -   Рассмотреть возможность добавления асинхронности в функции.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиком Morlevi.
=========================================================================================

Этот модуль содержит функции для авторизации на сайте Morlevi,
сбора информации о товарах и их категориях.

.. module:: src.suppliers.ivory
   :platform: Windows, Unix
   :synopsis: Модуль для работы с поставщиком Morlevi
"""

import ast
from pathlib import Path
import requests
import pandas as pd
from typing import List, Any
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from src.settings import StringFormatter
from src.settings import json_loads
from src.logger.logger import logger
from src.suppliers.Product import Product


MODE = 'dev'

def login(supplier):
    """
    Выполняет вход на сайт поставщика.

    :param supplier: Объект поставщика.
    :type supplier: object
    :return: True в случае успешного входа, None в случае ошибки.
    :rtype: bool or None
    """
    _s = supplier
    _d = _s.driver
    _d.get_url('https://www.morlevi.co.il')
    if _login(_s):
        return True
    else:
        try:
            logger.error('Ошибка, пытаюсь закрыть popup')
            _d.page_refresh()
            if _login(_s):
                return True

            close_pop_up_locator = _s.locators['login']['close_pop_up_locator']
            close_pop_up_btn = _d.execute_locator(close_pop_up_locator)
            _d.wait(5)
            # Проверка типа элемента и закрытие popup
            if isinstance(close_pop_up_btn, list):
                for b in close_pop_up_btn:
                    try:
                        b.click()
                        if _login(_s):
                            return True
                    except Exception as ex:
                        logger.error(f'Ошибка закрытия модального окна: {ex}')
                        continue
            elif isinstance(close_pop_up_btn, WebElement):
                close_pop_up_btn.click()
                return _login(_s)
        except Exception as ex:
            logger.error(f'Не удалось залогиниться: {ex}')
            return

def _login(_s):
    """
    Вспомогательная функция для выполнения входа на сайт.

    :param _s: Объект поставщика.
    :type _s: object
    :return: True в случае успешного входа, None в случае ошибки.
    :rtype: bool or None
    """
    logger.debug('Собссно, логин Морлеви')
    _d = _s.driver
    _d.refresh()
    _l = _s.locators['login']
    try:
        _d.execute_locator(_l['open_login_dialog_locator'])
        _d.wait(1.3)
        _d.execute_locator(_l['email_locator'])
        _d.wait(.7)
        _d.execute_locator(_l['password_locator'])
        _d.wait(.7)
        _d.execute_locator(_l['loginbutton_locator'])
        logger.debug('Mor logged in')
        return True
    except Exception as ex:
        logger.error(f'LOGIN ERROR: {ex}')
        return

def grab_product_page(s):
    """
    Собирает информацию о товаре на странице.

    :param s: Объект поставщика.
    :type s: object
    :return: Объект Product с собранными данными или None в случае ошибки.
    :rtype: Product or None
    """
    p = Product(supplier=s)
    _l = s.locators['product']
    _d = s.driver
    _field = p.fields

    # Закрытие модального окна
    try:
        _d.click(s.locators['close_pop_up_locator'])
    except Exception as ex:
       logger.error(f'Не удалось закрыть модальное окно: {ex}')
       return None
    
    def set_id():
        """Устанавливает id товара."""
        _id = _d.execute_locator(_l['sku_locator'])
        if isinstance(_id, list):
            _field['id'] = _id[0]
            _field['Rewritten URL'] = str(_id[1]).replace(' ', '-')

    def set_sku_suppl():
        """Устанавливает sku поставщика."""
        _field['sku suppl'] = _field['id']

    def set_sku_prod():
         """Устанавливает sku товара."""
         _field['sku'] = f'mlv-{_field["id"]}'

    def set_title():
         """Устанавливает заголовок товара."""
         _field['title'] = _d.title

    def set_summary():
        """Устанавливает краткое описание товара."""
        _field['summary'] = _d.execute_locator(_l['summary_locator'])
        _field['meta description'] = _field['summary']

    def set_description():
         """Устанавливает полное описание товара."""
         _field['description'] = _d.execute_locator(_l['description_locator'])

    def set_cost_price():
        """Устанавливает цену товара."""
        _price = _d.execute_locator(_l['price_locator'])
        if _price:
            _price = _price.replace(',', '')
            _price = StringFormatter.clear_price(_price)
            try:
                 _field['cost price'] = round(eval(f'{_price}{s.settings["price_rule"]}'))
            except (ValueError, TypeError, SyntaxError) as ex:
                logger.error(f'Ошибка при вычислении цены: {ex}, price: {_price}')
                return False
        else:
            logger.error('Не найдена цена для товара')
            return False
        return True


    def set_before_tax_price():
        """Устанавливает цену без налога."""
        _field['price tax excluded'] = _field['cost price']
        return True

    def set_delivery():
        """Устанавливает параметры доставки (TODO: перенести в комбинации)."""
        ...

    def set_images():
        """Устанавливает изображения товара."""
        _images = _d.execute_locator(_l['main_image_locator'])
        if not _images:
            return
        _field['img url'] = _images

    def set_combinations():
        """Устанавливает комбинации товара."""
        ...

    def set_qty():
         """Устанавливает количество товара."""
         ...

    def set_specification():
        """Устанавливает спецификацию товара."""
        _field['specification'] = _d.execute_locator(_l['product_name_locator'])

    def set_customer_reviews():
         """Устанавливает отзывы покупателей."""
         ...

    def set_supplier():
         """Устанавливает ID поставщика."""
         _field['supplier'] = '2784'
         ...

    def set_rewritted_URL():
         """Устанавливает переписанный URL."""
         ...
    
    set_id()
    set_sku_suppl()
    set_sku_prod()
    set_title()
    if not set_cost_price():
        return None
    set_before_tax_price()
    set_delivery()
    set_images()
    set_combinations()
    set_description()
    set_summary()
    set_supplier()
    set_rewritted_URL()
    set_specification()


    return p


def list_products_in_category_from_pagination(supplier):
    """
    Собирает список ссылок на товары в категории с пагинацией.

    :param supplier: Объект поставщика.
    :type supplier: object
    :return: Список ссылок на товары.
    :rtype: list
    """
    _s = supplier
    _d = _s.driver
    _l = _s.locators['product']['link_to_product_locator']

    list_products_in_category = []
    _product_list_from_page = _d.execute_locator(_l)

    if not _product_list_from_page:
        return list_products_in_category

    if isinstance(_product_list_from_page, list):
        list_products_in_category.extend(_product_list_from_page)
    else:
        list_products_in_category.append(_product_list_from_page)

    pages = _d.execute_locator(_s.locators['pagination']['a'])
    if isinstance(pages, list):
        for page in pages:
            _perv_url = _d.current_url
            try:
                page.click()
                _product_list_from_page = _d.execute_locator(_l)
            except Exception as ex:
                logger.error(f"Ошибка при клике на страницу пагинации: {ex}")
                break

            if _perv_url == _d.current_url:
                break

            if isinstance(_product_list_from_page, list):
                list_products_in_category.extend(_product_list_from_page)
            elif _product_list_from_page:
                 list_products_in_category.append(_product_list_from_page)


    return list(set(list_products_in_category)) if isinstance(list_products_in_category, list) else list_products_in_category


def get_list_products_in_category(s, scenario, presath):
    """
    Получает список товаров в категории.

    :param s: Объект поставщика.
    :type s: object
    :param scenario: JSON сценарий.
    :type scenario: dict
    :param presath: Объект PrestaShopWebServiceDict.
    :type presath: object
    :return: None
    """
    l = list_products_in_category_from_pagination(s)
    ...


def get_list_categories_from_site(s, scenario_file, brand=''):
    """
    Получает список категорий с сайта.

    :param s: Объект поставщика.
    :type s: object
    :param scenario_file: Путь к файлу сценария.
    :type scenario_file: str
    :param brand: Бренд.
    :type brand: str
    :return: None
    """
    ...

```