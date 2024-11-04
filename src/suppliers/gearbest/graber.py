## \file src/suppliers/gearbest/graber.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Optional
from dataclasses import dataclass, field
from functools import wraps

from src import gs

from src.suppliers import Graber as Grbr, Locator
from src.product import ProductFields
from src.webdriver import Driver
from src.utils.jjson import j_loads_ns
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException

from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Any, Callable

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

supplier_pefix = 'gearbest'
@dataclass(frozen=True)
class Graber(Grbr):
    """Graber class for morlevi grabbing operations."""
    supplier_prefix: str = field(default = supplier_pefix)
    d: Driver = None  # d будет назначен позже в `grab_page()`
    l: Locator = None  # l будет назначен позже в `__post_init__()`

    def __post_init__(self):
        """Post-initialization to load the locator namespace and set global variables."""

        locator_path = Path(gs.path.src, 'suppliers', self.supplier_prefix, 'locators', 'product.json')
        object.__setattr__(self, 'l', Locator(self.supplier_prefix))
        global l
        l = self.l                                                                  
        super().__init__(self.supplier_prefix, self.l)

    async def grab_page(self, driver: Driver) -> ProductFields:
        """Asynchronous function to grab product fields.

        Args:
            driver (Driver): The driver instance to use for grabbing.

        Returns:
            ProductFields: The grabbed product fields.
        """
        global d
        d = self.d = driver  
        
        ...
        # Логика извлечения данных
        async def fetch_all_data(**kwards):
        
            # Call function to fetch specific data
            # await fetch_specific_data(**kwards)  

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

