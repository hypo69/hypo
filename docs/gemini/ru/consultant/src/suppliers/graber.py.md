# Анализ кода модуля `graber.py`

**Качество кода**
9
 -  Плюсы
    -   Код хорошо структурирован, с разделением на классы и функции, что обеспечивает читаемость и удобство в сопровождении.
    -   Используется асинхронное программирование для неблокирующих операций, что повышает производительность.
    -   Применена система логирования для отслеживания ошибок и предупреждений.
    -   Присутствуют docstring для классов, методов и функций, что способствует пониманию кода.
    -   Имеется декоратор `@close_pop_up` для обработки всплывающих окон.
    -   Используются `normalize_*` функции для приведения типов данных к единому стандарту.
 -  Минусы
    -   Много повторяющегося кода в методах, отвечающих за получение значений полей (блоки `try-except`, проверки `if not value:`, запись в `self.fields.*`).
    -   Некоторые методы содержат `...` в блоках обработки ошибок, что не является хорошей практикой.
    -   Дублирование кода в методе `error`
    -   В некоторых методах отсутствует проверка на `None` перед вызовом `normalize_*` функций.
    -   В `local_saved_image` есть потенциальный баг при передачи `id_supplier` через kwargs, также есть `todo` по фиксации путей.
    -   Встречаются конструкции `value or await ... or ''` их можно заменить на `value or await ...` c `default=''` в методе.
    -   Импорт `header` не используется.

**Рекомендации по улучшению**

1.  **Рефакторинг методов получения значений**:
    -   Создайте общую функцию для извлечения и нормализации значений полей, чтобы избежать дублирования кода в каждом методе.

2.  **Удаление `...`**:
    -   Замените все `...` на конкретную обработку ошибок. В идеале, просто логировать ошибку и возвращать `None` или дефолтное значение.
  
3. **Улучшение декоратора `close_pop_up`**
   - Добавить проверку `Context.driver is not None` перед попыткой вызвать `execute_locator` для предотвращения ошибки при отсутствии драйвера.

4.  **Улучшение `local_saved_image`**:
    -   Передать `id_supplier` через аргументы функции или контекст.
    -   Избавится от `todo` по фиксации путей

5.  **Оптимизация проверок и присваивания**:
    -   Использовать значение по умолчанию в `await self.driver.execute_locator(locator, default='')` для упрощения логики.
    -   Использовать `normalize_string(value, default='')` и другие нормализаторы для упрощения логики.

6.  **Исправить дублирование кода**:
    -   Метод `error` дублируется, нужно оставить один.

7. **Убрать неиспользуемые импорты**
     -Удалить импорт `header`
**Оптимизированный код**

```python
from __future__ import annotations

## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
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
s = `suppler_prefix`
from src.suppliers import Graber
locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json`)

class G(Graber):

    @close_pop_up()
    async def name(self, value:Optional[Any] = None):
        self.fields.name = <Ваша реализация>
        )
    ```
    Таблица поставщиков:
    https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""
MODE = 'dev'

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

# from header import header # не использутся
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
# from src.webdriver.driver import Driver  # не требуется импортировать здесь
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url, save_png
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

    :param value: Дополнительное значение для декоратора.
    :type value: 'Driver', optional
    :return: Декоратор, оборачивающий функцию.
    :rtype: Callable
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator and Context.driver is not None: # Проверяем, что драйвер существует
                try:
                    # код исполняет закрытие всплывающего окна
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close  
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            # код исполняет основную функцию
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""
    
    def __init__(self, supplier_prefix: str, driver: 'Driver'):
        """Инициализация класса Graber.

        :param supplier_prefix: Префикс поставщика.
        :type supplier_prefix: str
        :param driver: Экземпляр класса Driver.
        :type driver: 'Driver'
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.driver = driver
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix

    async def error(self, field: str):
        """Обработчик ошибок для полей.
        
        :param field: Имя поля, для которого произошла ошибка.
        :type field: str
        """
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.
        
        :param value: Значение для установки.
        :type value: Any
        :param locator_func: Функция для получения значения из локатора.
        :type locator_func: Callable[[], Any]
        :param field_name: Название поля.
        :type field_name: str
        :param default: Значение по умолчанию. По умолчанию пустая строка.
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


    async def grab_page(self, *args, **kwards) -> ProductFields:
        """Асинхронная функция для сбора полей продукта.
        
        :param args: Кортеж с названиями полей для сбора.
        :type args: tuple
        :param kwards: Словарь с ключами и значениями для каждого поля.
        :type kwards: dict
        :return: Собранные поля продукта.
        :rtype: ProductFields
        """
        async def fetch_all_data(*args, **kwards):
            # Динамическое вызовы функций для каждого поля из args
            for filed_name in args:
                #method_name = method_name.replace('_', '')  # Преобразуем имя поля в метод
                function = getattr(self, filed_name, None)  # Получаем метод по имени
                if function:
                    await function(kwards.get(filed_name, ''))

        # Вызов функции для получения всех данных
        await fetch_all_data(*args, **kwards)
        return self.fields


    @close_pop_up()
    async def additional_shipping_cost(self, value:Optional[Any] = None):
        """Получение и установка стоимости доставки.
        
        :param value: Значение можно передать в словаре kwargs через ключ {additional_shipping_cost = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.additional_shipping_cost`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.additional_shipping_cost = normalize_string(value or  await self.driver.execute_locator(self.locator.additional_shipping_cost, default='') )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `additional_shipping_cost`", ex)
            return


    @close_pop_up()
    async def delivery_in_stock(self, value:Optional[Any] = None):
        """Получение и установка статуса доставки на складе.
        
        :param value: Значение можно передать в словаре kwargs через ключ {delivery_in_stock = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.delivery_in_stock`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.delivery_in_stock = normalize_string( value or  await self.driver.execute_locator(self.locator.delivery_in_stock, default='') )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `delivery_in_stock`", ex)
            return


    @close_pop_up()
    async def active(self, value:Optional[Any] = None):
        """Получение и установка статуса активности товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {active = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.active`.
        Принимаемое значение 1/0
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = normalize_int( value or  await self.driver.execute_locator(self.locator.active, default=1))
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `active`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.active}")
            return

        # Код записывает результат в поле `active` объекта `ProductFields`
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value:Optional[Any] = None):
        """Получение и установка дополнительного времени доставки.
        
        :param value: Значение можно передать в словаре kwargs через ключ {additional_delivery_times = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.additional_delivery_times`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.additional_delivery_times, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `additional_delivery_times`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.additional_delivery_times}")
            return

        # Код записывает результат в поле `additional_delivery_times` объекта `ProductFields`
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value:Optional[Any] = None):
        """Получение и установка статуса управления запасами.
        
        :param value: Значение можно передать в словаре kwargs через ключ {advanced_stock_management = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.advanced_stock_management`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.advanced_stock_management, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `advanced_stock_management`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.advanced_stock_management}")
            return

        # Код записывает результат в поле `advanced_stock_management` объекта `ProductFields`
        self.fields.advanced_stock_management = value
        return True
    @close_pop_up()
    async def affiliate_short_link(self, value:Optional[Any] = None):
        """Получение и установка короткой партнерской ссылки.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_short_link = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_short_link`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.affiliate_short_link = value or  await self.driver.execute_locator(self.locator.affiliate_short_link, default='')
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_short_link`", ex)
            return

    @close_pop_up()
    async def affiliate_summary(self, value:Optional[Any] = None):
        """Получение и установка партнерского резюме.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_summary = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.affiliate_summary = normalize_string( value or  await self.driver.execute_locator(self.locator.affiliate_summary, default='') )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary`", ex)
            return


    @close_pop_up()
    async def affiliate_summary_2(self, value:Optional[Any] = None):
        """Получение и установка партнерского резюме 2.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_summary_2 = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary_2`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.affiliate_summary_2, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary_2`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_summary_2}")
            return

        # Код записывает результат в поле `affiliate_summary_2` объекта `ProductFields`
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value:Optional[Any] = None):
        """Получение и установка партнерского текста.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_text = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_text`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.affiliate_text, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_text`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_text}")
            return

        # Код записывает результат в поле `affiliate_text` объекта `ProductFields`
        self.fields.affiliate_text = value
        return True
    @close_pop_up()
    async def affiliate_image_large(self, value:Optional[Any] = None):
        """Получение и установка большого партнерского изображения.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_large = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_large`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.affiliate_image_large  = value or  await self.driver.execute_locator(self.locator.affiliate_image_large, default='')
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_large`", ex)
            return

    @close_pop_up()
    async def affiliate_image_medium(self, value:Optional[Any] = None):
        """Получение и установка среднего партнерского изображения.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_medium = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_medium`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or  await self.driver.execute_locator(self.locator.affiliate_image_medium, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_medium`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Код записывает результат в поле `affiliate_image_medium` объекта `ProductFields`
        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value:Optional[Any] = None):
        """Получение и установка маленького партнерского изображения.
        
        :param value: Значение можно передать в словаре kwargs через ключ {affiliate_image_small = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_small`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or  await self.driver.execute_locator(self.locator.affiliate_image_small, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_small`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Код записывает результат в поле `affiliate_image_small` объекта `ProductFields`
        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value:Optional[Any] = None):
        """Получение и установка даты доступности.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_date = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_date`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or  await self.driver.execute_locator(self.locator.available_date, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_date`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Код записывает результат в поле `available_date` объекта `ProductFields`
        self.fields.available_date = locator_result
        return True
    @close_pop_up()
    async def available_for_order(self, value:Optional[Any] = None):
        """Получение и установка статуса доступности для заказа.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_for_order`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.available_for_order, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_for_order`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_for_order}")
            return

        # Код записывает результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value:Optional[Any] = None):
        """Получение и установка статуса доступности позже.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_later`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.available_later, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_later`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_later}")
            return

        # Код записывает результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value:Optional[Any] = None):
        """Получение и установка статуса доступности сейчас.
        
        :param value: Значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_now`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.available_now, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_now`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_now}")
            return

        # Код записывает результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """Установка дополнительных категорий.
        
        :param value: Строка или список категорий. Если не передано, используется пустое значение.
        :type value: str | list, optional
        :return: Словарь с ID категорий.
        :rtype: dict
        
        Значение можно передать в словаре kwargs через ключ {additional_categories = `value`} при определении класса.
        Если `value` было передано, оно подставляется в поле `ProductFields.additional_categories`.
        """
        self.fields.additional_categories = value or  ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value:Optional[Any] = None):
        """Получение и установка кэшированного атрибута по умолчанию.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.cache_default_attribute`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.cache_default_attribute, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_default_attribute`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_default_attribute}")
            return

        # Код записывает результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value
        return True
    @close_pop_up()
    async def cache_has_attachments(self, value:Optional[Any] = None):
        """Получение и установка статуса наличия вложений в кэше.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.cache_has_attachments`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.cache_has_attachments, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_has_attachments`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_has_attachments}")
            return

        # Код записывает результат в поле `cache_has_attachments` объекта `ProductFields`
        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value:Optional[Any] = None):
        """Получение и установка статуса упаковки в кэше.
        
        :param value: Значение можно передать в словаре kwargs через ключ {cache_is_pack = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.cache_is_pack`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.cache_is_pack, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_is_pack`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_is_pack}")
            return

        # Код записывает результат в поле `cache_is_pack` объекта `ProductFields`
        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value:Optional[Any] = None):
        """Получение и установка условия товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {condition = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.condition`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.condition, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `condition`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.condition}")
            return

        # Код записывает результат в поле `condition` объекта `ProductFields`
        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value:Optional[Any] = None):
        """Получение и установка статуса настройки товара.
        
        :param value: Значение можно передать в словаре kwargs через ключ {customizable = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.customizable`.
        :type value: Any, optional
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or  await self.driver.execute_locator(self.locator.customizable, default='')
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `customizable`", ex)
            return

        # Проверка валидности `value`
        if not value:
            logger