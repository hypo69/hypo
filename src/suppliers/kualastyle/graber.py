## \file ../src/suppliers/morlevi/graber.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
""" morlevi
"""

import os, sys, asyncio
from pathlib import Path
from typing import List, Union, Dict, Any, Optional
from types import SimpleNamespace
from urllib import response
from langdetect import detect
from functools import wraps

from src import gs
from src.suppliers import Supplier
from src.product import ProductFields, record
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils import pprint 
from src.logger import logger 
from src.logger.exceptions import ExecuteLocatorException
from src.prestashop import Prestashop



supplier_prefix = 'kualastyle'

s: Supplier = Supplier(supplier_prefix = supplier_prefix)
#l: dict = j_loads(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
l: SimpleNamespace
l = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
if not l:
    logger.debug(f"Не определились локаторы - ошибка в файле  {gs.path.src}/suppliers/{supplier_prefix}/locators/product.json")
    ...
f: ProductFields
d: Driver

def close_pop_up(value:Any = None):
    """
    Decorator to call `d.execute_locator` before the actual function logic.
    
    Args:
        locator_key (str): Locator key to be executed before the function logic.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Execute locator before the original function logic
            try:
                result = d.execute_locator(l.close_popup)
                ...
                
            except ExecuteLocatorException as e:
                #raise  # Re-raise the exception if needed
                ...

            # Continue with the original function logic
            return func(*args, **kwargs)
        return wrapper
    return decorator

async def async_grab_page(driver:Driver) -> ProductFields:
    """"""
    ...
    global d
    d = driver



    async def fetch_specific_data(value:Any = None):
        """Место для специальных операций с полями """
        return True
                
    async def fetch_all_data(**kwards):
        global f
        f = ProductFields()
    
        # Call function to fetch specific data
        # await fetch_specific_data(**kwards)  

        # Uncomment the following lines to fetch specific data
        # await additional_shipping_cost(kwards.get("additional_shipping_cost", ''))
        # await delivery_in_stock(kwards.get("delivery_in_stock", ''))
        # await active(kwards.get("active", ''))
        # await additional_delivery_times(kwards.get("additional_delivery_times", ''))
        # await advanced_stock_management(kwards.get("advanced_stock_management", ''))
        # await affiliate_short_link(kwards.get("affiliate_short_link", ''))
        # await affiliate_summary(kwards.get("affiliate_summary", ''))
        # await affiliate_summary_2(kwards.get("affiliate_summary_2", ''))
        # await affiliate_text(kwards.get("affiliate_text", ''))
        # await affiliate_image_large(kwards.get("affiliate_image_large", ''))
        # await affiliate_image_medium(kwards.get("affiliate_image_medium", ''))
        # await affiliate_image_small(kwards.get("affiliate_image_small", ''))
        # await available_date(kwards.get("available_date", ''))
        # await available_for_order(kwards.get("available_for_order", ''))
        # await available_later(kwards.get("available_later", ''))
        # await available_now(kwards.get("available_now", ''))
        # await cache_default_attribute(kwards.get("cache_default_attribute", ''))
        # await cache_has_attachments(kwards.get("cache_has_attachments", ''))
        # await cache_is_pack(kwards.get("cache_is_pack", ''))
        # await condition(kwards.get("condition", ''))
        # await customizable(kwards.get("customizable", ''))
        # await date_add(kwards.get("date_add", ''))
        # await date_upd(kwards.get("date_upd", ''))
        # await default_image_url(kwards.get("default_image_url", ''))
        # await delivery_in_stock(kwards.get("delivery_in_stock", ''))
        # await delivery_out_stock(kwards.get("delivery_out_stock", ''))
        # await depth(kwards.get("depth", ''))
        await description(kwards.get("description", ''))
        await description_short(kwards.get("description_short", ''))
        # await ean13(kwards.get("ean13", ''))
        # await ecotax(kwards.get("ecotax", ''))
        # await height(kwards.get("height", ''))
        # await how_to_use(kwards.get("how_to_use", ''))
        # await id_category_default(kwards.get("id_category_default", ''))
        # await additional_categories(f.id_category_default, s.current_scenario['presta_categories']['additional_categories'])
        # await id_default_combination(kwards.get("id_default_combination", ''))
        # await id_default_image(kwards.get("id_default_image", ''))
        # await id_manufacturer(kwards.get("id_manufacturer", ''))
        # await id_product(kwards.get("id_product", ''))
        # await id_supplier(kwards.get("id_supplier", ''))
        # await id_tax(kwards.get("id_tax", ''))
        # await id_type_redirected(kwards.get("id_type_redirected", ''))
        # await images_urls(kwards.get("images_urls", ''))
        # await indexed(kwards.get("indexed", ''))
        # await ingredients(kwards.get("ingredients", ''))
        # await meta_description(kwards.get("meta_description", ''))
        # await meta_keywords(kwards.get("meta_keywords", ''))
        # await meta_title(kwards.get("meta_title", ''))
        # await is_virtual(kwards.get("is_virtual", ''))
        # await isbn(kwards.get("isbn", ''))
        await name(kwards.get("name", ''))
        # await link_rewrite(kwards.get("link_rewrite", ''))
        # await location(kwards.get("location", ''))
        # await low_stock_alert(kwards.get("low_stock_alert", ''))
        # await low_stock_threshold(kwards.get("low_stock_threshold", ''))
        # await minimal_quantity(kwards.get("minimal_quantity", ''))
        # await mpn(kwards.get("mpn", ''))
        # await online_only(kwards.get("online_only", ''))
        # await on_sale(kwards.get("on_sale", ''))
        # await out_of_stock(kwards.get("out_of_stock", ''))
        # await pack_stock_type(kwards.get("pack_stock_type", ''))
        # await locale(kwards.get("locale", ''))        
        # await price(kwards.get("price", ''))
        # await product_type(kwards.get("product_type", ''))
        # await quantity_discount(kwards.get("quantity_discount", ''))
        # await redirect_type(kwards.get("redirect_type", ''))
        # await reference(kwards.get("reference", ''))
        # await show_condition(kwards.get("show_condition", ''))
        # await show_price(kwards.get("show_price", ''))
        # await specification(kwards.get("specification", ''))
        # await state(kwards.get("state", ''))
        # await text_fields(kwards.get("text_fields", ''))
        # await unit_price_ratio(kwards.get("unit_price_ratio", ''))
        # await unity(kwards.get("unity", ''))
        # await upc(kwards.get("upc", ''))
        # await uploadable_files(kwards.get("uploadable_files", ''))
        # await visibility(kwards.get("visibility", ''))
        # await weight(kwards.get("weight", ''))
        # await wholesale_price(kwards.get("wholesale_price", ''))
        # await width(kwards.get("width", ''))
        # await local_saved_image(kwards.get("local_saved_image", ''))
        # await local_saved_video(kwards.get("local_saved_video", ''))

    # Call the function to fetch all data
    await fetch_all_data()
    return f


@close_pop_up()
async def additional_shipping_cost(value:Any = None):
    f.additional_shipping_cost = value if value else d.execute_locator(l.additional_shipping_cost) or ''
        
@close_pop_up()
async def delivery_in_stock(value:Any = None):
    f.delivery_in_stock = value if value else d.execute_locator(l.delivery_in_stock) or ''
        
@close_pop_up()
async def active(value:Any = None):
    f.active = value if value else d.execute_locator(l.active) or ''

@close_pop_up()
async def additional_delivery_times(value:Any = None):
    f.additional_shipping_cost = value if value else d.execute_locator(l.additional_delivery_times) or ''

        
@close_pop_up()
async def advanced_stock_management(value:Any = None):
    f.advanced_stock_management = value if value else d.execute_locator(l.advanced_stock_management) or ''

@close_pop_up()
async def affiliate_short_link(value:Any = None):
    f.affiliate_short_link = value if value else d.execute_locator(l.affiliate_short_link) or ''

@close_pop_up()
async def affiliate_summary(value:Any = None):
    f.affiliate_summary = value if value else d.execute_locator(l.affiliate_summary) or ''

@close_pop_up()
async def affiliate_summary_2(value:Any = None):
    f.affiliate_summary_2 = value if value else d.execute_locator(l.affiliate_summary_2) or ''
        
@close_pop_up()
async def affiliate_text(value:Any = None):
    f.affiliate_text = value if value else d.execute_locator(l.affiliate_text) or ''
        
@close_pop_up()
async def affiliate_image_large(value:Any = None):
    f.affiliate_image_large = value if value else d.execute_locator(l.affiliate_image_large) or ''
        
@close_pop_up()
async def affiliate_image_medium(value:Any = None):
    f.affiliate_image_medium = value if value else d.execute_locator(l.affiliate_image_medium) or ''
        
@close_pop_up()
async def affiliate_image_small(value:Any = None):
    f.affiliate_image_small = value if value else d.execute_locator(l.affiliate_image_small) or ''
        
@close_pop_up()
async def available_date(value:Any = None):
    f.available_date = value if value else d.execute_locator(l.available_date) or ''

@close_pop_up()
async def available_for_order(value:Any = None):
    f.available_for_order = value if value else d.execute_locator(l.available_for_order) or ''

@close_pop_up()
async def available_later(value:Any = None):
    f.available_later = value if value else d.execute_locator(l.available_later) or ''

@close_pop_up()
async def available_now(value:Any = None):
    f.available_now = value if value else d.execute_locator(l.available_now) or ''

@close_pop_up()
async def additional_categories(value: str | list = None) -> Dict:
    f.additional_categories = value if value else ''
        
@close_pop_up()
async def cache_default_attribute(value:Any = None):
    f.cache_default_attribute = value if value else d.execute_locator(l.cache_default_attribute) or ''

@close_pop_up()
async def cache_has_attachments(value:Any = None):
    f.cache_default_attribute = value if value else d.execute_locator(l.cache_default_attribute) or ''

@close_pop_up()
async def cache_is_pack(value:Any = None):
    f.cache_is_pack = value if value else d.execute_locator(l.cache_is_pack) or ''

@close_pop_up()
async def condition(value:Any = None):
    f.condition = value if value else d.execute_locator(l.condition) or ''     
        
@close_pop_up()
async def customizable(value:Any = None):
    f.customizable = value if value else d.execute_locator(l.customizable) or ''

@close_pop_up()
async def date_add(value:Any = None):
    f.customizable = value if value else d.execute_locator(l.date_add) or ''

@close_pop_up()
async def date_upd(value:Any = None):
    f.date_upd = value if value else d.execute_locator(l.date_upd) or ''
    
@close_pop_up()
async def delivery_out_stock(value:Any = None):
    f.delivery_out_stock = value if value else d.execute_locator(l.delivery_out_stock) or ''

@close_pop_up()
async def depth(value:Any = None):
    f.depth = value if value else d.execute_locator(l.depth) or ''
        
@close_pop_up()
async def description(value:Any = None):
    f.description = value if value else d.execute_locator(l.description) or ''


@close_pop_up()
async def description_short(value:Any = None):
    f.description_short = value if value else d.execute_locator(l.description_short) or ''

@close_pop_up()
async def id_category_default(value:Any = None):
    f.id_category_default = s.current_scenario.get("presta_categories", {}).get("default_category", '')

@close_pop_up()
async def id_default_combination(value:Any = None):
    f.id_default_combination = value if value else d.execute_locator(l.id_default_combination) or ''

@close_pop_up()
async def id_product(value:Any = None):
    if value:
       f.id_product = value
       return
    if not f.id_supplier:
        f.id_supplier = d.execute_locator(l.id_supplier)  or None
    if f.id_supplier:
        f.id_product = supplier_prefix+'-'+f.id_supplier
    ...
@close_pop_up()
async def locale(value:Any = None):
    i18n = d.locale
    if not i18n:
        text = f.name['language'][0]['value']
        i18n = detect(text)
        ...
    f.locale = i18n

    ...
@close_pop_up()
async def id_default_image(value:Any = None):
    f.id_default_image = value if value else d.execute_locator(l.id_default_image) or ''

@close_pop_up()
async def ean13(value:Any = None):
    f.id_default_image = value if value else d.execute_locator(l.id_default_image) or ''

@close_pop_up()
async def ecotax(value:Any = None):
    f.ecotax = value if value else d.execute_locator(l.ecotax) or ''

@close_pop_up()
async def height(value:Any = None):
    f.height = value if value else d.execute_locator(l.height) or ''

@close_pop_up()
async def how_to_use(value:Any = None):
    f.how_to_use = value if value else d.execute_locator(l.how_to_use) or ''

@close_pop_up()
async def id_manufacturer(value:Any = None):
    f.id_manufacturer = value if value else d.execute_locator(l.id_manufacturer) or ''
    ...
@close_pop_up()    
async def id_supplier(value:Any = None):
    f.id_manufacturer = value if value else d.execute_locator(l.id_manufacturer) or ''
        
@close_pop_up()
async def id_tax(value:Any = None):
    f.id_manufacturer = value if value else d.execute_locator(l.id_manufacturer) or ''

@close_pop_up()
async def id_type_redirected(value:Any = None):
    f.id_type_redirected = value if value else d.execute_locator(l.id_type_redirected) or ''

@close_pop_up()
async def images_urls(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''


@close_pop_up()
async def indexed(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''

@close_pop_up()
async def ingredients(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''

@close_pop_up()
async def meta_description(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''

@close_pop_up()
async def meta_keywords(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''
        
@close_pop_up()
async def meta_title(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''
        
@close_pop_up()    
async def is_virtual(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''

@close_pop_up()
async def isbn(value:Any = None):
    f.images_urls = value if value else d.execute_locator(l.images_urls) or ''

@close_pop_up()
async def link_rewrite(value:Any = None) -> str:
    f.link_rewrite = value if value else d.execute_locator(l.link_rewrite) or ''
   
@close_pop_up()
async def location(value:Any = None):
    f.location = value if value else d.execute_locator(l.location) or ''

@close_pop_up()
async def low_stock_alert(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def low_stock_threshold(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def minimal_quantity(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def mpn(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def name(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''
        
    
@close_pop_up()
async def online_only(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''
        
@close_pop_up()
async def on_sale(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''
        
@close_pop_up()
async def out_of_stock(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def pack_stock_type(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def price(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def product_type(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()    
async def quantity(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def quantity_discount(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def redirect_type(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def reference(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def show_condition(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def show_price(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def state(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def text_fields(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def unit_price_ratio(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def unity(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def upc(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def uploadable_files(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def default_image_url(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def visibility(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''
        

@close_pop_up()
async def weight(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def wholesale_price(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def width(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''

@close_pop_up()
async def specification(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''


@close_pop_up()
async def link(value:Any = None):
    f.low_stock_alert = value if value else d.execute_locator(l.low_stock_alert) or ''
        

async def byer_protection(value:Any = None):
    f.byer_protection = value if value else d.execute_locator(l.byer_protection) or ''
        

async def customer_reviews(value:Any = None):
    f.customer_reviews = value if value else d.execute_locator(l.customer_reviews) or ''

async def link_to_video(value:Any = None):
    f.link_to_video = value if value else d.execute_locator(l.link_to_video) or ''

async def image_local_saved_path(value:Any = None):
    f.image_local_saved_path = value if value else d.execute_locator(l.image_local_saved_path) or ''

async def video_local_saved_path(value:Any = None):
    f.video_local_saved_path = value if value else d.execute_locator(l.video_local_saved_path) or ''
        
        

