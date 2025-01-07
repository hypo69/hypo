## \file /src/webdriver/executor.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

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
    StaleElementReferenceException,  # Этот импорт был добавлен
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
from src.logger.logger import logger
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
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "CLASS_NAME": By.CLASS_NAME,
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
            locator: Locator data (dict, SimpleNamespace, or Locator).
            timeout: Timeout for locating the element.
            timeout_for_event: The wait condition ('presence_of_element_located', 'element_to_be_clickable').
            message: Optional message to send.
            typing_speed: Typing speed for send_keys events.
            continue_on_error: Whether to continue on error.

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
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not locator.attribute and not locator.selector:
            return None # <- локатор - заглушка

        async def _parse_locator(
            locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """ Parses and executes locator instructions.

            Args:
                loc (Union[dict, SimpleNamespace]): Locator data.
                message (Optional[str]): Message to send, if applicable.

            Returns:
                Union[str, list, dict, WebElement, bool]: Result of the execution.
            """
            locator = (
                locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return 

            try:
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(locator.attribute)
                    """Я могу установить константное или формульное значение в аттрибут локатора и забирать его при условии {'by':'VALUE'}"""
                    if locator.by == 'VALUE':
                        return locator.attribute

            except Exception as ex:
                logger.debug(f"Locator Error: {locator=}")
                ...
                return

            if locator.event:
                return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(locator, timeout, timeout_for_event)

        return await _parse_locator(locator, message)

    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """Evaluates and processes locator attributes.

        Args:
            attribute (Union[str, List[str], dict]): Attributes to evaluate.

        Returns:
            Union[str, List[str], dict]: Evaluated attributes.

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
            return getattr(Keys, re.findall(r"%(\w+)%", attr)[0], None) if re.match(r"^%\w+%", attr) else attr

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
        """ Retrieves attributes from an element or list of elements found by the given locator.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.

        Returns:
            Union[str, list, dict, WebElement | list[WebElement] | None]: The attribute value(s) or dictionary with attributes.

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
    
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        web_element: WebElement = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            logger.debug(f"Не нашелся : {locator=}\n", None, False)
            ...
            return

        def _parse_dict_string(attr_string: str) -> dict | None:
            """ Parses a string like '{attr1:attr2}' into a locator.

            Args:
                attr_string (str): String representing a dictionary-like structure.

            Returns:
                dict: Parsed dictionary or None if parsing fails.
            """
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))
                }
            except ValueError as ex:
                logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\n", ex, False)
                ...
                return
                logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\n", ex, False)
                ...
                return

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """ Retrieves attribute values for each key in a given dictionary.

            Args:
                element (WebElement): The web element to retrieve attributes from.
                attr_dict (dict): A dictionary where keys/values represent attribute names.

            Returns:
                dict: Dictionary with attributes and their corresponding values.
            """
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    logger.debug(f"Error retrieving attributes '{key}' or '{value}' from element.", ex, False)
                    ...
                    return
            return result

        if web_element:
            # Check if the attribute is a dictionary-like string
            if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
                attr_dict = _parse_dict_string(locator.attribute)

                if isinstance(web_element, list):
                    return [_get_attributes_from_dict(el, attr_dict) for el in web_element]
                return _get_attributes_from_dict(web_element, attr_dict)

            if isinstance(web_element, list):
                ret: list = []
                try:
                    for e in web_element:
                        ret.append(f'{e.get_attribute(locator.attribute)}')
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    logger.debug(f"Error in get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}\n", ex, False)
                    ...
                    return
            
            return web_element.get_attribute(locator.attribute)
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
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрация веб-элементов по правилу, указанному в `locator.if_list`.
            """
            if not isinstance(web_elements, list):
                return web_elements

            if_list = locator.if_list

            if if_list == 'all':
                return web_elements
            elif if_list == 'first':
                return web_elements[0]
            elif if_list == 'last':
                return web_elements[-1]
            elif if_list == 'even':
                return [web_elements[i] for i in range(0, len(web_elements), 2)]
            elif if_list == 'odd':
                return [web_elements[i] for i in range(1, len(web_elements), 2)]
            elif isinstance(if_list, list):
                return [web_elements[i] for i in if_list]
            elif isinstance(if_list, int):
                return web_elements[if_list - 1]

            return web_elements

        driver = self.driver
        locator = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )

        if not locator:
            raise ValueError('Некорректный локатор.')
            ...


        web_elements = None
        try:
            # Если timeout = 0, сразу попытаться найти элемент без ожидания
            if timeout == 0:
                        web_elements = await asyncio.to_thread(
                            driver.find_elements, locator.by, locator.selector
                        )
            else:
                # Выбор условия ожидания
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located
                )

                # Ожидание элементов через блокирующий вызов в асинхронном контексте
                web_elements = await asyncio.to_thread(
                    WebDriverWait(driver, timeout).until,
                    condition((locator.by, locator.selector))
                )


            return await _parse_elements_list(web_elements, locator)
        except TimeoutException as ex:
            logger.error(f'Таймаут для локатора: {locator}', ex, False)
            ...
            return None
        except Exception as ex:
            logger.error(f'Ошибка локатора: {locator}', ex, False)
            ...
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
        """ Takes a screenshot of the located web element.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.
            message (Optional[str], optional): Message to send to the element. Defaults to None.
            typing_speed (float, optional): Speed of typing for send message events. Defaults to 0.
            continue_on_error (bool, optional): Whether to continue in case of an error. Defaults to True.
            webelement (Optional[WebElement], optional): Pre-fetched web element. Defaults to None.

        Returns:
            BinaryIO | None: Binary stream of the screenshot or None if failed.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)

        if not webelement:
            return

        try:
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
            logger.error(f"Не удалось захватить скриншот\n", ex)
            ...
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
            timeout: Timeout for locating the element.
            timeout_for_event: Timeout for waiting for the event.
            message (Optional[str], optional): Message to send with the event, if applicable. Defaults to None.
            typing_speed (int, optional): Speed of typing for send_keys events. Defaults to 0.

        Returns:
            bool: Returns True if event execution was successful, False otherwise.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        # Retrieve the web element based on the locator
        webelement = await self.get_webelement_by_locator(                                     
            locator,
            timeout, 
            timeout_for_event
        )

        if not webelement:
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement

        for event in events:
            if event == "click()":
                try:
                    webelement.click()
                    # await asyncio.to_thread(webelement.click)
                    # result.append(True)
                    continue
                except ElementClickInterceptedException as ex:
                    logger.error(f"Element click intercepted:  {locator=}\n", ex, False)
                    ...
                    return 
                except Exception as ex:
                    logger.error(f"Element click intercepted: {locator=}\n", ex, False)
                    ...
                    return 

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                logger.debug(f"Должна быть пауза, но что-то не срослось: {locator=}\n")
                ...
                return False

            elif event == "upload_media()":
                if not message:
                    logger.debug(f"Message is required for upload_media event. Message: {pprint(message, text_color='WHITE',bg_color='RED')}", None, False)
                    ... 
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    logger.debug(f"Error uploading media: {message=}", ex, False)
                    ...
                    return False

            elif event == "screenshot()":
                try:
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                    logger.error(f"Error taking screenshot: {locator=}", ex, False)
                    ...
                    return False

            elif event == "clear()":
                try:
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    logger.error(f"Error clearing element: {locator=}", ex, False)
                    ...
                    return False

            elif event.startswith("send_keys("):
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip("'")
                        if hasattr(Keys, key):
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                    await asyncio.to_thread(actions.perform)
                except Exception as ex:
                    logger.error(f"Error sending keys: {locator=}", ex, False)
                    ...    
                    return False

            elif event.startswith("type("):
                message = event.replace("type(", "").replace(")", "")
                if typing_speed:
                    for character in message:
                        await asyncio.to_thread(webelement.send_keys, character)
                        await asyncio.sleep(typing_speed)
                else:
                    await asyncio.to_thread(webelement.send_keys, message)

        return result if result else True

    async def send_message(self,               
                        locator: SimpleNamespace | dict,
                        timeout:float = 5 , 
                        timeout_for_event: str = 'presence_of_element_located',
                        message: str = None,
                        typing_speed: float = 0,
                        continue_on_error: bool = True,

    ) -> bool:
        """Sends a message to a web element.

        Args:
            self (Driver): The instance of the Driver class.
            locator (dict | SimpleNamespace): Information about the element's location on the page.
                                              It can be a dictionary or a SimpleNamespace object.
            message (Optional[str], optional): The message to be sent to the web element. Defaults to `None`.
            replace_dict (dict, optional): A dictionary for replacing certain characters in the message. Defaults to {";": "SHIFT+ENTER"}.
            typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

        Returns:
            bool: Returns `True` if the message was sent successfully, `False` otherwise.

        Example:
            >>> driver = Driver()
            >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
            True
       

        """
        ...

        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )

        def type_message(
            el: WebElement,
            message: str,
            replace_dict: dict = {";":"SHIFT+ENTER"},
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

            message = message.split(" ")

            for word in message:
                word += " "
                try:
                    for letter in word:
                        if letter in replace_dict.keys():
                            self.actions.key_down(Keys.SHIFT).send_keys(
                                Keys.ENTER
                            ).key_up(Keys.SHIFT)
                            """ TODO:
                                делать проверку в словаре подмен """
                            # self.actions.perform()
                            # key = replace_dict[letter].split('+')
                            # self.actions.key_down(key[0])
                            # self.actions.send_keys(key[1])
                            # self.actions.key_up(key[0])
                            # self.actions.perform()
                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            self.actions.perform()
                except Exception as ex:
                    logger.error(f"Error typing message\n{message=}\n{word=}\n{letter=}\n", ex)
                    ...
                    continue  # <- если была ошибка в передаче буквы - пока игнорую ёё
                    """ TODO:
                        Установить обработчик ошибок """
            return True

        ...

        webelement = self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        if not webelement or (isinstance(webelement, list) and len(webelement) == 0):
            return 
        webelement = webelement[0] if isinstance(webelement, list) else webelement
        self.actions.move_to_element(webelement)
        type_message(
            el=webelement,
            message=message,
            replace_dict={";":"SHIFT+ENTER"},
            typing_speed=typing_speed,
        )
        return True
