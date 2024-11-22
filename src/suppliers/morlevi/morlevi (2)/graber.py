## \file hypotez/src/suppliers/morlevi/morlevi (2)/graber.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.morlevi.morlevi (2) 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'development'
  
""" module: src.suppliers.morlevi.morlevi (2) """


""" morlevi
"""

import os, sys, asyncio
from pathlib import Path
from typing import List, Union, Dict, Any, Optional
from types import SimpleNamespace
from urllib import response
from langdetect import detect
from functools import wraps
...
from src import gs
from src.suppliers import Supplier
from src.product import ProductFields, record
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils import pprint 
from src.logger import logger 
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.PrestaShop import PrestaShop

...

supplier_prefix = 'morlevi'

s: Supplier = Supplier(supplier_prefix = supplier_prefix)
#l: dict = j_loads(gs.path.src / 'suppliers' / self.supplier_prefix / 'locators' / 'product.json')
l: SimpleNamespace
l = j_loads_ns(gs.path.src / 'suppliers' / self.supplier_prefix / 'locators' / 'product.json')
if not l:
    logger.debug(f"Не определились локаторы - ошибка в файле  {gs.path.src}/suppliers/{supplier_prefix}/locators/product.json")
    ...
f: ProductFields
d: Driver

def close_popup():
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
                # result = d.execute_locator(l.close_popup)
                ...
                
            except ExecuteLocatorException as e:
                #raise  # Re-raise the exception if needed
                ...

            # Continue with the original function logic
            return func(*args, **kwargs)
        return wrapper
    return decorator

async def grab_page(driver:Driver) -> ProductFields:
    """"""
    ...
    global d
    d = driver



    async def fetch_specific_data():
        """Место для специальных операций с полями """
        return True
                
    async def fetch_all_data():
        global f
        f = ProductFields()
        #await fetch_specific_data()  # Call function to fetch specific data
        
        # await additional_shipping_cost()
        # await delivery_in_stock()
        # await active()
        # await additional_delivery_times()
        # await advanced_stock_management()
        # await affiliate_short_link()
        # await affiliate_summary()
        # await affiliate_summary_2()
        # await affiliate_text()
        # await affiliate_image_large( )
        # await affiliate_image_medium()
        # await affiliate_image_small()
        # await available_date()
        # await available_for_order()
        # await available_later()
        # await available_now()

        # await cache_default_attribute()
        # await cache_has_attachments()
        # await cache_is_pack()
        # await condition()
        # await customizable()
        # await date_add()
        # await date_upd()
        await default_image_url()
        # await delivery_in_stock()
        # await delivery_out_stock()
        # await depth()
        await description()
        # await description_short()
        # await ean13()
        # await ecotax()
        # await height()
        # await how_to_use()
        # await id_category_default()
        # await additional_categories(f.id_category_default, s.current_scenario['presta_categories']['additional_categories'])
        # await id_default_combination()
        # await id_default_image()
        # await id_manufacturer()
        await id_product()
        # await id_supplier()
        # await id_tax()
        # await id_type_redirected()
        # await images_urls()
        # await indexed()
        # await ingredients()
        # await meta_description()
        # await meta_keywords()
        # await meta_title()
        # await is_virtual()
        # await isbn()
        await name()
        # await link_rewrite()
        # await location()
        # await low_stock_alert()
        # await low_stock_threshold()
        # await meta_description()
        # await meta_keywords()
        # await minimal_quantity()
        # await mpn()
        
        # await online_only()
        # await on_sale()
        # await out_of_stock()
        # await pack_stock_type()
        # await locale()        
        # await price()
        # await product_type()
        # await quantity_discount()
        # await redirect_type()
        # await reference()
        # await show_condition()
        # await show_price()
        # await state()
        # await text_fields()
        # await unit_price_ratio()
        # await unity()
        # await upc()
        # await uploadable_files()
        # await visibility()
        # await weight()
        # await wholesale_price()
        # await width()

    # Call the function to fetch all data
    await fetch_all_data()
    return f

@close_popup()
async def additional_shipping_cost():
    """  Function for field additional_shipping_cost"""
    ...
    if not f.additional_shipping_cost:
        try:
            #f.additional_shipping_cost = d.execute_locator(l["additional_shipping_cost"]) or ''
            f.additional_shipping_cost = d.execute_locator(l_ns.additional_shipping_cost) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `additional_shipping_cost`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        
@close_popup()
async def delivery_in_stock():
    """  Function for field delivery_in_stock"""
    ...
    if not f.delivery_in_stock:
        try:
            #f.delivery_in_stock = d.execute_locator(l["delivery_in_stock"]) or ''
            f.delivery_in_stock = d.execute_locator(l_ns.delivery_in_stock) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `delivery_in_stock`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
        
@close_popup()
async def active():
    """  Function for field active"""
    ...

@close_popup()
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
        
@close_popup()
async def advanced_stock_management():
    """  Function for field advanced_stock_management"""
    ...

@close_popup()
async def affiliate_short_link():
    """  Function for field affiliate_short_link"""
    try:
        f.affiliate_short_link = d.current_url
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field affiliate_short_link: ", e)
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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

@close_popup()
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

@close_popup()
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

@close_popup()
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

@close_popup()
async def additional_categories(category_id: list[str], categories_ids: Optional[list[str]] = None) -> Dict:
    """  Function for field additional_categories"""
    # 
    #                   Это поле должно заполнятся на клиенте. 
    # try:
    #     f.set_additional_categories(category_id, categories_ids)
    # except Exception as e:
    #     logger.error(f"Error occurred while executing the locator for the field condition: ", e)
    ...
        
@close_popup()
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
@close_popup()
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
@close_popup()
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
@close_popup()
async def condition():
    """  Function for field condition"""
    try:
        f.condition = d.execute_locator(l.condition) or 'new'
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field condition: ", e)
    except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `condition`: """, e)        
        
@close_popup()
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
@close_popup()
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
@close_popup()
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
    
@close_popup()
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
        
    
@close_popup()
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
        
@close_popup()
async def description():
    """  Function for field description
    d.execute_locator(l["description"]) может вернуть объект/список selenium
    """
    ...
    try:
        f.description = d.execute_locator(l.description)  or ''
        if isinstance(f.description,list):
            ...
    except ExecuteLocatorException as eх:
        logger.error(f"""Error occurred while executing the locator for the field `description`: 
                        response type: {type(response)}                                 
                    response: {pprint(response)}""", eх)
    except Exception as ex:
        logger.debug(f"""Error occurred while executing the locator for the field `description`: """, ex)
        ...


@close_popup()
async def description_short():
    """  Function for field description
    d.execute_locator(l["description"]) может вернуть объект/список selenium
    """
    ...
    try:
        f.description_short = d.execute_locator(l.description_short)  or ''
        if isinstance(f.description_short,list):
            ...
    except ExecuteLocatorException as eх:
        logger.error(f"""Error occurred while executing the locator for the field `description_short`: 
                        response type: {type(response)}                                 
                    response: {pprint(response)}""", eх)
    except Exception as ex:
        logger.critical(f"""Error occurred while executing the locator for the field `description_short`: """, ex)
        ...

@close_popup()
async def id_category_default():
    """  Function for field id_category_default"""
    f.id_category_default = s.current_scenario["presta_categories"]["default_category"]
@close_popup()
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

@close_popup()
async def id_product():
    """  Function for field id_product"""
    ...
    if not f.id_product:
        try:
            if not f.id_supplier:
                f.id_supplier = d.execute_locator(l.id_supplier)  or None
            if f.id_supplier:
                f.id_product = supplier_prefix+'-'+f.id_supplier

        except ExecuteLocatorException as ex:
            logger.critical(f"""Error occurred while executing the locator for the field `id_product`: 
                         response type: {type(response)}                                 
                        response: {pprint(response)}""", ex)
            ...
        except Exception as ex:
            logger.critical(f"""Error occurred while executing the locator for the field `id_product`: """, ex)
            ...
    ...
@close_popup()
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
@close_popup()
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

@close_popup()
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
        
@close_popup()
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
@close_popup()
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
@close_popup()
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

@close_popup()
async def id_manufacturer():
    """  Function for field id_manufacturer"""
    ...
    if not f.id_manufacturer:
        try:
            f.id_manufacturer = d.execute_locator(l.id_manufacturer)  or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `id_manufacturer`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
        except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `id_manufacturer`: """, e)
    ...
@close_popup()    
async def id_supplier():
    """  Function for field id_supplier"""
    ...
    if not f.id_supplier:
        try:
            f.id_supplier = d.execute_locator(l.id_supplier) or ''
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `id_supplier`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ...
        
@close_popup()
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
@close_popup()
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

@close_popup()
async def images_urls():
    """  Function for field images_urls"""
    if not f.images_urls:
        try:
            response = d.execute_locator(l.images_urls) or ''
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
        
@close_popup()
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
@close_popup()
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

@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        
@close_popup()    
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
@close_popup()
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
        
@close_popup()
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
        f.link_rewrite = normalizer.normalize_link_rewrite(_product_fileds['name']) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the link_rewrite: ", e)
    except Exception as e:
            logger.critical(f"""Error occurred while executing the locator for the field `link_rewrite`: """, e)
...    
@close_popup()
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
@close_popup()
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
@close_popup()
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
@close_popup()
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
@close_popup()
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

@close_popup()
async def name():
    """  Function for field name"""
    try:
        rawname = d.execute_locator (l.name)
        if not rawname:
            logger.error("Нет данных")
            return
            
        rawname = rawname[0] if isinstance(rawname, list) else rawname
        f.name = normalizer.normalize_name(rawname)
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field name: ", e)
        
    
@close_popup()
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
        
@close_popup()
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
        
@close_popup()
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
        

@close_popup()
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

@close_popup()
async def price():
    """  Function for field price"""
    ...
    if not f.price:
        try:
            rawprice = d.execute_locator(l["price"])[0] or ''
            f.price = normalizer.normalize_price(rawprice)
            ...
        except ExecuteLocatorException as e:
            logger.error(f"""Error occurred while executing the locator for the field `delivery_out_stock`: 
                            response type: {type(response)}
                        response: {pprint(response)}""", e)
    ... 
@close_popup()
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
@close_popup()    
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
@close_popup()
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
@close_popup()
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
@close_popup()
async def reference():
    """  Function for field reference
    locator_description на HB заполняется в отдельной функции. См выше 
    """
    ...
    f.reference = f"""{s.supplier_id}-{f.supplier_reference}"""
    ... 
@close_popup()
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
@close_popup()
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
@close_popup()
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
@close_popup()
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
@close_popup()
async def unit_price_ratio():
    """  Function for field unit_price_ratio"""
    try:
        #f.unit_price_ratio =  d.execute_locator(l["unit_price_ratio"])[0]  or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field unit_price_ratio: ", e)
@close_popup()
async def unity():
    """  Function for field unity"""
    try:
        #f.unity =  d.execute_locator(l["unity"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field unity: ", e)
@close_popup()
async def upc():
    """  Function for field upc"""
    try:
        #f.upc =  d.execute_locator(l["upc"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field upc: ", e)
...
@close_popup()
async def uploadable_files():
    """  Function for field uploadable_files"""
    try:
        #f.uploadable_files =  d.execute_locator(l["uploadable_files"])[0] or ''
        ...
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field upc: ", e)
    ...

@close_popup()
async def default_image_url():
    """  Function for field default_image_url"""
    try:
        d.scroll(scrolls = 1, frame_size = 200, direction = 'down')
        f.default_image_url =  d.execute_locator(l.default_image_url) or '' # <- может вернуть png как `bytes` !
        ...
    except ExecuteLocatorException as ex:
        logger.error(f"Error occurred while executing the locator for the field default_image_url: ", ex)

@close_popup()
async def visibility():
    """  Function for field visibility"""
    try:
        f.visibility = d.execute_locator(l.visibility) or 'both'
    except ExecuteLocatorException as ex:
        logger.error(f"Error occurred while executing the locator for the field visibility: ", ex)
        

@close_popup()
async def weight():
    """  Function for field weight"""
    try:
        f.weight = d.execute_locator(l.weight) or ''
    except ExecuteLocatorException as ex:
        logger.error(f"Error occurred while executing the locator for the field weight: ", ex)
@close_popup()
async def wholesale_price():
    """  Function for field wholesale_price"""
    try:
        f.wholesale_price = d.execute_locator(l.wholesale_price) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field wholesale_price: ", e)
@close_popup()
async def width():
    """  Function for field width"""
    try:
        f.width = d.execute_locator(l.width) or ''
    except ExecuteLocatorException as e:
        logger.error(f"Error occurred while executing the locator for the field width: ", e)

@close_popup()
async def specification():
    """  Function for field width
    В HB нет такого поля. Копирую из 
    """
    f.specification =  f.description 
    


@close_popup()
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
        
        

