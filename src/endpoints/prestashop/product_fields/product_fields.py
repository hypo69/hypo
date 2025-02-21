## \file /src/endpoints/prestashop/product_fields/product_fields.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
.. module:: endpoints.prestashop.product_fields.product_fields
	:platform: Windows, Unix
	:synopsis: Расписано каждое поле товара для таблиц престашоп"""

from __future__ import annotations
import asyncio
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional,  Any
from types import SimpleNamespace

import header
from header import __root__
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import read_text_file
from src.logger import logger
from src.logger.exceptions import ProductFieldException  # If you have this exception class


@dataclass
class ProductFields:
    """Класс, описывающий поля товара в формате API PrestaShop."""

    
    #product_fields_list: List[str] = field(init=False)
    presta_fields: SimpleNamespace = field(init=False)

    """ Индексы языков, которые я устанавливаю в бд престашоп:
    1. Английский
    2. Иврит
    3. Русский
    """
    id_lang: int

    base_path:Path = __root__ / 'src' / 'endpoints' / 'prestashop' 

    def __post_init__(self):
        """Инициализация класса после создания экземпляра. 
       """

             

    def _payload(self) -> bool:
        """
        Загрузка дефолтных значений полей.
        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """

        presta_fields_list:list =  read_text_file(self.base_path / 'product_fields' / 'fields_list.txt', as_list=True) 
        if not presta_fields_list:
            logger.error(f"Ошибка загрузки файла со списком полей ")
            ...
            return False

        try:
            self.presta_fields:SimpleNamespace = SimpleNamespace(**{key: None for key in presta_fields_list})
        except Exception as ex:
            logger.error(f"Ошибка конвертации", ex)
            ...
            return

        data_dict: dict = j_loads (self.base_path  / 'product_fields' / 'product_fields_default_values.json')
        if not data_dict:
            logger.debug(f"Ошибка загрузки полей из файла product_fields_default_values.json")
            ...
            return False
        try:
            for name, value in data_dict.items():
                setattr(self.presta_fields, name, value )
            return True
        except Exception as ex:
            logger.error(f"Exception ", ex)
            ...
            return False 


    # --------------------------------------------------------------------------
    #                  Язык
    # --------------------------------------------------------------------------

    @property
    def id_lang(self) -> int:
        """ property `id_lang: int(10)` 
        Индех языка для мультиязычных полей товара.
        """
        return self.id_lang

    @id_lang.setter
    def id_lang(self, value: int = 1):
        """ setter Индекс языка для мультиязычных полей товара."""
        self.id_lang = value



    # --------------------------------------------------------------------------
    #                  Поля таблицы ps_product
    # --------------------------------------------------------------------------




    @property
    def id_product(self) -> Optional[int]:
        """ property `ps_product.id_product: int(10) unsigned` """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int = None):
        """ setter `ID` товара. Для нового товара id назначается из `PrestaShop`. """
        try:
            self.presta_fields.id_product = value
        except Exception as ex:
            logger.error(f"Ошибка при установке id_product:",ex)

    @property
    def id_supplier(self) -> Optional[int]:
        """ property `ps_product.id_supplier: int(10) unsigned` """
        return self.presta_fields.id_supplier

    @id_supplier.setter
    def id_supplier(self, value: int = None):
        """ setter `ID` поставщика."""
        try:
            self.presta_fields.id_supplier = value
        except Exception as ex:
           logger.error(f"Ошибка при установке id_supplier:",ex)


    @property
    def id_manufacturer(self) -> Optional[int]:
        """ property `ps_product.id_manufacturer: int(10) unsigned` """
        return self.presta_fields.id_manufacturer

    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None):
        """ setter `ID` бренда."""
        try:
             self.presta_fields.id_manufacturer = value
        except Exception as ex:
             logger.error(f"Ошибка при установке id_manufacturer:",ex)

    @property
    def id_category_default(self) -> Optional[int]:
        """ property `ps_product.id_category_default: int(10) unsigned` """
        return self.presta_fields.id_category_default

    @id_category_default.setter
    def id_category_default(self, value: int):
        """ setter `ID` главной категории товара."""
        try:
            self.presta_fields.id_category_default = value
        except Exception as ex:
            logger.error(f"Ошибка при установке id_shop_default:",ex)

   
    @property
    def id_shop_default(self) -> Optional[int]:
        """ property `ps_product.id_shop_default: int(10) unsigned` """
        return self.presta_fields.id_shop_default

    @id_shop_default.setter
    def id_shop_default(self, value: int ):
        """ setter `ID` магазина по умолчанию."""
        try:
            self.presta_fields.id_shop_default = value or 1
        except Exception as ex:
            logger.error(f"Ошибка при установке id_shop_default:",ex)

    @property
    def id_shop(self) -> Optional[int]:
        """ property `ps_product.id_shop: int(10) unsigned` """
        return self.presta_fields.id_shop

    @id_shop.setter
    def id_shop(self, value: int):
        """ setter `ID` магазина (для multishop)."""
        try:
            self.presta_fields.id_shop = value or 1
        except Exception as ex:
             logger.error(f"Ошибка при установке id_shop:",ex)

    @property
    def id_tax(self) -> Optional[int]:
        """ property `ps_product.id_tax: int(11) unsigned` """
        return self.presta_fields.id_tax
    
    @id_tax.setter
    def id_tax(self, value: int):
         """ setter `ID` налога."""
        
         try:
            self.presta_fields.id_tax = value
         except Exception as ex:
            logger.error(f"Ошибка при установке id_tax:",ex)


    @property
    def on_sale(self) -> int:
        """ property `ps_product.on_sale: tinyint(1) unsigned` """
        return self.presta_fields.on_sale
    
    @on_sale.setter
    def on_sale(self, value: int ):
        """ setter Флаг распродажи."""
        self.presta_fields.on_sale = value

    @property
    def online_only(self) -> int:
        """ property `ps_product.online_only: tinyint(1) unsigned` """
        return self.presta_fields.online_only

    @online_only.setter
    def online_only(self, value: int|bool ):
        """ setter Флаг "только онлайн". """
        self.presta_fields.online_only = int(value)

    @property
    def ean13(self) -> Optional[str]:
        """ property `ps_product.ean13: varchar(13)` """
        return self.presta_fields.ean13

    @ean13.setter
    def ean13(self, value: str):
        """ setter EAN13 код товара."""
        self.presta_fields.ean13 = value

    @property
    def isbn(self) -> Optional[str]:
        """ property `ps_product.isbn: varchar(32)` """
        return self.presta_fields.isbn
    
    @isbn.setter
    def isbn(self, value: str):
        """ setter ISBN код товара."""
        self.presta_fields.isbn = value

    @property
    def upc(self) -> Optional[str]:
        """ property `ps_product.upc: varchar(12)` """
        return self.presta_fields.upc
    
    @upc.setter
    def upc(self, value: str):
        """ setter UPC код товара."""
        self.presta_fields.upc = value

    @property
    def mpn(self) -> Optional[str]:
        """ property `ps_product.mpn: varchar(40)` """
        return self.presta_fields.mpn
    
    @mpn.setter
    def mpn(self, value: str):
        """ setter MPN код товара."""
        self.presta_fields.mpn = value
   

    @property
    def ecotax(self) -> Optional[float]:
        """ property `ps_product.ecotax: decimal(17,6)` """
        return self.presta_fields.ecotax

    @ecotax.setter
    def ecotax(self, value: float = None):
        """ setter Эко налог."""
        self.presta_fields.ecotax = value

    @property
    def minimal_quantity(self) -> int:
         """ property `ps_product.minimal_quantity: int(10) unsigned` """
         return self.presta_fields.minimal_quantity

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 1):
        """ setter Минимальное количество товара для заказа."""
        self.presta_fields.minimal_quantity = value
   
    @property
    def low_stock_threshold(self) -> int:
        """ property `ps_product.low_stock_threshold: int(10)` """
        return self.presta_fields.low_stock_threshold

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: int):
        """ setter Пороговое значение для уведомления о низком запасе."""
        self.presta_fields.low_stock_threshold = value

    @property
    def low_stock_alert(self) -> int:
        """ property `ps_product.low_stock_alert: tinyint(1)` """
        return self.presta_fields.low_stock_alert

    @low_stock_alert.setter
    def low_stock_alert(self, value: int):
        """ setter Флаг уведомления о низком запасе."""
        self.presta_fields.low_stock_alert = value
  
    @property
    def price(self) -> float:
        """ property `ps_product.price: decimal(20,6)` """
        return self.presta_fields.price
    
    @price.setter
    def price(self, value: str | int | float):
        """ setter Цена товара."""
        try:
            self.presta_fields.price = float(value)
        except ValueError as ex:
            logger.error(f"Недопустимое значение для цены: {value}. Ошибка:",ex)
            return

    @property
    def wholesale_price(self) -> Optional[float]:
        """ property `ps_product.wholesale_price: decimal(20,6)` """
        return self.presta_fields.wholesale_price
    
    @wholesale_price.setter
    def wholesale_price(self, value: str | int | float):
        """ setter Оптовая цена."""
        self.presta_fields.wholesale_price = float(value)
    
    @property
    def unity(self) -> Optional[str]:
        """ property `ps_product.unity: varchar(255)` """
        return self.presta_fields.unity
    
    @unity.setter
    def unity(self, value: str):
        """ setter Единица измерения."""
        self.presta_fields.unity = value

    @property
    def unit_price_ratio(self) -> float:
        """ property `ps_product.unit_price_ratio: decimal(20,6)` """
        return self.presta_fields.unit_price_ratio

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float):
        """ setter Соотношение цены за единицу."""
        self.presta_fields.unit_price_ratio = value
   
    @property
    def additional_shipping_cost(self) -> float:
         """ property `ps_product.additional_shipping_cost: decimal(20,6)` """
         return self.presta_fields.additional_shipping_cost
    
    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: float):
        """ setter Дополнительная стоимость доставки."""
        self.presta_fields.additional_shipping_cost = value

    @property
    def reference(self) -> Optional[str]:
        """ property `ps_product.reference: varchar(64)` """
        return self.presta_fields.reference

    @reference.setter
    def reference(self, value: str):
        """ setter Артикул товара."""
        self.presta_fields.reference = value
    
    @property
    def supplier_reference(self) -> Optional[str]:
        """ property `ps_product.supplier_reference: varchar(64)` """
        return self.presta_fields.supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, value: str):
        """ setter Артикул поставщика."""
        self.presta_fields.supplier_reference = value

    @property
    def location(self) -> Optional[str]:
        """ property `ps_product.location: varchar(255)` """
        return self.presta_fields.location

    @location.setter
    def location(self, value: str):
        """ setter Местоположение товара на складе."""
        self.presta_fields.location = value

    @property
    def width(self) -> Optional[float]:
        """ property `ps_product.width: decimal(20,6)` """
        return self.presta_fields.width
    
    @width.setter
    def width(self, value: float = None):
        """ setter Ширина товара."""
        self.presta_fields.width = value

    @property
    def height(self) -> Optional[float]:
        """ property `ps_product.height: decimal(20,6)` """
        return self.presta_fields.height
    
    @height.setter
    def height(self, value: float = None):
        """ setter Высота товара."""
        self.presta_fields.height = value
    
    @property
    def depth(self) -> Optional[float]:
        """ property `ps_product.depth: decimal(20,6)` """
        return self.presta_fields.depth
    
    @depth.setter
    def depth(self, value: float = None):
        """ setter Глубина товара."""
        self.presta_fields.depth = value

    @property
    def weight(self) -> Optional[float]:
        """ property `ps_product.weight: decimal(20,6)` """
        return self.presta_fields.weight
   
    @weight.setter
    def weight(self, value: float = None):
        """ setter Вес товара."""
        self.presta_fields.weight = value
    
    @property
    def volume(self) -> Optional[str]:
        """ property `ps_product.volume: varchar(100)` """
        return self.presta_fields.volume
    
    @volume.setter
    def volume(self, value: str):
        """ setter Объем товара."""
        self.presta_fields.volume = value
    
    @property
    def out_of_stock(self) -> Optional[int]:
        """ property `ps_product.out_of_stock: int(10) unsigned` """
        return self.presta_fields.out_of_stock
    
    @out_of_stock.setter
    def out_of_stock(self, value: int = None):
        """ setter Действие при отсутствии товара на складе."""
        self.presta_fields.out_of_stock = value
    
    @property
    def additional_delivery_times(self) -> Optional[int]:
        """ property `ps_product.additional_delivery_times: tinyint(1) unsigned` """
        return self.presta_fields.additional_delivery_times
   
    @additional_delivery_times.setter
    def additional_delivery_times(self, value: int):
        """ setter Дополнительное время доставки."""
        self.presta_fields.additional_delivery_times = value
    
    @property
    def quantity_discount(self) -> Optional[int]:
        """ property `ps_product.quantity_discount: tinyint(1)` """
        return self.presta_fields.quantity_discount

    @quantity_discount.setter
    def quantity_discount(self, value: int):
        """ setter Флаг скидки на количество."""
        self.presta_fields.quantity_discount = value
    
    @property
    def customizable(self) -> Optional[int]:
        """ property `ps_product.customizable: tinyint(2)` """
        return self.presta_fields.customizable

    @customizable.setter
    def customizable(self, value: int):
        """ setter Флаг возможности кастомизации."""
        self.presta_fields.customizable = value

    @property
    def uploadable_files(self) -> Optional[int]:
        """ property `ps_product.uploadable_files: tinyint(4)` """
        return self.presta_fields.uploadable_files

    @uploadable_files.setter
    def uploadable_files(self, value: int):
        """ setter Флаг возможности загрузки файлов."""
        self.presta_fields.uploadable_files = value
    
    @property
    def text_fields(self) -> Optional[int]:
        """ property `ps_product.text_fields: tinyint(4)` """
        return self.presta_fields.text_fields

    @text_fields.setter
    def text_fields(self, value: int):
        """ setter Количество текстовых полей."""
        self.presta_fields.text_fields = value

    @property
    def active(self) -> Optional[int]:
        """ property `ps_product.active: tinyint(1) unsigned` """
        return self.presta_fields.active

    @active.setter
    def active(self, value: int = 1):
        """ setter Флаг активности товара."""
        self.presta_fields.active = value

    class EnumRedirect(Enum):
        """Перечисление для типов редиректов."""
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'

    @property
    def redirect_type(self) -> Optional[str]:
       """ property `ps_product.redirect_type: enum('404','301-product','302-product','301-category','302-category')` """
       return self.presta_fields.redirect_type

    @redirect_type.setter
    def redirect_type(self, value: EnumRedirect | str):
        """ setter Тип редиректа. """
        self.presta_fields.redirect_type = str(value)

    @property
    def id_type_redirected(self) -> Optional[int]:
        """ property `ps_product.id_type_redirected: int(10) unsigned` """
        return self.presta_fields.id_type_redirected

    @id_type_redirected.setter
    def id_type_redirected(self, value: int):
        """ setter ID связанного редиректа."""
        self.presta_fields.id_type_redirected = value

    @property
    def available_for_order(self) -> Optional[int]:
        """ property `ps_product.available_for_order: tinyint(1)` """
        return self.presta_fields.available_for_order
    
    @available_for_order.setter
    def available_for_order(self, value: int):
        """ setter Флаг доступности для заказа."""
        self.presta_fields.available_for_order = value

    @property
    def available_date(self) -> Optional[datetime]:
        """ property `ps_product.available_date: date` """
        return self.presta_fields.available_date

    @available_date.setter
    def available_date(self, value: datetime = datetime.now()):
         """ setter Дата доступности товара."""
         self.presta_fields.available_date = value
    
    @property
    def show_condition(self) -> Optional[int]:
        """ property `ps_product.show_condition: tinyint(1)` """
        return self.presta_fields.show_condition
    
    @show_condition.setter
    def show_condition(self, value: int = 1):
        """ setter Флаг отображения состояния товара."""
        self.presta_fields.show_condition = value

    class EnumCondition(Enum):
        """Перечисление для состояний товара."""
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'

    @property
    def condition(self) -> Optional[str]:
        """ property `ps_product.condition: enum('new','used','refurbished')` """
        return self.presta_fields.condition
    
    @condition.setter
    def condition(self, value: EnumCondition | str = EnumCondition.NEW):
         """ setter Состояние товара."""
         self.presta_fields.condition = str(value)

    @property
    def show_price(self) -> Optional[int]:
        """ property `ps_product.show_price: tinyint(1)` """
        return self.presta_fields.show_price
    
    @show_price.setter
    def show_price(self, value: int = 1):
        """ setter Флаг отображения цены."""
        self.presta_fields.show_price = value
    
    @property
    def indexed(self) -> Optional[int]:
        """ property `ps_product.indexed: tinyint(1)` """
        return self.presta_fields.indexed

    @indexed.setter
    def indexed(self, value: int = 1):
        """ setter Флаг индексации товара."""
        self.presta_fields.indexed = value

    class EnumVisibity(Enum):
        """Перечисление для видимости товара."""
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'

    @property
    def visibility(self) -> Optional[str]:
         """ property `ps_product.visibility: enum('both','catalog','search','none')` """
         return self.presta_fields.visibility
    
    @visibility.setter
    def visibility(self, value: EnumVisibity | str = EnumVisibity.BOTH):
        """ setter Видимость товара."""
        self.presta_fields.visibility = str(value)
    
    @property
    def cache_is_pack(self) -> Optional[int]:
        """ property `ps_product.cache_is_pack: tinyint(1)` """
        return self.presta_fields.cache_is_pack
    
    @cache_is_pack.setter
    def cache_is_pack(self, value: int = 1):
         """ setter Флаг кэширования как пакет товара."""
         self.presta_fields.cache_is_pack = value
    
    @property
    def cache_has_attachments(self) -> Optional[int]:
        """ property `ps_product.cache_has_attachments: tinyint(1)` """
        return self.presta_fields.cache_has_attachments

    @cache_has_attachments.setter
    def cache_has_attachments(self, value: int = 1):
         """ setter Флаг кэширования вложений."""
         self.presta_fields.cache_has_attachments = value

    @property
    def is_virtual(self) -> Optional[int]:
        """ property `ps_product.is_virtual: tinyint(1)` """
        return self.presta_fields.is_virtual
    
    @is_virtual.setter
    def is_virtual(self, value: int = 1):
        """ setter Флаг виртуального товара."""
        self.presta_fields.is_virtual = value
    
    @property
    def cache_default_attribute(self) -> Optional[int]:
        """ property `ps_product.cache_default_attribute: int(10) unsigned` """
        return self.presta_fields.cache_default_attribute

    @cache_default_attribute.setter
    def cache_default_attribute(self, value: int = 1):
        """ setter ID атрибута по умолчанию для кэширования."""
        self.presta_fields.cache_default_attribute = value
    
    @property
    def date_add(self) -> Optional[datetime]:
        """ property `ps_product.date_add: datetime` """
        return self.presta_fields.date_add
    
    @date_add.setter
    def date_add(self, value: datetime = datetime.now()):
        """ setter Дата добавления товара."""
        self.presta_fields.date_add = value

    @property
    def date_upd(self) -> Optional[datetime]:
        """ property `ps_product.date_upd: datetime` """
        return self.presta_fields.date_upd
    
    @date_upd.setter
    def date_upd(self, value: datetime = datetime.now()):
         """ setter Дата обновления товара."""
         self.presta_fields.date_upd = value

    @property
    def advanced_stock_management(self) -> Optional[int]:
        """ property `ps_product.advanced_stock_management: tinyint(1)` """
        return self.presta_fields.advanced_stock_management
    
    @advanced_stock_management.setter
    def advanced_stock_management(self, value: int):
         """ setter Флаг расширенного управления запасами."""
         self.presta_fields.advanced_stock_management = value
    
    @property
    def pack_stock_type(self) -> Optional[int]:
        """ property `ps_product.pack_stock_type: int(11) unsigned` """
        return self.presta_fields.pack_stock_type

    @pack_stock_type.setter
    def pack_stock_type(self, value: int):
        """ setter Тип управления запасами пакета товаров."""
        self.presta_fields.pack_stock_type = value
    
    @property
    def state(self) -> Optional[int]:
        """ property `ps_product.state: int(11) unsigned` """
        return self.presta_fields.state
   
    @state.setter
    def state(self, value: int):
        """ setter Состояние товара."""
        self.presta_fields.state = value

    class EnumProductType(Enum):
        """Перечисление для типов товаров."""
        STANDARD = 'standard'
        PACK = 'pack'
        VIRTUAL = 'virtual'
        COMBINATIONS = 'combinations'
        EMPTY = ''

    @property
    def product_type(self) -> Optional[str]:
        """ property `ps_product.product_type: enum('standard', 'pack', 'virtual', 'combinations', '')` """
        return self.presta_fields.product_type

    @product_type.setter
    def product_type(self, value: EnumProductType | str = EnumProductType.STANDARD):
        """ setter Тип товара."""
        self.presta_fields.product_type = str(value)
    
    # --------------------------------------------------------------------------
    #                Поля таблицы ps_product_lang
    # --------------------------------------------------------------------------

    @property
    def description(self) -> Optional[str]:
        """ property `ps_product_lang.description: text` """
        return self.presta_fields.description

    @description.setter
    def description(self, value: str):
        """ setter Описание товара. Мультиязычное поле. """
        try:
            _lang_index = str(self.lang_index)
            lang_dict = {'attrs': {'id': _lang_index}, 'value': value}

            if not hasattr(self.presta_fields, 'description') or not isinstance(self.presta_fields.description, dict) or 'language' not in self.presta_fields.description:
                # Если структура отсутствует, создаем ее в виде словаря
                self.presta_fields.description = {'language': lang_dict}
            else:
                language_list = self.presta_fields.description['language']
                
                # Проверяем, есть ли уже язык с таким ID
                found = False
                for i, lang_dict_existing in enumerate(language_list):
                    if lang_dict_existing['attrs']['id'] == _lang_index:
                        language_list[i]['value'] = value  # Заменяем значение
                        found = True
                        break
                
                # Если язык с таким ID не найден, добавляем его в список
                if not found:
                    language_list.append(lang_dict)
        except Exception as ex:
            logger.error(f"Ошибка при установке description: {ex}", exc_info=True)

    @property
    def description_short(self) -> Optional[str]:
         """ property `ps_product_lang.description_short: text` """
         return self.presta_fields.description_short
    
    @description_short.setter
    def description_short(self, value: str):
        """ setter Краткое описание товара. Мультиязычное поле."""
        try:
            self.presta_fields.description_short = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке description_short:",ex)

    @property
    def link_rewrite(self) -> Optional[str]:
         """ property `ps_product_lang.link_rewrite: varchar(128)` """
         return self.presta_fields.link_rewrite
    
    @link_rewrite.setter
    def link_rewrite(self, value: str):
        """ setter URL товара. Мультиязычное поле."""
        try:
             self.presta_fields.link_rewrite = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке link_rewrite:",ex)

    @property
    def meta_description(self) -> Optional[str]:
        """ property `ps_product_lang.meta_description: varchar(512)` """
        return self.presta_fields.meta_description
   
    @meta_description.setter
    def meta_description(self, value: str):
        """ setter Meta описание товара. Мультиязычное поле."""
        try:
             self.presta_fields.meta_description = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке meta_description:",ex)
    
    @property
    def meta_keywords(self) -> Optional[str]:
        """ property `ps_product_lang.meta_keywords: varchar(255)` """
        return self.presta_fields.meta_keywords
   
    @meta_keywords.setter
    def meta_keywords(self, value: str):
         """ setter Meta ключевые слова товара. Мультиязычное поле."""
         try:
            self.presta_fields.meta_keywords = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
         except Exception as ex:
             logger.error(f"Ошибка при установке meta_keywords:",ex)

    @property
    def meta_title(self) -> Optional[str]:
        """ property `ps_product_lang.meta_title: varchar(128)` """
        return self.presta_fields.meta_title
    
    @meta_title.setter
    def meta_title(self, value: str):
        """ setter Meta заголовок товара. Мультиязычное поле."""
        try:
            self.presta_fields.meta_title = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке meta_title:",ex)

    @property
    def name(self) -> Optional[str]:
         """ property `ps_product_lang.name: varchar(128)` """
         return self.presta_fields.name
    
    @name.setter
    def name(self, value: str):
        """ setter Название товара. Мультиязычное поле."""
        try:
            _lang_index:str = str(self.id_lang)
            lang_dict:dict = {'attrs': {'id': _lang_index}, 'value': value}

            if not hasattr(self.presta_fields, 'name') or not isinstance(self.presta_fields.name, dict) or 'language' not in self.presta_fields.name:
                # Если структура отсутствует, создаем ее в виде списка
                self.presta_fields.name:dict | list = {'language': lang_dict}
            else:
                language_list = self.presta_fields.name['language']

                if not language_list:  # Проверка на пустой список
                    self.presta_fields.name['language'] = lang_dict
                    return
                
                # Проверяем, есть ли уже язык с таким ID
                found = False
                for i, lang_dict_existing in enumerate(language_list):
                    if lang_dict_existing['attrs']['id'] == _lang_index:
                        language_list[i]['value'] = value  # Заменяем значение
                        found = True
                        break
                
                # Если язык с таким ID не найден, добавляем его в список
                if not found:
                    language_list.append(lang_dict)

        except Exception as ex:
            logger.error(f"Ошибка при установке name: {ex}", exc_info=True)


    @property
    def available_now(self) -> Optional[str]:
        """ property `ps_product_lang.available_now: varchar(255)` """
        return self.presta_fields.available_now

    @available_now.setter
    def available_now(self, value: str):
        """ setter Текст "в наличии". Мультиязычное поле."""
        try:
            self.presta_fields.available_now = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке available_now:",ex)

    @property
    def available_later(self) -> Optional[str]:
         """ property `ps_product_lang.available_later: varchar(255)` """
         return self.presta_fields.available_later

    @available_later.setter
    def available_later(self, value: str):
        """ setter Текст "ожидается". Мультиязычное поле."""
        try:
             self.presta_fields.available_later = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке available_later:",ex)

    @property
    def delivery_in_stock(self) -> Optional[str]:
        """ property `ps_product_lang.delivery_in_stock: varchar(255)` """
        return self.presta_fields.delivery_in_stock
    
    @delivery_in_stock.setter
    def delivery_in_stock(self, value: str):
        """ setter Текст доставки при наличии. Мультиязычное поле."""
        try:
            self.presta_fields.delivery_in_stock = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке delivery_in_stock:",ex)

    @property
    def delivery_out_stock(self) -> Optional[str]:
        """ property `ps_product_lang.delivery_out_stock: varchar(255)` """
        return self.presta_fields.delivery_out_stock
    
    @delivery_out_stock.setter
    def delivery_out_stock(self, value: str):
        """ setter Текст доставки при отсутствии. Мультиязычное поле."""
        try:
            self.presta_fields.delivery_out_stock = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке delivery_out_stock:",ex)

    @property
    def delivery_additional_message(self) -> Optional[str]:
         """ property `ps_product_lang.delivery_additional_message: tinytext` """
         return self.presta_fields.delivery_additional_message
   
    @delivery_additional_message.setter
    def delivery_additional_message(self, value: str):
        """ setter Дополнительное сообщение о доставке. Мультиязычное поле."""
        try:
            self.presta_fields.delivery_additional_message = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке delivery_additional_message:",ex)

    @property
    def affiliate_short_link(self) -> Optional[str]:
        """ property `ps_product_lang.affiliate_short_link: tinytext` """
        return self.presta_fields.affiliate_short_link

    @affiliate_short_link.setter
    def affiliate_short_link(self, value: str):
        """ setter Короткая ссылка аффилиата. Мультиязычное поле."""
        try:
            self.presta_fields.affiliate_short_link = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке affiliate_short_link:",ex)

    @property
    def affiliate_text(self) -> Optional[str]:
        """ property `ps_product_lang.affiliate_text: tinytext` """
        return self.presta_fields.affiliate_text
    
    @affiliate_text.setter
    def affiliate_text(self, value: str):
         """ setter Текст аффилиата. Мультиязычное поле."""
         try:
            self.presta_fields.affiliate_text = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
         except Exception as ex:
             logger.error(f"Ошибка при установке affiliate_text:",ex)
    
    @property
    def affiliate_summary(self) -> Optional[str]:
         """ property `ps_product_lang.affiliate_summary: tinytext` """
         return self.presta_fields.affiliate_summary
    
    @affiliate_summary.setter
    def affiliate_summary(self, value: str):
        """ setter Краткое описание аффилиата. Мультиязычное поле."""
        try:
           self.presta_fields.affiliate_summary = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке affiliate_summary:",ex)
    
    @property
    def affiliate_summary_2(self) -> Optional[str]:
        """ property `ps_product_lang.affiliate_summary_2: tinytext` """
        return self.presta_fields.affiliate_summary_2

    @affiliate_summary_2.setter
    def affiliate_summary_2(self, value: str):
        """ setter Второе краткое описание аффилиата. Мультиязычное поле."""
        try:
           self.presta_fields.affiliate_summary_2 = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке affiliate_summary_2:",ex)
  
    @property
    def affiliate_image_small(self) -> Optional[str]:
        """ property `ps_product_lang.affiliate_image_small: varchar(512)` """
        return self.presta_fields.affiliate_image_small
  
    @affiliate_image_small.setter
    def affiliate_image_small(self, value: str):
        """ setter Маленькое изображение аффилиата. Мультиязычное поле."""
        try:
           self.presta_fields.affiliate_image_small = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
           logger.error(f"Ошибка при установке affiliate_image_small:",ex)
    
    @property
    def affiliate_image_medium(self) -> Optional[str]:
        """ property `ps_product_lang.affiliate_image_medium: varchar(512)` """
        return self.presta_fields.affiliate_image_medium

    @affiliate_image_medium.setter
    def affiliate_image_medium(self, value: str):
        """ setter Среднее изображение аффилиата. Мультиязычное поле."""
        try:
            self.presta_fields.affiliate_image_medium = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
            logger.error(f"Ошибка при установке affiliate_image_medium:",ex)

    @property
    def affiliate_image_large(self) -> Optional[str]:
         """ property `ps_product_lang.affiliate_image_large: varchar(512)` """
         return self.presta_fields.affiliate_image_large
   
    @affiliate_image_large.setter
    def affiliate_image_large(self, value: str):
        """ setter Большое изображение аффилиата. Мультиязычное поле."""
        try:
            self.presta_fields.affiliate_image_large = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке affiliate_image_large:",ex)

    @property
    def ingredients(self) -> Optional[str]:
        """ property `ps_product_lang.ingredients: tinytext` """
        return self.presta_fields.ingredients

    @ingredients.setter
    def ingredients(self, value: str):
        """ setter Список ингридиентов. Мультиязычное поле."""
        try:
            self.presta_fields.ingredients = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке ingredients:",ex)
    
    @property
    def specification(self) -> Optional[str]:
         """ property `ps_product_lang.specification: tinytext` """
         return self.presta_fields.specification

    @specification.setter
    def specification(self, value: str):
        """ setter Спецификация товара. Мультиязычное поле."""
        try:
            self.presta_fields.specification = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке specification:",ex)
    
    @property
    def how_to_use(self) -> Optional[str]:
        """ property `ps_product_lang.how_to_use: tinytext` """
        return self.presta_fields.how_to_use
    
    @how_to_use.setter
    def how_to_use(self, value: str):
        """ setter Как использовать товар. Мультиязычное поле."""
        try:
             self.presta_fields.how_to_use = {'language': [{'attrs': {'id': self.id_lang}, 'value': value}]}
        except Exception as ex:
             logger.error(f"Ошибка при установке how_to_use:",ex)

    @property
    def id_default_image(self) -> Optional[int]:
        """ property `ps_product.id_default_image: int(10) unsigned` """
        return self.presta_fields.id_default_image
   
    @id_default_image.setter
    def id_default_image(self, value: int = None):
        """ setter ID изображения по умолчанию."""
        try:
           self.presta_fields.id_default_image = value
        except Exception as ex:
            logger.error(f"Ошибка при установке id_default_image:",ex)
    
    @property
    def link_to_video(self) -> Optional[str]:
        """ property `ps_product.link_to_video: varchar(255)` """
        return self.presta_fields.link_to_video if hasattr(self.presta_fields, 'link_to_video') else ""
    
    @link_to_video.setter
    def link_to_video(self, value: str):
         """ setter Ссылка на видео."""
         self.presta_fields.link_to_video = value



    @property
    def local_image_path(self) -> Optional[str]:
        """ property Путь к локальному изображению."""
        return self.local_image_path.local_image_path
   
    @local_image_path.setter
    def local_image_path(self, value: str):
        """ setter Устанавливает путь к локальному изображению."""
        self.presta_fields.local_image_path = value

    @property
    def local_video_path(self) -> Optional[str]:
        """ property Путь к локальному видео."""
        return self.presta_fields.local_video_path

    @local_video_path.setter
    def local_video_path(self, value: str):
        """ setter Устанавливает путь к локальному видео."""
        self.presta_fields.local_video_path = value

    @property
    def position_in_category(self) -> Optional[int]:
         """ property `ps_category_product.position: int(10) unsigned` """
         return self.presta_fields.position_in_category
    
    @position_in_category.setter
    def position_in_category(self, value:int = None):
        """ setter  Позиция товара в категории."""
        try:
            self.presta_fields.position_in_category = value
        except Exception as ex:
           logger.error(f'Ошибка при установке `position_in_category` {value} : ',ex)









    ########################################################################

    # self.presta_fields.associations

    ########################################################################

    def _ensure_associations(self):
        """Убеждается, что структура associations существует в presta_fields."""
        if not hasattr(self.presta_fields, 'associations'):
            self.presta_fields.associations = {}



    @property
    def additional_categories(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('categories') if hasattr(self.presta_fields, 'associations') else []

    def additional_category_append(self, category_id: int | str):
        """Добавляет связь с категорией, если ее еще нет."""
        
        self._ensure_associations()
        try:
            category_id = int(category_id)
        except (ValueError, Exception) as ex:
            logger.error("`category_id` должен быть `int`",ex)
            return


        if 'categories' not in self.presta_fields.associations:
            self.presta_fields.associations['categories']:list[dict] = []
        
        category_id_str = str(category_id)
        
        # проверяем есть ли уже такая категория
        if not any(d['id'] == category_id_str for d in self.presta_fields.associations['categories']):
            self.presta_fields.associations['categories'].append({'id': category_id_str})

    def additional_categories_clear(self):
        """Очищает все связи с категориями."""
        self._ensure_associations()
        if 'categories' in self.presta_fields.associations:
            del self.presta_fields.associations['categories']


    @property
    def product_images(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('images') if hasattr(self.presta_fields, 'images') else []

    def product_image_append(self, image_id: int):
        """Добавляет связь с изображением."""
        self._ensure_associations()
        if 'images' not in self.presta_fields.associations:
            self.presta_fields.associations['images'] = []
        self.presta_fields.associations['images'].append({'id': str(image_id)})

    def product_images_clear(self):
        """Очищает все связи с изображениями."""
        self._ensure_associations()
        if 'images' in self.presta_fields.associations:
            del self.presta_fields.associations['images']


    @property
    def images_urls(self) -> Optional[List[str]]:
        """ property Список URL дополнительных изображений."""
        return self.presta_fields.images_urls if hasattr(self.presta_fields, 'images_urls') else ""

    def images_urls_append(self, value: List[str] = None):
        """Устанавливает список URL, откуда скачать дополнительные изображения."""
        if value is None:
            return

        if not isinstance(value, list):
            logger.warning("images_urls_append: value должен быть списком строк.")
            return

        valid_urls = [url for url in value if isinstance(url, str) and url]  # Filter for valid strings

        if 'images_urls' not in self.assist_fields_dict:
             self.presta_fields.images_urls = []

        for url in valid_urls:
            if url not in self.assist_fields_dict['images_urls']: #  проверка на уникальность
                self.presta_fields.images_urls.append(url)

    def product_images_clear(self):
        """Очищает все связи с изображениями."""
        self._ensure_associations()
        if 'images_urls' in self.presta_fields.associations:
            del self.presta_fields.images_urls

    @property
    def product_combinations(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('combinations') if hasattr(self.presta_fields, 'combinations') else []

    def product_combination_append(self, combination_id: int):
        """Добавляет связь с комбинацией."""
        self._ensure_associations()
        if 'combinations' not in self.presta_fields.associations:
            self.presta_fields.associations['combinations'] = []
        self.presta_fields.associations['combinations'].append({'id': str(combination_id)})


    def product_combinations_clear(self):
        """Очищает все связи с комбинациями."""
        self._ensure_associations()
        if 'combinations' in self.presta_fields.associations:
            del self.presta_fields.associations['combinations']



    @property
    def product_options(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('product_option_values') if hasattr(self.presta_fields, 'product_option_values') else []

    def product_options_append(self, product_option_value_id: int):
        """Добавляет связь со значением опции продукта."""
        self._ensure_associations()
        if 'product_option_values' not in self.presta_fields.associations:
            self.presta_fields.associations['product_option_values'] = []
        self.presta_fields.associations['product_option_values'].append({'id': str(product_option_value_id)})

    def product_options_clear(self):
        """Очищает все связи со значениями опций продукта."""
        self._ensure_associations()
        if 'product_option_values' in self.presta_fields.associations:
            del self.presta_fields.associations['product_option_values']


    @property
    def product_product_features(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('product_features') if hasattr(self.presta_fields, 'product_features') else []

    def product_features_append(self, feature_id: int, feature_value_id: int):
        """Добавляет связь с характеристикой продукта."""
        self._ensure_associations()
        if 'product_features' not in self.presta_fields.associations:
            self.presta_fields.associations['product_features'] = []
        self.presta_fields.associations['product_features'].append(
            {'id': str(feature_id), 'id_feature_value': str(feature_value_id)}
        )

    def product_features_clear(self):
        """Очищает все связи с характеристиками продукта."""
        self._ensure_associations()
        if 'product_features' in self.presta_fields.associations:
            del self.presta_fields.associations['product_features']


    @property
    def product_product_tags(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('tags') if hasattr(self.presta_fields, 'tags') else []

    def product_tag_append(self, tag_id: int):
        """Добавляет связь с тегом."""
        self._ensure_associations()
        if 'tags' not in self.presta_fields.associations:
            self.presta_fields.associations['tags'] = []
        self.presta_fields.associations['tags'].append({'id': str(tag_id)})

    def product_tags_clear(self):
        """Очищает все связи с тегами."""
        self._ensure_associations()
        if 'tags' in self.presta_fields.associations:
            del self.presta_fields.associations['tags']

    @property
    def product_stock_availables(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('stock_availables') if hasattr(self.presta_fields, 'stock_availables') else []


    def product_stock_available_append(self, stock_available_id: int, product_attribute_id: int):
        """Добавляет связь с доступностью на складе."""
        self._ensure_associations()
        if 'stock_availables' not in self.presta_fields.associations:
            self.presta_fields.associations['stock_availables'] = []
        self.presta_fields.associations['stock_availables'].append(
            {'id': str(stock_available_id), 'id_product_attribute': str(product_attribute_id)}
        )

    def product_stock_availables_clear(self):
        """Очищает все связи с доступностью на складе."""
        self._ensure_associations()
        if 'stock_availables' in self.presta_fields.associations:
            del self.presta_fields.associations['stock_availables']

    @property
    def product_attachments(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('attachments') if hasattr(self.presta_fields, 'attachments') else []


    def product_attachment_append(self, attachment_id: int):
        """Добавляет связь с вложением."""
        self._ensure_associations()
        if 'attachments' not in self.presta_fields.associations:
            self.presta_fields.associations['attachments'] = []
        self.presta_fields.associations['attachments'].append({'id': str(attachment_id)})

    def product_attachments_clear(self):
        """Очищает все связи с вложениями."""
        self._ensure_associations()
        if 'attachments' in self.presta_fields.associations:
            del self.presta_fields.associations['attachments']

    @property
    def product_accessories(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('accessories') if hasattr(self.presta_fields, 'accessories') else []

    def product_accessory_append(self, accessory_id: int):
        """Добавляет связь с аксессуаром."""
        self._ensure_associations()
        if 'accessories' not in self.presta_fields.associations:
            self.presta_fields.associations['accessories'] = []
        self.presta_fields.associations['accessories'].append({'id': str(accessory_id)})

    def product_accessories_clear(self):
        """Очищает все связи с аксессуарами."""
        self._ensure_associations()
        if 'accessories' in self.presta_fields.associations:
            del self.presta_fields.associations['accessories']

    @property
    def product_bundle(self) -> Optional[List[dict]]:
        """"""
        return self.presta_fields.associations.get('product_bundle') if hasattr(self.presta_fields, 'product_bundle') else []

    def product_bundle_append(self, bundle_id: int, product_attribute_id: int, quantity: int):
        """Добавляет связь с бандлом продукта."""
        self._ensure_associations()
        if 'product_bundle' not in self.presta_fields.associations:
            self.presta_fields.associations['product_bundle'] = []
        self.presta_fields.associations['product_bundle'].append(
            {'id': str(bundle_id), 'id_product_attribute': str(product_attribute_id), 'quantity': str(quantity)}
        )

    def product_bundle_clear(self):
        """Очищает все связи с бандлами продуктов."""
        self._ensure_associations()
        if 'product_bundle' in self.presta_fields.associations:
            del self.presta_fields.associations['product_bundle']

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует объект ProductFields в словарь для PrestaShop API,
        исключая ключи, значения которых равны None или пустой строке,
        и формирует мультиязычные поля в нужном формате. Все поля должны быть представлены как строки.

        Returns:
            Dict[str, Any]: Словарь с полями, готовый для PrestaShop API.
        """
        product_dict = {}

        # -- ps_product fields --
        def str_val(value: Any) -> Optional[str]:
            """Helper function to convert values to strings, handling None."""
            return str(value) if value is not None else None

        if self.id_product is not None:
            product_dict["id_product"] = str_val(self.id_product)
        if self.id_supplier is not None:
            product_dict["id_supplier"] = str_val(self.id_supplier)
        if self.id_manufacturer is not None:
            product_dict["id_manufacturer"] = str_val(self.id_manufacturer)
        if self.id_category_default is not None:
            product_dict["id_category_default"] = str_val(self.id_category_default)
        if self.id_shop_default is not None:
            product_dict["id_shop_default"] = str_val(self.id_shop_default)
        if self.id_shop is not None:
            product_dict["id_shop"] = str_val(self.id_shop)
        if self.id_tax is not None:
            product_dict["id_tax"] = str_val(self.id_tax)
        if self.on_sale is not None:
            product_dict["on_sale"] = str_val(self.on_sale)
        if self.online_only is not None:
            product_dict["online_only"] = str_val(self.online_only)
        if self.ean13:
            product_dict["ean13"] = str_val(self.ean13)
        if self.isbn:
            product_dict["isbn"] = str_val(self.isbn)
        if self.upc:
            product_dict["upc"] = str_val(self.upc)
        if self.mpn:
            product_dict["mpn"] = str_val(self.mpn)
        if self.ecotax:
            product_dict["ecotax"] = str_val(self.ecotax)
        if self.minimal_quantity:
            product_dict["minimal_quantity"] = str_val(self.minimal_quantity)
        if self.low_stock_threshold:
            product_dict["low_stock_threshold"] = str_val(self.low_stock_threshold)
        if self.low_stock_alert:
            product_dict["low_stock_alert"] = str_val(self.low_stock_alert)
        if self.price:
            product_dict["price"] = str_val(self.price)
        if self.wholesale_price:
            product_dict["wholesale_price"] = str_val(self.wholesale_price)
        if self.unity:
            product_dict["unity"] = str_val(self.unity)
        if self.unit_price_ratio:
            product_dict["unit_price_ratio"] = str_val(self.unit_price_ratio)
        if self.additional_shipping_cost:
            product_dict["additional_shipping_cost"] = str_val(self.additional_shipping_cost)
        if self.reference:
            product_dict["reference"] = str_val(self.reference)
        if self.supplier_reference:
            product_dict["supplier_reference"] = str_val(self.supplier_reference)
        if self.location:
            product_dict["location"] = str_val(self.location)
        if self.width:
            product_dict["width"] = str_val(self.width)
        if self.height:
            product_dict["height"] = str_val(self.height)
        if self.depth:
            product_dict["depth"] = str_val(self.depth)
        if self.weight:
            product_dict["weight"] = str_val(self.weight)
        if self.volume:
            product_dict["volume"] = str_val(self.volume)
        if self.out_of_stock:
            product_dict["out_of_stock"] = str_val(self.out_of_stock)
        if self.additional_delivery_times:
            product_dict["additional_delivery_times"] = str_val(self.additional_delivery_times)
        if self.quantity_discount:
            product_dict["quantity_discount"] = str_val(self.quantity_discount)
        if self.customizable:
            product_dict["customizable"] = str_val(self.customizable)
        if self.uploadable_files:
            product_dict["uploadable_files"] = str_val(self.uploadable_files)
        if self.text_fields:
            product_dict["text_fields"] = str_val(self.text_fields)
        if self.active is not None:
            product_dict["active"] = str_val(self.active)
        if self.redirect_type:
            product_dict["redirect_type"] = str_val(self.redirect_type)
        if self.id_type_redirected:
            product_dict["id_type_redirected"] = str_val(self.id_type_redirected)
        if self.available_for_order is not None:
            product_dict["available_for_order"] = str_val(self.available_for_order)
        if self.available_date:
            product_dict["available_date"] = str_val(self.available_date.isoformat() if isinstance(self.available_date,datetime) else self.available_date)
        if self.show_condition is not None:
            product_dict["show_condition"] = str_val(self.show_condition)
        if self.condition:
            product_dict["condition"] = str_val(self.condition)
        if self.show_price is not None:
            product_dict["show_price"] = str_val(self.show_price)
        if self.indexed is not None:
            product_dict["indexed"] = str_val(self.indexed)
        if self.visibility:
            product_dict["visibility"] = str_val(self.visibility)
        if self.cache_is_pack is not None:
            product_dict["cache_is_pack"] = str_val(self.cache_is_pack)
        if self.cache_has_attachments is not None:
            product_dict["cache_has_attachments"] = str_val(self.cache_has_attachments)
        if self.is_virtual is not None:
            product_dict["is_virtual"] = str_val(self.is_virtual)
        if self.cache_default_attribute:
            product_dict["cache_default_attribute"] = str_val(self.cache_default_attribute)
        if self.date_add:
           product_dict["date_add"] = str_val(self.date_add.isoformat() if isinstance(self.date_add,datetime) else self.date_add)
        if self.date_upd:
           product_dict["date_upd"] = str_val(self.date_upd.isoformat()  if isinstance(self.date_upd,datetime) else self.date_upd)
        if self.advanced_stock_management is not None:
            product_dict["advanced_stock_management"] = str_val(self.advanced_stock_management)
        if self.pack_stock_type:
            product_dict["pack_stock_type"] = str_val(self.pack_stock_type)
        if self.state:
            product_dict["state"] = str_val(self.state)
        if self.product_type:
            product_dict["product_type"] = str_val(self.product_type)
        if self.id_default_image:
            product_dict["id_default_image"] = str_val(self.id_default_image)

        # -- ps_product_lang fields --
        if self.description:
            product_dict["description"] = self._format_multilang_value(self.description)
        if self.description_short:
            product_dict["description_short"] = self._format_multilang_value(self.description_short)
        if self.link_rewrite:
            product_dict["link_rewrite"] = self._format_multilang_value(self.link_rewrite)
        if self.meta_description:
            product_dict["meta_description"] = self._format_multilang_value(self.meta_description)
        if self.meta_keywords:
            product_dict["meta_keywords"] = self._format_multilang_value(self.meta_keywords)
        if self.meta_title:
            product_dict["meta_title"] = self._format_multilang_value(self.meta_title)
        if self.name:
            product_dict["name"] = self._format_multilang_value(self.name)
        if self.available_now:
            product_dict["available_now"] = self._format_multilang_value(self.available_now)
        if self.available_later:
            product_dict["available_later"] = self._format_multilang_value(self.available_later)
        if self.delivery_in_stock:
            product_dict["delivery_in_stock"] = self._format_multilang_value(self.delivery_in_stock)
        if self.delivery_out_stock:
            product_dict["delivery_out_stock"] = self._format_multilang_value(self.delivery_out_stock)
        if self.delivery_additional_message:
            product_dict["delivery_additional_message"] = self._format_multilang_value(self.delivery_additional_message)
        if self.affiliate_short_link:
            product_dict["affiliate_short_link"] = self._format_multilang_value(self.affiliate_short_link)
        if self.affiliate_text:
            product_dict["affiliate_text"] = self._format_multilang_value(self.affiliate_text)
        if self.affiliate_summary:
            product_dict["affiliate_summary"] = self._format_multilang_value(self.affiliate_summary)
        if self.affiliate_summary_2:
            product_dict["affiliate_summary_2"] = self._format_multilang_value(self.affiliate_summary_2)
        if self.affiliate_image_small:
            product_dict["affiliate_image_small"] = self._format_multilang_value(self.affiliate_image_small)
        if self.affiliate_image_medium:
            product_dict["affiliate_image_medium"] = self._format_multilang_value(self.affiliate_image_medium)
        if self.affiliate_image_large:
            product_dict["affiliate_image_large"] = self._format_multilang_value(self.affiliate_image_large)
        if self.ingredients:
            product_dict["ingredients"] = self._format_multilang_value(self.ingredients)
        if self.specification:
            product_dict["specification"] = self._format_multilang_value(self.specification)
        if self.how_to_use:
            product_dict["how_to_use"] = self._format_multilang_value(self.how_to_use)

        # -- service fields

        # if self.images_urls:
        #     product_dict["images_urls"] = [str_val(url) for url in self.images_urls] if isinstance(self.images_urls, list) else str_val(self.images_urls)
        # if self.position_in_category:
        #     product_dict["position_in_category"] = str_val(self.position_in_category)
        # if self.link_to_video:
        #     product_dict["link_to_video"] = str_val(self.link_to_video)




        # Добавление associations, если они есть
        associations_dict = {}
        if hasattr(self.presta_fields, 'associations') and self.presta_fields.associations:

            if 'categories' in self.presta_fields.associations and self.presta_fields.associations['categories']:
                associations_dict['categories'] = [{'id': str_val(cat['id'])} for cat in self.presta_fields.associations['categories']]
            if 'images' in self.presta_fields.associations and self.presta_fields.associations['images']:
                associations_dict['images'] = [{'id': str_val(img['id'])} for img in self.presta_fields.associations['images']]
            if 'combinations' in self.presta_fields.associations and self.presta_fields.associations['combinations']:
                associations_dict['combinations'] = [{'id': str_val(comb['id'])} for comb in self.presta_fields.associations['combinations']]
            if 'product_option_values' in self.presta_fields.associations and self.presta_fields.associations['product_option_values']:
                associations_dict['product_option_values'] = [{'id': str_val(val['id'])} for val in self.presta_fields.associations['product_option_values']]
            if 'product_features' in self.presta_fields.associations and self.presta_fields.associations['product_features']:
                associations_dict['product_features'] = [{'id': str_val(feat['id']), 'id_feature_value': str_val(feat['id_feature_value'])} for feat in self.presta_fields.associations['product_features']]
            if 'tags' in self.presta_fields.associations and self.presta_fields.associations['tags']:
                associations_dict['tags'] = [{'id': str_val(tag['id'])} for tag in self.presta_fields.associations['tags']]
            if 'stock_availables' in self.presta_fields.associations and self.presta_fields.associations['stock_availables']:
                associations_dict['stock_availables'] = [{'id': str_val(stock['id']), 'id_product_attribute': str_val(stock['id_product_attribute'])} for stock in self.presta_fields.associations['stock_availables']]
            if 'attachments' in self.presta_fields.associations and self.presta_fields.associations['attachments']:
                associations_dict['attachments'] = [{'id': str_val(attach['id'])} for attach in self.presta_fields.associations['attachments']]
            if 'accessories' in self.presta_fields.associations and self.presta_fields.associations['accessories']:
                associations_dict['accessories'] = [{'id': str_val(acc['id'])} for acc in self.presta_fields.associations['accessories']]
            if 'product_bundle' in self.presta_fields.associations and self.presta_fields.associations['product_bundle']:
                associations_dict['product_bundle'] = [{'id': str_val(bundle['id']), 'id_product_attribute': str_val(bundle['id_product_attribute']), 'quantity': str_val(bundle['quantity'])} for bundle in self.presta_fields.associations['product_bundle']]

            if associations_dict:  # Только если есть что добавлять, добавляем ключ associations
                product_dict["associations"] = associations_dict

        return product_dict

    def _format_multilang_value(self, data: Any) -> List[Dict[str, str]]:
        """
        Форматирует мультиязычные значения в список словарей для PrestaShop API. Все значения представляются как строки.

        Args:
            data (Any): Значение поля. Если это словарь, ожидается структура {'language': [{'attrs': {'id': lang_id}, 'value': value}]}

        Returns:
            List[Dict[str, str]]: Список словарей, где каждый словарь содержит 'id' и 'value' (все как строки) для каждого языка.
        """
        result = []
        if isinstance(data, dict) and 'language' in data:
            for lang_dict in data['language']:
                lang_id = lang_dict['attrs']['id']
                lang_value = lang_dict['value']
                result.append({"id": str(lang_id), "value": str(lang_value)})
        else:
            # Fallback: Create a list with one entry for the current language
            result.append({"id": str(self.id_lang), "value": str(data)})
        return result