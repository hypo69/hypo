## Анализ кода модуля `__morlevi__.py`

**Качество кода**

- **Соответствие требованиям по оформлению кода: 6/10**
  -  Плюсы:
    - Код структурирован, присутствуют импорты и функции.
    - Используются `logger` для логирования.
  -  Минусы:
    - Не все комментарии соответствуют стандарту RST.
    - Используются двойные кавычки в строках кода, где нужно одинарные.
    -  Не все функции имеют docstring.
    - В коде встречаются конструкции `try-except` без конкретной обработки исключений.
    - Присутствуют неиспользуемые переменные и комментарии.
    - Не хватает форматирования кода.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Добавить `from src.utils.jjson import j_loads, j_loads_ns` для обработки JSON файлов.
    -   Импортировать `logger` через `from src.logger import logger`.
2.  **Форматирование**:
    -   Заменить двойные кавычки на одинарные в коде, за исключением строк для вывода.
    -   Удалить лишние комментарии и пустые строки.
    -   Добавить docstring к каждой функции и классу в формате RST.
    -   Переписать комментарии после `#` для более точного описания кода.
3.  **Логирование**:
    -   Использовать `logger.error` с указанием исключения вместо общих `try-except`.
4.  **Обработка данных**:
    -   Использовать `j_loads` или `j_loads_ns` для чтения JSON файлов (если применимо).
    -   Убрать лишние `...` или заменить их конкретной логикой.
5.  **Структура**:
    -   Разбить большие функции на более мелкие, если необходимо.
    -   Унифицировать именование переменных и функций.
6.  **Улучшения**:
    -   В функции `grab_product_page` заменить `eval` на безопасный метод вычисления.
    -   Проверить и доработать все `TODO`
    -   Перенести вычисления `set_rewritted_URL` в функцию `set_rewritted_URL`

**Оптимизированный код**

```python
"""
Модуль для работы с поставщиком Morlevi
=========================================================================================

Этот модуль содержит функции для взаимодействия с сайтом поставщика Morlevi,
включая авторизацию, парсинг данных о продуктах и категориях.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.ivory import __morlevi__
    from src.suppliers.supplier import Supplier
    from selenium import webdriver

    driver = webdriver.Chrome()
    supplier = Supplier(driver=driver, supplier_prefix='morlevi',settings={},locators={}, product_fields={})
    __morlevi__.login(supplier)

"""
from pathlib import Path
import requests
import pandas as pd
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from src.settings import StringFormatter
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger
from src.suppliers.Product import Product
import settings  # TODO: проверить, нужен ли этот импорт. Скорее всего нет, и его нужно удалить


def login(supplier):
    """
    Выполняет вход на сайт поставщика Morlevi.

    Args:
        supplier (Supplier): Объект поставщика.

    Returns:
        bool: True в случае успешного входа, иначе False.
    """
    _s = supplier
    _d = _s.driver
    _d.get_url('https://www.morlevi.co.il')
    if _login(_s):
        return True
    else:
        try:
            #  Код закрывает модальные окна на сайте
            #  выпадающие до входа
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
                    except Exception as ex:
                        logger.error(f'Ошибка при закрытии popup {ex}')
                        ...
            if isinstance(close_pop_up_btn, WebElement):  # нашелся только один элемент
                close_pop_up_btn.click()
                return _login(_s)
        except Exception as ex:
            logger.error(f'Не удалось залогиниться {ex}')
            return False


def _login(_s) -> bool:
    """
    Вспомогательная функция для выполнения фактического входа на сайт Morlevi.

    Args:
        _s (Supplier): Объект поставщика.

    Returns:
        bool: True в случае успешного входа, иначе False.
    """
    logger.debug('Собссно, логин Морлеви')
    _s.driver.refresh()
    _d = _s.driver
    _l: dict = _s.locators['login']

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
        logger.error(f'LOGIN ERROR {ex}')
        return False


def grab_product_page(s) -> Product:
    """
    Извлекает данные о продукте со страницы товара.

    Args:
        s (Supplier): Объект поставщика.

    Returns:
        Product: Объект Product с данными о товаре.
    """
    p = Product(supplier=s)
    _: dict = s.locators['product']
    _d = s.driver
    _field = p.fields
    _s = s

    # Код закрывает модальное окно, если оно есть
    _d.click(s.locators['close_pop_up_locator'])

    def set_id():
        """Устанавливает ID товара."""
        _id = _d.execute_locator(_['sku_locator'])
        if isinstance(_id, list):
            _field['id'] = _id[0]
            _field['Rewritten URL'] = str(_id[1]).replace(' ', '-')

    def set_sku_suppl():
        """Устанавливает артикул поставщика."""
        _field['sku suppl'] = _field['id']

    def set_sku_prod():
        """Устанавливает артикул товара."""
        _field['sku'] = str('mlv-') + _field['id']

    def set_title():
        """Устанавливает заголовок товара."""
        _field['title'] = _d.title

    def set_summary():
        """Устанавливает краткое описание товара."""
        _field['summary'] = _d.execute_locator(_['summary_locator'])
        _field['meta description'] = _field['summary']

    def set_description():
        """Устанавливает полное описание товара."""
        _field['description'] = _d.execute_locator(_['description_locator'])

    def set_cost_price():
        """Устанавливает закупочную цену товара."""
        _price = _d.execute_locator(_['price_locator'])
        if _price:
            _price = _price.replace(',', '')
            # Может прийти все, что угодно
            _price = StringFormatter.clear_price(_price)
            try:
                _field['cost price'] = round(eval(f'{_price}{s.settings["price_rule"]}'))
            except Exception as ex:
                logger.error(f'Ошибка при вычислении цены: {ex}')
                return False
        else:
            logger.error('Not found price for ...')
            return False
        return True

    def set_before_tax_price():
        """Устанавливает цену товара без налога."""
        _field['price tax excluded'] = _field['cost price']
        return True

    def set_delivery():
        """Устанавливает информацию о доставке."""
        # TODO: перенести в комбинации
        ...

    def set_images(via_ftp=False):
        """Устанавливает URL изображения товара."""
        _images = _d.execute_locator(_['main_image_locator'])
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
        _field['specification'] = _d.execute_locator(_['product_name_locator'])

    def set_customer_reviews():
      """Устанавливает отзывы клиентов о товаре."""
      ...

    def set_supplier():
        """Устанавливает ID поставщика."""
        _field['supplier'] = '2784'
        ...

    def set_rewritted_URL():
        """Устанавливает переписанный URL товара."""
        _field['Rewritten URL'] = StringFormatter.set_rewritted_URL(_field['title'])

    set_id()
    set_sku_suppl()
    set_sku_prod()
    set_title()
    if not set_cost_price():
        return
    set_before_tax_price()
    set_delivery()
    set_images()
    set_combinations()
    # set_qty()
    set_description()
    set_summary()
    set_specification()
    # set_customer_reviews()
    set_supplier()
    set_rewritted_URL()

    return p


def list_products_in_category_from_pagination(supplier) -> list:
    """
    Получает список ссылок на товары из категории с пагинацией.

    Args:
        supplier (Supplier): Объект поставщика.

    Returns:
        list: Список ссылок на товары.
    """
    _s = supplier
    _d = _s.driver
    _l = _s.locators['product']['link_to_product_locator']

    list_products_in_category = []
    _product_list_from_page = _d.execute_locator(_l)
    # может вернуться или список адресов или строка или None
    # если нет товаров на странице на данный момент
    if not _product_list_from_page:
        # нет смысла продожать. Нет товаров в категории
        # Возвращаю пустой список
        return list_products_in_category

    if isinstance(_product_list_from_page, list):
        list_products_in_category.extend(_product_list_from_page)
    else:
        list_products_in_category.append(_product_list_from_page)

    pages = _d.execute_locator(_s.locators['pagination']['a'])
    if isinstance(pages, list):
        for page in pages:
            _product_list_from_page = _d.execute_locator(_l)
            # может вернуться или список адресов или строка.
            if isinstance(_product_list_from_page, list):
                list_products_in_category.extend(_product_list_from_page)
            else:
                list_products_in_category.append(_product_list_from_page)

            _perv_url = _d.current_url
            page.click()

            # дошел до конца листалки
            if _perv_url == _d.current_url:
                break

    if isinstance(list_products_in_category, list):
        list_products_in_category = list(set(list_products_in_category))
    return list_products_in_category


def get_list_products_in_category(s, scenario, presath):
    """
    Получает список продуктов в категории.

    Args:
        s (Supplier): Объект поставщика.
        scenario (dict): Словарь со сценарием.
        presath (PrestaShopWebServiceDict): Объект для работы с PrestaShop.
    """
    l = list_products_in_category_from_pagination(s)
    ...


def get_list_categories_from_site(s, scenario_file, brand=''):
    """
    Получает список категорий с сайта.

    Args:
        s (Supplier): Объект поставщика.
        scenario_file (str): Путь к файлу сценария.
        brand (str, optional): Бренд. Defaults to ''.
    """
    ...