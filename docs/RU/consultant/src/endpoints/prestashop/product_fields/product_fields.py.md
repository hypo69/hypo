## Анализ кода модуля `product_fields`

**Качество кода: 7/10**
-   **Плюсы:**
    -   Хорошая структура и организация кода с использованием `dataclass` для представления полей товара.
    -   Применение `property` и `setter` для доступа к полям, что обеспечивает инкапсуляцию.
    -   Использование `SimpleNamespace` для хранения данных.
    -   Применение `logger` для логирования ошибок.
    -   Документирование функций и свойств с использованием docstrings.
    -   Наличие enum-ов для полей с ограниченным набором значений.
-   **Минусы:**
    -   Избыточное использование `try-except` блоков.
    -   Много повторяющегося кода в setter-ах, которые можно оптимизировать.
    -   Не всегда последовательное использование типов данных в setter-ах.
    -   Некоторые docstring неполные, например, отсутствуют @details.
    -   Комментарии в коде иногда не соответствуют PEP-8.
    -   Местами используется `...` как заглушка, что нежелательно в готовом коде.
    -   Некоторые переменные не имеют аннотации типов.
    -   Слишком много закомментированного кода.
    -   Много кода который дублируется

**Рекомендации по улучшению**
1.  **Устранить избыточность `try-except`**:
    -   Использовать общую функцию для установки значений полей с обработкой ошибок.
2.  **Оптимизировать `setter`**:
    -   Создать общую логику для setter, которая будет обрабатывать все типы данных и выводить ошибки.
3.  **Унифицировать типы данных**:
    -   Привести типы данных в setter к одному стандарту, где это возможно.
4.  **Заполнить docstring**:
    -   Дополнить docstring, включая все необходимые секции, например, `@details`, `@param`, `@returns`, `@raises`.
5.  **Улучшить комментарии**:
    -   Следовать PEP-8 при написании комментариев, то есть один пробел после `#`.
6.  **Убрать заглушки `...`**:
    -   Заменить `...` на конкретный код или логирование.
7.  **Добавить аннотацию типов**:
    -   Аннотировать типы переменных, где это возможно.
8.  **Удалить лишний код**:
    -   Удалить закомментированный код, который не используется.
9.  **Объединить повторяющийся код**
    -    Создать общую логику для обработки свойств
10. **Добавить документацию для модуля**
    -   Добавить общую документацию для модуля в начале файла
    -   Добавить инструкцию по использованию модуля

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль `product_fields`
=========================================================================================
Модуль содержит класс `ProductFields`, который используется для представления и управления полями
товара в контексте PrestaShop. Этот модуль обеспечивает структурированный доступ к полям товара
и их значениям, а также включает методы для валидации и преобразования данных.

Класс `ProductFields` предоставляет интерфейс для работы с полями товаров PrestaShop,
включая как основные поля из таблицы `ps_product`, так и мультиязычные поля из `ps_product_lang`.
Он загружает значения полей по умолчанию из файлов конфигурации, обеспечивая согласованность данных.

Использование
-------------
Для работы с классом `ProductFields`, сначала необходимо создать экземпляр, передав индекс языка.
Все свойства класса `ProductFields` соответствуют полям в таблицах PrestaShop и имеют геттеры и сеттеры.

Пример использования
--------------------
.. code-block:: python

    from src.endpoints.prestashop.product_fields.product_fields import ProductFields
    from src.logger import logger
    
    try:
        product = ProductFields(lang_index=1)
        product.name = "Новый товар"
        product.price = 19.99
        product.active = 1
        
        print(f"Имя товара: {product.name}")
        print(f"Цена товара: {product.price}")
        print(f"Активность товара: {product.active}")
    except Exception as ex:
        logger.error("Произошла ошибка при создании объекта ProductFields", ex)


.. todo:: Внимательно посмотреть, как работает langdetect
"""

import asyncio
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional, Any
from types import SimpleNamespace

from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import read_text_file
from src.logger import logger
from src.logger.exceptions import ProductFieldException


@dataclass
class ProductFields:
    """Класс, описывающий поля товара в формате API PrestaShop."""

    lang_index: int
    product_fields_list: List[str] = field(init=False)
    presta_fields: SimpleNamespace = field(init=False)
    assist_fields_dict: Dict[str, Any] = field(default_factory=lambda: {
        'default_image_url': '',
        'images_urls': []
    })
    base_path: Path = gs.path.endpoints / 'prestashop'

    def __post_init__(self):
        """Инициализация класса после создания экземпляра. Загружаются данные полей, языков и их идентификаторов."""
        if not self._payload():
            logger.error("Ошибка загрузки полей")
            return

    def _payload(self) -> bool:
        """Загрузка дефолтных значений полей.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        presta_fields_list: list = read_text_file(self.base_path / 'product_fields' / 'fields_list.txt', as_list=True)
        if not presta_fields_list:
            logger.error("Ошибка загрузки файла со списком полей ")
            return False

        try:
            self.presta_fields: SimpleNamespace = SimpleNamespace(**{key: None for key in presta_fields_list})
        except Exception as ex:
            logger.error("Ошибка конвертации", ex)
            return False

        data_ns: SimpleNamespace = j_loads_ns(
            self.base_path / 'product_fields' / 'product_fields_default_values.json')
        if not data_ns:
            logger.error("Ошибка загрузки полей из файла product_fields_default_values.json")
            return False
        try:
            for name in data_ns.__dict__:  # используем __dict__ для итерации по атрибутам
                value = getattr(data_ns, name)
                setattr(self.presta_fields, name, value)  # Use setattr on presta_fields
            return True
        except Exception as ex:
            logger.error(f"Exception ", ex)
            return False

    def _set_field(self, field_name: str, value: Any) -> bool:
        """Устанавливает значение поля и обрабатывает ошибки.

        Args:
            field_name (str): Название поля для установки.
            value (Any): Значение для установки.

        Returns:
             bool: True если поле успешно установлено, False в противном случае.
        Raises:
            ProductFieldException: Если возникает ошибка при установке значения поля.
        """
        try:
            setattr(self.presta_fields, field_name, value)
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: '{field_name}' данными {value}", ex)
            return False


    @property
    def associations(self) -> Optional[Dict]:
        """Возвращает словарь ключей ассоциаций."""
        return self.presta_fields.associations or None

    @associations.setter
    def associations(self, value: Dict[str, Optional[str]]):
        """Устанавливает словарь ассоциаций."""
        self.presta_fields.associations = value

    @property
    def id_product(self) -> Optional[int]:
        """ <sub>*[property]*</sub>  `ps_product.id: int(10) unsigned` """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int = None):
        """ <sub>*[setter]*</sub>  `ID` товара. *для нового тoвара id назначется из `PrestaShop`*

        @details Запись нового товара в престашоп делается в два шага:
        -> в престасшоп заносятся парамеры, которые не связаны с ID, например, название товара, артикул и т.п.
        <- От престашоп возвращается словарь, в котором установлено ID.
        -> теперь можно грузить фото, доп парамерты, короче все, что завязано на id товара
        @param id_product `int`  :  Требуется при операциях над существующим товаром. `ps_product.id` .
        Для нового товара ID вернется из системы при занесении товара в базу данных.
        @returns bool `True` if success, else `False`
        """
        self._set_field('id_product', value)


    @property
    def id_supplier(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.id_supplier: int(10) unsigned`
         @details: привязываю товар к id поставщика
        """
        return self.presta_fields.id_supplier or None


    @id_supplier.setter
    def id_supplier(self, value: int = None):
        """  <sub>*[setter]*</sub> """
        self._set_field('id_supplier', value)

    @property
    def id_manufacturer(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.id_manufacturer: int(10) unsigned`
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
        self._set_field('id_manufacturer', value)


    @property
    def id_category_default(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.id_category_default: int(10) unsigned`
         @details: привязываю товар к главной категории для этого товара
        """
        return self.presta_fields.id_category_default or None

    @id_category_default.setter
    def id_category_default(self, value: int):
        """  <sub>*[setter]*</sub> Сюда передается та категория, которая будет однознчно - родительская `ps_product.id_category_default: int(10) unsigned`"""
        self._set_field('id_category_default', value)

    @property
    def additional_categories(self) -> Optional[dict]:
        """  <sub>*[property]*</sub>
        возвращает словарь категорий товара восстановленный из файла сценария таблица `ps_category_product`"""
        return self.presta_fields.associations.categories if hasattr(self.presta_fields.associations, 'categories') else None

    @additional_categories.setter
    def additional_categories(self, value: int | list[int]):
        """  <sub>*[setter]*</sub>   Дополнительные к основной категории.
        При задании доп ключей прдеыдущие значения заменяются новыми из `additional_categories`.
        Для добавления новых к уже существующим используй  функцию additional_categories_append()
        """
        value = value if isinstance(value, list) else [value]

        for v in value:
            try:
                v: int = int(v)
            except Exception as ex:
                logger.error(f'недопустимое значение для категории {v=}, Должен быть `int`')
                continue

            try:
                if not hasattr(self.presta_fields.associations, 'categories'):
                    setattr(self.presta_fields.associations, 'categories', SimpleNamespace(category=[SimpleNamespace(**{'id': v})]))
                    continue

                self.presta_fields.associations.categories.category.append(SimpleNamespace(**{'id': v}))

            except Exception as ex:
                logger.error(f"Ошибка заполнения поля: 'additional_categories' данными {v}", ex)
                return

    @property
    def id_shop_default(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
         @details: ID магазина по умолчанию . Используется в multishop"""
        return self.presta_fields.id_shop_default or None

    @id_shop_default.setter
    def id_shop_default(self, value: int = None):
        """  <sub>*[setter]*</sub>   `ps_product.id_shop_default: int(10) unsigned`
            `ID` магазина заказчика """
        self._set_field('id_shop_default', value or 1)

    @property
    def id_shop(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
         @details: ID магазина по умолчанию . Используется multishop"""
        return self.presta_fields.id_shop_default or None

    @id_shop.setter
    def id_shop(self, value: int = None):
        """  <sub>*[setter]*</sub>   `ps_product.id_shop: int(10) unsigned`
            `ID` магазина заказчика """
        self._set_field('id_shop', value or 1)

    @property
    def id_tax(self) -> Optional[int]:
        """  <sub>*[property]*</sub> tax_rule `int`  :  `ID` НДС  `ps_product.id_tax: int(10) unsigned`"""
        return self.presta_fields.id_tax or None

    @id_tax.setter
    def id_tax(self, value: int = None):
        """   <sub>*[setter]*</sub>  `ID` ндс. מע''מ = 13 """
        self._set_field('id_tax', int(value))

    @property
    def on_sale(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.on_sale: tinyint(1)  unsigned`"""
        return self.presta_fields.on_sale or None

    @on_sale.setter
    def on_sale(self, value: int = 0):
        """  <sub>*[setter]*</sub> `1` - распродажа
        @param value (int, optional): Defaults to 0.
        @returns bool: _ @details_
        """
        self._set_field('on_sale', value)

    @property
    def online_only(self) -> Optional[int]:
        """   <sub>*[property]*</sub>   `ps_product.online_only: tinyint(1) unsigned`
        field DB type: tinyint(1) unsigned
         @details: товар только онлайн """
        return self.presta_fields.online_only or None

    @online_only.setter
    def online_only(self, value: int = 0) -> bool:
        """   <sub>*[setter]*</sub> """
        return self._set_field('online_only', value)

    @property
    def ean13(self) -> Optional[str]:
        """  <sub>*[property]*</sub>   `ps_product.ean13  varchar(13)`
        field DB type:
         @details: __prod_desc__"""
        return self.presta_fields.ean13 or None

    @ean13.setter
    def ean13(self, value: str = None) -> bool:
        """   <sub>*[setter]*</sub>   `ean13`
        field DB type:  varchar(13)
         @details: __prod_desc__"""
        return self._set_field('ean13', value)

    @property
    def isbn(self) -> Optional[str]:
        """   <sub>*[property]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__"""
        return self.presta_fields.isbn or None

    @isbn.setter
    def isbn(self, value: str = None) -> bool:
        """   <sub>*[setter]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__"""
        return self._set_field('isbn', value)

    @property
    def upc(self) -> Optional[str]:
        """  <sub>*[property]*</sub>   `upc`
        field DB type: varchar(12)
         @details: __prod_desc__"""
        return self.presta_fields.upc or None

    @upc.setter
    def upc(self, value: str = None) -> bool:
        """   <sub>*[setter]*</sub>   `ps_product.upc`
        field DB type: varchar(12)
         @details: __prod_desc__"""
        return self._set_field('upc', value)

    @property
    def mpn(self) -> Optional[str]:
        """  <sub>*[property]*</sub>   `ps_product.mpn`
        field DB type: varchar(40)
         @details: __prod_desc__"""
        return self.presta_fields.mpn or None

    @mpn.setter
    def mpn(self, value: str = None) -> bool:
        """   <sub>*[setter]*</sub>  """
        return self._set_field('mpn', value)

    @property
    def ecotax(self) -> Optional[str]:
        """  <sub>*[property]*</sub>   `ps_product.ecotax`
        field DB type:  decimal(17,6)
         @details: __prod_desc__"""
        return self.presta_fields.ecotax or None

    @ecotax.setter
    def ecotax(self, value: str = None) -> bool:
        """   <sub>*[setter]*</sub>  """
        return self._set_field('ecotax', value)


    @property
    def minimal_quantity(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.minimal_quantity`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.minimal_quantity or None

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('minimal_quantity', value)

    @property
    def low_stock_threshold(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.low_stock_threshold`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.low_stock_threshold or None

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: str = '') -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('low_stock_threshold', value)

    @property
    def low_stock_alert(self) -> Optional[int]:
        """  <sub>*[property]*</sub>  `ps_product.low_stock_alert`
        field DB type: tinyint(1)
         @details: __prod_desc__"""
        return self.presta_fields.low_stock_alert or None

    @low_stock_alert.setter
    def low_stock_alert(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('low_stock_alert', value)

    @property
    def price(self) -> Optional[float]:
        """  <sub>*[property]*</sub>  `ps_product.price`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.price or None

    @price.setter
    def price(self, value: str | int | float) -> bool:
        """  <sub>*[setter]*</sub>   """
        if not value:
            return False
        return self._set_field('price', value)

    @property
    def wholesale_price(self) -> Optional[float]:
        """  <sub>*[property]*</sub>  `ps_product.wholesale_price`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.wholesale_price or None

    @wholesale_price.setter
    def wholesale_price(self, value: str = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('wholesale_price', value)

    @property
    def unity(self) -> Optional[str]:
        """  <sub>*[property]*</sub>  `ps_product.unity`
        field DB type: varchar(255)
         @details: __prod_desc__"""
        return self.presta_fields.unity or None

    @unity.setter
    def unity(self, value: str = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('unity', value)

    @property
    def unit_price_ratio(self) -> Optional[float]:
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
        return self.presta_fields.unit_price_ratio or None

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('unit_price_ratio', value)

    @property
    def additional_shipping_cost(self) -> Optional[float]:
        """  <sub>*[property]*</sub> `ps_product.additional_shipping_cost`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.additional_shipping_cost or None

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('additional_shipping_cost', value)

    @property
    def reference(self) -> Optional[str]:
        """  <sub>*[property]*</sub> `ps_product.reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__
        """
        return self.presta_fields.reference or None

    @reference.setter
    def reference(self, value: str = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('reference', str(value))

    @property
    def supplier_reference(self) -> Optional[str]:
        """  <sub>*[property]*</sub>  `ps_product.supplier_reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__
        """
        return self.presta_fields.supplier_reference or None

    @supplier_reference.setter
    def supplier_reference(self, value: str = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('supplier_reference', str(value))

    @property
    def location(self) -> Optional[str]:
        """  <sub>*[property]*</sub> `ps_product.location`
        field DB type: varchar(255)
         @details: __prod_desc__"""
        return self.presta_fields.location or None

    @location.setter
    def location(self, value: str = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('location', value)

    @property
    def width(self) -> Optional[float]:
        """  <sub>*[property]*</sub> `ps_product.width`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.width or None

    @width.setter
    def width(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('width', value)

    @property
    def height(self) -> Optional[float]:
        """  <sub>*[property]*</sub> `ps_product.height`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.height or None

    @height.setter
    def height(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('height', value)

    @property
    def depth(self) -> Optional[float]:
        """  <sub>*[property]*</sub> `[28] ps_product.depth  decimal(20,6)`
        field DB type:
         @details: __prod_desc__"""
        return self.presta_fields.depth or None

    @depth.setter
    def depth(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('depth', value)

    @property
    def weight(self) -> Optional[float]:
        """  <sub>*[property]*</sub> `ps_product.weight`
        field DB type: decimal(20,6)
         @details: __prod_desc__"""
        return self.presta_fields.weight or None

    @weight.setter
    def weight(self, value: float = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('weight', value)

    @property
    def volume(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.state`
        field DB type: int(11)
         @details: __prod_desc__"""
        return self.presta_fields.volume or None

    @volume.setter
    def volume(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('volume', value)

    @property
    def out_of_stock(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.out_of_stock`
        field DB type: int(10)
         @details: __prod_desc__"""
        return self.presta_fields.out_of_stock or None

    @out_of_stock.setter
    def out_of_stock(self, value: int = None) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('out_of_stock', value)

    @property
    def additional_delivery_times(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.additional_delivery_times tinyint(1)`
         @details: __prod_desc__"""
        return self.presta_fields.additional_delivery_times or None

    @additional_delivery_times.setter
    def additional_delivery_times(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('additional_delivery_times', value)

    @property
    def quantity_discount(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.quantity_discount`
        field DB type: tinyint(1)
         @details: __prod_desc__"""
        return self.presta_fields.quantity_discount or None

    @quantity_discount.setter
    def quantity_discount(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('quantity_discount', value)

    @property
    def customizable(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.customizable`
        field DB type: tinyint(2)
         @details: __prod_desc__"""
        return self.presta_fields.customizable or None

    @customizable.setter
    def customizable(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('customizable', value)

    @property
    def uploadable_files(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.uploadable_files`
        field DB type: tinyint(4)
         @details: __prod_desc__"""
        return self.presta_fields.uploadable_files or None

    @uploadable_files.setter
    def uploadable_files(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('uploadable_files', value)

    @property
    def text_fields(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.text_fields`
        field DB type: tinyint(4)
         @details: __prod_desc__"""
        return self.presta_fields.text_fields or None

    @text_fields.setter
    def text_fields(self, value: int = 0) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('text_fields', value)

    @property
    def active(self) -> Optional[int]:
        """  <sub>*[property]*</sub> `ps_product.active`
        field DB type: tinyint(1)
         @details: __prod_desc__"""
        return self.presta_fields.active or None

    @active.setter
    def active(self, value: int = 1) -> bool:
        """  <sub>*[setter]*</sub>   """
        return self._set_field('active', value)

    @property
    def redirect_type(self) -> Optional[str]:
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
        return self.presta_fields.redirect_type or None

    class EnumRedirect(Enum):
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'

    @redirect_type.setter
    def redirect_type(self, value: EnumRedirect | str) -> bool:
        """  <sub>*[setter]*</sub>   Редирект.
        Редиректы представляют собой механизм перенаправления пользователя или браузера с одного URL-адреса на другой. Они часто используются