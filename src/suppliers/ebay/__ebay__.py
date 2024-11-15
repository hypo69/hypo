## \file hypotez/src/suppliers/ebay/__ebay__.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.ebay """
MODE = 'debug'
""" module: src.suppliers.ebay """
MODE = 'debug'
"""  [File's Description]

@namespace src: src
 \package src.suppliers.ebay
\file __ebay__.py
 
 @section libs imports:
  - pathlib 
  - selenium.webdriver.remote.webelement 
  - selenium.webdriver.common.keys 
  - gs 
  - gs 
  - gs 
  - suppliers.Product 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""


from pathlib import Path
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.keys import Keys
import settings 
import settings 
from src.settings import StringFormatter
json_loads = settinsettings.json_loads
from src.suppliers.Product import Product 
logger = settings.logger


def login(s):
    _d = s.driver
    _l : dict = s.locators['login']
    _d.get_url('https://ebay.com')
    _d.execute_locator(_l['open_login'])
    _d.wait(.7)
    _d.execute_locator(_l['user_id'])
    _d.wait(.7)
    _d.execute_locator(_l['button_continue_login'])
    _d.wait(.7)
    _d.execute_locator(_l['password'])
    _d.wait(.7)
    _d.execute_locator(_l['button_login'])
    _d.wait(.7)
    ...

def product_attributes(self, p, delimeter, elements):
    i=0
    skip = False
    c = p.combinations 
    ''' просто сокращенная запись '''
    for e in build_list_from_html_elements(self, delimeter, elements):
        if i%2 == 0:

            if not p.skip_row(e):
                '''
                -----^^^^^^^^^^   
                слова в колонке, которые надо пропустить находятся в файле
                PRESTA_product_combinations_syStringNormalizeronyms_<lg>.json['skip']
                '''
                i+=1
                skip = True
                continue

            attr = formatter.remove_HTML_tags(e)
            ''' первое значение '''
            if c["Attribute (Name:Type: Position)"] == "": c["Attribute (Name:Type: Position)"] = f'''{attr}:select:0'''
            else: c["Attribute (Name:Type: Position)"] += f''', {attr}:select:0'''
            ''' остальные значения '''
        else:
            if skip:
                i+=1        
                skip = False
                continue

            val = e.next
            if c["value (Name:Type: Position)"] == "":c["value (Name:Type: Position)"] = f'''{e.next}:select:0'''
            else: c["value (Name:Type: Position)"] += f''',{e.next}:select:0'''
        i+=1
        ...



def list_products_in_category_from_pagination(supplier,scenario):
    ''' листалка '''
    _s = supplier
    _d = _s.driver
    _l : dict = _s.locators['product']['link_to_product_locator']


    _d.scroll(prokrutok=1,direction='forward')

    list_products_in_category: list = _d.execute_locator(_l)
    '''@ВАЖНО! Здесь по сценарию я получаю не ссылки на странивы, а элененты
        на которырые надо нажимать '''
    
    if not list_products_in_category: return
    ''' В этой категории нет товаров. Это нормально '''
    
    while True:
        ''' листалка '''
        perv_url = _d.current_url
        _d.execute_locator(_s.locators['pagination']['->'])
        if perv_url == _d.current_url:
            ''' если больше некуда нажимать - выхожу '''
            break
        list_products_in_category.append(_d.execute_locator(_l))
   
            

    if isinstance(list_products_in_category,str):
        ''' если я получил всего один товар - возвращаю его списоком '''
        _ret:list = []
        _ret.append(list_products_in_category)
        return _ret
    else:
       return list_products_in_category

def get_list_products_in_category(s, scenario = None):
   return list_products_in_category_from_pagination(s,scenario)

def update_categories_in_scenario_file(supplier,current_scenario_filename):
    return Truee