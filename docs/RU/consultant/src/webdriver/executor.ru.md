# Анализ кода модуля `executor.py`

**Качество кода: 7/10**
- **Плюсы**
    - Хорошая структурированность кода и четкое разделение на классы и методы.
    - Наличие подробного описания модуля, классов и методов.
    - Использование Mermaid-диаграмм для визуализации потоков выполнения, что помогает понять логику работы.
    - Реализация обработки ошибок с использованием try-except, хотя можно усовершенствовать.
- **Минусы**
    - Отсутствие необходимых импортов в коде.
    - Стандартный `json.load` используется для чтения файлов, вместо `j_loads` или `j_loads_ns`.
    - Не все функции и методы имеют docstring в формате RST.
    - Избыточное использование стандартных блоков `try-except`.
    - Не используется `from src.logger.logger import logger` для логирования.
    - Отсутствие примеров использования с подробными объяснениями.
    - Не везде соблюдены требования к одинарным кавычкам в коде.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить все необходимые импорты для корректной работы кода.
2.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` для чтения файлов.
3.  **Документация**: Добавить docstring в формате RST для всех функций и методов, включая примеры использования.
4.  **Логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок и заменить стандартные try-except на использование `logger.error`.
5.  **Форматирование**: Привести все строки к одинарным кавычкам, кроме строк вывода.
6.  **Комментарии**: Добавить более подробные комментарии к блокам кода.
7.  **Примеры**: Включить примеры использования для ключевых функций и классов с пояснениями.
8.  **Рефакторинг**: Оптимизировать код, избегая избыточных проверок и повторений.
9.  **Структура**: Привести в соответствие названия переменных, функций и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для автоматизации взаимодействия с веб-элементами с использованием Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который используется для взаимодействия с веб-элементами на основе предоставленных локаторов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver=driver)
    locator = {
        'by': 'ID',
        'selector': 'some_element_id',
        'event': 'click()'
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
from src.utils.jjson import j_loads
from src.logger.logger import logger
from selenium.common.exceptions import StaleElementReferenceException
# from json import load  # Заменено на src.utils.jjson
# from src.logger import logger # Заменено на from src.logger.logger import logger


@dataclass
class ProductFields:
    """
    Класс данных для хранения полей продукта.

    Attributes:
        name (Optional[str]): Название продукта.
        description (Optional[str]): Описание продукта.
        specification (Optional[str]): Спецификация продукта.
        price (Optional[str]): Цена продукта.
        sku (Optional[str]): SKU продукта.
        images (Optional[List[str]]): Список URL изображений продукта.
        attributes (Optional[Dict[str, str]]): Словарь атрибутов продукта.
        add_fields (Optional[Dict[str, str]]): Дополнительные поля продукта.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    specification: Optional[str] = None
    price: Optional[str] = None
    sku: Optional[str] = None
    images: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None
    add_fields: Optional[Dict[str, str]] = None


class Actions(str, Enum):
    """
    Перечисление возможных действий с веб-элементом.

    Attributes:
        CLICK (str): Клик по элементу.
        SEND (str): Отправка сообщения элементу.
    """
    CLICK = 'click()'
    SEND = 'send_message()'


class ByType(str, Enum):
    """
    Перечисление типов локаторов `By`.

    Attributes:
        ID (str): Локатор по ID.
        XPATH (str): Локатор по XPath.
        CSS_SELECTOR (str): Локатор по CSS-селектору.
        CLASS_NAME (str): Локатор по имени класса.
        TAG_NAME (str): Локатор по имени тега.
        LINK_TEXT (str): Локатор по тексту ссылки.
        PARTIAL_LINK_TEXT (str): Локатор по части текста ссылки.
        NAME (str): Локатор по имени.
    """
    ID = 'id'
    XPATH = 'xpath'
    CSS_SELECTOR = 'css_selector'
    CLASS_NAME = 'class_name'
    TAG_NAME = 'tag_name'
    LINK_TEXT = 'link_text'
    PARTIAL_LINK_TEXT = 'partial_link_text'
    NAME = 'name'


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий над веб-элементами на основе предоставленных локаторов.

    Attributes:
        driver (WebDriver): Экземпляр Selenium WebDriver.
        actions (ActionChains): Объект ActionChains для выполнения сложных действий.
        by_mapping (Dict[str, str]): Словарь, сопоставляющий типы локаторов с методами By Selenium.
        mode (str): Режим выполнения (`debug`, `dev` и т.д.).
    """
    driver: WebDriver
    actions: ActionChains = field(init=False)
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        ByType.ID: By.ID,
        ByType.XPATH: By.XPATH,
        ByType.CSS_SELECTOR: By.CSS_SELECTOR,
        ByType.CLASS_NAME: By.CLASS_NAME,
        ByType.TAG_NAME: By.TAG_NAME,
        ByType.LINK_TEXT: By.LINK_TEXT,
        ByType.PARTIAL_LINK_TEXT: By.PARTIAL_LINK_TEXT,
        ByType.NAME: By.NAME,
    })
    mode: str = 'dev'

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[SimpleNamespace, Dict]) -> Optional[Any]:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        Args:
            locator (Union[SimpleNamespace, Dict]): Локатор в виде SimpleNamespace или словаря.

        Returns:
            Optional[Any]: Результат выполнения действия или None в случае ошибки.

        """
        # Проверка типа локатора, и если это словарь - преобразование в SimpleNamespace
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
        # Определение функции _parse_locator
        async def _parse_locator(_locator):
            # Проверка наличия события, атрибута или обязательного поля
            if not any([hasattr(_locator, 'event'), hasattr(_locator, 'attribute'), hasattr(_locator, 'by') and hasattr(_locator, 'selector')]):
                logger.debug(f'Локатор не имеет обязательных полей {locator}')
                return None
            try:
                # Попытка получить by и вызвать _evaluate_attribute для получения значения атрибута
                if hasattr(_locator, 'by') and hasattr(_locator, 'selector'):
                    by = self.by_mapping.get(_locator.by)
                    if not by:
                        logger.error(f'Неизвестный тип локатора {_locator.by}')
                        return None
                    if hasattr(_locator, 'attribute'):
                        return await self.evaluate_locator(locator=_locator)
                    # Проверка наличия события
                    if hasattr(_locator, 'event'):
                        return await self.execute_event(_locator)
                    # Получение веб-элемента
                    return await self.get_webelement_by_locator(_locator)
            except Exception as ex:
                logger.error(f'Ошибка при обработке локатора {_locator}: {ex}')
                return None
        # Выполнение асинхронной функции _parse_locator и возврат результата
        return await _parse_locator(locator)
    
    async def evaluate_locator(self, locator: SimpleNamespace) -> Optional[Union[str, list[str]]]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.

        Returns:
             Optional[Union[str, list[str]]]: Значение атрибута или список значений или None в случае ошибки.

        """
        # Проверка, является ли атрибут списком
        if isinstance(locator.attribute, list):
            # Вызов _evaluate для каждого атрибута
            tasks = [self._evaluate(locator, attribute) for attribute in locator.attribute]
            # Возврат списка результатов
            return await asyncio.gather(*tasks)
        else:
            # Вызов _evaluate для одного атрибута
            return await self._evaluate(locator, locator.attribute)

    async def _evaluate(self, locator: SimpleNamespace, attribute: str) -> Optional[str]:
        """
        Извлекает значение атрибута для заданного локатора и атрибута.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            attribute (str): Имя атрибута.

        Returns:
            Optional[str]: Значение атрибута или None в случае ошибки.

        """
        try:
            # Получение веб-элемента по локатору
            web_element = await self.get_webelement_by_locator(locator)
            # Проверка, найден ли веб-элемент
            if not web_element:
                logger.debug(f'Веб-элемент не найден по локатору {locator}')
                return None
            # Проверка, является ли атрибут строкой, похожей на словарь
            if isinstance(attribute, str) and attribute.startswith('{') and attribute.endswith('}'):
                try:
                    # Разбор строки атрибута в словарь
                    attribute_dict = j_loads(attribute)
                    # Проверка, является ли веб-элемент списком
                    if isinstance(web_element, list):
                        # Получение атрибутов для каждого элемента в списке
                        return [item.get_attribute(attr) for item in web_element for attr in attribute_dict]
                    # Получение атрибута для одного веб-элемента
                    return [web_element.get_attribute(attr) for attr in attribute_dict]
                except Exception as e:
                    logger.error(f'Ошибка при разборе атрибута как словаря {attribute} {e}')
                    return None
            else:
                # Проверка, является ли веб-элемент списком
                if isinstance(web_element, list):
                     # Получение атрибутов для каждого элемента в списке
                    return [item.get_attribute(attribute) for item in web_element]
                # Получение атрибута для одного веб-элемента
                return web_element.get_attribute(attribute)
        except Exception as ex:
            logger.error(f'Ошибка при получении атрибута {attribute} {ex}')
            return None

    async def get_attribute_by_locator(self, locator: Union[SimpleNamespace, Dict]) -> Optional[Union[str, list[str]]]:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        Args:
            locator (Union[SimpleNamespace, Dict]): Локатор в виде SimpleNamespace или словаря.

        Returns:
            Optional[Union[str, list[str]]]: Значение атрибута или список значений, или None, если элемент не найден или произошла ошибка.
        """
        # Преобразование локатора в SimpleNamespace, если это словарь
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
        # Получение веб-элемента
        web_element = await self.get_webelement_by_locator(locator)
        # Проверка, найден ли веб-элемент
        if not web_element:
            logger.debug(f'Веб-элемент не найден по локатору {locator}')
            return None
        # Проверка, является ли locator.attribute строкой, похожей на словарь
        if hasattr(locator, 'attribute') and isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
            try:
                # Разбор строки locator.attribute в словарь
                attribute_dict = j_loads(locator.attribute)
                # Проверка, является ли веб-элемент списком
                if isinstance(web_element, list):
                    # Получение атрибутов для каждого элемента в списке
                    return [item.get_attribute(attr) for item in web_element for attr in attribute_dict]
                 # Получение атрибута для одного веб-элемента
                return [web_element.get_attribute(attr) for attr in attribute_dict]
            except Exception as ex:
                logger.error(f'Ошибка при разборе атрибута как словаря {locator.attribute} {ex}')
                return None
        else:
             # Проверка, является ли веб-элемент списком
            if isinstance(web_element, list):
                 # Получение атрибутов для каждого элемента в списке
                if hasattr(locator, 'attribute'):
                   return [item.get_attribute(locator.attribute) for item in web_element]
                return [item.text for item in web_element]
             # Получение атрибута для одного веб-элемента
            if hasattr(locator, 'attribute'):
                return web_element.get_attribute(locator.attribute)
            return web_element.text
    
    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элементы на основе предоставленного локатора.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.

        Returns:
            Optional[Union[WebElement, List[WebElement]]]: Веб-элемент или список веб-элементов, или None, если элемент не найден.
        """
        try:
            # Получение типа локатора из словаря self.by_mapping
            by = self.by_mapping.get(locator.by)
            # Проверка, найден ли тип локатора
            if not by:
                logger.error(f'Неизвестный тип локатора {locator.by}')
                return None
            # Получение всех веб-элементов, если указано all=True
            if hasattr(locator, 'all') and locator.all:
                return self.driver.find_elements(by, locator.selector)
            # Получение одного веб-элемента
            element = self.driver.find_element(by, locator.selector)
            return element
        except Exception as ex:
            logger.error(f'Ошибка при получении веб-элемента {locator} {ex}')
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, file_path: Union[str, Path]) -> bool:
        """
        Делает скриншот найденного веб-элемента.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            file_path (Union[str, Path]): Путь к файлу для сохранения скриншота.

        Returns:
            bool: True, если скриншот успешно сделан, False в противном случае.
        """
        try:
            # Получение веб-элемента по локатору
            element = await self.get_webelement_by_locator(locator)
            if element:
                # Сохранение скриншота веб-элемента
                element.screenshot(str(file_path))
                return True
            return False
        except Exception as ex:
            logger.error(f'Не удалось сделать скриншот {file_path} {ex}')
            return False

    async def execute_event(self, locator: SimpleNamespace) -> bool:
        """
        Выполняет события, связанные с локатором.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.

        Returns:
            bool: True, если событие выполнено успешно, False в противном случае.
        """
        try:
            # Получение веб-элемента по локатору
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            # Выполнение действия в зависимости от типа события
            if locator.event == Actions.CLICK:
                element.click()
            # Проверка на наличие аргументов в событии
            elif hasattr(locator, 'args') and locator.event == Actions.SEND:
                element.send_keys(locator.args)
            return True
        except StaleElementReferenceException as ex:
            logger.error(f'Элемент устарел {locator} {ex}')
            return False
        except Exception as ex:
            logger.error(f'Не удалось выполнить событие {locator} {ex}')
            return False

    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        Args:
            locator (SimpleNamespace): Локатор в виде SimpleNamespace.
            message (str): Сообщение для отправки.

        Returns:
             bool: True, если сообщение отправлено успешно, False в противном случае.
        """
        try:
            # Получение веб-элемента по локатору
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False
            # Отправка сообщения веб-элементу
            element.send_keys(message)
            return True
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение {message} {ex}')
            return False
```