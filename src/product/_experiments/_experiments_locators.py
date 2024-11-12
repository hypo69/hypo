## \file hypotez/src/product/_experiments/_experiments_locators.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.product._experiments """
import header
from header import ProductFieldsLocators, gs, j_dumps, j_loads
from pathlib import Path

# Пример использования
file_path = Path(gs.path.src,'suppliers', 'hb', 'locators','product.json')    
product_fields_locators = ProductFieldsLocators(file_path)
print(product_fields_locators.get_attribute("condition", "attribute"))  # Выводит значение атрибута "attribute" для ключа "condition"
print(product_fields_locators.get_attribute("default_image_url", "selector"))  # Выводит значение атрибута "selector" для ключа "default_image_url"

