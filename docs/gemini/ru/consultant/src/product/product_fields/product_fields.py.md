## Анализ кода модуля product_fields.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы и методы, что делает его более читаемым и поддерживаемым.
    - Использованы property и setter для доступа и изменения полей, что обеспечивает инкапсуляцию данных.
    - Есть базовая обработка ошибок с использованием `try-except` блоков и логирования с помощью `logger.error`.
    - Использованы `j_loads` и `j_loads_ns` для загрузки JSON, что соответствует инструкции.
    - Присутствует подробная документация в формате reStructuredText (RST) для класса и его методов.
    - Для перечислений использованы Enum.

- Минусы
    - Много повторяющегося кода в setter-ах, особенно в блоках обработки исключений, что можно было бы вынести в отдельную функцию.
    - Использование `...` как заглушки нежелательно в финальном коде и должно быть заменено на логику или удалено.
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - Присутствуют комментарии `#`, не имеющие описания кода.
    - Некоторые `setter` методы не возвращают значения, хотя по логике должны.
    - Не всегда используется явное указание типа при возврате значения в методах.
    -  В блоках `try-except`  в основном только логирование, но нет возврата ошибки

**Рекомендации по улучшению**

1. **Улучшение обработки ошибок**:
   - Создать декоратор для обработки ошибок в setter-ах, чтобы избежать дублирования кода. Декоратор должен логировать ошибку и возвращать `False`.
   - В блоках `try-except` добавить возвращение `False` или `None` в случае ошибки, чтобы вызывающий код мог обработать ошибку.
2. **Улучшение документации**:
   - Все комментарии должны соответствовать стандарту reStructuredText (RST), включая docstring.
   - Добавить более подробные комментарии к каждому блоку кода.
   - Уточнить docstring для параметров функций и методов, добавив типы.
   - Использовать более точные формулировки в комментариях и docstring.
3. **Улучшение структуры кода**:
   - Заменить все `...` на реальный код или удалить.
   - Вынести дублирующийся код в отдельные функции или методы.
   - Добавить проверки типов в setter-ах перед присваиванием значений.
   - Пересмотреть логику `locale` и убедиться, что она соответствует требованиям.
4.  **Общие рекомендации**:
   - Пересмотреть использование `getattr` и `setattr`, возможно, стоит использовать более явный подход.
   - Уточнить и унифицировать типы возвращаемых значений.
   -  Использовать type hinting везде, где это необходимо, чтобы улучшить читаемость и предотвратить ошибки.
5.  **Дополнительно**:
    - Добавить валидаторы там где они указанны в `todo`.
    - Добавить валидаторы для типов входных значений в сеттерах.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с полями товара PrestaShop.
=========================================================================================

Этот модуль определяет класс :class:`ProductFields`, который используется для управления и
манипулирования полями товаров в контексте API PrestaShop. Включает в себя загрузку
дефолтных значений, установку и получение значений для различных полей товара.

Модуль также предоставляет возможность работы с мультиязычными полями.

Пример использования
--------------------

.. code-block:: python

    from src.product.product_fields.product_fields import ProductFields

    product_fields = ProductFields()
    product_fields.id_product = 123
    print(product_fields.id_product)

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

          Column Name                 Data Type               Allowed NULL
  1       `id_product`                int(10) unsigned        [V]
  2       `id_supplier`               int(10) unsigned        [V]
  3       `id_manufacturer`           int(10) unsigned        [v]
  4       `id_category_default`       int(10) unsigned        [v]
  5       `id_shop_default`           int(10) unsigned        [v]
  6       `id_tax`                    int(11) unsigned        [v]
  7       `on_sale`                   tinyint(1) unsigned     [v]
  8       `online_only`               tinyint(1) unsigned     [v]
  9       `ean13`                     varchar(13)             [v]
  10      `isbn`                      varchar(32)
  11      `upc`                       varchar(12)
  12      `mpn`                       varchar(40)
  13      `ecotax`                    decimal(17,6)
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

class ProductFields:
    """
    Класс для представления полей продукта PrestaShop.

    Этот класс управляет полями продуктов PrestaShop, загружая их из файла,
    устанавливая и получая значения для этих полей.
    """

    def __init__(self) -> None:
        """
        Инициализирует класс `ProductFields`.

        Загружает список полей продукта, устанавливает соответствие языков и
        инициализирует `presta_fields` и `assist_fields_dict` для хранения
        данных.
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
        Загружает список полей продукта из текстового файла.

        :return: Список строк, представляющих поля продукта.
        :rtype: List[str]
        """
        return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)

    def _payload(self) -> bool:
        """
        Загружает значения по умолчанию для полей продукта из JSON файла.

        :return: `True` если значения успешно загружены, `False` в противном случае.
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
        Возвращает словарь ассоциаций.
        """
        return self.presta_fields.associations or None

    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]) -> None:
        """
        Устанавливает словарь ассоциаций.

        :param value: Словарь ассоциаций.
        :type value: Dict[str, Optional[str]]
        """
        self.presta_fields.associations = value

    @property
    def id_product(self) -> Optional[int]:
        """
        :return:  `ps_product.id: int(10) unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: Optional[int] = None) -> None:
        """
        Устанавливает `ID` товара.

        Если `ID` товара передается, он устанавливается в поле `id_product`.
        Для нового товара `ID` будет получен из системы при занесении в базу.
        
        :param value: ID товара, по умолчанию `None`.
        :type value: Optional[int]
        
        :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_product = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ID' данными {value}\nОшибка: {ex}")
            return

    @property
    def id_supplier(self) -> Optional[int]:
        """
         :return: `ps_product.id_supplier: int(10) unsigned`
         :rtype: Optional[int]
        """
        return self.presta_fields.id_supplier or None

    @id_supplier.setter
    def id_supplier(self, value: Optional[int] = None) -> bool:
        """
        Устанавливает `ID` поставщика товара.

        :param value: ID поставщика, по умолчанию `None`.
        :type value: Optional[int]

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.id_supplier = value
            return True

        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: `ps_product.id_supplier` данными {value}\nОшибка: {ex}")
            return False

    @property
    def id_manufacturer(self) -> Optional[int]:
        """
        :return: `ps_product.id_manufacturer: int(10) unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_manufacturer or None

    @id_manufacturer.setter
    def id_manufacturer(self, value: Optional[int] = None) -> None:
        """
        Устанавливает `ID` производителя товара.

        Бренд может быть передан как по имени, так и по ID.

        :param value: ID производителя, по умолчанию `None`.
        :type value: Optional[int]
        
         :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_manufacturer = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'Brand' данными {value}\nОшибка: {ex}")
            return

    @property
    def id_category_default(self) -> Optional[int]:
        """
        :return: `ps_product.id_category_default: int(10) unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_category_default or None

    @id_category_default.setter
    def id_category_default(self, value: int) -> None:
        """
         Устанавливает `ID` родительской категории товара.

        :param value: ID родительской категории товара
        :type value: int
        
        :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_category_default = value

        except ProductFieldException as ex:
            logger.critical(f"Ошибка заполнения поля: 'id_category_default' данными {value}\nОшибка: {ex}")
            return

    @property
    def additional_categories(self) -> Optional[dict]:
        """
          :return: Словарь дополнительных категорий товара из `ps_category_product`.
          :rtype: Optional[dict]
        """
        return self.presta_fields.associations.categories if self.presta_fields.associations else None

    @additional_categories.setter
    def additional_categories(self, value: int | list[int]) -> None:
        """
        Устанавливает дополнительные категории для товара.

        Если передано несколько категорий, предыдущие значения будут заменены.

        :param value: ID или список ID дополнительных категорий.
        :type value: int | list[int]
       
        :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        value = value if isinstance(value, list) else [value]

        for v in value:
            if not isinstance(v, int):
                logger.error(f'недопустимое значение для категории {v=}, Должен быть `int`')
                continue

            try:
                if not self.presta_fields.associations:
                     self.presta_fields.associations = {'categories':{}}
                if not  self.presta_fields.associations.get('categories'):
                    self.presta_fields.associations['categories'] = {}
                self.presta_fields.associations['categories'].update({'id': v})

            except ProductFieldException as ex:
                logger.error(f"Ошибка заполнения поля: 'additional_categories' данными {v}\nОшибка: {ex}")
                return

    @property
    def id_shop_default(self) -> Optional[int]:
        """
        :return: `ps_product.id_shop_default: int(10) unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default or ''

    @id_shop_default.setter
    def id_shop_default(self, value: Optional[int] = None) -> None:
        """
        Устанавливает `ID` магазина по умолчанию.

        :param value: ID магазина, по умолчанию `None`.
        :type value: Optional[int]
        
         :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_shop_default = value

        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'id_shop_default' данными {value}\nОшибка: {ex}")
            return

    @property
    def id_shop(self) -> Optional[int]:
        """
        :return: `ps_product.id_shop_default: int(10) unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default or ''

    @id_shop.setter
    def id_shop(self, value: Optional[int] = None) -> None:
        """
        Устанавливает `ID` магазина.

        :param value: ID магазина, по умолчанию `None`.
        :type value: Optional[int]

         :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_shop = value

        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'id_shop' данными {value}\nОшибка: {ex}")
            return

    @property
    def id_tax(self) -> Optional[int]:
        """
         :return: `ps_product.id_tax: int(10) unsigned`
         :rtype: Optional[int]
        """
        return self.presta_fields.id_tax or ''

    @id_tax.setter
    def id_tax(self, value: int) -> None:
        """
        Устанавливает `ID` налога.

        :param value: ID налога.
        :type value: int
        
        :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.id_tax = int(value)

        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'Tax rule ID' данными {value}\nОшибка: {ex}")
            return

    @property
    def on_sale(self) -> Optional[int]:
        """
        :return: `ps_product.on_sale: tinyint(1)  unsigned`
        :rtype: Optional[int]
        """
        return self.presta_fields.on_sale or ''

    @on_sale.setter
    def on_sale(self, value: int = 0) -> None:
        """
        Устанавливает флаг распродажи.

        :param value: 1 - распродажа, 0 - нет. По умолчанию 0.
        :type value: int, optional
        
        :raises ProductFieldException: если произошла ошибка при установке значения.
        """
        try:
            self.presta_fields.on_sale = value

        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'On sale (0/1)' данными {value}\nОшибка: {ex}")
            return

    @property
    def online_only(self) -> Optional[int]:
        """
         :return: `ps_product.online_only: tinyint(1) unsigned`
         :rtype: Optional[int]
        """
        return self.presta_fields.online_only or ''

    @online_only.setter
    def online_only(self, value: int = 0) -> bool:
        """
        Устанавливает флаг "только онлайн".

        :param value: 1 - только онлайн, 0 - нет. По умолчанию 0.
        :type value: int, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.online_only = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'online_only' данными {value}", ex)
            return False

    @property
    def ean13(self) -> Optional[str]:
        """
         :return: `ps_product.ean13  varchar(13)`
         :rtype: Optional[str]
        """
        return self.presta_fields.ean13 or ''

    @ean13.setter
    def ean13(self, value: Optional[str] = None, lang: str = 'en') -> bool:
        """
        Устанавливает штрихкод EAN13.

        :param value: Штрихкод EAN13, по умолчанию `None`.
        :type value: Optional[str]
        :param lang: Язык, по умолчанию 'en'.
        :type lang: str, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.ean13 = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ean13' данными {value}", ex)
            return False

    @property
    def isbn(self) -> Optional[str]:
        """
         :return: `isbn`
         :rtype: Optional[str]
        """
        return self.presta_fields.isbn or ''

    @isbn.setter
    def isbn(self, value: Optional[str] = None, lang: str = 'en') -> bool:
        """
        Устанавливает ISBN товара.

        :param value: ISBN, по умолчанию `None`.
        :type value: Optional[str]
        :param lang: Язык, по умолчанию 'en'.
        :type lang: str, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.isbn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'isbn' данными {value}\nОшибка: {ex}")
            return False

    @property
    def upc(self) -> Optional[str]:
        """
         :return:  `upc`
         :rtype: Optional[str]
        """
        return self.presta_fields.upc or ''

    @upc.setter
    def upc(self, value: Optional[str] = None, lang: str = 'en') -> bool:
        """
         Устанавливает UPC товара.

        :param value: UPC, по умолчанию `None`.
        :type value: Optional[str]
        :param lang: Язык, по умолчанию 'en'.
        :type lang: str, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.upc = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'isbn' данными {value}\nОшибка: {ex}")
            return False

    @property
    def mpn(self) -> Optional[str]:
        """
         :return: `ps_product.mpn`
         :rtype: Optional[str]
        """
        return self.presta_fields.mpn or ''

    @mpn.setter
    def mpn(self, value: Optional[str] = None, lang: str = 'en') -> bool:
        """
         Устанавливает MPN товара.

        :param value: MPN, по умолчанию `None`.
        :type value: Optional[str]
         :param lang: Язык, по умолчанию 'en'.
        :type lang: str, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.mpn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
                         Ошибка заполнения поля: `ps_product.mpn` данными {value}
                         -----------------
                            Ошибка: {ex}""")
            return False

    @property
    def ecotax(self) -> Optional[str]:
        """
         :return: `ps_product.ecotax`
         :rtype: Optional[str]
        """
        return self.presta_fields.ecotax or ''

    @ecotax.setter
    def ecotax(self, value: Optional[str] = None, lang: str = 'en') -> bool:
        """
        Устанавливает `ecotax` товара.

        :param value: `ecotax`, по умолчанию `None`.
        :type value: Optional[str]
        :param lang: Язык, по умолчанию 'en'.
        :type lang: str, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.ecotax = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ecotax' данными {value}", ex)
            return False

    @property
    def minimal_quantity(self) -> Optional[int]:
        """
          :return: `ps_product.minimal_quantity`
          :rtype: Optional[int]
        """
        return self.presta_fields.minimal_quantity or ''

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 0) -> bool:
        """
        Устанавливает минимальное количество товара.

        :param value: Минимальное количество товара, по умолчанию 0.
        :type value: int, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.minimal_quantity = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'minimal_quantity' данными {value}\nОшибка: {ex}")
            return False

    @property
    def low_stock_threshold(self) -> Optional[int]:
        """
         :return: `ps_product.low_stock_threshold`
         :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_threshold or ''

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: Optional[int] = None) -> bool:
        """
         Устанавливает порог низкого запаса товара.

        :param value: Порог низкого запаса, по умолчанию `None`.
        :type value: Optional[int]

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.low_stock_threshold = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_threshold' данными {value}
            Ошибка: {ex}""")
            return False

    @property
    def low_stock_alert(self) -> Optional[int]:
        """
         :return:  `ps_product.low_stock_alert`
         :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_alert or ''

    @low_stock_alert.setter
    def low_stock_alert(self, value: int = 0) -> bool:
        """
        Устанавливает флаг уведомления о низком запасе товара.

        :param value: Флаг уведомления (0 или 1), по умолчанию 0.
        :type value: int, optional

        :return: `True` если значение установлено успешно, `False` если возникла ошибка.
        :rtype: bool
        """
        try:
            self.presta_fields.low_stock_alert = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_alert' данными {value}
            Ошибка:{ex}""")
            return False

    @property
    def price(self) -> Optional[float]:
        """
         :return: `ps_product.price`
         :rtype: Optional[float]
        """
        return self.presta_fields.price or 0

    @price.setter
    def price(self, value: str | int | float) -> bool:
         """