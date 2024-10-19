""" Шаблон файла `graber.py` поставщика

@todo
    1. проверить на что влияет `out_of_stock()`
"""
## \file ../src/suppliers/grabber_template.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

import asyncio
from pathlib import Path
from typing import List, Dict, Any
from types import SimpleNamespace
from langdetect import detect
from src import gs
from src.suppliers import Supplier
from src.product import ProductFields, record
from src.category import Category
from src.webdriver import Driver as Webdriver
from src.utils import j_loads, j_dumps, pprint, StringFormatter, ProductFieldsNormalizer, ProductFieldsValidator
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException


s: Supplier
l: SimpleNamespace
d: Webdriver
f: ProductFields = ProductFields()

def fetch_and_normalize(field_name: str, normalizer_func):
    """ Декоратор для извлечения данных с помощью `execute_locator` и их нормализации"""
    def decorator(func):
        @wraps(func)
        async def wrapper():
            if not getattr(f, field_name):
                try:
                    raw_data = d.execute_locator(l[field_name]) or ''
                    normalized_data = normalizer_func(raw_data)
                    setattr(f, field_name, normalized_data)
                except ExecuteLocatorException as ex:
                    logger.error(f"Error occurred while executing the locator for the field `{field_name}`: "
                                 f"-------------", ex)
        return wrapper
    return decorator


async def async_grab_page(supplier: Supplier) -> ProductFields:
    """ Асинхронная функция для сбора данных со страницы товара"""

    global s, d, l
    s = supplier
    d = s.driver
    l = s.locators["product"]
    l = l if isinstance(l, SimpleNamespace) else SimpleNamespace(**l)

    async def fetch_specific_data():
        """ Поля, специфичные только для алиэкспресс"""
        # Пример реализации специфичных данных
        # f.specific_field = await d.execute_locator(l["specific_field"]) or ''
        pass

    async def fetch_all_data():
        """ Асинхронная функция для вызова всех функций сбора данных"""
        await fetch_specific_data()  # Call function to fetch specific data

        # Используем асинхронный вызов всех функций
        tasks = [
            additional_shipping_cost(),
            delivery_in_stock(),
            active(),
            additional_delivery_times(),
            advanced_stock_management(),
            affiliate_short_link(),
            affiliate_summary(),
            affiliate_summary_2(),
            affiliate_text(),
            affiliate_image_large(),
            affiliate_image_medium(),
            affiliate_image_small(),
            available_date(),
            available_for_order(),
            available_later(),
            available_now(),
            cache_default_attribute(),
            cache_has_attachments(),
            cache_is_pack(),
            condition(),
            customizable(),
            date_add(),
            date_upd(),
            delivery_out_stock(),
            depth(),
            description(),
            ean13(),
            ecotax(),
            height(),
            how_to_use(),
            id_category_default(),
            additional_categories = [f.id_category_default, s.current_scenario['presta_categories']['additional_categories']],
            id_default_combination(),
            id_default_image(),
            id_manufacturer(),
            id_product(),
            id_supplier(),
            id_tax(),
            id_type_redirected(),
            images_urls(),
            indexed(),
            ingredients(),
            meta_description(),
            meta_keywords(),
            meta_title(),
            is_virtual(),
            isbn(),
            name(),
            link_rewrite(),
            location(),
            low_stock_alert(),
            low_stock_threshold(),
            minimal_quantity(),
            mpn(),
            online_only(),
            on_sale(),
            out_of_stock(),
            pack_stock_type(),
            locale(),
            price(),
            product_type(),
            quantity_discount(),
            redirect_type(),
            reference(),
            show_condition(),
            show_price(),
            state(),
            text_fields(),
            unit_price_ratio(),
            unity(),
            upc(),
            uploadable_files(),
            default_image_url(),
            visibility(),
            weight(),
            wholesale_price(),
            width()
        ]

        await asyncio.gather(*tasks)  # Асинхронно выполняем все задачи

    # Call the function to fetch all data
    await fetch_all_data()
    return f

@fetch_and_normalize("additional_shipping_cost", ProductFieldsNormalizer.normalize_additional_shipping_cost)
async def additional_shipping_cost():
    """ Function for field additional_shipping_cost"""
    ...

@fetch_and_normalize("delivery_in_stock", ProductFieldsNormalizer.normalize_delivery_in_stock)
async def delivery_in_stock():
    """ Function for field delivery_in_stock"""
    ...

@fetch_and_normalize("active", ProductFieldsNormalizer.normalize_active)
async def active():
    """ Function for field active"""
    ...

@fetch_and_normalize("additional_delivery_times", ProductFieldsNormalizer.normalize_additional_delivery_times)
async def additional_delivery_times():
    """ Function for field additional_delivery_times"""
    ...

@fetch_and_normalize("advanced_stock_management", ProductFieldsNormalizer.normalize_advanced_stock_management)
async def advanced_stock_management():
    """ Function for field advanced_stock_management"""
    ...

@fetch_and_normalize("affiliate_short_link", ProductFieldsNormalizer.normalize_affiliate_short_link)
async def affiliate_short_link():
    """ Function for field affiliate_short_link"""
    ...

@fetch_and_normalize("affiliate_summary", ProductFieldsNormalizer.normalize_affiliate_summary)
async def affiliate_summary():
    """ Function for field affiliate_summary"""
    ...

@fetch_and_normalize("affiliate_summary_2", ProductFieldsNormalizer.normalize_affiliate_summary_2)
async def affiliate_summary_2():
    """ Function for field affiliate_summary_2"""
    ...

@fetch_and_normalize("affiliate_text", ProductFieldsNormalizer.normalize_affiliate_text)
async def affiliate_text():
    """ Function for field affiliate_text"""
    ...

@fetch_and_normalize("affiliate_image_large", ProductFieldsNormalizer.normalize_affiliate_image_large)
async def affiliate_image_large():
    """ Function for field affiliate_image_large"""
    ...

@fetch_and_normalize("affiliate_image_medium", ProductFieldsNormalizer.normalize_affiliate_image_medium)
async def affiliate_image_medium():
    """ Function for field affiliate_image_medium"""
    ...

@fetch_and_normalize("affiliate_image_small", ProductFieldsNormalizer.normalize_affiliate_image_small)
async def affiliate_image_small():
    """ Function for field affiliate_image_small"""
    ...

@fetch_and_normalize("available_now", ProductFieldsNormalizer.normalize_available_date)
async def available_now():
    """ Function for field available_date"""
    ...

@fetch_and_normalize("available_date", ProductFieldsNormalizer.normalize_available_date)
async def available_date():
    """ Function for field available_date"""
    ...

@fetch_and_normalize("available_for_order", ProductFieldsNormalizer.normalize_available_for_order)
async def available_for_order():
    """ Function for field available_for_order"""
    ...

@fetch_and_normalize("available_later", ProductFieldsNormalizer.normalize_available_later)
async def available_later():
    """ Function for field available_later"""
    ...

@fetch_and_normalize("cache_default_attribute", ProductFieldsNormalizer.normalize_cache_default_attribute)
async def cache_default_attribute():
    """ Function for field cache_default_attribute"""
    ...

@fetch_and_normalize("cache_has_attachments", ProductFieldsNormalizer.normalize_cache_has_attachments)
async def cache_has_attachments():
    """ Function for field cache_has_attachments"""
    ...

@fetch_and_normalize("cache_is_pack", ProductFieldsNormalizer.normalize_cache_is_pack)
async def cache_is_pack():
    """ Function for field cache_is_pack"""
    ...

@fetch_and_normalize("condition", ProductFieldsNormalizer.normalize_condition)
async def condition():
    """ Function for field condition"""
    ...

@fetch_and_normalize("customizable", ProductFieldsNormalizer.normalize_customizable)
async def customizable():
    """ Function for field customizable"""
    ...

@fetch_and_normalize("date_add", ProductFieldsNormalizer.normalize_date_add)
async def date_add():
    """ Function for field date_add"""
    ...

@fetch_and_normalize("date_upd", ProductFieldsNormalizer.normalize_date_upd)
async def date_upd():
    """ Function for field date_upd"""
    ...

@fetch_and_normalize("delivery_out_stock", ProductFieldsNormalizer.normalize_delivery_out_stock)
async def delivery_out_stock():
    """ Function for field delivery_out_stock"""
    ...

@fetch_and_normalize("depth", ProductFieldsNormalizer.normalize_depth)
async def depth():
    """ Function for field depth"""
    ...

@fetch_and_normalize("description", ProductFieldsNormalizer.normalize_description)
async def description():
    """ Function for field description"""
    ...

@fetch_and_normalize("ean13", ProductFieldsNormalizer.normalize_ean13)
async def ean13():
    """ Function for field ean13"""
    ...

@fetch_and_normalize("ecotax", ProductFieldsNormalizer.normalize_ecotax)
async def ecotax():
    """ Function for field ecotax"""
    ...

@fetch_and_normalize("height", ProductFieldsNormalizer.normalize_height)
async def height():
    """ Function for field height"""
    ...

@fetch_and_normalize("how_to_use", ProductFieldsNormalizer.normalize_how_to_use)
async def how_to_use():
    """ Function for field how_to_use"""
    ...

@fetch_and_normalize("id_category_default", ProductFieldsNormalizer.normalize_id_category_default)
async def id_category_default():
    """ Function for field id_category_default"""
    ...

@fetch_and_normalize("id_default_combination", ProductFieldsNormalizer.normalize_id_default_combination)
async def id_default_combination():
    """ Function for field id_default_combination"""
    ...

@fetch_and_normalize("id_default_image", ProductFieldsNormalizer.normalize_id_default_image)
async def id_default_image():
    """ Function for field id_default_image"""
    ...

@fetch_and_normalize("id_manufacturer", ProductFieldsNormalizer.normalize_id_manufacturer)
async def id_manufacturer():
    """ Function for field id_manufacturer"""
    ...

@fetch_and_normalize("id_product", ProductFieldsNormalizer.normalize_id_product)
async def id_product():
    """ Function for field id_product"""
    ...

@fetch_and_normalize("id_supplier", ProductFieldsNormalizer.normalize_id_supplier)
async def id_supplier():
    """ Function for field id_supplier"""
    ...

@fetch_and_normalize("id_tax", ProductFieldsNormalizer.normalize_id_tax)
async def id_tax():
    """ Function for field id_tax"""
    ...

@fetch_and_normalize("id_type_redirected", ProductFieldsNormalizer.normalize_id_type_redirected)
async def id_type_redirected():
    """ Function for field id_type_redirected"""
    ...

@fetch_and_normalize("images_urls", ProductFieldsNormalizer.normalize_images_urls)
async def images_urls():
    """ Function for field images_urls"""
    ...

@fetch_and_normalize("indexed", ProductFieldsNormalizer.normalize_indexed)
async def indexed():
    """ Function for field indexed"""
    ...

@fetch_and_normalize("ingredients", ProductFieldsNormalizer.normalize_ingredients)
async def ingredients():
    """ Function for field ingredients"""
    ...

@fetch_and_normalize("meta_description", ProductFieldsNormalizer.normalize_meta_description)
async def meta_description():
    """ Function for field meta_description"""
    ...

@fetch_and_normalize("meta_keywords", ProductFieldsNormalizer.normalize_meta_keywords)
async def meta_keywords():
    """ Function for field meta_keywords"""
    ...

@fetch_and_normalize("meta_title", ProductFieldsNormalizer.normalize_meta_title)
async def meta_title():
    """ Function for field meta_title"""
    ...

@fetch_and_normalize("is_virtual", ProductFieldsNormalizer.normalize_is_virtual)
async def is_virtual():
    """ Function for field is_virtual"""
    ...

@fetch_and_normalize("isbn", ProductFieldsNormalizer.normalize_isbn)
async def isbn():
    """ Function for field isbn"""
    ...

@fetch_and_normalize("name", ProductFieldsNormalizer.normalize_name)
async def name():
    """ Function for field name"""
    ...

@fetch_and_normalize("link_rewrite", ProductFieldsNormalizer.normalize_link_rewrite)
async def link_rewrite():
    """ Function for field link_rewrite"""
    ...

@fetch_and_normalize("location", ProductFieldsNormalizer.normalize_location)
async def location():
    """ Function for field location"""
    ...

@fetch_and_normalize("low_stock_alert", ProductFieldsNormalizer.normalize_low_stock_alert)
async def low_stock_alert():
    """ Function for field low_stock_alert"""
    ...

@fetch_and_normalize("low_stock_threshold", ProductFieldsNormalizer.normalize_low_stock_threshold)
async def low_stock_threshold():
    """ Function for field low_stock_threshold"""
    ...

@fetch_and_normalize("minimal_quantity", ProductFieldsNormalizer.normalize_minimal_quantity)
async def minimal_quantity():
    """ Function for field minimal_quantity"""
    ...

@fetch_and_normalize("mpn", ProductFieldsNormalizer.normalize_mpn)
async def mpn():
    """ Function for field mpn"""
    ...

@fetch_and_normalize("name_language", ProductFieldsNormalizer.normalize_name_language)
async def name_language():
    """ Function for field name_language"""
    ...

@fetch_and_normalize("price", ProductFieldsNormalizer.normalize_price)
async def price():
    """ Function for field price"""
    ...

@fetch_and_normalize("quantity", ProductFieldsNormalizer.normalize_quantity)
async def quantity():
    """ Function for field quantity"""
    ...

@fetch_and_normalize("reference", ProductFieldsNormalizer.normalize_reference)
async def reference():
    """ Function for field reference"""
    ...

@fetch_and_normalize("short_description", ProductFieldsNormalizer.normalize_short_description)
async def short_description():
    """ Function for field short_description"""
    ...

@fetch_and_normalize("specific_price", ProductFieldsNormalizer.normalize_specific_price)
async def specific_price():
    """ Function for field specific_price"""
    ...

@fetch_and_normalize("supplier_name", ProductFieldsNormalizer.normalize_supplier_name)
async def supplier_name():
    """ Function for field supplier_name"""
    ...

@fetch_and_normalize("tags", ProductFieldsNormalizer.normalize_tags)
async def tags():
    """ Function for field tags"""
    ...

@fetch_and_normalize("unit_price", ProductFieldsNormalizer.normalize_unit_price)
async def unit_price():
    """ Function for field unit_price"""
    ...

@fetch_and_normalize("width", ProductFieldsNormalizer.normalize_width)
async def width():
    """ Function for field width"""
    ...

