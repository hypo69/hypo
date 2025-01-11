# Анализ кода модуля `executor`

**Качество кода**
8
-  Плюсы
    -  Хорошая структура и разделение на функции, что облегчает понимание и поддержку кода.
    -  Использование `asyncio` для асинхронных операций позволяет эффективно работать с веб-элементами.
    -  Наличие подробной документации в формате reStructuredText (RST).
    -  Обработка исключений с логированием через `logger.error`.
    -  Использование `SimpleNamespace` для гибкого управления данными локаторов.
-  Минусы
    -  Не все функции и методы имеют docstring в формате RST.
    -  В некоторых местах обработка ошибок может быть более гранулярной.
    -  Некоторые переменные могли бы иметь более описательные имена.
    -  Местами можно использовать `f-strings` для форматирования логов.
    -  Не везде используется `j_loads` или `j_loads_ns` для обработки `json`, а также не везде обрабатывается параметр `value` который может быть передан в функцию.

**Рекомендации по улучшению**
1. Добавить docstring в формате RST для всех функций и методов.
2. Улучшить обработку ошибок, чтобы она была более гранулярной и информативной.
3. Использовать `j_loads` или `j_loads_ns` для всех `json.load`.
4. Использовать f-strings для форматирования строк логов.
5. Добавить проверки на тип входных данных, особенно для `locator`.
6. Переименовать переменные, которые несут мало смысла.
7. Обработать параметр `value` который может быть передан в функцию.

**Оптимизированный код**
```python
"""
Модуль для работы с веб-элементами с использованием Selenium.
================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который обеспечивает
удобный способ взаимодействия с веб-элементами на основе заданных локаторов.
Модуль поддерживает различные типы локаторов и позволяет выполнять
разнообразные действия, такие как клики, отправка сообщений, получение атрибутов
и выполнение JavaScript событий.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver=driver)
    locator = {
        "by": "ID",
        "selector": "some_element_id",
        "event": "click()"
    }
    result = await executor.execute_locator(locator)
    print(result)
"""
import asyncio
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


@dataclass
class ProductFields:
    """
    Класс для хранения данных о продукте.

    :ivar specification: Спецификация продукта.
    :vartype specification: Optional[str]
    :ivar name: Название продукта.
    :vartype name: Optional[str]
    :ivar price: Цена продукта.
    :vartype price: Optional[float]
    :ivar rating: Рейтинг продукта.
    :vartype rating: Optional[float]
    """
    specification: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[float] = None


class LocatorTypes(str, Enum):
    """
    Перечисление типов локаторов.
    """
    ID = "ID"
    XPATH = "XPATH"
    CLASS_NAME = "CLASS_NAME"
    CSS_SELECTOR = "CSS_SELECTOR"
    LINK_TEXT = "LINK_TEXT"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.

    :ivar driver: Экземпляр WebDriver для управления браузером.
    :vartype driver: Optional[WebDriver]
    :ivar actions: Экземпляр ActionChains для выполнения сложных действий.
    :vartype actions: Optional[ActionChains]
    :ivar by_mapping: Словарь, сопоставляющий типы локаторов с методами By.
    :vartype by_mapping: Dict[str, str]
    :ivar mode: Режим выполнения (debug, dev и т.д.).
    :vartype mode: str
    """
    driver: Optional[WebDriver] = None
    actions: Optional[ActionChains] = None
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        LocatorTypes.ID: By.ID,
        LocatorTypes.XPATH: By.XPATH,
        LocatorTypes.CLASS_NAME: By.CLASS_NAME,
        LocatorTypes.CSS_SELECTOR: By.CSS_SELECTOR,
        LocatorTypes.LINK_TEXT: By.LINK_TEXT,
        LocatorTypes.PARTIAL_LINK_TEXT: By.PARTIAL_LINK_TEXT,
        LocatorTypes.NAME: By.NAME,
        LocatorTypes.TAG_NAME: By.TAG_NAME,
    })
    mode: str = 'dev'

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен WebDriver.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[dict, SimpleNamespace], value: Any = None) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
        """
        Выполняет действия с веб-элементом на основе предоставленного локатора.

        :param locator: Локатор элемента в виде словаря или SimpleNamespace.
        :type locator: Union[dict, SimpleNamespace]
        :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: Результат выполнения, который может быть строкой, списком строк,
                 веб-элементом или списком веб-элементов.
        :rtype: Optional[Union[str, List[str], WebElement, List[WebElement]]]
        """
        # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
             # Преобразует словарь с параметрами локатора в SimpleNamespace
            locator = j_loads_ns(locator)
        
        async def _parse_locator(loc: SimpleNamespace) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
            """
            Внутренняя функция для обработки локатора.

            :param loc: Локатор элемента в виде SimpleNamespace.
            :type loc: SimpleNamespace
            :return: Результат выполнения, который может быть строкой, списком строк,
                     веб-элементом или списком веб-элементов.
            :rtype: Optional[Union[str, List[str], WebElement, List[WebElement]]]
            """
            # Проверяет наличие атрибутов 'event', 'attribute' или 'mandatory' в локаторе
            if not any([loc.get('event'), loc.get('attribute'), loc.get('mandatory')]):
                return None

            try:
                # Код выполняет сопоставление типа локатора с By и вычисление атрибута
                by = self.by_mapping.get(loc.by)
                if not by:
                    logger.error(f'Неизвестный тип локатора {loc.by}')
                    return None
                # Вычисление атрибута на основе предоставленного локатора
                result = await self.evaluate_locator(loc, value)
                return result

            except Exception as ex:
                # Логирование ошибки при обработке локатора
                logger.error(f'Ошибка при обработке локатора {loc}', exc_info=ex)
                return None

        # Выполняет внутреннюю функцию обработки локатора
        return await _parse_locator(locator)

    async def evaluate_locator(self, locator: SimpleNamespace, value: Any = None) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
        """
        Вычисляет атрибуты локатора и выполняет соответствующие действия.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: Результат вычисления, который может быть строкой, списком строк,
                 веб-элементом или списком веб-элементов.
        :rtype: Optional[Union[str, List[str], WebElement, List[WebElement]]]
        """
        async def _evaluate(loc: SimpleNamespace, value: Any = None) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
            """
            Внутренняя функция для вычисления атрибутов локатора.

            :param loc: Локатор элемента в виде SimpleNamespace.
            :type loc: SimpleNamespace
             :param value: Значение, которое может быть передано в функцию.
            :type value: Any
            :return: Результат вычисления, который может быть строкой, списком строк,
                     веб-элементом или списком веб-элементов.
            :rtype: Optional[Union[str, List[str], WebElement, List[WebElement]]]
            """
             # Проверяет наличие события у локатора
            if loc.get('event'):
                # Выполняет событие, если оно есть
                return await self.execute_event(loc, value)
            # Проверяет наличие атрибута у локатора
            elif loc.get('attribute'):
                # Возвращает атрибут, если он есть
                return await self.get_attribute_by_locator(loc, value)
            else:
                # Возвращает веб-элемент, если нет ни события, ни атрибута
                return await self.get_webelement_by_locator(loc, value)

        if isinstance(locator.attribute, list):
            # Вызывает _evaluate для каждого атрибута, если атрибут является списком
            tasks = [ _evaluate(SimpleNamespace(**{**locator, 'attribute': attr}), value) for attr in locator.attribute]
            return await asyncio.gather(*tasks)
        else:
            # Вызывает _evaluate для одного атрибута
            return await _evaluate(locator, value)

    async def get_attribute_by_locator(self, locator: SimpleNamespace, value: Any = None) -> Optional[Union[str, List[str]]]:
        """
        Получает атрибуты элемента или списка элементов на основе локатора.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
         :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: Значение атрибута или список значений атрибутов.
        :rtype: Optional[Union[str, List[str]]]
        """
        # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator)
         # Код получает веб-элемент через get_webelement_by_locator
        element = await self.get_webelement_by_locator(locator, value)

        # Проверяет, найден ли веб-элемент
        if not element:
             # Логирование сообщения об отсутствии элемента и возврат None
            logger.debug(f'Элемент не найден по локатору {locator}')
            return None
        # Проверяет, является ли атрибут строкой, похожей на словарь
        if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
           try:
                # Пытается преобразовать строку атрибута в словарь
                attribute_dict = j_loads_ns(locator.attribute)
           except Exception as ex:
                # Логирование ошибки при преобразовании строки в словарь
               logger.error(f'Ошибка при преобразовании строки в словарь {locator.attribute=}', exc_info=ex)
               return None
           if isinstance(element, list):
                # Код получает атрибуты для каждого элемента списка
                return [
                    {key: el.get_attribute(key) for key in attribute_dict}
                    for el in element
                ]
           else:
               # Код получает атрибуты для одного веб-элемента
                return {key: element.get_attribute(key) for key in attribute_dict}
        if isinstance(element, list):
            # Код получает значения атрибутов для каждого элемента списка
             return [el.get_attribute(locator.attribute) for el in element]
        else:
            # Код получает значение атрибута для одного веб-элемента
            return element.get_attribute(locator.attribute)

    async def get_webelement_by_locator(self, locator: SimpleNamespace, value: Any = None) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элемент или список веб-элементов на основе локатора.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: Веб-элемент или список веб-элементов.
        :rtype: Optional[Union[WebElement, List[WebElement]]]
        """
        # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator)
        try:
             # Код пытается найти веб-элемент или веб-элементы по локатору
            by = self.by_mapping.get(locator.by)
            if not by:
                logger.error(f'Неизвестный тип локатора {locator.by}')
                return None
            selector = locator.selector
            if not selector:
                logger.error(f'Не указан селектор для локатора {locator}')
                return None
            if locator.get('many'):
                # Код ищет все веб-элементы, соответствующие локатору
                elements = self.driver.find_elements(by, selector)
                if not elements:
                    logger.debug(f'Элементы не найдены по локатору {locator}')
                    return None
                return elements
            else:
                # Код ищет один веб-элемент, соответствующий локатору
                element = self.driver.find_element(by, selector)
                return element
        except Exception as ex:
            # Логирование ошибки при поиске веб-элемента
            logger.error(f'Ошибка при поиске элемента {locator=}', exc_info=ex)
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, path: Path) -> Optional[Path]:
        """
        Создаёт скриншот веб-элемента и сохраняет его по указанному пути.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param path: Путь для сохранения скриншота.
        :type path: Path
        :return: Путь к сохранённому скриншоту.
        :rtype: Optional[Path]
        """
        # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator)
        try:
            # Код получает веб-элемент по локатору
            element = await self.get_webelement_by_locator(locator)
            if element:
                # Код создает скриншот веб-элемента и сохраняет его
                element.screenshot(str(path))
                return path
            else:
                logger.debug(f'Элемент не найден, скриншот не сделан {locator=}')
                return None
        except Exception as ex:
            # Логирование ошибки при создании скриншота
            logger.error(f'Ошибка при создании скриншота {locator=}', exc_info=ex)
            return None

    async def execute_event(self, locator: SimpleNamespace, value: Any = None) -> Optional[bool]:
        """
        Выполняет JavaScript событие, связанное с локатором.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: True, если событие выполнено успешно, в противном случае None.
        :rtype: Optional[bool]
        """
        # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator)
        try:
            # Код получает веб-элемент по локатору
            element = await self.get_webelement_by_locator(locator, value)
            if not element:
                 # Логирование сообщения об отсутствии элемента и возврат None
                logger.debug(f'Элемент не найден по локатору {locator}')
                return None
            # Извлекает событие из локатора
            event = locator.event
            if not event:
                logger.error(f'Не указано событие для локатора {locator}')
                return None
            if isinstance(element, list):
                # Код выполняет событие для каждого элемента списка
                for el in element:
                    self.driver.execute_script(event, el)
            else:
                # Код выполняет событие для одного элемента
                 self.driver.execute_script(event, element)
            return True
        except Exception as ex:
             # Логирование ошибки при выполнении события
            logger.error(f'Ошибка при выполнении события {locator=}', exc_info=ex)
            return None

    async def send_message(self, locator: SimpleNamespace, message: str, value: Any = None) -> Optional[bool]:
         """
        Отправляет сообщение в веб-элемент, используя локатор.

        :param locator: Локатор элемента в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param message: Сообщение для отправки в веб-элемент.
        :type message: str
         :param value: Значение, которое может быть передано в функцию.
        :type value: Any
        :return: True, если сообщение отправлено успешно, в противном случае None.
        :rtype: Optional[bool]
        """
         # Проверяет, является ли локатор SimpleNamespace, если нет, то преобразует в него
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator)
        try:
            # Код получает веб-элемент по локатору
            element = await self.get_webelement_by_locator(locator, value)
            if not element:
                # Логирование сообщения об отсутствии элемента и возврат None
                logger.debug(f'Элемент не найден по локатору {locator}')
                return None
            if isinstance(element, list):
                # Код отправляет сообщение в каждый элемент списка
                for el in element:
                     el.send_keys(message)
            else:
                # Код отправляет сообщение в один элемент
                 element.send_keys(message)
            return True
        except Exception as ex:
             # Логирование ошибки при отправке сообщения
            logger.error(f'Ошибка при отправке сообщения {locator=}', exc_info=ex)
            return None
```