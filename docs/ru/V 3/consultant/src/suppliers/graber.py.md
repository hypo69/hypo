## Анализ кода модуля `graber.py`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Использование асинхронности для неблокирующих операций.
  - Наличие базовой структуры для сбора данных с веб-страниц.
  - Использование декоратора `close_pop_up` для обработки всплывающих окон.
- **Минусы**:
  - Много повторяющегося кода, особенно в методах для извлечения и установки значений полей.
  - Отсутствие документации для некоторых функций и классов.
  - Непоследовательное использование `j_loads` и `j_loads_ns`.
  - Большое количество `...` как заглушек.
  - Смешанный стиль комментариев.

**Рекомендации по улучшению:**

1.  **Улучшение структуры и обработки ошибок**:
    *   Необходимо добавить больше обработки исключений и логирования, чтобы упростить отладку и поддержку.
    *   Использовать `j_loads` или `j_loads_ns` для загрузки JSON-файлов конфигурации.
    *   Удалить или заменить все `...` на конкретную реализацию или `pass`.

2.  **Рефакторинг повторяющегося кода**:
    *   Создать универсальные функции для извлечения и нормализации данных, чтобы избежать дублирования кода.
    *   Использовать параметризацию для упрощения обработки различных полей.

3.  **Документация**:
    *   Добавить подробные комментарии и документацию для всех функций, методов и классов.
    *   Описать назначение каждого атрибута класса.

4.  **Улучшение декоратора `close_pop_up`**:
    *   Рассмотреть возможность сделать декоратор более гибким, чтобы он мог принимать параметры для различных сценариев закрытия всплывающих окон.

5.  **Стандартизация**:
    *   Привести код в соответствие со стандартами PEP8.
    *   Использовать консистентный стиль кавычек (одинарные).
    *   Удалить неиспользуемые импорты.

6.  **Типизация**:
    *   Необходимо проверить и добавить аннотации типов для всех переменных и возвращаемых значений, где это отсутствует.

**Оптимизированный код:**

```python
## \file /src/suppliers/graber.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль содержит базовый класс для сбора данных со страниц HTML поставщиков.
=========================================================================

Класс :class:`Graber` предназначен для извлечения данных о товарах с использованием веб-драйвера.
Он использует локаторы, хранящиеся в JSON-файлах, для определения местоположения полей на странице.

Подробности о локаторах можно найти в [locators.ru.md](locators.ru.md).

Пример использования:
----------------------

>>> s = 'supplier_prefix'
>>> from src.suppliers import Graber
>>> locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

>>> class G(Graber):
...     @close_pop_up()
...     async def name(self, value: Optional[Any] = None):
...         self.fields.name = <Ваша реализация>

Таблица поставщиков:
https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""

import asyncio
import datetime
import os
import sys
from functools import wraps
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Generator, Optional

from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.logger.exceptions import ExecuteLocatorException
from src.logger.logger import logger
from src.utils.image import save_image, save_image_async, save_image_from_url_async
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint as print
from src.utils.string.normalizer import (
    normalize_boolean,
    normalize_float,
    normalize_int,
    normalize_sku,
    normalize_sql_date,
    normalize_string,
)

# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек, используемых в процессе сбора данных.

    :ivar driver: Объект драйвера для управления браузером.
    :vartype driver: 'Driver'
    :ivar locator_for_decorator: Локатор для декоратора `@close_pop_up`.
    :vartype locator_for_decorator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    driver: 'Driver' = None
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


def close_pop_up() -> Callable:
    """
    Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Декоратор использует `Context.locator_for_decorator` для определения локатора, который нужно выполнить для закрытия окна.

    Returns:
        Callable: Декоратор, который оборачивает функцию.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    # Выполняем локатор для закрытия всплывающего окна
                    await Context.driver.execute_locator(Context.locator_for_decorator)
                except ExecuteLocatorException as ex:
                    # Логируем ошибку выполнения локатора в режиме отладки
                    logger.debug(f'Ошибка выполнения локатора: {ex}', exc_info=True)
                finally:
                    # Сбрасываем локатор после выполнения
                    Context.locator_for_decorator = None

            # Вызываем основную функцию
            return await func(*args, **kwargs)

        return wrapper

    return decorator


class Graber:
    """Базовый класс для сбора данных со страницы товара."""

    def __init__(self, supplier_prefix: str, lang_index: int, driver: 'Driver'):
        """
        Инициализирует новый экземпляр класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика, используемый для загрузки локаторов.
            lang_index (int): Индекс языка для установки базового языка.
            driver ('Driver'): Экземпляр веб-драйвера для взаимодействия с веб-страницей.
        """
        self.supplier_prefix = supplier_prefix
        # Загружаем локаторы из JSON-файла
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.driver = driver
        self.fields: ProductFields = ProductFields(lang_index)  # <- установка базового языка. Тип - `int`
        Context.driver = self.driver
        Context.supplier_prefix = None
        """Если установлен Context.locator_for_decorator - выполнится декоратор `@close_pop_up`"""
        Context.locator_for_decorator = None

    async def error(self, field: str):
        """
        Обрабатывает ошибку, возникшую при сборе данных для определенного поля.

        Args:
            field (str): Название поля, для которого произошла ошибка.
        """
        logger.debug(f'Ошибка заполнения поля {field}')

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """
        Универсальная функция для установки значений полей с обработкой ошибок.

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

    def grab_page(self, *args, **kwards) -> ProductFields:
        """
        Выполняет асинхронный сбор данных о продукте и возвращает объект ProductFields.

        Args:
            *args: Имена полей, которые нужно собрать.
            **kwards: Дополнительные аргументы для передачи в функции сбора полей.

        Returns:
            ProductFields: Объект, содержащий собранные данные о продукте.
        """
        return asyncio.run(self.grab_page_async(*args, **kwards))

    async def grab_page_async(self, *args, **kwards) -> ProductFields:
        """
        Асинхронная функция для сбора полей продукта.

        Args:
            *args: Список имен полей, которые необходимо извлечь.
            **kwards: Словарь с дополнительными параметрами для каждой функции извлечения.

        Returns:
            ProductFields: Объект ProductFields с заполненными данными.
        """
        async def fetch_all_data(*args, **kwards):
            # Динамическое вызовы функций для каждого поля из args
            for filed_name in args:
                function = getattr(self, filed_name, None)
                if function:
                    await function(kwards.get(filed_name, ''))  # Просто вызываем с await, так как все функции асинхронные

        await fetch_all_data(*args, **kwards)
        return self.fields

    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает дополнительную стоимость доставки.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.additional_shipping_cost = normalize_string(value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or '')
            if not self.fields.additional_shipping_cost:
                logger.error('Поле `additional_shipping_cost` не получило значения')
                return None

            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `additional_shipping_cost`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус доставки в наличии.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.delivery_in_stock = normalize_string(value or await self.driver.execute_locator(self.locator.delivery_in_stock) or '')
            if not self.fields.delivery_in_stock:
                logger.error('Поле `delivery_in_stock` не получило значения')
                return None
            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `delivery_in_stock`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус активности.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.active = normalize_int(value or await self.driver.execute_locator(self.locator.active) or 1)
            if not self.fields.active:
                return None
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `active`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.active}')
            return None

        # Записываем результат в поле `active` объекта `ProductFields`
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает дополнительное время доставки.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.additional_delivery_times) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `additional_delivery_times`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.additional_delivery_times}')
            return None

        # Записываем результат в поле `additional_delivery_times` объекта `ProductFields`
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус расширенного управления запасами.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.advanced_stock_management) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `advanced_stock_management`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.advanced_stock_management}')
            return None

        # Записываем результат в поле `advanced_stock_management` объекта `ProductFields`
        self.fields.advanced_stock_management = value
        return True

    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает короткую ссылку для филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_short_link = value or await self.driver.execute_locator(self.locator.affiliate_short_link) or ''
            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_short_link`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает краткое описание филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_summary = normalize_string(value or await self.driver.execute_locator(self.locator.affiliate_summary) or '')
            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_summary`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает второе краткое описание филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_summary_2) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_summary_2`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_summary_2}')
            return None

        # Записываем результат в поле `affiliate_summary_2` объекта `ProductFields`
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает текст филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_text`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_text}')
            return None

        # Записываем результат в поле `affiliate_text` объекта `ProductFields`
        self.fields.affiliate_text = value
        return True

    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает большое изображение филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_image_large = value or await self.driver.execute_locator(self.locator.affiliate_image_large) or ''
            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_image_large`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает среднее изображение филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_medium) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_image_medium`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        # Записываем результат в поле `affiliate_image_medium` объекта `ProductFields`
        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает маленькое изображение филиала.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_small) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `affiliate_image_small`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        # Записываем результат в поле `affiliate_image_small` объекта `ProductFields`
        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает доступную дату.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.available_date) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `available_date`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        # Записываем результат в поле `available_date` объекта `ProductFields`
        self.fields.available_date = locator_result
        return True

    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "доступно для заказа".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_for_order) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `available_for_order`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_for_order}')
            return None

        # Записываем результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "доступно позже".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `available_later`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_later}')
            return None

        # Записываем результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "доступно сейчас".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `available_now`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_now}')
            return None

        # Записываем результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """
        Устанавливает дополнительные категории.

        Args:
            value (str | list, optional): Строка или список категорий. Если не передано, используется пустое значение. Defaults to None.

        Returns:
            dict: Словарь с ID категорий.
        """
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает кэшированный атрибут по умолчанию.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_default_attribute) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `cache_default_attribute`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_default_attribute}')
            return None

        # Записываем результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value
        return True

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "кэш содержит вложения".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_has_attachments) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `cache_has_attachments`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_has_attachments}')
            return None

        # Записываем результат в поле `cache_has_attachments` объекта `ProductFields`
        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "является комплектом".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_is_pack) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `cache_is_pack`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_is_pack}')
            return None

        # Записываем результат в поле `cache_is_pack` объекта `ProductFields`
        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает состояние товара.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.condition) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `condition`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.condition}')
            return None

        # Записываем результат в поле `condition` объекта `ProductFields`
        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус "настраиваемый".

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.customizable) or ''
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `customizable`', ex, exc_info=True)
            return None

        # Проверка валидности `value`
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.customizable}')
            return None

        # Записываем результат в поле `customizable` объекта `ProductFields`
        self.fields.customizable = value
        return True

    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool | None:
        """
        Извлекает и устанавливает дату добавления.

        Args:
            value (Optional[str  |  datetime.date], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.date_add = normalize_sql_date(value or await self.driver.execute_locator(self.locator.date_add) or gs.now)
            return True
        except Exception as ex:
            logger.error('Ошибка получения значения в поле `date_add`', ex, exc_info=True)
            return None

    @close_pop_up()
    async def date_upd(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает дату обновления.

        Args:
            value (Optional[Any], optional): Значение, которое можно передать через kwargs. Defaults to None.

        Returns:
            bool | None: True в случае успеха, None в случае ошибки.
        """
        try:
            # Получаем значение через execute_locator