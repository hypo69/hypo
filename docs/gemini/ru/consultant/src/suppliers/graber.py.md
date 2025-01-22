### Анализ кода модуля `graber`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование асинхронности для неблокирующих операций.
    - Применение декоратора `close_pop_up` для обработки всплывающих окон.
    - Наличие класса `Context` для хранения глобальных настроек.
    - Применение `normalize_*` функций для обработки данных.
    - Использование `j_loads_ns` для загрузки JSON-конфигураций.
    - Применение `logger.error` для обработки ошибок.
    - Применение `ProductFields` для хранения данных.
    - Использование `asyncio.to_thread` для выполнения синхронных функций в асинхронном коде.
- **Минусы**:
    -   Использование `try-except` с `...` (многоточие) для игнорирования ошибок.
    -   Множественные проверки на `if not value:`  в методах.
    -   Не всегда используется  `normalize_string` перед присваиванием значений в поля.
    -   Отсутствие документации в формате **RST** для большинства функций и классов.
    -   Не везде используется `value or` в обработке данных.
    -   Не везде корректно обрабатываются возвращаемые значения в методах.
    -   Использование `normalize_int` и `normalize_string` для `ProductFields.show_price` и `ProductFields.show_condition` может привести к ошибкам.
    -   В некоторых методах отсутствует возврат значения (например,  `how_to_use`).
    -   Дублирование кода в некоторых блоках.

**Рекомендации по улучшению**:

- Заменить `...` (многоточие) на `return`  или `continue` в блоках обработки ошибок, если это необходимо.
- Добавить **RST**-документацию для всех функций, методов и классов.
- Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` в соответствии с инструкциями.
- Оптимизировать код, избегая дублирования проверок `if not value:`, возможно, вынести эту логику в отдельную функцию.
- Проверять типы данных при присваивании значений полям, использовать соответствующие функции нормализации.
- Использовать `value or` в обработке значений, где это целесообразно.
- Добавить проверки возвращаемых значений в методах и в случае необходимости возвращать  `True` или `False`
- Использовать `logger.debug` вместо `print` для отладочного вывода.
- Оптимизировать  вызовы `logger.error` для более информативной отладки.
- Проверить все методы на корректность присвоения значений.

**Оптимизированный код**:
```python
"""
Модуль для сбора данных о товарах с веб-страниц поставщиков.
============================================================

Модуль содержит класс :class:`Graber`, который является базовым классом для сбора данных о товарах
с веб-страниц различных поставщиков. Он использует веб-драйвер (класс :class:`Driver`) для навигации по страницам
и извлечения необходимых данных с использованием локаторов, хранящихся в JSON-файлах.

Класс Graber предоставляет методы для сбора различных полей товара, таких как название, описание, артикул, цена и т.д.
Для не стандартной обработки полей товара,  переопределите соответствующую функцию в своем классе.

Пример использования
----------------------
.. code-block:: python

    s = 'suppler_prefix'
    from src.suppliers import Graber
    locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

    class G(Graber):

        @close_pop_up()
        async def name(self, value: Optional[Any] = None):
            self.fields.name = <Ваша реализация>
            )

Таблица поставщиков:
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
from src.endpoints.prestashop.product_fields import ProductFields
from src.utils.jjson import j_loads_ns
from src.utils.image import save_image, save_image_from_url
from src.utils.string.normalizer import (
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_sql_date,
    normalize_sku,
)
from src.logger.exceptions import ExecuteLocatorException
from src.utils.printer import pprint
from src.logger.logger import logger  # Correct import


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
    Декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

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
                    await Context.driver.execute_locator(Context.locator_for_decorator)
                    ...
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', exc_info=ex)  # corrected log
            return await func(*args, **kwargs)

        return wrapper

    return decorator


class Graber:
    """
    Базовый класс для сбора данных со страницы для всех поставщиков.

    :param supplier_prefix: Префикс поставщика.
    :type supplier_prefix: str
    :param driver: Экземпляр класса Driver.
    :type driver: 'Driver'
    """

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
            gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json'
        )
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
        :type default: Any
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
        """
        Асинхронная функция для сбора полей продукта.

        :param args: Кортеж с названиями полей для сбора.
        :type args: tuple
        :param kwards: Словарь с ключами и значениями для каждого поля.
        :type kwards: dict
        :return: Собранные поля продукта.
        :rtype: ProductFields
        """

        async def fetch_all_data(*args, **kwards):
            """Внутренняя функция для динамического вызова методов."""
            for filed_name in args:
                function = getattr(self, filed_name, None)
                if function:
                    await function(kwards.get(filed_name, ''))

        await fetch_all_data(*args, **kwards)
        return self.fields

    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает стоимость дополнительной доставки.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.additional_shipping_cost = normalize_string(
                value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or ''
            )
            return True
        except Exception as ex:
            logger.error("Ошибка получения значения в поле `additional_shipping_cost`", exc_info=ex)
            return False

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус наличия на складе.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.delivery_in_stock = normalize_string(
                value or await self.driver.execute_locator(self.locator.delivery_in_stock) or ''
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `delivery_in_stock`", exc_info=ex)
            return False

    @close_pop_up()
    async def active(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус активности.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = normalize_int(
                value or await self.driver.execute_locator(self.locator.active) or 1
            )
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `active`", exc_info=ex)
            return False

        if not value:
            logger.debug(f"Невалидный результат {value=}\nлокатор {self.locator.active}")
            return False

        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает дополнительное время доставки.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.additional_delivery_times
            ) or ''
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `additional_delivery_times`", exc_info=ex
            )
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\nлокатор {self.locator.additional_delivery_times}"
            )
            return False

        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус расширенного управления запасами.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.advanced_stock_management
            ) or ''
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `advanced_stock_management`", exc_info=ex
            )
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\nлокатор {self.locator.advanced_stock_management}"
            )
            return False

        self.fields.advanced_stock_management = value
        return True

    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает короткую партнерскую ссылку.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.affiliate_short_link = (
                value
                or await self.driver.execute_locator(self.locator.affiliate_short_link)
                or ''
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_short_link`", exc_info=ex)
            return False

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает партнерское описание.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.affiliate_summary = normalize_string(
                value or await self.driver.execute_locator(self.locator.affiliate_summary) or ''
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary`", exc_info=ex)
            return False

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None) -> bool:
        """
         Извлекает и устанавливает дополнительное партнерское описание.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.affiliate_summary_2
            ) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary_2`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\nлокатор {self.locator.affiliate_summary_2}"
            )
            return False

        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None) -> bool:
        """
         Извлекает и устанавливает партнерский текст.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_text`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\nлокатор {self.locator.affiliate_text}"
            )
            return False

        self.fields.affiliate_text = value
        return True

    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает большую партнерскую картинку.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.affiliate_image_large = (
                value
                or await self.driver.execute_locator(self.locator.affiliate_image_large)
                or ''
            )
            return True
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `affiliate_image_large`", exc_info=ex
            )
            return False

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает среднюю партнерскую картинку.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            locator_result = (
                value
                or await self.driver.execute_locator(self.locator.affiliate_image_medium)
                or ''
            )
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `affiliate_image_medium`", exc_info=ex
            )
            return False

        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return False

        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает маленькую партнерскую картинку.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            locator_result = (
                value
                or await self.driver.execute_locator(self.locator.affiliate_image_small)
                or ''
            )
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `affiliate_image_small`", exc_info=ex
            )
            return False

        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return False

        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает доступную дату.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            locator_result = (
                value or await self.driver.execute_locator(self.locator.available_date) or ''
            )
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_date`", exc_info=ex)
            return False

        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            return False

        self.fields.available_date = locator_result
        return True

    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности для заказа.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.available_for_order
            ) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_for_order`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.available_for_order}"
            )
            return False

        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности позже.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_later`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.available_later}"
            )
            return False

        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доступности сейчас.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_now`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.available_now}"
            )
            return False

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
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает атрибут кэша по умолчанию.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.cache_default_attribute
            ) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_default_attribute`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.cache_default_attribute}"
            )
            return False

        self.fields.cache_default_attribute = value
        return True

    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None) -> bool:
        """
         Извлекает и устанавливает статус наличия вложений в кэше.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(
                self.locator.cache_has_attachments
            ) or ''
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `cache_has_attachments`", exc_info=ex
            )
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.cache_has_attachments}"
            )
            return False

        self.fields.cache_has_attachments = value
        return True

    @close_pop_up()
    async def cache_is_pack(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус "является ли набор" в кэше.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.cache_is_pack) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_is_pack`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.cache_is_pack}"
            )
            return False

        self.fields.cache_is_pack = value
        return True

    @close_pop_up()
    async def condition(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает условие товара.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.condition) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `condition`", exc_info=ex)
            return False

        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.condition}")
            return False

        self.fields.condition = value
        return True

    @close_pop_up()
    async def customizable(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус "настраиваемый".

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = value or await self.driver.execute_locator(self.locator.customizable) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `customizable`", exc_info=ex)
            return False

        if not value:
            logger.debug(
                f"Невалидный результат {value=}\\nлокатор {self.locator.customizable}"
            )
            return False

        self.fields.customizable = value
        return True

    @close_pop_up()
    async def date_add(self, value: Optional[str | datetime.date] = None) -> bool:
        """
         Извлекает и устанавливает дату добавления.

        :param value: Значение для установки.
        :type value: str | datetime.date, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.date_add = normalize_sql_date(
                value or await self.driver.execute_locator(self.locator.date_add) or gs.now
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `date_add`", exc_info=ex)
            return False

    @close_pop_up()
    async def date_upd(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает дату обновления.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.date_upd = normalize_sql_date(
                value or await self.driver.execute_locator(self.locator.date_upd) or gs.now
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `date_upd`", exc_info=ex)
            return False

    @close_pop_up()
    async def delivery_out_stock(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает статус доставки при отсутствии на складе.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.delivery_out_stock = normalize_string(
                value or await self.driver.execute_locator(self.locator.delivery_out_stock) or ''
            )
            return True
        except Exception as ex:
            logger.error(
                f"Ошибка получения значения в поле `delivery_out_stock`", exc_info=ex
            )
            return False

    @close_pop_up()
    async def depth(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает глубину товара.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            self.fields.depth = normalize_float(
                value or await self.driver.execute_locator(self.locator.depth) or ''
            )
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `depth`", exc_info=ex)
            return False

    @close_pop_up()
    async def description(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает описание товара.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        if value:
            self.fields.description = value
            return True
        try:
            raw_value = await self.driver.execute_locator(self.locator.description)
            self.fields.description = normalize_string(raw_value)
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `description` \n {pprint(raw_value)}", exc_info=ex)
            return False

    @close_pop_up()
    async def description_short(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает краткое описание товара.

        :param value: Значение для установки.
        :type value: Any, optional
        :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        try:
            value = normalize_string(
                value or await self.driver.execute_locator(self.locator.description_short) or ''
            )
            if value:
                self.fields.description_short = value
                return True
            return False
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `description_short`", exc_info=ex)
            return False

        self.fields.description_short = value
        return True

    @close_pop_up()
    async def id_category_default(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает ID категории по умолчанию.

        :param value: Значение для установки.
        :type value: Any, optional
         :return: True, если значение успешно установлено, иначе False.
        :rtype: bool
        """
        self.fields.id_category_default = value
        return True

    @close_pop_up()
    async def id_default_combination(self, value: Optional[Any] = None) -> bool:
        """
        Извлекает и устанавливает ID комбинации по умолчанию.

        :param value: Значение для установки.
        :type value