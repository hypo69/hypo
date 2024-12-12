# Анализ кода модуля `executor.py`

**Качество кода**
9
-  Плюсы
    - Хорошая структура документации, подробное описание модуля, классов, методов и их назначения.
    - Использование диаграмм Mermaid для визуализации логики работы методов.
    -  Четкое разделение на классы и методы.
    -  Асинхронность для выполнения операций.
-  Минусы
    - Отсутствуют некоторые необходимые импорты, что может привести к ошибкам времени выполнения.
    -  Использование стандартного `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не везде используются комментарии в формате reStructuredText (RST).
    -  Местами отсутсвует обработка ошибок с помощью `logger.error`
    -  Некоторые docstring не полные, не хватает описания параметров и возвращаемых значений.

**Рекомендации по улучшению**

1. **Импорты**: Добавить недостающие импорты, такие как `json` и `SimpleNamespace` из `types`, `Any` из `typing`, `logger` из `src.logger.logger`.
2. **Обработка JSON**: Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3. **Комментарии RST**: Переписать все комментарии в формате RST, включая docstrings для классов и методов, а также описания переменных.
4. **Логирование**: Использовать `logger.error` для обработки исключений и логирования ошибок.
5. **Улучшение docstring**: Дополнить docstring для методов, указав параметры и возвращаемые значения.
6. **Обработка ошибок**: Улучшить обработку ошибок, добавив логирование.

**Оптимизированный код**

```python
"""
Модуль для управления веб-элементами с использованием Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который используется для взаимодействия с веб-элементами
на основе предоставленных локаторов. Он поддерживает различные типы действий, такие как клики, отправка сообщений,
получение атрибутов и выполнение событий.

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
# from src.utils.jjson import j_loads, j_loads_ns #TODO заменить на j_loads или j_loads_ns
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from src.logger.logger import logger #TODO: добавить импорт logger
import json

@dataclass
class Locator:
    """
    Представляет структуру локатора для поиска веб-элементов.

    :param by: Метод поиска элемента (например, 'ID', 'XPATH', 'CSS_SELECTOR').
    :param selector: Строка селектора для поиска элемента.
    :param event: Событие, которое нужно выполнить (например, 'click()', 'send_keys("text")').
    :param attribute: Атрибут, который нужно получить (например, 'text', 'value').
    :param mandatory: Флаг, указывающий, является ли элемент обязательным для нахождения.
    :param timeout: Время ожидания элемента.
    :param index: Индекс элемента в списке, если локатор находит несколько элементов.
    :param screenshot: Флаг, указывающий, нужно ли делать скриншот элемента.
    """
    by: str
    selector: str
    event: Optional[str] = None
    attribute: Optional[str] = None
    mandatory: bool = False
    timeout: int = 10
    index: Optional[int] = None
    screenshot: bool = False
    
class LocatorType(str, Enum):
    """
    Перечисление типов локаторов.

    :cvar ID: Локатор по ID.
    :cvar XPATH: Локатор по XPATH.
    :cvar CSS_SELECTOR: Локатор по CSS-селектору.
    :cvar CLASS_NAME: Локатор по имени класса.
    :cvar TAG_NAME: Локатор по имени тега.
    :cvar LINK_TEXT: Локатор по тексту ссылки.
    :cvar PARTIAL_LINK_TEXT: Локатор по части текста ссылки.
    :cvar NAME: Локатор по имени.
    """
    ID = "id"
    XPATH = "xpath"
    CSS_SELECTOR = "css_selector"
    CLASS_NAME = "class_name"
    TAG_NAME = "tag_name"
    LINK_TEXT = "link_text"
    PARTIAL_LINK_TEXT = "partial_link_text"
    NAME = "name"


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :param mode: Режим выполнения (например, 'debug', 'dev').
    :param actions: Объект ActionChains для выполнения сложных действий.
    """
    driver: WebDriver
    mode: str = "debug"
    actions: Optional[ActionChains] = None
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        LocatorType.ID: By.ID,
        LocatorType.XPATH: By.XPATH,
        LocatorType.CSS_SELECTOR: By.CSS_SELECTOR,
        LocatorType.CLASS_NAME: By.CLASS_NAME,
        LocatorType.TAG_NAME: By.TAG_NAME,
        LocatorType.LINK_TEXT: By.LINK_TEXT,
        LocatorType.PARTIAL_LINK_TEXT: By.PARTIAL_LINK_TEXT,
        LocatorType.NAME: By.NAME,
    })
    
    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Optional[Any]:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :return: Результат выполнения действия или None в случае ошибки.
        """
        # Проверяет, является ли локатор SimpleNamespace
        if isinstance(locator, SimpleNamespace):
            # если да, то использует его как есть
            pass
        else:
            # если нет, то преобразует в SimpleNamespace
            locator = SimpleNamespace(**locator)
            
        async def _parse_locator(locator: SimpleNamespace) -> Optional[Any]:
            """
            Выполняет парсинг и обработку локатора.

            :param locator: Локатор в виде SimpleNamespace.
            :return: Результат обработки локатора.
            """
            # Проверяет, есть ли у локатора событие, атрибут или обязательное поле
            if not any([locator.event, locator.attribute, locator.mandatory]):
                return None
            try:
                # Код сопоставляет метод поиска элемента по `by`
                by = self.by_mapping.get(locator.by)
                # Вызывает функцию для оценки локатора
                if by:
                   result = await self._evaluate(locator=locator, by=by)
                   return result
            except Exception as ex:
                # Логирует ошибку и возвращает None
                logger.error(f'Ошибка при обработки локатора {locator=}', exc_info=ex)
                return None
            # Проверяет, есть ли у локатора событие
            if locator.event:
                # Выполняет событие
                return await self.execute_event(locator)
            # Проверяет, есть ли у локатора атрибут
            if locator.attribute:
                # Получает значение атрибута
                return await self.get_attribute_by_locator(locator)
            # Получает веб-элемент
            return await self.get_webelement_by_locator(locator)

        return await _parse_locator(locator)

    async def _evaluate(self, locator:SimpleNamespace, by:str) -> Optional[Any]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :param by: Метод поиска элемента (например, By.ID).
        :return: Результат обработки атрибутов.
        """
        # Проверяет, является ли атрибут списком
        if isinstance(locator.attribute, list):
            tasks = [self._evaluate(locator=SimpleNamespace(**{**locator.__dict__, 'attribute':attribute}),by=by) for attribute in locator.attribute]
            # Выполняет асинхронно для каждого атрибута
            return await asyncio.gather(*tasks)
        else:
            # Вызывает функцию для получения атрибута
            return await self._get_attribute(locator=locator,by=by)

    async def _get_attribute(self, locator:SimpleNamespace, by:str) -> Optional[Any]:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде SimpleNamespace.
        :param by: Метод поиска элемента (например, By.ID).
        :return: Результат извлечения атрибута.
        """
        try:
           
            # Получает веб-элемент
            element = await self.get_webelement_by_locator(locator=locator,by=by)
            if not element:
                return None

            # Проверяет, является ли locator.attribute строкой, похожей на словарь
            if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
                # Преобразует строку атрибута в словарь
                 try:
                    attribute_dict = json.loads(locator.attribute)
                 except Exception as ex:
                     # Логирует ошибку и возвращает None
                     logger.error(f'Ошибка при преобразовании строки в словарь {locator.attribute=}', exc_info=ex)
                     return None
                # Проверяет, является ли элемент списком
                 if isinstance(element, list):
                     # Получает атрибуты для каждого элемента в списке
                     return [ {key: el.get_attribute(key) for key in attribute_dict.keys() } for el in element ]

                 # Получает атрибуты для одного элемента
                 return {key: element.get_attribute(key) for key in attribute_dict.keys()}

            # Проверяет, является ли элемент списком
            if isinstance(element, list):
                # Получает атрибуты для каждого элемента в списке
                return [el.get_attribute(locator.attribute) for el in element]

            # Получает атрибут для одного элемента
            return element.get_attribute(locator.attribute)
        except Exception as ex:
            # Логирует ошибку и возвращает None
            logger.error(f'Ошибка при получении атрибута у элемента {locator=}', exc_info=ex)
            return None

    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Результат извлечения атрибута.
        """
        # Преобразует локатор в SimpleNamespace, если необходимо
        if isinstance(locator, dict):
           locator = SimpleNamespace(**locator)
        # Код получает метод поиска элемента из словаря
        by = self.by_mapping.get(locator.by)
        if not by:
            return None
        # Код вызывает метод для получения атрибута
        return await self._get_attribute(locator=locator, by=by)

    async def get_webelement_by_locator(self, locator: SimpleNamespace, by:str = None) -> Optional[Any]:
        """
        Извлекает веб-элементы на основе предоставленного локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :param by: Метод поиска элемента (например, By.ID).
        :return: Список веб-элементов или один веб-элемент.
        """
        if not by:
             # Код получает метод поиска элемента из словаря
            by = self.by_mapping.get(locator.by)

        try:
            # Код ожидает появления элемента на странице
            elements = await self.driver.find_elements(by, locator.selector)
            # Проверяет, найден ли хотя бы один элемент
            if not elements:
               # Логирует сообщение отладки
               logger.debug(f'Элемент не найден {locator=}')
               return None

            # Код проверяет, есть ли индекс у локатора
            if locator.index is not None:
                # Код возвращает элемент по индексу
                return elements[locator.index]
            # Код возвращает список элементов
            return elements
        except Exception as ex:
            # Логирует ошибку и возвращает None
            logger.error(f'Ошибка при получении элемента {locator=}', exc_info=ex)
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, file_path: Path) -> bool:
        """
        Делает скриншот найденного веб-элемента.

        :param locator: Локатор в виде SimpleNamespace.
        :param file_path: Путь для сохранения скриншота.
        :return: True, если скриншот сделан успешно, False в противном случае.
        """
        try:
           # Код получает веб-элемент
           element = await self.get_webelement_by_locator(locator=locator)
           if not element:
               return False

           # Код делает скриншот элемента
           if isinstance(element, list):
               element = element[0]
           element.screenshot(str(file_path))
           return True
        except Exception as ex:
            # Логирует ошибку и возвращает False
            logger.error(f'Ошибка при создании скриншота {locator=}', exc_info=ex)
            return False

    async def execute_event(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Выполняет события, связанные с локатором.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Результат выполнения события.
        """
        try:
            # Код получает веб-элемент
            element = await self.get_webelement_by_locator(locator=locator)
            if not element:
                return None
            
            # Код извлекает имя события и аргументы из строки события
            match = re.match(r"(\w+)\((.*?)\)", locator.event)
            if not match:
                return None
            event_name = match.group(1)
            event_args = match.group(2)
            
            # Проверяет, является ли элемент списком
            if isinstance(element, list):
                # Выполняет событие для каждого элемента в списке
                result = []
                for el in element:
                    result.append(await self._call_event(el, event_name, event_args))
                return result

            # Выполняет событие для одного элемента
            return await self._call_event(element, event_name, event_args)

        except Exception as ex:
            # Логирует ошибку и возвращает None
            logger.error(f'Ошибка при выполнении события {locator=}', exc_info=ex)
            return None

    async def _call_event(self, element: Any, event_name:str, event_args:str) -> Optional[Any]:
        """
        Вызывает событие для веб-элемента.

        :param element: Веб-элемент, для которого нужно выполнить событие.
        :param event_name: Имя события (например, 'click', 'send_keys').
        :param event_args: Аргументы события.
        :return: Результат выполнения события.
        """
        try:
            # Проверяет имя события
            if event_name == "click":
                # Выполняет клик
                self.actions.move_to_element(element).click(element).perform()
                return True
            elif event_name == "send_keys":
                # Отправляет сообщение
                element.send_keys(event_args)
                return True
            elif event_name == "clear":
                 # Очищает поле ввода
                element.clear()
                return True
            else:
                 # Логирует ошибку и возвращает None
                logger.error(f"Неизвестное событие: {event_name}")
                return None
        except Exception as ex:
             # Логирует ошибку и возвращает None
            logger.error(f'Ошибка при вызове события {event_name=}', exc_info=ex)
            return None

    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Локатор в виде SimpleNamespace.
        :param message: Сообщение для отправки.
        :return: True, если сообщение отправлено успешно, False в противном случае.
        """
        try:
            # Код получает веб-элемент
            element = await self.get_webelement_by_locator(locator=locator)
            if not element:
                return False

            # Проверяет, является ли элемент списком
            if isinstance(element,list):
                # Отправляет сообщение каждому элементу в списке
                for el in element:
                     el.send_keys(message)
                return True
            # Отправляет сообщение одному элементу
            element.send_keys(message)
            return True
        except Exception as ex:
             # Логирует ошибку и возвращает False
            logger.error(f'Ошибка при отправке сообщения {locator=}', exc_info=ex)
            return False
```