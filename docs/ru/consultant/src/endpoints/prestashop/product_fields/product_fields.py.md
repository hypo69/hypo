### Анализ кода модуля `product_fields`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование `dataclass` для представления структуры данных.
    - Применение `SimpleNamespace` для доступа к данным по атрибутам.
    - Аккуратное разделение на свойства и сеттеры с документацией.
    - Логирование ошибок через `logger.error`.
    - Понятная структура с разделением на поля `ps_product` и `ps_product_lang`.
- **Минусы**:
    - Избыточное использование `try-except` блоков с пустым `return` внутри, что может затруднить отладку.
    - Непоследовательное использование `None` и `''` для пустых значений.
    - Смешивание типов данных в сеттерах (например, `value: str | int | float` в `price`).
    - Большое количество повторяющегося кода в сеттерах (логика обработки ошибок).
    - Отсутствие валидации входных данных перед присвоением значения.
    - Использование `getattr` и `setattr` вместо прямого доступа к атрибутам.
    - Комментарии `__prod_desc__` неинформативны.
    - Непоследовательное использование f-строк и конкатенации строк в сообщениях логера.
    - Дублирование кода для `id_shop` и `id_shop_default`.
    - Некоторые методы не возвращают `bool` при успехе, а просто завершаются.
    - Код `if value: ... else: ...` для установки `page_lang` можно упростить.
    - Поля типа `dict` инициализируются с помощью костылей, лучше использовать `default_factory`

**Рекомендации по улучшению**:

- **Унификация обработки ошибок**:
    - Вместо множества `try-except` блоков в сеттерах, можно создать общий обработчик ошибок, который будет логировать ошибку и возвращать `False`.
- **Приведение типов**:
    - В сеттерах следует явно приводить входные данные к ожидаемому типу перед присвоением.
- **Валидация данных**:
    - Добавить проверки данных перед присвоением. Например, проверять, что `id` является целым числом.
- **Унификация пустых значений**:
    - Использовать `None` для представления пустых значений и проверять на `None` при получении значения.
- **Рефакторинг сеттеров**:
    - Избегать повторений кода, вынося общие операции в отдельные методы.
    - Сделать явным возвращение `bool` в сеттерах.
- **Улучшение комментариев**:
    - Заменить `__prod_desc__` на более точные и информативные описания полей.
- **Форматирование строк**:
    - Привести все строки к единому формату, используя f-строки.
- **Устранение дублирования**:
    - Объединить методы `id_shop` и `id_shop_default` в один, передавая атрибут для установки.
- **Упрощение инициализации полей dict**:
     - Использовать  `default_factory=dict` для полей типа `dict`, а не инициализировать их в `__post_init__`
- **Упрощение кода для  `page_lang`**:
   -  Упростить установку через `self.assist_fields_dict['page_lang'] = value`

**Оптимизированный код**:

```python
"""
Модуль для работы с полями товаров PrestaShop.
==================================================

Модуль содержит класс :class:`ProductFields`, который используется для представления и управления полями товаров в PrestaShop.
Он обеспечивает методы для установки и получения значений различных полей товаров, включая основные и мультиязычные поля,
а также поддерживает обработку ошибок и логирование.

Пример использования
----------------------
.. code-block:: python

    from src.endpoints.prestashop.product_fields.product_fields import ProductFields
    
    product_fields = ProductFields(lang_index=1)
    product_fields.id_product = 123
    print(product_fields.id_product)

"""

import asyncio
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional
from types import SimpleNamespace

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file
from src.utils.convertors.dict import dict2ns
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException


@dataclass
class ProductFields:
    """
    Класс, описывающий поля товара в формате API PrestaShop.

    :param lang_index: Индекс языка для мультиязычных полей.
    :type lang_index: int
    :param product_fields_list: Список полей товара (инициализируется автоматически).
    :type product_fields_list: List[str]
    :param presta_fields: Объект `SimpleNamespace` для хранения полей PrestaShop (инициализируется автоматически).
    :type presta_fields: SimpleNamespace
    :param assist_fields_dict: Словарь для хранения служебных полей, таких как URL изображений и код языка (инициализируется автоматически).
    :type assist_fields_dict: Dict[str, any]
    :param base_path: Базовый путь к файлам конфигурации PrestaShop.
    :type base_path: Path

    """
    lang_index: int
    product_fields_list: List[str] = field(init=False)
    presta_fields: SimpleNamespace = field(init=False)
    assist_fields_dict: Dict[str, any] = field(default_factory=lambda: {
        'default_image_url': '',
        'images_urls': []
    })
    base_path: Path = gs.path.endpoints / 'prestashop'

    def __post_init__(self):
        """
        Инициализация класса после создания экземпляра. Загружаются данные полей, языков и их идентификаторов.
        """
        if not self._payload():
            logger.debug("Ошибка загрузки полей")
            ...
            return

    def _payload(self) -> bool:
        """
        Загрузка дефолтных значений полей.

        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        presta_fields_list = read_text_file(self.base_path / 'product_fields' / 'fields_list.txt', as_list=True)
        if not presta_fields_list:
            logger.error("Ошибка загрузки файла со списком полей")
            return False

        try:
            self.presta_fields = SimpleNamespace(**{key: None for key in presta_fields_list})
        except Exception as ex:
            logger.error(f"Ошибка конвертации {ex=}")
            return False

        data_ns = j_loads_ns(self.base_path / 'product_fields' / 'product_fields_default_values.json')
        if not data_ns:
            logger.debug("Ошибка загрузки полей из файла product_fields_default_values.json")
            return False

        try:
            for name in data_ns.__dict__:
                value = getattr(data_ns, name)
                setattr(self.presta_fields, name, value)
            return True
        except Exception as ex:
            logger.error(f"Ошибка при инициализации полей {ex=}")
            return False

    @property
    def associations(self) -> Optional[Dict]:
        """
        Возвращает словарь ключей ассоциаций.

        :return: Словарь ключей ассоциаций, или None, если не установлен.
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
         <sub>*[property]*</sub>  `ps_product.id: int(10) unsigned`

        :return: ID товара.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int = None) -> bool:
        """
        <sub>*[setter]*</sub>  `ID` товара. *для нового товара id назначается из `PrestaShop`*

        :param value: ID товара.
        :type value: int, optional
        :return: True, если ID товара успешно установлен, иначе False.
        :rtype: bool

        :details: Запись нового товара в PrestaShop делается в два шага:
            -> в PrestaShop заносятся параметры, которые не связаны с ID, например, название товара, артикул и т.п.
            <- От PrestaShop возвращается словарь, в котором установлен ID.
            -> теперь можно грузить фото, доп. параметры, короче все, что завязано на id товара
        """
        return self._set_field('id_product', value, int)

    @property
    def id_supplier(self) -> Optional[int]:
        """
        <sub>*[property]*</sub>  `ps_product.id_supplier: int(10) unsigned`
         @details: привязываю товар к id поставщика

        :return: ID поставщика.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_supplier

    @id_supplier.setter
    def id_supplier(self, value: int = None) -> bool:
        """
        <sub>*[setter]*</sub>  Устанавливает ID поставщика.

        :param value: ID поставщика.
        :type value: int, optional
        :return: True, если ID поставщика успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_supplier', value, int)

    @property
    def id_manufacturer(self) -> Optional[int]:
        """
        <sub>*[property]*</sub> `ps_product.id_manufacturer: int(10) unsigned`
        field
        @details: means BRAND.
            Бренд может быть передан как по имени так и по ID.
            Таблица брендов:
        :return: ID производителя.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_manufacturer

    @id_manufacturer.setter
    def id_manufacturer(self, value: int = None) -> bool:
        """
        <sub>*[setter]*</sub>  Бренд может быть передан как по имени так и по ID
        `ps_product.id_manufacturer`
        field type: int(10) unsigned
        @details: привязываю товар к бренду

        :param value: ID производителя.
        :type value: int, optional
        :return: True, если ID производителя успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_manufacturer', value, int)

    @property
    def id_category_default(self) -> Optional[int]:
        """
         <sub>*[property]*</sub>  `ps_product.id_category_default: int(10) unsigned`
         @details: привязываю товар к главной категории для этого товара
         :return: ID категории по умолчанию.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_category_default

    @id_category_default.setter
    def id_category_default(self, value: int) -> bool:
        """
        <sub>*[setter]*</sub> Сюда передается та категория, которая будет однозначно родительской `ps_product.id_category_default: int(10) unsigned`

        :param value: ID категории по умолчанию.
        :type value: int
         :return: True, если ID категории успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_category_default', value, int)

    @property
    def additional_categories(self) -> Optional[list]:
        """
         <sub>*[property]*</sub>
        возвращает словарь категорий товара восстановленный из файла сценария таблица `ps_category_product`

        :return: Дополнительные категории.
        :rtype: Optional[list]
        """
        if not hasattr(self.presta_fields.associations, 'categories'):
            return None

        if not hasattr(self.presta_fields.associations.categories, 'category'):
           return None
        return self.presta_fields.associations.categories.category

    @additional_categories.setter
    def additional_categories(self, value: int | list[int]) -> bool:
        """
        <sub>*[setter]*</sub>   Дополнительные к основной категории.
        При задании доп ключей предыдущие значения заменяются новыми из `additional_categories`.
        Для добавления новых к уже существующим используй  функцию additional_categories_append()

        :param value: ID категории или список ID категорий.
        :type value: int | list[int]
        :return: True, если дополнительные категории успешно установлены, иначе False.
        :rtype: bool
        """
        if not hasattr(self.presta_fields.associations, 'categories'):
            self.presta_fields.associations.categories = SimpleNamespace(category=[])

        value = value if isinstance(value, list) else [value]
        try:
            for v in value:
                 v = int(v)
                 self.presta_fields.associations.categories.category.append(SimpleNamespace(id=v))
            return True
        except Exception as ex:
             logger.error(f"Ошибка при  установке additional_categories {v=} {ex=}")
             return False
    @property
    def id_shop_default(self) -> Optional[int]:
        """
         <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
        @details: ID магазина по умолчанию. Используется в multishop

        :return: ID магазина по умолчанию.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop_default

    @id_shop_default.setter
    def id_shop_default(self, value: int = None) -> bool:
        """
        <sub>*[setter]*</sub>   `ps_product.id_shop_default: int(10) unsigned`
        `ID` магазина заказчика

        :param value: ID магазина по умолчанию.
        :type value: int, optional
         :return: True, если ID магазина успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_shop_default', value or 1, int)

    @property
    def id_shop(self) -> Optional[int]:
        """
        <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
        @details: ID магазина по умолчанию. Используется multishop

        :return: ID магазина.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_shop

    @id_shop.setter
    def id_shop(self, value: int = None) -> bool:
        """
         <sub>*[setter]*</sub>   `ps_product.id_shop: int(10) unsigned`
            `ID` магазина заказчика
        :param value: ID магазина.
        :type value: int, optional
         :return: True, если ID магазина успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_shop', value or 1, int)

    @property
    def id_tax(self) -> Optional[int]:
        """
        <sub>*[property]*</sub> tax_rule `int`  :  `ID` НДС  `ps_product.id_tax: int(10) unsigned`

        :return: ID налога.
        :rtype: Optional[int]
        """
        return self.presta_fields.id_tax

    @id_tax.setter
    def id_tax(self, value: int) -> bool:
        """
        <sub>*[setter]*</sub>  `ID` ндс. מע"מ = 13

        :param value: ID налога.
        :type value: int
         :return: True, если ID налога успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('id_tax', value, int)

    @property
    def on_sale(self) -> Optional[int]:
        """
        <sub>*[property]*</sub> `ps_product.on_sale: tinyint(1)  unsigned`

        :return: Признак распродажи.
        :rtype: Optional[int]
        """
        return self.presta_fields.on_sale

    @on_sale.setter
    def on_sale(self, value: int = 0) -> bool:
        """
        <sub>*[setter]*</sub> `1` - распродажа

        :param value: Признак распродажи.
        :type value: int, optional
         :return: True, если признак распродажи успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('on_sale', value, int)

    @property
    def online_only(self) -> Optional[int]:
        """
         <sub>*[property]*</sub>   `ps_product.online_only: tinyint(1) unsigned`
        field DB type: tinyint(1) unsigned
         @details: товар только онлайн

        :return: Признак "только онлайн".
        :rtype: Optional[int]
        """
        return self.presta_fields.online_only

    @online_only.setter
    def online_only(self, value: int = 0) -> bool:
        """
        <sub>*[setter]*</sub> Устанавливает признак "только онлайн".

        :param value: Признак "только онлайн".
        :type value: int, optional
        :return: True, если признак "только онлайн" успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('online_only', value, int)

    @property
    def ean13(self) -> Optional[str]:
        """
         <sub>*[property]*</sub>   `ps_product.ean13  varchar(13)`
        field DB type:
         @details: __prod_desc__

        :return: EAN13 товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.ean13

    @ean13.setter
    def ean13(self, value: str = None) -> bool:
        """
         <sub>*[setter]*</sub>   `ean13`
        field DB type:  varchar(13)
         @details: __prod_desc__

        :param value: EAN13 товара.
        :type value: str, optional
         :return: True, если EAN13 товара успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('ean13', value, str)

    @property
    def isbn(self) -> Optional[str]:
        """
        <sub>*[property]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__

        :return: ISBN товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.isbn

    @isbn.setter
    def isbn(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>   `isbn`
        field DB type: varchar(32)
         @details: __prod_desc__

        :param value: ISBN товара.
        :type value: str, optional
         :return: True, если ISBN товара успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('isbn', value, str)

    @property
    def upc(self) -> Optional[str]:
        """
        <sub>*[property]*</sub>   `upc`
        field DB type: varchar(12)
         @details: __prod_desc__

        :return: UPC товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.upc

    @upc.setter
    def upc(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>   `ps_product.upc`
        field DB type: varchar(12)
         @details: __prod_desc__

        :param value: UPC товара.
        :type value: str, optional
         :return: True, если UPC товара успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('upc', value, str)

    @property
    def mpn(self) -> Optional[str]:
        """
         <sub>*[property]*</sub>   `ps_product.mpn`
        field DB type: varchar(40)
         @details: __prod_desc__

        :return: MPN товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.mpn

    @mpn.setter
    def mpn(self, value: str = None) -> bool:
        """
         <sub>*[setter]*</sub>   Устанавливает MPN товара.

        :param value: MPN товара.
        :type value: str, optional
        :return: True, если MPN товара успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('mpn', value, str)

    @property
    def ecotax(self) -> Optional[str]:
        """
         <sub>*[property]*</sub>   `ps_product.ecotax`
        field DB type:  decimal(17,6)
         @details: __prod_desc__

        :return: Ecotax.
        :rtype: Optional[str]
        """
        return self.presta_fields.ecotax

    @ecotax.setter
    def ecotax(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>  Устанавливает ecotax.

        :param value: Ecotax.
        :type value: str, optional
         :return: True, если ecotax успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('ecotax', value, str)

    @property
    def minimal_quantity(self) -> Optional[int]:
        """
         <sub>*[property]*</sub>  `ps_product.minimal_quantity`
        field DB type: int(10)
         @details: __prod_desc__

        :return: Минимальное количество товара.
        :rtype: Optional[int]
        """
        return self.presta_fields.minimal_quantity

    @minimal_quantity.setter
    def minimal_quantity(self, value: int = 0) -> bool:
        """
        <sub>*[setter]*</sub>  Устанавливает минимальное количество товара.

        :param value: Минимальное количество товара.
        :type value: int, optional
         :return: True, если минимальное количество товара успешно установлено, иначе False.
        :rtype: bool
        """
        return self._set_field('minimal_quantity', value, int)

    @property
    def low_stock_threshold(self) -> Optional[int]:
        """
         <sub>*[property]*</sub>  `ps_product.low_stock_threshold`
        field DB type: int(10)
         @details: __prod_desc__

        :return: Порог низкого запаса.
        :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_threshold

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: int = None) -> bool:
        """
        <sub>*[setter]*</sub>   Устанавливает порог низкого запаса.

        :param value: Порог низкого запаса.
        :type value: int, optional
        :return: True, если порог низкого запаса успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('low_stock_threshold', value, int)

    @property
    def low_stock_alert(self) -> Optional[int]:
        """
        <sub>*[property]*</sub>  `ps_product.low_stock_alert`
        field DB type: tinyint(1)
         @details: __prod_desc__

        :return: Признак оповещения о низком запасе.
        :rtype: Optional[int]
        """
        return self.presta_fields.low_stock_alert

    @low_stock_alert.setter
    def low_stock_alert(self, value: int = 0) -> bool:
        """
        <sub>*[setter]*</sub>   Устанавливает признак оповещения о низком запасе.

        :param value: Признак оповещения о низком запасе.
        :type value: int, optional
         :return: True, если признак оповещения о низком запасе успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('low_stock_alert', value, int)

    @property
    def price(self) -> Optional[float]:
        """
         <sub>*[property]*</sub>  `ps_product.price`
        field DB type: decimal(20,6)
         @details: __prod_desc__

        :return: Цена товара.
        :rtype: Optional[float]
        """
        return self.presta_fields.price

    @price.setter
    def price(self, value: float = None) -> bool:
        """
         <sub>*[setter]*</sub>   Устанавливает цену товара.

        :param value: Цена товара.
        :type value: int | float | str, optional
         :return: True, если цена товара успешно установлена, иначе False.
        :rtype: bool
        """
        return self._set_field('price', value, float)

    @property
    def wholesale_price(self) -> Optional[float]:
        """
        <sub>*[property]*</sub>  `ps_product.wholesale_price`
        field DB type: decimal(20,6)
         @details: __prod_desc__

        :return: Оптовая цена товара.
        :rtype: Optional[float]
        """
        return self.presta_fields.wholesale_price

    @wholesale_price.setter
    def wholesale_price(self, value: float = None) -> bool:
        """
        <sub>*[setter]*</sub>  Устанавливает оптовую цену товара.

        :param value: Оптовая цена товара.
        :type value: str, optional
         :return: True, если оптовая цена товара успешно установлена, иначе False.
        :rtype: bool
        """
        return self._set_field('wholesale_price', value, float)

    @property
    def unity(self) -> Optional[str]:
        """
        <sub>*[property]*</sub>  `ps_product.unity`
        field DB type: varchar(255)
         @details: __prod_desc__

        :return: Единица измерения товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.unity

    @unity.setter
    def unity(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>   Устанавливает единицу измерения товара.

        :param value: Единица измерения товара.
        :type value: str, optional
         :return: True, если единица измерения товара успешно установлена, иначе False.
        :rtype: bool
        """
        return self._set_field('unity', value, str)

    @property
    def unit_price_ratio(self) -> Optional[float]:
        """
        <sub>*[property]*</sub>  `ps_product.unit_price_ratio`
        field DB type: decimal(20,6)
        Тип значения для `unit_price_ratio`  может быть:
        1. **Число с плавающей запятой (float)**:
            Если `unit_price_ratio` представляет собой отношение или коэффициент,
            то его значение чаще всего будет дробным числом, например, 1.5 или 0.75.
        2. **Целое число (int)**: В некоторых случаях это может быть целое число,
            например, если речь идет о коэффициенте в целочисленном формате, например, 2 (что может означать удвоение цены).
        3. **Строка (str)**: В редких случаях, если значение может включать специальные обозначения или единицы измерения,
            его можно представить в виде строки, например, "1.5x".
        Обычно в большинстве приложений и систем управления данными наиболее распространённый тип для коэффициента — это **число с плавающей запятой (float)**.

        :return: Коэффициент цены за единицу.
        :rtype: Optional[float]
        """
        return self.presta_fields.unit_price_ratio

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float = 0) -> bool:
        """
        <sub>*[setter]*</sub>   Устанавливает коэффициент цены за единицу.

        :param value: Коэффициент цены за единицу.
        :type value: float, optional
         :return: True, если коэффициент цены за единицу успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('unit_price_ratio', value, float)

    @property
    def additional_shipping_cost(self) -> Optional[float]:
        """
         <sub>*[property]*</sub> `ps_product.additional_shipping_cost`
        field DB type: decimal(20,6)
         @details: __prod_desc__

        :return: Дополнительная стоимость доставки.
        :rtype: Optional[float]
        """
        return self.presta_fields.additional_shipping_cost

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: int = 0) -> bool:
        """
         <sub>*[setter]*</sub>   Устанавливает дополнительную стоимость доставки.

        :param value: Дополнительная стоимость доставки.
        :type value: int, optional
        :return: True, если дополнительная стоимость доставки успешно установлена, иначе False.
        :rtype: bool
        """
        return self._set_field('additional_shipping_cost', value, float)

    @property
    def reference(self) -> Optional[str]:
        """
        <sub>*[property]*</sub> `ps_product.reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__

        :return: Артикул товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.reference

    @reference.setter
    def reference(self, value: str = None) -> bool:
        """
         <sub>*[setter]*</sub>   Устанавливает артикул товара.

        :param value: Артикул товара.
        :type value: str, optional
         :return: True, если артикул товара успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('reference', value, str)

    @property
    def supplier_reference(self) -> Optional[str]:
        """
         <sub>*[property]*</sub>  `ps_product.supplier_reference`
        field DB type: `varchar(64)`
         @details: __prod_desc__

        :return: Артикул поставщика.
        :rtype: Optional[str]
        """
        return self.presta_fields.supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>   Устанавливает артикул поставщика.

        :param value: Артикул поставщика.
        :type value: str, optional
         :return: True, если артикул поставщика успешно установлен, иначе False.
        :rtype: bool
        """
        return self._set_field('supplier_reference', value, str)

    @property
    def location(self) -> Optional[str]:
        """
         <sub>*[property]*</sub> `ps_product.location`
        field DB type: varchar(255)
         @details: __prod_desc__

        :return: Местоположение товара.
        :rtype: Optional[str]
        """
        return self.presta_fields.location

    @location.setter
    def location(self, value: str = None) -> bool:
        """
        <sub>*[setter]*</sub>  Устанавливает местоположение товара.

        :param value: Местоположение товара.
        :type value: str, optional
         :return: True, если местоположение товара успешно установлено, иначе False.
        :rtype: bool
        """
        return self._set_field('location', value, str)

    @property
    def width(self) -> Optional[float]:
        """
         <sub>*[property]*</sub> `ps_product.width`
        field DB type: decimal(20,6)
         @details: __prod_desc__

        :return: Ширина товара.
        :rtype: Optional[float]
        """
        return self.presta_fields.width

    @width.setter
    def width(self, value: float = None) -> bool:
        """
         <sub>*[setter]*</sub>   Устанавливает ширину товара.

        :param value: Ширина товара.
        :type value: float, optional
         :return: True, если ширина товара успешно установлена, иначе False.
        :rtype: bool
        """
        return self._set_field('width', value, float)

    @property
    def height(self) -> Optional[float]:
        """
        <sub>*[property]*</sub> `ps_product.height