# Анализ кода модуля `product`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Имеется подробное описание классов и их методов.
    - Используются статические методы, когда это необходимо.
    - Есть разделение на `Product`, `ProductFields` и `PrestaShop`, что соответствует принципу единственной ответственности.
 - Минусы
    - Отсутствуют docstring для классов и методов в коде.
    - Нет обработки исключений и логирования ошибок.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Не все импорты прописаны, и не указано что импортируется.
    - Используются стандартные блоки `try-except` вместо `logger.error`.
    - Повторяющаяся функциональность `get_parent_categories` в `Product` и `Category`

**Рекомендации по улучшению**

1. **Документация**:
   - Добавить docstring в формате reStructuredText (RST) для всех классов, методов и переменных.
   - Описать каждый класс и метод, включая параметры, возвращаемые значения и возможные исключения.
   - Включить примеры использования.
2. **Обработка данных**:
   - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов JSON.
3. **Логирование**:
    - Использовать `from src.logger.logger import logger` для логирования ошибок.
    - Заменить стандартные блоки `try-except` на `logger.error` для обработки ошибок.
4. **Структура кода**:
    - Проверить и добавить отсутствующие импорты в код.
    - Привести имена переменных в соответствие с ранее обработанными файлами.
    - Устранить дублирование функциональности `get_parent_categories`.
5. **Общая оптимизация**:
    -  Переработать структуру свойств `ProductFields`, чтобы добавить подробные описания, параметры, возвращаемые значения и исключения для каждого из них.
    - Улучшить читаемость кода за счет форматирования и комментариев.

**Оптимизированный код**
```python
"""
Модуль для работы с продуктами в PrestaShop
=========================================================================================

Этот модуль содержит класс :class:`Product`, который используется для взаимодействия с продуктами
в PrestaShop, включая получение данных с веб-страницы продукта и отправку данных через API PrestaShop.
Он также включает вспомогательные классы :class:`ProductFields` и использует методы :class:`PrestaShop`.

Пример использования
--------------------

Пример использования класса `Product`:

.. code-block:: python

    from src.product.product import Product

    product = Product(driver=driver,  api_url='...', api_key='...')
    product.load_from_web()
    product.update_in_prestashop()
"""
import json
from types import SimpleNamespace
from typing import List, Optional, Any, Dict
from src.utils.jjson import j_loads, j_loads_ns
from src.endpoints.prestashop import PrestaShop  # импорт класса PrestaShop
from src.product.product_fields.product_fields import ProductFields # импорт класса ProductFields
from src.category.category import Category # импорт класса Category
from src.logger.logger import logger

class Product(ProductFields, PrestaShop):
    """
    Класс для работы с продуктами, объединяющий функциональность полей продукта и API PrestaShop.

    :param args: Произвольные позиционные аргументы.
    :param kwargs: Произвольные именованные аргументы.
    """
    def __init__(self, *args, **kwargs):
        # Инициализирует класс Product, вызывая конструкторы родительских классов ProductFields и PrestaShop.
        super().__init__(*args, **kwargs)

    def get_parent_categories(self, id_category: int, dept: int = 0) -> list:
        """
        Возвращает список родительских категорий для заданной категории.

        Дублирует функциональность метода `get_parents` из класса `Category`.

        :param id_category: ID категории.
        :param dept: Глубина категории (по умолчанию 0).
        :return: Список родительских категорий.
        :raises TypeError: Если `id_category` не является целым числом.
        """
        # Проверяет, что id_category является целым числом, иначе вызывает исключение TypeError
        if not isinstance(id_category, int):
            logger.error(f'Ошибка типа данных: id_category должен быть целым числом, а не {type(id_category)}')
            raise TypeError(f'id_category должен быть целым числом, а не {type(id_category)}')
        # Вызывает статический метод get_parents из класса Category для получения списка родительских категорий
        return Category.get_parents(id_category, dept)

    @staticmethod
    def get_parent_categories_static(id_category: int, dept: int = 0) -> list:
        """
        Статический метод для получения списка родительских категорий.
        
        :param id_category: ID категории.
        :param dept: Глубина категории (по умолчанию 0).
        :return: Список родительских категорий.
        :raises TypeError: Если `id_category` не является целым числом.
        """
        # Проверяет, что id_category является целым числом, иначе вызывает исключение TypeError
        if not isinstance(id_category, int):
            logger.error(f'Ошибка типа данных: id_category должен быть целым числом, а не {type(id_category)}')
            raise TypeError(f'id_category должен быть целым числом, а не {type(id_category)}')
        # Вызывает статический метод get_parents из класса Category для получения списка родительских категорий
        return Category.get_parents(id_category, dept)


```
```python
"""
Модуль для работы с полями продукта
=========================================================================================

Этот модуль содержит класс :class:`ProductFields`, который используется для управления полями продукта.
Он загружает список полей продукта из файла, предоставляет методы для доступа и изменения этих полей
и обеспечивает базовую структуру для работы с данными продукта.

Пример использования
--------------------

Пример использования класса `ProductFields`:

.. code-block:: python

    from src.product.product_fields.product_fields import ProductFields

    product_fields = ProductFields()
    print(product_fields.presta_fields.name)
    product_fields.presta_fields.name = 'New Name'
"""
import json
from types import SimpleNamespace
from typing import List, Optional, Any, Dict
from src.utils.jjson import j_loads, j_loads_ns # импорт функций j_loads и j_loads_ns
from src.logger.logger import logger # импорт logger

class ProductFields:
    """
    Класс для работы с полями продукта, загружает и управляет данными о полях.

    :ivar product_fields_list: Список полей продукта.
    :ivar language: Словарь соответствия кодов языков и их ID.
    :ivar presta_fields: Объект `SimpleNamespace` для хранения полей продукта.
    :ivar assist_fields_dict: Словарь дополнительных полей (например, URL изображений).
    """

    def __init__(self):
        """
        Инициализирует объект `ProductFields`. Загружает список полей, языки и дефолтные значения.
        """
        # Загружает список полей продукта из файла
        self.product_fields_list = self._load_product_fields_list()
        # Загружает дефолтные значения полей
        self._payload()
        # Инициализирует словарь для хранения полей продукта
        self.presta_fields = SimpleNamespace()
        # Инициализирует словарь для хранения дополнительных полей
        self.assist_fields_dict = {}
        # Загружает соответствие между кодами языков и их ID
        self.language = j_loads_ns('src/config/language.json')

    def _load_product_fields_list(self) -> List[str]:
        """
        Загружает список полей продукта из файла.

        :return: Список полей продукта.
        :raises FileNotFoundError: Если файл `fields_list.txt` не найден.
        """
        try:
            # Открывает файл fields_list.txt и читает построчно все поля
            with open('src/product/product_fields/fields_list.txt', 'r', encoding='utf-8') as f:
                # Возвращает список полей продукта
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError as e:
             # Логирует ошибку, если файл не найден
            logger.error(f'Файл src/product/product_fields/fields_list.txt не найден: {e}')
            raise

    def _payload(self) -> bool:
        """
        Загружает дефолтные значения полей из файла `product_fields_default_values.json`.

        :return: `True`, если загрузка успешна, `False` в случае ошибки.
        """
        try:
            # Загружает JSON данные из файла product_fields_default_values.json, используя j_loads
            data = j_loads('src/product/product_fields/product_fields_default_values.json')
            if data:
                # Обновляет  словарь атрибутов экземпляра класса значениями из файла
                for key, value in data.items():
                    setattr(self.presta_fields, key, value)
                return True
            return False
        except Exception as e:
            # Логирует ошибку при загрузке данных
            logger.error(f'Ошибка загрузки дефолтных значений полей продукта из файла: {e}')
            return False

    @property
    def id_product(self) -> Optional[int]:
        """
         `ID` товара. Для нового товара ID назначается из PrestaShop.

        :return: `ID` товара, либо `None` если не установлен.
        """
        # Возвращает ID продукта из объекта presta_fields
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int) -> None:
        """
        Устанавливает `ID` товара.

        :param value: `ID` товара.
        """
        # Устанавливает значение id_product в объекте presta_fields
        self.presta_fields.id_product = value


    @property
    def id_supplier(self) -> Optional[int]:
        """
        `ID` поставщика товара.

        :return: `ID` поставщика, либо `None` если не установлен.
        """
        # Возвращает id_supplier из объекта presta_fields
        return self.presta_fields.id_supplier

    @id_supplier.setter
    def id_supplier(self, value: int) -> None:
        """
        Устанавливает `ID` поставщика товара.

        :param value: `ID` поставщика.
        """
        # Устанавливает значение id_supplier в объекте presta_fields
        self.presta_fields.id_supplier = value


    @property
    def id_manufacturer(self) -> Optional[int]:
        """
        `ID` производителя товара.

        :return: `ID` производителя, либо `None` если не установлен.
        """
        # Возвращает id_manufacturer из объекта presta_fields
        return self.presta_fields.id_manufacturer

    @id_manufacturer.setter
    def id_manufacturer(self, value: int) -> None:
        """
        Устанавливает `ID` производителя товара.

        :param value: `ID` производителя.
        """
        # Устанавливает значение id_manufacturer в объекте presta_fields
        self.presta_fields.id_manufacturer = value

    @property
    def id_category_default(self) -> Optional[int]:
        """
        `ID` категории по умолчанию для товара.

        :return: `ID` категории по умолчанию, либо `None` если не установлен.
        """
        # Возвращает id_category_default из объекта presta_fields
        return self.presta_fields.id_category_default

    @id_category_default.setter
    def id_category_default(self, value: int) -> None:
        """
        Устанавливает `ID` категории по умолчанию для товара.

        :param value: `ID` категории по умолчанию.
        """
        # Устанавливает значение id_category_default в объекте presta_fields
        self.presta_fields.id_category_default = value

    @property
    def id_shop_default(self) -> Optional[int]:
        """
        `ID` магазина по умолчанию для товара.

        :return: `ID` магазина по умолчанию, либо `None` если не установлен.
        """
        # Возвращает id_shop_default из объекта presta_fields
        return self.presta_fields.id_shop_default

    @id_shop_default.setter
    def id_shop_default(self, value: int) -> None:
        """
        Устанавливает `ID` магазина по умолчанию для товара.

        :param value: `ID` магазина по умолчанию.
        """
        # Устанавливает значение id_shop_default в объекте presta_fields
        self.presta_fields.id_shop_default = value

    @property
    def id_tax(self) -> Optional[int]:
        """
        `ID` налога для товара.

        :return: `ID` налога, либо `None` если не установлен.
        """
        # Возвращает id_tax из объекта presta_fields
        return self.presta_fields.id_tax

    @id_tax.setter
    def id_tax(self, value: int) -> None:
        """
        Устанавливает `ID` налога для товара.

        :param value: `ID` налога.
        """
        # Устанавливает значение id_tax в объекте presta_fields
        self.presta_fields.id_tax = value

    @property
    def on_sale(self) -> Optional[bool]:
        """
        Показывает, находится ли товар в продаже.

        :return: `True`, если товар в продаже, `False` если нет, или `None` если не установлено.
        """
        # Возвращает on_sale из объекта presta_fields
        return self.presta_fields.on_sale

    @on_sale.setter
    def on_sale(self, value: bool) -> None:
        """
        Устанавливает, находится ли товар в продаже.

        :param value: `True`, если товар в продаже, `False` если нет.
        """
        # Устанавливает значение on_sale в объекте presta_fields
        self.presta_fields.on_sale = value

    @property
    def online_only(self) -> Optional[bool]:
        """
        Показывает, доступен ли товар только онлайн.

        :return: `True`, если товар доступен только онлайн, `False` если нет, или `None` если не установлено.
        """
        # Возвращает online_only из объекта presta_fields
        return self.presta_fields.online_only

    @online_only.setter
    def online_only(self, value: bool) -> None:
        """
        Устанавливает, доступен ли товар только онлайн.

        :param value: `True`, если товар доступен только онлайн, `False` если нет.
        """
        # Устанавливает значение online_only в объекте presta_fields
        self.presta_fields.online_only = value

    @property
    def ean13(self) -> Optional[str]:
        """
        Штрихкод EAN13 товара.

        :return: Штрихкод EAN13, либо `None` если не установлен.
        """
        # Возвращает ean13 из объекта presta_fields
        return self.presta_fields.ean13

    @ean13.setter
    def ean13(self, value: str) -> None:
        """
        Устанавливает штрихкод EAN13 товара.

        :param value: Штрихкод EAN13.
        """
        # Устанавливает значение ean13 в объекте presta_fields
        self.presta_fields.ean13 = value

    @property
    def isbn(self) -> Optional[str]:
        """
        Международный стандартный книжный номер ISBN товара.

        :return: ISBN, либо `None` если не установлен.
        """
        # Возвращает isbn из объекта presta_fields
        return self.presta_fields.isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        """
        Устанавливает международный стандартный книжный номер ISBN товара.

        :param value: ISBN.
        """
        # Устанавливает значение isbn в объекте presta_fields
        self.presta_fields.isbn = value


    @property
    def upc(self) -> Optional[str]:
        """
        Универсальный код товара UPC.

        :return: Код UPC, либо `None` если не установлен.
        """
        # Возвращает upc из объекта presta_fields
        return self.presta_fields.upc

    @upc.setter
    def upc(self, value: str) -> None:
        """
        Устанавливает универсальный код товара UPC.

        :param value: Код UPC.
        """
        # Устанавливает значение upc в объекте presta_fields
        self.presta_fields.upc = value

    @property
    def mpn(self) -> Optional[str]:
        """
        Номер детали производителя MPN.

        :return: Номер MPN, либо `None` если не установлен.
        """
        # Возвращает mpn из объекта presta_fields
        return self.presta_fields.mpn

    @mpn.setter
    def mpn(self, value: str) -> None:
        """
        Устанавливает номер детали производителя MPN.

        :param value: Номер MPN.
        """
        # Устанавливает значение mpn в объекте presta_fields
        self.presta_fields.mpn = value


    @property
    def ecotax(self) -> Optional[float]:
        """
        Сумма экологического налога.

        :return: Сумма налога, либо `None` если не установлена.
        """
        # Возвращает ecotax из объекта presta_fields
        return self.presta_fields.ecotax

    @ecotax.setter
    def ecotax(self, value: float) -> None:
        """
        Устанавливает сумму экологического налога.

        :param value: Сумма налога.
        """
        # Устанавливает значение ecotax в объекте presta_fields
        self.presta_fields.ecotax = value

    @property
    def quantity(self) -> Optional[int]:
        """
        Количество товара на складе.

        :return: Количество товара, либо `None` если не установлено.
        """
        # Возвращает quantity из объекта presta_fields
        return self.presta_fields.quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Устанавливает количество товара на складе.

        :param value: Количество товара.
        """
        # Устанавливает значение quantity в объекте presta_fields
        self.presta_fields.quantity = value


    @property
    def minimal_quantity(self) -> Optional[int]:
        """
        Минимальное количество товара для заказа.

        :return: Минимальное количество, либо `None` если не установлено.
        """
        # Возвращает minimal_quantity из объекта presta_fields
        return self.presta_fields.minimal_quantity

    @minimal_quantity.setter
    def minimal_quantity(self, value: int) -> None:
        """
        Устанавливает минимальное количество товара для заказа.

        :param value: Минимальное количество.
        """
        # Устанавливает значение minimal_quantity в объекте presta_fields
        self.presta_fields.minimal_quantity = value


    @property
    def low_stock_threshold(self) -> Optional[int]:
         """
        Порог низкого запаса товара.

        :return: Порог низкого запаса, либо `None` если не установлен.
        """
         # Возвращает low_stock_threshold из объекта presta_fields
         return self.presta_fields.low_stock_threshold

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: int) -> None:
        """
        Устанавливает порог низкого запаса товара.

        :param value: Порог низкого запаса.
        """
        # Устанавливает значение low_stock_threshold в объекте presta_fields
        self.presta_fields.low_stock_threshold = value


    @property
    def low_stock_alert(self) -> Optional[bool]:
        """
        Включено ли оповещение о низком запасе.

        :return: `True` если оповещение включено, `False` если нет, или `None` если не установлено.
        """
        # Возвращает low_stock_alert из объекта presta_fields
        return self.presta_fields.low_stock_alert

    @low_stock_alert.setter
    def low_stock_alert(self, value: bool) -> None:
        """
        Устанавливает, включено ли оповещение о низком запасе.

        :param value: `True` если оповещение включено, `False` если нет.
        """
        # Устанавливает значение low_stock_alert в объекте presta_fields
        self.presta_fields.low_stock_alert = value

    @property
    def price(self) -> Optional[float]:
        """
        Цена товара.

        :return: Цена товара, либо `None` если не установлена.
        """
        # Возвращает price из объекта presta_fields
        return self.presta_fields.price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает цену товара.

        :param value: Цена товара.
        """
        # Устанавливает значение price в объекте presta_fields
        self.presta_fields.price = value


    @property
    def wholesale_price(self) -> Optional[float]:
        """
        Оптовая цена товара.

        :return: Оптовая цена, либо `None` если не установлена.
        """
        # Возвращает wholesale_price из объекта presta_fields
        return self.presta_fields.wholesale_price

    @wholesale_price.setter
    def wholesale_price(self, value: float) -> None:
        """
        Устанавливает оптовую цену товара.

        :param value: Оптовая цена.
        """
        # Устанавливает значение wholesale_price в объекте presta_fields
        self.presta_fields.wholesale_price = value


    @property
    def unity(self) -> Optional[str]:
        """
        Единица измерения товара.

        :return: Единица измерения, либо `None` если не установлена.
        """
        # Возвращает unity из объекта presta_fields
        return self.presta_fields.unity

    @unity.setter
    def unity(self, value: str) -> None:
        """
        Устанавливает единицу измерения товара.

        :param value: Единица измерения.
        """
        # Устанавливает значение unity в объекте presta_fields
        self.presta_fields.unity = value

    @property
    def unit_price_ratio(self) -> Optional[float]:
        """
        Соотношение цены за единицу товара.

        :return: Соотношение цены, либо `None` если не установлено.
        """
        # Возвращает unit_price_ratio из объекта presta_fields
        return self.presta_fields.unit_price_ratio

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float) -> None:
        """
        Устанавливает соотношение цены за единицу товара.

        :param value: Соотношение цены.
        """
        # Устанавливает значение unit_price_ratio в объекте presta_fields
        self.presta_fields.unit_price_ratio = value

    @property
    def additional_shipping_cost(self) -> Optional[float]:
        """
        Дополнительная стоимость доставки товара.

        :return: Стоимость доставки, либо `None` если не установлена.
        """
        # Возвращает additional_shipping_cost из объекта presta_fields
        return self.presta_fields.additional_shipping_cost

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: float) -> None:
        """
        Устанавливает дополнительную стоимость доставки товара.

        :param value: Стоимость доставки.
        """
        # Устанавливает значение additional_shipping_cost в объекте presta_fields
        self.presta_fields.additional_shipping_cost = value

    @property
    def reference(self) -> Optional[str]:
        """
        Артикул товара.

        :return: Артикул товара, либо `None` если не установлен.
        """
        # Возвращает reference из объекта presta_fields
        return self.presta_fields.reference

    @reference.setter
    def reference(self, value: str) -> None:
        """
        Устанавливает артикул товара.

        :param value: Артикул товара.
        """
        # Устанавливает значение reference в объекте presta_fields
        self.presta_fields.reference = value

    @property
    def supplier_reference(self) -> Optional[str]:
        """
        Артикул поставщика товара.

        :return: Артикул поставщика, либо `None` если не установлен.
        """
        # Возвращает supplier_reference из объекта presta_fields
        return self.presta_fields.supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, value: str) -> None:
        """
        Устанавливает артикул поставщика товара.

        :param value: Артикул поставщика.
        """
        # Устанавливает значение supplier_reference в объекте presta_fields
        self.presta_fields.supplier_reference = value


    @property
    def location(self) -> Optional[str]:
        """
        Местоположение товара на складе.

        :return: Местоположение товара, либо `None` если не установлено.
        """
        # Возвращает location из объекта presta_fields
        return self.presta_fields.location

    @location.setter
    def location(self, value: str) -> None:
         """
        Устанавливает местоположение товара на складе.

        :param value: Местоположение товара.
        """
         # Устанавливает значение location в объекте presta_fields
         self.presta_fields.location = value


    @property
    def width(self) -> Optional[float]:
        """
        Ширина товара.

        :return: Ширина товара, либо `None` если не установлена.
        """
        # Возвращает width из объекта presta_fields
        return self.presta_fields.width

    @width.setter
    def width(self, value: float) -> None:
        """
        Устанавливает ширину товара.

        :param value: Ширина товара.
        """
        # Устанавливает значение width в объекте presta_fields
        self.presta_fields.width = value

    @property
    def height(self) -> Optional[float]:
        """
        Высота товара.

        :return: Высота товара, либо `None` если не установлена.
        """
        # Возвращает height из объекта presta_fields
        return self.presta_fields.height

    @height.setter
    def height(self, value: float) -> None:
        """
        Устанавливает высоту товара.

        :param value: Высота товара.
        """
        # Устанавливает значение height в объекте presta_fields
        self.presta_fields.height = value

    @property
    def depth(self) -> Optional[float]:
        """
        Глубина товара.

        :return: Глубина товара, либо `None` если не установлена.
        """
        # Возвращает depth из объекта presta_fields
        return self.presta_fields.depth

    @depth.setter
    def depth(self, value: float) -> None:
        """
        Устанавливает глубину товара.

        :param value: Глубина товара.
        """
        # Устанавливает значение depth в объекте presta_fields
        self.presta_fields.depth = value


    @property
    def weight(self) -> Optional[float]:
        """
        Вес товара.

        :return: Вес товара, либо `None` если не установлен.
        """
        # Возвращает weight из объекта presta_fields
        return self.presta_fields.weight

    @weight.setter
    def weight(self, value: float) -> None:
        """
        Устанавливает вес товара.

        :param value: Вес товара.
        """
        # Устанавливает значение weight в объекте presta_fields
        self.presta_fields.weight = value


    @property
    def volume(self) -> Optional[float]:
        """
        Объем товара.

        :return: Объем товара, либо `None` если не установлен.
        """
        # Возвращает volume из объекта presta_fields
        return self.presta_fields.volume

    @volume.setter
    def volume(self, value: float) -> None:
        """
        Устанавливает объем товара.

        :param value: Объем товара.
        """
        # Устанавливает значение volume в объекте presta_fields
        self.presta_fields.volume = value


    @property
    def out_of_stock(self) -> Optional[int]:
        """
        Действие при отсутствии товара на складе.

        :return: Код действия, либо `None` если не установлен.
        """
        # Возвращает out_of_stock из объекта presta_fields
        return self.presta_fields.out_of_stock

    @out_of_stock.setter
    def out_of_stock(self, value: int) -> None:
        """
        Устанавливает действие при отсутствии товара на складе.

        :param value: Код действия.
        """
        # Устанавливает значение out_of_stock в объекте presta_fields
        self.presta_fields.out_of_stock = value


    @property
    def additional_delivery_times(self) -> Optional[int]:
        """
        Дополнительное время доставки.

        :return: Время доставки, либо `None` если не установлено.
        """
        # Возвращает additional_delivery_times из объекта presta_fields
        return self.presta_fields.additional_delivery_times

    @additional_delivery_times.setter
    def additional_delivery_times(self, value: int) -> None:
        """
        Устанавливает дополнительное время доставки.

        :param value: Время доставки.
        """
        # Устанавливает значение additional_delivery_times в объекте presta_fields
        self.presta_fields.additional_delivery_times = value


    @property
    def quantity_discount(self) -> Optional[bool]:
        """
        Разрешены ли скидки за количество.

        :return: `True` если скидки разрешены, `False` если нет, или `None` если не установлено.
        """
        # Возвращает quantity_discount из объекта presta_fields
        return self.presta_fields.quantity_discount

    @quantity_discount.setter
    def quantity_discount(self, value: bool) -> None:
        """
        Устанавливает, разрешены ли скидки за количество.

        :param value: `True` если скидки разрешены, `False` если нет.
        """
        # Устанавливает значение quantity_discount в объекте presta_fields
        self.presta_fields.quantity_discount = value

    @property
    def customizable(self) -> Optional[bool]:
         """
        Возможность кастомизации товара.

        :return: `True` если товар можно кастомизировать, `False` если нет, или `None` если не установлено.
        """
         # Возвращает customizable из объекта presta_fields
         return self.presta_fields.customizable

    @customizable.setter
    def customizable(self, value: bool) -> None:
        """
        Устанавливает возможность кастомизации товара.

        :param value: `True` если товар можно кастомизировать, `False` если нет.
        """
        # Устанавливает значение customizable в объекте presta_fields
        self.presta_fields.customizable = value


    @property
    def uploadable_files(self) -> Optional[int]:
         """
        Количество загружаемых файлов.

        :return: Количество файлов, либо `None` если не установлено.
        """
         # Возвращает uploadable_files из объекта presta_fields
         return self.presta_fields.uploadable_files

    @uploadable_files.setter
    def uploadable_files(self, value: int) -> None:
        """
        Устанавливает количество загружаемых файлов.

        :param value: Количество файлов.
        """
        # Устанавливает значение uploadable_files в объекте presta_fields
        self.presta_fields.uploadable_files = value

    @property
    def text_fields(self) -> Optional[int]:
         """
        Количество текстовых полей.

        :return: Количество текстовых полей, либо `None` если не установлено.
        """
         # Возвращает text_fields из объекта presta_fields
         return self.presta_fields.text_fields

    @text_fields.setter
    def text_fields(self, value: int)