# Анализ кода модуля `__morlevi__`

**Качество кода**
8
- Плюсы
    - Код разбит на функции, что улучшает читаемость и повторное использование.
    - Используется `logger` для логирования ошибок и отладки, что является хорошей практикой.
    - Присутствуют docstring, но их необходимо доработать.
    - Код использует `execute_locator` для взаимодействия с веб-элементами, что является хорошей абстракцией.
- Минусы
    - Использование `eval` для вычисления цены может быть опасным и должно быть пересмотрено.
    - Много `...` в коде, что указывает на незавершенность функционала.
    - Присутствуют неиспользуемые импорты.
    - Отсутствует полноценная документация в формате reStructuredText.
    - Не всегда используется `j_loads` или `j_loads_ns`.
    - Использование `try-except` без конкретизации исключений может скрыть важные ошибки.
    - Необходимо унифицировать использование кавычек (`'` вместо `"`).

**Рекомендации по улучшению**

1.  **Документация**:
    *   Дополнить docstring для модуля, классов и функций в формате reStructuredText.
    *   Уточнить описания аргументов и возвращаемых значений.

2.  **Импорты**:
    *   Удалить неиспользуемые импорты.
    *   Использовать `from src.utils.jjson import j_loads, j_loads_ns` для загрузки JSON.

3.  **Обработка цен**:
    *   Заменить `eval` на более безопасный способ вычисления цены (например, с использованием `decimal` или `float`).

4.  **Логирование**:
    *   В `try-except` блоках конкретизировать типы исключений, которые обрабатываются.
    *   Использовать `logger.error` с конкретным сообщением об ошибке и передавать исключение для трассировки.

5.  **Рефакторинг**:
    *   Удалить все `...` в коде и реализовать необходимый функционал.
    *   Унифицировать использование кавычек (использовать одинарные кавычки).
    *   Упростить логику работы с модальными окнами, избегая дублирования кода.
    *   Добавить проверки на типы данных в местах, где это необходимо.

6.  **Комментарии**:
    *   Переписать все комментарии в формате RST.

7.  **Улучшения**:
    *   Перенести логику установки доставки в комбинации.
    *   Реализовать функции `set_qty`, `set_customer_reviews`, `set_rewritted_URL`.
    *   Оптимизировать код для повышения производительности.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиком Morlevi.
=========================================================================================

Этот модуль содержит функции для аутентификации, сбора данных о товарах
и их категориях с сайта поставщика Morlevi.

.. module:: src.suppliers.ivory.__morlevi__
   :platform: Windows, Unix
   :synopsis: Модуль для работы с поставщиком Morlevi.

.. codeauthor:: [Name] [Last Name]
   :date: 07.11.2023
"""
from pathlib import Path
import requests
import pandas as pd
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from src.settings import StringFormatter
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
from src.suppliers.Product import Product
import settings

MODE = 'dev'


def login(supplier):
    """
    Выполняет вход на сайт поставщика.

    :param supplier: Объект поставщика.
    :type supplier: src.suppliers.Supplier
    :return: True, если вход выполнен успешно, иначе None.
    :rtype: bool or None
    """
    _s = supplier
    _d = _s.driver
    _d.get_url('https://www.morlevi.co.il')
    if _login(_s):
        return True
    else:
        try:
            """
            Закрытие модальных окон сайта.
            """
            logger.error('Ошибка, пытаюсь закрыть popup')
            _d.page_refresh()
            if _login(_s):
                return True

            close_pop_up_locator = _s.locators['login']['close_pop_up_locator']
            close_pop_up_btn = _d.execute_locator(close_pop_up_locator)
            _d.wait(5)

            if isinstance(close_pop_up_btn, list):  # Если появилось несколько
                for b in close_pop_up_btn:
                    try:
                        b.click()
                        if _login(_s):
                            return True
                    except Exception:
                        logger.error('Не удалось закрыть модальное окно', exc_info=True)
            elif isinstance(close_pop_up_btn, WebElement):  # нашелся только один элемент
                close_pop_up_btn.click()
                return _login(_s)
        except Exception as ex:
            logger.error(f'Не удалось залогиниться', exc_info=True)
            return

def _login(_s):
    """
    Выполняет фактический вход на сайт поставщика.

    :param _s: Объект поставщика.
    :type _s: src.suppliers.Supplier
    :return: True, если вход выполнен успешно, иначе None.
    :rtype: bool or None
    """
    logger.debug('Собссно, логин Морлеви')
    _s.driver.refresh()
    _d = _s.driver
    _l: dict = _s.locators['login']
    try:
        _d.execute_locator(_l['open_login_dialog_locator'])
        _d.wait(1.3)
        _d.execute_locator(_l['email_locator'])
        _d.wait(0.7)
        _d.execute_locator(_l['password_locator'])
        _d.wait(0.7)
        _d.execute_locator(_l['loginbutton_locator'])
        logger.debug('Mor logged in')
        return True
    except Exception as ex:
        logger.error(f'LOGIN ERROR', exc_info=True)
        return


def grab_product_page(s):
    """
    Собирает информацию о товаре со страницы.

    :param s: Объект поставщика.
    :type s: src.suppliers.Supplier
    :return: Объект товара с заполненными полями.
    :rtype: src.suppliers.Product.Product
    """
    p = Product(supplier=s)
    _l: dict = s.locators['product']
    _d = s.driver
    _field = p.fields
    _s = s

    """
     Морлеви может выкинуть модальное окно.
    """
    try:
        _d.click(s.locators['close_pop_up_locator'])
    except Exception:
        logger.error('Не удалось закрыть модальное окно при сборе товара', exc_info=True)

    def set_id():
        """Устанавливает ID товара."""
        _id = _d.execute_locator(_l['sku_locator'])
        if isinstance(_id, list):
            _field['id'] = _id[0]
            _field['Rewritten URL'] = str(_id[1]).replace(' ', '-')

    def set_sku_suppl():
        """Устанавливает артикул поставщика."""
        _field['sku suppl'] = _field['id']

    def set_sku_prod():
        """Устанавливает артикул товара."""
        _field['sku'] = 'mlv-' + _field['id']

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
            except Exception as ex:
                logger.error(f'Не удалось вычислить цену: {_price}', exc_info=True)
                return
        else:
           logger.error(f'Не найдена цена для товара', exc_info=True)
           return False
        return True

    def set_before_tax_price():
        """Устанавливает цену без налога."""
        _field['price tax excluded'] = _field['cost price']
        return True

    def set_delivery():
        """Устанавливает информацию о доставке."""
        """TODO  перенести в комбинации """
        # product_delivery_list = _d.execute_locator(_l['product_delivery_locator'])
        # for i in product_delivery_list:
        #    ...
        ...

    def set_images(via_ftp=False):
        """Устанавливает URL изображения товара."""
        # _http_server = f'http://davidka.esy.es/supplier_imgs/{_s.supplier_prefix}'
        # _img_name = f'{_field['sku']}.png'
        # _field['img url'] = f'{_http_server}/{_img_name}'
        # screenshot = _d.execute_locator(_l['main_image_locator'])
        # _s.save_and_send_via_ftp({_img_name: screenshot})
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
        """Устанавливает переписанный URL товара."""
        # _field['Rewritten URL'] = StringFormatter.set_rewritted_URL(_field['title'])
        ...
    set_id()
    set_sku_suppl()
    set_sku_prod()
    set_title()
    set_cost_price()
    set_before_tax_price()
    set_delivery()
    set_images()
    set_combinations()
    # set_qty()
    # set_byer_protection()
    set_description()
    set_summary()
    # set_specification()
    # set_customer_reviews()
    set_supplier()
    set_rewritted_URL()

    return p
    ...

def list_products_in_category_from_pagination(supplier):
    """
    Собирает список ссылок на товары из категории с пагинацией.

    :param supplier: Объект поставщика.
    :type supplier: src.suppliers.Supplier
    :return: Список ссылок на товары.
    :rtype: list
    """
    _s = supplier
    _d = _s.driver
    _l = _s.locators['product']['link_to_product_locator']

    list_products_in_category: list = []
    _product_list_from_page = _d.execute_locator(_l)
    """
     Может вернуться или список адресов, или строка, или None.
     Если нет товаров на странице в данный момент.
    """
    if not _product_list_from_page:
        """
         Нет смысла продолжать. Нет товаров в категории.
         Возвращаю пустой список.
        """
        return list_products_in_category

    if isinstance(_product_list_from_page, list):
        list_products_in_category.extend(_product_list_from_page)
    else:
        list_products_in_category.append(_product_list_from_page)

    pages = _d.execute_locator(_s.locators['pagination']['a'])
    if isinstance(pages, list):
        for page in pages:
            _product_list_from_page = _d.execute_locator(_l)
            """
             Может вернуться или список адресов, или строка.
            """
            if isinstance(_product_list_from_page, list):
                list_products_in_category.extend(_product_list_from_page)
            else:
                list_products_in_category.append(_product_list_from_page)
            _perv_url = _d.current_url
            page.click()
            """
             Дошел до конца листалки
            """
            if _perv_url == _d.current_url:
                break

    if isinstance(list_products_in_category, list):
        list_products_in_category = list(set(list_products_in_category))
    return list_products_in_category


def get_list_products_in_category(s, scenario, presath):
    """
    Собирает список товаров в категории.

    :param s: Объект поставщика.
    :type s: src.suppliers.Supplier
    :param scenario: JSON данные для сценария.
    :type scenario: dict
    :param presath: Объект PrestaShopWebServiceDict.
    :type presath: src.prestashop.PrestaShopWebServiceDict
    """
    l = list_products_in_category_from_pagination(s)
    ...


def get_list_categories_from_site(s, scenario_file, brand=''):
    """
    Собирает список категорий с сайта.

    :param s: Объект поставщика.
    :type s: src.suppliers.Supplier
    :param scenario_file: Путь к файлу сценария.
    :type scenario_file: str
    :param brand: Название бренда.
    :type brand: str
    """
    ...
```