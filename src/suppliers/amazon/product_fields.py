## \file hypotez/src/suppliers/amazon/product_fields.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.amazon """
"""   [File's Description]

@namespace src: src
 \package src.suppliers.amazon
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


""" Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
1. Заполняю поля, необходимые для создания нового товара
2. Получаю `id_product` созданного товара
3. Используя полученный `id_product` загружаю дефолтную картинку
4. итд.
"""

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
    """ добавляю поля в таблицу, 
    которые могут по разному наполняться ( в зависимости от строения локатора) 
   
    
    Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
    1. (->) Добавляю поля, необходимые для создания нового товара
    2. (<-) Получаю `id_product` созданного товара
    3. (->) Используя полученный `id_product` загружаю дефолтную картинку и другие элементы
            в новый товар
    4. итд.
    """


    
    _field.active = asyncio.run (  )
    _field.additional_delivery_times = asyncio.run (  )
    _field.additional_shipping_cost  = asyncio.run (  )
    _field.advanced_stock_management = asyncio.run (  )
    _field.affiliate_short_link = asyncio.run (  )
    _field.affiliate_summary = asyncio.run (  )
    _field.affiliate_summary_2 = asyncio.run (  )
    _field.affiliate_text = asyncio.run (  )
    _field.available_date = asyncio.run (  )
    _field.available_for_order = asyncio.run (  )
    _field.available_later = asyncio.run (  )
    _field.available_now = asyncio.run (  )
    _field.cache_default_attribute = asyncio.run (  )
    _field.cache_has_attachments = asyncio.run (  )
    _field.cache_is_pack = asyncio.run (  )
    #_field.category_ids_append <- добавочные категории.
    #_field.category_ids <- 
    _field.condition = asyncio.run (  )
    _field.customizable = asyncio.run (  )
    _field.date_add = asyncio.run (  )
    _field.date_upd = asyncio.run (  )
    _field.delivery_in_stock = asyncio.run (  )
    _field.delivery_out_stock = asyncio.run (  )
    _field.depth = asyncio.run (  )
    _field.description = asyncio.run (  )
    _field.description_short = asyncio.run (  )
    _field.ean13 = asyncio.run (  )
    _field.ecotax = asyncio.run (  )
    _field.height = asyncio.run (  )
    _field.how_to_use = asyncio.run (  )
    _field.id_category_default = asyncio.run (  )
    _field.id_default_combination = asyncio.run (  )
    _field.id_default_image = asyncio.run (  )
    _field.id_lang = asyncio.run (  )
    _field.id_manufacturer = asyncio.run (  )
    _field.id_product = asyncio.run (  )
    _field.id_shop_default = asyncio.run (  )
    _field.id_product = asyncio.run (  )
    _field.id_supplier = asyncio.run (  )
    _field.id_tax = asyncio.run (  )
    _field.id_type_redirected = asyncio.run (  )
    _field.images_urls = asyncio.run (  )
    _field.indexed = asyncio.run (  )
    _field.ingredients = asyncio.run (  )
    _field.id_tax = asyncio.run (  )
    _field.id_type_redirected = asyncio.run (  )
    _field.images_urls = asyncio.run (  )
    _field.indexed = asyncio.run (  )
    _field.ingredients = asyncio.run (  )
    _field.is_virtual = asyncio.run (  )
    _field.isbn = asyncio.run (  )
    _field.link_rewrite = asyncio.run (  )
    _field.location = asyncio.run (  )
    _field.low_stock_alert = asyncio.run (  )
    _field.low_stock_threshold = asyncio.run (  )
    _field.meta_description = asyncio.run (  )
    _field.meta_keywords = asyncio.run (  )
    _field.meta_title = asyncio.run (  )
    _field.minimal_quantity = asyncio.run (  )
    _field.mpn = asyncio.run (  )
    _field.name = asyncio.run (  )
    _field.online_only = asyncio.run (  )
    _field.on_sale = asyncio.run (  )
    _field.out_of_stock = asyncio.run (  )
    _field.pack_stock_type = asyncio.run (  )
    _field.position_in_category = asyncio.run (  )
    _field.price = asyncio.run (  )
    _field.product_type = asyncio.run (  )
    _field.quantity = asyncio.run (  )
    _field.quantity_discount = asyncio.run (  )
    _field.redirect_type = asyncio.run (  )
    _field.reference = asyncio.run (  )
    _field.show_condition = asyncio.run (  )
    _field.show_price = asyncio.run (  )
    _field.state = asyncio.run (  )
    _field.supplier_reference = asyncio.run (  )
    _field.text_fields = asyncio.run (  )
    _field.unit_price_ratio = asyncio.run (  )
    _field.unity = asyncio.run (  )
    _field.upc = asyncio.run (  )
    _field.uploadable_files = asyncio.run (  )
    _field.default_image_url = asyncio.run (  )
    _field.visibility = asyncio.run (  )
    _field.weight = asyncio.run (  )
    _field.wholesale_price = asyncio.run (  )
    _field.width = asyncio.run (  )
    _ = s.driver.execute_locator
    l = s.reread_locators('product')



    def set_price(s, format: str = 'str') -> str | float:
        """ Привожу денюшку через флаг `format` к 
        [ ] float 
        [v] str
        """
        #l = s.reread_locators('product')
        try:
            raw_price = _ ( l ['price']['new'] )[0]
            ''' raw_price получаю в таком виде:
            ILS382.00\nILS382\n.\n00
            '''
            raw_price = str (raw_price).split ('\n')[0]
            return StringNormalizer.normalize_price (raw_price)
        except Exception as ex:
            logger.error (ex)
            return

   

    ASIN = _ (l ['ASIN'] )
    f.reference = f'{s.supplier_id}-{ASIN}'
    f.supplier_reference = ASIN
    f.price = set_price (s, format = 'str')
    f.name = _ (l ['name'] )[0]
    f.images_urls = _ (l ['additional_images_urls'] )[0]
    try:    
        #f.description_short = _ (l ['description_short'] )[0]
        f.description_short = _ (l ['description_short'] )[0]
    except Exception as ex:
        logger.error(ex)
        return

    f.id_supplier = s.supplier_id
        
    affiliate = _(l['affiliate_short_link'])[1][0]
    affiliate = affiliate[1][0]
    f.affiliate_short_link = affiliate

    f.link_rewrite = f.reference
    #TODO: неправильно сделано!!!!

    
    return f

