## \file /src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.prestashop 
	:platform: Windows, Unix
	:synopsis:

"""


from types import SimpleNamespace
from typing import Optional
import header
from src.logger.logger import logger
from src.utils.printer import pprint
from .api import PrestaShop

class PrestaProduct(PrestaShop):
    """Класс товара из модуля PrestaShop.
    
    Непосредственно выполняет все операции через API.
    
    ------------------------------------
    Methods:
        check(product_reference: str): Проверка наличия товара в БД по product_reference (SKU, MKT).
            Вернет словарь товара, если товар есть, иначе False.
        search(filter: str, value: str): Расширенный поиск в БД по фильтрам.
        get(id_product): Возвращает информацию о товаре по ID.
    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """Инициализация товара PrestaShop.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.
        """
        
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        super().__init__(api_domain, api_key, *args, **kwards)
