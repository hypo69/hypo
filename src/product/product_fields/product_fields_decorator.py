﻿## \file src/suppliers/product_fields_decorator.py
## \file ../src/product/product_fields/product_fields_decorator.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" 
@file src/suppliers/product_fields_decorator.py
Декоратор для функций заполнения полей в файле `graber.py` поставщика
"""
...
from functools import wraps
from src.logger.exceptions import ExecuteLocatorException
from src.logger import logger
from src.utils import pprint

def fetch_and_normalize(field_name: str, normalizer_func):
    """ Декоратор для извлечения данных с помощью `execute_locator` и их нормализации"""
    def decorator(func):
        @wraps(func)
        async def wrapper():
            if not getattr(f, field_name):
                try:
                    raw_data = d.execute_locator(l[field_name]) or ''
                    normalized_data = normalizer_func(raw_data)
                    setattr(f, field_name, normalized_data)
                except ExecuteLocatorException as ex:
                    logger.error(f"Error occurred while executing the locator for the field `{field_name}`: "
                                 f"response type: {type(response)}, response: {pprint(response)}", ex)
        return wrapper
    return decorator