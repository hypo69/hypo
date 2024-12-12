# Анализ кода модуля `executor.py`

**Качество кода**
9
- Плюсы
    -  Код хорошо структурирован, с чётким разделением на классы и методы.
    -  Используются асинхронные операции, что хорошо для производительности.
    -  Присутствуют подробные комментарии, описывающие работу различных частей кода.
    -  Реализована обработка ошибок с логированием.
    -  Применены `SimpleNamespace` для работы с конфигурацией локаторов.
    -  Имеются диаграммы Mermaid, визуализирующие логику работы основных методов.
    -  Предоставлено описание модуля в формате RST.
- Минусы
    -  Не все комментарии соответствуют стандарту RST, что усложняет автоматическую генерацию документации.
    -  Некоторые участки кода могут быть переписаны для лучшей читаемости и производительности.
    -  Отсутствуют некоторые необходимые импорты, например, `src.utils.jjson`.
    -  Используется стандартный `json.loads` вместо `j_loads` из `src.utils.jjson`.
    -  Не всегда используются полные docstring для функций и методов.
    -  Присутствует избыточное использование блоков `try-except`.

**Рекомендации по улучшению**

1.  **Форматирование комментариев:** Привести все комментарии к стандарту reStructuredText (RST), особенно docstrings.
2.  **Использование `j_loads`:** Заменить `json.loads` на `j_loads_ns` для загрузки JSON.
3.  **Логирование ошибок:** Вместо блоков `try-except` использовать `logger.error` для логирования ошибок и продолжения выполнения.
4.  **Добавить необходимые импорты:** Добавить отсутствующие импорты, такие как `j_loads_ns` и `logger`.
5.  **Рефакторинг методов:** Улучшить читаемость и производительность методов, где это необходимо.
6.  **Улучшить docstrings:** Добавить docstrings ко всем функциям, методам и классам, включая описания параметров и возвращаемых значений.
7.  **Избавиться от избыточных проверок:** Оптимизировать проверки на типы данных и условий.
8.  **Придерживаться единого стиля именования:** Убедиться, что имена переменных и методов соответствуют ранее обработанным файлам.
9. **Удалить избыточные диаграмы** Диаграмы Mermaid уже есть в README файле, в коде они будут избыточными

**Оптимизированный код**

```python
"""
Модуль для управления взаимодействиями с веб-элементами.
===========================================================

Этот модуль предоставляет класс :class:`ExecuteLocator` для автоматизации
взаимодействий с веб-элементами с использованием Selenium.
Он позволяет находить, взаимодействовать и извлекать информацию с веб-страниц.

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
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns  # Исправлено: импорт j_loads_ns
from json import JSONDecodeError


@dataclass
class Locator:
    """
    Представляет структуру локатора.

    :param by: Метод поиска элемента (например, "ID", "XPATH", "CLASS_NAME").
    :param selector: Селектор для поиска элемента.
    :param event: Событие для выполнения (например, "click()", "send_keys('text')").
    :param attribute: Атрибут для получения (например, "value", "text").
    :param mandatory: Флаг, указывающий на обязательность нахождения элемента.
    :param delay: Задержка перед выполнением действия.
    :param name: Имя локатора.
    """
    by: str
    selector: str
    event: Optional[str] = None
    attribute: Optional[Union[str, List[str]]] = None
    mandatory: Optional[bool] = False
    delay: Optional[int] = 0
    name: Optional[str] = None


class ByType(str, Enum):
    """
    Перечисление типов поиска элементов.
    """
    ID = "id"
    XPATH = "xpath"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :param actions: Экземпляр ActionChains для выполнения сложных действий.
    :param by_mapping: Словарь, отображающий типы локаторов на методы By.
    :param mode: Режим работы (например, "debug", "dev").
    """
    driver: WebDriver
    actions: ActionChains = field(init=False)
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        ByType.ID: By.ID,
        ByType.XPATH: By.XPATH,
        ByType.CLASS_NAME: By.CLASS_NAME,
        ByType.CSS_SELECTOR: By.CSS_SELECTOR,
        ByType.LINK_TEXT: By.LINK_TEXT,
        ByType.PARTIAL_LINK_TEXT: By.PARTIAL_LINK_TEXT,
        ByType.NAME: By.NAME,
        ByType.TAG_NAME: By.TAG_NAME,
    })
    mode: str = "dev"

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)


    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Any:
        """
        Выполняет действия с веб-элементом на основе предоставленного локатора.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :return: Результат выполнения действия.
        """
        # Проверка типа локатора и преобразование в SimpleNamespace
        if not isinstance(locator, SimpleNamespace):
            locator = j_loads_ns(locator) if isinstance(locator, str) else SimpleNamespace(**locator)
            # locator = SimpleNamespace(**locator) # Заменено на j_loads_ns для обработки строк
        
        async def _parse_locator(locator: SimpleNamespace) -> Any:
           """
           Внутренняя функция для обработки локатора и выполнения действий.

           :param locator: Локатор в формате SimpleNamespace.
           :return: Результат обработки локатора.
           """
           if not any([locator.event, locator.attribute, locator.mandatory]):
                return None

           try:
               # Проверка и установка метода поиска элемента
               by = self.by_mapping.get(locator.by.lower())
               if not by:
                   logger.error(f'Неизвестный метод поиска: {locator.by}')
                   return None

               # Вызов _evaluate для получения результатов атрибута
               if locator.attribute:
                   attribute_result = await self._evaluate(locator)
                   return attribute_result

               # Выполнение события
               if locator.event:
                   event_result = await self.execute_event(locator)
                   return event_result

               # Получение элемента, если атрибут или событие не определены
               element_result = await self.get_webelement_by_locator(locator)
               return element_result


           except Exception as ex:
               logger.error(f"Ошибка при обработке локатора: {locator}", exc_info=ex)
               return None
        # Вызов внутренней функции _parse_locator для обработки локатора
        return await _parse_locator(locator)


    async def _evaluate(self, locator: SimpleNamespace) -> Optional[Union[List[Any], Any]]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор в формате SimpleNamespace.
        :return: Результат обработки атрибутов.
        """
        if isinstance(locator.attribute, list):
            results = await asyncio.gather(*[self._evaluate_attribute(locator, attr) for attr in locator.attribute])
            return results
        return await self._evaluate_attribute(locator, locator.attribute)

    async def _evaluate_attribute(self, locator: SimpleNamespace, attribute: str) -> Any:
      """
      Вспомогательная функция для оценки одного атрибута локатора.

      :param locator: Локатор в формате SimpleNamespace.
      :param attribute: Атрибут для оценки.
      :return: Результат оценки атрибута.
      """
      try:
         return await self.get_attribute_by_locator(
                SimpleNamespace(**{**locator.__dict__, "attribute": attribute})
            )
      except Exception as ex:
          logger.error(f"Ошибка при оценке атрибута {attribute} локатора: {locator}", exc_info=ex)
          return None


    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Union[List[Any], Any]]:
        """
        Извлекает атрибут(ы) из элемента(-ов) на основе локатора.

        :param locator: Локатор в формате SimpleNamespace.
        :return: Значение атрибута или список значений.
        """
        # Преобразование в SimpleNamespace, если это словарь
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        element = await self.get_webelement_by_locator(locator)

        # Проверка, найден ли элемент
        if not element:
            logger.debug(f"Элемент не найден: {locator}")
            return None

        # Обработка атрибута, если это строка в формате JSON
        if isinstance(locator.attribute, str) and locator.attribute.startswith("{") and locator.attribute.endswith("}"):
            try:
                attribute_dict = j_loads_ns(locator.attribute)
                # attribute_dict = json.loads(locator.attribute) # Заменено на j_loads_ns
            except (JSONDecodeError, TypeError) as ex:
                 logger.error(f"Ошибка при разборе JSON из атрибута: {locator.attribute}", exc_info=ex)
                 return None
            if isinstance(element, list):
                return [
                    {key: el.get_attribute(value) for key, value in attribute_dict.items()}
                    for el in element
                ]
            return {key: element.get_attribute(value) for key, value in attribute_dict.items()}

        # Получение атрибута для одного элемента или списка элементов
        if isinstance(element, list):
            return [el.get_attribute(locator.attribute) for el in element]
        return element.get_attribute(locator.attribute)

    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элемент(ы) на основе локатора.

        :param locator: Локатор в формате SimpleNamespace.
        :return: Веб-элемент или список веб-элементов.
        """
        by = self.by_mapping.get(locator.by.lower())
        if not by:
            logger.error(f'Неизвестный метод поиска: {locator.by}')
            return None
        try:
          if locator.selector.startswith('(') and locator.selector.endswith(')'):
              elements = self.driver.find_elements(by, locator.selector)
              if not elements:
                   logger.debug(f"Элементы не найдены: {locator}")
                   return None
              return elements
          element = self.driver.find_element(by, locator.selector)
          return element
        except Exception as ex:
            logger.error(f"Элемент не найден по локатору: {locator}", exc_info=ex)
            return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, path: Path) -> Optional[bool]:
        """
        Делает снимок экрана веб-элемента и сохраняет его в файл.

        :param locator: Локатор в формате SimpleNamespace.
        :param path: Путь для сохранения снимка экрана.
        :return: True, если снимок экрана сделан успешно, иначе None.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f"Элемент не найден для снимка экрана: {locator}")
            return None
        try:
            element.screenshot(path)
            return True
        except Exception as ex:
            logger.error(f"Не удалось сделать снимок экрана элемента: {locator}", exc_info=ex)
            return None


    async def execute_event(self, locator: SimpleNamespace) -> Optional[bool]:
        """
        Выполняет событие для веб-элемента.

        :param locator: Локатор в формате SimpleNamespace.
        :return: True, если событие выполнено успешно, иначе None.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f"Элемент не найден для выполнения события: {locator}")
            return None

        try:
            event = locator.event
            if event.startswith("send_keys"):
                match = re.search(r"\('(.+)'\)", event)
                if match:
                    value = match.group(1)
                    element.send_keys(value)
                    return True
            if event == "click()":
                element.click()
                return True
            if event.startswith("move_to_element"):
                 self.actions.move_to_element(element).perform()
                 return True
            return False

        except Exception as ex:
            logger.error(f"Ошибка при выполнении события: {locator.event} для элемента {locator}", exc_info=ex)
            return None


    async def send_message(self, locator: SimpleNamespace, message: str) -> Optional[bool]:
        """
        Отправляет сообщение в веб-элемент.

        :param locator: Локатор в формате SimpleNamespace.
        :param message: Сообщение для отправки.
        :return: True, если сообщение отправлено успешно, иначе None.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
             logger.debug(f"Элемент не найден для отправки сообщения: {locator}")
             return None
        try:
            element.send_keys(message)
            return True
        except Exception as ex:
            logger.error(f"Ошибка при отправке сообщения в элемент: {locator}", exc_info=ex)
            return None
```