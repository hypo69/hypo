## \file /src/suppliers/ivory/__morlevi__.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.ivory 
	:platform: Windows, Unix
	:synopsis:

"""


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
"""
  
""" module: src.suppliers.ivory """


"""    Supplier: morlevi


@namespace src: src
 \package src.suppliers.morlevi
\file __morlevi__.py
 
 @section libs imports:
  - pathlib 
  - requests 
  - pandas 
  - selenium.webdriver.remote.webelement 
  - selenium.webdriver.common.keys 
  - gs 
  - gs 
  - suppliers.Product 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""



from pathlib import Path
import requests
import pandas as pd


from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.keys import Keys

import settings 
from src.settings import StringFormatter
json_loads = settinsettings.json_loads
logger = settings.logger
from src.suppliers.Product import Product 



def login(supplier):
    _s = supplier
    _d = _s.driver
    _d.get_url('https://www.morlevi.co.il')
    if _login(_s): return True
    else: 

        try:
            '''
            закрываю модальные окна сайта
            выпадающие до входа
            '''
            logger.error( f''' Ошибка, пытаюсь закрыть popup''')
            _d.page_refresh()
            if _login(_s): return True




            

            close_pop_up_locator = _s.locators['login']['close_pop_up_locator']
            close_pop_up_btn = _d.execute_locator(close_pop_up_locator)
            _d.wait(5)

            if str(type(close_pop_up_btn)).execute_locator("class 'list'") >-1:  # Если появилось несколько
                for b in close_pop_up_btn:
                    try:
                        b.click()
                        if _login(_s) : 
                            
                            return True
                            break
                    except: ...
            if str(type(close_pop_up_btn)).execute_locator("webelement") >-1:  # нашелся только один элемент
                close_pop_up_btn.click()
                return _login(_s)
        except Exception as ex:
            logger.error(f''' 
            Не удалось залогиниться 
            ''')
            return

def _login(_s):
    logger.debug( f''' Собссно, логин Морлеви''')
    _s.driver.refresh()
    #self.driver.switch_to_active_element()
    _d = _s.driver
    _l : dict = _s.locators['login']
 
    try:
        
        _d.execute_locator(_['open_login_dialog_locator'])
        _d.wait(1.3)
        _d.execute_locator(_['email_locator'])
        _d.wait(.7)
        _d.execute_locator(_['password_locator'])
        _d.wait(.7)
        _d.execute_locator(_['loginbutton_locator'])
        logger.debug('Mor logged in')
        return True
    except Exception as ex:
        logger.error(f''' LOGIN ERROR 
        {ex.with_traceback(ex.__traceback__)}''')
        return

def grab_product_page(s):
    p = Product(supplier = s)
    _ : dict = s.locators['product']
    _d = s.driver
    _field = p.fields
    _s = s


    ''' морлеви может выкинуть модальное окно '''
    _d.click(s.locators['close_pop_up_locator'])

    
    
    def set_id():
        _id = _d.execute_locator(_['sku_locator'])
        if isinstance(_id,list):
            _field['id']=_id[0]
            _field['Rewritten URL'] = str(_id[1]).replace(' ','-')
    def set_sku_suppl():
        _field['sku suppl'] = _field['id']

    def set_sku_prod():
        _field['sku'] = str('mlv-') + _field['id']

    def set_title():
        _field['title'] = _d.title

    def set_summary():
        _field['summary'] = _d.execute_locator(_['summary_locator'])
        _field['meta description'] = _field['summary']

    def set_description():
        _field['description'] = _d.execute_locator(_['description_locator'])

    def set_cost_price():
        _price = _d.execute_locator(_['price_locator'])
        if  _price!=False:
            _price=_price.replace(',','')
            '''  Может прийти все, что угодно  '''
            _price = StringFormatter.clear_price(_price)
            _field['cost price'] =  round(eval(f'''{_price}{s.settings['price_rule']}'''))
        else:
           logger.error(f''' Not found price for ... ''')
           return
        return True
    def set_before_tax_price():
        _field['price tax excluded']  = _field['cost price']
     
        return True

    def set_delivery():
        '''TODO  перенести в комбинации '''
        #product_delivery_list = _d.execute_locator(_['product_delivery_locator'])
        #for i in product_delivery_list:
        #    ...


    def set_images(via_ftp=False):

        #_http_server = f'''http://davidka.esy.es/supplier_imgs/{_s.supplier_prefix}'''
        #_img_name = f'''{_field['sku']}.png'''
        #_field['img url'] =f'''{_http_server}/{_img_name}'''
        #screenshot = _d.execute_locator(_['main_image_locator'])
        #_s.save_and_send_via_ftp({_img_name:screenshot})
       
        _images = _d.execute_locator(_['main_image_locator'])
        if not _images: return
        _field['img url'] = _images

    def set_combinations():...

    def set_qty():...

    def set_specification():
        _field['specification']= _d.execute_locator(_['product_name_locator'])

    def set_customer_reviews():...

    def set_supplier():
        _field['supplier'] = '2784'
        ...

    def set_rewritted_URL():
        #_field['Rewritten URL'] = StringFormatter.set_rewritted_URL(_field['title'])
        ...
    set_id()
    set_sku_suppl()
    set_sku_prod()
    set_title()
    set_cost_price()
    set_before_tax_price()
    set_delivery()
    set_images()
    set_combinations()
    #set_qty()
    #set_byer_protection()
    set_description()
    set_summary()
    #set_specification()
    #set_customer_reviews()
    set_supplier()
    set_rewritted_URL()



    return p
    ...

def list_products_in_category_from_pagination(supplier):
    
    _s = supplier
    _d = _s.driver
    _l = _s.locators['product']['link_to_product_locator']

    list_products_in_category : list = []
    _product_list_from_page = _d.execute_locator(_l)
    ''' может вернуться или список адресов или строка или None 
    если нет товаров на странице на  данный момент'''
    if _product_list_from_page is None or not _product_list_from_page: 
        ''' нет смысла продожать. Нет товаров в категории 
        Возвращаю пустой список'''
        #logger.debug(f''' Нет товаров в категории по адресу {_d.current_url}''')
        return list_products_in_category

    if isinstance(_product_list_from_page,list):
        list_products_in_category.extend(_product_list_from_page)
    else:
        list_products_in_category.append(_product_list_from_page) 

    pages = _d.execute_locator(_s.locators['pagination']['a'])
    if isinstance(pages,list):
        for page in pages:
            _product_list_from_page = _d.execute_locator(_l)
            ''' может вернуться или список адресов или строка. '''
            if isinstance(_product_list_from_page,list):
                list_products_in_category.extend(_product_list_from_page)
            else:
                list_products_in_category.append(_product_list_from_page) 

            _perv_url = _d.current_url
            page.click()

            ''' дошел до конца листалки '''
            if _perv_url == _d.current_url:break


    if isinstance(list_products_in_category, list):
        list_products_in_category = list(set(list_products_in_category))
    return list_products_in_category

def get_list_products_in_category(s, scenario, presath):
    """
    s:Supplier
    scenario:JSON
    presath:PrestaShopWebServiceDict
    """
    l = list_products_in_category_from_pagination(s,scenario)
    ...

def get_list_categories_from_site(s,scenario_file,brand=''):
    ...