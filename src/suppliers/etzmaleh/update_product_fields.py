## \file src/suppliers/etzmaleh/update_product_fields.py
"""   [File's Description]


@namespace src: src
 \package src.suppliers.etzmaleh
\file update_product_fields.py
 
 @section libs imports:
  - typing 
  - time 
  - gs 
  - helpers 
  - tools 
  - product 
  - suppliers 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""

## \file ../src/suppliers/etzmaleh/update_product_fields.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from typing import Union
import time
# ----------------------------
from src import gs
from src.logger import logger
from src.utils import StringFormatter, StringNormalizer
from src.product import Product, ProductFields
from src.suppliers import Supplier
# ----------------------------

def set_product_fields(s:Supplier,f:ProductFields) -> ProductFields:

    """ Собираю информацию со страницы товара
    """
    _d = s.driver
    p = Product(webelements_locators = s.locators.get('product'))
    
    _l = p.webelements_locators

    """ ID,ASIN,SKU,SUPPLIER SKU """
    
    def set_name_brand(p) -> bool:
        """ set the product ID & brand
        Attrs:
    
            
        @returns
    	"""
        _product_name = _d.execute_locator(_l['name'])
        # '''TODO: Это баг! '''

        p.field_name = _product_name
        p.field_brand = _d.execute_locator(_l['Brand'])
        ...



        
    #               """  SUMMARY,DESCRIPTION,REF DESCRIPTION,CONDITION  """
    
    def set_summary_description_meta() -> bool:
        """ set the 
        @returns
    	"""
        p.field_summary = _d.execute_locator(_l['Summary'])
        p.field_specification = _d.execute_locator(_l['Specification'])
        p.field_description = _d.execute_locator(_l['Description'])
        p.field_refurbished_product_decription = _d.execute_locator(
            _l['Refirbished product description'])
        if p.field_refurbished_product_decription is None:
            p.field_condition = 'new'

        ...

        
        
        
        
    #               SCREENSHOT                  #

    try:
        screenshot = _d.execute_locator(_l['Screenshot'])
    except Exception as ex:
        logger.exception(f"Ошибка", ex)

    
    
    #           PRICE,QTY                   #
    
    
    try:
        _price = _d.execute_locator(_l['Price tax excluded'])
        if len(_price) == 0:
            logger.error(f'''Промахнулся мимо цены.  
            URL:{_d.current_url}
            LOCATOR: {_l['price']}''')
            ...
            #'''TODO: Это баг! '''
        _price = StringFormatter.clear_price(_price)
        if _price == 0:
            logger.error(f'''Промахнулся мимо цены.  
            {_d.current_url}''')
            #'''TODO: Это баг! '''
            return
        p.field_cost_price = p.field_price_tax_exluded = p.field_price_tax_included = _price
        p.field_qty = _d.execute_locator(_l['Quantity'])
    except Exception as ex:
        logger.error(f"""Exception message - {ex.with_traceback()}""",ex)

    
    
    #           AFFILIATE               #
    
    try:
        p.field_affiliate_short_link = _d.execute_locator(_l['affiliate_link'])[1]
        p.field_affiliate_text = _d.execute_locator(_l['affiliate_img_HTML'])[1]
        p.field_affiliate_summary = _d.execute_locator(_l['affiliate_iframe'])[1]
    except Exception as ex:
        logger.error(f'''  exception message ''',ex)
    # """
    # если локатор список, то ответ тоже будет списком
    # """
   

    ## set_delivery    
    def set_delivery():
        _shipping = _d.execute_locator(_l['product_shipping_details'])
        if 'FREE Shipping' in _shipping:
            _field['shipping price'] = 0
            return True
        _field['shipping price'] = StringFormatter.clear_price(_shipping)
        return True
   

   
    def set_images():
        _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
        _img_name = f'''{_field['sku']}.png'''
        _field['img url'] =f'''{_http_server}/{_img_name}'''
        screenshot = _d.execute_locator(_l['main_image_locator'])
        s.save_and_send_via_ftp({_img_name:screenshot})
      


    return pp