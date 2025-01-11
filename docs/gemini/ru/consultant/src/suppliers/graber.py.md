# Анализ кода модуля graber.py

**Качество кода: 7/10**

- **Плюсы**
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются асинхронные функции, что хорошо для IO-bound операций.
    - Присутствует базовая обработка ошибок с использованием `try-except` и логированием.
    - Используется декоратор `close_pop_up` для обработки всплывающих окон.
    - Присутствует документация в формате RST для модуля и основных классов.
    - Код использует `j_loads_ns` для загрузки JSON файлов.
    - Используется `normalize_string`, `normalize_int`, `normalize_float`, `normalize_boolean`, `normalize_sql_date`, `normalize_sku` для нормализации данных.

- **Минусы**
    -   Избыточное использование `try-except` блоков в каждой функции.
    -   Много дублирования кода в функциях для получения значений.
    -   Не все функции имеют подробное описание в формате RST.
    -   Не все функции возвращают `True` при успешном выполнении.
    -   Использование `...` в качестве "точки остановки" не является лучшей практикой.
    -   Отсутствует обработка ошибок при сохранении изображений.
    -   Не все логи записываются с уровнем `logger.error`, что может затруднить отладку.
    -   Не везде используется форматирование строк f-string.
    -   Некоторые комментарии не совсем информативные.
    -   Не везде есть проверки на `None` перед выполнением операций.
    -   Импорт `header` не используется.
    -   Не везде используется `asyncio.to_thread` при вызове синхронных функций.
    -   Не используется `from src.logger.logger import logger`.
    -  Не везде где требуется используются одинарные ковычки в коде.

**Рекомендации по улучшению**
1. **Улучшить обработку ошибок**:
    -   Использовать `logger.error` для записи ошибок и возвращать `False` при ошибке.
    -   Удалить избыточные `try-except` блоки, где это возможно.
2.  **Унифицировать функции**:
    -   Реализовать единую функцию для получения значений через `execute_locator` с обработкой ошибок, чтобы избежать дублирования кода.
3.  **Документирование**:
    -   Добавить подробную документацию в формате RST для всех функций и методов.
    -   Использовать docstring для переменных классов.
4.  **Улучшить читаемость**:
    -   Использовать f-строки для форматирования логов.
    -   Избавиться от `...` и использовать `pass` или `continue` в зависимости от логики.
5.  **Стандартизация кода**:
    -  Использовать везде одинарные ковычки `'строка'`.
    -  Все импорты должны соответствовать стандартам проекта.
    -  Все функции которые исполняют `self.fields.<field_name> = <value>`  должны возвращать `True` в случае успеха.
6.  **Улучшить сохранение изображений**:
    -   Добавить проверку на наличие директории `tmp` и ее создание, если ее нет.
7. **Улучшить именование**:
    - Переименовать `filed_name` в `field_name`.
    - Переименовать `kwards` в `kwargs`.
    - Переименовать `byer_protection` в `buyer_protection`.
    - Переименовать `img_tmp_path` в `image_tmp_path`.
8.  **Оптимизация**:
    - Использовать `asyncio.to_thread` при вызове синхронных функций (например, `normalize_string`).
    - Убрать импорт `header`.
9.  **Безопасность**
    - Проверять  `raw_image` на `None` или пустую строку перед использованием.
    -   Добавить обработку ошибок при сохранении изображения.
10. **Сообщения об ошибках**:
    -  Улучшить сообщения об ошибках, добавив больше контекста.

**Оптимизированный код**
```python
from __future__ import annotations

# \\file /src/suppliers/graber.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.suppliers
    :platform: Windows, Unix
    :synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`, `описание`, `спецификация`, `артикул`, `цена`, ...) собирает веб-драйвер (class: [`Driver`](../webdriver))
    Местоположение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))

## Для нестандартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = 'suppler_prefix'
from src.suppliers import Graber
locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

class G(Graber):

    @close_pop_up()
    async def name(self, value:Optional[Any] = None):
        self.fields.name = <Ваша реализация>
        )
    ```
              Таблица поставщиков:
              https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""

import datetime
import os
import sys
import asyncio
from pathlib import Path
from typing import Optional, Any
from types import SimpleNamespace
from typing import Callable
from langdetect import detect
from functools import wraps

# import header # не используется
from src import gs

from src.endpoints.prestashop.product_fields import ProductFields
from src.category import Category
# from src.webdriver.driver import Driver  # не требуется импортировать здесь
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_image_from_url, save_image
from src.utils.string.normalizer import( normalize_string,
                                        normalize_int,
                                        normalize_float,
                                        normalize_boolean,
                                        normalize_sql_date,
                                        normalize_sku )
from src.logger.exceptions import ExecuteLocatorException
#from src.endpoints.prestashop import PrestaShop
from src.utils.printer import pprint
from src.logger.logger import logger


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

    # Атрибуты класса
    driver: 'Driver' = None
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


# Определение декоратора для закрытия всплывающих окон
# В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# Общее название декоратора `@close_pop_up` можно изменить
# Если декоратор не используется в поставщике - поставь
def close_pop_up(value: 'Driver' = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

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
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close
                    ...
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, driver: 'Driver'):
        """Инициализация класса Graber.

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
        """Обработчик ошибок для полей."""
        logger.debug(f'Ошибка заполнения поля {field}')

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.

        Args:
            value (Any): Значение для установки.
            locator_func (Callable[[], Any]): Функция для получения значения из локатора.
            field_name (str): Название поля.
            default (Any): Значение по умолчанию. По умолчанию пустая строка.

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


    async def grab_page(self, *args, **kwargs) -> ProductFields:
        """Асинхронная функция для сбора полей продукта.

        Args:
            args (tuple): Кортеж с названиями полей для сбора.
            kwargs (dict): Словарь с ключами и значениями для каждого поля.

        Returns:
            ProductFields: Собранные поля продукта.
        """
        async def fetch_all_data(*args, **kwargs):
            # Динамические вызовы функций для каждого поля из args
            for field_name in args:
                function = getattr(self, field_name, None)  # Получаем метод по имени
                if function:
                    await function(kwargs.get(field_name, ''))

        # Вызов функции для получения всех данных
        await fetch_all_data(*args, **kwargs)
        return self.fields

    def error(self, field: str):
        """Error handler for fields."""
        logger.debug(f'Ошибка заполнения поля {field}')


    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool:
        """Fetch and set additional shipping cost.
        Args:
            value (Any): это значение можно передать в словаре kwargs чеез ключ {additional_shipping_cost = `value`} при определении класса
            если `value` был передан - его значение подставляется в поле `ProductFields.additional_shipping_cost`
        """
        try:
            # Получаем значение через execute_locator
            self.fields.additional_shipping_cost = normalize_string(value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or '')
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_shipping_cost`', ex)
            return False


    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool:
        """Fetch and set delivery in stock status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {delivery_in_stock = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.delivery_in_stock`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.delivery_in_stock = normalize_string(value or await self.driver.execute_locator(self.locator.delivery_in_stock) or '')
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `delivery_in_stock`', ex)
            return False


    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool:
        """Fetch and set active status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {active = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.active`.
            Принимаемое значение 1/0
        """
        try:
            # Получаем значение через execute_locator
            value = normalize_int(value or await self.driver.execute_locator(self.locator.active) or 1)
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `active`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.active}')
            return False

        # Записываем результат в поле `active` объекта `ProductFields`
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool:
        """Fetch and set additional delivery times.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {additional_delivery_times = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.additional_delivery_times`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.additional_delivery_times) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_delivery_times`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.additional_delivery_times}')
            return False

        # Записываем результат в поле `additional_delivery_times` объекта `ProductFields`
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool:
        """Fetch and set advanced stock management status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {advanced_stock_management = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.advanced_stock_management`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.advanced_stock_management) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `advanced_stock_management`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.advanced_stock_management}')
            return False

        # Записываем результат в поле `advanced_stock_management` объекта `ProductFields`
        self.fields.advanced_stock_management = value
        return True

    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate short link.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_short_link = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_short_link`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_short_link = value or await self.driver.execute_locator(self.locator.affiliate_short_link) or ''
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_short_link`', ex)
            return False

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate summary.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_summary = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_summary = normalize_string(value or await self.driver.execute_locator(self.locator.affiliate_summary) or '')
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary`', ex)
            return False


    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate summary 2.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_summary_2 = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary_2`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_summary_2) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary_2`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_summary_2}')
            return False

        # Записываем результат в поле `affiliate_summary_2` объекта `ProductFields`
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate text.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_text = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_text`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_text`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_text}')
            return False

        # Записываем результат в поле `affiliate_text` объекта `ProductFields`
        self.fields.affiliate_text = value
        return True

    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate large image.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_large = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_large`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_image_large = value or await self.driver.execute_locator(self.locator.affiliate_image_large) or ''
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_large`', ex)
            return False

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate medium image.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_medium = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_medium`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_medium) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_medium`', ex)
            return False

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return False

        # Записываем результат в поле `affiliate_image_medium` объекта `ProductFields`
        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool:
        """Fetch and set affiliate small image.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_small = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_small`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_small) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_small`', ex)
            return False

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return False

        # Записываем результат в поле `affiliate_image_small` объекта `ProductFields`
        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool:
        """Fetch and set available date.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {available_date = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_date`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.available_date) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_date`', ex)
            return False

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return False

        # Записываем результат в поле `available_date` объекта `ProductFields`
        self.fields.available_date = locator_result
        return True

    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool:
        """Fetch and set available for order status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_for_order`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_for_order) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_for_order`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_for_order}')
            return False

        # Записываем результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool:
        """Fetch and set available later status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_later`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_later`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_later}')
            return False

        # Записываем результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool:
        """Fetch and set available now status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.available_now`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_now`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_now}')
            return False

        # Записываем результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """Set additional categories.

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
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool:
        """Fetch and set cache default attribute.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_default_attribute`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_default_attribute) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_default_attribute`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_default_attribute}')
            return False

        # Записываем результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value
        return True

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool:
        """Fetch and set cache has attachments status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_has_attachments`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_has_attachments) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_has_attachments`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_has_attachments}')
            return False

        # Записываем результат в поле `cache_has_attachments` объекта `ProductFields`
        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool:
        """Fetch and set cache is pack status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {cache_is_pack = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.cache_is_pack`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_is_pack) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_is_pack`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_is_pack}')
            return False

        # Записываем результат в поле `cache_is_pack` объекта `ProductFields`
        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool:
        """Fetch and set product condition.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {condition = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.condition`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.condition) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `condition`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.condition}')
            return False

        # Записываем результат в поле `condition` объекта `ProductFields`
        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool:
        """Fetch and set customizable status.

        Args:
            value (Any): это значение можно передать в словаре kwargs через ключ {customizable = `value`} при определении класса.
            Если `value` был передан, его значение подставляется в поле `ProductFields.customizable`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.customizable) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `customizable`', ex)
            return False

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.customizable}')
            return False

        # Записываем результат в поле `customizable` объекта `ProductFields`
        self.fields.customizable = value
        return True

    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool:
        """Fetch and set date added