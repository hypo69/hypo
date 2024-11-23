## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers 
	:platform: Windows, Unix
	:synopsis:  Базовый класс сбора данных со старницы для всех поставщиков. 
Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = `suppler_prefix`
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json`)

class G(Graber):

    @close_pop_up()
    async def name(self, value: Any = None):
        self.fields.name = <Ваша реализация>
        )
    ```

"""
MODE = 'development'


import os
import sys
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable
from langdetect import detect
from functools import wraps

import header
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import PrestaShop

# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: Driver
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    # Атрибуты класса
    driver: Driver = None
    locator: SimpleNamespace = None
    supplier_prefix: str = None


# Определение декоратора для закрытия всплывающих окон
# В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# Общее название декоратора `@close_pop_up` можно изменить 
# Если декоратор не используется в поставщике - надо закомментировать строку
# ```await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close``` 
def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator.close_pop_up:
                try:
                    await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                    ... 
                except ExecuteLocatorException as e:
                    logger.debug(f'Ошибка выполнения локатора: {e}')
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator


def check_value(func):
    """Декоратор для проверки аргумента `value` перед выполнением функции."""
    async def wrapper(self, value: Any = None, *args, **kwargs):
        if not value:
            logger.debug(f"Нет аргумента {value=}")
            return
        return await func(self, value, *args, **kwargs)
    return wrapper

class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""
    
    def __init__(self, supplier_prefix: str, driver:Driver):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locator (Locator): Экземпляр класса Locator.
            driver (Driver): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        self.locator:SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.l = self.locator
        self.driver:Driver = driver
        self.d = self.driver
        self.fields:ProductFields = ProductFields()
        Context.driver = self.driver
        Context.locator = SimpleNamespace(
            close_pop_up= None  # Пример задания локатора
        )
        Context.supplier_prefix =  supplier_prefix

    async def error(self, field: str):
        """Обработчик ошибок для полей."""
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.

        Args:
            value (Any): Значение для установки.
            locator_func (Callable[[], Any]): Функция для получения значения из локатора.
            field_name (str): Название поля.
            default (Any): Значение по умолчанию. По умолчанию пустая строка.

        Returns:
            Any: Установленное значение.
        """
        locator_result = await asyncio.to_thread(locator_func)
        if value:
            return value
        if locator_result:
            return locator_result
        await self.error(field_name)
        return default

    async def grab_page(self) -> ProductFields:
        """Асинхронная функция для сбора полей продукта.

        Returns:
            ProductFields: Собранные поля продукта.
        """
        async def fetch_all_data(**kwargs):
            # Вызов функции для получения конкретных данных
            # await self.fetch_specific_data(**kwargs)  # Убедитесь, что эта функция реализована

            # Uncomment the following lines to fetch specific data
            await self.id_product(kwards.get("id_product", ''))
            # await self.additional_shipping_cost(kwards.get("additional_shipping_cost", ''))
            # await self.delivery_in_stock(kwards.get("delivery_in_stock", ''))
            # await self.active(kwards.get("active", ''))
            # await self.additional_delivery_times(kwards.get("additional_delivery_times", ''))
            # await self.advanced_stock_management(kwards.get("advanced_stock_management", ''))
            # await self.affiliate_short_link(kwards.get("affiliate_short_link", ''))
            # await self.affiliate_summary(kwards.get("affiliate_summary", ''))
            # await self.affiliate_summary_2(kwards.get("affiliate_summary_2", ''))
            # await self.affiliate_text(kwards.get("affiliate_text", ''))
            # await self.affiliate_image_large(kwards.get("affiliate_image_large", ''))
            # await self.affiliate_image_medium(kwards.get("affiliate_image_medium", ''))
            # await self.affiliate_image_small(kwards.get("affiliate_image_small", ''))
            # await self.available_date(kwards.get("available_date", ''))
            # await self.available_for_order(kwards.get("available_for_order", ''))
            # await self.available_later(kwards.get("available_later", ''))
            # await self.available_now(kwards.get("available_now", ''))
            # await self.cache_default_attribute(kwards.get("cache_default_attribute", ''))
            # await self.cache_has_attachments(kwards.get("cache_has_attachments", ''))
            # await self.cache_is_pack(kwards.get("cache_is_pack", ''))
            # await self.condition(kwards.get("condition", ''))
            # await self.customizable(kwards.get("customizable", ''))
            # await self.date_add(kwards.get("date_add", ''))
            # await self.date_upd(kwards.get("date_upd", ''))
            # await self.default_image_url(kwards.get("default_image_url", ''))
            # await self.delivery_in_stock(kwards.get("delivery_in_stock", ''))
            # await self.delivery_out_stock(kwards.get("delivery_out_stock", ''))
            # await self.depth(kwards.get("depth", ''))
            # await self.description(kwards.get("description", ''))
            await self.description_short(kwards.get("description_short", ''))
            # await self.ean13(kwards.get("ean13", ''))
            # await self.ecotax(kwards.get("ecotax", ''))
            # await self.height(kwards.get("height", ''))
            # await self.how_to_use(kwards.get("how_to_use", ''))
            # await self.id_category_default(kwards.get("id_category_default", ''))
            # await self.additional_categories(f.id_category_default, s.current_scenario['presta_categories']['additional_categories'])
            # await self.id_default_combination(kwards.get("id_default_combination", ''))
            # await self.id_default_image(kwards.get("id_default_image", ''))
            # await self.id_manufacturer(kwards.get("id_manufacturer", ''))
            # await self.id_supplier(kwards.get("id_supplier", ''))
            # await self.id_tax(kwards.get("id_tax", ''))
            # await self.id_type_redirected(kwards.get("id_type_redirected", ''))
            # await self.images_urls(kwards.get("images_urls", ''))
            # await self.indexed(kwards.get("indexed", ''))
            # await self.ingredients(kwards.get("ingredients", ''))
            # await self.meta_description(kwards.get("meta_description", ''))
            # await self.meta_keywords(kwards.get("meta_keywords", ''))
            # await self.meta_title(kwards.get("meta_title", ''))
            # await self.is_virtual(kwards.get("is_virtual", ''))
            # await self.isbn(kwards.get("isbn", ''))
            await self.name(kwards.get("name", ''))
            # await self.link_rewrite(kwards.get("link_rewrite", ''))
            # await self.location(kwards.get("location", ''))
            # await self.low_stock_alert(kwards.get("low_stock_alert", ''))
            # await self.low_stock_threshold(kwards.get("low_stock_threshold", ''))
            # await self.minimal_quantity(kwards.get("minimal_quantity", ''))
            # await self.mpn(kwards.get("mpn", ''))
            # await self.online_only(kwards.get("online_only", ''))
            # await self.on_sale(kwards.get("on_sale", ''))
            # await self.out_of_stock(kwards.get("out_of_stock", ''))
            # await self.pack_stock_type(kwards.get("pack_stock_type", ''))
            # await self.locale(kwards.get("locale", ''))        
            # await self.price(kwards.get("price", ''))
            # await self.product_type(kwards.get("product_type", ''))
            # await self.quantity_discount(kwards.get("quantity_discount", ''))
            # await self.redirect_type(kwards.get("redirect_type", ''))
            # await self.reference(kwards.get("reference", ''))
            # await self.show_condition(kwards.get("show_condition", ''))
            # await self.show_price(kwards.get("show_price", ''))
            await self.specification(kwards.get("specification", ''))
            # await self.state(kwards.get("state", ''))
            # await self.text_fields(kwards.get("text_fields", ''))
            # await self.unit_price_ratio(kwards.get("unit_price_ratio", ''))
            # await self.unity(kwards.get("unity", ''))
            # await self.upc(kwards.get("upc", ''))
            # await self.uploadable_files(kwards.get("uploadable_files", ''))
            # await self.visibility(kwards.get("visibility", ''))
            # await self.weight(kwards.get("weight", ''))
            # await self.wholesale_price(kwards.get("wholesale_price", ''))
            # await self.width(kwards.get("width", ''))
            await self.local_saved_image(kwards.get("local_saved_image", ''))
            # await self.local_saved_video(kwards.get("local_saved_video", ''))

        # Call the function to fetch all data
        await fetch_all_data()
        return self.fields

    def error(self, field: str):
        """Error handler for fields."""
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self, 
        value: Any, 
        locator_func: Callable[[], Any], 
        field_name: str, 
        default: Any = ''
    ) -> Any:
        """Universal function for setting field values with error handling."""
        if value:
            return value
        result = await locator_func()  # Ожидаем выполнение корутины
        return result if result else self.error(field_name) or default




    @close_pop_up()
    async def additional_shipping_cost(self, value: Any = None):
        """Fetch and set additional shipping cost.
        Args:
        value (Any): это значение можно передать в словаре kwards чеез ключ {additional_shipping_cost = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.additional_shipping_cost
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.additional_shipping_cost) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.additional_shipping_cost}")
            return

        # Записываем результат в поле `additional_shipping_cost` объекта `ProductFields`
        self.fields.additional_shipping_cost = value
    @close_pop_up()
    async def delivery_in_stock(self, value: Any = None):
        """Fetch and set delivery in stock status.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {delivery_in_stock = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.delivery_in_stock`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.delivery_in_stock) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.delivery_in_stock = await self.set_field_value(
            value, 
            lambda: locator_result,
            'delivery_in_stock'
        )


    @close_pop_up()
    async def active(self, value: Any = None):
        """Fetch and set active status.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {active = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.active`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.active) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.active = await self.set_field_value(
            value, 
            lambda: locator_result,
            'active'
        )


    @close_pop_up()
    async def additional_delivery_times(self, value: Any = None):
        """Fetch and set additional delivery times.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {additional_delivery_times = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.additional_delivery_times`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.additional_delivery_times) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.additional_delivery_times = await self.set_field_value(
            value, 
            lambda: locator_result,
            'additional_delivery_times'
        )


    @close_pop_up()
    async def advanced_stock_management(self, value: Any = None):
        """Fetch and set advanced stock management status.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {advanced_stock_management = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.advanced_stock_management`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.advanced_stock_management) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.advanced_stock_management = await self.set_field_value(
            value, 
            lambda: locator_result,
            'advanced_stock_management'
        )


    @close_pop_up()
    async def affiliate_short_link(self, value: Any = None):
        """Fetch and set affiliate short link.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_short_link = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_short_link`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_short_link) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_short_link = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_short_link'
        )


    @close_pop_up()
    async def affiliate_summary(self, value: Any = None):
        """Fetch and set affiliate summary.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_summary = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_summary`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_summary) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_summary = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_summary'
        )
    @close_pop_up()
    async def affiliate_summary_2(self, value: Any = None):
        """Fetch and set affiliate summary 2.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_summary_2 = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_summary_2`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_summary_2) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_summary_2 = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_summary_2'
        )


    @close_pop_up()
    async def affiliate_text(self, value: Any = None):
        """Fetch and set affiliate text.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_text = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_text`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_text) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_text = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_text'
        )


    @close_pop_up()
    async def affiliate_image_large(self, value: Any = None):
        """Fetch and set affiliate large image.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_image_large = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_image_large`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_image_large) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_image_large = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_image_large'
        )


    @close_pop_up()
    async def affiliate_image_medium(self, value: Any = None):
        """Fetch and set affiliate medium image.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_image_medium = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_image_medium`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_image_medium) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_image_medium = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_image_medium'
        )


    @close_pop_up()
    async def affiliate_image_small(self, value: Any = None):
        """Fetch and set affiliate small image.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {affiliate_image_small = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.affiliate_image_small`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.affiliate_image_small) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.affiliate_image_small = await self.set_field_value(
            value, 
            lambda: locator_result,
            'affiliate_image_small'
        )


    @close_pop_up()
    async def available_date(self, value: Any = None):
        """Fetch and set available date.
    
        Args:
        value (Any): это значение можно передать в словаре kwards через ключ {available_date = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.available_date`
        """
    
        # Получаем значение через execute_locator
        locator_result = await self.d.execute_locator(self.l.available_date) or ''
    
        # Проверяем валидность результата
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле объекта
        self.fields.available_date = await self.set_field_value(
            value, 
            lambda: locator_result,
            'available_date'
        )

    @close_pop_up()
    async def available_for_order(self, value: Any = None):
        """Fetch and set available for order status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.available_for_order`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.available_for_order) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.available_for_order}")
            return

        # Записываем результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value


    @close_pop_up()
    async def available_later(self, value: Any = None):
        """Fetch and set available later status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.available_later`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.available_later) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.available_later}")
            return

        # Записываем результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value


    @close_pop_up()
    async def available_now(self, value: Any = None):
        """Fetch and set available now status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.available_now`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.available_now) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.available_now}")
            return

        # Записываем результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value


    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """Set additional categories.

        Это значение можно передать в словаре kwargs через ключ {additional_categories = `value`} при определении класса.
        Если `value` было передано, оно подставляется в поле `ProductFields.additional_categories`.

        Args:
        value (str | list, optional): Строка или список категорий. Если не передано, используется пустое значение.
    
        Returns:
        dict: Словарь с ID категорий.
        """

        self.fields.additional_categories = value if value else ''


    @close_pop_up()
    async def cache_default_attribute(self, value: Any = None):
        """Fetch and set cache default attribute.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.cache_default_attribute`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.cache_default_attribute) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.cache_default_attribute}")
            return

        # Записываем результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value


    @close_pop_up()
    async def cache_has_attachments(self, value: Any = None):
        """Fetch and set cache has attachments status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.cache_has_attachments`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.cache_has_attachments) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.cache_has_attachments}")
            return

        # Записываем результат в поле `cache_has_attachments` объекта `ProductFields`
        self.fields.cache_has_attachments = value


    @close_pop_up()
    async def cache_is_pack(self, value: Any = None):
        """Fetch and set cache is pack status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {cache_is_pack = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.cache_is_pack`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.cache_is_pack) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.cache_is_pack}")
            return

        # Записываем результат в поле `cache_is_pack` объекта `ProductFields`
        self.fields.cache_is_pack = value


    @close_pop_up()
    async def condition(self, value: Any = None):
        """Fetch and set product condition.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {condition = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.condition`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.condition) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.condition}")
            return

        # Записываем результат в поле `condition` объекта `ProductFields`
        self.fields.condition = value


    @close_pop_up()
    async def customizable(self, value: Any = None):
        """Fetch and set customizable status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {customizable = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.customizable`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.customizable) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.customizable}")
            return

        # Записываем результат в поле `customizable` объекта `ProductFields`
        self.fields.customizable = value


    @close_pop_up()
    async def date_add(self, value: Any = None):
        """Fetch and set date added.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {date_add = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.date_add`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.date_add) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.date_add}")
            return

        # Записываем результат в поле `date_add` объекта `ProductFields`
        self.fields.date_add = value


    @close_pop_up()
    async def date_upd(self, value: Any = None):
        """Fetch and set date updated.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {date_upd = `value`} при определении класса.
        если `value` был передан - его значение подставляется в поле `ProductFields.date_upd`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.date_upd) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.date_upd}")
            return

        # Записываем результат в поле `date_upd` объекта `ProductFields`
        self.fields.date_upd = value
    @close_pop_up()
    async def delivery_out_stock(self, value: Any = None):
        """Fetch and set delivery out of stock.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {delivery_out_stock = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.delivery_out_stock`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.delivery_out_stock) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.delivery_out_stock}")
            return

        # Записываем результат в поле `delivery_out_stock` объекта `ProductFields`
        self.fields.delivery_out_stock = value


    @close_pop_up()
    async def depth(self, value: Any = None):
        """Fetch and set depth.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {depth = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.depth`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.depth) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.depth}")
            return

        # Записываем результат в поле `depth` объекта `ProductFields`
        self.fields.depth = value


    @close_pop_up()
    async def description(self, value: Any = None):
        """Fetch and set description.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {description = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.description`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.description) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.description}")
            return

        # Записываем результат в поле `description` объекта `ProductFields`
        self.fields.description = value


    @close_pop_up()
    async def description_short(self, value: Any = None):
        """Fetch and set short description.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {description_short = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.description_short`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.description_short) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.description_short}")
            return

        # Записываем результат в поле `description_short` объекта `ProductFields`
        self.fields.description_short = value


    @close_pop_up()
    async def id_category_default(self, value: Any = None):
        """Fetch and set default category ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_category_default = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_category_default`.
        """

        # Записываем значение в поле `id_category_default` объекта `ProductFields`
        self.fields.id_category_default = value


    @close_pop_up()
    async def id_default_combination(self, value: Any = None):
        """Fetch and set default combination ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_default_combination = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_default_combination`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_default_combination) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_default_combination}")
            return

        # Записываем результат в поле `id_default_combination` объекта `ProductFields`
        self.fields.id_default_combination = value


    @close_pop_up()
    async def id_product(self, value: Any = None):
        """Fetch and set product ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_product = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_product`.
        """

        # Получаем значение id_supplier, если оно не передано
        self.fields.id_supplier = self.fields.id_supplier or await self.d.execute_locator(self.l.id_supplier)
    
        # Формируем id_product с учетом supplier_prefix
        self.fields.id_product = f"{self.supplier_prefix}{f'-{self.fields.id_supplier}' if self.fields.id_supplier else ''}-{value}"


    @close_pop_up()
    async def locale(self, value: Any = None):
        """Fetch and set locale.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {locale = `value`} при определении класса.
        Если `value` не было передано, оно определяется автоматически.
        """

        # Если value не передано, определяем locale автоматически
        i18n = value or d.locale
        if not i18n and self.fields.name['language'][0]['value']:
            text = self.fields.name['language'][0]['value']
            i18n = detect(text)
    
        # Записываем результат в поле `locale` объекта `ProductFields`
        self.fields.locale = i18n


    @close_pop_up()
    async def id_default_image(self, value: Any = None):
        """Fetch and set default image ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_default_image = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_default_image`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_default_image) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_default_image}")
            return

        # Записываем результат в поле `id_default_image` объекта `ProductFields`
        self.fields.id_default_image = value


    @close_pop_up()
    async def ean13(self, value: Any = None):
        """Fetch and set EAN13 code.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {ean13 = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.ean13`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.ean13) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.ean13}")
            return

        # Записываем результат в поле `ean13` объекта `ProductFields`
        self.fields.ean13 = value


    @close_pop_up()
    async def ecotax(self, value: Any = None):
        """Fetch and set ecotax.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {ecotax = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.ecotax`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.ecotax) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.ecotax}")
            return

        # Записываем результат в поле `ecotax` объекта `ProductFields`
        self.fields.ecotax = value


    @close_pop_up()
    async def height(self, value: Any = None):
        """Fetch and set height.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {height = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.height`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.height) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.height}")
            return

        # Записываем результат в поле `height` объекта `ProductFields`
        self.fields.height = value


    @close_pop_up()
    async def how_to_use(self, value: Any = None):
        """Fetch and set how to use.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {how_to_use = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.how_to_use`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.how_to_use) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.how_to_use}")
            return

        # Записываем результат в поле `how_to_use` объекта `ProductFields`
        self.fields.how_to_use = value

    @close_pop_up()
    async def id_manufacturer(self, value: Any = None):
        """Fetch and set manufacturer ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_manufacturer = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_manufacturer`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_manufacturer) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_manufacturer}")
            return

        # Записываем результат в поле `id_manufacturer` объекта `ProductFields`
        self.fields.id_manufacturer = value


    @close_pop_up()
    async def id_supplier(self, value: Any = None):
        """Fetch and set supplier ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_supplier = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_supplier`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_supplier) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_supplier}")
            return

        # Записываем результат в поле `id_supplier` объекта `ProductFields`
        self.fields.id_supplier = value


    @close_pop_up()
    async def id_tax(self, value: Any = None):
        """Fetch and set tax ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_tax = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_tax`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_tax) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_tax}")
            return

        # Записываем результат в поле `id_tax` объекта `ProductFields`
        self.fields.id_tax = value


    @close_pop_up()
    async def id_type_redirected(self, value: Any = None):
        """Fetch and set redirected type ID.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {id_type_redirected = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.id_type_redirected`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.id_type_redirected) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.id_type_redirected}")
            return

        # Записываем результат в поле `id_type_redirected` объекта `ProductFields`
        self.fields.id_type_redirected = value


    @close_pop_up()
    async def images_urls(self, value: Any = None):
        """Fetch and set image URLs.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {images_urls = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.images_urls`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.images_urls) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.images_urls}")
            return

        # Записываем результат в поле `images_urls` объекта `ProductFields`
        self.fields.images_urls = value


    @close_pop_up()
    async def indexed(self, value: Any = None):
        """Fetch and set indexed status.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {indexed = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.indexed`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.indexed) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.indexed}")
            return

        # Записываем результат в поле `indexed` объекта `ProductFields`
        self.fields.indexed = value


    @close_pop_up()
    async def ingredients(self, value: Any = None):
        """Fetch and set ingredients.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {ingredients = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.ingredients`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.ingredients) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.ingredients}")
            return

        # Записываем результат в поле `ingredients` объекта `ProductFields`
        self.fields.ingredients = value


    @close_pop_up()
    async def meta_description(self, value: Any = None):
        """Fetch and set meta description.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {meta_description = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.meta_description`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.meta_description) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.meta_description}")
            return

        # Записываем результат в поле `meta_description` объекта `ProductFields`
        self.fields.meta_description = value


    @close_pop_up()
    async def meta_keywords(self, value: Any = None):
        """Fetch and set meta keywords.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {meta_keywords = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.meta_keywords`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.meta_keywords) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.meta_keywords}")
            return

        # Записываем результат в поле `meta_keywords` объекта `ProductFields`
        self.fields.meta_keywords = value


    @close_pop_up()
    async def meta_title(self, value: Any = None):
        """Fetch and set meta title.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {meta_title = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.meta_title`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.meta_title) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.meta_title}")
            return

        # Записываем результат в поле `meta_title` объекта `ProductFields`
        self.fields.meta_title = value


    @close_pop_up()
    async def is_virtual(self, value: Any = None):
        """Fetch and set virtual status.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {is_virtual = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.is_virtual`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.is_virtual) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.is_virtual}")
            return

        # Записываем результат в поле `is_virtual` объекта `ProductFields`
        self.fields.is_virtual = value


    @close_pop_up()
    async def isbn(self, value: Any = None):
        """Fetch and set ISBN.
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {isbn = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.isbn`.
        """

        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.isbn) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.isbn}")
            return

        # Записываем результат в поле `isbn` объекта `ProductFields`
        self.fields.isbn = value
    @close_pop_up()
    async def link_rewrite(self, value: Any = None):
        """Fetch and set link rewrite.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {link_rewrite = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.link_rewrite`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.link_rewrite) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.link_rewrite}")
            return
    
        # Записываем результат в поле `link_rewrite` объекта `ProductFields`
        self.fields.link_rewrite = value


    @close_pop_up()
    async def location(self, value: Any = None):
        """Fetch and set location.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {location = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.location`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.location) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.location}")
            return
    
        # Записываем результат в поле `location` объекта `ProductFields`
        self.fields.location = value


    @close_pop_up()
    async def low_stock_alert(self, value: Any = None):
        """Fetch and set low stock alert.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {low_stock_alert = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.low_stock_alert`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.low_stock_alert) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.low_stock_alert}")
            return
    
        # Записываем результат в поле `low_stock_alert` объекта `ProductFields`
        self.fields.low_stock_alert = value


    @close_pop_up()
    async def low_stock_threshold(self, value: Any = None):
        """Fetch and set low stock threshold.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {low_stock_threshold = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.low_stock_threshold`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.low_stock_threshold) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.low_stock_threshold}")
            return
    
        # Записываем результат в поле `low_stock_threshold` объекта `ProductFields`
        self.fields.low_stock_threshold = value


    @close_pop_up()
    async def minimal_quantity(self, value: Any = None):
        """Fetch and set minimal quantity.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {minimal_quantity = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.minimal_quantity`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.minimal_quantity) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.minimal_quantity}")
            return
    
        # Записываем результат в поле `minimal_quantity` объекта `ProductFields`
        self.fields.minimal_quantity = value


    @close_pop_up()
    async def mpn(self, value: Any = None):
        """Fetch and set MPN (Manufacturer Part Number).
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {mpn = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.mpn`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.mpn) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.mpn}")
            return
    
        # Записываем результат в поле `mpn` объекта `ProductFields`
        self.fields.mpn = value


    @close_pop_up()
    async def name(self, value: Any = None):
        """Fetch and set product name.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {name = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.name`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.name) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.name}")
            return
    
        # Записываем результат в поле `name` объекта `ProductFields`
        self.fields.name = value


    @close_pop_up()
    async def online_only(self, value: Any = None):
        """Fetch and set online-only status.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {online_only = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.online_only`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.online_only) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.online_only}")
            return
    
        # Записываем результат в поле `online_only` объекта `ProductFields`
        self.fields.online_only = value


    @close_pop_up()
    async def on_sale(self, value: Any = None):
        """Fetch and set on sale status.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {on_sale = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.on_sale`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.on_sale) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.on_sale}")
            return
    
        # Записываем результат в поле `on_sale` объекта `ProductFields`
        self.fields.on_sale = value


    @close_pop_up()
    async def out_of_stock(self, value: Any = None):
        """Fetch and set out of stock status.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {out_of_stock = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.out_of_stock`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.out_of_stock) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.out_of_stock}")
            return
    
        # Записываем результат в поле `out_of_stock` объекта `ProductFields`
        self.fields.out_of_stock = value


    @close_pop_up()
    async def pack_stock_type(self, value: Any = None):
        """Fetch and set pack stock type.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {pack_stock_type = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.pack_stock_type`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.pack_stock_type) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.pack_stock_type}")
            return
    
        # Записываем результат в поле `pack_stock_type` объекта `ProductFields`
        self.fields.pack_stock_type = value


    @close_pop_up()
    async def price(self, value: Any = None):
        """Fetch and set price.
    
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {price = `value`} при определении класса.
        Если `value` было передано, его значение подставляется в поле `ProductFields.price`.
        """
    
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.price) or ''
    
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.price}")
            return
    
        # Записываем результат в поле `price` объекта `ProductFields`
        self.fields.price = value


    @close_pop_up()
    async def product_type(self, value: Any = None):
        """Fetch and set product type.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {product_type = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.product_type`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.product_type) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.product_type}")
            return

        # Записываем результат в поле `product_type` объекта `ProductFields`
        self.fields.product_type = value

    @close_pop_up()
    async def quantity(self, value: Any = None):
        """Fetch and set quantity.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {quantity = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.quantity`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.quantity) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.quantity}")
            return

        # Записываем результат в поле `quantity` объекта `ProductFields`
        self.fields.quantity = value

    @close_pop_up()
    async def quantity_discount(self, value: Any = None):
        """Fetch and set quantity discount.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {quantity_discount = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.quantity_discount`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.quantity_discount) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.quantity_discount}")
            return

        # Записываем результат в поле `quantity_discount` объекта `ProductFields`
        self.fields.quantity_discount = value

    @close_pop_up()
    async def redirect_type(self, value: Any = None):
        """Fetch and set redirect type.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {redirect_type = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.redirect_type`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.redirect_type) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.redirect_type}")
            return

        # Записываем результат в поле `redirect_type` объекта `ProductFields`
        self.fields.redirect_type = value

    @close_pop_up()
    async def reference(self, value: Any = None):
        """Fetch and set reference.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {reference = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.reference`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.reference) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.reference}")
            return

        # Записываем результат в поле `reference` объекта `ProductFields`
        self.fields.reference = value
    @close_pop_up()
    async def show_condition(self, value: Any = None):
        """Fetch and set show condition.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {show_condition = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.show_condition`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.show_condition) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.show_condition}")
            return

        # Записываем результат в поле `show_condition` объекта `ProductFields`
        self.fields.show_condition = value

    @close_pop_up()
    async def show_price(self, value: Any = None):
        """Fetch and set show price.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {show_price = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.show_price`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.show_price) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.show_price}")
            return

        # Записываем результат в поле `show_price` объекта `ProductFields`
        self.fields.show_price = value

    @close_pop_up()
    async def state(self, value: Any = None):
        """Fetch and set state.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {state = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.state`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.state) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.state}")
            return

        # Записываем результат в поле `state` объекта `ProductFields`
        self.fields.state = value

    @close_pop_up()
    async def text_fields(self, value: Any = None):
        """Fetch and set text fields.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {text_fields = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.text_fields`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.text_fields) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.text_fields}")
            return

        # Записываем результат в поле `text_fields` объекта `ProductFields`
        self.fields.text_fields = value

    @close_pop_up()
    async def unit_price_ratio(self, value: Any = None):
        """Fetch and set unit price ratio.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {unit_price_ratio = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.unit_price_ratio`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.unit_price_ratio) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.unit_price_ratio}")
            return

        # Записываем результат в поле `unit_price_ratio` объекта `ProductFields`
        self.fields.unit_price_ratio = value

    @close_pop_up()
    async def unity(self, value: Any = None):
        """Fetch and set unity.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {unity = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.unity`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.unity) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.unity}")
            return

        # Записываем результат в поле `unity` объекта `ProductFields`
        self.fields.unity = value

    @close_pop_up()
    async def upc(self, value: Any = None):
        """Fetch and set UPC.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {upc = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.upc`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.upc) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.upc}")
            return

        # Записываем результат в поле `upc` объекта `ProductFields`
        self.fields.upc = value

    @close_pop_up()
    async def uploadable_files(self, value: Any = None):
        """Fetch and set uploadable files.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {uploadable_files = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.uploadable_files`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.uploadable_files) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.uploadable_files}")
            return

        # Записываем результат в поле `uploadable_files` объекта `ProductFields`
        self.fields.uploadable_files = value

    @close_pop_up()
    async def default_image_url(self, value: Any = None):
        """Fetch and set default image URL.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {default_image_url = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.default_image_url`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.default_image_url) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.default_image_url}")
            return

        # Записываем результат в поле `default_image_url` объекта `ProductFields`
        self.fields.default_image_url = value

    @close_pop_up()
    async def visibility(self, value: Any = None):
        """Fetch and set visibility.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {visibility = `value`} при определении класса.
        Если `value` был передан - его значение подставляется в поле `ProductFields.visibility`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.visibility) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.visibility}")
            return

        # Записываем результат в поле `visibility` объекта `ProductFields`
        self.fields.visibility = value
    @close_pop_up()
    async def weight(self, value: Any = None):
        """Fetch and set weight.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {weight = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.weight`.
        """
        
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.weight) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.weight}")
            return
        
        # Записываем результат в поле `weight` объекта `ProductFields`
        self.fields.weight = value

    @close_pop_up()
    async def wholesale_price(self, value: Any = None):
        """Fetch and set wholesale price.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {wholesale_price = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.wholesale_price`.
        """
        
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.wholesale_price) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.wholesale_price}")
            return
        
        # Записываем результат в поле `wholesale_price` объекта `ProductFields`
        self.fields.wholesale_price = value

    @close_pop_up()
    async def width(self, value: Any = None):
        """Fetch and set width.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {width = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.width`.
        """
        
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.width) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.width}")
            return
        
        # Записываем результат в поле `width` объекта `ProductFields`
        self.fields.width = value

    @close_pop_up()
    async def specification(self, value: Any = None):
        """Fetch and set specification.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {specification = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.specification`.
        """
        
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.specification) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.specification}")
            return
        
        # Записываем результат в поле `specification` объекта `ProductFields`
        self.fields.specification = value

    @close_pop_up()
    async def link(self, value: Any = None):
        """Fetch and set link.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {link = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.link`.
        """
        
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.link) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.link}")
            return
        
        # Записываем результат в поле `link` объекта `ProductFields`
        self.fields.link = value
    @close_pop_up()
    async def byer_protection(self, value: Any = None):
        """Fetch and set buyer protection.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {byer_protection = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.byer_protection`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.byer_protection) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.byer_protection}")
            return

        # Записываем результат в поле `byer_protection` объекта `ProductFields`
        self.fields.byer_protection = value

    @close_pop_up()
    async def customer_reviews(self, value: Any = None):
        """Fetch and set customer reviews.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {customer_reviews = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.customer_reviews`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.customer_reviews) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.customer_reviews}")
            return

        # Записываем результат в поле `customer_reviews` объекта `ProductFields`
        self.fields.customer_reviews = value

    @close_pop_up()
    async def link_to_video(self, value: Any = None):
        """Fetch and set link to video.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {link_to_video = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.link_to_video`.
        """
        # Получаем значение через execute_locator
        value = value if value else await self.d.execute_locator(self.l.link_to_video) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.link_to_video}")
            return

        # Записываем результат в поле `link_to_video` объекта `ProductFields`
        self.fields.link_to_video = value

    @close_pop_up()
    async def local_saved_image(self, value: Any = None):
        """Fetch and save image locally.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {local_saved_image = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.local_saved_image`.
        """
        # Получаем значение через execute_locator и сохраняем изображение
        value = value if value else save_png_from_url(self.d.execute_locator(self.l.default_image_url), self.fields.id_product)
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.default_image_url}")
            return

        # Записываем результат в поле `local_saved_image` объекта `ProductFields`
        self.fields.local_saved_image = value

    @close_pop_up()
    async def local_saved_video(self, value: Any = None):
        """Fetch and save video locally.
        
        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {local_saved_video = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.local_saved_video`.
        """
        # Получаем значение через execute_locator и сохраняем видео
        value = value if value else await self.d.execute_locator(self.l.local_saved_video) or ''
        
        # Проверяем валидность результата
        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.l.local_saved_video}")
            return

        # Записываем результат в поле `local_saved_video` объекта `ProductFields`
        self.fields.local_saved_video = value
