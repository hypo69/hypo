## Анализ кода модуля `executor.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и использует классы и асинхронные функции для управления веб-элементами.
    -  Используются dataclass для хранения данных.
    - Присутствует подробная документация в виде docstrings.
    -  Логирование осуществляется через `logger`.
    - Используются `SimpleNamespace` для гибкой работы с данными локатора.
    - Присутствует обработка исключений.
    - Используется асинхронность для неблокирующих операций.
-  Минусы
    -  Не везде используется `asyncio.to_thread` для блокирующих операций.
    -  Есть места, где `try-except` можно упростить с использованием `logger.error`.
    - В некоторых местах отсутствует проверка на None при использовании результатов функций.
    - Дублирование логирования ошибки в `_parse_dict_string`
    -   В `send_message` не используется `asyncio.to_thread`, что может блокировать eventloop.
    -  В `send_message` для отправки клавиш, захардкожены клавиши `SHIFT+ENTER` вместо использования  `replace_dict`
    - В `send_message` используется continue вместо `return False` при ошибке.
    - В `get_webelement_by_locator` в блоке `if timeout == 0` не используется `await asyncio.to_thread` при вызове `driver.find_elements`, что может блокировать eventloop.
    - В `get_webelement_by_locator` есть `raise ValueError`, но не обрабатывается в вызывающей функции.
    - `from src.logger.logger import logger` не используется во всем модуле
    - `...` не используется для останова кода. 
    - В `execute_event` используется continue вместо `return False` при ошибке.
    - В `execute_event` дублируется код при вызове `click` при возникновении исключения.
    - В `execute_event` можно заменить `if event == "clear()"` и другие `elif` на `match-case`.
    - В `get_attribute_by_locator` не используется `await asyncio.to_thread` для  `web_element.get_attribute`, что может блокировать eventloop.

**Рекомендации по улучшению**

1.  **Логирование**:
    -   Заменить использование `print` на `logger.debug` или `logger.error` для стандартизации логирования.
    -   Улучшить форматирование сообщений об ошибках в `logger.error`.
2.  **Обработка ошибок**:
    -   Вместо `try-except` с пустым `except` использовать `logger.error` для отлова и логирования исключений.
    -   Проверить все места, где есть `...` и добавить обработку ошибок или возвращать `None` / `False`.
    -   В функции `get_attribute_by_locator` заменить множественный вызов logger.debug на один.
3.  **Асинхронность**:
    -   Использовать `await asyncio.to_thread` для всех блокирующих операций (например, `driver.find_elements`, `web_element.click`, `web_element.send_keys`, `web_element.get_attribute` и т.д.)
    -   Проверить все методы на предмет блокирующих вызовов и перевести их в неблокирующие.
4.  **Структура кода**:
    -   Удалить `...` как точки остановки.
    -   Улучшить документацию: добавить примеры использования для всех методов и классов.
    -   В `send_message`  заменить захардкоженные значения на использование `replace_dict`.
    -   В `send_message` заменить `continue` на `return False` при ошибке.
    -   В `execute_event` заменить множественные `if-elif` на `match-case`.
    -   Удалить `continue`  из `execute_event`  и возвращать `return False` при ошибке.
    -  В `execute_event` перенести дублирующийся код обработки ошибок в отдельную функцию.
5.  **Улучшения**:
    -   Добавить проверку на `None` перед использованием результатов функций.
    -   Привести все имена переменных и функций в соответствие с PEP8.
    -    В `get_webelement_by_locator` в блоке `if timeout == 0` использовать `await asyncio.to_thread` при вызове `driver.find_elements`.
    - В `get_webelement_by_locator` добавить обработку `raise ValueError`.
    - В `get_attribute_by_locator` использовать `await asyncio.to_thread` для  `web_element.get_attribute`.
    
**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
.. module:: src.webdriver
    :platform: Windows, Unix
    :synopsis: The purpose of the `executor` module is to perform actions on web elements based on provided configurations,
known as "locators." These configurations (or "locators") are dictionaries containing information on how to locate and interact with elements on a web page. The module provides the following functionalities:

1. **Parsing and Handling Locators**: Converts dictionaries with configurations into `SimpleNamespace` objects,
allowing for flexible manipulation of locator data.

2. **Interacting with Web Elements**: Depending on the provided data, the module can perform various actions such as clicks,
sending messages, executing events, and retrieving attributes from web elements.

3. **Error Handling**: The module supports continuing execution in case of an error, allowing for the processing of web pages
that might have unstable elements or require a special approach.

4. **Support for Multiple Locator Types**: Handles both single and multiple locators, enabling the identification and interaction
with one or several web elements simultaneously.

This module provides flexibility and versatility in working with web elements, enabling the automation of complex web interaction scenarios.


"""
import asyncio
import re
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import BinaryIO, ByteString, Dict, List, Optional, Union

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    JavascriptException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import header
from src import gs
from src.logger.logger import logger  # Используем logger из src.logger
from src.logger.exceptions import (
    DefaultSettingsException,
    ExecuteLocatorException,
    WebDriverException,
)

from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint
from src.utils.image import save_image


@dataclass
class ExecuteLocator:
    """Locator handler for web elements using Selenium."""
    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        'XPATH': By.XPATH,
        'ID': By.ID,
        'TAG_NAME': By.TAG_NAME,
        'CSS_SELECTOR': By.CSS_SELECTOR,
        'NAME': By.NAME,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'CLASS_NAME': By.CLASS_NAME,
    })
    mode: str = 'debug'

    def __post_init__(self):
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: Optional[float] = 0,
        continue_on_error: Optional[bool] = True,
    ) -> str | list | dict | WebElement | bool:
        """Executes actions on a web element based on the provided locator.

        Args:
            locator (dict | SimpleNamespace): Locator data.
            timeout (float, optional): Timeout for locating the element.
            timeout_for_event (str, optional): The wait condition ('presence_of_element_located', 'element_to_be_clickable').
            message (str, optional): Optional message to send.
            typing_speed (float, optional): Typing speed for send_keys events.
            continue_on_error (bool, optional): Whether to continue on error.

        Returns:
            str | list | dict | WebElement | bool: Outcome based on locator instructions.

        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B --> C{Is locator SimpleNamespace?}
            C -->|Yes| D[Use locator as is]
            C -->|No| E[Convert dict to SimpleNamespace]
            E --> D
            D --> F[Define async function _parse_locator]
            F --> G[Check if locator has event, attribute, or mandatory]
            G -->|No| H[Return None]
            G -->|Yes| I[Try to map by and evaluate attribute]
            I --> J[Catch exceptions and log if needed]
            J --> K{Does locator have event?}
            K -->|Yes| L[Execute event]
            K -->|No| M{Does locator have attribute?}
            M -->|Yes| N[Get attribute by locator]
            M -->|No| O[Get web element by locator]
            L --> P[Return result of event]
            N --> P[Return attribute result]
            O --> P[Return web element result]
            P --> Q[Return final result of _parse_locator]
            Q --> R[Return result of execute_locator]
            R --> S[End]

        ```
        """
        # проверяем тип локатора и преобразуем его в SimpleNamespace если это необходимо
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        # если нет атрибутов или селектора - возвращаем None
        if not locator or (not locator.attribute and not locator.selector):
            return None  # <- локатор - заглушка

        async def _parse_locator(
            locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """Parses and executes locator instructions.

            Args:
                locator (Union[dict, SimpleNamespace]): Locator data.
                message (str, optional): Message to send, if applicable.

            Returns:
                str | list | dict | WebElement | bool: Result of the execution.
            """
            #  преобразуем локатор в SimpleNamespace
            locator = (
                locator if isinstance(locator, SimpleNamespace)
                else SimpleNamespace(**locator)
            )
            # проверяем наличие event, attribute или mandatory
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return
            try:
                #  получаем тип локатора
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    # вычисляем значение атрибута
                    locator.attribute = await self.evaluate_locator(locator.attribute)
                    # проверяем если тип локатора VALUE
                    if locator.by == 'VALUE':
                        return locator.attribute
            except Exception as ex:
                logger.debug(f"Locator Error: {locator=}", ex)
                return
            # исполняем событие если есть
            if locator.event:
                return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)
            # получаем атрибут
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            # получаем вебэлемент
            return await self.get_webelement_by_locator(locator, timeout, timeout_for_event)

        return await _parse_locator(locator, message)

    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """Evaluates and processes locator attributes.

        Args:
            attribute (str | List[str] | dict): Attributes to evaluate.

        Returns:
            str | List[str] | dict: Evaluated attributes.
        
        ```mermaid
                graph TD
            A[Start] --> B[Check if attribute is list]
            B -->|Yes| C[Iterate over each attribute in list]
            C --> D[Call _evaluate for each attribute]
            D --> E[Return gathered results from asyncio.gather]
            B -->|No| F[Call _evaluate for single attribute]
            F --> G[Return result of _evaluate]
            G --> H[End]
            E --> H
        ```
        """
        async def _evaluate(attr: str) -> Optional[str]:
            # ищем соответствие в Keys, если находим - возвращаем значение
            match = re.findall(r"%(\\w+)%", attr)
            if match:
                return getattr(Keys, match[0], None)
            return attr

        # если атрибут - список, проходим по нему
        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))

    async def get_attribute_by_locator(
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) ->  WebElement | list[WebElement] | None:
        """Retrieves attributes from an element or list of elements found by the given locator.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.

        Returns:
            str | list | dict | WebElement | list[WebElement] | None: The attribute value(s) or dictionary with attributes.

        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B -->|Yes| C[Convert locator to SimpleNamespace if needed]
            C --> D[Call get_webelement_by_locator]
            D --> E[Check if web_element is found]
            E -->|No| F[Log debug message and return]
            E -->|Yes| G[Check if locator.attribute is a dictionary-like string]
            G -->|Yes| H[Parse locator.attribute string to dict]
            H --> I[Check if web_element is a list]
            I -->|Yes| J[Retrieve attributes for each element in list]
            J --> K[Return list of attributes]
            I -->|No| L[Retrieve attributes for a single web_element]
            L --> K
            G -->|No| M[Check if web_element is a list]
            M -->|Yes| N[Retrieve attributes for each element in list]
            N --> O[Return list of attributes or single attribute]
            M -->|No| P[Retrieve attribute for a single web_element]
            P --> O
            O --> Q[End]
            F --> Q
        ```
        """
        # проверяем тип локатора и преобразуем его в SimpleNamespace если это необходимо
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )
        # получаем вебэлемент
        web_element: WebElement | list[WebElement] | None = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        # если элемент не найден - логируем ошибку и возвращаем None
        if not web_element:
            logger.debug(f"Не нашелся : {locator=}", None, False)
            return

        def _parse_dict_string(attr_string: str) -> dict | None:
            """Parses a string like '{attr1:attr2}' into a locator.

            Args:
                attr_string (str): String representing a dictionary-like structure.

            Returns:
                dict: Parsed dictionary or None if parsing fails.
            """
            try:
                #  парсим строку в словарь
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))
                }
            except ValueError as ex:
                logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}", ex, False)
                return

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """Retrieves attribute values for each key in a given dictionary.

            Args:
                element (WebElement): The web element to retrieve attributes from.
                attr_dict (dict): A dictionary where keys/values represent attribute names.

            Returns:
                dict: Dictionary with attributes and their corresponding values.
            """
            result = {}
            # проходим по всем атрибутам в словаре
            for key, value in attr_dict.items():
                try:
                    # получаем значения атрибутов
                    attr_key = await asyncio.to_thread(web_element.get_attribute, key)
                    attr_value = await asyncio.to_thread(web_element.get_attribute, value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    logger.debug(f"Error retrieving attributes '{key}' or '{value}' from element.", ex, False)
                    return
            return result
        
        # если вебэлемент найден - продолжаем
        if web_element:
            # проверяем если атрибут - строка и начинается с {
            if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
                # парсим строку в словарь
                attr_dict = _parse_dict_string(locator.attribute)
                # если вебэлемент - список, проходим по нему
                if isinstance(web_element, list):
                    return [_get_attributes_from_dict(el, attr_dict) for el in web_element]
                return _get_attributes_from_dict(web_element, attr_dict)
            # если вебэлемент - список, проходим по нему
            if isinstance(web_element, list):
                ret: list = []
                try:
                    for e in web_element:
                        # получаем значение атрибута для каждого элемента
                        ret.append(await asyncio.to_thread(e.get_attribute, locator.attribute))
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    logger.debug(f"Error in get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}", ex, False)
                    return
            # если вебэлемент не список
            return await asyncio.to_thread(web_element.get_attribute, locator.attribute)
        return

    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located'
    ) -> WebElement | List[WebElement] | None:
        """
        Функция извлекает веб-элемент или список элементов по указанному локатору.
        .. :todo:
            Продумать как передать `timeout_for_event`
        """
        #  устанавливаем timeout
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрация веб-элементов по правилу, указанному в `locator.if_list`.
            """
            # если вебэлемент не список - возвращаем его
            if not isinstance(web_elements, list):
                return web_elements

            if_list = locator.if_list
            # фильтруем список по правилу
            match if_list:
                case 'all':
                    return web_elements
                case 'first':
                    return web_elements[0]
                case 'last':
                    return web_elements[-1]
                case 'even':
                    return [web_elements[i] for i in range(0, len(web_elements), 2)]
                case 'odd':
                    return [web_elements[i] for i in range(1, len(web_elements), 2)]
                case list():
                    return [web_elements[i] for i in if_list]
                case int():
                    return web_elements[if_list - 1]
            return web_elements

        driver = self.driver
        # преобразуем локатор в SimpleNamespace
        locator = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )
        # если локатор некорректный, выбрасываем исключение
        if not locator:
            raise ValueError('Некорректный локатор.')
        
        web_elements = None
        try:
            # Если timeout = 0, сразу попытаться найти элемент без ожидания
            if timeout == 0:
                web_elements = await asyncio.to_thread(
                     driver.find_elements, locator.by, locator.selector
                )
            else:
                #  выбираем условие ожидания
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located
                )
                # ожидание элементов
                web_elements = await asyncio.to_thread(
                    WebDriverWait(driver, timeout).until,
                    condition((locator.by, locator.selector))
                )
            # фильтруем список элементов
            return await _parse_elements_list(web_elements, locator)
        except TimeoutException as ex:
            logger.error(f'Таймаут для локатора: {locator}', ex, False)
            return None
        except Exception as ex:
            logger.error(f'Ошибка локатора: {locator}', ex, False)
            return None


    async def get_webelement_as_screenshot(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
        webelement: Optional[WebElement] = None
    ) -> BinaryIO | None:
        """Takes a screenshot of the located web element.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.
            message (str, optional): Message to send to the element. Defaults to None.
            typing_speed (float, optional): Speed of typing for send message events. Defaults to 0.
            continue_on_error (bool, optional): Whether to continue in case of an error. Defaults to True.
            webelement (WebElement, optional): Pre-fetched web element. Defaults to None.

        Returns:
            BinaryIO | None: Binary stream of the screenshot or None if failed.
        """
         # проверяем тип локатора и преобразуем его в SimpleNamespace если это необходимо
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )
        # если вебэлемент не передан - получаем его
        if not webelement:
            webelement = await self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)
        # если вебэлемент не найден
        if not webelement:
            return
        try:
            # делаем скриншот
            screenshot_stream = await asyncio.to_thread(webelement.screenshot_as_png)
            return screenshot_stream
        except Exception as ex:
            logger.error(f"Не удалось захватить скриншот", ex)
            return


    async def execute_event(self,
                             locator: SimpleNamespace | dict,
                             timeout: float = 5,
                             timeout_for_event: str = 'presence_of_element_located',
                             message: str = None,
                             typing_speed: float = 0,
                             continue_on_error: bool = True,
    ) -> str | list[str] | bytes | list[bytes] | bool:
        """
        Execute the events associated with a locator.

        Args:
            locator (SimpleNamespace | dict): Locator specifying the element and event to execute.
            timeout (float): Timeout for locating the element.
            timeout_for_event (str): Timeout for waiting for the event.
            message (str, optional): Message to send with the event, if applicable. Defaults to None.
            typing_speed (float, optional): Speed of typing for send_keys events. Defaults to 0.

        Returns:
            str | list[str] | bytes | list[bytes] | bool: Returns result if event execution was successful, False otherwise.
        """
         # проверяем тип локатора и преобразуем его в SimpleNamespace если это необходимо
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )
        # получаем список событий
        events = str(locator.event).split(";")
        result: list = []
        # получаем вебэлемент
        web_element = await self.get_webelement_by_locator(
            locator,
            timeout,
            timeout_for_event
        )
        # если вебэлемент не найден, возвращаем False
        if not web_element:
            return False
        # если вебэлемент список, берем первый элемент
        web_element = web_element[0] if isinstance(web_element, list) else web_element
        
        async def _execute_single_event(event:str, element: WebElement) ->  bool | str | list[str] | bytes | list[bytes] | None:
            """ Executes single event on web element
            """
            match event:
                case "click()":
                    try:
                        await asyncio.to_thread(element.click)
                        return True
                    except ElementClickInterceptedException as ex:
                         logger.error(f"Element click intercepted:  {locator=}", ex, False)
                         return False
                    except Exception as ex:
                        logger.error(f"Element click error: {locator=}", ex, False)
                        return False
                case str() if event.startswith("pause("):
                    match = re.match(r"pause\\((\\d+)\\)", event)
                    if match:
                        pause_duration = int(match.group(1))
                        await asyncio.sleep(pause_duration)
                        return True
                    logger.debug(f"Должна быть пауза, но что-то не срослось: {locator=}")
                    return False
                case "upload_media()":
                    if not message:
                        logger.debug(f"Message is required for upload_media event. Message: {pprint(message, text_color='WHITE',bg_color='RED')}", None, False)
                        return False
                    try:
                        await asyncio.to_thread(element.send_keys, message)
                        return True
                    except Exception as ex:
                        logger.debug(f"Error uploading media: {message=}", ex, False)
                        return False
                case "screenshot()":
                    try:
                        return await self.get_webelement_as_screenshot(locator, webelement=element)
                    except Exception as ex:
                        logger.error(f"Error taking screenshot: {locator=}", ex, False)
                        return False
                case "clear()":
                    try:
                        await asyncio.to_thread(element.clear)
                        return True
                    except Exception as ex:
                        logger.error(f"Error clearing element: {locator=}", ex, False)
                        return False
                case str() if event.startswith("send_keys("):
                    keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                    try:
                        actions = ActionChains(self.driver)
                        for key in keys_to_send:
                            key = key.strip().strip("\'")
                            if hasattr(Keys, key):
                                key_to_send = getattr(Keys, key)
                                actions.send_keys(key_to_send)
                        await asyncio.to_thread(actions.perform)
                        return True
                    except Exception as ex:
                        logger.error(f"Error sending keys: {locator=}", ex, False)
                        return False
                case str() if event.startswith("type("):
                    message = event.replace("type(", "").replace(")", "")
                    if typing_speed:
                        for character in message:
                            await asyncio.to_thread(element.send_keys, character)
                            await asyncio.sleep(typing_speed)
                    else:
                        await asyncio.to_thread(element.send_keys, message)
                    return True
            return None

        for event in events:
            event_result = await _execute_single_event(event, web_element)
            if event_result is False:
                return False
            if event_result is not True and event_result is not None:
                result.append(event_result)
                
        return result if result else True

    async def send_message(self,
                        locator: SimpleNamespace | dict,
                        timeout: float = 5,
                        timeout_for_event: str = 'presence_of_element_located',
                        message: str = None,
                        typing_speed: float = 0,
                        continue_on_error: bool = True,
    ) -> bool:
        """Sends a message to a web element.

        Args:
            locator (dict | SimpleNamespace): Information about the element's location on the page.
                                              It can be a dictionary or a SimpleNamespace object.
            message (str, optional): The message to be sent to the web element. Defaults to `None`.
            typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

        Returns:
            bool: Returns `True` if the message was sent successfully, `False` otherwise.

        Example:
            >>> driver = Driver()
            >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
            True
        """
        #  преобразуем локатор в SimpleNamespace
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )
        
        async def type_message(
            el: WebElement,
            message: str,
            replace_dict: dict = {";": "SHIFT+ENTER"},
            typing_speed: float = typing_speed,
        ) -> bool:
            """Types a message into a web element with a specified typing speed.

            Args:
                el (WebElement): The web element to type the message into.
                message (str): The message to type.
                replace_dict (dict, optional): Dictionary for character replacements in the message. Defaults to {";": "SHIFT+ENTER"}.
                typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

            Returns:
                bool: Returns `True` if the message was typed successfully, `False` otherwise.

            Example:
                >>> element = driver.get_element_by_id("messageBox")
                >>> driver.type_message(el=element, message="Hello World", typing_speed=0.1)
                True
            """
            # разбиваем сообщение на слова
            message = message.split(" ")
            # проходим по всем словам
            for word in message:
                word += " "
                try:
                    # проходим по всем буквам в слове
                    for letter in word:
                        # если есть совпадение в словаре замен - выполняем замену
                        if letter in replace_dict:
                            keys_to_send = replace_dict[letter].split('+')
                            actions = ActionChains(self.driver)
                            for key in keys_to_send:
                                key_to_send = getattr(Keys, key)
                                actions.key_down(key_to_send)
                            actions.send_keys(Keys.ENTER)
                            for key in reversed(keys_to_send):
                                key_to_send = getattr(Keys, key)
                                actions.key_up(key_to_send)
                            await asyncio.to_thread(actions.perform)
                        # если нет - отправляем букву
                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            await asyncio.to_thread(self.actions.perform)
                except Exception as ex:
                    logger.error(f"Error typing message\n{message=}\n{word=}\n{letter=}", ex)
                    continue  # если была ошибка в передаче буквы - пока игнорую ёё
            return True

        # получаем вебэлемент
        webelement:WebElement = await self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        # если вебэлемент не найден, возвращаем False
        if not webelement or (isinstance(webelement, list) and len(webelement) == 0):
            return False
        # если вебэлемент - список, берем первый элемент
        webelement = webelement[0] if isinstance(webe