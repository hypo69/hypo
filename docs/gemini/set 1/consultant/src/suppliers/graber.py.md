# Анализ кода модуля `graber.py`

**Качество кода**
7
-  Плюсы
    - Код имеет четкую структуру, разбит на классы и функции.
    - Используется асинхронное программирование для эффективного сбора данных.
    - Присутствует базовая обработка ошибок с помощью `try-except`, а также логирование.
    - Используется декоратор `close_pop_up` для обработки всплывающих окон.
    - Присутствует документация к классам и функциям.
-  Минусы
    - Не все функции имеют docstring в формате reStructuredText (RST).
    - Имеется избыточное использование try-except, что можно заменить на `logger.error`.
    - Не везде используется `normalize_string` там где это требуется.
    - Не всегда используется `await` при вызове асинхронных функций.
    - В некоторых методах есть дублирование кода, например проверка `if not value:`
    - Не все комментарии написаны в стиле reStructuredText
    - Есть проблемы с форматированием кода, а именно отступы, пустые строки.

**Рекомендации по улучшению**
1. **Документация:**
   - Переписать все комментарии в формате reStructuredText (RST).
   - Добавить подробные docstring для всех функций, методов и классов.
   - Использовать `:param:` и `:return:` для описания параметров и возвращаемых значений.

2. **Импорты:**
    -  Удалить неиспользуемые импорты, а именно `from src.webdriver.driver import Driver`
    -  Добавить `from src.logger.logger import logger` для явного импорта логгера.

3.  **Обработка ошибок:**
    -   Избегать избыточного использования `try-except` блоков. Вместо этого использовать `logger.error` для логирования ошибок и возврата из функции.
    -   Унифицировать обработку ошибок с использованием декоратора `close_pop_up`.
    -   Проверку на валидность значения вынести в отдельную функцию.

4.  **Рефакторинг:**
   -  Устранить дублирование кода в методах, где происходит проверка на `if not value:`.
   -  Использовать `asyncio.to_thread` для функций, которые могут блокировать основной поток, как в `set_field_value`.
   -  Унифицировать логику получения данных из локатора, используя общую функцию.
   -  Сделать более гибкую передачу параметров в декораторе `close_pop_up`, например, через kwargs.
   -  Переименовать `kwards` в `kwargs` в функциях `grab_page` и `fetch_all_data`.
   -   Использовать `normalize_string` там где это требуется
   -   Использовать `await` при вызове асинхронных функций

5.  **Форматирование:**
   -   Исправить отступы и пустые строки в коде.

**Оптимизированный код**
```python
"""
Модуль для сбора данных о товарах с веб-страниц поставщиков.
=========================================================================================

Модуль содержит класс :class:`Graber`, который является базовым классом для сбора данных
с HTML-страниц поставщиков. Он использует веб-драйвер для извлечения данных с целевых полей,
таких как название, описание, спецификация, артикул и цена. Местоположение каждого поля
определяется его локатором, хранящимся в JSON-файлах в директории `locators` каждого поставщика.
([подробно о локаторах](locators.ru.md)).

Для нестандартной обработки полей товара можно переопределить функцию в своем классе.

Пример:

.. code-block:: python

    s = 'suppler_prefix'
    from src.suppliers import Graber
    locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

    class G(Graber):

        @close_pop_up()
        async def name(self, value: Optional[Any] = None):
            self.fields.name = <Ваша реализация>
"""
from __future__ import annotations

import asyncio
import datetime
import os
import sys
from functools import wraps
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Optional

from langdetect import detect

import header
from src import gs
from src.category import Category
from src.logger.exceptions import ExecuteLocatorException
from src.logger.logger import logger
from src.product.product_fields import ProductFields
from src.utils.image import save_png, save_png_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint
from src.utils.string.normalizer import (
    normalize_boolean,
    normalize_float,
    normalize_int,
    normalize_sql_date,
    normalize_string,
)

MODE = 'dev'


# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: 'Driver'
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    driver: 'Driver' = None
    locator_for_decorator: SimpleNamespace = None
    supplier_prefix: str = None


def close_pop_up(value: 'Driver' = None) -> Callable:
    """
    Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    :param value: Дополнительное значение для декоратора.
    :type value: 'Driver', optional
    :return: Декоратор, оборачивающий функцию.
    :rtype: Callable
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(
                        Context.locator_for_decorator
                    )  # Код исполняет закрытие всплывающего окна
                    ...
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            return await func(*args, **kwargs)  # Код исполняет основную функцию

        return wrapper

    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, driver: 'Driver'):
        """
        Инициализация класса Graber.

        :param supplier_prefix: Префикс поставщика.
        :type supplier_prefix: str
        :param driver: Экземпляр класса Driver.
        :type driver: 'Driver'
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(
            gs.path.src
            / 'suppliers'
            / supplier_prefix
            / 'locators'
            / 'product.json'
        )
        self.driver = driver
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix

    async def error(self, field: str):
        """
        Логирует ошибку заполнения поля.

        :param field: Название поля, где произошла ошибка.
        :type field: str
        """
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = '',
    ) -> Any:
        """
        Универсальная функция для установки значений полей с обработкой ошибок.

        :param value: Значение для установки.
        :type value: Any
        :param locator_func: Функция для получения значения из локатора.
        :type locator_func: Callable[[], Any]
        :param field_name: Название поля.
        :type field_name: str
        :param default: Значение по умолчанию.
        :type default: Any, optional
        :return: Установленное значение.
        :rtype: Any
        """
        locator_result = await asyncio.to_thread(locator_func)
        if value:
            return value
        if locator_result:
            return locator_result
        await self.error(field_name)
        return default

    async def grab_page(self, *args, **kwargs) -> ProductFields:
        """
        Асинхронная функция для сбора полей продукта.

        :param args: Кортеж с названиями полей для сбора.
        :type args: tuple
        :param kwargs: Словарь с ключами и значениями для каждого поля.
        :type kwargs: dict
        :return: Собранные поля продукта.
        :rtype: ProductFields
        """

        async def fetch_all_data(*args, **kwargs):
            # Код исполняет динамический вызов функций для каждого поля из args
            for field_name in args:
                function = getattr(
                    self, field_name, None
                )  # Получаем метод по имени
                if function:
                    await function(
                        kwargs.get(field_name, '')
                    )  # Вызов метода с аргументом из словаря kwargs

        # Код исполняет вызов функции для получения всех данных
        await fetch_all_data(*args, **kwargs)
        return self.fields

    def error(self, field: str):
        """
        Логирует ошибку для полей.
        
        :param field: Название поля, где произошла ошибка.
        :type field: str
        """
        logger.debug(f"Ошибка заполнения поля {field}")

    async def _fetch_and_set_field(
        self,
        field_name: str,
        locator_key: str,
        value: Optional[Any] = None,
        normalize_func: Optional[Callable[[Any], Any]] = None,
        default: Optional[Any] = None,
    ) -> bool:
        """
        Универсальная функция для получения и установки значения поля.

        :param field_name: Название поля.
        :type field_name: str
        :param locator_key: Ключ локатора.
        :type locator_key: str
        :param value: Значение для установки, если предоставлено.
        :type value: Optional[Any], optional
        :param normalize_func: Функция для нормализации значения.
        :type normalize_func: Optional[Callable[[Any], Any]], optional
        :param default: Значение по умолчанию.
        :type default: Optional[Any], optional
        :return: `True` если значение установлено, `False` в противном случае.
        :rtype: bool
        """
        try:
            if value:
                setattr(self.fields, field_name, value)
                return True
            locator_value = await self.driver.execute_locator(
                getattr(self.locator, locator_key)
            )
            if locator_value:
                normalized_value = (
                    normalize_func(locator_value)
                    if normalize_func
                    else locator_value
                )
                setattr(self.fields, field_name, normalized_value)
                return True
            if default is not None:
                setattr(self.fields, field_name, default)
                return True
            logger.debug(
                f"Невалидный результат {locator_value=}\\nлокатор {getattr(self.locator, locator_key)}"
            )
            return False
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `{field_name}`",
                ex,
            )
            return False
    
    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает дополнительную стоимость доставки.
        
        :param value: Значение можно передать в словаре kwargs через ключ {additional_shipping_cost = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.additional_shipping_cost`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'additional_shipping_cost',
            'additional_shipping_cost',
            value,
            normalize_string,
        )

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус наличия на складе.
        
        :param value: Значение можно передать в словаре kwargs через ключ {delivery_in_stock = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.delivery_in_stock`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'delivery_in_stock',
            'delivery_in_stock',
            value,
            normalize_string,
        )

    @close_pop_up()
    async def active(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус активности.
        
        :param value: Значение можно передать в словаре kwargs через ключ {active = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.active`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'active', 'active', value, normalize_int, 1
        )

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None):
         """
        Извлекает и устанавливает дополнительное время доставки.
        
        :param value: Значение можно передать в словаре kwargs через ключ {additional_delivery_times = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.additional_delivery_times`.
        :type value: Optional[Any], optional
         """
         return await self._fetch_and_set_field(
             'additional_delivery_times', 'additional_delivery_times', value
         )

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус расширенного управления запасами.
        
        :param value: Значение можно передать в словаре kwargs через ключ {advanced_stock_management = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.advanced_stock_management`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'advanced_stock_management', 'advanced_stock_management', value
        )

    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает короткую партнерскую ссылку.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_short_link = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_short_link`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_short_link', 'affiliate_short_link', value
        )

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает партнерское описание.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_summary = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_summary`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_summary',
            'affiliate_summary',
            value,
            normalize_string,
        )

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает второе партнерское описание.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_summary_2 = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_summary_2`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_summary_2', 'affiliate_summary_2', value
        )

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает партнерский текст.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_text = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_text`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_text', 'affiliate_text', value
        )

    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает большое партнерское изображение.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_large = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_image_large`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_image_large', 'affiliate_image_large', value
        )

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает среднее партнерское изображение.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_medium = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_image_medium`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_image_medium', 'affiliate_image_medium', value
        )

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает маленькое партнерское изображение.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_small = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.affiliate_image_small`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'affiliate_image_small', 'affiliate_image_small', value
        )

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает дату доступности.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_date = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.available_date`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'available_date', 'available_date', value
        )

    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус доступности для заказа.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.available_for_order`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'available_for_order', 'available_for_order', value
        )

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус доступности позже.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.available_later`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'available_later', 'available_later', value
        )

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус доступности сейчас.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.available_now`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'available_now', 'available_now', value
        )

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """
        Устанавливает дополнительные категории.

        :param value: Значение можно передать в словаре kwargs через ключ {additional_categories = `value`} при определении класса.
        Если `value` передано, оно подставляется в поле `ProductFields.additional_categories`.
        :type value: str | list, optional
        :return: Словарь с ID категорий.
        :rtype: dict
        """
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает кэшированный атрибут по умолчанию.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.cache_default_attribute`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'cache_default_attribute', 'cache_default_attribute', value
        )

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус наличия вложений в кэше.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.cache_has_attachments`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'cache_has_attachments', 'cache_has_attachments', value
        )

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус является ли товар набором в кэше.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_is_pack = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.cache_is_pack`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'cache_is_pack', 'cache_is_pack', value
        )

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает условие товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {condition = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.condition`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'condition', 'condition', value
        )

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус настраиваемости.
        
        :param value: Значение можно передать в словаре kwargs через ключ {customizable = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.customizable`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'customizable', 'customizable', value
        )

    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None):
        """
        Извлекает и устанавливает дату добавления.
        
        :param value: Значение можно передать в словаре kwargs через ключ {date_add = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.date_add`.
        :type value: Optional[str | datetime.date], optional
        """
        return await self._fetch_and_set_field(
            'date_add', 'date_add', value, normalize_sql_date, gs.now
        )

    @close_pop_up()
    async def date_upd(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает дату обновления.
        
        :param value: Значение можно передать в словаре kwargs через ключ {date_upd = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.date_upd`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'date_upd', 'date_upd', value, normalize_sql_date, gs.now
        )

    @close_pop_up()
    async def delivery_out_stock(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает статус доставки при отсутствии на складе.
        
        :param value: Значение можно передать в словаре kwargs через ключ {delivery_out_stock = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.delivery_out_stock`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'delivery_out_stock',
            'delivery_out_stock',
            value,
            normalize_string,
        )

    @close_pop_up()
    async def depth(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает глубину.
        
        :param value: Значение можно передать в словаре kwargs через ключ {depth = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.depth`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'depth', 'depth', value, normalize_float
        )

    @close_pop_up()
    async def description(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает описание товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {description = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.description`.
        :type value: Optional[Any], optional
        """
        if value:
            self.fields.description = value
            return True
        try:
            raw_value = await self.driver.execute_locator(self.locator.description)
            self.fields.description = normalize_string(raw_value)
            return True
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `description` \\n {pprint(raw_value)}",
                ex,
            )
            return False

    @close_pop_up()
    async def description_short(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает краткое описание товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {description_short = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.description_short`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'description_short',
            'description_short',
            value,
            normalize_string
        )

    @close_pop_up()
    async def id_category_default(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает ID категории по умолчанию.
        
        :param value: Значение можно передать в словаре kwargs через ключ {id_category_default = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.id_category_default`.
        :type value: Optional[Any], optional
        """
        self.fields.id_category_default = value
        return True

    @close_pop_up()
    async def id_default_combination(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает ID комбинации по умолчанию.
        
        :param value: Значение можно передать в словаре kwargs через ключ {id_default_combination = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.id_default_combination`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'id_default_combination', 'id_default_combination', value
        )

    @close_pop_up()
    async def id_product(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает ID продукта.
        
        :param value: Значение можно передать в словаре kwargs через ключ {id_product = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.id_product`.
        :type value: Optional[Any], optional
        """
        try:
            # Код исполняет получение значения id_supplier
            self.fields.id_supplier = normalize_string(
                self.fields.id_supplier
                or await self.driver.execute_locator(self.locator.id_supplier)
            )
            # Код исполняет формирование id_product
            self.fields.id_product = value or f"{self.supplier_prefix}{f'-{self.fields.id_supplier}' if self.fields.id_supplier else ''}"
            if self.fields.id_product:
                return True
            return False
        except Exception as ex:
            logger.error(f"Ошибка значения поля `id_product`", ex)
            return False

    @close_pop_up()
    async def locale(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает локаль.
        
        :param value: Значение можно передать в словаре kwargs через ключ {locale = `value`} при определении класса.
                      Если `value` не передан, оно определяется автоматически.
        :type value: Optional[Any], optional
        """
        i18n = value or d.locale
        if not i18n and self.fields.name['language'][0]['value']:
            text = self.fields.name['language'][0]['value']
            i18n = detect(text)
        self.fields.locale = i18n

    @close_pop_up()
    async def id_default_image(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает ID изображения по умолчанию.
        
        :param value: Значение можно передать в словаре kwargs через ключ {id_default_image = `value`} при определении класса.
                      Если `value` передан, его значение подставляется в поле `ProductFields.id_default_image`.
        :type value: Optional[Any], optional
        """
        return await self._fetch_and_set_field(
            'id_default_image', 'id_default_image', value
        )

    @close_pop_up()
    async def ean13(self, value: Optional[Any] = None):
        """
        Извлекает и устанавливает код EAN13.
        
        :param value: Значение можно передать в словаре kwargs через ключ {ean13 = `value`} при определении класса.
                      Если `value` передан, его значение под