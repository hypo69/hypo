## \file hypotez/src/endpoints/prestashop/pricelist.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop """
import sys
import os
from attr import attr, attrs
from pathlib import Path
from typing import Union
# ----------------------------------
from src import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop
# --------------------------------

class PriceListRequester(Prestashop):
    """
    Класс для запроса списка цен.

    Inherits:
        Prestashop
    """

    def __init__(self, api_credentials):
        """
        Инициализирует объект класса PriceListRequester.

        @param api_credentials: Словарь с учетными данными для API,
                                включая 'api_domain' и 'api_key'.
        """
        super().__init__(api_credentials['api_domain'], api_credentials['api_key'])

    def request_prices(self, products):
        """
        Запрашивает список цен для указанных товаров.

        @param products: Список товаров, для которых требуется получить цены.
        @return: Словарь, где ключами являются товары, а значениями - их цены.
                 Например: {'product1': 10.99, 'product2': 5.99}
        """
        # Здесь код для отправки запроса на получение цен из источника данных
        pass

    def update_source(self, new_source):
        """
        Обновляет источник данных для запроса цен.

        @param new_source: Новый источник данных.
        """
        self.source = new_source

    def modify_product_price(self, product, new_price):
        """
        Модифицирует цену указанного товара.

        @param product: Название товара.
        @param new_price: Новая цена товара.
        """
        # Здесь код для изменения цены товара в источнике данных
        pass

