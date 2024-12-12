## Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для описания полей товара в PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`ProductFields`, который используется для
описания полей товара в формате API PrestaShop. Класс включает в себя
свойства для каждого поля, соответствующего полям в таблицах `PrestaShop`.

langdetect в Python используется для определения языка текста. Он основан на
библиотеке language-detection, которая была разработана компанией Google и
использует метод Naive Bayes для классификации текста по языку.

Пример использования
--------------------

Пример использования langdetect:

.. code-block:: python

    from langdetect import detect, detect_langs

    # Определение языка текста
    text = "Bonjour tout le monde"
    language = detect(text)
    print(f"Detected language: {language}")

    # Определение вероятностей нескольких языков
    languages = detect_langs(text)
    print(f"Detected languages: {languages}")

Пример обработки исключений при использовании langdetect:

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

          Column Name                 Data Type\t            Allowed NULL
  1\t    `id_product`                int(10) unsigned\t    [V]
  2       `id_supplier`               int(10) unsigned\t    [V]
  3       `id_manufacturer`           int(10) unsigned\t    [v]
  4       `id_category_default`       int(10) unsigned\t    [v]
  5       `id_shop_default`           int(10) unsigned        [v]
  6       `id_tax`\t    int(11) unsigned        [v]
  7       `on_sale`                   tinyint(1) unsigned     [v]
  8       `online_only`               tinyint(1) unsigned     [v]
  9       `ean13`                     varchar(13)             [v]
  10      `isbn`                      varchar(32)
  11      `upc`                       varchar(12)
  12      `mpn`                       varchar(40)
  13\t    `ecotax`                    decimal(17,6)
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
from src.utils.file import read_text_file
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException 

"""Класс, описывающий поля товара в формате API PrestaShop."""
import header
from src.logger.logger import logger
from src.utils.jjson import j_loads
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional

class ProductFields:
    """
    Класс для представления полей товара в формате API PrestaShop.
    
    :ivar product_fields_list: Список полей продукта.
    :vartype product_fields_list: List[str]
    :ivar language: Словарь соответствия языков и их идентификаторов.
    :vartype language: Dict[str, int]
    :ivar presta_fields: Объект SimpleNamespace для хранения полей PrestaShop.
    :vartype presta_fields: SimpleNamespace
    :ivar assist_fields_dict: Словарь для хранения дополнительных полей.
    :vartype assist_fields_dict: Dict[str, Any]
    """

    def __init__(self):
        """
        Инициализация класса. 
        
        Загружаются данные полей, языков и их идентификаторов,
        а также устанавливаются дефолтные значения для полей.
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

        :return: Список полей, загруженных из текстового файла.
        :rtype: List[str]
        """
        return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)

    def _payload(self) -> bool:
        """
        Загрузка дефолтных значений полей.

        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
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
        """
        Возвращает словарь ключей ассоциаций.

        :return: Словарь ассоциаций или None.
        :rtype: Optional[Dict]
        """
        return self.presta_fields.associations or None

    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]):
        """
        Устанавливает словарь ассоциаций.

        :param value: Словарь ассоциаций.
        :type value: Dict[str, Optional[str]]
        """
        self.presta_fields.associations = value

    
    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]):
        """
        Свойство-сеттер для словаря ассоциаций. Список ассоциаций:

        :param value: Словарь ассоциаций.
        :type value: Dict[str, Optional[str]]
        """
        self.presta_fields.associations = value

    @property    
    def id_product(self) -> Optional[int]:
        """
        Свойство для получения `id_product` (ps_product.id: int(10) unsigned).

        :return: ID товара или None.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_product

    
    @id_product.setter     
    def id_product(self, value: int = None):
        """
        Свойство-сеттер для `id_product`. 
        
        ID товара. *для нового тoвара id назначется из `PrestaShop`*

        Запись нового товара в престашоп делается в два шага:
          -  в престасшоп заносятся парамеры, которые не связаны с ID, например, название товара, артикул и т.п.
          -  От престашоп возвращается словарь, в котором установлено ID.
          -  теперь можно грузить фото, доп парамерты, короче все, что завязано на id товара
        
        :param value: ID товара. Требуется при операциях над существующим товаром. `ps_product.id`.
        Для нового товара ID вернется из системы при занесении товара в базу данных.
        :type value: Optional[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        try:
            self.presta_fields.id_product = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}\n            Ошибка: """, ex)
            return


#   2   Поставщик
    @property
    def id_supplier(self):
        """
        Свойство для получения `id_supplier` (ps_product.id_supplier: int(10) unsigned).
        
        :details: привязываю товар к id поставщика
        :return: ID поставщика или None.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_supplier or None
    
    
    @id_supplier.setter
    def id_supplier(self, value: int = None):
        """
        Свойство-сеттер для `id_supplier`.
        
        :param value: ID поставщика.
        :type value: Optional[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        
        try:
            self.presta_fields.id_supplier = value
            return True

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: `ps_product.id_supplier` данными {value}\n            Ошибка: """, ex)
            return


#   3   Бренд
    
    @property
    def id_manufacturer(self) -> int:
        """
        Свойство для получения `id_manufacturer` (ps_product.id_manufacturer: int(10) unsigned).
        
        :details: Бренд может быть передан как по имени так и по ID.
            Таблица брендов:
        :return: ID производителя или None.
        :rtype: Optional[int]
        """

        return self.presta_fields.id_manufacturer or None
    
    
    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None):
        """
        Свойство-сеттер для `id_manufacturer`. 
        
        Бренд может быть передан как по имени так и по ID
        `ps_product.id_manufacturer`
        field type: int(10) unsigned
        :details: привязываю товар к бренду
        
        :param value: ID производителя.
        :type value: Optional[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.id_manufacturer = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Brand' данными {value}\n            Ошибка: """, ex)
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
    #         logger.error(f"""Ошибка заполнения поля: 'locale' данными {value}\n    #         Ошибка: """, ex)
    #         return
    ...

#   4   Главная категория этого товара
    
    @property
    def id_category_default(self) -> int:
        """
        Свойство для получения `id_category_default` (ps_product.id_category_default: int(10) unsigned).
        
        :details: привязываю товар к главной категории для этого товара
        :return: ID категории по умолчанию или None.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_category_default or None
    
    
    @id_category_default.setter
    def id_category_default(self, value: int):
        """
        Свойство-сеттер для `id_category_default`.
        
        Сюда передается та категория, которая будет однозначно - родительская `ps_product.id_category_default: int(10) unsigned`
        
        :param value: ID категории по умолчанию.
        :type value: int
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.id_category_default = value
            
        except ProductFieldException as ex:
            """ @todo - требуется валидатор"""
            logger.critical(f"""Ошибка заполнения поля: 'id_category_default' данными {value}\n            Ошибка: """, ex)
            return        

    @property
    def additional_categories(self) -> dict | None:
        """
        Свойство для получения словаря дополнительных категорий товара.

        :return: Словарь категорий товара или None.
        :rtype: Optional[Dict]
        """

        return self.presta_fields.associations.categories or None

    
    @additional_categories.setter    
    def additional_categories(self, value: int | list[int]):
        """
        Свойство-сеттер для дополнительных категорий.
        
        При задании доп ключей предыдущие значения заменяются новыми из `additional_categories`.
        Для добавления новых к уже существующим используй функцию `additional_categories_append()`.

        :param value: ID дополнительной категории или список ID дополнительных категорий.
        :type value: int | list[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
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
                logger.error(f"""Ошибка заполнения поля: 'additional_categories' данными {v}\n                Ошибка: """, ex)  
                return
   
# # # #   5   Магазин по умолчанию
    
    @property
    def id_shop_default(self) -> int:
        """
        Свойство для получения `id_shop_default` (ps_product.id_shop_default: int(10) unsigned).
        
        :details: ID магазина по умолчанию. Используется multishop
        :return: ID магазина по умолчанию.
        :rtype: int
        """

        return self.presta_fields.id_shop_default or ''
    
    @id_shop_default.setter
    def id_shop_default(self, value: int = None):
        """
        Свойство-сеттер для `id_shop_default`.
        
        `ID` магазина заказчика

        :param value: ID магазина по умолчанию.
        :type value: Optional[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.id_shop_default = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop_default' данными {value}\n            Ошибка: """, ex)
            return

# # #   5   Магазин по умолчанию
    
    @property
    def id_shop(self) -> int:
        """
        Свойство для получения `id_shop` (ps_product.id_shop_default: int(10) unsigned).
        
        :details: ID магазина по умолчанию. Используется multishop
        :return: ID магазина или ''.
        :rtype: int
        """

        return self.presta_fields.id_shop_default or ''
    
    @id_shop.setter
     
    def id_shop(self, value: int = None):
        """
        Свойство-сеттер для `id_shop`.
        
        `ID` магазина заказчика

        :param value: ID магазина.
        :type value: Optional[int]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.id_shop = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop' данными {value}\n            Ошибка: """, ex)
            return


#   6   НДС (Израиль - обычно 13)
    
    @property
    def id_tax(self) -> int:
        """
        Свойство для получения `id_tax` (ps_product.id_tax: int(10) unsigned).

        :return: ID налога или ''.
        :rtype: int
        """

        return self.presta_fields.id_tax or ''

    
    @id_tax.setter
         
    def id_tax(self, value: int ):
        """
        Свойство-сеттер для `id_tax`.
        
        `ID` ндс. מע"מ = 13
        
        :param value: ID налога.
        :type value: int
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.id_tax = int(value)

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Tax rule ID' данными {value}\n            Ошибка: """, ex)
            return

#   7   Распродажа - Mivtza
    
    @property
    
    def on_sale(self) -> int:
        """
        Свойство для получения `on_sale` (ps_product.on_sale: tinyint(1)  unsigned).

        :return: Флаг распродажи или ''.
        :rtype: int
        """

        return self.presta_fields.on_sale  or ''

    @on_sale.setter
         
    def on_sale(self, value = 0 ):
        """
        Свойство-сеттер для `on_sale`.
        
        `1` - распродажа

        :param value: 1 или 0. По умолчанию 0.
        :type value: int, optional
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: None
        :rtype: None
        """
        try:
            self.presta_fields.on_sale = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'On sale (0/1)' данными {value}\n            Ошибка: """, ex)
            return

#   8 online_only: только через онлайн
    
    @property
    def online_only(self) -> int:
        """
        Свойство для получения `online_only` (ps_product.online_only: tinyint(1) unsigned).
        
        :details: товар только онлайн
        :return: Флаг онлайн-продаж или ''.
        :rtype: int
        """

        return self.presta_fields.online_only or ''
    
    
    @online_only.setter
    def online_only(self, value = 0) -> bool:
        """
        Свойство-сеттер для `online_only`.
        
        :param value: 1 или 0. По умолчанию 0.
        :type value: int, optional
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
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
        """
        Свойство для получения `ean13` (ps_product.ean13  varchar(13)).
        
        :return: EAN13 или None.
        :rtype: Optional[str]
        """
        return self.presta_fields.ean13 or ''

    @ean13.setter
    def ean13(self, value:str = None, lang:str = 'en') -> bool:
        """
        Свойство-сеттер для `ean13`.

        :param value: Значение EAN13.
        :type value: Optional[str]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        try:
            self.presta_fields.ean13 = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ean13' данными {value}""", ex)
            return

#   10
    @property
    def isbn(self) -> str | None:
        """
        Свойство для получения `isbn`.
        
        :return: ISBN или None.
        :rtype: Optional[str]
        """
        return self.presta_fields.isbn or ''
        
    @isbn.setter
    def isbn(self, value:str = None, lang:str = 'en') -> bool:
        """
        Свойство-сеттер для `isbn`.
        
        :param value: Значение ISBN.
        :type value: Optional[str]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
         :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        try:
            self.presta_fields.isbn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}\n            Ошибка: """, ex)
            return

#   11
    
    @property
    def upc(self):
        """
        Свойство для получения `upc`.
        
        :return: UPC или ''.
        :rtype: str
        """
        return self.presta_fields.upc or ''
    
    
    @upc.setter
    def upc(self, value:str = None, lang:str = 'en') -> str | None:
        """
        Свойство-сеттер для `upc`.
        
        :param value: Значение UPC.
        :type value: Optional[str]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
         :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        try:
            self.presta_fields.upc = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}\n            Ошибка: """, ex)
            return

#   12  mpn
    
    @property
    def mpn(self) -> str:
        """
        Свойство для получения `mpn`.

        :return: MPN или ''.
        :rtype: str
        """
        return self.presta_fields.mpn or ''

    
    @mpn.setter
    def mpn(self, value:str = None, lang:str = 'en') -> bool:
        """
        Свойство-сеттер для `mpn`.
        
        :param value: Значение MPN.
        :type value: Optional[str]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
        try:
            self.presta_fields.mpn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
                         Ошибка заполнения поля: `ps_product.mpn` данными {value}\n                         -----------------\n                            Ошибка: """, ex)
            return

#   13   ecotax
    
    @property
    def ecotax(self):
        """
        Свойство для получения `ecotax`.

        :return: Ecotax или ''.
        :rtype: str
        """
        return self.presta_fields.ecotax or ''

    @ecotax.setter
    def ecotax(self, value:str = None, lang:str = 'en') -> bool:
        """
        Свойство-сеттер для `ecotax`.
        
        :param value: Значение ecotax.
        :type value: Optional[str]
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        :return: True в случае успеха, иначе None.
        :rtype: Optional[bool]
        """
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
    #         logger.error(f"""Ошибка заполнения поля: 'quantity' данными {value}\n    #