# Анализ кода модуля `executor`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и имеет четкое разделение на классы и методы.
    - Присутствует подробное описание модуля и его функциональности.
    - Используются асинхронные операции для неблокирующего выполнения.
    - Документация в формате Markdown.
- Минусы
    - Отсутствуют импорты `logger` из `src.logger.logger`, `j_loads`, `j_loads_ns` из `src.utils.jjson`.
    - Не все методы имеют docstring, отсутсвуют примеры использования и  описание параметров.
    - Используются стандартные блоки `try-except` вместо `logger.error`.
    - Не используется `from src.logger import logger`
    - Есть замечания к форматированию кода, а именно не используется одинарная ковычка для строк.
    - Код не полностью соответствует инструкциям по оформлению, не все функции, методы и переменные не документированы в формате RST.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить отсутствующие импорты `logger` из `src.logger.logger` и `j_loads`, `j_loads_ns` из `src.utils.jjson`.
2.  **Документация**: Добавить docstring в формате RST для всех классов, методов и функций, включая описание параметров и возвращаемых значений.
3.  **Обработка ошибок**: Использовать `logger.error` вместо стандартных `try-except` блоков.
4.  **Форматирование кода**: Привести все строковые литералы к одинарным кавычкам, за исключением случаев вывода в `print` или `logger.error`.
5.  **Улучшение читаемости**: Добавить комментарии `#` к блокам кода для пояснения их работы.
6.  **Логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок.
7. **Обработка данных**: Использовать `j_loads` или `j_loads_ns` вместо `json.load`
8. **Примеры**: Добавить примеры использования методов в docstring.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с веб-элементами с использованием Selenium.
=========================================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который предоставляет
гибкий фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = {
        'by': 'ID',
        'selector': 'some_element_id',
        'event': 'click()'
    }

    # Выполнение локатора
    result = await executor.execute_locator(locator)
    print(result)
"""
import asyncio
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Union

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.logger.logger import logger # Импортируем logger
from src.utils.jjson import j_loads, j_loads_ns # Импортируем j_loads, j_loads_ns


@dataclass
class Locator:
    """
    Класс для представления локатора.

    Attributes:
        by (str): Тип локатора (например, 'ID', 'XPATH', 'CSS_SELECTOR').
        selector (str): Строка-селектор для поиска элемента.
        event (str, optional): Событие, которое нужно выполнить (например, 'click()', 'send_keys(text)').
        attribute (str, optional): Атрибут, который нужно получить из элемента.
        mandatory (bool, optional): Флаг, указывающий, является ли локатор обязательным.
        screenshot (bool, optional): Флаг, указывающий, нужно ли делать скриншот элемента.
    """
    by: str
    selector: str
    event: str = None
    attribute: str = None
    mandatory: bool = False
    screenshot: bool = False


class Mode(str, Enum):
    """
    Перечисление для режимов выполнения.
    """
    DEBUG = 'debug'
    DEV = 'dev'
    PROD = 'prod'


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.

    Args:
        driver (WebDriver, optional): Экземпляр Selenium WebDriver.
        mode (Mode, optional): Режим выполнения.
    """
    driver: WebDriver = None
    mode: Mode = Mode.DEBUG
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        'ID': By.ID,
        'XPATH': By.XPATH,
        'CSS_SELECTOR': By.CSS_SELECTOR,
        'CLASS_NAME': By.CLASS_NAME,
        'TAG_NAME': By.TAG_NAME,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'NAME': By.NAME,
    })

    def __post_init__(self):
        """
        Инициализация объекта `ActionChains`, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Dict | SimpleNamespace) -> Any:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        Args:
            locator (Dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.

        Returns:
            Any: Результат выполнения действий (атрибут, веб-элемент, результат события) или None.

        Example:
            >>> locator = {'by': 'ID', 'selector': 'some_element_id', 'event': 'click()'}
            >>> result = await executor.execute_locator(locator)
        """
        # Проверяем, является ли локатор SimpleNamespace
        if isinstance(locator, SimpleNamespace):
            # Если да, используем локатор как есть
            parse_locator = locator
        else:
            # Если нет, преобразуем словарь в SimpleNamespace
            parse_locator = SimpleNamespace(**locator)

        # Определяем асинхронную функцию для парсинга локатора
        async def _parse_locator() -> Any:
            # Проверяем наличие события, атрибута или обязательного поля
            if not any([parse_locator.event, parse_locator.attribute, parse_locator.mandatory]):
                return None

            try:
                # Пытаемся сопоставить 'by' и оценить атрибут
                by = self.by_mapping.get(parse_locator.by)
                if not by:
                    logger.error(f'Неизвестный тип локатора: {parse_locator.by}')
                    return None

                # Выполняем действие в зависимости от наличия события или атрибута
                if parse_locator.event:
                    return await self.execute_event(parse_locator, by)
                if parse_locator.attribute:
                    return await self.get_attribute_by_locator(parse_locator, by)
                
                return await self.get_webelement_by_locator(parse_locator, by)

            except Exception as ex:
                # Логируем ошибку и возвращаем None
                logger.error(f'Ошибка при выполнении локатора: {parse_locator}', exc_info=ex)
                return None

        # Вызываем функцию парсинга локатора и возвращаем результат
        return await _parse_locator()
    
    async def evaluate_locator(self, locator: SimpleNamespace) -> Any:
        """
        Оценивает и обрабатывает атрибуты локатора.
        
        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.

        Returns:
            Any: Результат оценки атрибутов.

        Example:
            >>> locator = SimpleNamespace(attribute=['text', 'class'])
            >>> result = await executor.evaluate_locator(locator)
        """
        async def _evaluate(attr: str) -> Any:
            """
            Внутренняя функция для оценки одного атрибута.
            
            Args:
                attr (str): Атрибут для оценки.
            
            Returns:
                Any: Результат оценки атрибута.
            """
            try:
                return await self.execute_locator(SimpleNamespace(**{**locator.__dict__, 'attribute': attr}))
            except Exception as ex:
                logger.error(f'Ошибка при оценке атрибута {attr} для локатора {locator}', exc_info=ex)
                return None
        # Проверяем, является ли атрибут списком
        if isinstance(locator.attribute, list):
            # Если да, итерируем по каждому атрибуту и вызываем _evaluate
            return await asyncio.gather(*[_evaluate(attr) for attr in locator.attribute])
        else:
            # Если нет, вызываем _evaluate для одного атрибута
            return await _evaluate(locator.attribute)
    
    async def get_attribute_by_locator(self, locator: SimpleNamespace, by: By) -> Any:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            by (By): Тип локатора (например, By.ID, By.XPATH).

        Returns:
            Any: Значение атрибута или список значений атрибутов.

        Example:
             >>> locator = SimpleNamespace(by='ID', selector='some_element_id', attribute='text')
             >>> result = await executor.get_attribute_by_locator(locator, By.ID)
        """
        # Конвертируем локатор в SimpleNamespace если это словарь
        if isinstance(locator, dict):
           locator = SimpleNamespace(**locator)

        # Получаем веб-элемент по локатору
        element = await self.get_webelement_by_locator(locator, by)
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator}')
            return None
        
        # Проверяем, является ли locator.attribute строкой, похожей на словарь
        if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
            try:
                # Пытаемся распарсить строку в словарь
                attrs_dict = j_loads(locator.attribute)
                if isinstance(element, list):
                    # Если элемент - список, получаем атрибуты для каждого элемента
                    return [self.get_element_attribute(el, attrs_dict) for el in element]
                else:
                    # Если элемент один, получаем атрибуты для него
                    return self.get_element_attribute(element, attrs_dict)
            except Exception as ex:
                logger.error(f'Ошибка парсинга атрибутов {locator.attribute} как словаря', exc_info=ex)
        
        if isinstance(element, list):
                # Если элемент - список, получаем атрибуты для каждого элемента
                return [el.get_attribute(locator.attribute) for el in element]
        else:
            # Если элемент один, получаем атрибут для него
            return element.get_attribute(locator.attribute)

    def get_element_attribute(self, element: WebElement, attrs: dict) -> dict:
        """
         Получает значения атрибутов элемента на основе предоставленного словаря.

        Args:
            element (WebElement): Веб-элемент.
            attrs (dict): Словарь атрибутов, которые нужно получить.

        Returns:
           dict: Словарь, содержащий полученные атрибуты и их значения.
        """
        result = {}
        for key, value in attrs.items():
             # Пытаемся получить атрибут, если его нет устанавливаем значение None
            try:
                result[key] = element.get_attribute(value)
            except Exception as ex:
                 logger.error(f'Не удалось получить атрибут {value} у элемента {element}', exc_info=ex)
                 result[key] = None
        return result

    async def get_webelement_by_locator(self, locator: SimpleNamespace, by: By) ->  Union[WebElement, List[WebElement], None]:
        """
        Извлекает веб-элемент(ы) на основе предоставленного локатора.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            by (By): Тип локатора (например, By.ID, By.XPATH).

        Returns:
            Union[WebElement, List[WebElement], None]: Веб-элемент, список веб-элементов или None.

        Example:
            >>> locator = SimpleNamespace(by='ID', selector='some_element_id')
            >>> element = await executor.get_webelement_by_locator(locator, By.ID)
        """
        try:
            # Ищем все элементы, если не указано, что элемент обязательный
            if not locator.mandatory:
                elements = self.driver.find_elements(by, locator.selector)
                if elements:
                    return elements
                else:
                    logger.debug(f'Элемент(ы) не найден(ы) по локатору: {locator}')
                    return None
            else:
                # Ищем один элемент, если указано, что элемент обязательный
                element = self.driver.find_element(by, locator.selector)
                return element
        except Exception as ex:
            logger.error(f'Ошибка поиска элемента по локатору: {locator}', exc_info=ex)
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, by: By) -> str:
        """
        Делает скриншот найденного веб-элемента и возвращает его в формате base64.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            by (By): Тип локатора (например, By.ID, By.XPATH).

        Returns:
             str: Скриншот элемента в формате base64 или None, если элемент не найден.
        """
        try:
            # Получаем веб-элемент
            element = await self.get_webelement_by_locator(locator, by)
            if not element:
                logger.debug(f'Элемент не найден для скриншота по локатору: {locator}')
                return None

            # Если элемент является списком, получаем скриншот первого элемента
            if isinstance(element, list):
                 element = element[0]

            # Делаем скриншот и возвращаем его
            return element.screenshot_as_base64
        except Exception as ex:
             logger.error(f'Ошибка получения скриншота элемента по локатору: {locator}', exc_info=ex)
             return None

    async def execute_event(self, locator: SimpleNamespace, by: By) -> Any:
        """
        Выполняет событие, связанное с локатором.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            by (By): Тип локатора (например, By.ID, By.XPATH).

        Returns:
            Any: Результат выполнения события или None в случае ошибки.

        Example:
            >>> locator = SimpleNamespace(by='ID', selector='some_element_id', event='click()')
            >>> result = await executor.execute_event(locator, By.ID)
        """
        try:
            # Получаем веб-элемент
            element = await self.get_webelement_by_locator(locator, by)
            if not element:
                logger.debug(f'Элемент не найден для выполнения события по локатору: {locator}')
                return None

            # Если элемент - список, выполняем событие для каждого элемента
            if isinstance(element, list):
                return [self._do_event(el, locator.event) for el in element]
            else:
                 # Выполняем событие для одного элемента
                 return self._do_event(element, locator.event)
        except Exception as ex:
            logger.error(f'Ошибка выполнения события {locator.event} по локатору: {locator}', exc_info=ex)
            return None

    def _do_event(self, element: WebElement, event: str) -> Any:
        """
        Выполняет событие над элементом.
        
        Args:
            element (WebElement): Веб-элемент, над которым нужно выполнить событие.
            event (str): Строка, представляющая событие для выполнения (например, 'click()', 'send_keys(text)').
        
        Returns:
            Any: Результат выполнения события.
        """
        if event == 'click()':
            # Выполняем клик
            element.click()
            return True
        elif event.startswith('send_keys('):
            # Выполняем отправку сообщения
            text = event[len('send_keys('):-1]
            return self.send_message(element, text)
        else:
            logger.error(f'Неизвестное событие: {event}')
            return None
            
    def send_message(self, element: WebElement, text: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        Args:
             element (WebElement): Веб-элемент, которому нужно отправить сообщение.
             text (str): Текст сообщения.

        Returns:
            bool: True, если сообщение отправлено успешно, False в противном случае.
        """
        try:
            # Отправляем текст в элемент
            element.send_keys(text)
            return True
        except Exception as ex:
            logger.error(f'Ошибка отправки сообщения {text} элементу {element}', exc_info=ex)
            return False
```