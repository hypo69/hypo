## \file /src/db/manager_translations/_experiments/ProductTranslationsManager.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_translations._experiments 
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
  
""" module: src.db.manager_translations._experiments """



""" @namespace src.db.manager_translations._experiments """
from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_
...
import header
from  src.db.translations import   ProductTranslationsManager

manager = ProductTranslationsManager()

ProductTranslation = manager.ProductTranslation

fields = {
    'product_reference': 'reference_product_value',
    'locale': 'en',
    'name': 'Product Name',
    'description': 'Description of the product',
    'link_rewrite': 'product-name'
}
# Instert record
#manager.insert_record(fields)



# Select records with a specific product reference
records = manager.select_record(product_reference='reference_product_value')
for record in records:
    print(record.name, record.description)

# # Select records with multiple conditions using logical OR
# records = manager.select_record(or_(
#     ProductTranslation.locale == 'en',
#     ProductTranslation.locale == 'ru'
# ))

def get_translations_from_presta_translations_table(product_reference: str, i18n: str = None) -> list:
    """
    This function returns a dictionary of translations for product fields.
    
    :param product_reference: The reference of the product.
    :param i18n: The language locale (optional).
    :returns: A list of product translations.
    """
    with ProductTranslationsManager() as translations_manager:
        search_filter = {'product_reference': product_reference}
        product_translations = translations_manager.select_record(**search_filter)
    return product_translations

d = get_translations_from_presta_translations_table('reference_product_value', 'he')
...