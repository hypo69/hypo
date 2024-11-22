## \file hypotez/src/suppliers/aliexpress/_experiments/test_aliexpress_scenario.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress._experiments 
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
  
""" module: src.suppliers.aliexpress._experiments """




import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from pathlib import Path


# ----------------
from src import gs
from src.suppliers import Supplier
from src.product import Product
from categories import Category
from src.logger import logger



def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params)


supplier_prefix = 'aliexpress'
s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """



print(" Можно продолжать ")


test_scenario: dict = \
    {
        "iPhone 13 & 13 MINI": {
              "category ID on site": 40000002781737,
              "brand": "APPLE",
              "url": "https://hi5group.aliexpress.com/store/group/iPhone-13-13-mini/1053035_40000002781737.html",
              "active": True,
              "condition": "new",
              "presta_categories": {
                "template": {
                  "apple": "iPhone 13"
                }
              },
              "product combinations": [
                "bundle",
                "color"
              ]
            }
    }


test_products_list: list = ['https://s.click.aliexpress.com/e/_oFLpkfz', 
                            'https://s.click.aliexpress.com/e/_oE5V3d9', 
                            'https://s.click.aliexpress.com/e/_oDnvttN', 
                            'https://s.click.aliexpress.com/e/_olWWQCP', 
                            'https://s.click.aliexpress.com/e/_ok0xeMn']

def start_product():
    """ и категории и локаторы и product_fields нужны при инициализации класса Product для наглядности тестов 
    по умолачанию локаторы и так содержатся к классе `Supplier`
    """
    
    params: dict = \
    {
        'supplier':s,
        'webelements_locators':s.locators.get('product'),
        'product_categories':test_scenario['iPhone 13 & 13 MINI']['presta_categories'],
        #'product_fields':product_fields,
    }
    
    return Product(**params)

p = start_product()

d = s.driver
_ = d.execute_locator
f = p.fields
l = p.webelements_locators

d.get_url(test_products_list[0])

f.reference = d.current_url.split('/')[-1].split('.')[0]
f.price = _(l['price'])

if not p.check_if_product_in_presta_db(f.reference):
    p.add_2_PrestaShop(f)
...