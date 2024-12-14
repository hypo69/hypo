# Анализ кода модуля `graber.py`

**Качество кода**
8
*   **Плюсы**
    *   Код хорошо структурирован с использованием классов и функций.
    *   Присутствует базовая обработка ошибок с использованием `try-except` блоков и логирования.
    *   Используется асинхронность для выполнения операций с веб-драйвером.
    *   Реализован декоратор `close_pop_up` для обработки всплывающих окон.
    *   Используется `j_loads_ns` для загрузки JSON.
    *   Присутствуют функции для нормализации данных.

*   **Минусы**
    *   Много избыточных блоков `try-except` с `...` вместо более точной обработки ошибок.
    *   Не все функции имеют docstring,  необходимо добавить описание в формате RST.
    *   Использование `logger.debug` для ошибок может привести к засорению логов.
    *   Не все функции используют `normalize_string` для нормализации строк, что может привести к некорректным данным.
    *   Смешанное использование `value or await` и `await self.driver.execute_locator() or value`, что делает код менее читаемым.
    *   Сложная логика проверок `if not value: logger.debug... return` внутри каждой функции, можно упростить.
    *   Отсутствует описание и примеры использования для класса `Context`.

**Рекомендации по улучшению**

1.  **Унифицировать обработку ошибок**:
    *   Использовать `logger.error` для логирования ошибок, `logger.debug` оставить для отладочной информации.
    *   Избегать избыточных `try-except` блоков, где это возможно, вынести обработку ошибок в отдельную функцию.
    *   Убрать `...` и либо пробросить ошибку, либо корректно её обработать.

2.  **Документирование**:
    *   Добавить docstring в формате reStructuredText (RST) для всех функций, методов и классов.
    *   Добавить описание класса `Context` и его атрибутов в формате RST.
    *   Указать назначение и использование декоратора `@close_pop_up` в docstring.

3.  **Улучшить читаемость кода**:
    *   Упростить логику проверок `if not value`, возможно создать отдельную функцию для проверки валидности.
    *   Использовать `normalize_string` для всех строковых полей.
    *   Избегать дублирования кода, вынести общие операции в отдельные функции.
    *   Переписать блок получения данных из локатора, используя функцию с обработкой ошибок.
     
4.  **Улучшить сохранение локальных файлов**:
    *   Сделать путь для сохранения файлов настраиваемым.
    *   Обработать исключения при сохранении файлов.
   
5.  **Улучшить работу с локаторами**:
    *   Упростить вызов локаторов, через единую функцию, с логированием ошибки.

6.  **Использование `j_loads`**:
    *   Убедится что `j_loads_ns` используется во всех нужных местах.

**Оптимизированный код**

```python
"""
Модуль для сбора данных о товарах с веб-страниц поставщиков.
=========================================================================================

Этот модуль содержит класс :class:`Graber`, который обеспечивает базовый функционал для сбора данных
о товарах с веб-страниц поставщиков. Он использует веб-драйвер для навигации по страницам и извлечения
информации с помощью локаторов, определенных в JSON файлах.

Класс :class:`Graber` предоставляет методы для получения различных полей товара, таких как название,
описание, цена, артикул и т.д. Для нестандартной обработки полей товара можно переопределить
соответствующие методы в производных классах.

Пример использования:
---------------------

.. code-block:: python

    s = 'suppler_prefix'
    from src.suppliers import Graber
    locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json')

    class G(Graber):

        @close_pop_up()
        async def name(self, value:Optional[Any] = None):
            self.fields.name = <Ваша реализация>

Таблица поставщиков:
---------------------
https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?gid=1778506526#gid=1778506526
"""
from __future__ import annotations

import asyncio
import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional
from types import SimpleNamespace

from langdetect import detect

from src import gs
# from src.webdriver.driver import Driver # не требуется импортировать здесь
from src.category import Category
from src.logger.exceptions import ExecuteLocatorException
from src.logger.logger import logger
from src.product.product_fields import ProductFields
from src.utils.image import save_png, save_png_from_url
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint
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
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: 'Driver'
    :ivar locator_for_decorator: Пространство имен для хранения локаторов, которые будут использованы в декораторе `close_pop_up`.
    :vartype locator_for_decorator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    driver: 'Driver' = None
    locator_for_decorator: SimpleNamespace = None
    supplier_prefix: str = None


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
                    # код исполняет закрытие всплывающего окна через execute_locator
                    await Context.driver.execute_locator(Context.locator_for_decorator)
                except ExecuteLocatorException as ex:
                    # логирование ошибки при выполнении локатора
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            # код исполняет основную функцию
            return await func(*args, **kwargs)
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

    async def _execute_locator(self, locator: SimpleNamespace, default: Any = '') -> Any:
        """Выполняет локатор и возвращает результат.

        Args:
            locator (SimpleNamespace): Локатор для выполнения.
            default (Any): Значение по умолчанию, если локатор не вернул результата.

        Returns:
            Any: Результат выполнения локатора или значение по умолчанию.
        """
        try:
            # код исполняет получение значения через execute_locator
            result = await self.driver.execute_locator(locator)
            return result or default
        except Exception as ex:
            # логирование ошибки при выполнении локатора
            logger.error(f"Ошибка выполнения локатора: {locator=}", ex)
            return default

    async def error(self, field: str):
        """Обработчик ошибок для полей.

        Args:
            field (str): Название поля.
        """
        # логирование ошибки заполнения поля
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = '',
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.

        Args:
            value (Any): Значение для установки.
            locator_func (Callable[[], Any]): Функция для получения значения из локатора.
            field_name (str): Название поля.
            default (Any): Значение по умолчанию.

        Returns:
            Any: Установленное значение.
        """
        # код исполняет получение значения из локатора в отдельном потоке
        locator_result = await asyncio.to_thread(locator_func)
        if value:
            return value
        if locator_result:
            return locator_result
        # логирование ошибки, если значение не найдено
        await self.error(field_name)
        return default

    async def grab_page(self, *args, **kwards) -> ProductFields:
        """Асинхронная функция для сбора полей продукта.

        Args:
            args (tuple): Кортеж с названиями полей для сбора.
            kwards (dict): Словарь с ключами и значениями для каждого поля.

        Returns:
            ProductFields: Собранные поля продукта.
        """
        async def fetch_all_data(*args, **kwards):
            # Динамически вызываем функции для каждого поля из args
            for filed_name in args:
                # получаем метод по имени
                function = getattr(self, filed_name, None)
                if function:
                    # код исполняет вызов метода с параметром из kwards
                    await function(kwards.get(filed_name, ''))

        # код исполняет получение всех данных
        await fetch_all_data(*args, **kwards)
        return self.fields
    
    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None):
        """Устанавливает дополнительную стоимость доставки.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение и нормализацию значения через execute_locator
            self.fields.additional_shipping_cost = normalize_string(
                value or await self._execute_locator(self.locator.additional_shipping_cost)
            )
            return True
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `additional_shipping_cost`", ex)
            return

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None):
        """Устанавливает статус наличия на складе.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение и нормализацию значения через execute_locator
            self.fields.delivery_in_stock = normalize_string(
                value or await self._execute_locator(self.locator.delivery_in_stock)
            )
            return True
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `delivery_in_stock`", ex)
            return

    @close_pop_up()
    async def active(self, value: Optional[Any] = None):
        """Устанавливает статус активности товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение и нормализацию значения через execute_locator
            value = normalize_int(
                value or await self._execute_locator(self.locator.active, 1)
            )
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `active`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
             # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.active}")
            return

        # Записываем результат в поле `active` объекта `ProductFields`
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None):
        """Устанавливает дополнительное время доставки.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.additional_delivery_times)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `additional_delivery_times`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.additional_delivery_times}")
            return

        # Записываем результат в поле `additional_delivery_times` объекта `ProductFields`
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None):
        """Устанавливает статус расширенного управления запасами.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.advanced_stock_management)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `advanced_stock_management`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.advanced_stock_management}")
            return

        # Записываем результат в поле `advanced_stock_management` объекта `ProductFields`
        self.fields.advanced_stock_management = value
        return True
    
    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None):
        """Устанавливает партнерскую короткую ссылку.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.affiliate_short_link = value or await self._execute_locator(self.locator.affiliate_short_link)
            return True
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_short_link`", ex)
            return

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None):
        """Устанавливает партнерский сводный текст.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение и нормализацию значения через execute_locator
            self.fields.affiliate_summary = normalize_string(
                value or await self._execute_locator(self.locator.affiliate_summary)
            )
            return True
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_summary`", ex)
            return

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None):
        """Устанавливает второй партнерский сводный текст.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.affiliate_summary_2)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_summary_2`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_summary_2}")
            return

        # Записываем результат в поле `affiliate_summary_2` объекта `ProductFields`
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None):
        """Устанавливает партнерский текст.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.affiliate_text)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_text`", ex)
            return
        
        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_text}")
            return

        # Записываем результат в поле `affiliate_text` объекта `ProductFields`
        self.fields.affiliate_text = value
        return True
    
    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None):
        """Устанавливает большую партнерскую картинку.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            self.fields.affiliate_image_large = value or await self._execute_locator(self.locator.affiliate_image_large)
            return True
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_image_large`", ex)
            return

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None):
        """Устанавливает среднюю партнерскую картинку.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or await self._execute_locator(self.locator.affiliate_image_medium)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_image_medium`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле `affiliate_image_medium` объекта `ProductFields`
        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None):
        """Устанавливает маленькую партнерскую картинку.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or await self._execute_locator(self.locator.affiliate_image_small)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `affiliate_image_small`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле `affiliate_image_small` объекта `ProductFields`
        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None):
        """Устанавливает дату доступности товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            locator_result = value or await self._execute_locator(self.locator.available_date)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `available_date`", ex)
            return

        # Проверка валидности `value`
        if not locator_result:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {locator_result=}")
            return

        # Записываем результат в поле `available_date` объекта `ProductFields`
        self.fields.available_date = locator_result
        return True
    
    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None):
        """Устанавливает статус доступности для заказа.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.available_for_order)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `available_for_order`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_for_order}")
            return

        # Записываем результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None):
        """Устанавливает статус доступности позже.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
             # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.available_later)
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `available_later`", ex)
            return

        # Проверка валидности `value`
        if not value:
             # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_later}")
            return

        # Записываем результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None):
        """Устанавливает статус доступности сейчас.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.available_now)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `available_now`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_now}")
            return

        # Записываем результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """Устанавливает дополнительные категории.

        Args:
            value (str | list, optional): Строка или список категорий. Если не передано, используется пустое значение.

        Returns:
            dict: Словарь с ID категорий.
        """
        # устанавливает значение дополнительных категорий
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None):
        """Устанавливает кэш атрибута по умолчанию.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.cache_default_attribute)
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `cache_default_attribute`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_default_attribute}")
            return

        # Записываем результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value
        return True
    
    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None):
        """Устанавливает статус наличия вложений в кэше.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.cache_has_attachments)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `cache_has_attachments`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_has_attachments}")
            return

        # Записываем результат в поле `cache_has_attachments` объекта `ProductFields`
        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None):
        """Устанавливает статус комплекта в кэше.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.cache_is_pack)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `cache_is_pack`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_is_pack}")
            return

        # Записываем результат в поле `cache_is_pack` объекта `ProductFields`
        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None):
        """Устанавливает состояние товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.condition)
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `condition`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.condition}")
            return

        # Записываем результат в поле `condition` объекта `ProductFields`
        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None):
        """Устанавливает статус возможности настройки товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
             # код исполняет получение значения через execute_locator
            value = value or await self._execute_locator(self.locator.customizable)
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `customizable`", ex)
            return

        # Проверка валидности `value`
        if not value:
            # логирование невалидного значения
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.customizable}")
            return

        # Записываем результат в поле `customizable` объекта `ProductFields`
        self.fields.customizable = value
        return True
    
    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None):
        """Устанавливает дату добавления товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
             # код исполняет получение и нормализацию значения через execute_locator
            self.fields.date_add = normalize_sql_date(
                value or await self._execute_locator(self.locator.date_add, gs.now)
            )
            return True
        except Exception as ex:
             # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `date_add`", ex)
            return
        
    @close_pop_up()
    async def date_upd(self, value: Optional[Any] = None):
        """Устанавливает дату обновления товара.

        Args:
            value (Any, optional): Значение, которое можно передать через kwargs.
                Если `value` передано, оно используется; иначе используется значение из локатора.
        """
        try:
            # код исполняет получение и нормализацию значения через execute_locator
            self.fields.date_upd = normalize_sql_date(
                value or await self._execute_locator(self.locator.date_upd, gs.now)
            )
            return True
        except Exception as ex:
            # логирование ошибки получения значения
            logger.error(f"Ошибка получения значения в поле `date_upd`", ex)
            return

    @close_pop_up()
    async def delivery_out_stock(self, value: Optional[Any] = None):
        """