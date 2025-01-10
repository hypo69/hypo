# Анализ кода модуля `executor.py`

**Качество кода**
7
- Плюсы
    - Хорошая структура и организация кода.
    - Детальное описание модуля в формате `rst`.
    - Использование `mermaid` диаграмм для визуализации логики.
    - Асинхронное программирование.
    - Обработка ошибок с использованием `try-except`.
- Минусы
    - Не все функции и методы имеют docstring, хотя в инструкции это является обязательным.
    - Не используется `from src.logger.logger import logger`.
    - Стандартные блоки `try-except` используются избыточно.
    - Отсутствие приведения к единому стандарту именования, такие как `_parse_locator` и `get_webelement_by_locator`.

**Рекомендации по улучшению**

1. **Документирование**:
   - Добавить `docstring` для всех функций и методов в формате `rst`.
   - Обновить описание модуля, привести в соответствие с требованиями.
2.  **Логирование**:
    - Использовать `from src.logger.logger import logger` для логирования ошибок.
    - Избегать стандартных блоков `try-except`, использовать `logger.error` вместо них.
3. **Стиль кода**:
    - Привести в соответствие имена переменных, функций и импортов со стандартами.
    - Использовать одинарные кавычки для строк в коде, двойные - для `print`, `input`, и `logger.error`.
4. **Обработка данных**:
     - Использовать `j_loads` или `j_loads_ns` вместо стандартного `json.load` для чтения файлов, если это необходимо.

**Оптимизированный код**
```python
"""
Модуль для взаимодействия с веб-элементами с использованием Selenium.
======================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который позволяет автоматизировать взаимодействие
с веб-элементами на основе заданных локаторов. Он поддерживает различные действия, такие как клики, отправка
сообщений, выполнение событий и извлечение атрибутов.

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
from typing import Any, Dict, List, Optional, Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе заданных локаторов.

    Args:
        driver (WebDriver): Экземпляр WebDriver Selenium.
        mode (str, optional): Режим выполнения (debug, dev и т.д.). Defaults to 'dev'.

    Attributes:
        driver (WebDriver): Экземпляр WebDriver Selenium.
        actions (ActionChains): Объект ActionChains для выполнения сложных действий.
        by_mapping (dict): Словарь, связывающий типы локаторов с методами By Selenium.
        mode (str): Режим выполнения.

    """
    driver: WebDriver
    mode: str = 'dev'
    actions: Optional[ActionChains] = field(init=False, default=None)
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        'ID': By.ID,
        'XPATH': By.XPATH,
        'CLASS_NAME': By.CLASS_NAME,
        'CSS_SELECTOR': By.CSS_SELECTOR,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'NAME': By.NAME,
        'TAG_NAME': By.TAG_NAME
    })

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
        """
        Выполняет действия с веб-элементом на основе заданного локатора.

        Args:
            locator (Union[Dict, SimpleNamespace]): Словарь или SimpleNamespace, содержащий параметры локатора.

        Returns:
            Optional[Union[str, List[str], WebElement, List[WebElement]]]: Результат выполнения локатора
                или None, если локатор не содержит необходимых параметров.

        Flow Diagram:
        ```mermaid
            graph TD
            Start[Start] --> CheckLocatorType[Check if locator is SimpleNamespace or dict]
            CheckLocatorType --> IsSimpleNamespace{Is locator SimpleNamespace?}
            IsSimpleNamespace -->|Yes| UseLocatorAsIs[Use locator as is]
            IsSimpleNamespace -->|No| ConvertDictToSimpleNamespace[Convert dict to SimpleNamespace]
            ConvertDictToSimpleNamespace --> UseLocatorAsIs
            UseLocatorAsIs --> DefineParseLocator[Define async function _parse_locator]
            DefineParseLocator --> CheckEventAttributeMandatory[Check if locator has event, attribute, or mandatory]
            CheckEventAttributeMandatory -->|No| ReturnNone[Return None]
            CheckEventAttributeMandatory -->|Yes| TryMapByEvaluateAttribute[Try to map by and evaluate attribute]
            TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Catch exceptions and log if needed]
            CatchExceptionsAndLog --> HasEvent{Does locator have event?}
            HasEvent -->|Yes| ExecuteEvent[Execute event]
            HasEvent -->|No| HasAttribute{Does locator have attribute?}
            HasAttribute -->|Yes| GetAttributeByLocator[Get attribute by locator]
            HasAttribute -->|No| GetWebElementByLocator[Get web element by locator]
            ExecuteEvent --> ReturnEventResult[Return result of event]
            GetAttributeByLocator --> ReturnAttributeResult[Return attribute result]
            GetWebElementByLocator --> ReturnWebElementResult[Return web element result]
            ReturnEventResult --> ReturnFinalResult[Return final result of _parse_locator]
            ReturnAttributeResult --> ReturnFinalResult
            ReturnWebElementResult --> ReturnFinalResult
            ReturnFinalResult --> ReturnExecuteLocatorResult[Return result of execute_locator]
            ReturnExecuteLocatorResult --> End[End]
        ```
        """
        if not isinstance(locator, SimpleNamespace):
            # Код преобразует словарь в SimpleNamespace
            locator = j_loads_ns(locator)

        async def _parse_locator(locator: SimpleNamespace) -> Optional[Union[str, List[str], WebElement, List[WebElement]]]:
            """
            Внутренняя функция для обработки локатора.

            Args:
                locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

            Returns:
                 Optional[Union[str, List[str], WebElement, List[WebElement]]]: Результат обработки локатора
                или None, если локатор не содержит необходимых параметров.
            """
            # Проверяет наличие event, attribute, или mandatory в локаторе
            if not any([getattr(locator, 'event', None), getattr(locator, 'attribute', None), getattr(locator, 'mandatory', None)]):
                 # Если не найдено, возвращает None
                return None
            try:
                # Код вызывает evaluate_locator и обрабатывает результат
                if locator.by:
                    result = await self.evaluate_locator(locator)
                else:
                   logger.error(f'Не указан `by` в локаторе {locator}')
                   return None

            except Exception as ex:
               logger.error(f'Ошибка при обработке локатора {locator}', exc_info=ex)
               return None

            # Проверяет наличие event в локаторе
            if hasattr(locator, 'event') and locator.event:
                # Код вызывает execute_event и возвращает результат
                return await self.execute_event(locator)
            # Проверяет наличие attribute в локаторе
            if hasattr(locator, 'attribute') and locator.attribute:
                # Код вызывает get_attribute_by_locator и возвращает результат
                return await self.get_attribute_by_locator(locator)

            # Код вызывает get_webelement_by_locator и возвращает результат
            return await self.get_webelement_by_locator(locator)

        # Код вызывает _parse_locator и возвращает результат
        return await _parse_locator(locator)

    async def evaluate_locator(self, locator: SimpleNamespace) -> Optional[Union[List[Any], Any]]:
        """
         Оценивает и обрабатывает атрибуты локатора.

         Args:
             locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

         Returns:
            Optional[Union[List[Any], Any]]: Результат обработки атрибутов локатора
                 или None в случае ошибки.

        Flow Diagram:
        ```mermaid
            graph TD
            Start[Start] --> CheckIfAttributeIsList[Check if attribute is list]
            CheckIfAttributeIsList -->|Yes| IterateOverAttributes[Iterate over each attribute in list]
            IterateOverAttributes --> CallEvaluateForEachAttribute[Call _evaluate for each attribute]
            CallEvaluateForEachAttribute --> ReturnGatheredResults[Return gathered results from asyncio.gather]
            CheckIfAttributeIsList -->|No| CallEvaluateForSingleAttribute[Call _evaluate for single attribute]
            CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Return result of _evaluate]
            ReturnEvaluateResult --> End[End]
            ReturnGatheredResults --> End
        ```
        """
        async def _evaluate(locator: SimpleNamespace) -> Optional[Any]:
            """
             Внутренняя функция для оценки одного атрибута.

             Args:
                 locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

             Returns:
                 Optional[Any]: Результат оценки атрибута или None в случае ошибки.
            """
            try:
                # Код находит элемент с помощью get_webelement_by_locator
                element = await self.get_webelement_by_locator(locator)
                if not element:
                   logger.debug(f'Элемент не найден {locator=}')
                   return None
               # Код возвращает элемент, если он найден
                return element
            except Exception as ex:
                logger.error(f'Ошибка при оценке атрибута {locator=}', exc_info=ex)
                return None

        # Код проверяет, является ли атрибут списком
        if isinstance(locator.attribute, list):
             # Код вызывает _evaluate для каждого элемента списка и собирает результаты
            return await asyncio.gather(*[_evaluate(SimpleNamespace(**{**locator.__dict__, 'attribute':attribute})) for attribute in locator.attribute])

        # Код вызывает _evaluate для одного атрибута
        return await _evaluate(locator)


    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Union[str, List[str]]]:
        """
         Извлекает атрибуты из элемента или списка элементов, найденных с помощью локатора.

         Args:
            locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

         Returns:
             Optional[Union[str, List[str]]]: Атрибут или список атрибутов или None, если элемент не найден
             или произошла ошибка.
        Flow Diagram:
        ```mermaid
            graph TD
            Start[Start] --> CheckIfLocatorIsSimpleNamespaceOrDict[Check if locator is SimpleNamespace or dict]
            CheckIfLocatorIsSimpleNamespaceOrDict -->|Yes| ConvertLocatorToSimpleNamespaceIfNeeded[Convert locator to SimpleNamespace if needed]
            ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Call get_webelement_by_locator]
            CallGetWebElementByLocator --> CheckIfWebElementIsFound[Check if web_element is found]
            CheckIfWebElementIsFound -->|No| LogDebugMessageAndReturn[Log debug message and return]
            CheckIfWebElementIsFound -->|Yes| CheckIfAttributeIsDictionaryLikeString[Check if locator.attribute is a dictionary-like string]
            CheckIfAttributeIsDictionaryLikeString -->|Yes| ParseAttributeStringToDict[Parse locator.attribute string to dict]
            ParseAttributeStringToDict --> CheckIfWebElementIsList[Check if web_element is a list]
            CheckIfWebElementIsList -->|Yes| RetrieveAttributesForEachElementInList[Retrieve attributes for each element in list]
            RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Return list of attributes]
            CheckIfWebElementIsList -->|No| RetrieveAttributesForSingleWebElement[Retrieve attributes for a single web_element]
            RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes
            CheckIfAttributeIsDictionaryLikeString -->|No| CheckIfWebElementIsListAgain[Check if web_element is a list]
            CheckIfWebElementIsListAgain -->|Yes| RetrieveAttributesForEachElementInListAgain[Retrieve attributes for each element in list]
            RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Return list of attributes or single attribute]
            CheckIfWebElementIsListAgain -->|No| RetrieveAttributeForSingleWebElementAgain[Retrieve attribute for a single web_element]
            RetrieveAttributeForSingleWebElementAgain --> ReturnListOfAttributesOrSingleAttribute
            ReturnListOfAttributesOrSingleAttribute --> End[End]
            LogDebugMessageAndReturn --> End
        ```
         """
        if not isinstance(locator, SimpleNamespace):
           # Код преобразует locator в SimpleNamespace
            locator = j_loads_ns(locator)
        # Код получает веб-элемент(ы)
        element = await self.get_webelement_by_locator(locator)
        # Проверяет, найден ли элемент
        if not element:
           logger.debug(f'Элемент не найден {locator=}')
           return None
        # Проверяет, является ли атрибут строкой, похожей на словарь
        if isinstance(locator.attribute, str) and re.match(r'^[{\[].*[}\]]$', locator.attribute):
            try:
                # Код преобразует строку в словарь
                attribute_dict = j_loads_ns(locator.attribute)
            except Exception as ex:
               logger.error(f'Ошибка при парсинге атрибута как словаря {locator.attribute}', exc_info=ex)
               return None

            # Проверяет, является ли element списком
            if isinstance(element, list):
                # Код извлекает атрибуты из каждого элемента списка
                return [await self._get_attribute_from_element(elem, attribute_dict) for elem in element]
            # Код извлекает атрибуты из одного элемента
            return await self._get_attribute_from_element(element, attribute_dict)


        # Проверяет, является ли element списком
        if isinstance(element, list):
            # Код извлекает атрибуты из каждого элемента списка
            return [await self._get_attribute_from_element(elem, locator.attribute) for elem in element]

        # Код извлекает атрибут из одного элемента
        return await self._get_attribute_from_element(element, locator.attribute)

    async def _get_attribute_from_element(self, element: WebElement, attribute: Union[str, dict]) -> Optional[Union[str, dict]]:
        """
          Внутренняя функция для извлечения атрибута из веб-элемента.

          Args:
             element (WebElement): веб-элемент.
             attribute (Union[str, dict]): атрибут, который нужно извлечь.

          Returns:
               Optional[Union[str, dict]]: значение атрибута или None в случае ошибки.
        """
        try:
            if isinstance(attribute, dict):
                 # Код получает атрибут элемента и возвращает результат
                return {key: element.get_attribute(value) for key,value in attribute.items()}

            # Код получает атрибут элемента и возвращает результат
            return element.get_attribute(attribute)
        except Exception as ex:
            logger.error(f'Ошибка при получении атрибута {attribute} элемента {element}', exc_info=ex)
            return None


    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элемент(ы) на основе заданного локатора.

        Args:
            locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

        Returns:
           Optional[Union[WebElement, List[WebElement]]]: Веб-элемент или список веб-элементов
                или None, если элемент не найден.
        """
        try:
            # Код проверяет наличие by и selector в локаторе
            if not all([getattr(locator, 'by', None), getattr(locator, 'selector', None)]):
                 # Если не найден, возвращает None
                logger.debug(f'Невалидный локатор {locator=}')
                return None

            by = self.by_mapping.get(locator.by.upper())

            if not by:
                 # Если by не найден, возвращает None
                logger.debug(f'Невалидный by {locator.by=}')
                return None

            # Код проверяет наличие multiple в локаторе
            if hasattr(locator, 'multiple') and locator.multiple:
                # Код находит все элементы с помощью find_elements и возвращает результат
               elements = self.driver.find_elements(by, locator.selector)
               if not elements:
                    logger.debug(f'Элементы не найдены {locator=}')
               return elements
            # Код находит элемент с помощью find_element и возвращает результат
            element = self.driver.find_element(by, locator.selector)
            if not element:
                 logger.debug(f'Элемент не найден {locator=}')
            return element
        except Exception as ex:
            logger.error(f'Ошибка поиска элемента {locator=}', exc_info=ex)
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, path: str) -> bool:
        """
        Делает скриншот веб-элемента.

        Args:
            locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.
            path (str): Путь для сохранения скриншота.

        Returns:
            bool: True, если скриншот сделан успешно, False в противном случае.
        """
        try:
            # Код находит веб-элемент с помощью get_webelement_by_locator
            element = await self.get_webelement_by_locator(locator)
            if not element:
               return False
            # Код делает и сохраняет скриншот элемента
            element.screenshot(path)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при создании скриншота {locator=}, path={path}', exc_info=ex)
            return False

    async def execute_event(self, locator: SimpleNamespace) -> Optional[Any]:
         """
          Выполняет событие, связанное с локатором.

          Args:
            locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.

          Returns:
             Optional[Any]: Результат выполнения события или None в случае ошибки.
        """
         try:
            # Код получает элемент с помощью get_webelement_by_locator
            element = await self.get_webelement_by_locator(locator)

            if not element:
                return None
            # Код выполняет действие в зависимости от типа события
            if 'click' in locator.event:
                element.click()
            elif 'send_keys' in locator.event:
                # Извлекает текст из события
                match = re.search(r'send_keys\((.*?)\)', locator.event)
                if match:
                    text = match.group(1).strip('\'"')
                    element.send_keys(text)
            elif 'hover' in locator.event:
                # Код выполняет наведение курсора на элемент
                self.actions.move_to_element(element).perform()
            return True
         except Exception as ex:
              logger.error(f'Ошибка при выполнении события {locator=}', exc_info=ex)
              return None


    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        Args:
            locator (SimpleNamespace): SimpleNamespace, содержащий параметры локатора.
            message (str): Сообщение для отправки.

        Returns:
             bool: True, если сообщение отправлено успешно, False в противном случае.
        """
        try:
             # Код получает элемент с помощью get_webelement_by_locator
            element = await self.get_webelement_by_locator(locator)
            if not element:
               return False
            # Код отправляет сообщение
            element.send_keys(message)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при отправке сообщения {message} в элемент {locator=}', exc_info=ex)
            return False
```