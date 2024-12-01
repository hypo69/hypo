## \file hypotez/src/product/product_fields/product_fields.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.product.product_fields 
	:platform: Windows, Unix
	:synopsis: Расписано каждое поле товара для таблиц престашоп

 <b>Kласс `ProductFields` Расписано каждое поле товара для таблиц престашоп.</b> 
langdetect в Python используется для определения языка текста. Он основан на библиотеке language-detection, 
которая была разработана компанией Google и использует метод Naive Bayes для классификации текста по языку.

------

Вот пример того, как использовать langdetect для определения языка текста:

.. code-block:: python

    from langdetect import detect, detect_langs

    # Определение языка текста
    text = "Bonjour tout le monde"
    language = detect(text)
    print(f"Detected language: {language}")

    # Определение вероятностей нескольких языков
    languages = detect_langs(text)
    print(f"Detected languages: {languages}")

.. code-block:: python

    from langdetect import detect, detect_langs, LangDetectException

    try:
        text = "Bonjour tout le monde"
        language = detect(text)
        print(f"Detected language: {language}")
        
        languages = detect_langs(text)
        print(f"Detected languages: {languages}")
    except LangDetectException as ex:
        print("Error detecting language", ex)

.. todo:: Внимательно посмотреть, как работает langdetect
"""

"""
Наименование полей в классе соответствуют именам полей в таблицах `PrestaShop`
Порядок полей в этом файле соответствует номерам полей в таблице, 
В коде программы в дальнейшем я использую алфавитный порядок

.. image:: ps_model.png

### product filelds in PrestaShop db 
-------------------------------------------

      `ps_product`

          Column Name                 Data Type	            Allowed NULL
  1	    `id_product`                int(10) unsigned	    [V]
  2       `id_supplier`               int(10) unsigned	    [V]
  3       `id_manufacturer`           int(10) unsigned	    [v]
  4       `id_category_default`       int(10) unsigned	    [v]
  5       `id_shop_default`           int(10) unsigned        [v]
  6       `id_tax`	    int(11) unsigned        [v]
  7       `on_sale`                   tinyint(1) unsigned     [v]
  8       `online_only`               tinyint(1) unsigned     [v]
  9       `ean13`                     varchar(13)             [v]
  10      `isbn`                      varchar(32)
  11      `upc`                       varchar(12)
  12      `mpn`                       varchar(40)
  13	    `ecotax`                    decimal(17,6)
  14      `quantity`                  int(10)
  15      `minimal_quantity`          int(10) unsigned
  16      `low_stock_threshold`       int(10)
  17      `low_stock_alert`           tinyint(1)
  18      `price`                     decimal(20,6)
  19      `wholesale_price`           decimal(20,6)
  20      `unity`                     varchar(255)
  21      `unit_price_ratio`          decimal(20,6)
  22      `additional_shipping_cost`  decimal(20,6)
  23      `reference`                 varchar(64)
  24      `supplier_reference`        varchar(64)
  25      `location`                  varchar(255)
  26      `width`                     decimal(20,6)
  27      `height`                    decimal(20,6)
  28      `depth`                     decimal(20,6)
  29      `weight`                    decimal(20,6)
  30      `volume`                    varchar(100)
  31      `out_of_stock`              int(10) unsigned
  32      `additional_delivery_times` tinyint(1) unsigned # Совершенно непонятное поле
  33      `quantity_discount`         tinyint(1)
  34      `customizable`              tinyint(2)
  35      `uploadable_files`          tinyint(4)
  36      `text_fields`               tinyint(4)
  37      `active`                    tinyint(1) unsigned
  38      `redirect_type`             enum('404','301-product','302-product','301-category','302-category')
  39      `id_type_redirected`        int(10) unsigned
  40      `available_for_order`       tinyint(1)          # если товара нет в наличии у поставщика выставляю флаг в 0
  41      `available_date`            date
  42      `show_condition`            tinyint(1)
  43      `condition`                 enum('new','used','refurbished')
  44      `show_price`                tinyint(1)
  45      `indexed`                   tinyint(1)
  46      `visibility`                enum('both','catalog','search','none')
  47      `cache_is_pack`             tinyint(1)
  48      `cache_has_attachments`     tinyint(1)
  49      `is_virtual`                tinyint(1)
  50      `cache_default_attribute`   int(10) unsigned
  51      `date_add`                  datetime
  52      `date_upd`                  datetime
  53      `advanced_stock_management` tinyint(1)
  54      `pack_stock_type`           int(11) unsigned
  55      `state`                     int(11) unsigned
  56      `product_type`              enum('standard','pack','virtual','combinations','')
  57      `link_to_video`             varchar(255) 
  
----------

empty fields template
            f.active = 1
            f.additional_categories = None
            f.active = None
            f.additional_delivery_times = None
            f.additional_shipping_cost = None
            f.advanced_stock_management = None
            f.affiliate_short_link = None
            f.affiliate_summary = None
            f.affiliate_summary_2 = None
            f.affiliate_text = None
            f.affiliate_image_large = None
            f.affiliate_image_medium = None
            f.affiliate_image_small = None
            f.associations = None
            f.available_date = None
            f.available_for_order
            f.available_later = None
            f.available_now = None
            f.cache_default_attribute = None
            f.cache_has_attachments = None
            f.cache_is_pack = None
            f.condition = None
            f.customizable = None
            f.date_add = None
            f.date_upd = None
            f.delivery_in_stock = None
            f.delivery_out_stock = None
            f.depth = None
            f.description = None
            f.description_short = None
            f.ean13 = None
            f.ecotax = None
            f.height = None
            f.how_to_use = None
            f.specification = None
            f.id_category_default = None
            f.id_default_combination = None
            f.id_default_image = None
            f.locale = None
            f.id_manufacturer = None
            f.id_product = None
            f.id_shop_default = None
            f.id_shop = None
            f.id_product = None
            f.id_supplier = None
            f.id_tax = None
            f.id_type_redirected = None
            f.indexed = None
            f.ingredients = None
            f.images_urls = None
            f.is_virtual = None
            f.isbn = None
            f.link_rewrite = None
            f.location = None
            f.low_stock_alert = None
            f.low_stock_threshold = None
            f.meta_description = None
            f.meta_keywords = None
            f.meta_title = None
            f.minimal_quantity = None
            f.mpn = None
            f.name = None
            f.online_only = None
            f.on_sale = None
            f.out_of_stock = None
            f.pack_stock_type = None
            #'position_in_category = None  # <- Нельзя оставлять пустым Функция закомментриована
            f.price = None
            f.product_type = None
            #'quantity = None      # <- НЕЛЬЗЯ ПЕРЕДАВАТЬ ЗНАЧЕНИЕ. 
            f.quantity_discount = None
            f.redirect_type = None
            f.reference = None
            f.show_condition = None
            f.show_price = None
            f.specification = None
            f.state = None
            f.supplier_reference = None
            f.text_fields = None
            f.unit_price_ratio = None
            f.unity = None
            f.upc = None
            f.uploadable_files = None
            f.visibility = None
            f.volume = None
            f.weight = None
            f.wholesale_price = None
            f.width = None
"""

MODE = 'dev'
from pathlib import Path
from typing import List, Dict, Optional, Callable, Any
from pydantic import BaseModel, Field, validator
from types import SimpleNamespace, MappingProxyType
from sqlite3 import Date
from langdetect import detect
from functools import wraps
from enum import Enum

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.category import Category
from src.utils.string import StringFormatter as sf
from src.utils.file import read_text_file
from src.logger import logger
from src.logger.exceptions import ProductFieldException 

"""Класс, описывающий поля товара в формате API PrestaShop."""
import header
from src.logger import logger
from src.utils.jjson import j_loads
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional

class ProductFields:
    """Класс, описывающий поля товара в формате API PrestaShop."""

    def __init__(self):
        """
        Инициализация класса. Загружаются данные полей, языков и их идентификаторов.
        """
        self.product_fields_list = self._load_product_fields_list()
        self.language = {'en': 1, 'he': 2, 'ru': 3}
        # TODO: изменить логику так, чтобы словарь языков получался из presatshop клиента 

        self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})
        self.assist_fields_dict = {
            'default_image_url': '', 
            'images_urls': []
        }
        self._payload()

    def _load_product_fields_list(self) -> List[str]:
        """
        Загрузка списка полей из файла.

        Returns:
            List[str]: Список полей, загруженных из текстового файла.
        """
        return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)

    def _payload(self) -> bool:
        """
        Загрузка дефолтных значений полей.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))
        if not data:
            logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
            return False
        for name, value in data.items():
            setattr(self, name, value)
        return True


    @property
    def associations(self) -> Optional[Dict]:
        """Возвращает словарь ключей ассоциаций."""
        return self.presta_fields.associations or None

    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]):
        """Устанавливает словарь ассоциаций."""
        self.presta_fields.associations = value

    
    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]):
        """  <sub>*[setter]*</sub>  Словарь ассоциаций. Список ассоциаций: """
        self.presta_fields.associations = value

    @property    
    def id_product(self) -> Optional[int]:
        """ <sub>*[property]*</sub>  `ps_product.id: int(10) unsigned` """
        return self.presta_fields.id_product

    
    @id_product.setter     
    def id_product(self, value: int = None):
        """  <sub>*[setter]*</sub>  `ID` товара. *для нового тoвара id назначется из `PrestaShop`*
        @details Запись нового товара в престашоп делается в два шага:
        -> в престасшоп заносятся парамеры, которые не связаны с ID, например, название товара, артикул и т.п. 
        <- От престашоп возвращается словарь, в котором установлено ID. 
        -> теперь можно грузить фото, доп парамерты, короче все, что завязано на id товара
        @param id_product `int`  :  Требуется при операциях над существующим товаром. `ps_product.id` .  
        Для нового товара ID вернется из системы при занесении товара в базу данных.
        @returns bool `True` if success, else `False`
        """
        try:
            self.presta_fields.id_product = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
            Ошибка: """, ex)
            return


#   2   Поставщик
    @property
    def id_supplier(self):
        """  <sub>*[property]*</sub>  `ps_product.id_supplier: int(10) unsigned`
         @details: привязываю товар к id поставщика
        """
        return self.presta_fields.id_supplier or None
    
    
    @id_supplier.setter
    def id_supplier(self, value: int = None):
        """  <sub>*[setter]*</sub> """
        
        try:
            self.presta_fields.id_supplier = value
            return True

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: `ps_product.id_supplier` данными {value}
            Ошибка: """, ex)
            return


#   3   Бренд
    
    @property
    def id_manufacturer(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.id_manufacturer: int(10) unsigned`
        field
         @details: means BRAND. 
            Бренд может быть передан как по имени так и по ID.
            Таблица брендов:

            """

        return self.presta_fields.id_manufacturer or None
    
    
    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None):
        """  <sub>*[setter]*</sub>  Бренд может быть передан как по имени так и по ID 

         `ps_product.id_manufacturer`
        field type: int(10) unsigned
         @details: привязываю товар к бренду
        """
        try:
            self.presta_fields.id_manufacturer = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Brand' данными {value}
            Ошибка: """, ex)
            return
        
    # @property
    # def locale(self) -> int:
    #     """  <sub>*[property]*</sub> `ps_product_lang.locale: int(10) unsigned` """
    #     ...
    #     return self.assist_fields.locale or None
    # ...
    
    # @locale.setter    
    # def locale(self, value):
    #     """  <sub>*[setter]*</sub>  `ps_product_lang.locale: unsigned` """
    #     ...
    #     try:
    #         self.assist_fields.locale = value
    #     except ProductFieldException as ex:
    #         logger.error(f"""Ошибка заполнения поля: 'locale' данными {value}
    #         Ошибка: """, ex)
    #         return
    ...

#   4   Главная категория этого товара
    
    @property
    def id_category_default(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.id_category_default: int(10) unsigned`
         @details: привязываю товар к главной категории для этого товара
        """
        return self.presta_fields.id_category_default or None
    
    
    @id_category_default.setter
    def id_category_default(self, value: int):
        """  <sub>*[setter]*</sub> Сюда передается та категория, которая будет однознчно - родительская `ps_product.id_category_default: int(10) unsigned`"""
        try:
            self.presta_fields.id_category_default = value
            
        except ProductFieldException as ex:
            """ @todo - требуется валидатор"""
            logger.critical(f"""Ошибка заполнения поля: 'id_category_default' данными {value}
            Ошибка: """, ex)
            return        

    @property
    def additional_categories(self) -> dict | None:
        """  <sub>*[property]*</sub> 
        возвращает словарь категорий товара восстановленный из файла сценария таблица `ps_category_product`"""

        return self.presta_fields.associations.categories or None

    
    @additional_categories.setter    
    def additional_categories(self, value: int | list[int]):
        """  <sub>*[setter]*</sub>   Дополнительные к основной категории.
        При задании доп ключей прдеыдущие значения заменяются новыми из `additional_categories`.
        Для добавления новых к уже существующим используй  функцию additional_categories_append()
        """
        
        value = value if isinstance(value, list) else [value]
        
        for v in value:
            if not isinstance(v, int):
                logger.error(f'недопустимое значение для категории {v=}, Должен быть `int`')
                ...
                continue
                
            try:
                self.presta_fields.associations.categories.update({'id':v})
            
            except ProductFieldException as ex:
                logger.error(f"""Ошибка заполнения поля: 'additional_categories' данными {v}
                Ошибка: """, ex)  
                return
   
# # # #   5   Магазин по умолчанию
    
    @property
    def id_shop_default(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
         @details: ID магазина по умолчанию . Используется multishop"""

        return self.presta_fields.id_shop_default or ''
    
    @id_shop_default.setter
    def id_shop_default(self, value: int = None):
        """  <sub>*[setter]*</sub>   `ps_product.id_shop_default: int(10) unsigned`
            `ID` магазина заказчика """
        try:
            self.presta_fields.id_shop_default = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop_default' данными {value}
            Ошибка: """, ex)
            return

# # #   5   Магазин по умолчанию
    
    @property
    def id_shop(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
         @details: ID магазина по умолчанию . Используется multishop"""

        return self.presta_fields.id_shop_default or ''
    
    @id_shop.setter
     
    def id_shop(self, value: int = None):
        """  <sub>*[setter]*</sub>   `ps_product.id_shop: int(10) unsigned`
            `ID` магазина заказчика """
        try:
            self.presta_fields.id_shop = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop' данными {value}
            Ошибка: """, ex)
            return


#   6   НДС (Израиль - обычно 13)
    
    @property
    def id_tax(self) -> int:
        """  <sub>*[property]*</sub> tax_rule `int`  :  `ID` НДС  `ps_product.id_tax: int(10) unsigned`"""

        return self.presta_fields.id_tax or ''

    
    @id_tax.setter
         
    def id_tax(self, value: int ):
        """   <sub>*[setter]*</sub>  `ID` ндс. מע''מ = 13 """
        try:
            self.presta_fields.id_tax = int(value)

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Tax rule ID' данными {value}
            Ошибка: """, ex)
            return

#   7   Распродажа - Mivtza
    
    @property
    
    def on_sale(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.on_sale: tinyint(1)  unsigned`"""

        return self.presta_fields.on_sale  or ''

    @on_sale.setter
         
    def on_sale(self, value = 0 ):
        """  <sub>*[setter]*</sub> `1` - распродажа

        @param value (int, optional): Defaults to 0.

        @returns
            bool: _ @details_
        """
        try:
            self.presta_fields.on_sale = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'On sale (0/1)' данными {value}
            Ошибка: """, ex)
            return

#   8 online_only: только через онлайн
    
    @property
    def online_only(self) -> int:
        """   <sub>*[property]*</sub>   `ps_product.online_only: tinyint(1) unsigned`
        field DB type: tinyint(1) unsigned
         @details: товар только онлайн """

        return self.presta_fields.online_only or ''
    
    
    @online_only.setter
    def online_only(self, value = 0) -> bool:
        """   <sub>*[setter]*</sub> """
        try:
            self.presta_fields.online_only = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'online_only' данными {value}""",ex)
            ...
            return

#   9   ean13
    
    @property
    def ean13(self) -> str | None:
        """  <sub>*[property]*</sub>   `ps_product.ean13  varchar(13)`
        field DB type: 
         @details: __prod_desc__"""
        return self.presta_fields.ean13 or ''

    @ean13.setter
    def ean13(self, value:str = None, lang:str = 'en') -> bool:
        """   <sub>*[setter]*</sub>   `ean13`
        field DB type:  varchar(13)
         @details: __prod_desc__"""
        try:
            self.presta_fields.ean13 = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ean13' данными {value}""", ex)
            return

#   10
    @property
    def isbn(self) -> str | None:
        """   <sub>*[property]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__"""
        return self.presta_fields.isbn or ''
        
    @isbn.setter
    def isbn(self, value:str = None, lang:str = 'en') -> bool:
        """   <sub>*[setter]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__"""
        try:
            self.presta_fields.isbn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}
            Ошибка: """, ex)
            return

#   11
    
    @property
    def upc(self):
        """  <sub>*[property]*</sub>   `upc`
        field DB type: varchar(12)
         @details: __prod_desc__"""
        return self.presta_fields.upc or ''
    
    
    @upc.setter
    def upc(self, value:str = None, lang:str = 'en') -> str | None:
        """   <sub>*[setter]*</sub>   `ps_product.upc`
        field DB type: varchar(12)
         @details: __prod_desc__"""
        try:
            self.presta_fields.upc = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}
            Ошибка: """, ex)
            return

#   12  mpn
    
    @property
    def mpn(self) -> str:
        """  <sub>*[property]*</sub>   `ps_product.mpn`
        field DB type: varchar(40)
         @details: __prod_desc__"""
        return self.presta_fields.mpn or ''

    
    @mpn.setter
    def mpn(self, value:str = None, lang:str = 'en') -> bool:
        """   <sub>*[setter]*</sub>  """
        try:
            self.presta_fields.mpn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
                         Ошибка заполнения поля: `ps_product.mpn` данными {value}
                         -----------------
                            Ошибка: """, ex)
            return

#   13   ecotax
    
    @property
    def ecotax(self):
        """  <sub>*[property]*</sub>   `ps_product.ecotax`
        field DB type:  decimal(17,6)
         @details: __prod_desc__"""
        return self.presta_fields.ecotax or ''

    @ecotax.setter
    def ecotax(self, value:str = None, lang:str = 'en') -> bool:
        """   <sub>*[setter]*</sub>  """
        try:
            self.presta_fields.ecotax = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ecotax' данными {value}""", ex)
            return

# 14
    """ quantity не заполнять - апи ее не хочет  """
    # @property
    # def quantity(self) -> int:
    #     """  <sub>*[property]*</sub>   `ps_product.quantity`
    #     field DB type: int(10)
    #      @details: __prod_desc__"""

    #     return self.presta_fields.quantity

    
    # @quantity.setter
    #  
    # def quantity(self, value: int = 0) -> bool:
    #     """  <sub>*[setter]*</sub>   `ps_product.quantity` """
    #     try:
    #         self.presta_fields.quantity = value
    #         return True
    #     except ProductFieldException as ex:
    #         logger.error(f"""Ошибка заполнения поля: 'quantity' данными {value}
    #         Ошибка: """, ex)
    #         return

# 15
    
    @property
    def minimal_quantity(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.minimal_quantity`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.minimal_quantity or ''

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.minimal_quantity = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'minimal_quantity' данными {value}
            Ошибка: """, ex)
            return

#   16
    
    @property
    
    def low_stock_threshold(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.low_stock_threshold`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.low_stock_threshold or ''

    
    @low_stock_threshold.setter
    def low_stock_threshold(self, value: str = '') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.low_stock_threshold = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_threshold' данными {value}
            Ошибка: """, ex)
            return
#   17
    
    @property
    def low_stock_alert(self) -> int:
        """  <sub>*[property]*</sub>  `ps_product.low_stock_alert`
        field DB type: tinyint(1)
         @details: __prod_desc__"""
        return self.presta_fields.low_stock_alert or ''

    
    @low_stock_alert.setter
    def low_stock_alert(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.low_stock_alert = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_alert' данными {value}
            Ошибка:{ex}""")
            return
#   18
    
    @property
    def price(self) -> float:
        """  <sub>*[property]*</sub>  `ps_product.price`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.price  or 0
        
    
    @price.setter
    def price(self, value: str | int | float) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            if not value:
                return 0
            self.presta_fields.price = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'price' данными {value}""",ex)
            ...
            return
#   19
    
    @property
    def wholesale_price(self) -> float:
        """  <sub>*[property]*</sub>  `ps_product.wholesale_price`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.wholesale_price or ''

    
    @wholesale_price.setter
     
    def wholesale_price(self, value:str = None, lang:str = 'en') -> float:
        """  <sub>*[setter]*</sub>   """
        try:
            #self.presta_fields.wholesale_price = str (StringNormalizer.normalize_price (value) )
            self.presta_fields.wholesale_price = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'wholesale_price' данными {value}
            Ошибка: """, ex)
            return
#   20
    
    @property
    def unity(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product.unity`
        field DB type: varchar(255)
         @details: __prod_desc__"""
        return self.presta_fields.unity or ''
    
    @unity.setter
     
    def unity(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.unity = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'unity' данными {value}
            Ошибка: """, ex)
            return

#   21
    
    @property
    def unit_price_ratio(self) -> float:
        """  <sub>*[property]*</sub>  `ps_product.unit_price_ratio`
        field DB type: decimal(20,6)
         Тип значения для `unit_price_ratio`  может быть:
        1. **Число с плавающей запятой (float)**: 
            Если `unit_price_ratio` представляет собой отношение или коэффициент, 
            то его значение чаще всего будет дробным числом, например, 1.5 или 0.75.
        2. **Целое число (int)**: В некоторых случаях это может быть целое число, 
            например, если речь идет о коэффициенте в целочисленном формате, например, 2 (что может означать удвоение цены).
        3. **Строка (str)**: В редких случаях, если значение может включать специальные обозначения или единицы измерения, 
            его можно представить в виде строки, например, "1.5x".
        Обычно в большинстве приложений и систем управления данными наиболее распространённый тип для коэффициента — это **число с плавающей запятой (float)**."""
        return self.presta_fields.unit_price_ratio  or ''

    
    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.unit_price_ratio = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: `unit_price_ratio` данными {value}
            Ошибка: """, ex)
            return
#   22
    
    @property
    def additional_shipping_cost(self) -> float:
        """  <sub>*[property]*</sub> `ps_product.additional_shipping_cost`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.additional_shipping_cost  or ''

    
    @additional_shipping_cost.setter
     
    def additional_shipping_cost(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.additional_shipping_cost = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_shipping_cost' данными {value}
            Ошибка: """, ex)
            return
#   23
    
    @property
    def reference(self) -> str:
        """  <sub>*[property]*</sub> `ps_product.reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__
        """
        return self.presta_fields.reference  or ''

    
    @reference.setter
     
    def reference(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.reference = str(value)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'reference' данными {value}
            Ошибка: """, ex)
            return
        
    
    @property
    def supplier_reference(self):
        """  <sub>*[property]*</sub>  `ps_product.supplier_reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__
        """
        return self.presta_fields.supplier_reference  or ''
#   24
    
    @supplier_reference.setter
     
    def supplier_reference(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.supplier_reference = str(value)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'supplier_reference' данными {value}
            Ошибка: """, ex)
            return
#   25
    
    @property
    def location(self) -> str:
        """  <sub>*[property]*</sub> `ps_product.location`
        field DB type: varchar(255)
         @details: __prod_desc__"""
        return self.presta_fields.location  or ''

    
    @location.setter
     
    def location(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.location = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'location' данными {value}
            Ошибка: """, ex)
            return

#   26
    
    @property
    def width(self) -> float:
        """  <sub>*[property]*</sub> `ps_product.width`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.width or ''

    
    @width.setter
     
    def width(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.width = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'width' данными {value}
            Ошибка: """, ex)
            return
#   27
    
    @property
    def height(self) -> float:
        """  <sub>*[property]*</sub> `ps_product.height`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.height or ''

    
    @height.setter
     
    def height(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.height = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'height' данными {value}
            Ошибка: """, ex)
            return
#   28
    
    @property
    def depth(self) -> float:
        """  <sub>*[property]*</sub> `[28] ps_product.depth  decimal(20,6)`
        field DB type:
         @details: __prod_desc__"""
        return self.presta_fields.depth or ''

    
    @depth.setter
     
    def depth(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.depth = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'depth' данными {value}
            Ошибка: """, ex)
            return
#   29
    
    @property
    def weight(self) -> float:
        """  <sub>*[property]*</sub> `ps_product.weight`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.weight or ''

    
    @weight.setter
     
    def weight(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.weight = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'weight' данными {value}
            Ошибка: """, ex)
            return

    #  30
    @property
    def volume(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.state`
        field DB type: int(11)
         @details: __prod_desc__"""

        return self.presta_fields.volume  or ''
    
    
    @volume.setter
     
    def volume(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.volume = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'state' данными {value}
            Ошибка: """, ex)
            return

   # 31 
    @property
    def out_of_stock(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.out_of_stock`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.out_of_stock or ''

    
    @out_of_stock.setter
     
    def out_of_stock(self, value: int = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.out_of_stock = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'out_of_stock' данными {value}
            Ошибка: """, ex)
            return

  #  31
    
    @property
    def additional_delivery_times(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.additional_delivery_times tinyint(1)`
         @details: __prod_desc__"""
        return self.presta_fields.additional_delivery_times   or ''

    
    @additional_delivery_times.setter
     
    def additional_delivery_times(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.additional_delivery_times = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_delivery_times' данными {value}
            Ошибка: """, ex)
            return
  #  32
    
    @property
    def quantity_discount(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.quantity_discount`
        field DB type: tinyint(1)
         @details: __prod_desc__"""
        return self.presta_fields.quantity_discount or ''

    
    @quantity_discount.setter
     
    def quantity_discount(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.quantity_discount = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'quantity_discount' данными {value}
            Ошибка: """, ex)
            return

  #  33
    
    @property
    def customizable(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.customizable`
        field DB type: tinyint(2)
         @details: __prod_desc__"""
        return self.presta_fields.customizable  or ''

    
    @customizable.setter
     
    def customizable(self, value: int = 0) -> bool:
        try:
            self.presta_fields.customizable = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'customizable' данными {value}
            Ошибка: """, ex)
            return

  #  34
    
    @property
    def uploadable_files(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.uploadable_files`
        field DB type: tinyint(4)
         @details: __prod_desc__"""

        return self.presta_fields.uploadable_files or ''

    
    @uploadable_files.setter
     
    def uploadable_files(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.uploadable_files = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'uploadable_files' данными {value}
            Ошибка: """, ex)
            return
#  35
    
    @property
    def text_fields(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.text_fields`
        field DB type: tinyint(4)
         @details: __prod_desc__"""

        return self.presta_fields.text_fields  or ''

    
    @text_fields.setter
     
    def text_fields(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.text_fields = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'text_fields' данными {value}
            Ошибка: """, ex)
            return

#  36
    
    @property
    def active(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.active`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.active or ''

    
    @active.setter
     
    def active(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.active = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'active' данными {value}
            Ошибка: """, ex)
            return
   
        

#  37

        
    @property
    def redirect_type(self) -> str:
        """  <sub>*[property]*</sub> `[37] ps_product.redirect_type enum('404','301-product','302-product','301-category','302-category')`
        
    Редиректы HTTP 301 (Moved Permanently) и 302 (Found, временное перенаправление) различаются в том, как они обрабатываются браузерами и поисковыми системами:

    301 Moved Permanently (Постоянное перенаправление):

    Этот статус указывает на то, что ресурс был окончательно перемещен на новый URL.
    Браузеры и поисковые системы обычно кэшируют этот редирект, что означает, что при следующем запросе к тому же URL клиент будет напрямую перенаправлен на новый без обращения к оригинальному местоположению.
    Этот тип редиректа обычно используется, когда страница или ресурс были перенесены на новый адрес и больше не существуют по старому.
    302 Found (Временное перенаправление):

    Этот статус указывает на то, что ресурс временно перемещен на новый URL.
    Браузеры и поисковые системы могут повторять запросы к оригинальному URL, так как это считается временным перенаправлением.
    Этот тип редиректа подходит, когда ресурс временно недоступен на оригинальном местоположении, и клиент должен использовать новый адрес, но при этом оригинальное местоположение может быть использовано в будущем.
    Выбор между 301 и 302 зависит от того, насколько постоянно изменение местоположения ресурса. Если изменение постоянное, то рекомендуется использовать 301. Если изменение временное, то следует использовать 302.
    """
        return self.presta_fields.redirect_type  or ''


    
    class EnumRedirect(Enum):
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'
        
    @redirect_type.setter
     
    def redirect_type(self, value: EnumRedirect | str) -> bool:
        """  <sub>*[setter]*</sub>   Редирект. 
        Редиректы представляют собой механизм перенаправления пользователя или браузера с одного URL-адреса на другой. Они часто используются в веб-разработке для переноса посетителя с одной страницы на другую. Различные HTTP-статусы и типы редиректов сообщают браузеру или клиенту, как следует интерпретировать запрос и что делать дальше. В вашем коде вы используете строки для представления различных типов редиректов.

        ERROR_404 (404 Not Found):

        Этот редирект сообщает клиенту, что запрашиваемый ресурс не найден.
        Применяется, когда сервер не может найти запрашиваемую страницу или ресурс.
        REDIRECT_301_PRODUCT (301 Moved Permanently):

        Говорит браузеру, что ресурс был окончательно перемещен на новый URL.
        Этот тип редиректа особенно полезен для SEO, поскольку поисковые системы обычно обрабатывают его, перенося рейтинги страницы на новый адрес.
        REDIRECT_302_PRODUCT (302 Found):

        Указывает, что ресурс временно перемещен.
        Используется, когда ресурс временно недоступен, и запрос должен быть отправлен на временный адрес.
        REDIRECT_301_CATEGORY (301 Moved Permanently):

        Аналогичен REDIRECT_301_PRODUCT.
        Отправляет клиента на новый адрес с постоянным характером.
        REDIRECT_302_CATEGORY (302 Found):

        Аналогичен REDIRECT_302_PRODUCT.
        Перенаправление с временным характером для категории.

        ###пример

        @code
            def handle_redirect(redirect_typex):
                if redirect_type == EnumRedirect.ERROR_404:
                    # Обработка ошибки 404: страница не найдена
                    # Вызов функции или отображение соответствующей страницы
                    ...
                elif redirect_type in [EnumRedirect.REDIRECT_301_PRODUCT, EnumRedirect.REDIRECT_301_CATEGORY]:
                    # Обработка постоянного редиректа (301)
                    # Выполнение перенаправления на новый URL
                    ...
                elif redirect_type in [EnumRedirect.REDIRECT_302_PRODUCT, EnumRedirect.REDIRECT_302_CATEGORY]:
                    # Обработка временного редиректа (302)
                    # Выполнение временного перенаправления на новый URL
                    ...

        @edcode
        """
        try:
            self.presta_fields.redirect_type = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'redirect_type' данными {value}
            Ошибка: """, ex)
            return

 #  38
    
    @property
    def id_type_redirected(self) -> int:
        """  <sub>*[property]*</sub> `[38] ps_product.id_type_redirected  tinyint(10)`
        field DB type:
         @details: __prod_desc__"""

        return self.presta_fields.id_type_redirected or ''
    
    
    @id_type_redirected.setter
     
    def id_type_redirected(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.id_type_redirected = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'id_type_redirected' данными {value}
            Ошибка: """, ex)
            return

 #  39
    
    @property
    def available_for_order(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.available_for_order`
        field DB type: tinyint(10)
         @details: __prod_desc__"""

        return self.presta_fields.available_for_order  or ''

    
    @available_for_order.setter
     
    def available_for_order(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.available_for_order = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_for_order' данными {value}
            Ошибка: """, ex)
            return

 #  40
    
    @property
    def available_date(self) -> Date:
        """  <sub>*[property]*</sub> `ps_product.available_date`
        field DB type: date
         @details: __prod_desc__"""

        return self.presta_fields.available_date  or ''

    
    @available_date.setter
     
    def available_date(self, value: Date = Date.today) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.available_date = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_date' данными {value}
            Ошибка: """, ex)
            return

 #  41
    
    @property
    def show_condition(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.show_condition`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.show_condition or ''

    
    @show_condition.setter
     
    def show_condition(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.show_condition = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_condition' данными {value}
            Ошибка: """, ex)
            return

 #  42

    @property
    def condition(self) -> str:
        """  <sub>*[property]*</sub> `[42] ps_product.condition  enum('new','used','refurbished')`
         @details: __prod_desc__"""

        return self.presta_fields.condition   or ''
        
    class EnumCondition(Enum):
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'
       
    @condition.setter
     
    def condition(self, value: EnumCondition | str = EnumCondition.NEW) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.condition = str(value)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'condition' данными {value}
            Ошибка: """, ex)
            return

 #  43
    
    @property
    def show_price(self) -> int:
        """  <sub>*[property]*</sub> `[43] ps_product.show_price tinyint(1)`
        field DB type: 
         @details: __prod_desc__"""

        return self.presta_fields.show_price  or ''
    
    
    @show_price.setter
    def show_price(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.show_price = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_price' данными {value}
            Ошибка: """, ex)
            return

#  44
    
    @property
    def indexed(self) -> int:
        """  <sub>*[property]*</sub> `[44] ps_product.indexed  tinyint(1)`
         @details: __prod_desc__"""
        return self.presta_fields.indexed  or ''
    
    
    @indexed.setter
    def indexed(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.indexed = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'indexed' данными {value}
            Ошибка: """, ex)
            return

#  45
    
    @property
    def visibility(self) -> str:
        """  <sub>*[property]*</sub> `ps_product.visibility`
        field DB type: enum('both','catalog','search','none')
         @details: __prod_desc__"""

        return self.presta_fields.visibility  or ''

    class EnumVisibity(Enum):
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'

    
    @visibility.setter
     
    def visibility(self, value: EnumVisibity = EnumVisibity.BOTH) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.visibility = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'visibility' данными {value}
            Ошибка: """, ex)
            return


#  46

    
    @property
    def cache_is_pack(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.cache_is_pack`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.cache_is_pack   or ''
    
    
    @cache_is_pack.setter
     
    def cache_is_pack(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.cache_is_pack = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_is_pack' данными {value}
            Ошибка: """, ex)
            return

#  47
    
    @property
    def cache_has_attachments(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.cache_has_attachments`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.cache_has_attachments  or ''
    
    
    @cache_has_attachments.setter
     
    def cache_has_attachments(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.cache_has_attachments = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_has_attachments' данными {value}
            Ошибка: """, ex)
            return

#  48
    
    @property
    def is_virtual(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.is_virtual`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.is_virtual   or ''

    
    @is_virtual.setter
     
    def is_virtual(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.is_virtual = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'is_virtual' данными {value}
            Ошибка: """, ex)
            return

#  49
    
    @property
    def cache_default_attribute(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.cache_default_attribute`
        field DB type: int(10)
         @details: __prod_desc__"""

        return self.presta_fields.cache_default_attribute  or ''

    
    @cache_default_attribute.setter
     
    def cache_default_attribute(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.cache_default_attribute = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_default_attribute' данными {value}
            Ошибка: """, ex)
            return

#  50
    
    @property
    def date_add(self) -> Date:
        """  <sub>*[property]*</sub> `ps_product.date_add`
        field DB type: datetime
         @details: __prod_desc__"""

        return self.presta_fields.date_add  or ''
    
    
    @date_add.setter
     
    def date_add(self, value: Date = Date.today()) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.date_add = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_add' данными {value}
            Ошибка: """, ex)
            return

#  51
    
    @property
    def date_upd(self) -> Date:
        """  <sub>*[property]*</sub> `ps_product.date_upd`
        field DB type: datetime
         @details: __prod_desc__"""

        return self.presta_fields.date_upd  or ''
    
    
    @date_upd.setter
     
    def date_upd(self, value: Date = Date.today()) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.date_upd = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_upd' данными {value}
            Ошибка: """, ex)
            return


#  52
    
    @property
    def advanced_stock_management(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.advanced_stock_management`
        field DB type: tinyint(1)
         @details: __prod_desc__"""

        return self.presta_fields.advanced_stock_management or ''
    
    
    @advanced_stock_management.setter
    def advanced_stock_management(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.advanced_stock_management = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'advanced_stock_management' данными {value}
            Ошибка: """, ex)
            return

#  53
    
    @property
    def pack_stock_type(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.pack_stock_type`
        field DB type: int(11)
         @details: __prod_desc__"""

        return self.presta_fields.pack_stock_type or ''
    
    
    @pack_stock_type.setter
    def pack_stock_type(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.pack_stock_type = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'pack_stock_type' данными {value}
            Ошибка: """, ex)
            return


#  54
    
    @property
    def state(self) -> int:
        """  <sub>*[property]*</sub> `ps_product.state`
        field DB type: int(11)
         @details: __prod_desc__"""

        return self.presta_fields.state  or ''
    
    
    @state.setter
    def state(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.state = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'state' данными {value}
            Ошибка: """, ex)
            return


#  55
    
    @property
    def product_type(self) -> str:
        """  <sub>*[property]*</sub> `ps_product.product_type`
        field DB type: enum('standard', 'pack', 'virtual', 'combinations', '')
         @details: __prod_desc__"""

        return self.presta_fields.product_type   or ''

    class EnumProductType(Enum):
        STANDARD = 'standard'
        PACK = 'pack'
        VIRTUAL = 'virtual'
        COMBINATIONS = 'combinations'
        EMPTY = ''
          
    @product_type.setter
    def product_type(self, product_type: EnumProductType = EnumProductType.STANDARD) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.product_type = product_type
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'product_type' данными {product_type}
            Ошибка: """, ex)
            return


    ####################################################################################################################################
    #
    #
    #
    #           ТАБЛИЦА `ps_product_lang` - СОДЕРЖИТ МИЛЬТИЯЗЫЧНЫЕ ПОЛЯ 
    #
    #
    #       
    #
    # -----------------------------------------------------------------------------------------------------------------------------------

    #
    #           
    #
    #   |    Column Name	              |  Data Type	       | Comment
    #---------------------------------------------------------------------
    # 1	    `id_product`                    int(10) unsigned
    # 2	    `id_shop`	                    int(11) unsigned
    # 3	    `locale`	                    int(10) unsigned
    # 4	    `description`	                text
    # 5	    `description_short`	            text
    # 6	    `link_rewrite`	                varchar(128)
    # 7	    `meta_description`	            varchar(512)
    # 8	    `meta_keywords`	                varchar(255)
    # 9	    `meta_title`	                varchar(128)
    # 10	`name`	                        varchar(128)
    # 11	`available_now`	                varchar(255)        Заметка, о наличии товара сегодня
    # 12	`available_later`	            varchar(255)
    # 13	`delivery_in_stock`	            varchar(255)        Доставка, если товар н наличии
    # 14	`delivery_out_stock`	        varchar(255)        (Доставка если товара нет в наличии): Текст, который будет отображаться, когда товара нет в наличии.
    # 15    `delivery_additional_message`   tinytext            Мое поле. Доп для полей доставки. Например, война
    # 16	`affiliate_short_link`	        tinytext
    # 17	`affiliate_text`	            tinytext
    # 18	`affiliate_summary`	            tinytext
    # 19	`affiliate_summary_2`	        tinytext
    # 20    `affiliate_image_small`         varchar(512)
    # 21    `affiliate_image_medium`        varchar(512)
    # 22    `affiliate_image_large`         varchar(512)
    # 23	`ingredients`	                tinytext
    # 24	`how_to_use`        	        tinytext


    #   Поля `id_product`  берутся из верхних значениий в этом коде

    #
    #
    #
    ########################################################################################

    """ 
    `'locale` я по умолчанию выбираю `1`, т.к. при последующем парсинге полученных значений я делаю переводы 
    и упорядовачиваю языки в соответствии со схемой языков клиента Престашоп
    """

        
#   4
    
    @property
    def description(self) -> str:
        """  <sub>*[property]*</sub> `[4] ps_product_lang.description text`
        description: Описание """
        return self.presta_fields.description or ''


    @description.setter
    def description(self, value: str | list = '', lang:str = 'en') -> bool:
        """<sub>*[setter]*</sub>"""
        try:
            # # Convert list to string if necessary
            # if isinstance(value, list):
            #     value = ', '.join(map(str, value))
        
            self.presta_fields.description: dict = {
                'language': [{'attrs': {'id': '1'}, 'value': value}]
            }
            return True

        except ProductFieldException as ex:
            logger.error(
                f"""Ошибка заполнения поля: 'description' данными {value}
                Ошибка: """, ex
            )
            ...
            return
#   5
    
    @property
    def description_short(self) -> str:
        """  <sub>*[property]*</sub> `[5] ps_product_lang.description_short text`
        description: __prod_desc__"""

        return self.presta_fields.description_short  or ''
    
    @description_short.setter
    
    def description_short(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.description_short: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'description_short' данными {value}
            Ошибка: """, ex)
            return
#   6
    @property
    def link_rewrite(self) -> str:
        """  <sub>*[property]*</sub> `ps_product_lang.link_rewrite`
        field DB type: varchar(128)
        description: __prod_desc__"""
        return self.presta_fields.link_rewrite  or ''
                                                              
    
    @link_rewrite.setter
     
    def link_rewrite(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            #self.presta_fields.link_rewrite = link_rewrite
            self.presta_fields.link_rewrite: dict ={'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'link_rewrite' данными {value}
            Ошибка: """, ex)
            return
#   7
    
    @property
    def meta_description(self) -> str:
        """  <sub>*[property]*</sub> `[7] ps_product_lang.meta_description varchar(512)` 
        field DB type: 
        description: __prod_desc__"""
        return self.presta_fields.meta_description  or ''
    
    
    @meta_description.setter
     
    def meta_description(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.meta_description: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_description' данными {value}
            Ошибка: """, ex)
            return

#   8
    
    @property
    def meta_keywords(self):
        """  <sub>*[property]*</sub> `[8] ps_product_lang.meta_keywords varchar(255)`
        field DB type: 
        description: __prod_desc__"""
        return self.presta_fields.meta_keywords  or ''
    
    @meta_keywords.setter
     
    def meta_keywords(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.meta_keywords: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_keywords' данными {value}
            Ошибка: """, ex)
            return

#   9
    
    @property
    def meta_title(self) -> str:
        """  <sub>*[property]*</sub> `[9] s_product_lang.meta_title varchar(128)`
        description: __prod_desc__"""
        return self.presta_fields.meta_title or ''
    
    
    @meta_title.setter
     
    def meta_title(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.meta_title: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_title' данными {value}
            Ошибка: """, ex)
            return

#   10
    
    @property
    def name(self):
        """  <sub>*[property]*</sub> `[10] ps_product_lang.name  varchar(128)`
        description: __prod_desc__"""
        return self.presta_fields.name or ''
    
    
    @name.setter
     
    def name(self, value: str, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.name: dict = {'language':
                                                        [
                                                            {'attrs':{'id':self.language[lang]}, 'value': value},
                                                        ]
                                                     }
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'name' данными {value}
            Ошибка: """, ex)
            return

#   11
    
    @property
    def available_now(self) -> str:
        """  <sub>*[property]*</sub>  `[11] ps_product_lang.available_now varchar(255)`
        description: __prod_desc__"""
        return self.presta_fields.available_now or ''
    
    
    @available_now.setter
     
    def available_now(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.available_now: dict = {
                                                                'language':
                                                                    [
                                                                        {'attrs':{'id':self.language[lang]}, 'value':value},
                                                                    ]
                                                                }
                
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_now' данными {value}
            Ошибка: """, ex)
            return

#   12
    
    @property
    def available_later(self) -> str:
        """  <sub>*[property]*</sub>  field DB available_later: `[12] ps_product_lang.available_later varchar(255)`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.presta_fields.available_later or ''
    
    @available_later.setter
     
    def available_later(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.available_later: dict =  {
                                                                    'language':
                                                                        [
                                                                            {'attrs':{'id':self.language[lang]}, 'value':value},
                                                                        ]
                                                                    }
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_later' данными {value}
            Ошибка: """, ex)
            return


#   13
    
    @property
    def delivery_in_stock(self):
        """  <sub>*[property]*</sub>   `[13] ps_product_lang.delivery_in_stock varchar(255)`
        @details:  (Доставка при наличии товара): Текст, который будет отображаться, когда товар есть в наличии."""
        return self.presta_fields.delivery_in_stock or ''
    
    @delivery_in_stock.setter
     
    def delivery_in_stock(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>  Функция строит список словарей для поля `ps_product_lang.delivery_in_stock`
        @code
        {
            'language':[
                {'attrs':{'id':self.language[lang]}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]
        }
            @edcode
        """
        

        self.presta_fields.delivery_in_stock: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}

#   14
    
    @property
    def delivery_out_stock(self) -> str:
        """  <sub>*[property]*</sub>   `[14] ps_product_lang.delivery_out_stock varchar(256)` 
        description: __prod_desc__"""
        return self.presta_fields.delivery_out_stock
    
    @delivery_out_stock.setter
     
    def delivery_out_stock(self, value:str = None, lang:str = 'en') -> bool:
        self.presta_fields.delivery_out_stock: dict =   {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        
#   15

    @property
    def delivery_additional_message(self) -> str:
        """  <sub>*[property]*</sub>   `[15] ps_product_lang.delivery_out_stock`
        field DB type: 
        description: __prod_desc__"""
        return self.presta_fields.delivery_additional_message or None
    
    @delivery_additional_message.setter
     
    def delivery_additional_message(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub> Заметки по доставке. Например: война, хз когда доставим  
        Мультиязычное поле. Формирует словарь:
        @code
            {
            'language':[
            {'attrs':{'id':self.language[lang]}, 'value':delivery_additional_message},
            {'attrs':{'id':'2'}, 'value':delivery_additional_message},
            {'attrs':{'id':'3'}, 'value':delivery_additional_message},
            ]}
        @edcode
        """
        self.presta_fields.delivery_additional_message: dict  =  {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
  

#   16

    @property
    def affiliate_short_link(self) -> dict:
        """  <sub>*[property]*</sub>   `[15] ps_product_lang.affiliate_short_link  varchar(255)`
        description: __prod_desc__"""
        return self.presta_fields.affiliate_short_link or ''
    
    @affiliate_short_link.setter
     
    def affiliate_short_link(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub> Короткие линки на партнерские преогаммы. Мультиязычное поле.
        Формирует словарь:
        @code
         {
            'language':[
            {'attrs':{'id':self.language[lang]}, 'value':affiliate_short_link},
            {'attrs':{'id':'2'}, 'value':affiliate_short_link},
            {'attrs':{'id':'3'}, 'value':affiliate_short_link},
            ]}
            @edcode
        """
        try:
            self.presta_fields.affiliate_short_link: dict =   {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_short_link' данными {value}
            Ошибка: """, ex)
            return

#   17
    
    @property
    def affiliate_text(self) -> str:
        """  <sub>*[property]*</sub>   `[17] ps_product_lang.affiliate_text varchar(256)`"""
        return self.presta_fields.affiliate_text or None
    
    @affiliate_text.setter
    def affiliate_text(self, value:str = None, lang:str = 'en' ) -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.affiliate_text: dict =   {
                                                                'language':
                                                                    [
                                                                        {'attrs':{'id':self.language[lang]}, 'value':value},
                                                                    ]
                                                                }
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_text' данными {value} """, ex)
            return


#   18
    
    @property
    def affiliate_summary(self) -> str:
        """  <sub>*[property]*</sub>  `[18] ps_product_lang.affiliate_summary varchar(256)`"""
        return self.presta_fields.affiliate_summary or ''
    
    
    @affiliate_summary.setter 
    def affiliate_summary(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        if value and lang:
            self.presta_fields.affiliate_summary: dict =   {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}



#   19
    @property
    def affiliate_summary_2(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.presta_fields.affiliate_summary_2 or None

    
    @affiliate_summary_2.setter
     
    def affiliate_summary_2(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.affiliate_summary_2: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка: """, ex)
            return

#   20

    
    @property
    def affiliate_image_small(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.presta_fields.affiliate_image_small or None

    
    @affiliate_image_small.setter
    def affiliate_image_small(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.affiliate_image_small: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка: """, ex)
            return

 #   21

    
    @property
    def affiliate_image_medium(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.presta_fields.affiliate_image_medium or None

    
    @affiliate_image_medium.setter
     
    def affiliate_image_medium(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        try:
            self.presta_fields.affiliate_image_medium: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка: """, ex)
            return

    
 #   22
    @property
    def affiliate_image_large(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.presta_fields.affiliate_image_medium or ''

    
    @affiliate_image_large.setter
    def affiliate_image_large(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        self.presta_fields.affiliate_image_large: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
    ...

# 23
    @property
    def ingredients(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.ingredients`"""
        return getattr( self.presta_fields, 'ingredients', '')

    
    @ingredients.setter
    def ingredients(self, value: str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>  Ингридиенты. Текстовое поле - можно хранить фрагменты HTML кода 
        формирует список словарей:
        @code
        {
        'language':[
            {'attrs':{'id':self.language[lang]}, 'value':ingredients},
            {'attrs':{'id':'2'}, 'value':ingredients},
            {'attrs':{'id':'3'}, 'value':ingredients},
        ]}
        @edcode
        значение `ingredients` может быть блоком HTML
        """
        try:
            self.presta_fields.ingredients: dict =  {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        except ProductFieldException as ex:
            logger.error(f'Ошибка заполнения `ingredients` данными {value} Ошибка: ',ex)
            return
    ...
# 
    
    @property
    def specification(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.specification`"""
        return getattr(self.presta_fields, 'specification', '')


    
    @specification.setter
    def specification(self, value: str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>  specification. Текстовое поле - можно хранить фрагменты HTML кода 
        формирует список словарей:
        @code
        {
        'language':[
            {'attrs':{'id':self.language[lang]}, 'value':ingredients},
            {'attrs':{'id':'2'}, 'value':ingredients},
            {'attrs':{'id':'3'}, 'value':ingredients},
        ]}
        @edcode
        значение `ingredients` может быть блоком HTML
        """
        try:
            self.presta_fields.specification: dict =  {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        except ProductFieldException as ex:
            logger.error(f'Ошибка заполнения `specification` данными {value} Ошибка: ',ex)
            ...
            return
        
    @property
    def how_to_use(self) -> str:
        """  <sub>*[property]*</sub> `ps_product_lang.how_to_use` """
        return getattr(self.presta_fields, 'how_to_use', '')

    
    @how_to_use.setter
    def how_to_use(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>  `ps_product_lang.how_to_use` """
        try:
            self.presta_fields.how_to_use: dict = {'language':[{'attrs':{'id':self.language[lang]}, 'value':value},]}
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'how_to_use' данными {value}
            Ошибка: """, ex)
            return
    ...

    @property
    def id_default_image(self) -> str:
        """  <sub>*[property]*</sub>  field DB affiliate_summary_2: `_???????.id_default_image`"""
        ...

        return getattr(self.presta_fields, 'id_default_image', '')
    
    
    @id_default_image.setter
    def id_default_image(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        ...
        try:
            self.presta_fields.id_default_image = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_image' данными {value}
            Ошибка: """, ex)
            return
    ...
    # 57 link to video
    @property
    def link_to_video(self) -> str:
        """  <sub>*[property]*</sub>  `ps_product_lang.link_to_video` filed number 57"""
        ...
        return getattr(self.presta_fields, 'link_to_video', '')

    
    
    @link_to_video.setter
    def link_to_video(self, value:str = None) -> bool:
        """  <sub>*[setter]* link_to_video</sub>   """
        ...
        self.presta_fields.link_to_video = value or ''  

    @property
    def images_urls(self):
        """  <sub>*[property]*</sub>   __prod_name__
        field DB type: __prod_type__
        description: __prod_desc__"""
        return getattr(self.presta_fields, 'images_urls', '')

    @images_urls.setter
    def images_urls(self, value:str = None) -> bool:
        """  <sub>*[setter]* link_to_video</sub>   """
        ...
        self.presta_fields.link_to_video = value

    @property
    def local_saved_image(self):
        """  <sub>*[property]*</sub>   __prod_name__
        Путь к картинке, сохраненной на диске
        """
        return getattr(self.presta_fields, 'local_saved_image', '')

    @local_saved_image.setter
    def local_saved_image(self, value:str = None) -> bool:
        """  <sub>*[setter]* local_saved_image</sub>   """
        ...
        self.presta_fields.local_saved_image = value

    @property
    def local_saved_video(self):
        """  <sub>*[property]*</sub>   __prod_name__
            путь к видео , сохраннёному на диске"""
        return self.presta_fields.images_urls or ''

    @local_saved_video.setter
    def local_saved_video(self, value:str = None) -> bool:
        """  <sub>*[setter]* local_saved_image</sub>   """
        ...
        self.presta_fields.local_saved_image = value

    @property
    def position_in_category(self) -> str:
        """  <sub>*[property]*</sub>   field DB affiliate_summary_2: `_?????????.position_in_category`"""
        return self.presta_fields.position_in_category or ''

    
    @position_in_category.setter
    def position_in_category(self, value:str = None, lang:str = 'en') -> bool:
        """  <sub>*[setter]*</sub>   """
        self.presta_fields.position_in_category = value






        #########################################################################################
        #                                                                                       #
        #                   Служебные поля - images urls etc.                                   #
        #       Служебные поля не входят в основной словарь `presta_fields_dict`                #
        #       Они заносятся в служебный словарь `assist_fields_dict`                          #
        #       Здесь я храню                                                                   #
        #       - URL на дополнительные картинки                                                #
        #       - код языка на сайте поставщика. Потом мне надо будет распарсить                #
        #            мультиязычные строки                                                       #
        #                                                                                       #
        #                                                                                       #
        #########################################################################################





    @property
    def page_lang(self) -> str:
        """ код языка на котором я собираю информацию с сайта
        код хранится в объекте `Driver.page_lang`. Требуется для правильного расположения переводов"""
        ...
        return self.assist_fields_dict.page_lang

    @page_lang.setter        
    def page_lang(self, value = None) -> bool:
        if value:
            if 'page_lang' in self.assist_fields_dict.keys():
                self.assist_fields_dict.page_lang = value
            else:
                self.assist_fields_dict.update({'page_lang':value}) 



