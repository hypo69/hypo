# Анализ кода модуля `src.product`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разделен на модули с четкими обязанностями.
    - Присутствует подробное описание классов и их методов.
    - Документация в формате Markdown позволяет легко понять структуру кода и его назначение.
- Минусы
    - Отсутствуют `docstring` в коде.
    - Не используется логирование через `src.logger.logger`.
    - Не используется `j_loads` или `j_loads_ns` для загрузки `json`.
    - Нет примеров использования и обработки ошибок в описании методов.
    - Документация не соответствует стандарту reStructuredText (RST).

**Рекомендации по улучшению**

1.  **Документирование кода в RST:** Необходимо переписать документацию в формате reStructuredText (RST), включая docstring для классов, методов и функций.
2.  **Использование `j_loads`:** При загрузке JSON данных использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование ошибок:** Использовать `logger.error` для логирования ошибок вместо стандартных `try-except` блоков.
4.  **Добавление импортов:** Проверить и добавить необходимые импорты, которых нет в предоставленном коде.
5.  **Уточнение документации:** Уточнить документацию, добавив недостающие описания, примеры использования и обработки ошибок.
6.  **Рефакторинг:** Привести имена переменных, методов и классов в соответствие с ранее обработанными файлами, в том числе применить snake_case.
7.  **Добавить аннотации типов:** Добавить аннотации типов для параметров и возвращаемых значений функций и методов.

**Оптимизированный код**

```python
"""
Модуль для работы с продуктами PrestaShop.
=========================================

Этот модуль содержит классы для представления и управления продуктами
в PrestaShop, включая сбор данных с веб-сайта и взаимодействие с API.

Пример использования
--------------------

Пример инициализации класса Product:

.. code-block:: python

    from src.product.product import Product
    product = Product()
"""

from typing import List, Dict, Any
from types import SimpleNamespace
from src.endpoints.prestashop import PrestaShop  # импорт класса PrestaShop
from src.category.category import Category  # импорт класса Category
from src.product.product_fields.product_fields import ProductFields # импорт класса ProductFields
from src.utils.jjson import j_loads, j_loads_ns # импорт j_loads
from src.logger.logger import logger # импорт logger
#from src.endpoints.prestashop.product_fields import ProductFields # импорт ProductFields # Дубликат, удалил

class Product(ProductFields, PrestaShop):
    """
    Класс для представления и управления продуктами.

    Наследует функциональность от :class:`ProductFields` и :class:`PrestaShop`
    для работы с данными продукта и API PrestaShop.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализирует объект Product.

        :param args: Произвольные позиционные аргументы.
        :param kwargs: Произвольные именованные аргументы.
        """
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_parent_categories(id_category: int, dept: int = 0) -> List[Dict[str, Any]]:
        """
        Возвращает список родительских категорий для заданной категории.

        :param id_category: ID категории.
        :type id_category: int
        :param dept: Глубина категории, по умолчанию 0.
        :type dept: int, optional
        :raises TypeError: Если `id_category` не является целым числом.
        :return: Список родительских категорий.
        :rtype: List[Dict[str, Any]]
        """
        # Проверка типа id_category
        if not isinstance(id_category, int):
            logger.error(f'Ошибка типа данных: id_category={id_category} должен быть целым числом.') # Логируем ошибку
            raise TypeError(f'id_category должен быть целым числом, а не {type(id_category)}')
        try:
            # Код исполняет вызов метода get_parents из класса Category
            return Category.get_parents(id_category, dept)
        except Exception as ex:
             # Логирование любой ошибки
            logger.error(f'Ошибка при получении родительских категорий для id_category {id_category}: {ex}')
            return []


class ProductFields:
    """
    Класс для управления полями продукта.

    Предоставляет методы для доступа и изменения полей продукта,
    а также для загрузки данных из файлов.
    """
    def __init__(self):
        """
        Инициализирует объект ProductFields.

        Загружает список полей, языки и дефолтные значения.
        """
        self.product_fields_list = self._load_product_fields_list()
        self.language = self._load_languages()
        self.presta_fields = SimpleNamespace()
        self.assist_fields_dict = {}
        self._payload()

    def _load_product_fields_list(self) -> List[str]:
        """
        Загружает список полей из файла `fields_list.txt`.

        :return: Список полей продукта.
        :rtype: List[str]
        """
        try:
            # Код исполняет загрузку списка полей из файла fields_list.txt
            with open('fields_list.txt', 'r', encoding='utf-8') as file:
                return [line.strip() for line in file]
        except FileNotFoundError as ex:
            # Логирование ошибки если файл не найден
            logger.error(f'Файл fields_list.txt не найден: {ex}')
            return []
        except Exception as ex:
            # Логирование прочих ошибок при загрузке
            logger.error(f'Ошибка при загрузке списка полей: {ex}')
            return []

    def _load_languages(self) -> Dict[str, int]:
        """
        Загружает соответствие между кодами языков и их идентификаторами из файла `language.json`.

         :return: Словарь соответствия кодов языков и их идентификаторов.
        :rtype: Dict[str, int]
        """
        try:
             # Код исполняет загрузку языков из файла language.json
            with open('language.json', 'r', encoding='utf-8') as f:
                return j_loads(f)
        except FileNotFoundError as ex:
            # Логирование ошибки если файл не найден
            logger.error(f'Файл language.json не найден: {ex}')
            return {}
        except Exception as ex:
            # Логирование прочих ошибок при загрузке
            logger.error(f'Ошибка при загрузке языков: {ex}')
            return {}


    def _payload(self) -> bool:
        """
        Загружает дефолтные значения полей из файла `product_fields_default_values.json`.

        :return: True, если загрузка успешна, False в случае ошибки.
        :rtype: bool
        """
        try:
            # Код исполняет загрузку дефолтных значений полей из файла product_fields_default_values.json
            with open('product_fields_default_values.json', 'r', encoding='utf-8') as file:
                defaults = j_loads_ns(file)
                for field in self.product_fields_list:
                    setattr(self.presta_fields, field, getattr(defaults, field, None))
                return True
        except FileNotFoundError as ex:
            # Логирование ошибки если файл не найден
            logger.error(f'Файл product_fields_default_values.json не найден: {ex}')
            return False
        except Exception as ex:
            # Логирование прочих ошибок при загрузке
            logger.error(f'Ошибка при загрузке дефолтных значений полей: {ex}')
            return False

    @property
    def id_product(self) -> int:
        """
         Возвращает ID товара.

        :return: ID товара.
        :rtype: int
        """
        return self.presta_fields.id_product

    @id_product.setter
    def id_product(self, value: int) -> None:
        """
        Устанавливает ID товара.

        :param value: ID товара.
        :type value: int
        """
        self.presta_fields.id_product = value
    
    @property
    def id_supplier(self) -> int:
        """
         Возвращает ID поставщика.
        :return: ID поставщика
        :rtype: int
        """
        return self.presta_fields.id_supplier

    @id_supplier.setter
    def id_supplier(self, value: int) -> None:
        """
        Устанавливает ID поставщика.
        :param value: ID поставщика
        :type value: int
        """
        self.presta_fields.id_supplier = value
    
    @property
    def id_manufacturer(self) -> int:
        """
         Возвращает ID производителя.
        :return: ID производителя
        :rtype: int
        """
        return self.presta_fields.id_manufacturer

    @id_manufacturer.setter
    def id_manufacturer(self, value: int) -> None:
       """
       Устанавливает ID производителя.
       :param value: ID производителя
       :type value: int
       """
       self.presta_fields.id_manufacturer = value

    @property
    def id_category_default(self) -> int:
        """
        Возвращает ID категории по умолчанию.
        :return: ID категории по умолчанию.
        :rtype: int
        """
        return self.presta_fields.id_category_default

    @id_category_default.setter
    def id_category_default(self, value: int) -> None:
        """
        Устанавливает ID категории по умолчанию.
        :param value: ID категории по умолчанию.
        :type value: int
        """
        self.presta_fields.id_category_default = value

    @property
    def id_shop_default(self) -> int:
        """
        Возвращает ID магазина по умолчанию.
        :return: ID магазина по умолчанию.
        :rtype: int
        """
        return self.presta_fields.id_shop_default

    @id_shop_default.setter
    def id_shop_default(self, value: int) -> None:
        """
        Устанавливает ID магазина по умолчанию.
        :param value: ID магазина по умолчанию.
        :type value: int
        """
        self.presta_fields.id_shop_default = value

    @property
    def id_tax(self) -> int:
        """
        Возвращает ID налога.
        :return: ID налога.
        :rtype: int
        """
        return self.presta_fields.id_tax
    
    @id_tax.setter
    def id_tax(self, value: int) -> None:
        """
        Устанавливает ID налога.
        :param value: ID налога.
        :type value: int
        """
        self.presta_fields.id_tax = value

    @property
    def on_sale(self) -> bool:
        """
        Возвращает признак того, что товар на распродаже.
        :return: Признак распродажи.
        :rtype: bool
        """
        return self.presta_fields.on_sale

    @on_sale.setter
    def on_sale(self, value: bool) -> None:
        """
        Устанавливает признак того, что товар на распродаже.
        :param value: Признак распродажи.
        :type value: bool
        """
        self.presta_fields.on_sale = value

    @property
    def online_only(self) -> bool:
        """
        Возвращает признак того, что товар доступен только онлайн.
        :return: Признак доступности только онлайн.
        :rtype: bool
        """
        return self.presta_fields.online_only
    
    @online_only.setter
    def online_only(self, value: bool) -> None:
        """
        Устанавливает признак того, что товар доступен только онлайн.
        :param value: Признак доступности только онлайн.
        :type value: bool
        """
        self.presta_fields.online_only = value
    
    @property
    def ean13(self) -> str:
        """
        Возвращает EAN13 код товара.
        :return: EAN13 код товара.
        :rtype: str
        """
        return self.presta_fields.ean13
    
    @ean13.setter
    def ean13(self, value: str) -> None:
        """
        Устанавливает EAN13 код товара.
        :param value: EAN13 код товара.
        :type value: str
        """
        self.presta_fields.ean13 = value

    @property
    def isbn(self) -> str:
        """
        Возвращает ISBN код товара.
        :return: ISBN код товара.
        :rtype: str
        """
        return self.presta_fields.isbn
    
    @isbn.setter
    def isbn(self, value: str) -> None:
        """
        Устанавливает ISBN код товара.
        :param value: ISBN код товара.
        :type value: str
        """
        self.presta_fields.isbn = value

    @property
    def upc(self) -> str:
        """
        Возвращает UPC код товара.
        :return: UPC код товара.
        :rtype: str
        """
        return self.presta_fields.upc
    
    @upc.setter
    def upc(self, value: str) -> None:
        """
        Устанавливает UPC код товара.
        :param value: UPC код товара.
        :type value: str
        """
        self.presta_fields.upc = value

    @property
    def mpn(self) -> str:
        """
        Возвращает MPN код товара.
        :return: MPN код товара.
        :rtype: str
        """
        return self.presta_fields.mpn

    @mpn.setter
    def mpn(self, value: str) -> None:
        """
        Устанавливает MPN код товара.
        :param value: MPN код товара.
        :type value: str
        """
        self.presta_fields.mpn = value

    @property
    def ecotax(self) -> float:
        """
        Возвращает значение эконалога.
        :return: Эконалог.
        :rtype: float
        """
        return self.presta_fields.ecotax

    @ecotax.setter
    def ecotax(self, value: float) -> None:
        """
        Устанавливает значение эконалога.
        :param value: Эконалог.
        :type value: float
        """
        self.presta_fields.ecotax = value
    
    @property
    def quantity(self) -> int:
        """
        Возвращает количество товара в наличии.
        :return: Количество товара.
        :rtype: int
        """
        return self.presta_fields.quantity
    
    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Устанавливает количество товара в наличии.
        :param value: Количество товара.
        :type value: int
        """
        self.presta_fields.quantity = value
    
    @property
    def minimal_quantity(self) -> int:
        """
        Возвращает минимальное количество товара для заказа.
        :return: Минимальное количество товара.
        :rtype: int
        """
        return self.presta_fields.minimal_quantity
    
    @minimal_quantity.setter
    def minimal_quantity(self, value: int) -> None:
        """
        Устанавливает минимальное количество товара для заказа.
        :param value: Минимальное количество товара.
        :type value: int
        """
        self.presta_fields.minimal_quantity = value

    @property
    def low_stock_threshold(self) -> int:
       """
       Возвращает порог низкого уровня запасов.
       :return: Порог низкого уровня запасов.
       :rtype: int
       """
       return self.presta_fields.low_stock_threshold

    @low_stock_threshold.setter
    def low_stock_threshold(self, value: int) -> None:
        """
        Устанавливает порог низкого уровня запасов.
        :param value: Порог низкого уровня запасов.
        :type value: int
        """
        self.presta_fields.low_stock_threshold = value
    
    @property
    def low_stock_alert(self) -> bool:
       """
       Возвращает признак оповещения о низком уровне запасов.
       :return: Признак оповещения о низком уровне запасов.
       :rtype: bool
       """
       return self.presta_fields.low_stock_alert
    
    @low_stock_alert.setter
    def low_stock_alert(self, value: bool) -> None:
        """
        Устанавливает признак оповещения о низком уровне запасов.
        :param value: Признак оповещения о низком уровне запасов.
        :type value: bool
        """
        self.presta_fields.low_stock_alert = value

    @property
    def price(self) -> float:
        """
        Возвращает цену товара.
        :return: Цена товара.
        :rtype: float
        """
        return self.presta_fields.price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает цену товара.
        :param value: Цена товара.
        :type value: float
        """
        self.presta_fields.price = value

    @property
    def wholesale_price(self) -> float:
       """
       Возвращает оптовую цену товара.
       :return: Оптовая цена товара.
       :rtype: float
       """
       return self.presta_fields.wholesale_price
    
    @wholesale_price.setter
    def wholesale_price(self, value: float) -> None:
        """
        Устанавливает оптовую цену товара.
        :param value: Оптовая цена товара.
        :type value: float
        """
        self.presta_fields.wholesale_price = value
    
    @property
    def unity(self) -> str:
        """
         Возвращает единицу измерения товара.
         :return: Единица измерения товара.
         :rtype: str
        """
        return self.presta_fields.unity
    
    @unity.setter
    def unity(self, value: str) -> None:
        """
        Устанавливает единицу измерения товара.
        :param value: Единица измерения товара.
        :type value: str
        """
        self.presta_fields.unity = value

    @property
    def unit_price_ratio(self) -> float:
        """
        Возвращает отношение цены за единицу измерения.
        :return: Отношение цены за единицу измерения.
        :rtype: float
        """
        return self.presta_fields.unit_price_ratio

    @unit_price_ratio.setter
    def unit_price_ratio(self, value: float) -> None:
        """
        Устанавливает отношение цены за единицу измерения.
        :param value: Отношение цены за единицу измерения.
        :type value: float
        """
        self.presta_fields.unit_price_ratio = value

    @property
    def additional_shipping_cost(self) -> float:
        """
        Возвращает стоимость дополнительной доставки.
        :return: Стоимость дополнительной доставки.
        :rtype: float
        """
        return self.presta_fields.additional_shipping_cost
    
    @additional_shipping_cost.setter
    def additional_shipping_cost(self, value: float) -> None:
        """
        Устанавливает стоимость дополнительной доставки.
        :param value: Стоимость дополнительной доставки.
        :type value: float
        """
        self.presta_fields.additional_shipping_cost = value

    @property
    def reference(self) -> str:
        """
        Возвращает артикул товара.
        :return: Артикул товара.
        :rtype: str
        """
        return self.presta_fields.reference

    @reference.setter
    def reference(self, value: str) -> None:
        """
        Устанавливает артикул товара.
        :param value: Артикул товара.
        :type value: str
        """
        self.presta_fields.reference = value
    
    @property
    def supplier_reference(self) -> str:
        """
        Возвращает артикул поставщика.
        :return: Артикул поставщика.
        :rtype: str
        """
        return self.presta_fields.supplier_reference
    
    @supplier_reference.setter
    def supplier_reference(self, value: str) -> None:
        """
        Устанавливает артикул поставщика.
        :param value: Артикул поставщика.
        :type value: str
        """
        self.presta_fields.supplier_reference = value
    
    @property
    def location(self) -> str:
        """
        Возвращает местоположение товара.
        :return: Местоположение товара.
        :rtype: str
        """
        return self.presta_fields.location
    
    @location.setter
    def location(self, value: str) -> None:
        """
        Устанавливает местоположение товара.
        :param value: Местоположение товара.
        :type value: str
        """
        self.presta_fields.location = value

    @property
    def width(self) -> float:
        """
        Возвращает ширину товара.
        :return: Ширина товара.
        :rtype: float
        """
        return self.presta_fields.width
    
    @width.setter
    def width(self, value: float) -> None:
        """
        Устанавливает ширину товара.
        :param value: Ширина товара.
        :type value: float
        """
        self.presta_fields.width = value

    @property
    def height(self) -> float:
        """
        Возвращает высоту товара.
        :return: Высота товара.
        :rtype: float
        """
        return self.presta_fields.height

    @height.setter
    def height(self, value: float) -> None:
        """
        Устанавливает высоту товара.
        :param value: Высота товара.
        :type value: float
        """
        self.presta_fields.height = value
    
    @property
    def depth(self) -> float:
        """
        Возвращает глубину товара.
        :return: Глубина товара.
        :rtype: float
        """
        return self.presta_fields.depth
    
    @depth.setter
    def depth(self, value: float) -> None:
        """
        Устанавливает глубину товара.
        :param value: Глубина товара.
        :type value: float
        """
        self.presta_fields.depth = value

    @property
    def weight(self) -> float:
        """
        Возвращает вес товара.
        :return: Вес товара.
        :rtype: float
        """
        return self.presta_fields.weight
    
    @weight.setter
    def weight(self, value: float) -> None:
        """
        Устанавливает вес товара.
        :param value: Вес товара.
        :type value: float
        """
        self.presta_fields.weight = value

    @property
    def volume(self) -> float:
        """
        Возвращает объем товара.
        :return: Объем товара.
        :rtype: float
        """
        return self.presta_fields.volume
    
    @volume.setter
    def volume(self, value: float) -> None:
        """
        Устанавливает объем товара.
        :param value: Объем товара.
        :type value: float
        """
        self.presta_fields.volume = value

    @property
    def out_of_stock(self) -> int:
        """
        Возвращает значение для товара, когда его нет в наличии.
        :return: Значение для отсутствующего товара.
        :rtype: int
        """
        return self.presta_fields.out_of_stock

    @out_of_stock.setter
    def out_of_stock(self, value: int) -> None:
        """
        Устанавливает значение для товара, когда его нет в наличии.
        :param value: Значение для отсутствующего товара.
        :type value: int
        """
        self.presta_fields.out_of_stock = value

    @property
    def additional_delivery_times(self) -> int:
        """
        Возвращает время дополнительной доставки.
        :return: Время дополнительной доставки.
        :rtype: int
        """
        return self.presta_fields.additional_delivery_times
    
    @additional_delivery_times.setter
    def additional_delivery_times(self, value: int) -> None:
        """
        Устанавливает время дополнительной доставки.
        :param value: Время дополнительной доставки.
        :type value: int
        """
        self.presta_fields.additional_delivery_times = value

    @property
    def quantity_discount(self) -> bool:
       """
       Возвращает признак наличия скидки по количеству.
       :return: Признак наличия скидки по количеству.
       :rtype: bool
       """
       return self.presta_fields.quantity_discount
    
    @quantity_discount.setter
    def quantity_discount(self, value: bool) -> None:
       """
       Устанавливает признак наличия скидки по количеству.
       :param value: Признак наличия скидки по количеству.
       :type value: bool
       """
       self.presta_fields.quantity_discount = value

    @property
    def customizable(self) -> bool:
        """
        Возвращает признак настраиваемости товара.
        :return: Признак настраиваемости.
        :rtype: bool
        """
        return self.presta_fields.customizable
    
    @customizable.setter
    def customizable(self, value: bool) -> None:
        """
        Устанавливает признак настраиваемости товара.
        :param value: Признак настраиваемости.
        :type value: bool
        """
        self.presta_fields.customizable = value

    @property
    def uploadable_files(self) -> int:
        """
        Возвращает количество загружаемых файлов.
        :return: Количество загружаемых файлов.
        :rtype: int
        """
        return self.presta_fields.uploadable_files
    
    @uploadable_files.setter
    def uploadable_files(self, value: int) -> None:
        """
        Устанавливает количество загружаемых файлов.
        :param value: Количество загружаемых файлов.
        :type value: int
        """
        self.presta_fields.uploadable_files = value

    @property
    def text_fields(self) -> int:
       """
       Возвращает количество текстовых полей.
       :return: Количество текстовых полей.
       :rtype: int
       """
       return self.presta_fields.text_fields
    
    @text_fields.setter
    def text_fields(self, value: int) -> None:
       """
       Устанавливает количество текстовых полей.
       :param value: Количество текстовых полей.
       :type value: int
       """
       self.presta_fields.text_fields = value

    @property
    def active(self) -> bool:
        """
        Возвращает признак активности товара.
        :return: Признак активности.
        :rtype: bool
        """
        return self.presta_fields.active
    
    @active.setter
    def active(self, value: bool) -> None:
        """
        Устанавливает признак активности товара.
        :param value: Признак активности.
        :type value: bool
        """
        self.presta_fields.active = value

    @property
    def redirect_type(self) -> str:
        """
        Возвращает тип редиректа.
        :return: Тип редиректа.
        :rtype: str
        """
        return self.presta_fields.redirect_type
    
    @redirect_type.setter
    def redirect_type(self, value: str) -> None:
        """
        Устанавливает тип редиректа.
        :param value: Тип редиректа.
        :type value: str
        """
        self.presta_fields.redirect_type = value
    
    @property
    def id_type_redirected(self) -> int:
        """
        Возвращает ID редиректа.
        :return: ID редиректа.
        :rtype: int
        """
        return self.presta_fields.id_type_redirected
    
    @id_type_redirected.setter
    def id_type_redirected(self, value: int) -> None:
        """
        Устанавливает ID редиректа.
        :param value: ID редиректа.
        :type value: int
        """
        self.presta_fields.id_type_redirected = value

    @property
    def available_for_order(self) -> bool:
        """
        Возвращает признак доступности для заказа.
        :return: Признак доступности для заказа.
        :rtype: bool
        """
        return self.presta_fields.available_for_order

    @available_for_order.setter
    def available_for_order(self, value: bool) -> None:
        """
        Устанавливает признак доступности для заказа.
        :param value: Признак доступности для заказа.
        :type value: bool
        """
        self.presta_fields.available_for_order = value

    @property
    def available_date(self) -> str:
       """
       Возвращает дату доступности товара.
       :return: Дата доступности товара.
       :rtype: str
       """
       return self.presta_fields.available_date
    
    @available_date.setter
    def available_date(self, value: str) -> None:
        """
        Устанавливает дату доступности товара.
        :param value: Дата доступности товара.
        :type value: str
        """
        self.presta_fields.available_date = value
    
    @property
    def show_condition(self) -> bool:
       """
       Возвращает признак отображения состояния товара.
       :return: Признак отображения состояния товара.
       :rtype: bool
       """
       return self.presta_fields.show_condition
    
    @show_condition.setter
    def show_condition(self, value: bool) -> None:
        """
        Устанавливает признак отображения состояния товара.
        :param value: Признак отображения состояния товара.
        :type value: bool
        """
        self.presta_fields.show_condition = value

    @property
    def condition(self) -> str:
        """
        Возвращает состояние товара.
        :return: Состояние товара.
        :rtype: str
        """
        return self.presta_fields.condition
    
    @condition.setter
    def condition(self, value: str) -> None:
        """
        Устанавливает состояние товара.
        :param value: Состояние товара.
        :type value: str
        """
        self.presta_fields.condition = value

    @property
    def show_price(self) -> bool:
       """
       Возвращает признак отображения цены товара.
       :return: Признак отображения цены товара.
       :rtype: bool
       """
       return self.presta_fields.show_price

    @show_price.setter
    def show_price(self, value: bool) -> None:
       """
       Устанавливает признак отображения цены товара.
       :param value: Признак отображения цены товара.
       :type value: bool
       """
       self.presta_fields.show_price = value
    
    @property
    def indexed(self) -> bool:
       """
       Возвращает признак индексации товара.
       :return: Признак индексации.
       :rtype: bool
       """
       return self.presta_fields.indexed
    
    @indexed.setter
    def indexed(self, value: bool) -> None:
       """
       Устанавливает признак индексации товара.
       :param value: Признак индексации.
       :type value: bool
       """
       self.presta_fields.indexed = value
    
    @property
    def visibility(self) -> str:
       """
       Возвращает видимость товара.
       :return: Видимость товара.
       :rtype: str