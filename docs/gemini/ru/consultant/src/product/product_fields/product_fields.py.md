## Анализ кода модуля product_fields

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован с использованием классов и свойств для представления полей продукта.
    -  Используется `pydantic` для валидации данных.
    -  Присутствует логирование ошибок с использованием `src.logger.logger`.
    -  Код следует принципам ООП.
-  Минусы
    -  Много повторяющегося кода в setter-методах.
    -  Не все комментарии соответствуют стандарту reStructuredText (RST).
    -  Использование `...` в коде как точки остановки не является хорошей практикой.
    -  Не все импорты используются в коде, а некоторые избыточны.
    -  Много `try-except` блоков, которые можно оптимизировать.
    -  В некоторых местах отсутствует проверка типов данных.

**Рекомендации по улучшению**

1.  **Улучшение документации**:
    -   Переписать все комментарии и docstring в формате RST.
    -   Добавить подробное описание каждого поля, включая его тип и назначение.
    -   Описать предназначение каждого метода и класса.

2.  **Рефакторинг `setter` методов**:
    -   Создать единую функцию для установки значений полей, чтобы избежать дублирования кода.
    -   Использовать декоратор для логирования ошибок в `setter` методах.

3.  **Улучшение обработки ошибок**:
    -   Использовать `logger.error` вместо стандартных `try-except` блоков там, где это возможно.
    -   Добавить более информативные сообщения об ошибках.

4.  **Оптимизация импортов**:
    -   Удалить неиспользуемые импорты.
    -   Сгруппировать импорты по стандартной библиотеке и сторонним пакетам.

5.  **Улучшение структуры кода**:
    -   Разделить класс на более мелкие части, если это необходимо.
    -   Избегать использования `...` в коде, заменив их на конкретные действия или логирование.

6.  **Добавление валидации**:
    -   Использовать `pydantic` для валидации входных данных в `setter` методах.
    -   Проверять типы данных перед их установкой.

7.  **Пересмотреть логику работы со словарями**
    - При установке данных в мультиязычные поля дублируется код
    - Вынести формирование словаря в отдельную функцию

8.  **Удаление лишних комментариев**
    - Убрать или перевести все комментарии, которые не несут никакой информационной нагрузки.
    - Оставить только те комментарии, которые поясняют код

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для описания полей товара в формате API PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`ProductFields`, который используется для представления
полей товара в соответствии с API PrestaShop. Каждое поле товара имеет свойство,
которое можно установить и получить.

Модуль также включает в себя:
    - Загрузку списка полей из текстового файла.
    - Загрузку дефолтных значений полей из JSON файла.
    - Управление мультиязычными полями.

Пример использования
--------------------

Пример создания экземпляра класса `ProductFields`:

.. code-block:: python

    from src.product.product_fields.product_fields import ProductFields

    product_fields = ProductFields()
    product_fields.id_product = 123
    print(product_fields.id_product)

"""
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12



from pathlib import Path
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field, validator
from types import SimpleNamespace
from sqlite3 import Date
from enum import Enum
from functools import wraps

from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import read_text_file
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException

# from langdetect import detect # todo: разобраться как работает
# import header # todo: разобраться зачем header

def log_setter_errors(func):
    """Декоратор для логирования ошибок в setter методах."""
    @wraps(func)
    def wrapper(self, value: Any = None, lang: str = 'en') -> Optional[bool]:
        try:
            return func(self, value, lang)
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: {func.__name__} данными {value}""", exc_info=True)
            return
    return wrapper

def set_multilingual_field(self, field_name: str, value: Any, lang: str) -> bool:
    """Устанавливает значение мультиязычного поля."""
    try:
        setattr(self.presta_fields, field_name, {'language': [{'attrs': {'id': self.language[lang]}, 'value': value}]})
        return True
    except Exception as ex:
        logger.error(f'Ошибка заполнения мультиязычного поля {field_name} данными {value}', exc_info=True)
        return False


class ProductFields:
    """
    Класс, описывающий поля товара в формате API PrestaShop.

    Этот класс предоставляет свойства для доступа и установки значений полей товара,
    соответствующих структуре таблиц PrestaShop.

    :ivar product_fields_list: Список полей продукта, загруженных из файла.
    :vartype product_fields_list: List[str]
    :ivar language: Словарь, отображающий языковые коды в идентификаторы.
    :vartype language: Dict[str, int]
    :ivar presta_fields: Пространство имен для хранения значений полей продукта.
    :vartype presta_fields: SimpleNamespace
    :ivar assist_fields_dict: Дополнительный словарь для хранения дополнительных полей.
    :vartype assist_fields_dict: Dict[str, Any]
    """

    def __init__(self):
        """
        Инициализация класса.

        Загружаются данные полей, языков и их идентификаторов.
        """
        self.product_fields_list = self._load_product_fields_list()
        self.language = {'en': 1, 'he': 2, 'ru': 3} # TODO: изменить логику так, чтобы словарь языков получался из presatshop клиента
        self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})
        self.assist_fields_dict = {
            'default_image_url': '',
            'images_urls': []
        }
        self._payload()

    def _load_product_fields_list(self) -> List[str]:
        """
        Загружает список полей продукта из файла.

        :return: Список полей продукта.
        :rtype: List[str]
        """
        return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)

    def _payload(self) -> bool:
        """
        Загружает значения по умолчанию для полей продукта из JSON файла.

        :return: True, если загрузка прошла успешно, False в противном случае.
        :rtype: bool
        """
        data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))
        if not data:
            logger.error(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
            return False
        for name, value in data.items():
            setattr(self, name, value)
        return True

    @property
    def associations(self) -> Optional[Dict]:
        """
        Возвращает словарь ассоциаций.
        
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
    
    @property
    def id_product(self) -> Optional[int]:
        """
        Свойство `id_product`.

        :return: `ps_product.id`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_product

    @id_product.setter
    @log_setter_errors
    def id_product(self, value: int = None):
        """
        Устанавливает ID товара.

        :param value: ID товара.
        :type value: int, optional
        
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_product = value


    @property
    def id_supplier(self) -> Optional[int]:
        """
         Свойство `id_supplier`.
         
         :return: `ps_product.id_supplier`
         :rtype: Optional[int]
        """
        return self.presta_fields.id_supplier or None

    @id_supplier.setter
    @log_setter_errors
    def id_supplier(self, value: int = None) -> bool:
        """
         Устанавливает ID поставщика.
         
         :param value: ID поставщика.
         :type value: int, optional
         
         :return: True в случае успеха.
         :rtype: bool
        """
        self.presta_fields.id_supplier = value
        return True

    @property
    def id_manufacturer(self) -> Optional[int]:
        """
        Свойство `id_manufacturer` (Бренд).
        
        :return: `ps_product.id_manufacturer`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_manufacturer or None

    @id_manufacturer.setter
    @log_setter_errors
    def id_manufacturer(self, value: int = None):
        """
        Устанавливает ID производителя (бренда).
        
        :param value: ID производителя.
        :type value: int, optional
        
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_manufacturer = value

    @property
    def id_category_default(self) -> Optional[int]:
         """
         Свойство `id_category_default`.
         
         :return: `ps_product.id_category_default`
         :rtype: Optional[int]
         """
         
         
         return self.presta_fields.id_category_default or None

    @id_category_default.setter
    @log_setter_errors
    def id_category_default(self, value: int):
        """
        Устанавливает ID основной категории товара.
        
        :param value: ID основной категории.
        :type value: int
        
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_category_default = value
    
    @property
    def additional_categories(self) -> Optional[dict]:
        """
         Возвращает словарь дополнительных категорий.
         
         :return: Словарь категорий или None.
         :rtype: Optional[dict]
        """
        return self.presta_fields.associations.categories or None

    @additional_categories.setter
    @log_setter_errors
    def additional_categories(self, value: Union[int, List[int]]):
        """
         Устанавливает дополнительные категории товара.

         :param value: ID или список ID дополнительных категорий.
         :type value: Union[int, List[int]]

         :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        value = value if isinstance(value, list) else [value]
        for v in value:
            if not isinstance(v, int):
                logger.error(f'недопустимое значение для категории {v=}, Должен быть `int`')
                continue
            try:
                if not hasattr(self.presta_fields.associations, 'categories'):
                    self.presta_fields.associations.categories = {}
                self.presta_fields.associations.categories.update({'id': v})
            except ProductFieldException as ex:
                logger.error(f"""Ошибка заполнения поля: 'additional_categories' данными {v}""", exc_info=True)
                return

    @property
    def id_shop_default(self) -> Optional[int]:
        """
        Свойство `id_shop_default`.

        :return: `ps_product.id_shop_default`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default or ''

    @id_shop_default.setter
    @log_setter_errors
    def id_shop_default(self, value: int = None):
        """
        Устанавливает ID магазина по умолчанию.

        :param value: ID магазина.
        :type value: int, optional
        
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_shop_default = value

    @property
    def id_shop(self) -> Optional[int]:
        """
        Свойство `id_shop`.

        :return: `ps_product.id_shop`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default or ''

    @id_shop.setter
    @log_setter_errors
    def id_shop(self, value: int = None):
        """
        Устанавливает ID магазина.

        :param value: ID магазина.
        :type value: int, optional

        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_shop = value

    @property
    def id_tax(self) -> Optional[int]:
        """
        Свойство `id_tax`.

        :return: `ps_product.id_tax`
        :rtype: Optional[int]
        """
        return self.presta_fields.id_tax or ''

    @id_tax.setter
    @log_setter_errors
    def id_tax(self, value: int ):
        """
        Устанавливает ID налогового правила.

        :param value: ID налогового правила.
        :type value: int

        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.id_tax = int(value)

    @property
    def on_sale(self) -> Optional[int]:
        """
        Свойство `on_sale`.

        :return: `ps_product.on_sale`
        :rtype: Optional[int]
        """
        return self.presta_fields.on_sale  or ''

    @on_sale.setter
    @log_setter_errors
    def on_sale(self, value: int = 0 ):
        """
        Устанавливает флаг "распродажа".
        
        :param value: Флаг распродажи (0/1).
        :type value: int, optional
        
        :raises ProductFieldException: Если возникает ошибка при установке значения.
        """
        self.presta_fields.on_sale = value
    
    @property
    def online_only(self) -> Optional[int]:
         """
         Свойство `online_only`.
         
         :return: `ps_product.online_only`
         :rtype: Optional[int]
        """
         
         return self.presta_fields.online_only or ''

    @online_only.setter
    @log_setter_errors
    def online_only(self, value: int = 0) -> bool:
        """
         Устанавливает флаг "только онлайн".

         :param value: Флаг "только онлайн" (0/1).
         :type value: int, optional

         :return: True в случае успеха.
         :rtype: bool
        """
        self.presta_fields.online_only = value
        return True

    @property
    def ean13(self) -> Optional[str]:
        """
        Свойство `ean13`.

        :return: `ps_product.ean13`
        :rtype: Optional[str]
        """
        return self.presta_fields.ean13 or ''

    @ean13.setter
    @log_setter_errors
    def ean13(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает EAN13.
        
        :param value: EAN13.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.ean13 = value
        return True

    @property
    def isbn(self) -> Optional[str]:
        """
        Свойство `isbn`.

        :return: `ps_product.isbn`
        :rtype: Optional[str]
        """
        return self.presta_fields.isbn or ''

    @isbn.setter
    @log_setter_errors
    def isbn(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает ISBN.
        
        :param value: ISBN.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.isbn = value
        return True

    @property
    def upc(self) -> Optional[str]:
        """
        Свойство `upc`.

        :return: `ps_product.upc`
        :rtype: Optional[str]
        """
        return self.presta_fields.upc or ''

    @upc.setter
    @log_setter_errors
    def upc(self, value: str = None, lang: str = 'en') -> Optional[bool]:
        """
        Устанавливает UPC.
        
        :param value: UPC.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: Optional[bool]
        """
        self.presta_fields.upc = value
        return True

    @property
    def mpn(self) -> Optional[str]:
        """
        Свойство `mpn`.

        :return: `ps_product.mpn`
        :rtype: Optional[str]
        """
        return self.presta_fields.mpn or ''

    @mpn.setter
    @log_setter_errors
    def mpn(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает MPN.
        
        :param value: MPN.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.mpn = value
        return True

    @property
    def ecotax(self) -> Optional[str]:
        """
        Свойство `ecotax`.

        :return: `ps_product.ecotax`
        :rtype: Optional[str]
        """
        return self.presta_fields.ecotax or ''

    @ecotax.setter
    @log_setter_errors
    def ecotax(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает ecotax.
        
        :param value: Ecotax.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.ecotax = value
        return True

    @property
    def minimal_quantity(self) -> Optional[int]:
        """
        Свойство `minimal_quantity`.

        :return: `ps_product.minimal_quantity`
        :rtype: Optional[int]
        """
        return self.presta_fields.minimal_quantity or ''

    @minimal_quantity.setter
    @log_setter_errors
    def minimal_quantity(self, value: int = 0) -> bool:
        """
        Устанавливает минимальное количество.
        
        :param value: Минимальное количество.
        :type value: int, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.minimal_quantity = value
        return True

    @property
    def low_stock_threshold(self) -> Optional[int]:
        """
        Свойство `low_stock_threshold`.

        :return: `ps_product.low_stock_threshold`
        :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_threshold or ''

    @low_stock_threshold.setter
    @log_setter_errors
    def low_stock_threshold(self, value: str = '') -> bool:
        """
        Устанавливает порог низкого запаса.
        
        :param value: Порог низкого запаса.
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.low_stock_threshold = value
        return True

    @property
    def low_stock_alert(self) -> Optional[int]:
        """
        Свойство `low_stock_alert`.

        :return: `ps_product.low_stock_alert`
        :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_alert or ''

    @low_stock_alert.setter
    @log_setter_errors
    def low_stock_alert(self, value: int = 0) -> bool:
        """
        Устанавливает флаг уведомления о низком запасе.
        
        :param value: Флаг уведомления о низком запасе.
        :type value: int, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.low_stock_alert = value
        return True

    @property
    def price(self) -> Optional[float]:
        """
        Свойство `price`.

        :return: `ps_product.price`
        :rtype: Optional[float]
        """
        return self.presta_fields.price or 0

    @price.setter
    @log_setter_errors
    def price(self, value: Union[str, int, float]) -> bool:
        """
        Устанавливает цену товара.
        
        :param value: Цена товара.
        :type value: Union[str, int, float]
        
        :return: True в случае успеха.
        :rtype: bool
        """
        if not value:
            return False
        self.presta_fields.price = value
        return True

    @property
    def wholesale_price(self) -> Optional[float]:
        """
        Свойство `wholesale_price`.

        :return: `ps_product.wholesale_price`
        :rtype: Optional[float]
        """
        return self.presta_fields.wholesale_price or ''

    @wholesale_price.setter
    @log_setter_errors
    def wholesale_price(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает оптовую цену.
        
        :param value: Оптовая цена.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.wholesale_price = value
        return True

    @property
    def unity(self) -> Optional[str]:
        """
        Свойство `unity`.

        :return: `ps_product.unity`
        :rtype: Optional[str]
        """
        return self.presta_fields.unity or ''

    @unity.setter
    @log_setter_errors
    def unity(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает единицу измерения.
        
        :param value: Единица измерения.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.unity = value
        return True

    @property
    def unit_price_ratio(self) -> Optional[float]:
        """
        Свойство `unit_price_ratio`.

        :return: `ps_product.unit_price_ratio`
        :rtype: Optional[float]
        """
        return self.presta_fields.unit_price_ratio or ''

    @unit_price_ratio.setter
    @log_setter_errors
    def unit_price_ratio(self, value: float = 0) -> bool:
        """
        Устанавливает коэффициент цены за единицу.
        
        :param value: Коэффициент цены за единицу.
        :type value: float, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.unit_price_ratio = value
        return True

    @property
    def additional_shipping_cost(self) -> Optional[float]:
        """
        Свойство `additional_shipping_cost`.

        :return: `ps_product.additional_shipping_cost`
        :rtype: Optional[float]
        """
        return self.presta_fields.additional_shipping_cost or ''

    @additional_shipping_cost.setter
    @log_setter_errors
    def additional_shipping_cost(self, value: int = 1) -> bool:
        """
        Устанавливает дополнительную стоимость доставки.
        
        :param value: Дополнительная стоимость доставки.
        :type value: int, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.additional_shipping_cost = value
        return True

    @property
    def reference(self) -> Optional[str]:
        """
        Свойство `reference`.

        :return: `ps_product.reference`
        :rtype: Optional[str]
        """
        return self.presta_fields.reference or ''

    @reference.setter
    @log_setter_errors
    def reference(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает артикул.
        
        :param value: Артикул.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.reference = str(value)
        return True

    @property
    def supplier_reference(self) -> Optional[str]:
        """
        Свойство `supplier_reference`.

        :return: `ps_product.supplier_reference`
        :rtype: Optional[str]
        """
        return self.presta_fields.supplier_reference  or ''

    @supplier_reference.setter
    @log_setter_errors
    def supplier_reference(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает артикул поставщика.
        
        :param value: Артикул поставщика.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.supplier_reference = str(value)
        return True

    @property
    def location(self) -> Optional[str]:
        """
        Свойство `location`.

        :return: `ps_product.location`
        :rtype: Optional[str]
        """
        return self.presta_fields.location or ''

    @location.setter
    @log_setter_errors
    def location(self, value: str = None, lang: str = 'en') -> bool:
        """
        Устанавливает местоположение.
        
        :param value: Местоположение.
        :type value: str, optional
        
        :param lang: Язык
        :type value: str, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.location = value
        return True

    @property
    def width(self) -> Optional[float]:
        """
        Свойство `width`.

        :return: `ps_product.width`
        :rtype: Optional[float]
        """
        return self.presta_fields.width or ''

    @width.setter
    @log_setter_errors
    def width(self, value: float = None) -> bool:
        """
        Устанавливает ширину.
        
        :param value: Ширина.
        :type value: float, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.width = value
        return True

    @property
    def height(self) -> Optional[float]:
        """
        Свойство `height`.

        :return: `ps_product.height`
        :rtype: Optional[float]
        """
        return self.presta_fields.height or ''

    @height.setter
    @log_setter_errors
    def height(self, value: float = None) -> bool:
        """
        Устанавливает высоту.
        
        :param value: Высота.
        :type value: float, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.height = value
        return True

    @property
    def depth(self) -> Optional[float]:
        """
        Свойство `depth`.

        :return: `ps_product.depth`
        :rtype: Optional[float]
        """
        return self.presta_fields.depth or ''

    @depth.setter
    @log_setter_errors
    def depth(self, value: float = None) -> bool:
        """
        Устанавливает глубину.
        
        :param value: Глубина.
        :type value: float, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.depth = value
        return True

    @property
    def weight(self) -> Optional[float]:
        """
        Свойство `weight`.

        :return: `ps_product.weight`
        :rtype: Optional[float]
        """
        return self.presta_fields.weight or ''

    @weight.setter
    @log_setter_errors
    def weight(self, value: float = None) -> bool:
        """
        Устанавливает вес.
        
        :param value: Вес.
        :type value: float, optional
        
        :return: True в случае успеха.
        :rtype: bool
        """
        self.presta_fields.weight = value
        return True

    @property
    def volume(self) -> Optional[int]:
        """
         Свойство `volume`.

         :return: `ps_product.volume`
         :rtype: Optional[int]
        """
        return self.presta_fields.volume  or ''
    
    @volume.setter
    @log_setter_errors
    def volume(self, value: int = 0) -> bool:
        """
         Устанавливает объем.
         
         :param value: Объем.
         :type value: int, optional
         
         :return: True в случае успеха.
         :rtype: bool
        """
        self.presta_fields.volume = value
        return True

    @property
    def out_of_stock(self) -> Optional[int]:
        """
         Свойство `out_of_stock`.

         :return: `ps_product.out_of_stock`
         :rtype: Optional[int]
        """
        return self.presta_fields.out_of_stock or ''

    @out_of_stock.setter
    @log_setter_errors
    def out_of_stock(self, value: int = None) -> bool:
        """
         Устанавливает флаг "нет в наличии".
         
         :param value: Флаг "нет в наличии".
         :type value: int, optional
         
         :return: True в случае успеха.
         :rtype: bool
        """
        self.presta_fields.out_of_stock = value
        return True

    @property
    def additional_delivery_times(self) -> Optional[int]:
        """
         Свойство `additional_delivery_times