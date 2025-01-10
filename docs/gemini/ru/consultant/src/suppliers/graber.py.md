# Анализ кода модуля `graber.py`

**Качество кода**

-   **Соответствие требованиям по оформлению кода: 7/10**
    -   **Плюсы:**
        -   Код в основном соответствует стандарту PEP8.
        -   Используются асинхронные функции там, где это необходимо.
        -   Присутствует базовая обработка ошибок с помощью `try-except`.
        -   Используется `logger` для логирования.
        -   Присутствует описание модуля в формате RST.
        -   Используются `j_loads_ns` и `j_dumps`.
    -   **Минусы:**
        -   Много избыточных блоков `try-except` с `...` и `return`, что снижает читаемость.
        -   Используются двойные кавычки в docstring.
        -   Не все функции и методы документированы в формате RST.
        -   Не везде используется `logger.error` вместо `logger.debug` для ошибок.
        -   В некоторых местах есть `...` как точки остановки, хотя они должны быть убраны.
        -   Встречаются `value or await self.driver.execute_locator(...) or ''`, что можно упростить.
        -   Не все импорты соответствуют ранее обработанным файлам.
        -   Встречаются неинформативные комментарии вида `# Получаем значение через execute_locator`.
        -   Используется `from src import gs` что может привести к проблемам при рефакторинге.

**Рекомендации по улучшению**

1.  **Форматирование кода:**
    -   Заменить двойные кавычки на одинарные в коде, где это необходимо, кроме операций вывода.
    -   Удалить избыточные блоки `try-except` с `...` и `return`, использовать `logger.error` для логирования ошибок и возвращать `None` или `False` при ошибке.
    -   Документировать все функции, методы и переменные в формате RST.
    -   Использовать `from src.logger.logger import logger` для импорта логгера.
    -   Использовать константу `''` вместо `'\'\'`
2.  **Обработка данных:**
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` (уже выполнено).
    -   Заменить `...` на конкретные действия (например, `return None`).
3.  **Структура кода:**
    -   Проверить и добавить отсутствующие импорты.
    -   Привести имена функций и переменных в соответствие с ранее обработанными файлами.
4.  **Рефакторинг:**
    -   Упростить конструкции `value or await self.driver.execute_locator(...) or ''` (например, создать вспомогательную функцию).
    -   Удалить `# Получаем значение через execute_locator` - эти комментарии не информативны.
    -   Использовать `asyncio.to_thread` только в том случае, если это необходимо (например, для CPU-bound задач).
    -  Избегать использования `from src import gs`  и использовать `from src.config import gs`
5.  **Документация:**
    -   Добавить документацию в стиле RST ко всем функциям и методам, включая аргументы, возвращаемые значения и исключения.
    -   Использовать docstring для описания классов.

**Оптимизированный код**

```python
from __future__ import annotations

# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
.. module:: src.suppliers
    :platform: Windows, Unix
    :synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`,`описание`,`спецификация`,`артикул`,`цена`,...) собирает вебдрйвер (class: [`Driver`](../webdriver))
    Местополжение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))

Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = 'suppler_prefix'
from src.suppliers import Graber
locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

class G(Graber):

    @close_pop_up()
    async def name(self, value: Optional[Any] = None):
        self.fields.name = <Ваша реализация>
        )
    ```
              Таблица поставщиков:
              https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""

import datetime
import asyncio
from pathlib import Path
from typing import Optional, Any, Callable
from types import SimpleNamespace
from functools import wraps
from langdetect import detect

from src.config import gs
from src.endpoints.prestashop.product_fields import ProductFields
# from src.webdriver.driver import Driver # не требуется импортировать здесь
from src.utils.jjson import j_loads_ns
from src.utils.image import save_image_from_url, save_image
from src.utils.string.normalizer import (
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_boolean,
    normalize_sql_date,
    normalize_sku,
)
from src.logger.exceptions import ExecuteLocatorException
from src.utils.printer import pprint
from src.logger.logger import logger


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

    Args:
        value ('Driver'): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(Context.locator_for_decorator)
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
                    
            return await func(*args, **kwargs)
        return wrapper
    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, driver: 'Driver'):
        """
        Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            driver ('Driver'): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.driver = driver
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix

    async def error(self, field: str):
        """
        Обработчик ошибок для полей.
        
        Args:
            field (str): Название поля.
        """
        logger.debug(f'Ошибка заполнения поля {field}')

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = '',
    ) -> Any:
        """
        Универсальная функция для установки значений полей с обработкой ошибок.

        Args:
            value (Any): Значение для установки.
            locator_func (Callable[[], Any]): Функция для получения значения из локатора.
            field_name (str): Название поля.
            default (Any): Значение по умолчанию.

        Returns:
            Any: Установленное значение.
        """
        locator_result = await asyncio.to_thread(locator_func)
        if value:
            return value
        if locator_result:
            return locator_result
        await self.error(field_name)
        return default

    async def grab_page(self, *args, **kwards) -> ProductFields:
        """
        Асинхронная функция для сбора полей продукта.

        Args:
            args (tuple): Кортеж с названиями полей для сбора.
            kwards (dict): Словарь с ключами и значениями для каждого поля.

        Returns:
            ProductFields: Собранные поля продукта.
        """
        async def fetch_all_data(*args, **kwards):
            for filed_name in args:
                function = getattr(self, filed_name, None)
                if function:
                    await function(kwards.get(filed_name, ''))

        await fetch_all_data(*args, **kwards)
        return self.fields
    
    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set additional shipping cost.

        Args:
            value (Any): Это значение можно передать в словаре kwards через ключ {additional_shipping_cost = `value`} при определении класса
            Если `value` был передан - его значение подставляется в поле `ProductFields.additional_shipping_cost`
        
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.additional_shipping_cost = normalize_string(
                value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_shipping_cost`', ex)
            return None

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set delivery in stock status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {delivery_in_stock = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.delivery_in_stock`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.delivery_in_stock = normalize_string(
                value or await self.driver.execute_locator(self.locator.delivery_in_stock) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `delivery_in_stock`', ex)
            return None

    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set active status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {active = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.active`.
            Принимаемое значение 1/0.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = normalize_int(value or await self.driver.execute_locator(self.locator.active) or 1)
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `active`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.active}')
            return None

        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set additional delivery times.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {additional_delivery_times = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.additional_delivery_times`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.additional_delivery_times) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_delivery_times`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.additional_delivery_times}')
            return None

        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set advanced stock management status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {advanced_stock_management = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.advanced_stock_management`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.advanced_stock_management) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `advanced_stock_management`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.advanced_stock_management}')
            return None

        self.fields.advanced_stock_management = value
        return True
    
    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate short link.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_short_link = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_short_link`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.affiliate_short_link = value or await self.driver.execute_locator(
                self.locator.affiliate_short_link
            ) or ''
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_short_link`', ex)
            return None

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate summary.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_summary = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.affiliate_summary = normalize_string(
                value or await self.driver.execute_locator(self.locator.affiliate_summary) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary`', ex)
            return None

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate summary 2.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_summary_2 = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary_2`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.affiliate_summary_2) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary_2`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.affiliate_summary_2}')
            return None

        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate text.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_text = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_text`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_text`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.affiliate_text}')
            return None

        self.fields.affiliate_text = value
        return True
    
    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate large image.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_image_large = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_large`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.affiliate_image_large = value or await self.driver.execute_locator(
                self.locator.affiliate_image_large
            ) or ''
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_large`', ex)
            return None

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate medium image.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_image_medium = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_medium`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_medium) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_medium`', ex)
            return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set affiliate small image.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {affiliate_image_small = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_small`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_small) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_small`', ex)
            return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set available date.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {available_date = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_date`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.available_date) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_date`', ex)
            return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.available_date = locator_result
        return True
    
    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set available for order status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_for_order`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_for_order) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_for_order`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.available_for_order}')
            return None

        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set available later status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_later`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_later`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.available_later}')
            return None

        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set available now status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_now`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_now`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.available_now}')
            return None

        self.fields.available_now = value
        return True
    
    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """
        Set additional categories.

        Это значение можно передать в словаре kwargs через ключ {additional_categories = `value`} при определении класса.
        Если `value` было передано, оно подставляется в поле `ProductFields.additional_categories`.

        Args:
            value (str | list, optional): Строка или список категорий. Если не передано, используется пустое значение.

        Returns:
            dict: Словарь с ID категорий.
        """
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set cache default attribute.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_default_attribute`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_default_attribute) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_default_attribute`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.cache_default_attribute}')
            return None

        self.fields.cache_default_attribute = value
        return True
    
    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set cache has attachments status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_has_attachments`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_has_attachments) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_has_attachments`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.cache_has_attachments}')
            return None

        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set cache is pack status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {cache_is_pack = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_is_pack`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_is_pack) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_is_pack`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.cache_is_pack}')
            return None

        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set product condition.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {condition = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.condition`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.condition) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `condition`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.condition}')
            return None

        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set customizable status.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {customizable = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.customizable`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.customizable) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `customizable`', ex)
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.customizable}')
            return None

        self.fields.customizable = value
        return True
    
    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool|None:
        """
        Fetch and set date added.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {date_add = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.date_add`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.date_add = normalize_sql_date(
                value or await self.driver.execute_locator(self.locator.date_add) or gs.now
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `date_add`', ex)
            return None
    
    @close_pop_up()
    async def date_upd(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set date updated.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {date_upd = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.date_upd`.
        Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.date_upd = normalize_sql_date(
                value or await self.driver.execute_locator(self.locator.date_upd) or gs.now
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `date_upd`', ex)
            return None

    @close_pop_up()
    async def delivery_out_stock(self, value: Optional[Any] = None) -> bool|None:
        """
        Fetch and set delivery out of stock.

        Args:
            value (Any): Это значение можно передать в словаре kwargs через ключ {delivery_out_stock = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.delivery_out_stock`.
         Returns:
            bool: True если значение установлено
            None: если произошла ошибка
        """
        try:
            self.fields.delivery_out_stock = normalize_string(
                value or await self.driver.execute_locator(self.locator.delivery_out_stock) or ''
            )
            return True
        except Exception as