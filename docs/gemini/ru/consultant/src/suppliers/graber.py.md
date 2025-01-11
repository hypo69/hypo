### Анализ кода модуля `graber`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, используется асинхронное программирование.
    - Присутствует базовая документация в виде docstring.
    - Используются `normalize_string`, `normalize_int`, `normalize_float` и другие функции нормализации.
    - Применение декоратора `close_pop_up` для обработки всплывающих окон.
- **Минусы**:
    - Смешанное использование кавычек (используйте одинарные кавычки в коде).
    - Избыточное использование `try-except` блоков.
    - Не везде используется `logger.error` для записи ошибок.
    -  В некоторых функциях есть `...` как маркеры, которые нужно убрать.
    - Много повторяющегося кода в методах для каждого поля.
    - Отсутствует полная документация в формате RST.
    - Не все docstring содержат примеры использования.

**Рекомендации по улучшению:**

1. **Унификация кавычек:** Замените двойные кавычки на одинарные в коде, кроме `print`, `input` и `logger`.
2. **Обработка ошибок:** Используйте `logger.error` с указанием исключения `ex` вместо `print` для логирования ошибок.
3. **Удаление маркеров:** Замените все маркеры `...` на реализацию или удалите их.
4. **Рефакторинг:**  Выделите общую логику обработки полей в отдельную функцию или метод для избежания дублирования кода.
5. **Документация RST:** Добавьте полные docstring в формате RST для всех классов и методов, включая примеры использования.
6. **Импорт `logger`**: Импортируйте `logger` только из `src.logger.logger`
7. **Улучшение комментариев**: Сделайте комментарии более информативными, избегайте фраз вроде "получаем значение", "записываем результат".
8. **Переименование переменных**: Переименуйте `i18n` в более информативное название, например `locale_code`.
9. **Избегать `Any`**: По возможности, замените `Any` на более точные типы.

**Оптимизированный код:**

```python
from __future__ import annotations
## \file /src/suppliers/graber.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.suppliers
    :platform: Windows, Unix
    :synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`,`описание`,`спецификация`,`артикул`,`цена`,...) собирает вебдрйвер (class: [`Driver`](../webdriver))
    Местополжение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))
    
    ## Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
    Пример:
    
    .. code-block:: python
    
        s = 'suppler_prefix'
        from src.suppliers import Graber
        locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')
        
        class G(Graber):
        
            @close_pop_up()
            async def name(self, value:Optional[Any] = None):
                self.fields.name = <Ваша реализация>
                
    Таблица поставщиков:
    https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""


import datetime
import asyncio
from pathlib import Path
from typing import Optional, Any, Callable, TypeVar
from types import SimpleNamespace
from functools import wraps

from langdetect import detect

from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.category import Category
from src.utils.jjson import j_loads, j_loads_ns
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
from src.logger.logger import logger  # corrected import


T = TypeVar('T')

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
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


def close_pop_up(value: 'Driver' = None) -> Callable:
    """
    Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    :param value: Дополнительное значение для декоратора.
    :type value: 'Driver', optional
    :return: Декоратор, оборачивающий функцию.
    :rtype: Callable

    :Example:
        >>> @close_pop_up()
        >>> async def some_function():
        >>>     pass
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', exc_info=ex) # corrected logger call
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator


class Graber:
    """
    Базовый класс сбора данных со страницы для всех поставщиков.

    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar driver: Объект драйвера.
    :vartype driver: 'Driver'
    :ivar fields: Объект для хранения собранных полей продукта.
    :vartype fields: ProductFields
    """

    def __init__(self, supplier_prefix: str, driver: 'Driver'):
        """
        Инициализация класса Graber.

        :param supplier_prefix: Префикс поставщика.
        :type supplier_prefix: str
        :param driver: Экземпляр класса Driver.
        :type driver: 'Driver'
        
        :Example:
            >>> grabber = Graber('test_supplier', driver_instance)
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

        :param field: Название поля, в котором произошла ошибка.
        :type field: str

        :Example:
            >>> await self.error('name')
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

        :Example:
            >>> value = await self.set_field_value(None, lambda: 'Test value', 'name')
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
        :param kwards: Словарь с ключами и значениями для каждого поля.
        :type kwards: dict
        :return: Собранные поля продукта.
        :rtype: ProductFields

        :Example:
            >>> product_fields = await self.grab_page('name', 'price', name='My Product', price='100')
        """
        async def fetch_all_data(*args, **kwards):
            for filed_name in args:
                function = getattr(self, filed_name, None)
                if function:
                    await function(kwards.get(filed_name, ''))

        await fetch_all_data(*args, **kwards)
        return self.fields


    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает стоимость дополнительной доставки.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.additional_shipping_cost(value='10')
            >>> result = await self.additional_shipping_cost()
        """
        try:
            self.fields.additional_shipping_cost = normalize_string(
                value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_shipping_cost`', exc_info=ex) # corrected logger call
            return None
    
    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус наличия на складе.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.delivery_in_stock(value='In Stock')
            >>> result = await self.delivery_in_stock()
        """
        try:
            self.fields.delivery_in_stock = normalize_string(
                value or await self.driver.execute_locator(self.locator.delivery_in_stock) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `delivery_in_stock`', exc_info=ex) # corrected logger call
            return None

    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус активности товара.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.active(value=1)
            >>> result = await self.active()
        """
        try:
            value = normalize_int(value or await self.driver.execute_locator(self.locator.active) or 1)
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `active`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.active}')
            return None

        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает дополнительное время доставки.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

         :Example:
            >>> result = await self.additional_delivery_times(value='2 days')
            >>> result = await self.additional_delivery_times()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.additional_delivery_times) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `additional_delivery_times`', exc_info=ex) # corrected logger call
            return None
            
        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.additional_delivery_times}')
            return None

        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус расширенного управления запасами.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.advanced_stock_management(value='enabled')
            >>> result = await self.advanced_stock_management()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.advanced_stock_management) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `advanced_stock_management`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.advanced_stock_management}')
            return None

        self.fields.advanced_stock_management = value
        return True
    
    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает короткую ссылку аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.affiliate_short_link(value='http://short.link')
            >>> result = await self.affiliate_short_link()
        """
        try:
            self.fields.affiliate_short_link = value or await self.driver.execute_locator(
                self.locator.affiliate_short_link
            ) or ''
            return True
        except Exception as ex:
             logger.error(f'Ошибка получения значения в поле `affiliate_short_link`', exc_info=ex) # corrected logger call
             return None

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает сводку аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.affiliate_summary(value='Summary text')
            >>> result = await self.affiliate_summary()
        """
        try:
            self.fields.affiliate_summary = normalize_string(
                value or await self.driver.execute_locator(self.locator.affiliate_summary) or ''
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary`', exc_info=ex) # corrected logger call
            return None

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает вторую сводку аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.affiliate_summary_2(value='Second summary')
            >>> result = await self.affiliate_summary_2()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.affiliate_summary_2) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_summary_2`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_summary_2}')
            return None

        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает текст аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.affiliate_text(value='Affiliate text')
            >>> result = await self.affiliate_text()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_text`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.affiliate_text}')
            return None

        self.fields.affiliate_text = value
        return True
    
    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает большое изображение аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.affiliate_image_large(value='http://large.image.url')
            >>> result = await self.affiliate_image_large()
        """
        try:
            self.fields.affiliate_image_large = value or await self.driver.execute_locator(
                self.locator.affiliate_image_large
            ) or ''
            return True
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_large`', exc_info=ex) # corrected logger call
            return None

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает среднее изображение аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.affiliate_image_medium(value='http://medium.image.url')
            >>> result = await self.affiliate_image_medium()
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_medium) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_medium`', exc_info=ex) # corrected logger call
            return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает малое изображение аффилиата.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.affiliate_image_small(value='http://small.image.url')
            >>> result = await self.affiliate_image_small()
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_small) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `affiliate_image_small`', exc_info=ex) # corrected logger call
            return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает дату доступности товара.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.available_date(value='2024-12-24')
            >>> result = await self.available_date()
        """
        try:
            locator_result = value or await self.driver.execute_locator(self.locator.available_date) or ''
        except Exception as ex:
             logger.error(f'Ошибка получения значения в поле `available_date`', exc_info=ex) # corrected logger call
             return None

        if not locator_result:
            logger.debug(f'Невалидный результат {locator_result=}')
            return None

        self.fields.available_date = locator_result
        return True
    
    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус доступности для заказа.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.available_for_order(value='1')
            >>> result = await self.available_for_order()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_for_order) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_for_order`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_for_order}')
            return None

        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус доступности позже.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.available_later(value='Available later text')
            >>> result = await self.available_later()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `available_later`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_later}')
            return None

        self.fields.available_later = value
        return True
    
    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус доступности сейчас.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.available_now(value='Available now text')
            >>> result = await self.available_now()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
             logger.error(f'Ошибка получения значения в поле `available_now`', exc_info=ex) # corrected logger call
             return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.available_now}')
            return None

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

        :Example:
             >>> result = await self.additional_categories(value=['category1', 'category2'])
             >>> result = await self.additional_categories()
        """
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает кэшированный атрибут по умолчанию.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.cache_default_attribute(value='default_attribute')
            >>> result = await self.cache_default_attribute()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_default_attribute) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_default_attribute`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_default_attribute}')
            return None

        self.fields.cache_default_attribute = value
        return True

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус наличия вложений в кэше.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.cache_has_attachments(value='1')
            >>> result = await self.cache_has_attachments()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_has_attachments) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_has_attachments`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_has_attachments}')
            return None

        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус является ли товар набором в кэше.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.cache_is_pack(value='1')
            >>> result = await self.cache_is_pack()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_is_pack) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `cache_is_pack`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.cache_is_pack}')
            return None

        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает условие товара.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None

        :Example:
            >>> result = await self.condition(value='new')
            >>> result = await self.condition()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.condition) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `condition`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.condition}')
            return None

        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool | None:
        """
        Извлекает и устанавливает статус настраиваемости товара.

        :param value: Значение, переданное через kwargs.
        :type value: Any, optional
        :return: True при успешном выполнении, None в случае ошибки.
        :rtype: bool | None
        
        :Example:
            >>> result = await self.customizable(value='1')
            >>> result = await self.customizable()
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.customizable) or ''
        except Exception as ex:
            logger.error(f'Ошибка получения значения в поле `customizable`', exc_info=ex) # corrected logger call
            return None

        if not value:
            logger.debug(f'Невалидный результат {value=}\nлокатор {self.locator.customizable}')
            return None

        self.fields.customizable = value
        return True
    
    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool | None:
        """
        Извлекает и устанавливает дату добавления товара.

        :