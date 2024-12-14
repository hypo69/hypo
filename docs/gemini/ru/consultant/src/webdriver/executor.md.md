# Анализ кода модуля `executor.py`

**Качество кода**
7
- Плюсы
    - Код хорошо документирован с использованием reStructuredText (RST).
    -  Присутствуют подробные блок-схемы, описывающие логику выполнения ключевых функций.
    -  Используются асинхронные операции, что повышает производительность.
    -  Имеется базовая обработка ошибок с использованием `try-except` блоков.
- Минусы
    - Не хватает обработки ошибок с использованием `logger.error` и `...` вместо `try-except` блоков.
    -  Некоторые функции не имеют подробного RST описания.
    -  Импорты не соответствуют ранее обработанным файлам (отсутствуют необходимые, присутствуют лишние).

**Рекомендации по улучшению**
1. **Использовать `logger.error`**: Заменить `try-except` блоки на `logger.error` для логирования ошибок и `...` как точки остановки.
2. **Добавить RST документацию**: Добавить подробные docstring в формате RST для всех функций, методов и классов.
3. **Уточнить импорты**: Привести импорты в соответствие с ранее обработанными файлами и добавить необходимые.
4. **Улучшить именование**: Убедиться, что все имена функций, переменных и импортов соответствуют соглашениям и ранее обработанным файлам.
5. **Убрать лишние комментарии**: Убрать лишние комментарии, не несущие смысловой нагрузки.

**Оптимизированный код**
```python
"""
Модуль для управления и взаимодействия с веб-элементами с использованием Selenium.
==============================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который позволяет автоматизировать взаимодействие с веб-элементами.
Он включает в себя функции для поиска элементов, выполнения действий, отправки сообщений и получения атрибутов.
Модуль также поддерживает обработку ошибок и асинхронные операции.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

   from selenium import webdriver
   from src.webdriver.executor import ExecuteLocator

   # инициализация веб-драйвера
   driver = webdriver.Chrome()

   # инициализация ExecuteLocator
   executor = ExecuteLocator(driver=driver)

   # определение локатора
   locator = {
       "by": "ID",
       "selector": "some_element_id",
       "event": "click()"
   }

   # выполнение локатора
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
# from src.utils.jjson import j_loads, j_loads_ns # TODO импортировать из файла jjson
from src.logger.logger import logger


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.
    
    :param driver: Экземпляр Selenium WebDriver.
    :param actions: Экземпляр ActionChains для выполнения сложных действий.
    :param by_mapping: Словарь, связывающий типы локаторов с методами By.
    :param mode: Режим выполнения.
    """
    driver: WebDriver = None
    actions: ActionChains = field(init=False)
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        'ID': By.ID,
        'XPATH': By.XPATH,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'NAME': By.NAME,
        'TAG_NAME': By.TAG_NAME,
        'CLASS_NAME': By.CLASS_NAME,
        'CSS_SELECTOR': By.CSS_SELECTOR
    })
    mode: str = 'debug'

    def __post_init__(self):
        """Инициализирует ActionChains, если предоставлен драйвер."""
        if self.driver:
             self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Any:
        """
        Выполняет действия с веб-элементом на основе предоставленного локатора.
        
        :param locator: Локатор в виде словаря или SimpleNamespace.
        :return: Результат выполнения действий с элементом.
        """
        # Проверка типа локатора
        if isinstance(locator, dict):
           # преобразование словаря в SimpleNamespace
            locator = SimpleNamespace(**locator)

        async def _parse_locator(locator: SimpleNamespace) -> Any:
            """
            Внутренняя функция для обработки локатора.
            
            :param locator: Локатор в виде SimpleNamespace.
            :return: Результат обработки локатора.
            """
            if not any([getattr(locator, 'event', None), getattr(locator, 'attribute', None), getattr(locator, 'mandatory', None)]):
                return None
            
            try:
                # определение By
                by = self.by_mapping.get(locator.by)
                # оценка атрибута
                if hasattr(locator, 'attribute'):
                    result = await self.evaluate_locator(locator)
                    return result
                elif hasattr(locator, 'event'):
                    result = await self.execute_event(locator)
                    return result
                else:
                    result = await self.get_webelement_by_locator(locator)
                    return result
            except Exception as ex:
                logger.error(f'Ошибка при обработке локатора: {locator=}', ex)
                ...
                return None


        return await _parse_locator(locator)

    async def evaluate_locator(self, locator: SimpleNamespace) -> Any:
        """
        Оценивает атрибуты локатора.
        
        :param locator: Локатор в виде SimpleNamespace.
        :return: Результат оценки атрибутов.
        """
        
        async def _evaluate(locator: SimpleNamespace, attr) -> Any:
                """
                Внутренняя функция для оценки одного атрибута.
                
                :param locator: Локатор в виде SimpleNamespace.
                :param attr: Атрибут для оценки.
                :return: Результат оценки атрибута.
                """
                try:
                    if attr.startswith('text()'):
                        # получение текста элемента
                         element = await self.get_webelement_by_locator(locator)
                         return element.text if element else None
                    elif attr.startswith('get_attribute('):
                        # получение атрибута элемента
                        attribute_name = attr.split('get_attribute(')[1].split(')')[0].strip()
                        return await self.get_attribute_by_locator(locator,attribute_name=attribute_name)
                    elif attr.startswith('screenshot('):
                        # получение скриншота элемента
                        return await self.get_webelement_as_screenshot(locator)
                    else:
                        return await self.get_attribute_by_locator(locator, attribute_name=attr)
                except Exception as ex:
                    logger.error(f'Ошибка при оценке атрибута: {attr=}, {locator=}', ex)
                    ...
                    return None

        if isinstance(locator.attribute, list):
            # оценка списка атрибутов
            tasks = [_evaluate(locator, attr) for attr in locator.attribute]
            return await asyncio.gather(*tasks)
        else:
            # оценка одного атрибута
            return await _evaluate(locator, locator.attribute)

    async def get_attribute_by_locator(self, locator: Union[Dict, SimpleNamespace], attribute_name: str = None) -> Any:
        """
        Получает значение атрибута элемента или списка элементов по локатору.
        
        :param locator: Локатор в виде словаря или SimpleNamespace.
        :param attribute_name: Имя атрибута для получения.
        :return: Значение атрибута или список значений.
        """
        if isinstance(locator, dict):
             locator = SimpleNamespace(**locator)

        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            return None

        if isinstance(element, list):
             if isinstance(attribute_name, str) and attribute_name.startswith('{'):
                 try:
                    attribute_name = eval(attribute_name)
                 except Exception as ex:
                    logger.error(f'Ошибка при парсинге {attribute_name=}', ex)
                    ...
                    return None

                 if isinstance(attribute_name,dict):
                      return [
                        {key: el.get_attribute(value) for key, value in attribute_name.items()}
                        for el in element if el
                    ]
             else:
               return [el.get_attribute(attribute_name) for el in element if el]
        else:
           return element.get_attribute(attribute_name) if element else None


    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Получает веб-элемент или список веб-элементов по локатору.
        
        :param locator: Локатор в виде SimpleNamespace.
        :return: Веб-элемент или список веб-элементов, или None если не найден.
        """
        by = self.by_mapping.get(locator.by)
        selector = locator.selector
        try:
            if  hasattr(locator,'many') and locator.many:
                # поиск всех элементов
                elements = WebDriverWait(self.driver, 10).until(
                   ec.presence_of_all_elements_located((by, selector))
                )
                return elements
            else:
                # поиск одного элемента
                element = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((by, selector))
                )
                return element
        except (TimeoutException, StaleElementReferenceException) as ex:
            logger.error(f'Элемент не найден по локатору: {locator=}', ex)
            ...
            return None
    
    async def get_webelement_as_screenshot(self, locator: SimpleNamespace) -> Optional[str]:
        """
        Делает скриншот веб-элемента, найденного по локатору.
        
        :param locator: Локатор в виде SimpleNamespace.
        :return: Base64-encoded строка изображения или None если не найден.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            return None

        try:
            # получение скриншота элемента в формате base64
            return element.screenshot_as_base64
        except Exception as ex:
           logger.error(f'Не удалось получить скриншот элемента: {locator=}', ex)
           ...
           return None


    async def execute_event(self, locator: SimpleNamespace) -> Optional[bool]:
        """
        Выполняет событие с веб-элементом, найденным по локатору.
        
        :param locator: Локатор в виде SimpleNamespace.
        :return: True если событие выполнено, иначе None.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            return None

        try:
            event = locator.event
            if event.startswith('click()'):
                # выполнение клика
                element.click()
            elif event.startswith('send_keys('):
                # отправка сообщения
                keys = event.split('send_keys(')[1].split(')')[0].strip()
                await self.send_message(locator, keys)
            elif event.startswith('hover()'):
                # наведение курсора мыши
                self.actions.move_to_element(element).perform()
            elif event.startswith('scroll_to_element()'):
                # прокрутка до элемента
                 self.driver.execute_script("arguments[0].scrollIntoView();", element)
            elif event.startswith('js_click()'):
                # клик через JavaScript
                 self.driver.execute_script("arguments[0].click();", element)
            else:
                logger.debug(f'Неизвестное событие: {event=}')
                return None
            return True
        except Exception as ex:
            logger.error(f'Не удалось выполнить событие: {event=}, {locator=}', ex)
            ...
            return None
    
    async def send_message(self, locator: SimpleNamespace, message: str) -> Optional[bool]:
        """
        Отправляет сообщение веб-элементу, найденному по локатору.
        
        :param locator: Локатор в виде SimpleNamespace.
        :param message: Сообщение для отправки.
        :return: True если сообщение отправлено, иначе None.
        """
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            return None

        try:
           # отправка сообщения
            element.send_keys(message)
            return True
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение: {message=}, {locator=}', ex)
            ...
            return None
```