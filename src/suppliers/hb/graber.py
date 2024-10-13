## \file ../src/suppliers/hb/graber.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
""" Асинхронный сборщик полей товара HB -> product_fields
Модуль собирет поля со страницы товара и заполняет поля объекта ProductFields

@todo
    1. проверить на что влияет `out_of_stock()`
"""

import os, sys, asyncio
from pathlib import Path
from typing import List, Union, Dict, Any
from types import SimpleNamespace
from urllib import response

from langdetect import detect
...
from src import gs
from src.suppliers import Supplier
from src.product import ProductFields, record
from src.category import Category
from src.webdriver import Driver as Webdriver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils import pprint
from src.logger import logger 
from src.logger.exceptions import ExecuteLocatorException
from src.prestashop import Prestashop
...

supplier_prefix = 'hb'

s: Supplier = Supplier(supplier_prefix)
l: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
d: Webdriver = None
f: ProductFields = ProductFields()


async def async_grab_page() -> ProductFields:


    async def fetch_specific_data():
        webelements = d.execute_locator(l["product_reference_and_volume_and_price_for_100"])
        for webelement in webelements:
            if ('Fl.oz' in webelement.text) and ('מ"ל' in webelement.text):
                """объем"""
                f.volume = webelement.text
            elif str(r'מחיר ל100 מ"ל') in webelement.text:
                """цена за единицу товара
                @todo придумать куда
                """
                logger.debug(f"""поле цена за единицу товара не на своем месте """)
            elif 'מקט' in webelement.text:
                rawreference = webelement.text
                try:
                   f.supplier_reference = StringFormatter.clear_numbers(rawreference)
                   ...
                except ExecuteLocatorException as e:
                    logger.critical(f"""Не получил макат """, е)
                    ...
                    return
                
    async def fetch_all_data():
        await fetch_specific_data()  # Call function to fetch specific data
        
        await additional_shipping_cost()
        await delivery_in_stock()
        await active()
        await additional_delivery_times()
        await advanced_stock_management()
        await affiliate_short_link()
        await affiliate_summary()
        await affiliate_summary_2()
        await affiliate_text()
        await affiliate_image_large()
        await affiliate_image_medium()
        await affiliate_image_small()
        await available_date()
        await available_for_order()
        await available_later()
        await available_now()

        await cache_default_attribute()
        await cache_has_attachments()
        await cache_is_pack()
        await condition()
        await customizable()
        await date_add()
        await date_upd()
        await delivery_in_stock()
        await delivery_out_stock()
        await depth()
        await description()
        await ean13()
        await ecotax()
        await height()
        await how_to_use()
        await id_category_default()
        await additional_categories(f.id_category_default, s.current_scenario['presta_categories']['additional_categories'])
        await id_default_combination()
        await id_default_image()
        await id_manufacturer()
        await id_product()
        await id_supplier()
        await id_tax()
        await id_type_redirected()
        await images_urls()
        await indexed()
        await ingredients()
        await meta_description()
        await meta_keywords()
        await meta_title()
        await is_virtual()
        await isbn()
        await name()
        await link_rewrite()
        await location()
        await low_stock_alert()
        await low_stock_threshold()
        await meta_description()
        await meta_keywords()
        await minimal_quantity()
        await mpn()
        
        await online_only()
        await on_sale()
        await out_of_stock()
        await pack_stock_type()
        await locale()        
        await price()
        await product_type()
        await quantity_discount()
        await redirect_type()
        await reference()
        await show_condition()
        await show_price()
        await state()
        await text_fields()
        await unit_price_ratio()
        await unity()
        await upc()
        await uploadable_files()
        await default_image_url()
        await visibility()
        await weight()
        await wholesale_price()
        await width()

    # Call the function to fetch all data
    await fetch_all_data()
    return f








async def additional_shipping_cost():
    """  Function for field additional_shipping_cost"""
    ...
    if not f.additional_shipping_cost:
        try:
            f.additional_shipping_cost = d.execute_locator(l["additional_shipping_cost"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `additional_shipping_cost`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        

async def delivery_in_stock():
    """  Function for field delivery_in_stock"""
    ...
    if not f.delivery_in_stock:
        try:
            f.delivery_in_stock = d.execute_locator(l["delivery_in_stock"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `delivery_in_stock`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        

async def active():
    """  Function for field active"""
    ...

async def additional_delivery_times():
    """  Function for field additional_delivery_times"""
    ...
    if not f.additional_delivery_times:
        try:
            f.additional_delivery_times = d.execute_locator(l["additional_delivery_times"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `additional_delivery_times`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        

async def advanced_stock_management():
    """  Function for field advanced_stock_management"""
    ...

async def affiliate_short_link():
    """  Function for field affiliate_short_link"""
    try:
        f.affiliate_short_link = d.current_url
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field affiliate_short_link: ", e)
        


async def affiliate_summary():
    """  Function for field affiliate_summary"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ... 
        

async def affiliate_summary_2():
    """  Function for field affiliate_summary_2"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def affiliate_text():
    """  Function for field affiliate_text"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def affiliate_image_large():
    """  Function for field affiliate_image_large"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def affiliate_image_medium():
    """  Function for field affiliate_image_medium"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def affiliate_image_small():
    """  Function for field affiliate_image_small"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def available_date():
    """  Function for field available_date"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def available_for_order():
    """  Function for field available_for_order
    @
    """
    try:
        response = d.execute_locator(l["available_for_order"])
        f.available_for_order = 1 if available_for_order else 0

    except ExecuteLocatorException as e:
        logger.error(f"""Error occurred while executing the locator for the field `available_for_order`: 
                        response type: {type(response)}
                    response: {pprint(response)}""", e)
    except Exception as e:
        logger.critical(f"""Error occurred while executing the locator for the field `available_for_order`: """, e)
...

async def available_later():
    """  Function for field available_later"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def available_now():
    """  Function for field available_now"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def additional_categories(category_id:list[str], categories_ids:list[str] = None) -> Dict:
    """  Function for field additional_categories"""
    # 
    #                   Это поле должно заполнятся на клиенте. 
    # try:
    #     f.set_additional_categories(category_id, categories_ids)
    # except Exception as e:
    #     logger.error(f"Error occurred while executing the locator for the field condition: ", e)
    ...
        

async def cache_default_attribute():
    """  Function for field cache_default_attribute"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def cache_has_attachments():
    """  Function for field cache_has_attachments"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def cache_is_pack():
    """  Function for field cache_is_pack"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def condition():
    """  Function for field condition"""
    try:
        f.condition = d.execute_locator(l.condition) or 'new'
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field condition: ", e)
    except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `condition`: """, e)        
        

async def customizable():
    """  Function for field customizable"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def date_add():
    """  Function for field date_add"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def date_upd():
    """  Function for field date_upd"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
    

async def delivery_out_stock():
    """  Function for field delivery_out_stock"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...    
        
    
    
async def depth():
    """  Function for field depth"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def description():
    """  Function for field description
    d.execute_locator(l["description"]) может вернуть объект/список selenium
    """
    ...
    if not f.description:
        try:
            f.description = d.execute_locator(l["description"])  or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `description`: 
                         response type: {type(response)}                                 
                        response: {pprint(response)}""", e)
        except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `description`: """, e)
        
    ...
        

async def id_category_default():
    """  Function for field id_category_default"""
    f.id_category_default = s.current_scenario["presta_categories"]["default_category"]
    
async def id_default_combination():
    """  Function for field id_default_combination"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def id_product():
    """  Function for field id_product"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
    
async def locale():
    """  Function for field locale.
    current webpage lang
    """
    ...
    i18n = d.locale
    if not i18n:
        text = f.name['language'][0]['value']
        i18n = detect(text)
        ...
    f.locale = i18n

    ...
    
async def id_default_image():
    """  Function for field id_default_image"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...


async def ean13():
    """  Function for field ean13"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ... 
        

async def ecotax():
    """  Function for field ecotax"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def height():
    """  Function for field height"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def how_to_use():
    """  Function for field how_to_use"""
    ...
    if not f.how_to_use:
        try:
            f.how_to_use = d.execute_locator(l["how_to_use"])  or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `how_to_use`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
        except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `how_to_use`: """, e)
    ...


async def id_manufacturer():
    """  Function for field id_manufacturer"""
    ...
    if not f.id_manufacturer:
        try:
            f.id_manufacturer = d.execute_locator(l["id_manufacturer"])  or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `id_manufacturer`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
        except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `id_manufacturer`: """, e)
    ...
    
async def id_supplier():
    """  Function for field id_supplier"""
    ...
    if not f.id_supplier:
        try:
            f.id_supplier = d.execute_locator(l["id_supplier"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `id_supplier`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ...
        

async def id_tax():
    """  Function for field id_tax"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def id_type_redirected():
    """  Function for field id_type_redirected"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def images_urls():
    """  Function for field additional_images_urls"""
    if not f.images_urls:
        try:
            response = d.execute_locator(l["additional_images_urls"]) or ''
            ...
            f.images_urls = response
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `additional_images_urls`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
            ...
            return
        except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `additional_images_urls`: """, e)
            ...
            return
            
    ...
        

async def indexed():
    """  Function for field indexed"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def ingredients():
    """  Function for field ingredients"""
    ...
    if not f.ingredients:
        try:
            f.ingredients = d.execute_locator(l["ingredients"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `ingredients`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ...


async def meta_description():
    """  Function for field meta_description"""
    ...
    if not f.meta_description:
        try:
            f.meta_description = d.execute_locator(l["meta_description"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `meta_description`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ...    
        

async def meta_keywords():
    """  Function for field meta_keywords"""
    ...
    if not f.meta_keywords:
        try:
            f.meta_keywords = d.execute_locator(l["meta_keywords"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `meta_keywords`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        

async def meta_title():
    """  Function for field meta_title"""
    ...
    if not f.meta_title:
        try:
            f.meta_title = d.execute_locator(l["meta_title"]) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `meta_title`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        
    
async def is_virtual():
    """  Function for field is_virtual"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def isbn():
    """  Function for field isbn"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def link_rewrite() -> str:
    """  Function for field link_rewrite
    @todo
     - Исправить обязательного i18n `record(f,'en-US')`
    """
    ...
    global record
    if not f.name:name()
    _product_fileds = record(f.presta_fields_dict,'en-US') # <- плохое решение
    """ record возвращает плоский словарь """
    try:
        f.link_rewrite = ProductFieldsNormalizer.normalize_link_rewrite(_product_fileds['name']) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the link_rewrite: ", e)
    except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `link_rewrite`: """, e)
...    
    

async def location():
    """  Function for field location"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def low_stock_alert():
    """  Function for field low_stock_alert"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
    
async def low_stock_threshold():
    """  Function for field low_stock_threshold"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def minimal_quantity():
    """  Function for field minimal_quantity"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def mpn():
    """  Function for field mpn"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def name():
    """  Function for field name"""
    try:
        rawname = d.execute_locator (l["name"])[0] or ''
        f.name = ProductFieldsNormalizer.normalize_name(rawname)
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field name: ", e)
        
    

async def online_only():
    """  Function for field online_only"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def on_sale():
    """  Function for field on_sale"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        

async def out_of_stock():
    """  Function for field out_of_stock"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
        


async def pack_stock_type():
    """  Function for field pack_stock_type"""
    ...
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def price():
    """  Function for field price"""
    ...
    if not f.price:
        try:
            rawprice = d.execute_locator(l["price"])[0] or ''
            f.price = ProductFieldsNormalizer.normalize_price(rawprice)
            ...
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `delivery_out_stock`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 

async def product_type():
    """  Function for field product_type"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...
    
async def quantity():
    """  Function for field quantity"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def quantity_discount():
    """  Function for field quantity_discount"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def redirect_type():
    """  Function for field redirect_type"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def reference():
    """  Function for field reference
    locator_description на HB заполняется в отдельной функции. См выше 
    """
    ...
    f.reference = f"""{s.supplier_id}-{f.supplier_reference}"""
    ... 

async def show_condition():
    """  Function for field show_condition"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def show_price():
    """  Function for field show_price"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def state():
    """  Function for field state"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def text_fields():
    """  Function for field text_fields"""
    ...
    # if not f.<FIELD NAME>:
    #     try:
    #         f.<FIELD NAME> = d.execute_locator(l["<FIELD NAME>"]) or ''
    #     except ExecuteLocatorException as e:
    #         logger.error(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: 
    #                         response type: {type(response)}
    #                     response: {pprint(response)}""", e)
    #     except Exception as e:
    #         logger.critical(f"""Error occurred while executing the locator for the field `<FIELD NAME>`: """, e)
    ...

async def unit_price_ratio():
    """  Function for field unit_price_ratio"""
    try:
        #f.unit_price_ratio =  d.execute_locator(l["unit_price_ratio"])[0]  or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field unit_price_ratio: ", e)

async def unity():
    """  Function for field unity"""
    try:
        #f.unity =  d.execute_locator(l["unity"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field unity: ", e)

async def upc():
    """  Function for field upc"""
    try:
        #f.upc =  d.execute_locator(l["upc"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field upc: ", e)
...

async def uploadable_files():
    """  Function for field uploadable_files"""
    try:
        #f.uploadable_files =  d.execute_locator(l["uploadable_files"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field upc: ", e)
    ...

async def default_image_url():
    """  Function for field default_image_url"""
    try:
        f.default_image_url =  d.execute_locator(l["default_image_url"]) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field default_image_url: ", e)

async def visibility():
    """  Function for field visibility"""
    try:
        f.visibility = d.execute_locator(l["visibility"]) or 'both'
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field visibility: ", e)
        


async def weight():
    """  Function for field weight"""
    try:
        f.weight = d.execute_locator(l["weight"]) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field weight: ", e)

async def wholesale_price():
    """  Function for field wholesale_price"""
    try:
        f.wholesale_price = d.execute_locator(l["wholesale_price"]) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field wholesale_price: ", e)

async def width():
    """  Function for field width"""
    try:
        f.width = d.execute_locator(l["width"]) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field width: ", e)

       
async def specification():
    """  Function for field width
    В HB нет такого поля. Копирую из 
    """
    f.specification =  f.description 
    



async def link():
    """  Function for field link"""
    try:
        f["link_to_product"] = d.current_url.split('?')[0]  or ''
        return True
    except Exception as e:
        logger.error(f"Ошибка при получении ссылки на продукт: ", e)
        

async def byer_protection():
    """  Function for field byer_protection"""
    try:
        f["product_byer_protection"] = d.execute_locator(l["byer_protection_locator"]) or ''
        return True
    except ExecuteLocatorException as e:
        f["product_byer_protection"] = None
        logger.error(f"Error occurred while executing the locator for the field byer_protection: ", e)
        

async def customer_reviews():
    """  Function for field customer_reviews"""
    try:
        f["product_customer_reviews"] = d.execute_locator(l["customer_reviews_locator"]) or ''
        return True
    except ExecuteLocatorException as e:
        f["product_customer_reviews"] = None
        logger.error(f"Error occurred while executing the locator for the field customer_reviews: ", e)
        
# 57

async def link_to_video():
    """  Function for field link_to_video"""
    try:
        f["product_customer_reviews"] = d.execute_locator(l["link_to_video"]) or ''
        return True
    except ExecuteLocatorException as e:
        f["product_customer_reviews"] = None
        logger.error(f"Error occurred while executing the locator for the field link_to_video: ", e)
        
        

