## Анализ кода модуля product_fields

**Качество кода**

8
-  Плюсы
    - Код хорошо структурирован и разбит на классы и методы.
    - Используются `property` и `setter` для доступа к полям, что обеспечивает инкапсуляцию и гибкость.
    - Присутствует базовая обработка ошибок с использованием `try-except` и логирования.
    - Имеется подробная документация в виде docstrings.
    -  Используется `SimpleNamespace` для хранения полей товара.
-  Минусы
    -  Много повторяющегося кода в сеттерах свойств (особенно в блоке `ps_product_lang`).
    -  Не все сеттеры возвращают `True` в случае успеха, некоторые возвращают `None`.
    -  Используются стандартные блоки `try-except` без необходимости.
    -   Комментарии после `#` не всегда информативны и не соответствуют стандарту RST.
    -   Много `...` в коде, которые не являются точками остановки.
    -  Не используются валидаторы для данных.
    -   В некоторых местах используются `or ''` вместо `or None`.
    -  Не используется единый стиль форматирования словарей для вставки данных.

**Рекомендации по улучшению**

1.  **Улучшить обработку ошибок:**
    -  Использовать `logger.error` для логирования ошибок вместо `print`.
    -  Устранить избыточные блоки `try-except`, где это возможно, заменяя их проверками и логированием.

2.  **Рефакторинг сеттеров:**
    -  Устранить дублирование кода в сеттерах, особенно в блоке `ps_product_lang`, создав общую функцию для установки значений.
    -  Добавить валидацию данных в сеттерах.
    -  Все сеттеры должны возвращать `True` при успехе и ничего или `False` при ошибке.

3.  **Улучшить документацию:**
    -  Переписать комментарии в формате RST.
    -  Включить примеры использования методов и классов в документацию.

4.  **Использовать `j_loads_ns`:**
    -  Использовать `j_loads_ns` для загрузки JSON данных в `_payload`.

5.  **Устранить неиспользуемый код:**
    - Удалить или закомментировать неиспользуемые блоки кода и импорты.
    - Удалить все  `...` если это не точки остановки.

6.  **Унифицировать  стиль словарей данных:**
    - Использовать единый шаблон для словарей, который добавляется в базу данных.
    - Использовать единый способ форматирования данных для вставки в словари, например, `{'language': [{'attrs': {'id': self.language[lang]}, 'value': value}]}`.

7. **Добавить валидацию данных:**
   - Использовать `pydantic` для валидации данных, приходящих в сеттеры.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для описания полей товара в PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`ProductFields`, который используется для управления и описания
полей товара в формате, совместимом с API PrestaShop.

Класс `ProductFields` предоставляет интерфейс для работы с полями товаров,
включая их чтение, запись и валидацию. Поля соответствуют структуре таблиц PrestaShop.

Пример использования
--------------------

Пример использования класса `ProductFields`:

.. code-block:: python

    from src.product.product_fields.product_fields import ProductFields

    product_fields = ProductFields()
    product_fields.id_product = 123
    product_fields.name = 'Test Product'
    print(product_fields.id_product)
    print(product_fields.name)


.. todo:: Внимательно посмотреть, как работает langdetect
"""

MODE = 'dev'
from pathlib import Path
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, validator
from types import SimpleNamespace
from sqlite3 import Date
from langdetect import detect
from functools import wraps
from enum import Enum

from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import read_text_file
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException


class ProductFields:
    """
    Класс для управления полями товара в формате API PrestaShop.
    =========================================================================================

    Этот класс инкапсулирует логику работы с полями товара, обеспечивая их хранение,
    загрузку, и валидацию. Поля соответствуют структуре таблиц PrestaShop.

    :ivar product_fields_list: Список полей товара.
    :vartype product_fields_list: List[str]
    :ivar language: Словарь идентификаторов языков.
    :vartype language: Dict[str, int]
    :ivar presta_fields: SimpleNamespace для хранения полей PrestaShop.
    :vartype presta_fields: SimpleNamespace
    :ivar assist_fields_dict: Словарь для хранения служебных полей.
    :vartype assist_fields_dict: Dict[str, Any]
    """

    def __init__(self):
        """
        Инициализация класса.

        Загружает список полей товара, устанавливает соответствия языков
        и инициализирует структуру для хранения данных.
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
        Загружает список полей товара из файла.

        :return: Список полей товара.
        :rtype: List[str]
        """
        return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)

    def _payload(self) -> bool:
        """
        Загружает значения полей по умолчанию из файла.

        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        data = j_loads_ns(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json')) # используем j_loads_ns
        if not data:
            logger.error(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
            return False
        for name, value in data.__dict__.items(): # Обращение к данным как к атрибутам
            setattr(self, name, value)
        return True

    @property
    def associations(self) -> Optional[Dict]:
        """
        Возвращает словарь ассоциаций.
        :return: словарь ассоциаций.
        :rtype: Optional[Dict]
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
        Возвращает ID товара.
        :return: ID товара.
        :rtype: Optional[int]
         """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int = None) -> None:
        """
        Устанавливает ID товара.

         Если `value` был передан, его значение подставляется в поле `ProductFields.id_product`.
         ID товара требуется при операциях над существующим товаром.
         Для нового товара ID вернется из системы при занесении товара в базу данных.

         :param value: ID товара.
         :type value: int, optional
         """
        try:
            self.presta_fields.id_product = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ID' данными {value}", exc_info=ex)

    @property
    def id_supplier(self) -> Optional[int]:
        """
        Возвращает ID поставщика.
        :return: ID поставщика.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_supplier or None

    @id_supplier.setter
    def id_supplier(self, value: int = None) -> bool:
        """
        Устанавливает ID поставщика.
         :param value: ID поставщика.
         :type value: int, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.id_supplier = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ps_product.id_supplier' данными {value}", exc_info=ex)
            return False

    @property
    def id_manufacturer(self) -> Optional[int]:
        """
        Возвращает ID производителя.
         :return: ID производителя.
         :rtype: Optional[int]
        """
        return self.presta_fields.id_manufacturer or None

    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None) -> None:
        """
        Устанавливает ID производителя.

        :param value: ID производителя.
        :type value: int, optional
        """
        try:
            self.presta_fields.id_manufacturer = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'Brand' данными {value}", exc_info=ex)

    @property
    def id_category_default(self) -> Optional[int]:
        """
        Возвращает ID категории по умолчанию.
        :return: ID категории по умолчанию.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_category_default or None

    @id_category_default.setter
    def id_category_default(self, value: int) -> None:
        """
        Устанавливает ID категории по умолчанию.

        :param value: ID категории по умолчанию.
        :type value: int
        """
        try:
            self.presta_fields.id_category_default = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'id_category_default' данными {value}", exc_info=ex)

    @property
    def additional_categories(self) -> Optional[dict]:
        """
        Возвращает словарь дополнительных категорий.
         :return: Словарь дополнительных категорий.
         :rtype: Optional[dict]
        """
        return self.presta_fields.associations.categories if self.presta_fields.associations else None

    @additional_categories.setter
    def additional_categories(self, value: int | list[int]) -> None:
        """
        Устанавливает дополнительные категории.
        Если передан список, то каждый элемент списка добавляется как доп. категория.

        :param value: ID или список ID дополнительных категорий.
        :type value: int | list[int]
        """
        value = value if isinstance(value, list) else [value]

        if not self.presta_fields.associations:
            self.presta_fields.associations = {'categories': {}}

        for v in value:
            if not isinstance(v, int):
                logger.error(f'Недопустимое значение для категории {v=}, Должен быть `int`')
                continue

            try:
                self.presta_fields.associations['categories'].update({'id': v})
            except ProductFieldException as ex:
                logger.error(f"Ошибка заполнения поля: 'additional_categories' данными {v}", exc_info=ex)
                return

    @property
    def id_shop_default(self) -> Optional[int]:
        """
        Возвращает ID магазина по умолчанию.
         :return: ID магазина по умолчанию.
         :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default or None

    @id_shop_default.setter
    def id_shop_default(self, value: int = None) -> None:
        """
         Устанавливает ID магазина по умолчанию.

         :param value: ID магазина по умолчанию.
         :type value: int, optional
         """
        try:
            self.presta_fields.id_shop_default = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'id_shop_default' данными {value}", exc_info=ex)

    @property
    def id_shop(self) -> Optional[int]:
        """
         Возвращает ID магазина.

        :return: ID магазина.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop or None

    @id_shop.setter
    def id_shop(self, value: int = None) -> None:
        """
        Устанавливает ID магазина.
        :param value: ID магазина.
        :type value: int, optional
        """
        try:
            self.presta_fields.id_shop = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'id_shop' данными {value}", exc_info=ex)

    @property
    def id_tax(self) -> Optional[int]:
        """
        Возвращает ID налога.
         :return: ID налога.
         :rtype: Optional[int]
        """
        return self.presta_fields.id_tax or None

    @id_tax.setter
    def id_tax(self, value: int) -> None:
        """
        Устанавливает ID налога.
        :param value: ID налога.
        :type value: int
        """
        try:
            self.presta_fields.id_tax = int(value)
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'Tax rule ID' данными {value}", exc_info=ex)

    @property
    def on_sale(self) -> Optional[int]:
        """
        Возвращает флаг распродажи.
        :return: Флаг распродажи.
        :rtype: Optional[int]
        """
        return self.presta_fields.on_sale or None

    @on_sale.setter
    def on_sale(self, value: int = 0) -> None:
        """
         Устанавливает флаг распродажи.

        :param value: Флаг распродажи (0 или 1).
        :type value: int, optional
        """
        try:
            self.presta_fields.on_sale = value
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'On sale (0/1)' данными {value}", exc_info=ex)

    @property
    def online_only(self) -> Optional[int]:
        """
        Возвращает флаг "только онлайн".
         :return: Флаг "только онлайн".
         :rtype: Optional[int]
        """
        return self.presta_fields.online_only or None

    @online_only.setter
    def online_only(self, value: int = 0) -> bool:
        """
        Устанавливает флаг "только онлайн".
         :param value: Флаг "только онлайн" (0 или 1).
         :type value: int, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.online_only = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'online_only' данными {value}", exc_info=ex)
            return False

    @property
    def ean13(self) -> Optional[str]:
        """
        Возвращает EAN13.
         :return: EAN13.
         :rtype: Optional[str]
        """
        return self.presta_fields.ean13 or None

    @ean13.setter
    def ean13(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает EAN13.
         :param value: EAN13.
         :type value: str, optional
         :param lang: Язык.
         :type lang: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.ean13 = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ean13' данными {value}", exc_info=ex)
            return False

    @property
    def isbn(self) -> Optional[str]:
        """
        Возвращает ISBN.
        :return: ISBN.
        :rtype: Optional[str]
        """
        return self.presta_fields.isbn or None

    @isbn.setter
    def isbn(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает ISBN.
        :param value: ISBN.
        :type value: str, optional
        :param lang: Язык.
        :type lang: str, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.isbn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'isbn' данными {value}", exc_info=ex)
            return False

    @property
    def upc(self) -> Optional[str]:
        """
        Возвращает UPC.
        :return: UPC.
        :rtype: Optional[str]
        """
        return self.presta_fields.upc or None

    @upc.setter
    def upc(self, value: str = None, lang: str = 'en') -> bool:
        """
         Устанавливает UPC.
         :param value: UPC.
         :type value: str, optional
         :param lang: Язык.
         :type lang: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.upc = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'isbn' данными {value}", exc_info=ex)
            return False

    @property
    def mpn(self) -> Optional[str]:
        """
         Возвращает MPN.
         :return: MPN.
         :rtype: Optional[str]
        """
        return self.presta_fields.mpn or None

    @mpn.setter
    def mpn(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает MPN.
        :param value: MPN.
        :type value: str, optional
        :param lang: Язык.
        :type lang: str, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.mpn = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: `ps_product.mpn` данными {value}", exc_info=ex)
            return False

    @property
    def ecotax(self) -> Optional[str]:
        """
         Возвращает ecotax.
        :return: ecotax.
        :rtype: Optional[str]
        """
        return self.presta_fields.ecotax or None

    @ecotax.setter
    def ecotax(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает ecotax.

        :param value: ecotax.
        :type value: str, optional
        :param lang: Язык.
        :type lang: str, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.ecotax = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'ecotax' данными {value}", exc_info=ex)
            return False

    @property
    def minimal_quantity(self) -> Optional[int]:
        """
         Возвращает минимальное количество.
         :return: Минимальное количество.
         :rtype: Optional[int]
        """
        return self.presta_fields.minimal_quantity or None

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 0) -> bool:
        """
        Устанавливает минимальное количество.
         :param value: Минимальное количество.
         :type value: int, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.minimal_quantity = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'minimal_quantity' данными {value}", exc_info=ex)
            return False

    @property
    def low_stock_threshold(self) -> Optional[int]:
        """
         Возвращает порог низкого остатка.
         :return: Порог низкого остатка.
         :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_threshold or None

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: str = '') -> bool:
        """
         Устанавливает порог низкого остатка.
         :param value: Порог низкого остатка.
         :type value: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.low_stock_threshold = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'low_stock_threshold' данными {value}", exc_info=ex)
            return False

    @property
    def low_stock_alert(self) -> Optional[int]:
        """
         Возвращает флаг оповещения о низком остатке.
         :return: Флаг оповещения о низком остатке.
         :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_alert or None

    @low_stock_alert.setter
    def low_stock_alert(self, value: int = 0) -> bool:
        """
        Устанавливает флаг оповещения о низком остатке.
        :param value: Флаг оповещения о низком остатке (0 или 1).
        :type value: int, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.low_stock_alert = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'low_stock_alert' данными {value}", exc_info=ex)
            return False

    @property
    def price(self) -> Optional[float]:
        """
        Возвращает цену товара.
         :return: Цена товара.
         :rtype: Optional[float]
        """
        return self.presta_fields.price or None

    @price.setter
    def price(self, value: str | int | float) -> bool:
        """
        Устанавливает цену товара.

        :param value: Цена товара.
        :type value: str | int | float
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            if not value:
                return False
            self.presta_fields.price = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'price' данными {value}", exc_info=ex)
            return False

    @property
    def wholesale_price(self) -> Optional[float]:
        """
         Возвращает оптовую цену.
         :return: Оптовая цена.
         :rtype: Optional[float]
        """
        return self.presta_fields.wholesale_price or None

    @wholesale_price.setter
    def wholesale_price(self, value: str = None, lang: str = 'en') -> bool:
        """
         Устанавливает оптовую цену.
         :param value: Оптовая цена.
         :type value: str, optional
         :param lang: Язык.
         :type lang: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.wholesale_price = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'wholesale_price' данными {value}", exc_info=ex)
            return False

    @property
    def unity(self) -> Optional[str]:
        """
        Возвращает единицу измерения.
         :return: Единица измерения.
         :rtype: Optional[str]
        """
        return self.presta_fields.unity or None

    @unity.setter
    def unity(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает единицу измерения.
         :param value: Единица измерения.
         :type value: str, optional
         :param lang: Язык.
         :type lang: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.unity = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'unity' данными {value}", exc_info=ex)
            return False

    @property
    def unit_price_ratio(self) -> Optional[float]:
        """
        Возвращает коэффициент цены за единицу.
         :return: Коэффициент цены за единицу.
         :rtype: Optional[float]
        """
        return self.presta_fields.unit_price_ratio or None

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float = 0) -> bool:
        """
        Устанавливает коэффициент цены за единицу.
         :param value: Коэффициент цены за единицу.
         :type value: float, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.unit_price_ratio = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: `unit_price_ratio` данными {value}", exc_info=ex)
            return False

    @property
    def additional_shipping_cost(self) -> Optional[float]:
        """
         Возвращает стоимость дополнительной доставки.
         :return: Стоимость дополнительной доставки.
         :rtype: Optional[float]
        """
        return self.presta_fields.additional_shipping_cost or None

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: int = 1) -> bool:
        """
        Устанавливает стоимость дополнительной доставки.
        :param value: Стоимость дополнительной доставки.
        :type value: int, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.additional_shipping_cost = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'additional_shipping_cost' данными {value}", exc_info=ex)
            return False

    @property
    def reference(self) -> Optional[str]:
        """
        Возвращает артикул.
         :return: Артикул.
         :rtype: Optional[str]
        """
        return self.presta_fields.reference or None

    @reference.setter
    def reference(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает артикул.
         :param value: Артикул.
         :type value: str, optional
         :param lang: Язык.
         :type lang: str, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.reference = str(value)
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'reference' данными {value}", exc_info=ex)
            return False

    @property
    def supplier_reference(self) -> Optional[str]:
        """
        Возвращает артикул поставщика.
         :return: Артикул поставщика.
         :rtype: Optional[str]
        """
        return self.presta_fields.supplier_reference or None

    @supplier_reference.setter
    def supplier_reference(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает артикул поставщика.

        :param value: Артикул поставщика.
        :type value: str, optional
        :param lang: Язык.
        :type lang: str, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.supplier_reference = str(value)
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'supplier_reference' данными {value}", exc_info=ex)
            return False

    @property
    def location(self) -> Optional[str]:
        """
        Возвращает местоположение.
         :return: Местоположение.
         :rtype: Optional[str]
        """
        return self.presta_fields.location or None

    @location.setter
    def location(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает местоположение.

        :param value: Местоположение.
        :type value: str, optional
        :param lang: Язык.
        :type lang: str, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.location = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'location' данными {value}", exc_info=ex)
            return False

    @property
    def width(self) -> Optional[float]:
        """
        Возвращает ширину.
        :return: Ширина.
        :rtype: Optional[float]
        """
        return self.presta_fields.width or None

    @width.setter
    def width(self, value: float = None) -> bool:
        """
        Устанавливает ширину.
         :param value: Ширина.
         :type value: float, optional
         :return: True при успехе, иначе False.
         :rtype: bool
        """
        try:
            self.presta_fields.width = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'width' данными {value}", exc_info=ex)
            return False

    @property
    def height(self) -> Optional[float]:
        """
        Возвращает высоту.
         :return: Высота.
         :rtype: Optional[float]
        """
        return self.presta_fields.height or None

    @height.setter
    def height(self, value: float = None) -> bool:
        """
        Устанавливает высоту.
        :param value: Высота.
        :type value: float, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.height = value
            return True
        except ProductFieldException as ex:
            logger.error(f"Ошибка заполнения поля: 'height' данными {value}", exc_info=ex)
            return False

    @property
    def depth(self) -> Optional[float]:
        """
         Возвращает глубину.
         :return: Глубина.
         :rtype: Optional[float]
        """
        return self.presta_fields.depth or None

    @depth.setter
    def depth(self, value: float = None) -> bool:
        """
        Устанавливает глубину.

        :param value: Глубина.
        :type value: float, optional
        :return: True при успехе, иначе False.
        :rtype: bool
        """
        try:
            self.presta_fields.depth = value
            return True
        except ProductFieldException as ex: