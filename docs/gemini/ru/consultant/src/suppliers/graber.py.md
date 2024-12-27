# Анализ кода модуля `graber.py`

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 7/10
    *   **Плюсы**:
        *   Используется reStructuredText для docstring и комментариев, в основном правильно.
        *   Логирование ошибок выполняется через `logger.error`.
        *   Используются `j_loads` и `j_loads_ns` для загрузки JSON.
        *   Присутствует декоратор `@close_pop_up`.
    *   **Минусы**:
        *   Много избыточных try-except блоков с `...` и `return`, которые можно заменить на логирование и проброс ошибок.
        *   Не везде используются f-строки для форматирования логов.
        *   Некоторые docstring не полностью соответствуют стандарту reStructuredText.
        *   В некоторых функциях присутсвует `return True` хотя они могут ничего не возвращать.
        *   Используются неинформативные сообщения в логах `Ошибка получения значения в поле ...`
        *   Имена переменных `kwards` и `filed_name`
        *   Не переименован `filed_name` -> `field_name`
        *   Использованно `pprint` для отладки
        *   Много дублирующего кода
        *   Не везде добавлены комментарии в стиле RST

**Рекомендации по улучшению**
1.  **Удалить избыточные `try-except` блоки**: Переписать большинство блоков try-except для логирования ошибок и дальнейшего проброса исключений, где это уместно.
2.  **Унифицировать логирование**: Использовать f-строки для форматирования логов и более информативные сообщения об ошибках.
3.  **Улучшить документацию**: Привести все docstring в соответствие со стандартом reStructuredText.
4.  **Упростить функции**: Упростить функции, которые могут ничего не возвращать, но возвращают `True`.
5.  **Переименовать переменные**: Переименовать `kwards` в `kwargs` и `filed_name` в `field_name` для соответствия PEP8
6.  **Убрать `pprint`** Удалить `pprint` из финального варианта кода
7.  **Унифицировать доступ к `value`** Сделать проверку `if value:` и присваивание значения `self.fields.name = value`  в отдельную функцию, что бы сократить дублирование кода
8.  **Добавить RST docstring** добавить docstring в RST стиле для функций
9.  **Избегать магических значений** - заменить на константы

**Оптимизированный код**
```python
from __future__ import annotations

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers
   :platform: Windows, Unix
   :synopsis: Базовый класс сбора данных со страницы HTML поставщиков.
    Целевые поля страницы (`название`, `описание`, `спецификация`, `артикул`, `цена`, ...) собирает вебдрайвер (class: [`Driver`](../webdriver))
    Местоположение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))

    Для нестандартной обработки полей товара просто переопределите функцию в своем классе.

    Пример:

    .. code-block:: python

        s = `suppler_prefix`
        from src.suppliers imoprt Graber
        locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json')

        class G(Graber):

            @close_pop_up()
            async def name(self, value:Optional[Any] = None):
                self.fields.name = <Ваша реализация>

    Таблица поставщиков:
    https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""

MODE = 'dev'
DEFAULT_INT_VALUE = 1
DEFAULT_STRING_VALUE = ''
DEFAULT_FLOAT_VALUE = 0.0

import datetime
import os
import sys
import asyncio
from pathlib import Path
from typing import Optional, Any, Callable
from types import SimpleNamespace
from functools import wraps
from langdetect import detect

import header
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url, save_png
from src.utils.string.normalizer import (
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_boolean,
    normalize_sql_date,
    normalize_sku,
)
from src.logger.exceptions import ExecuteLocatorException
from src.logger.logger import logger


class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: `Driver`
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
                    # Выполняет локатор для закрытия всплывающего окна.
                    await Context.driver.execute_locator(Context.locator_for_decorator)
                    ...
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', exc_info=ex)
            return await func(*args, **kwargs)
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
        :type driver: `Driver`
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

        :param field: Название поля, для которого произошла ошибка.
        :type field: str
        """
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = DEFAULT_STRING_VALUE
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
            # Динамически вызывает функции для каждого поля из args
            for field_name in args:
                function = getattr(self, field_name, None)
                if function:
                    await function(kwargs.get(field_name, DEFAULT_STRING_VALUE))

        # Вызывает функцию для получения всех данных
        await fetch_all_data(*args, **kwargs)
        return self.fields
    
    def _set_field(self, value: Any, field_name: str):
      """
      Устанавливает значение поля, если оно передано.

      :param value: Значение для установки.
      :type value: Any
      :param field_name: Название поля.
      :type field_name: str
      """
      if value:
          setattr(self.fields, field_name, value)
          return True
      return False
    

    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает стоимость дополнительной доставки.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator и нормализует его.
            locator_value =  await self.driver.execute_locator(self.locator.additional_shipping_cost)
            value = normalize_string(value or locator_value or DEFAULT_STRING_VALUE)
            self.fields.additional_shipping_cost = value
            return True
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `additional_shipping_cost`", exc_info=ex)
            ...
            return

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доставки в наличии.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator и нормализует его.
            locator_value = await self.driver.execute_locator(self.locator.delivery_in_stock)
            value = normalize_string(value or locator_value or DEFAULT_STRING_VALUE)
            self.fields.delivery_in_stock = value
            return True
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `delivery_in_stock`", exc_info=ex)
            ...
            return

    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус активности.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator и нормализует его.
            locator_value = await self.driver.execute_locator(self.locator.active)
            value = normalize_int(value or locator_value or DEFAULT_INT_VALUE)
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `active`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.active}")
            ...
            return

        # Записывает результат в поле `active` объекта `ProductFields`.
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает дополнительное время доставки.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
             # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.additional_delivery_times)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `additional_delivery_times`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.additional_delivery_times}")
            ...
            return

        # Записывает результат в поле `additional_delivery_times` объекта `ProductFields`.
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус расширенного управления запасами.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value =  await self.driver.execute_locator(self.locator.advanced_stock_management)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `advanced_stock_management`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.advanced_stock_management}")
            ...
            return

        # Записывает результат в поле `advanced_stock_management` объекта `ProductFields`.
        self.fields.advanced_stock_management = value
        return True

    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает короткую ссылку аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.affiliate_short_link)
            self.fields.affiliate_short_link = value or locator_value or DEFAULT_STRING_VALUE
            return True
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_short_link`", exc_info=ex)
            ...
            return

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает сводку аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator и нормализует его.
            locator_value = await self.driver.execute_locator(self.locator.affiliate_summary)
            self.fields.affiliate_summary = normalize_string(value or locator_value or DEFAULT_STRING_VALUE)
            return True
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_summary`", exc_info=ex)
            ...
            return

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает сводку аффилиата 2.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.affiliate_summary_2)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_summary_2`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.affiliate_summary_2}")
            ...
            return

        # Записывает результат в поле `affiliate_summary_2` объекта `ProductFields`.
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает текст аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
             # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.affiliate_text)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_text`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.affiliate_text}")
            ...
            return

        # Записывает результат в поле `affiliate_text` объекта `ProductFields`.
        self.fields.affiliate_text = value
        return True

    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает большое изображение аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.affiliate_image_large)
            self.fields.affiliate_image_large = value or locator_value or DEFAULT_STRING_VALUE
            return True
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_image_large`", exc_info=ex)
            ...
            return

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает среднее изображение аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
         :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_result =  await self.driver.execute_locator(self.locator.affiliate_image_medium)
            value = value or locator_result or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_image_medium`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}")
            ...
            return

        # Записывает результат в поле `affiliate_image_medium` объекта `ProductFields`.
        self.fields.affiliate_image_medium = value
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает малое изображение аффилиата.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_result = await self.driver.execute_locator(self.locator.affiliate_image_small)
            value = value or locator_result or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `affiliate_image_small`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}")
            ...
            return

        # Записывает результат в поле `affiliate_image_small` объекта `ProductFields`.
        self.fields.affiliate_image_small = value
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает дату доступности.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_result = await self.driver.execute_locator(self.locator.available_date)
            value = value or locator_result or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `available_date`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}")
            ...
            return

        # Записывает результат в поле `available_date` объекта `ProductFields`.
        self.fields.available_date = value
        return True

    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности для заказа.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value =  await self.driver.execute_locator(self.locator.available_for_order)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `available_for_order`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.available_for_order}")
            ...
            return

        # Записывает результат в поле `available_for_order` объекта `ProductFields`.
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности позже.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
             # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.available_later)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `available_later`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.available_later}")
            ...
            return

        # Записывает результат в поле `available_later` объекта `ProductFields`.
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности сейчас.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.available_now)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
             logger.error(f"Ошибка при получении значения для поля `available_now`", exc_info=ex)
             ...
             return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.available_now}")
            ...
            return

        # Записывает результат в поле `available_now` объекта `ProductFields`.
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """
        Устанавливает дополнительные категории.

        :param value: Строка или список категорий.
        :type value: str | list, optional
        :return: Словарь с ID категорий.
        :rtype: dict
        """
        self.fields.additional_categories = value or DEFAULT_STRING_VALUE
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает кэшированный атрибут по умолчанию.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
         :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.cache_default_attribute)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `cache_default_attribute`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.cache_default_attribute}")
            ...
            return

        # Записывает результат в поле `cache_default_attribute` объекта `ProductFields`.
        self.fields.cache_default_attribute = value
        return True

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус наличия вложений в кэше.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.cache_has_attachments)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `cache_has_attachments`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.cache_has_attachments}")
            ...
            return

        # Записывает результат в поле `cache_has_attachments` объекта `ProductFields`.
        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус является ли товар комплектом в кэше.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.cache_is_pack)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `cache_is_pack`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.cache_is_pack}")
            ...
            return

        # Записывает результат в поле `cache_is_pack` объекта `ProductFields`.
        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает условие продукта.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.condition)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `condition`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.condition}")
            ...
            return

        # Записывает результат в поле `condition` объекта `ProductFields`.
        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус настраиваемости.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: Any, optional
        :return: True если значение установлено, иначе - None.
        :rtype: bool
        """
        try:
            # Получает значение через execute_locator.
            locator_value = await self.driver.execute_locator(self.locator.customizable)
            value = value or locator_value or DEFAULT_STRING_VALUE
        except Exception as ex:
            logger.error(f"Ошибка при получении значения для поля `customizable`", exc_info=ex)
            ...
            return

        # Проверяет валидность значения.
        if not value:
            logger.debug(f"Невалидный результат {value=}, локатор {self.locator.customizable}")
            ...
            return

        # Записывает результат в поле `customizable` объекта `ProductFields`.
        self.fields.customizable = value
        return True

    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool:
        """
        Извлекает и устанавливает дату добавления.

        :param value: Значение, которое можно передать через словарь kwargs.
        :type value: str | datetime.date, optional
        :return: True если значение установлено, иначе - None.