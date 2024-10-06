## \file src/suppliers/ksp/scrapper.py
"""   [File's Description]


@namespace src: src
 \package src.suppliers.ksp
\file scrapper.py
 
 @section libs imports:
  - product 
  - gs 
  - tools 
  
Author(s):
  - Created by [Name] [Last Name] on 08.11.2023 .
"""

## \file ../src/suppliers/ksp/scrapper.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python


from src.product import Product

from src import gs, logger

from src.utils import StringFormatter

## grab data from product page
def grab_product_page(s) -> Product:
    """ Собираю информацию со страницы товара
    """
    _d = s.driver
    p = Product(webelements_locators = s.locators_product)
    _l = p.webelements_locators

    f'''
    
    ID,ASIN,SKU,SUPPLIER SKU
    
    '''
    p.field_supplier_id = s.settings['supplier_id']
    ASIN = _d.current_url.split(f'''/''')[-2]
    p.field_sku = f'''{p.field_supplier_id}_{ASIN} '''
    p.field_supplier_sku = ASIN
    
    f'''
    
    NAME,BRAND
    
    '''
    _product_name = _d.execute_locator(_l['Name*'])
    if len(_product_name) == 0:
        logger.error(f'''Промахнулся мимо Name.  
        {_d.current_url}''')
        #'''TODO: Это баг! '''

    p.field_name = _product_name
    p.field_brand = _d.execute_locator(_l['Brand'])
    
    f'''
    
    SUMMARY,DESCRIPTION,REF DESCRIPTION,CONDITION
    
    '''
    try:
        p.field_summary = _d.execute_locator(_l['Summary'])
        p.field_specification = _d.execute_locator(_l['Specification'])
        p.field_description = _d.execute_locator(_l['Description'])
        p.field_refurbished_product_decription = _d.execute_locator(
            _l['Refirbished product description'])
        if p.field_refurbished_product_decription is None:
            p.field_condition = 'new'

        # p.field_additional_product_info = _d.execute_locator(_l['addition_information'])
        # p.raw_html_product_addition_information = _d.execute_locator(_l['addition_information'])
        # p.raw_html_product_addition_information += _d.execute_locator(_l['techical_details'])


    except Exception as ex:
        logger.error(f"Ошибка!",ех)
    f'''
    
    SCREENSHOT
    
    '''
    try:
        screenshot = _d.execute_locator(_l['Screenshot'])
    except Exception as ex:
        logger.exception(f"Ошибка", ex)
    f'''
    
    PRICE,QTY
    
    '''
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
        logger.error(f'''  exception message ''',ex)
    f'''
    
    AFFILIATE
    
    '''
    try:
        p.field_affiliate_short_link = _d.execute_locator(_l['affiliate_link'])[1]
        p.field_affiliate_text = _d.execute_locator(_l['affiliate_img_HTML'])[1]
        p.field_affiliate_summary = _d.execute_locator(_l['affiliate_iframe'])[1]
    except Exception as ex:
        logger.error(f'''  exception message ''',ex)
    """
    если локатор список, то ответ тоже будет списком
    """
    #p.add()
    return p
    # ПЕРЕПОЛНЕНИЯ БУФЕРА
    #json_product_addition_information = html2json(raw_html_product_addition_information)
    #raw_html_techical_details = html2json(raw_html_product_addition_information)

    ...

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