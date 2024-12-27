# Анализ кода модуля `executor`

**Качество кода**
9
-  Плюсы
    -   Хорошо структурированный и подробный `README.md` с описанием функциональности модуля, классов и их методов.
    -   Наличие диаграмм потоков Mermaid для визуализации логики работы основных методов.
    -   Примеры использования кода и перечень зависимостей.
    -   Описание обработки ошибок.
-  Минусы
    -   Не используются docstring в коде для описания классов и методов.
    -   Отсутствует логирование ошибок через `src.logger.logger`.
    -   Используется `json.loads` вместо `j_loads` или `j_loads_ns`.
    -   Не все импорты могут быть необходимы.

**Рекомендации по улучшению**

1.  **Добавить docstring**: Добавить документацию в формате reStructuredText (RST) для всех классов, методов и переменных.
2.  **Использовать `j_loads_ns`**: Заменить использование `json.loads` на `j_loads_ns` для загрузки JSON.
3.  **Логирование ошибок**: Использовать `logger.error` вместо `try-except` для обработки ошибок, где это возможно.
4.  **Уточнить импорты**: Проверить и оставить только необходимые импорты, убрать лишние.
5. **Рефакторинг**: Улучшить читаемость и переименовать переменные.
6. **Соответствие стандартам**: Привести код к единому стилю, включая использование одинарных кавычек и аннотаций типов.

**Оптимизированный код**

```python
"""
Модуль для выполнения действий с веб-элементами на основе локаторов.
====================================================================

Этот модуль предоставляет класс `ExecuteLocator` для взаимодействия с веб-элементами
на веб-странице с использованием Selenium WebDriver. Он обрабатывает локаторы
для поиска элементов, выполнения действий (клики, отправка сообщений) и
извлечения атрибутов.

Пример использования
--------------------

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = {
        "by": "ID",
        "selector": "some_element_id",
        "event": "click()"
    }

    # Выполнение локатора
    result = await executor.execute_locator(locator)
    print(result)
"""
import asyncio
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Union
# from typing import Any, Dict, List, Optional, Union # Исправлено опечатку
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException #не используется
from src.utils.jjson import j_loads_ns # Исправлено импорт
from src.logger.logger import logger #добавлен импорт логера


class EventType(str, Enum):
    """
    Перечисление типов событий для веб-элементов.

    Поддерживаемые типы:
      - click
      - send_keys
      - set_value
    """

    CLICK = 'click()'
    SEND_KEYS = 'send_keys'
    SET_VALUE = 'set_value'


@dataclass
class Locator:
    """
    Класс для представления локатора веб-элемента.

    Атрибуты:
        by (str): Тип локатора (например, 'ID', 'XPATH', 'CSS_SELECTOR').
        selector (str): Значение локатора.
        event (str, optional): Событие, которое нужно выполнить.
        attribute (str, optional): Атрибут для извлечения.
        wait (int, optional): Время ожидания элемента в секундах.
        mandatory (bool, optional): Является ли элемент обязательным.
        message (str, optional): Сообщение для отправки.
    """
    by: str
    selector: str
    event: Optional[str] = None
    attribute: Optional[str] = None
    wait: Optional[int] = 10
    mandatory: Optional[bool] = True
    message: Optional[str] = None


class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.

    Args:
        driver (WebDriver): Экземпляр Selenium WebDriver.
        mode (str, optional): Режим выполнения (например, 'debug', 'dev'). Defaults to 'dev'.

    Attributes:
        driver (WebDriver): Экземпляр Selenium WebDriver.
        actions (ActionChains): Объект ActionChains для выполнения сложных действий.
        by_mapping (dict): Словарь, сопоставляющий типы локаторов с методами By Selenium.
        mode (str): Режим выполнения.
    """

    def __init__(self, driver: WebDriver, mode: str = 'dev') -> None:
        """Инициализирует класс ExecuteLocator."""
        self.driver = driver
        self.actions = ActionChains(driver) if driver else None
        self.by_mapping = {
            'ID': By.ID,
            'XPATH': By.XPATH,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'CLASS_NAME': By.CLASS_NAME,
            'NAME': By.NAME,
            'LINK_TEXT': By.LINK_TEXT,
            'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
            'TAG_NAME': By.TAG_NAME
        }
        self.mode = mode

    async def execute_locator(self, locator: Union[dict, SimpleNamespace]) -> Any:
        """
        Выполняет действие с веб-элементом на основе предоставленного локатора.

        Args:
            locator (Union[dict, SimpleNamespace]): Локатор веб-элемента.

        Returns:
            Any: Результат выполнения действия или None в случае ошибки.
        """
        # проверяем тип локатора и преобразовываем его в SimpleNamespace, если нужно
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        async def _parse_locator(locator: SimpleNamespace) -> Any:
             """
            Внутренняя функция для обработки локатора.

            Args:
                locator (SimpleNamespace): Локатор веб-элемента.

            Returns:
                Any: Результат обработки локатора.
            """
             # Проверка на наличие обязательных атрибутов или событий.
             if not any([locator.event, locator.attribute, locator.mandatory]):
                return None

             try:
                 # Сопоставляем тип локатора и извлекаем атрибут, если нужно.
                by = self.by_mapping.get(locator.by)
                if not by:
                    logger.error(f"Неподдерживаемый тип локатора: {locator.by}")
                    return None
                if locator.attribute:
                     return await self.get_attribute_by_locator(locator)
                 # Проверяем наличие события.
                if locator.event:
                   return await self.execute_event(locator)

                return await self.get_webelement_by_locator(locator)
             except Exception as ex:
                  logger.error(f"Ошибка при обработке локатора {locator}", exc_info=ex)
                  return None
        return await _parse_locator(locator)

    async def evaluate_locator(self, locator: Union[dict, SimpleNamespace]) -> Optional[Union[List, Any]]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            locator (Union[dict, SimpleNamespace]): Локатор веб-элемента.

        Returns:
            Optional[Union[List, Any]]: Список результатов или одиночный результат, или None, если не удалось.
        """
        # проверяем тип локатора и преобразовываем его в SimpleNamespace, если нужно
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        async def _evaluate(locator: SimpleNamespace) -> Any:
           """
           Внутренняя функция для извлечения атрибутов.

           Args:
               locator (SimpleNamespace): Локатор веб-элемента.

           Returns:
               Any: Результат извлечения атрибута.
           """
           try:
               if not locator.attribute:
                    return None
               return await self.get_attribute_by_locator(locator)
           except Exception as ex:
                logger.error(f"Ошибка при оценке локатора: {locator}", exc_info=ex)
                return None
        if isinstance(locator.attribute, list):
            return await asyncio.gather(*(_evaluate(locator) for locator in locator.attribute))
        return await _evaluate(locator)


    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Union[List, Any]]:
         """
         Извлекает атрибуты из веб-элемента или списка элементов.

         Args:
             locator (SimpleNamespace): Локатор веб-элемента.

         Returns:
             Optional[Union[List, Any]]: Список атрибутов или один атрибут, или None, если не удалось.
         """
         if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
         try:
             element = await self.get_webelement_by_locator(locator)
             if not element:
                  logger.debug(f'Элемент не найден {locator=}')
                  return None
             if isinstance(locator.attribute, str) and locator.attribute.startswith('{'):
                try:
                    attribute_dict = j_loads_ns(locator.attribute)
                except Exception as ex:
                    logger.error(f"Ошибка парсинга строки в словарь: {locator.attribute}", exc_info=ex)
                    return None
                if isinstance(element, list):
                    return [ await self._get_attribute(attr, el) for el in element for attr in attribute_dict ]
                return [ await self._get_attribute(attr, element) for attr in attribute_dict ]
             if isinstance(element, list):
                return [ await self._get_attribute(locator.attribute, el) for el in element ]
             return await self._get_attribute(locator.attribute, element)
         except Exception as ex:
              logger.error(f"Ошибка при получении атрибута: {locator}", exc_info=ex)
              return None

    async def _get_attribute(self, attribute: str, element: Any) -> Optional[Any]:
        """
        Вспомогательный метод для извлечения одного атрибута.

        Args:
             attribute (str): Название атрибута.
             element (Any): Веб-элемент.

        Returns:
             Optional[Any]: Значение атрибута или None.
        """
        try:
            return element.get_attribute(attribute)
        except Exception as ex:
           logger.error(f'Ошибка при получении атрибута "{attribute}" из элемента {element}', exc_info=ex)
           return None


    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[List, Any]]:
        """
        Извлекает веб-элемент(ы) на основе предоставленного локатора.

        Args:
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            Optional[Union[List, Any]]: Веб-элемент или список элементов, или None, если не найдены.
        """
        by = self.by_mapping.get(locator.by)
        if not by:
            logger.error(f"Неподдерживаемый тип локатора: {locator.by}")
            return None
        try:
            wait = WebDriverWait(self.driver, locator.wait)

            if not locator.mandatory:
                elements = self.driver.find_elements(by, locator.selector)
                if self.mode == 'debug':
                    logger.debug(f'Найдено {len(elements)} элементов по локатору {locator}')
                return elements if elements else None

            elements = wait.until(
                ec.presence_of_all_elements_located((by, locator.selector))
                )
            if self.mode == 'debug':
                logger.debug(f'Найдено {len(elements)} элементов по локатору {locator}')
            return elements if len(elements) > 1 else elements[0]

        except Exception as ex:
             logger.error(f'Элемент не найден {locator=}', exc_info=ex)
             return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, path: Path) -> bool:
         """
         Делает скриншот веб-элемента.

         Args:
             locator (SimpleNamespace): Локатор веб-элемента.
             path (Path): Путь для сохранения скриншота.

         Returns:
             bool: True, если скриншот сделан успешно, False в противном случае.
         """
         element = await self.get_webelement_by_locator(locator)
         if not element:
             logger.debug(f'Элемент для скриншота не найден {locator=}')
             return False
         try:
            element.screenshot(path)
            return True
         except Exception as ex:
              logger.error(f"Не удалось сделать скриншот элемента: {locator}", exc_info=ex)
              return False


    async def execute_event(self, locator: SimpleNamespace) -> bool:
        """
        Выполняет событие с веб-элементом.

        Args:
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            bool: True, если событие выполнено успешно, False в противном случае.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Элемент для события не найден {locator=}')
            return False
        event_type =  locator.event.split('(')[0]

        try:
           if event_type == EventType.CLICK:
                element.click()
                return True
           if event_type == EventType.SEND_KEYS:
               if not locator.message:
                    logger.error(f'Для события {EventType.SEND_KEYS} нужно передать параметр `message` {locator=}')
                    return False
               element.send_keys(locator.message)
               return True
           if event_type == EventType.SET_VALUE:
               if not locator.message:
                    logger.error(f'Для события {EventType.SET_VALUE} нужно передать параметр `message` {locator=}')
                    return False
               self.driver.execute_script(f'arguments[0].value = "{locator.message}";', element)
               return True
           return False
        except Exception as ex:
             logger.error(f'Не удалось выполнить событие {locator.event} для элемента {locator=}', exc_info=ex)
             return False

    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
       """
       Отправляет сообщение веб-элементу.

       Args:
            locator (SimpleNamespace): Локатор веб-элемента.
            message (str): Сообщение для отправки.

       Returns:
            bool: True, если сообщение отправлено успешно, False в противном случае.
       """
       if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
       try:
           locator.message = message
           locator.event = EventType.SEND_KEYS
           return await self.execute_event(locator)
       except Exception as ex:
            logger.error(f'Не удалось отправить сообщение {message} для элемента {locator=}', exc_info=ex)
            return False

```