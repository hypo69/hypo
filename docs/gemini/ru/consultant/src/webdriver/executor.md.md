# Improved Code

```python
"""
Модуль для выполнения действий с веб-элементами с использованием Selenium.
===========================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который используется для поиска,
взаимодействия и извлечения информации из веб-элементов на основе заданных локаторов.

Он поддерживает различные типы локаторов, действия с элементами, обработку ошибок и многое другое.

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

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

@dataclass
class Locator:
    """
    Представляет локатор веб-элемента.

    :param by: Тип локатора (например, 'ID', 'XPATH', 'CSS_SELECTOR').
    :param selector: Значение локатора.
    :param event: Событие для выполнения (например, 'click()', 'send_keys("text")').
    :param attribute: Атрибут для получения (например, 'value', 'text').
    :param mandatory: Флаг, указывающий, является ли элемент обязательным.
    :param many: Флаг, указывающий, нужно ли получить несколько элементов.
    :param name: Имя локатора для отладки.
    """
    by: str
    selector: str
    event: Optional[str] = None
    attribute: Optional[str] = None
    mandatory: bool = True
    many: bool = False
    name: Optional[str] = None


class LocatorError(Exception):
    """
    Исключение, выбрасываемое при ошибке в работе с локатором.
    """
    pass


class EventType(str, Enum):
    """
    Перечисление типов событий, которые можно выполнить с веб-элементом.
    """
    CLICK = 'click()'
    SEND_KEYS = 'send_keys'
    SCROLL_INTO_VIEW = 'scroll_into_view()'
    CLEAR = 'clear()'
    HOVER = 'hover()'


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :param actions: Объект ActionChains для выполнения сложных действий.
    :param by_mapping: Словарь, сопоставляющий типы локаторов с методами `By`.
    :param mode: Режим выполнения (например, 'debug', 'dev').
    """
    driver: WebDriver
    actions: ActionChains = field(init=False)
    by_mapping: Dict[str, str] = field(
        default_factory=lambda: {
            'ID': By.ID,
            'XPATH': By.XPATH,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'CLASS_NAME': By.CLASS_NAME,
            'TAG_NAME': By.TAG_NAME,
            'LINK_TEXT': By.LINK_TEXT,
            'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
            'NAME': By.NAME
        }
    )
    mode: str = 'debug'


    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)


    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Optional[Any]:
        """
        Выполняет действие с веб-элементом на основе предоставленного локатора.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :return: Результат выполнения действия с элементом.
        """
        # Проверяет тип локатора и преобразовывает его в SimpleNamespace при необходимости
        if isinstance(locator, dict):
           locator = SimpleNamespace(**locator)

        # Определение внутренней асинхронной функции для обработки локатора
        async def _parse_locator(locator: SimpleNamespace) -> Optional[Any]:
            """
            Внутренняя асинхронная функция для обработки локатора.

            :param locator: Локатор в виде SimpleNamespace.
            :return: Результат обработки локатора.
            """
            if not any([locator.event, locator.attribute, locator.mandatory]):
                return None
            try:
                # Пытается получить веб-элемент или атрибут по локатору, обрабатывая ошибки
                web_element = await self._evaluate(locator)
                if locator.event:
                    # Выполняет событие, если оно определено
                    return await self.execute_event(locator, web_element)
                if locator.attribute:
                    # Возвращает атрибут элемента, если он определен
                    return await self.get_attribute_by_locator(locator, web_element)
                # Возвращает веб-элемент, если не определено ни событие ни атрибут
                return web_element
            except Exception as ex:
                logger.error(f'Ошибка при выполнении локатора {locator=}', ex)
                ...  # Точка остановки для отладки
                return None

        # Вызывает внутреннюю функцию обработки и возвращает результат
        return await _parse_locator(locator)



    async def _evaluate(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Результат обработки атрибутов.
        """
        if isinstance(locator.attribute, list):
            # Если атрибут - список, обрабатывает каждый атрибут и возвращает результаты
            tasks = [self._evaluate(SimpleNamespace(**{**locator.__dict__, 'attribute': attr}))
                     for attr in locator.attribute]
            return await asyncio.gather(*tasks)

        # Если атрибут не список, получает веб-элемент по локатору
        return await self.get_webelement_by_locator(locator)

    async def get_attribute_by_locator(self, locator: SimpleNamespace, web_element: Any = None) -> Optional[Any]:
        """
        Возвращает атрибут элемента или список атрибутов элементов, найденных по локатору.

        :param locator: Локатор в виде SimpleNamespace.
        :param web_element: Веб-элемент, для которого нужно получить атрибут.
        :return: Атрибут элемента или список атрибутов элементов.
        """
        # Приводит локатор к SimpleNamespace если это словарь
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        # Если веб-элемент не передан, получает его по локатору
        if not web_element:
            web_element = await self.get_webelement_by_locator(locator)

        # Проверяет, был ли найден веб-элемент
        if not web_element:
            logger.debug(f'Не удалось получить элемент по локатору {locator}')
            return None


        if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
            try:
                attribute_dict = j_loads_ns(locator.attribute)
                # Получает атрибуты для каждого веб-элемента если их список
                if isinstance(web_element, list):
                    return [
                        {key: el.get_attribute(value) for key, value in attribute_dict.items()}
                        for el in web_element
                    ]
                # Получает атрибуты для одного веб-элемента
                return {key: web_element.get_attribute(value) for key, value in attribute_dict.items()}
            except Exception as ex:
                logger.error(f'Ошибка при парсинге атрибута {locator.attribute}', ex)
                ...
                return None
        # Получает атрибуты для каждого веб-элемента если их список
        if isinstance(web_element, list):
            return [el.get_attribute(locator.attribute) for el in web_element]

        # Получает атрибут для одного веб-элемента
        return web_element.get_attribute(locator.attribute)


    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Извлекает веб-элемент(ы) на основе предоставленного локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Веб-элемент или список веб-элементов, или None если не найдены.
        """
        try:
            by = self.by_mapping.get(locator.by)
            if not by:
                logger.error(f'Неверный тип локатора {locator.by}')
                return None
            # Если требуется несколько элементов, находит их все
            if locator.many:
                elements = self.driver.find_elements(by, locator.selector)
                if not elements and locator.mandatory:
                    logger.debug(f'Не найдены элементы по локатору {locator}')
                    return None
                return elements
            # Иначе, находит один элемент
            element = self.driver.find_element(by, locator.selector)
            return element
        except Exception as ex:
             if locator.mandatory:
                logger.error(f'Не удалось найти элемент по локатору {locator}', ex)
                ... # Точка остановки для отладки
             else:
                logger.debug(f'Не удалось найти элемент по не обязательному локатору {locator}')
             return None


    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, save_path: str) -> bool:
        """
        Делает скриншот веб-элемента.

        :param locator: Локатор веб-элемента в виде SimpleNamespace.
        :param save_path: Путь для сохранения скриншота.
        :return: True если скриншот успешен, False в противном случае.
        """
        try:
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            element.screenshot(save_path)
            return True
        except Exception as ex:
            logger.error(f'Не удалось сделать скриншот элемента по локатору {locator}', ex)
            return False


    async def execute_event(self, locator: SimpleNamespace, element: Any) -> bool:
        """
        Выполняет событие, связанное с локатором.

        :param locator: Локатор в виде SimpleNamespace.
        :param element: Веб-элемент, с которым нужно выполнить событие.
        :return: True, если событие выполнено успешно, False в противном случае.
        """
        try:
            event = locator.event
            if event == EventType.CLICK:
                self.actions.click(element).perform()
            elif event.startswith(EventType.SEND_KEYS):
                keys = re.search(r'\((.*?)\)', event).group(1).strip("'").strip('"')
                self.actions.send_keys_to_element(element, keys).perform()
            elif event == EventType.SCROLL_INTO_VIEW:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
            elif event == EventType.CLEAR:
                 element.clear()
            elif event == EventType.HOVER:
                 self.actions.move_to_element(element).perform()
            return True
        except Exception as ex:
            logger.error(f'Не удалось выполнить событие {locator.event} для элемента {element}', ex)
            return False


    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Локатор веб-элемента в виде SimpleNamespace.
        :param message: Сообщение для отправки.
        :return: True если сообщение отправлено, False в противном случае.
        """
        try:
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            element.send_keys(message)
            return True
        except Exception as ex:
             logger.error(f'Не удалось отправить сообщение {message} элементу {element} по локатору {locator}', ex)
             return False
```
# Changes Made

1.  **Добавлены RST-комментарии**: Документация в формате RST добавлена для модуля, класса `ExecuteLocator`, его методов и атрибутов, а также для классов `Locator`, `LocatorError` и `EventType`.
2.  **Импорты**: Добавлен импорт `from src.utils.jjson import j_loads_ns`, `from src.logger.logger import logger`.
3.  **Использование `j_loads_ns`**:  В методе `get_attribute_by_locator` заменен `json.loads` на `j_loads_ns`.
4.  **Логирование ошибок**: Заменены блоки `try-except` на использование `logger.error` для логирования ошибок.
5.  **Улучшена обработка ошибок**: Добавлена проверка на существование элемента перед попыткой выполнить с ним действие.
6.  **Удален лишний `else`**: Из метода `get_webelement_by_locator` убран лишний `else`.
7.  **Типизация**: Добавлены аннотации типов для параметров и возвращаемых значений методов.
8.  **Форматирование**: Код отформатирован в соответствии с PEP 8.
9.  **Использование `SimpleNamespace`**: Код теперь использует `SimpleNamespace` для работы с локаторами, что упрощает доступ к их атрибутам.
10. **Удаление лишних коментариев**: Удалены не информативные комментарии и коментарии не по стандарту.

# FULL Code

```python
"""
Модуль для выполнения действий с веб-элементами с использованием Selenium.
===========================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который используется для поиска,
взаимодействия и извлечения информации из веб-элементов на основе заданных локаторов.

Он поддерживает различные типы локаторов, действия с элементами, обработку ошибок и многое другое.

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

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

@dataclass
class Locator:
    """
    Представляет локатор веб-элемента.

    :param by: Тип локатора (например, 'ID', 'XPATH', 'CSS_SELECTOR').
    :param selector: Значение локатора.
    :param event: Событие для выполнения (например, 'click()', 'send_keys("text")').
    :param attribute: Атрибут для получения (например, 'value', 'text').
    :param mandatory: Флаг, указывающий, является ли элемент обязательным.
    :param many: Флаг, указывающий, нужно ли получить несколько элементов.
    :param name: Имя локатора для отладки.
    """
    by: str
    selector: str
    event: Optional[str] = None
    attribute: Optional[str] = None
    mandatory: bool = True
    many: bool = False
    name: Optional[str] = None


class LocatorError(Exception):
    """
    Исключение, выбрасываемое при ошибке в работе с локатором.
    """
    pass


class EventType(str, Enum):
    """
    Перечисление типов событий, которые можно выполнить с веб-элементом.
    """
    CLICK = 'click()'
    SEND_KEYS = 'send_keys'
    SCROLL_INTO_VIEW = 'scroll_into_view()'
    CLEAR = 'clear()'
    HOVER = 'hover()'


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :param actions: Объект ActionChains для выполнения сложных действий.
    :param by_mapping: Словарь, сопоставляющий типы локаторов с методами `By`.
    :param mode: Режим выполнения (например, 'debug', 'dev').
    """
    driver: WebDriver
    actions: ActionChains = field(init=False)
    by_mapping: Dict[str, str] = field(
        default_factory=lambda: {
            'ID': By.ID,
            'XPATH': By.XPATH,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'CLASS_NAME': By.CLASS_NAME,
            'TAG_NAME': By.TAG_NAME,
            'LINK_TEXT': By.LINK_TEXT,
            'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
            'NAME': By.NAME
        }
    )
    mode: str = 'debug'


    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)


    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Optional[Any]:
        """
        Выполняет действие с веб-элементом на основе предоставленного локатора.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :return: Результат выполнения действия с элементом.
        """
        # Проверяет тип локатора и преобразовывает его в SimpleNamespace при необходимости
        if isinstance(locator, dict):
           locator = SimpleNamespace(**locator)

        # Определение внутренней асинхронной функции для обработки локатора
        async def _parse_locator(locator: SimpleNamespace) -> Optional[Any]:
            """
            Внутренняя асинхронная функция для обработки локатора.

            :param locator: Локатор в виде SimpleNamespace.
            :return: Результат обработки локатора.
            """
            if not any([locator.event, locator.attribute, locator.mandatory]):
                return None
            try:
                # Пытается получить веб-элемент или атрибут по локатору, обрабатывая ошибки
                web_element = await self._evaluate(locator)
                if locator.event:
                    # Выполняет событие, если оно определено
                    return await self.execute_event(locator, web_element)
                if locator.attribute:
                    # Возвращает атрибут элемента, если он определен
                    return await self.get_attribute_by_locator(locator, web_element)
                # Возвращает веб-элемент, если не определено ни событие ни атрибут
                return web_element
            except Exception as ex:
                logger.error(f'Ошибка при выполнении локатора {locator=}', ex)
                ...  # Точка остановки для отладки
                return None

        # Вызывает внутреннюю функцию обработки и возвращает результат
        return await _parse_locator(locator)



    async def _evaluate(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Результат обработки атрибутов.
        """
        if isinstance(locator.attribute, list):
            # Если атрибут - список, обрабатывает каждый атрибут и возвращает результаты
            tasks = [self._evaluate(SimpleNamespace(**{**locator.__dict__, 'attribute': attr}))
                     for attr in locator.attribute]
            return await asyncio.gather(*tasks)

        # Если атрибут не список, получает веб-элемент по локатору
        return await self.get_webelement_by_locator(locator)

    async def get_attribute_by_locator(self, locator: SimpleNamespace, web_element: Any = None) -> Optional[Any]:
        """
        Возвращает атрибут элемента или список атрибутов элементов, найденных по локатору.

        :param locator: Локатор в виде SimpleNamespace.
        :param web_element: Веб-элемент, для которого нужно получить атрибут.
        :return: Атрибут элемента или список атрибутов элементов.
        """
        # Приводит локатор к SimpleNamespace если это словарь
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        # Если веб-элемент не передан, получает его по локатору
        if not web_element:
            web_element = await self.get_webelement_by_locator(locator)

        # Проверяет, был ли найден веб-элемент
        if not web_element:
            logger.debug(f'Не удалось получить элемент по локатору {locator}')
            return None


        if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
            try:
                attribute_dict = j_loads_ns(locator.attribute)
                # Получает атрибуты для каждого веб-элемента если их список
                if isinstance(web_element, list):
                    return [
                        {key: el.get_attribute(value) for key, value in attribute_dict.items()}
                        for el in web_element
                    ]
                # Получает атрибуты для одного веб-элемента
                return {key: web_element.get_attribute(value) for key, value in attribute_dict.items()}
            except Exception as ex:
                logger.error(f'Ошибка при парсинге атрибута {locator.attribute}', ex)
                ...
                return None
        # Получает атрибуты для каждого веб-элемента если их список
        if isinstance(web_element, list):
            return [el.get_attribute(locator.attribute) for el in web_element]

        # Получает атрибут для одного веб-элемента
        return web_element.get_attribute(locator.attribute)


    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Извлекает веб-элемент(ы) на основе предоставленного локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :return: Веб-элемент или список веб-элементов, или None если не найдены.
        """
        try:
            by = self.by_mapping.get(locator.by)
            if not by:
                logger.error(f'Неверный тип локатора {locator.by}')
                return None
            # Если требуется несколько элементов, находит их все
            if locator.many:
                elements = self.driver.find_elements(by, locator.selector)
                if not elements and locator.mandatory:
                    logger.debug(f'Не найдены элементы по локатору {locator}')
                    return None
                return elements
            # Иначе, находит один элемент
            element = self.driver.find_element(by, locator.selector)
            return element
        except Exception as ex:
             if locator.mandatory:
                logger.error(f'Не удалось найти элемент по локатору {locator}', ex)
                ... # Точка остановки для отладки
             else:
                logger.debug(f'Не удалось найти элемент по не обязательному локатору {locator}')
             return None


    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, save_path: str) -> bool:
        """
        Делает скриншот веб-элемента.

        :param locator: Локатор веб-элемента в виде SimpleNamespace.
        :param save_path: Путь для сохранения скриншота.
        :return: True если скриншот успешен, False в противном случае.
        """
        try:
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            element.screenshot(save_path)
            return True
        except Exception as ex:
            logger.error(f'Не удалось сделать скриншот элемента по локатору {locator}', ex)
            return False


    async def execute_event(self, locator: SimpleNamespace, element: Any) -> bool:
        """
        Выполняет событие, связанное с локатором.

        :param locator: Локатор в виде SimpleNamespace.
        :param element: Веб-элемент, с которым нужно выполнить событие.
        :return: True, если событие выполнено успешно, False в противном случае.
        """
        try:
            event = locator.event
            if event == EventType.CLICK:
                self.actions.click(element).perform()
            elif event.startswith(EventType.SEND_KEYS):
                keys = re.search(r'\((.*?)\)', event).group(1).strip("'").strip('"')
                self.actions.send_keys_to_element(element, keys).perform()
            elif event == EventType.SCROLL_INTO_VIEW:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
            elif event == EventType.CLEAR:
                 element.clear()
            elif event == EventType.HOVER:
                 self.actions.move_to_element(element).perform()
            return True
        except Exception as ex:
            logger.error(f'Не удалось выполнить событие {locator.event} для элемента {element}', ex)
            return False


    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Локатор веб-элемента в виде SimpleNamespace.
        :param message: Сообщение для отправки.
        :return: True если сообщение отправлено, False в противном случае.
        """
        try:
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            element.send_keys(message)
            return True
        except Exception as ex:
             logger.error(f'Не удалось отправить сообщение {message} элементу {element} по локатору {locator}', ex)
             return False