### Анализ кода модуля `product_fields`

#### Качество кода:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код хорошо структурирован и организован в классы и методы, что облегчает понимание и поддержку.
  - Использованы аннотации типов, что улучшает читаемость и помогает в отладке.
  - Присутствуют property и setter для доступа к полям, что позволяет контролировать значения и добавлять логику при установке/получении значений.
  - Использованы dataclass, что сокращает boilerplate код для классов, хранящих данные.
- **Минусы**:
  - Не все функции и методы имеют подробные docstring, что затрудняет понимание их назначения и использования.
  - В коде встречаются закомментированные участки, которые следует удалить или объяснить их назначение.
  - Некоторые методы обработки ошибок содержат `...`, что указывает на незавершенную реализацию.

#### Рекомендации по улучшению:
1. **Документирование кода**:
   - Добавить docstring для всех функций, методов и классов, используя указанный формат.
   - Описать назначение каждого property и setter.
   - Указать типы исключений, которые могут быть выброшены.
   - Привести примеры использования наиболее важных методов.
2. **Обработка ошибок**:
   - Заменить все `...` в блоках обработки исключений на конкретные действия, такие как логирование ошибки и/или выброс исключения.
   - Использовать `logger.error` с параметром `exc_info=True` для логирования полной трассировки исключения.
3. **Использование `j_loads` и `logger`**:
   - Убедиться, что `j_loads` используется для загрузки JSON файлов.
   - Использовать `logger` из `src.logger` для логирования.
4. **Улучшение читаемости**:
   - Использовать одинарные кавычки для строк.
   - Добавить пробелы вокруг операторов присваивания.
   - Избавиться от закомментированного кода.
5. **Форматирование мультиязычных значений**:
   - Разобраться с закомментированным кодом в `_format_multilang_value` и привести его в соответствие с требованиями API PrestaShop.
6. **Улучшение наименований**:
   - Переименовать `product_product_features` в `product_features` для краткости и ясности.

#### Оптимизированный код:

```python
## \file /src/endpoints/prestashop/product_fields/product_fields.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль для работы с полями товара в PrestaShop API.
=====================================================

Модуль содержит класс :class:`ProductFields`, который используется для описания и управления полями товара,
предназначенными для таблиц PrestaShop.

Пример использования:
--------------------

>>> product_fields = ProductFields()
>>> product_fields.name = 'Новый товар'
>>> product_fields.price = 100.0
>>> product_data = product_fields.to_dict()
"""

import asyncio
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional, Any
from types import SimpleNamespace

import header
from header import __root__
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import read_text_file
from src.utils.string.normalizer import (
    normalize_boolean,
    normalize_float,
    normalize_sql_date,
    normalize_int,
)
from src.logger import logger
from src.logger.exceptions import ProductFieldException  # If you have this exception class


@dataclass
class ProductFields:
    """
    Класс, описывающий поля товара в формате API PrestaShop.
    Индексы языков, которые я устанавливаю в бд престашоп:
    1. Английский
    2. Иврит
    3. Русский
    """

    presta_fields: SimpleNamespace = field(init=False)
    id_lang: int = field(default=1)

    def __post_init__(self) -> None:
        """
        Инициализация объекта ProductFields после создания.
        """
        self._payload()

    def _payload(self) -> bool:
        """
        Загрузка дефолтных значений полей.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        base_path: Path = __root__ / 'src' / 'endpoints' / 'prestashop'
        presta_fields_list: list = read_text_file(base_path / 'product_fields' / 'fields_list.txt', as_list=True)
        if not presta_fields_list:
            logger.error('Ошибка загрузки файла со списком полей')
            # TODO: Добавить обработку ошибки
            return False

        try:
            self.presta_fields: SimpleNamespace = SimpleNamespace(**{key: None for key in presta_fields_list})
        except Exception as ex:
            logger.error('Ошибка конвертации', ex, exc_info=True)
            # TODO: Добавить обработку ошибки
            return False

        data_dict: dict = j_loads(base_path / 'product_fields' / 'product_fields_default_values.json')
        if not data_dict:
            logger.debug('Ошибка загрузки полей из файла product_fields_default_values.json')
            # TODO: Добавить обработку ошибки
            return False
        try:
            for name, value in data_dict.items():
                setattr(self.presta_fields, name, value)
            return True
        except Exception as ex:
            logger.error('Exception', ex, exc_info=True)
            # TODO: Добавить обработку ошибки
            return False

    def _set_multilang_value(self, field_name: str, value: str) -> bool:
        """
        Устанавливает мультиязычное значение для заданного поля.

        Args:
            field_name (str): Имя поля (например, 'name', 'description').
            value (str): Значение для установки.

        Returns:
            bool: True, если установка прошла успешно, иначе False.
        """
        try:
            _lang_index = str(self.id_lang)

            # Create the language-specific data structure
            lang_data = {
                'language': {
                    'id': _lang_index
                },
                'value': value
            }

            # Get the existing field value, or None if it doesn't exist
            field = getattr(self.presta_fields, field_name, None)

            if field is None:
                # If the field doesn't exist, create a list with the new language data
                setattr(self.presta_fields, field_name, [lang_data])
            else:
                # If the field exists, append the new language data to the existing list
                if not isinstance(field, list):
                   #Если вдруг там не список, то создадим список
                   setattr(self.presta_fields, field_name, [lang_data])
                else:
                    field.append(lang_data)

            return True

        except Exception as ex:
            logger.error(f'Ошибка установки значения в мультиязычное поле {field_name}\n'
                         f'Значение {value}:\n', ex, exc_info=True)
            return False

    # --------------------------------------------------------------------------
    #                  Поля таблицы ps_product
    # --------------------------------------------------------------------------

    @property
    def id_product(self) -> Optional[int]:
        """property `ps_product.id_product: int(10) unsigned`"""
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int = None) -> None:
        """setter `ID` товара. Для нового товара id назначается из `PrestaShop`."""
        try:
            self.presta_fields.id_product = value
        except Exception as ex:
            logger.error('Ошибка при установке id_product:', ex, exc_info=True)

    @property
    def id_supplier(self) -> Optional[int]:
        """property `ps_product.id_supplier: int(10) unsigned`"""
        return self.presta_fields.id_supplier

    @id_supplier.setter
    def id_supplier(self, value: int = None) -> None:
        """setter `ID` поставщика."""
        try:
            self.presta_fields.id_supplier = value
        except Exception as ex:
            logger.error('Ошибка при установке id_supplier:', ex, exc_info=True)

    @property
    def id_manufacturer(self) -> Optional[int]:
        """property `ps_product.id_manufacturer: int(10) unsigned`"""
        return self.presta_fields.id_manufacturer

    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None) -> None:
        """setter `ID` бренда."""
        try:
            self.presta_fields.id_manufacturer = value
        except Exception as ex:
            logger.error('Ошибка при установке id_manufacturer:', ex, exc_info=True)

    @property
    def id_category_default(self) -> Optional[int]:
        """property `ps_product.id_category_default: int(10) unsigned`"""
        return self.presta_fields.id_category_default

    @id_category_default.setter
    def id_category_default(self, value: int) -> None:
        """setter `ID` главной категории товара."""
        try:
            self.presta_fields.id_category_default = value
        except Exception as ex:
            logger.error('Ошибка при установке id_shop_default:', ex, exc_info=True)

    @property
    def id_shop_default(self) -> Optional[int]:
        """property `ps_product.id_shop_default: int(10) unsigned`"""
        return self.presta_fields.id_shop_default

    @id_shop_default.setter
    def id_shop_default(self, value: int) -> None:
        """setter `ID` магазина по умолчанию."""
        try:
            self.presta_fields.id_shop_default = value or 1
        except Exception as ex:
            logger.error('Ошибка при установке id_shop_default:', ex, exc_info=True)

    @property
    def id_shop(self) -> Optional[int]:
        """property `ps_product.id_shop: int(10) unsigned`"""
        return self.presta_fields.id_shop

    @id_shop.setter
    def id_shop(self, value: int) -> None:
        """setter `ID` магазина (для multishop)."""
        try:
            self.presta_fields.id_shop = value or 1
        except Exception as ex:
            logger.error('Ошибка при установке id_shop:', ex, exc_info=True)

    @property
    def id_tax(self) -> Optional[int]:
        """property `ps_product.id_tax: int(11) unsigned`"""
        return self.presta_fields.id_tax

    @id_tax.setter
    def id_tax(self, value: int) -> None:
        """setter `ID` налога."""
        try:
            self.presta_fields.id_tax = value
        except Exception as ex:
            logger.error('Ошибка при установке id_tax:', ex, exc_info=True)

    @property
    def position_in_category(self) -> Optional[int]:
        """property `ps_category_product.position: int(10) unsigned`"""
        return self.presta_fields.position_in_category

    @position_in_category.setter
    def position_in_category(self, value: int = None) -> None:
        """setter Позиция товара в категории."""
        try:
            self.presta_fields.position_in_category = value
        except Exception as ex:
            logger.error(f'Ошибка при установке `position_in_category` {value} :', ex, exc_info=True)

    @property
    def on_sale(self) -> int:
        """property `ps_product.on_sale: tinyint(1) unsigned`"""
        return self.presta_fields.on_sale

    @on_sale.setter
    def on_sale(self, value: int) -> None:
        """setter Флаг распродажи."""
        self.presta_fields.on_sale = value

    @property
    def online_only(self) -> int:
        """property `ps_product.online_only: tinyint(1) unsigned`"""
        return self.presta_fields.online_only

    @online_only.setter
    def online_only(self, value: int | bool) -> None:
        """setter Флаг 'только онлайн'."""
        self.presta_fields.online_only = int(value)

    @property
    def ean13(self) -> Optional[str]:
        """property `ps_product.ean13: varchar(13)`"""
        return self.presta_fields.ean13

    @ean13.setter
    def ean13(self, value: str) -> None:
        """setter EAN13 код товара."""
        self.presta_fields.ean13 = value

    @property
    def isbn(self) -> Optional[str]:
        """property `ps_product.isbn: varchar(32)`"""
        return self.presta_fields.isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        """setter ISBN код товара."""
        self.presta_fields.isbn = value

    @property
    def upc(self) -> Optional[str]:
        """property `ps_product.upc: varchar(12)`"""
        return self.presta_fields.upc

    @upc.setter
    def upc(self, value: str) -> None:
        """setter UPC код товара."""
        self.presta_fields.upc = value

    @property
    def mpn(self) -> Optional[str]:
        """property `ps_product.mpn: varchar(40)`"""
        return self.presta_fields.mpn

    @mpn.setter
    def mpn(self, value: str) -> None:
        """setter MPN код товара."""
        self.presta_fields.mpn = value

    @property
    def ecotax(self) -> Optional[float]:
        """property `ps_product.ecotax: decimal(17,6)`"""
        return self.presta_fields.ecotax

    @ecotax.setter
    def ecotax(self, value: float = None) -> None:
        """setter Эко налог."""
        self.presta_fields.ecotax = value

    @property
    def minimal_quantity(self) -> int:
        """property `ps_product.minimal_quantity: int(10) unsigned`"""
        return self.presta_fields.minimal_quantity

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 1) -> None:
        """setter Минимальное количество товара для заказа."""
        self.presta_fields.minimal_quantity = value

    @property
    def low_stock_threshold(self) -> int:
        """property `ps_product.low_stock_threshold: int(10)`"""
        return self.presta_fields.low_stock_threshold

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: int) -> None:
        """setter Пороговое значение для уведомления о низком запасе."""
        self.presta_fields.low_stock_threshold = value

    @property
    def low_stock_alert(self) -> int:
        """property `ps_product.low_stock_alert: tinyint(1)`"""
        return self.presta_fields.low_stock_alert

    @low_stock_alert.setter
    def low_stock_alert(self, value: int) -> None:
        """setter Флаг уведомления о низком запасе."""
        self.presta_fields.low_stock_alert = value

    @property
    def price(self) -> float:
        """property `ps_product.price: decimal(20,6)`"""
        return self.presta_fields.price

    @price.setter
    def price(self, value: str | int | float) -> None:
        """setter Цена товара."""
        try:
            self.presta_fields.price = normalize_float(value)
        except ValueError as ex:
            logger.error(f'Недопустимое значение для цены: {value}. Ошибка:', ex, exc_info=True)
            return

    @property
    def wholesale_price(self) -> Optional[float]:
        """property `ps_product.wholesale_price: decimal(20,6)`"""
        return self.presta_fields.wholesale_price

    @wholesale_price.setter
    def wholesale_price(self, value: str | int | float) -> None:
        """setter Оптовая цена."""
        self.presta_fields.wholesale_price = float(value)

    @property
    def unity(self) -> Optional[str]:
        """property `ps_product.unity: varchar(255)`"""
        return self.presta_fields.unity

    @unity.setter
    def unity(self, value: str) -> None:
        """setter Единица измерения."""
        self.presta_fields.unity = value

    @property
    def unit_price_ratio(self) -> float:
        """property `ps_product.unit_price_ratio: decimal(20,6)`"""
        return self.presta_fields.unit_price_ratio

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float) -> None:
        """setter Соотношение цены за единицу."""
        self.presta_fields.unit_price_ratio = value

    @property
    def additional_shipping_cost(self) -> float:
        """property `ps_product.additional_shipping_cost: decimal(20,6)`"""
        return self.presta_fields.additional_shipping_cost

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: float) -> None:
        """setter Дополнительная стоимость доставки."""
        self.presta_fields.additional_shipping_cost = value

    @property
    def reference(self) -> Optional[str]:
        """property `ps_product.reference: varchar(64)`"""
        return self.presta_fields.reference

    @reference.setter
    def reference(self, value: str) -> None:
        """setter Артикул товара."""
        self.presta_fields.reference = value

    @property
    def supplier_reference(self) -> Optional[str]:
        """property `ps_product.supplier_reference: varchar(64)`"""
        return self.presta_fields.supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, value: str) -> None:
        """setter Артикул поставщика."""
        self.presta_fields.supplier_reference = value

    @property
    def location(self) -> Optional[str]:
        """property `ps_product.location: varchar(255)`"""
        return self.presta_fields.location

    @location.setter
    def location(self, value: str) -> None:
        """setter Местоположение товара на складе."""
        self.presta_fields.location = value

    @property
    def width(self) -> Optional[float]:
        """property `ps_product.width: decimal(20,6)`"""
        return self.presta_fields.width

    @width.setter
    def width(self, value: float = None) -> None:
        """setter Ширина товара."""
        self.presta_fields.width = value

    @property
    def height(self) -> Optional[float]:
        """property `ps_product.height: decimal(20,6)`"""
        return self.presta_fields.height

    @height.setter
    def height(self, value: float = None) -> None:
        """setter Высота товара."""
        self.presta_fields.height = value

    @property
    def depth(self) -> Optional[float]:
        """property `ps_product.depth: decimal(20,6)`"""
        return self.presta_fields.depth

    @depth.setter
    def depth(self, value: float = None) -> None:
        """setter Глубина товара."""
        self.presta_fields.depth = value

    @property
    def weight(self) -> Optional[float]:
        """property `ps_product.weight: decimal(20,6)`"""
        return self.presta_fields.weight

    @weight.setter
    def weight(self, value: float = None) -> None:
        """setter Вес товара."""
        self.presta_fields.weight = value

    @property
    def volume(self) -> Optional[str]:
        """property `ps_product.volume: varchar(100)`"""
        return self.presta_fields.volume

    @volume.setter
    def volume(self, value: str) -> None:
        """setter Объем товара."""
        self.presta_fields.volume = value

    @property
    def out_of_stock(self) -> Optional[int]:
        """property `ps_product.out_of_stock: int(10) unsigned`"""
        return self.presta_fields.out_of_stock

    @out_of_stock.setter
    def out_of_stock(self, value: int = None) -> None:
        """setter Действие при отсутствии товара на складе."""
        self.presta_fields.out_of_stock = value

    @property
    def additional_delivery_times(self) -> Optional[int]:
        """property `ps_product.additional_delivery_times: tinyint(1) unsigned`"""
        return self.presta_fields.additional_delivery_times

    @additional_delivery_times.setter
    def additional_delivery_times(self, value: int) -> None:
        """setter Дополнительное время доставки."""
        self.presta_fields.additional_delivery_times = value

    @property
    def quantity_discount(self) -> Optional[int]:
        """property `ps_product.quantity_discount: tinyint(1)`"""
        return self.presta_fields.quantity_discount

    @quantity_discount.setter
    def quantity_discount(self, value: int) -> None:
        """setter Флаг скидки на количество."""
        self.presta_fields.quantity_discount = value

    @property
    def customizable(self) -> Optional[int]:
        """property `ps_product.customizable: tinyint(2)`"""
        return self.presta_fields.customizable

    @customizable.setter
    def customizable(self, value: int) -> None:
        """setter Флаг возможности кастомизации."""
        self.presta_fields.customizable = value

    @property
    def uploadable_files(self) -> Optional[int]:
        """property `ps_product.uploadable_files: tinyint(4)`"""
        return self.presta_fields.uploadable_files

    @uploadable_files.setter
    def uploadable_files(self, value: int) -> None:
        """setter Флаг возможности загрузки файлов."""
        self.presta_fields.uploadable_files = value

    @property
    def text_fields(self) -> Optional[int]:
        """property `ps_product.text_fields: tinyint(4)`"""
        return self.presta_fields.text_fields

    @text_fields.setter
    def text_fields(self, value: int) -> None:
        """setter Количество текстовых полей."""
        self.presta_fields.text_fields = value

    @property
    def active(self) -> Optional[int]:
        """property `ps_product.active: tinyint(1) unsigned`"""
        return self.presta_fields.active

    @active.setter
    def active(self, value: int = 1) -> None:
        """setter Флаг активности товара."""
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
        """property `ps_product.redirect_type: enum('404','301-product','302-product','301-category','302-category')`"""
        return self.presta_fields.redirect_type

    @redirect_type.setter
    def redirect_type(self, value: EnumRedirect | str) -> None:
        """setter Тип редиректа."""
        self.presta_fields.redirect_type = str(value)

    @property
    def id_type_redirected(self) -> Optional[int]:
        """property `ps_product.id_type_redirected: int(10) unsigned`"""
        return self.presta_fields.id_type_redirected

    @id_type_redirected.setter
    def id_type_redirected(self, value: int) -> None:
        """setter ID связанного редиректа."""
        self.presta_fields.id_type_redirected = value

    @property
    def available_for_order(self) -> Optional[int]:
        """property `ps_product.available_for_order: tinyint(1)`"""
        return self.presta_fields.available_for_order

    @available_for_order.setter
    def available_for_order(self, value: int) -> None:
        """setter Флаг доступности для заказа."""
        self.presta_fields.available_for_order = value

    @property
    def available_date(self) -> Optional[datetime]:
        """property `ps_product.available_date: date`"""
        return self.presta_fields.available_date

    @available_date.setter
    def available_date(self, value: datetime = datetime.now()) -> None:
        """setter Дата доступности товара."""
        self.presta_fields.available_date = value

    @property
    def show_condition(self) -> Optional[int]:
        """property `ps_product.show_condition: tinyint(1)`"""
        return self.presta_fields.show_condition

    @show_condition.setter
    def show_condition(self, value: int = 1) -> None:
        """setter Флаг отображения состояния товара."""
        self.presta_fields.show_condition = value

    class EnumCondition(Enum):
        """Перечисление для состояний товара."""
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'

    @property
    def condition(self) -> Optional[str]:
        """property `ps_product.condition: enum('new','used','refurbished')`"""
        return self.presta_fields.condition

    @condition.setter
    def condition(self, value: EnumCondition | str = EnumCondition.NEW) -> None:
        """setter Состояние товара."""
        self.presta_fields.condition = str(value)

    @property
    def show_price(self) -> Optional[int]:
        """property `ps_product.show_price: tinyint(1)`"""
        return self.presta_fields.show_price

    @show_price.setter
    def show_price(self, value: int = 1) -> None:
        """setter Флаг отображения цены."""
        self.presta_fields.show_price = value

    @property
    def indexed(self) -> Optional[int]:
        """property `ps_product.indexed: tinyint(1)`"""
        return self.presta_fields.indexed

    @indexed.setter
    def indexed(self, value: int = 1) -> None:
        """setter Флаг индексации товара."""
        self.presta_fields.indexed = value

    class EnumVisibity(Enum):
        """Перечисление для видимости товара."""
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'

    @property
    def visibility(self) -> Optional[str]:
        """property `ps_product.visibility: enum('both','catalog','search','none')`"""
        return self.presta_fields.visibility

    @visibility.setter
    def visibility(self, value: EnumVisibity | str = EnumVisibity.BOTH) -> None:
        """setter Видимость товара."""
        self.presta_fields.visibility = str(value)

    @property
    def cache_is_pack(self) -> Optional[int]:
        """property `ps_product.cache_is_pack: tinyint(1)`"""
        return self.presta_fields.cache_is_pack

    @cache_is_pack.setter
    def cache_is_pack(self, value: int = 1) -> None:
        """setter Флаг кэширования как пакет товара."""
        self.presta_fields.cache_is_pack = value

    @property
    def cache_has_attachments(self) -> Optional[int]:
        """property `ps_product.cache_has_attachments: tinyint(1)`"""
        return self.presta_fields.cache_has_attachments

    @cache_has_attachments.setter
    def cache_has_attachments(self, value: int = 1) -> None:
        """setter Флаг кэширования вложений."""
        self.presta_fields.cache_has_attachments = value

    @property
    def is_virtual(self) -> Optional[int]:
        """property `ps_product.is_virtual: tinyint(1)`"""
        return self.presta_fields.is_virtual

    @is_virtual.setter
    def is_virtual(self, value: int = 1) -> None:
        """setter Флаг виртуального товара."""
        self.presta_fields.is_virtual = value

    @property
    def cache_default_attribute(self) -> Optional[int]:
        """property `ps_product.cache_default_attribute: int(10) unsigned`"""
        return self.presta_fields.cache_default_attribute

    @cache_default_attribute.setter
    def cache_default_attribute(self, value: int = 1) -> None:
        """setter ID атрибута по умолчанию для кэширования."""
        self.presta_fields.cache_default_attribute = value

    @property
    def date_add(self) -> Optional[datetime]:
        """property `ps_product.date_add: datetime`"""
        return self.presta_fields.date_add

    @date_add.setter
    def date_add(self, value: datetime = datetime.now()) -> None:
        """setter Дата добавления товара."""
        self.presta_fields.date_add = value

    @property
    def date_upd(self) -> Optional[datetime]:
        """property `ps_product.date_upd: datetime`"""
        return self.presta_fields.date_upd

    @date_upd.setter
    def date_upd(self, value: datetime = datetime.now()) -> None:
        """setter Дата обновления товара."""
        self.presta_fields.date_upd = value

    @property
    def advanced_stock_management(self) -> Optional[int]:
        """property `ps_product.advanced_stock_management: tinyint(1)`"""
        return self.presta_fields.advanced_stock_management

    @advanced_stock_management.setter
    def advanced_stock_management(self, value: int) -> None:
        """setter Флаг расширенного управления запасами."""
        self.presta_fields.advanced_stock_management = value

    @property
    def pack_stock_type(self) -> Optional[int]:
        """property `ps_product.pack_stock_type: int(11) unsigned`"""
        return self.presta_fields.pack_stock_type

    @pack_stock_type.setter
    def pack_stock_type(self, value: int) -> None:
        """setter Тип управления запасами пакета товаров."""
        self.presta_fields.pack_stock_type = value

    @property
    def state(self) -> Optional[int]:
        """property `ps_product.state: int(11) unsigned`"""
        return self.presta_fields.state

    @state.setter
    def state(self, value: int) -> None:
        """setter Состояние товара."""
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
        """property `ps_product.product_type: enum('standard', 'pack', 'virtual', 'combinations', '')`"""
        return self.presta_fields.product_type