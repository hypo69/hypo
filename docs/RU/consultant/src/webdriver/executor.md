# Анализ кода модуля `executor.py`

**Качество кода**
7
- Плюсы
    -   Хорошее подробное описание модуля, классов и методов.
    -   Наличие диаграмм последовательностей для основных методов.
    -   Примеры использования.
- Минусы
    -   Не указаны все необходимые импорты в коде.
    -   Отсутствуют docstring для функций и классов.
    -   Использование try-except без логирования ошибок.
    -   Некоторые переменные и функции не соответствуют стилю кода.

**Рекомендации по улучшению**

1.  **Добавить отсутствующие импорты**:
    -   Добавить `from src.logger.logger import logger` для логирования ошибок.
    -   Добавить `from src.utils.jjson import j_loads, j_loads_ns` для работы с json.
    -   Добавить `from selenium.webdriver.common.by import By` для работы с локаторами.
    -   Добавить `from selenium.webdriver.support.wait import WebDriverWait` для ожидания элементов.
    -   Добавить `from selenium.webdriver.support import expected_conditions as EC` для проверки условий.
2.  **Добавить docstring**:
    -   Добавить документацию в формате RST ко всем функциям, методам и классам.
3.  **Улучшить обработку ошибок**:
    -   Заменить стандартные `try-except` блоки на обработку ошибок через `logger.error`, где это возможно.
4.  **Рефакторинг кода**:
    -   Привести в соответствие имена переменных и функций с ранее обработанными файлами.
5. **Улучшение комментариев:**
    -  Комментарии должны быть более информативными, описывая назначение кода.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с веб-элементами с использованием Selenium.
========================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который позволяет автоматизировать взаимодействие с веб-элементами,
используя Selenium. Он поддерживает различные типы локаторов, действия с элементами (клики, отправку сообщений, выполнение JavaScript),
а также извлечение атрибутов и создание скриншотов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация ExecuteLocator
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
from typing import Any, Callable, Dict, List, Optional, Union

from selenium.webdriver import ActionChains
#from selenium.webdriver.common.by import By # Импорт By для определения типа локатора
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from src.logger.logger import logger # импортируем logger
#from src.utils.jjson import j_loads, j_loads_ns # импортируем j_loads, j_loads_ns
# TODO добавить import для j_loads и j_loads_ns


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе заданных локаторов.

    Args:
        driver (WebDriver): Экземпляр Selenium WebDriver.
        mode (str, optional): Режим выполнения. По умолчанию 'dev'.

    Attributes:
        driver (WebDriver): Экземпляр Selenium WebDriver.
        actions (ActionChains): Объект для выполнения цепочек действий.
        by_mapping (dict): Словарь соответствий типа локатора и метода By.
        mode (str): Режим выполнения.

    """
    driver: WebDriver
    mode: str = 'dev'
    actions: ActionChains = field(init=False)

    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        'ID': 'id',
        'XPATH': 'xpath',
        'CLASS_NAME': 'class name',
        'CSS_SELECTOR': 'css selector',
        'LINK_TEXT': 'link text',
        'PARTIAL_LINK_TEXT': 'partial link text',
        'NAME': 'name',
        'TAG_NAME': 'tag name',
    })

    def __post_init__(self):
        """
        Инициализация объекта ActionChains, если передан драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[dict, SimpleNamespace]) -> Optional[Any]:
        """
        Выполняет действия с веб-элементом на основе заданного локатора.

        Args:
            locator (Union[dict, SimpleNamespace]): Словарь или SimpleNamespace с данными локатора.

        Returns:
            Optional[Any]: Результат выполнения действия с элементом или None в случае неудачи.

        """
        # Проверка, является ли локатор SimpleNamespace или словарем, при необходимости преобразует в SimpleNamespace
        if isinstance(locator, SimpleNamespace):
            _locator = locator
        else:
            _locator = SimpleNamespace(**locator)
        
        # Определяем внутреннюю функцию _parse_locator
        async def _parse_locator(_locator: SimpleNamespace) -> Optional[Any]:
             # Проверка наличия 'event', 'attribute' или 'mandatory' в локаторе
            if not any(hasattr(_locator, attr) for attr in ['event', 'attribute', 'mandatory']):
                 return None
            try:
                # Пытаемся получить и обработать элемент по локатору
                by = self.by_mapping.get(_locator.by)
                if not by:
                    logger.error(f'Неверный тип локатора: {_locator.by}')
                    return None

                #  вызывает асинхронную функцию _evaluate для обработки атрибутов, если они есть
                if hasattr(_locator, 'attribute'):
                    return await self.evaluate_locator(_locator)
                # проверяет наличие события, и вызывает функцию execute_event
                elif hasattr(_locator, 'event'):
                   return await self.execute_event(_locator)
                # вызывает функцию для получения веб элемента
                else:
                     return await self.get_webelement_by_locator(_locator)

            except Exception as ex:
                logger.error(f'Ошибка при выполнении локатора: {locator}', exc_info=ex)
                return None

        # Возвращаем результат выполнения _parse_locator
        return await _parse_locator(_locator)



    async def evaluate_locator(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.

        Returns:
            Optional[Any]: Значение атрибута или список значений, если атрибут задан как список.

        """
        # Проверка, является ли атрибут списком
        if isinstance(locator.attribute, list):
            # Если атрибут список, то обрабатываем каждый элемент списка
            results = await asyncio.gather(*[self._evaluate(locator, attr) for attr in locator.attribute])
            return results
        else:
            # Если атрибут не список, то обрабатываем его как одиночный
            return await self._evaluate(locator, locator.attribute)


    async def _evaluate(self, locator: SimpleNamespace, attribute: str) -> Optional[Any]:
        """
        Вспомогательная функция для оценки одного атрибута.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.
            attribute (str): Имя атрибута.

        Returns:
            Optional[Any]: Значение атрибута или None в случае ошибки.

        """
        try:
            # Код получает веб-элемент по локатору
            element = await self.get_webelement_by_locator(locator)
            if not element:
                logger.debug(f'Элемент не найден {locator=}')
                return None
            
            if isinstance(element, list):
                # если элемент - список, извлекает значения атрибута для каждого элемента
                results = [getattr(el, attribute, None) for el in element if el]
                return results if results else None
            else:
                # если элемент не список, то извлекаем значение атрибута
                return getattr(element, attribute, None)

        except Exception as ex:
             # Логирование ошибки в случае неудачи
             logger.error(f'Ошибка при получении атрибута {attribute} по локатору {locator=}', exc_info=ex)
             return None



    async def get_attribute_by_locator(self, locator: Union[dict, SimpleNamespace]) -> Optional[Union[str, List[str]]]:
        """
        Извлекает атрибуты элемента или списка элементов по заданному локатору.

        Args:
            locator (Union[dict, SimpleNamespace]): Словарь или SimpleNamespace с данными локатора.

        Returns:
             Optional[Union[str, List[str]]]: Значение атрибута или список значений, или None, если элемент не найден.

        """
        # Преобразует локатор в SimpleNamespace при необходимости
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
        
        #  получает веб-элемент с помощью функции get_webelement_by_locator
        element = await self.get_webelement_by_locator(locator)

        # Проверяет, найден ли веб-элемент. Если нет, возвращаем None
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            return None
        
        # Проверяет, является ли атрибут строкой, похожей на словарь.
        if isinstance(locator.attribute, str) and locator.attribute.startswith('{') and locator.attribute.endswith('}'):
           try:
               # Пытается преобразовать строку атрибута в словарь.
              attribute_dict = j_loads(locator.attribute)
           except Exception as ex:
                logger.error(f'Не удалось преобразовать атрибут в словарь {locator.attribute}', exc_info=ex)
                attribute_dict = {}

           if isinstance(element, list):
              # Извлекает атрибуты для каждого элемента в списке
                return [self._get_attribute(el, attribute_dict) for el in element if el]
           else:
              # извлекает атрибут для одиночного веб-элемента
               return self._get_attribute(element, attribute_dict)

        # Если элемент является списком, то обрабатываем каждый элемент списка
        if isinstance(element, list):
            return [getattr(el, locator.attribute, None) for el in element if el]
        else:
             # Если элемент не список, то возвращаем значение атрибута
            return getattr(element, locator.attribute, None)

    def _get_attribute(self, element: WebElement, attribute_dict: Dict) -> Dict:
        """
        Извлекает атрибуты элемента на основе словаря атрибутов.

        Args:
            element (WebElement): Веб-элемент, из которого извлекаются атрибуты.
            attribute_dict (Dict): Словарь с атрибутами для извлечения.

         Returns:
            Dict: Словарь с извлеченными атрибутами.

        """
        result = {}
        for key, value in attribute_dict.items():
           result[key] = element.get_attribute(value)
        return result

    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элемент или список элементов по заданному локатору.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.

        Returns:
            Optional[Union[WebElement, List[WebElement]]]: Веб-элемент или список элементов, или None, если элемент не найден.

        """
        try:
            # Проверяет наличие локатора 'all'
            if getattr(locator, 'all', None):
                # Находит все веб-элементы по локатору
                return self.driver.find_elements(self.by_mapping[locator.by], locator.selector)
            else:
                 # Находит один веб-элемент по локатору
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.presence_of_element_located((self.by_mapping[locator.by], locator.selector)))
                return element
        except Exception as ex:
            logger.error(f'Не удалось найти веб-элемент по локатору {locator=}', exc_info=ex)
            return None


    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, file_path: Union[str, Path]) -> bool:
         """
        Создает и сохраняет скриншот веб-элемента.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.
            file_path (Union[str, Path]): Путь для сохранения скриншота.

        Returns:
            bool: True, если скриншот успешно создан и сохранен, иначе False.

        """
         try:
            # Получает веб-элемент
            element = await self.get_webelement_by_locator(locator)
            if element:
                 # Сохраняет скриншот
                element.screenshot(str(file_path))
                return True
            return False
         except Exception as ex:
            logger.error(f'Не удалось сделать скриншот элемента {locator=}', exc_info=ex)
            return False


    async def execute_event(self, locator: SimpleNamespace) -> bool:
        """
        Выполняет JavaScript событие для веб-элемента.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.

        Returns:
            bool: True, если событие успешно выполнено, иначе False.

        """
        try:
            # Получает веб-элемент
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False

            # Выполняет JavaScript событие
            if isinstance(element, list):
               # Выполняет событие на каждом элементе списка
                for el in element:
                    self.driver.execute_script(locator.event, el)
            else:
                self.driver.execute_script(locator.event, element)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при выполнении события {locator.event} для {locator=}', exc_info=ex)
            return False



    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        Args:
            locator (SimpleNamespace): Объект SimpleNamespace с данными локатора.
            message (str): Сообщение для отправки.

        Returns:
            bool: True, если сообщение успешно отправлено, иначе False.

        """
        try:
            # Получает веб-элемент
            element = await self.get_webelement_by_locator(locator)
            if not element:
                return False

             # Отправляет сообщение в веб-элемент
            if isinstance(element, list):
                for el in element:
                     el.send_keys(message)
            else:
               element.send_keys(message)
            return True
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение {message} в элемент {locator=}', exc_info=ex)
            return False
```