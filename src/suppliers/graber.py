## \file ../src/suppliers/graber.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
""" Базовый класс сбора данных со старницы для всех поставщиков
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import Any, Callable
from langdetect import detect
from functools import wraps

from src import gs
from src.suppliers.locator import Locator
from src.product.product_fields import ProductFields
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException
from src.prestashop import Prestashop

d: Driver = None
l: Locator = None

# Определение декоратора для закрытия всплывающих окон
def close_popup(value: Any = None) -> Callable:
    """Creates a decorator to close pop-ups before executing the main function logic.

    Args:
        value (Any): Optional value passed to the decorator.

    Returns:
        Callable: The decorator wrapping the function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                await d.execute_locator(l.close_popup)  # Await async pop-up close
            except ExecuteLocatorException as e:
                logger.debug(f"Error executing locator: {e}")
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator

class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""
    
    def __init__(self, supplier_prefix: str, locator: Locator):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locator (Locator): Экземпляр класса Locator.
            driver (Driver): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        global l
        l = self.l = locator
        self.fields = ProductFields()

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
        return (
            value if value else
            await asyncio.to_thread(locator_func) if locator_func() else
            self.error(field_name) or default
        )

    @close_popup()
    async def additional_shipping_cost(self, value: Any = None):
        """Fetch and set additional shipping cost."""
        self.fields.additional_shipping_cost = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.additional_shipping_cost) or []), 
            'additional_shipping_cost'
        )

    @close_popup()
    async def delivery_in_stock(self, value: Any = None):
        """Fetch and set delivery in stock status."""
        self.fields.delivery_in_stock = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.delivery_in_stock) or []), 
            'delivery_in_stock'
        )

    @close_popup()
    async def active(self, value: Any = None):
        """Fetch and set active status."""
        self.fields.active = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.active) or []), 
            'active'
        )

    @close_popup()
    async def additional_delivery_times(self, value: Any = None):
        """Fetch and set additional delivery times."""
        self.fields.additional_delivery_times = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.additional_delivery_times) or []), 
            'additional_delivery_times'
        )

    @close_popup()
    async def advanced_stock_management(self, value: Any = None):
        """Fetch and set advanced stock management status."""
        self.fields.advanced_stock_management = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.advanced_stock_management) or []), 
            'advanced_stock_management'
        )

    @close_popup()
    async def affiliate_short_link(self, value: Any = None):
        """Fetch and set affiliate short link."""
        self.fields.affiliate_short_link = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_short_link) or []), 
            'affiliate_short_link'
        )

    @close_popup()
    async def affiliate_summary(self, value: Any = None):
        """Fetch and set affiliate summary."""
        self.fields.affiliate_summary = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_summary) or []), 
            'affiliate_summary'
        )

    @close_popup()
    async def affiliate_summary_2(self, value: Any = None):
        """Fetch and set affiliate summary 2."""
        self.fields.affiliate_summary_2 = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_summary_2) or []), 
            'affiliate_summary_2'
        )



    @close_popup()
    async def affiliate_text(self, value: Any = None):
        self.fields.affiliate_text = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_text) or []), 
            'affiliate_text'
        )

    @close_popup()
    async def affiliate_image_large(self, value: Any = None):
        self.fields.affiliate_image_large = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_image_large) or []), 
            'affiliate_image_large'
        )

    @close_popup()
    async def affiliate_image_medium(self, value: Any = None):
        self.fields.affiliate_image_medium = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_image_medium) or []), 
            'affiliate_image_medium'
        )
    @close_popup()
    async def affiliate_image_small(self, value: Any = None):
        self.fields.affiliate_image_small = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.affiliate_image_small) or []), 
            'affiliate_image_small'
        )

    @close_popup()
    async def available_date(self, value: Any = None):
        self.fields.available_date = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.available_date) or []), 
            'available_date'
        )

    @close_popup()
    async def available_for_order(self, value: Any = None):
        self.fields.available_for_order = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.available_for_order) or []), 
            'available_for_order'
        )

    @close_popup()
    async def available_later(self, value: Any = None):
        self.fields.available_later = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.available_later) or []), 
            'available_later'
        )

    @close_popup()
    async def available_now(self, value: Any = None):
        f.available_now = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.available_now) or []), 
            'available_now'
        )

    @close_popup()
    async def additional_categories(self, value: str | list = None) -> dict:
        self.fields.additional_categories = value if value else ''

    @close_popup()
    async def cache_default_attribute(self, value: Any = None):
        self.fields.cache_default_attribute = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.cache_default_attribute) or []), 
            'cache_default_attribute'
        )

    @close_popup()
    async def cache_has_attachments(self, value: Any = None):
        self.fields.cache_has_attachments = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.cache_default_attribute) or []), 
            'cache_has_attachments'
        )

    @close_popup()
    async def cache_is_pack(self, value: Any = None):
        self.fields.cache_is_pack = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.cache_is_pack) or []), 
            'cache_is_pack'
        )

    @close_popup()
    async def condition(self, value: Any = None):
        self.fields.condition = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.condition) or []), 
            'condition'
        )

    @close_popup()
    async def condition(self, value: Any = None):
        self.fields.condition = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.condition) or []), 
            'condition'
        )

    @close_popup()
    async def customizable(self, value: Any = None):
        self.fields.customizable = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.customizable) or []), 
            'customizable'
        )

    @close_popup()
    async def date_add(self, value: Any = None):
        self.fields.date_add = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.date_add) or []), 
            'date_add'
        )

    @close_popup()
    async def date_upd(self, value: Any = None):
        self.fields.date_upd = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.date_upd) or []), 
            'date_upd'
        )

    @close_popup()
    async def delivery_out_stock(self, value: Any = None):
        self.fields.delivery_out_stock = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.delivery_out_stock) or []), 
            'delivery_out_stock'
        )

    @close_popup()
    async def depth(self, value: Any = None):
        self.fields.depth = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.depth) or []), 
            'depth'
        )

    @close_popup()
    async def description(self, value: Any = None):
        self.fields.description = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.description) or []), 
            'description'
        )

    @close_popup()
    async def description_short(self, value: Any = None):
        self.fields.description_short = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.description_short) or []), 
            'description_short'
        )

    @close_popup()
    async def id_category_default(self, value: Any = None):
        self.fields.id_category_default = value

    @close_popup()
    async def id_default_combination(self, value: Any = None):
        self.fields.id_default_combination = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_default_combination) or []), 
            'id_default_combination'
        )

    @close_popup()
    async def id_product(self, value: Any = None):
        if value:
            self.fields.id_product = value
            return
        self.fields.id_supplier = self.fields.id_supplier or self.d.execute_locator(self.l.id_supplier)
        self.fields.id_product = f"{self.supplier_prefix}-{self.fields.id_supplier}" if self.fields.id_supplier else None

    @close_popup()
    async def locale(self, value: Any = None):
        i18n = value or d.locale
        if not i18n and self.fields.name['language'][0]['value']:
            text = self.fields.name['language'][0]['value']
            i18n = detect(text)
        self.fields.locale = i18n

    @close_popup()
    async def id_default_image(self, value: Any = None):
        self.fields.id_default_image = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_default_image) or []), 
            'id_default_image'
        )

    @close_popup()
    async def ean13(self, value: Any = None):
        self.fields.ean13 = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.ean13) or []), 
            'ean13'
        )

    @close_popup()
    async def ecotax(self, value: Any = None):
        self.fields.ecotax = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.ecotax) or []), 
            'ecotax'
        )

    @close_popup()
    async def height(self, value: Any = None):
        self.fields.height = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.height) or []), 
            'height'
        )

    @close_popup()
    async def how_to_use(self, value: Any = None):
        self.fields.how_to_use = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.how_to_use) or []), 
            'how_to_use'
        )

    @close_popup()
    async def id_manufacturer(self, value: Any = None):
        self.fields.id_manufacturer = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_manufacturer) or []), 
            'id_manufacturer'
        )

    @close_popup()
    async def id_supplier(self, value: Any = None):
        self.fields.id_supplier = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_supplier) or []), 
            'id_supplier'
        )

    @close_popup()
    async def id_tax(self, value: Any = None):
        self.fields.id_tax = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_tax) or []), 
            'id_tax'
        )

    @close_popup()
    async def id_type_redirected(self, value: Any = None):
        self.fields.id_type_redirected = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.id_type_redirected) or []), 
            'id_type_redirected'
        )

    @close_popup()
    async def images_urls(self, value: Any = None):
        self.fields.images_urls = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.images_urls) or []), 
            'images_urls'
        )
    @close_popup()
    async def indexed(self, value: Any = None):
        self.fields.indexed = await self.set_field_value(
            value, 
            lambda: ''.join(self.d.execute_locator(self.l.indexed) or []), 
            'indexed'
        )


    @close_popup()
    async def ingredients(self, value: Any = None):
        self.fields.images_urls = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.images_urls) or []),
            'images_urls'
        )

    @close_popup()
    async def meta_description(self, value: Any = None):
        self.fields.meta_description = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.meta_description) or []),
            'meta_description'
        )

    @close_popup()
    async def meta_keywords(self, value: Any = None):
        self.fields.meta_keywords = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.meta_keywords) or []),
            'meta_keywords'
        )

    @close_popup()
    async def meta_title(self, value: Any = None):
        self.fields.meta_title = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.meta_title) or []),
            'meta_title'
        )

    @close_popup()
    async def is_virtual(self, value: Any = None):
        self.fields.is_virtual = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.is_virtual) or []),
            'is_virtual'
        )

    @close_popup()
    async def isbn(self, value: Any = None):
        self.fields.isbn = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.isbn) or []),
            'isbn'
        )


    @close_popup()
    async def link_rewrite(self, value: Any = None) -> str:
        self.fields.link_rewrite = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.link_rewrite) or []),
            'link_rewrite'
        )

    @close_popup()
    async def location(self, value: Any = None):
        self.fields.location = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.location) or []),
            'location'
        )

    @close_popup()
    async def low_stock_alert(self, value: Any = None):
        self.fields.low_stock_alert = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.low_stock_alert) or []),
            'low_stock_alert'
        )

    @close_popup()
    async def low_stock_threshold(self, value: Any = None):
        self.fields.low_stock_threshold = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.low_stock_threshold) or []),
            'low_stock_threshold'
        )

    @close_popup()
    async def minimal_quantity(self, value: Any = None):
        self.fields.minimal_quantity = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.minimal_quantity) or []),
            'minimal_quantity'
        )

    @close_popup()
    async def mpn(self, value: Any = None):
        self.fields.mpn = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.mpn) or []),
            'mpn'
        )

    @close_popup()
    async def name(self, value: Any = None):
        self.fields.name = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.name) or []),
            'name'
        )

    @close_popup()
    async def online_only(self, value: Any = None):
        self.fields.online_only = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.online_only) or []),
            'online_only'
        )

    @close_popup()
    async def on_sale(self, value: Any = None):
        self.fields.on_sale = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.on_sale) or []),
            'on_sale'
        )

    @close_popup()
    async def out_of_stock(self, value: Any = None):
        self.fields.out_of_stock = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.out_of_stock) or []),
            'out_of_stock'
        )

    @close_popup()
    async def pack_stock_type(self, value: Any = None):
        self.fields.pack_stock_type = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.pack_stock_type) or []),
            'pack_stock_type'
        )

    @close_popup()
    async def price(self, value: Any = None):
        self.fields.price = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.price) or []),
            'price'
        )

    @close_popup()
    async def product_type(self, value: Any = None):
        self.fields.product_type = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.product_type) or []),
            'product_type'
        )

    @close_popup()
    async def quantity(self, value: Any = None):
        self.fields.quantity = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.quantity) or []),
            'quantity'
        )

    @close_popup()
    async def quantity_discount(self, value: Any = None):
        self.fields.quantity_discount = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.quantity_discount) or []),
            'quantity_discount'
        )

    @close_popup()
    async def redirect_type(self, value: Any = None):
        self.fields.redirect_type = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.redirect_type) or []),
            'redirect_type'
        )

    @close_popup()
    async def reference(self, value: Any = None):
        self.fields.reference = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.reference) or []),
            'reference'
        )

    @close_popup()
    async def show_condition(self, value: Any = None):
        self.fields.show_condition = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.show_condition) or []),
            'show_condition'
        )

    @close_popup()
    async def show_price(self, value: Any = None):
        self.fields.show_price = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.show_price) or []),
            'show_price'
        )

    @close_popup()
    async def state(self, value: Any = None):
        self.fields.state = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.state) or []),
            'state'
        )

    @close_popup()
    async def text_fields(self, value: Any = None):
        self.fields.text_fields = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.text_fields) or []),
            'text_fields'
        )

    @close_popup()
    async def unit_price_ratio(self, value: Any = None):
        self.fields.unit_price_ratio = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.unit_price_ratio) or []),
            'unit_price_ratio'
        )


    @close_popup()
    async def unity(self, value: Any = None):
        selself.fields.fields.unity = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.unity) or []),
            'unity'
        )

    @close_popup()
    async def upc(self, value: Any = None):
        selself.fields.fields.upc = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.upc) or []),
            'upc'
        )

    @close_popup()
    async def uploadable_files(self, value: Any = None):
        selself.fields.fields.uploadable_files = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.uploadable_files) or []),
            'uploadable_files'
        )

    @close_popup()
    async def default_image_url(self, value: Any = None):
        selself.fields.fields.default_image_url = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.default_image_url) or []),
            'default_image_url'
        )

    @close_popup()
    async def visibility(self, value: Any = None):
        selself.fields.fields.visibility = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.visibility) or []),
            'visibility'
        )

    @close_popup()
    async def weight(self, value: Any = None):
        selself.fields.fields.weight = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.weight) or []),
            'weight'
        )

    @close_popup()
    async def wholesale_price(self, value: Any = None):
        selself.fields.fields.wholesale_price = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.wholesale_price) or []),
            'wholesale_price'
        )

    @close_popup()
    async def width(self, value: Any = None):
        selself.fields.fields.width = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.width) or []),
            'width'
        )

    @close_popup()
    async def specification(self, value: Any = None):
        selself.fields.fields.specification = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.specification) or []),
            'specification'
        )

    @close_popup()
    async def link(self, value: Any = None):
        selself.fields.fields.link = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.link) or []),
            'link'
        )

    @close_popup()
    async def byer_protection(self, value: Any = None):
        self.fields.byer_protection = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.byer_protection) or []),
            'byer_protection'
        )

    @close_popup()
    async def customer_reviews(self, value: Any = None):
        self.fields.customer_reviews = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.customer_reviews) or []),
            'customer_reviews'
        )

    @close_popup()
    async def link_to_video(self, value: Any = None):
        self.fields.link_to_video = await self.set_field_value(
            value,
            lambda: ''.join(self.d.execute_locator(self.l.link_to_video) or []),
            'link_to_video'
        )

    @close_popup()
    async def local_saved_image(self, value: Any = None):
        self.fields.local_saved_image = await self.set_field_value(
            value,
            lambda: save_png_from_url( d.execute_locator(self.l.default_image_url), f.id_product),
            'local_saved_image'
        )

    @close_popup()
    async def local_saved_video(self, value: Any = None):
        self.fields.local_saved_video = await self.set_field_value(
            value,
            lambda: d.execute_locator(self.l.local_saved_video),
            'local_saved_video'
        )
