## \file ../src/webdriver/executor.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
The purpose of the `executor` module is to perform actions on web elements based on provided configurations, 
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


import sys
import asyncio
import re
from types import SimpleNamespace
from typing import ByteString, BinaryIO, Optional
from pathlib import Path
import time
from typing import List, Union, Dict
from enum import Enum

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    JavascriptException,
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException
)

from src import gs
from src.utils import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.utils.string import StringFormatter
from src.logger import logger
from src.logger.exceptions import (
    DefaultSettingsException,
    WebDriverException,
    ExecuteLocatorException,
)


class ExecuteLocator:
    """ Locator handler"""

    driver = None
    actions: ActionChains = None
    by_mapping = {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "CLASS_NAME": By.CLASS_NAME,
    }
    mode = 'debug'
    def __init__(self, driver, *args, **kwargs):
        """ Locator handler
        @param driver: `src.webdriver.Driver`
        """
        self.driver = driver
        self.actions = ActionChains(driver)

    def execute_locator(
    self,
    locator: dict,
    timeout:float = 0, 
    timeout_for_event: str = 'presence_of_element_located',
    message: str = None,
    typing_speed: float = 0,
    continue_on_error: bool = True,
    ) -> str | list | dict | WebElement | bool:
        """
    Executes the logic specified in the locator dictionary to interact with web elements.

    Args:
        locator (dict): The locator dictionary containing information for locating and interacting with web elements.
        message (str, optional): Message to send when interacting with the web element. Defaults to `None`.
        typing_speed (float, optional): Speed of typing in seconds per character (if applicable). Defaults to `0`.
        continue_on_error (bool, optional): Whether to continue executing in case of an error. Defaults to `True`.

    Returns:
        str | list | dict | WebElement | bool: Various results based on the locator's configuration,
        which may include a string, list, dictionary, web element, or boolean.

    Example:
        >>> locator = {
        >>>     "by": "ID",
        >>>     "selector": "username",
        >>>     "event": "click",
        >>>     "attribute": "value"
        >>> }
        >>> result: str = self.execute_locator(locator)
        >>> print(result)
        'JohnDoe'

    """
        ...
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
        )

        def _parse_locator(
            locator: dict | SimpleNamespace, message: str
        ) -> str | list | dict | WebElement | bool:
            """
            Parses and executes the locator instructions to perform actions on web elements.

            Args:
                locator (dict | SimpleNamespace): Locator dictionary or SimpleNamespace with details for locating and interacting with web elements.
                message (str): Message to send when interacting with the web element.

            Returns:
                str | list | dict | WebElement | bool: Result of parsing and executing the locator's instructions.

            Example:
                >>> locator = SimpleNamespace(
                >>>     by="ID",
                >>>     selector="username",
                >>>     event="click",
                >>>     attribute="value"
                >>> )
                >>> result: str = self._parse_locator(locator, message="JohnDoe")
                >>> print(result)
                'JohnDoe'

            .. Flowchart::

            +--------------------------------------------+
            |           Start: Execute Locator           |
            +--------------------------------------------+
                                |
                                V
                      +-------------------------+
                      | Parse Locator Data Type |
                      +-------------------------+
                                |
                                V
                    +------------------------------+
                    | Initialize SimpleNamespace   |
                    +------------------------------+
                                |
                                V
             +---------------------------------------------------+
             | Check if Event, Attribute, and Mandatory are None |
             +---------------------------------------------------+
                                |
                                V
                    +------------------------------+
                    | Get 'by' and 'event' Values  |
                    +------------------------------+
                                |
                                V
              +-----------------------------------------+
              | Evaluate Attribute if Exists            |
              +-----------------------------------------+
                                |
                                V
             +-----------------------------------------------------+
             | Check Locator 'by' Value: 'VALUE', 'No Event', etc. |
             +-----------------------------------------------------+
                                |
                                V
             +--------------------------------------------+
             | Execute Event / Send message or Return     |
             | Attribute/Element                          |
             +--------------------------------------------+
                                |
                                V
                            End Flow
            """
            locator = (
                locator
                if isinstance(locator, SimpleNamespace)
                else SimpleNamespace(**locator)
            )

            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return None

            try:
                by = locator.by.upper()
                event = locator.event
                attribute = self.evaluate_locator(locator.attribute) if locator.attribute else None
                locator.by = self.by_mapping.get(by, by)
            except Exception as ex:
                if self.mode == 'debug': 
                    logger.debug(f"Ошибка в локарое: {pprint(locator, text_color='RED',bg_color='BLACK',font_style="BOLD")}\n", ex, True)
                    ...
                return

            # Общие аргументы для всех функций
            args = (locator, timeout, timeout_for_event, message, typing_speed)

            if by == "VALUE":
                # Return value through attribute, could be a computed function
                return locator.attribute

            if not event and not attribute:
                # Case where the entire element is needed
                return self.get_webelement_by_locator(*args)

            if event:
                # Event is provided, perform action
                return self.execute_event(*args)

            elif message:
                # Send message to element
                return self.send_message(*args)

            if attribute:
                # Return the attribute of the element
                return self.get_attribute_by_locator(locator)


        if isinstance(locator.by, list):
            locators = [
                SimpleNamespace(
                    **{
                        "attribute": locator.attribute[i],
                        "by": locator.by[i],
                        "selector": locator.selector[i],
                        "event": locator.event[i],
                        "if_list":"first","use_mouse": locator.use_mouse[i]
                        if "use_mouse" in locator and isinstance(locator.use_mouse, list)
                        else None,
                        "mandatory": locator.mandatory[i]
                        if "mandatory" in locator and isinstance(locator.mandatory, list)
                        else None,
                        "locator_description": locator.locator_description[i]
                        if "locator_description" in locator
                        and isinstance(locator.locator_description, list)
                        else None,
                    }
                )
                for i in range(len(locator.by))
            ]
            ret = [_parse_locator(loc, message) for loc in locators]
        else:
            result = _parse_locator(locator, message)

        return result

    def evaluate_locator(
        self, attribute: str | list[str] | dict
    ) -> str | list[str] | dict:
        r"""Evaluates the locator's attribute.

                          Args:
                              attribute (str | list[str] | dict): The locator attribute, which can be a single attribute as a string, a list of attributes, or a dictionary of attributes.

                          Returns:
                              str | list[str] | dict: The evaluated attribute value. If the input is a list or dictionary, the output will be the evaluated list or dictionary respectively.

                          Example:
                              >>> loc: str = "%ENTER%"
                              >>> evaluate_locator(loc)
                              'Keys.ENTER'

                              >>> locs: list[str] = ["%ENTER%", "%SHIFT%"]
                              >>> evaluate_locator(locs)
                              ['Keys.ENTER', 'Keys.SHIFT']

                              >>> loc_dict: dict = {"key1": "%ENTER%", "key2": "%SHIFT%"}
                              >>> evaluate_locator(loc_dict)
                              {'key1': 'Keys.ENTER', 'key2': 'Keys.SHIFT'}

                          Flowchart:

            +-------------------------------+
            | Start                         |
            +-------------------------------+
                        |
                        v
            +------------------------------------+
            | Call `evaluate_locator(attribute)` |
            +------------------------------------+
                        |
              +---------+---------+
              |                   |
              v                   v
        +----------------+     +-----------------------------+
        | Is attribute   |-N-->| Call `_evaluate(attribute)` |
        | a list?        |     +-----------------------------+
        |                |                |
        +--------+-------+                |
                 |                        |
                 v                        |
        +--------+---------+              |
        | For each item in |              |
        | the list, call   |              |
        | `_evaluate(attr)`|              |
        +------------------+              |
                 |                        |
                 v                        v
        +----------------+   +----------------------+
        | Call `_evaluate`|  | Does attribute match |
        | with a single   |->| pattern ^%\w+%?      |
        | attribute value |  +----------------------+
        +-----------------+          |
                                     |
                           +------Y--+--N---+
                           |                |
                           v                |
              +---------------------+       |
              | Extract key and use |       |
              | getattr(Keys, key,  |       |
              | None)               |       |
              +---------------------+       |
                        |                   |
                        v                   V
              +---------------------+  +-------------------------+
              | Return evaluated    |  |                         |
              | attribute           |  |  Return attribute as is |
              +---------------------+  +-------------------------+
                        |                   |
                        v                   v
               +-------------------------------------+
               | End                                 |
               +-------------------------------------+

        """
        ...

        def _evaluate(attribute: str) -> str | None:
            """Helper function to evaluate a single attribute value.

            Args:
                attribute (str): The attribute value to evaluate.

            Returns:
                str | None: The evaluated attribute value. If the attribute matches a pattern, returns the corresponding `Keys` value; otherwise, returns the original attribute.

            Example:
                >>> attr: str = "%ENTER%"
                >>> _evaluate(attr)
                'Keys.ENTER'

                >>> attr: str = "some_string"
                >>> _evaluate(attr)
                'some_string'
            """
            if attribute and re.match(r"^%\w+%", attribute):
                return getattr(Keys, re.findall(r"%(\w+)%", attribute)[0], None)
            return attribute

        ...

        if isinstance(attribute, list):
            return [_evaluate(attr) for attr in attribute]
        return _evaluate(attribute)
    
    def get_webelement_by_locator(self,
                                    locator: dict,
                                    timeout:float = 5 , 
                                    timeout_for_event: str = 'presence_of_element_located',
                                    message: str = None,
                                    typing_speed: float = 0,
                                    continue_on_error: bool = True,) -> WebElement | list[WebElement] | None:
        """
        Retrieves web elements on the page based on the provided locator, with options to wait for specific conditions.

        Args:
            locator (dict | SimpleNamespace): A dictionary or SimpleNamespace object containing the locator details, including 'by' and 'selector'.
            message (str, optional): An optional message to log in case of errors or additional context. Defaults to None.
            timeout (float, optional): The maximum time (in seconds) to wait for the web element. Defaults to 10 seconds.
            timeout_for_event (str, optional): The condition to wait for, either 'presence_of_element_located' or 'element_to_be_clickable'. Defaults to 'presence_of_element_located'.

        Returns:
            WebElement | list[WebElement] | None:
                - A single WebElement if exactly one matching element is found.
                - A list of WebElements if multiple matching elements are found.
                - None if no matching elements are found or an error occurs.

        Raises:
            ExecuteLocatorException: If the locator is marked as mandatory and no element can be located, the exception is raised.
        """
        d = self.driver
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
        )
        if timeout_for_event == 'presence_of_element_located':
            try:
                # Wait for the presence of the element
                WebDriverWait(d, timeout).until(
                    EC.presence_of_element_located((locator.by, locator.selector))
                )
            except (NoSuchElementException, TimeoutException) as ex:
                if self.mode == 'debug': 
                    logger.debug(f"Could not find element: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, True)
                    ...
                return
        if timeout_for_event == 'element_to_be_clickable':
            try:
                # Wait for the element to be clickable
                WebDriverWait(d, timeout).until(
                    EC.element_to_be_clickable((locator.by, locator.selector))
                )
            except (NoSuchElementException, TimeoutException) as ex:
                if self.mode == 'debug': 
                    logger.debug(f"Element not clickable: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, False)
                    ...
                return
                ...

        try:
            # Find all elements matching the locator
            elements = d.find_elements(locator.by, locator.selector)
        except Exception as ex:
            if self.mode == 'debug': 
                logger.debug(f"Could not find elements: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, False)
                ...
            return

        if not hasattr(locator, 'if_list'):
            return elements

        if  locator.if_list == 'first':
            return elements[0] if isinstance(elements, list) else elements

        elif locator.if_list == 'last':
            return elements[len(elements) - 1] if isinstance(elements, list) else elements

        else:
            return elements

    def get_attribute_by_locator(self,                                     
                                    locator: SimpleNamespace | dict,
                                    timeout:float = 5 , 
                                    timeout_for_event: str = 'presence_of_element_located',
                                    message: str = None,
                                    typing_speed: float = 0,
                                    continue_on_error: bool = True,) -> str | list | dict | WebElement | list[WebElement] | None:
        """! Retrieves attributes from an element or list of elements found by the given locator.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 10 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.

        Returns:
            str | list | dict | bool: The attribute value(s) or dictionary with attributes if parsed from a string.
                - If the element is a list, returns a list of dictionaries or attributes.
                - If the element is a single element, returns the attribute or dictionary.
                - If the element is not found, returns `None`.
        """
        
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
        )

        element:WebElement = self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not element:
            if self.mode == 'debug': 
                logger.debug(f"Element not clickable: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", None, False)
            return
       
        def _parse_dict_string(attr_string: str) -> dict | None:
            """! Parses a string like '{attr1:attr2}' into a dictionary.

            Args:
                attr_string (str): String representing a dictionary-like structure.

            Returns:
                dict: Parsed dictionary.
            """
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))
                }
            except ValueError as ex:
                if self.mode == 'debug': 
                    logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE',bg_color='RED')}\n", ex, False)
                ...
                return
            except Exception as ex:
                if self.mode == 'debug': 
                    logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE',bg_color='RED')}\n", ex, False)
                ...
                return

        def _get_attributes_from_dict(element: WebElement, attr_dict: dict) -> dict:
            """! Retrieves attribute values for each key in a given dictionary.

            Args:
                element (WebElement): The web element to retrieve attributes from.
                attr_dict (dict): A dictionary where keys/values represent attribute names.

            Returns:
                dict: Dictionary with attributes and their corresponding values.
            """
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = element.get_attribute(key)
                    attr_value = element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.debug(
                            f"Error retrieving attributes '{pprint(key, text_color='WHITE',bg_color='RED')}' or '{pprint(value, text_color='WHITE',bg_color='RED')}' from element.", ex, False)
                    ...
                    return
            return result

        if element:

            # Определяем, является ли атрибут строкой словаря
            if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
                attr_dict = _parse_dict_string(locator.attribute)

                if isinstance(element, list):
                    return [_get_attributes_from_dict(el, attr_dict) for el in element]
                return _get_attributes_from_dict(element, attr_dict)

            
            if isinstance(element, list):
                ret:list = []
                try:
                    for e in element:
                        ret.append(f'{e.get_attribute(locator.attribute)}')
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.debug(f"Error in get_attribute(): {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, False)
                    ...
                    return
            return element.get_attribute(locator.attribute)
        return 

    def get_webelement_as_screenshot(self,                                     
                                    locator: SimpleNamespace | dict,
                                    timeout:float = 5 , 
                                    timeout_for_event: str = 'presence_of_element_located',
                                    message: str = None,
                                    typing_speed: float = 0,
                                    continue_on_error: bool = True,
                                    webelement: Optional[WebElement] = None) -> BinaryIO | None:
        """  Беру скиншот элемента в формате `.png`.
        @todo добавить возможность делать скриншот всего экрана, его части, всплывающих окон
        Takes a screenshot of a given WebElement object and returns it as a PNG image.

        @param webelement: вебэлемент.
        locator_description Вначале по локатору достается вебэлемент, а потом прогоняю его через функцию
        и получаю массив байтов, по сути, картинку

        @returns Бинарный код изображения
            A binary PNG image if succesStringFormatterul, False if the element is no longer attached to the DOM or an error occurs.
        """
        if not webelement:
            webelement = self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)
        
        if not webelement:
            return 

        webelement = webelement[0] if isinstance(webelement, list) else webelement
        ...
        return webelement.screenshot_as_png


    def execute_event(self,              
                    locator: SimpleNamespace | dict,
                    timeout:float = 5 , 
                    timeout_for_event: str = 'presence_of_element_located',
                    message: str = None,
                    typing_speed: float = 0,
                    continue_on_error: bool = True,
    ) -> bool | bytes | list[bytes]:
        """
        Execute the events associated with a locator.

        Args:
            locator (SimpleNamespace | dict): Locator specifying the element and event to execute.
            timeout: Timeout for locating the element.
            timeout_for_event: Timeout for waiting for the event.
            message (Optional[str], optional): Message to send with the event, if applicable. Defaults to None.
            typing_speed (int, optional): Speed of typing for send_keys events. Defaults to 0.
            max_attempts (int, optional): Number of attempts to handle element click if intercepted. Defaults to 20.

        Returns:
            bool: Returns True if event execution was successful, False otherwise.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
        )
        events = str(locator.event).split(";")
        result: list = []
        # Retrieve the web element based on the locator
        webelement = self.get_webelement_by_locator(                                     
                                    locator,
                                    timeout, 
                                    timeout_for_event,
                                    message,
                                    typing_speed,
                                    continue_on_error,)
        ...

        if not webelement:
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement

        for event in events:
            if event == "click()":
                try:
                    webelement.click()
                    result.append(True)
                    continue
                except ElementClickInterceptedException as ex:
                    if self.mode == 'debug': 
                        logger.debug(f"Element click intercepted: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, False)
                    ...
                    return False
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.debug(f"Element click intercepted: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n", ex, False)
                    ...
                    return False

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    time.sleep(pause_duration)
                    result.append(True)
                    continue
                if self.mode == 'debug': 
                    logger.debug(f"Invalid pause duration: {pprint(event, text_color='WHITE',bg_color='RED')}\n")
                    ...
                return False

            elif event == "upload_media()":
                if not message:
                    if self.mode == 'debug': 
                        logger.debug(f"Message is required for upload_media event. Message: {pprint(message, text_color='WHITE',bg_color='RED')}", None, False)
                    ...
                    return False
                try:
                    webelement.send_keys(message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.debug(f"Error uploading media: {pprint(message, text_color='WHITE',bg_color='RED')}", ex, False)
                        ...
                    return False

            elif event == "screenshot()":
                try:
                    result.append(self.get_webelement_as_screenshot(locator, webelement = webelement))
                    ...
                except Exception as ex:
                    if self.mode == 'debug':
                        logger.error(f"Error taking screenshot: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}", ex, False)
                    ...
                    return False

            elif event == "clear()":
                try:
                    webelement.clear()
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.error(f"Error clearing element: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}", ex, False)
                    ...
                    return False

            elif event.startswith("send_keys("):
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip("'")
                        if hasattr(Keys, key):
                            # Get the actual key from the Keys object
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                        else:
                            actions.send_keys(key)
                    actions.perform()
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.error(f"Error clearing element: {pprint(locator, text_color='YELLOW',bg_color='BLACK')}\n{pprint(keys_to_send, text_color='WHITE',bg_color='RED')}", ex, False)
                    ...
                    return False

            # Handling backspace(n)
            elif event.startswith("backspace("):
                webelement.send_keys(Keys.END)
                field_value = webelement.get_attribute('value')
                for _ in range(len(field_value)):
                    webelement.send_keys(Keys.BACKSPACE)

            elif event == "%EXTERNAL_MESSAGE%":
                if not message:
                    logger.error("External message is required but not provided.")
                    return False
                try:
                    self.send_message(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event, message = message, typing_speed=typing_speed)
                    result.append(True)
                except Exception as ex:
                    if self.mode == 'debug': 
                        logger.error(f"Error sending external message:{pprint(message, text_color='WHITE',bg_color='RED')} {pprint(locator, text_color='YELLOW',bg_color='BLACK')}", ex, False)
                    ...
                    return False

            else:
                ... # <- implementation of other events 
        ...
        return result[0] if len(result) == 1 else result if len(result) > 1 else False 

    def send_message(self,               
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
        Flowchart:
                    +-------------------------+
                    |        Start            |
                    +-------------------------+
                                |
                                V
                    +-------------------------+
                    | Convert Locator         |
                    | - If dict, convert to   |
                    |   SimpleNamespace       |
                    | - If SimpleNamespace,   |
                    |   use directly          |
                    +-------------------------+
                                |
                                V
                    +-------------------------+
                    | Retrieve Web Element    |
                    | - Call get_webelement_by|
                    |   _locator(locator)     |
                    +-------------------------+
                                |
                                V
                    +-------------------------+
                    | Is Web Element Valid?   |
                    | - If None or empty list |
                    |   return False          |
                    +-------------------------+
                            /       \
                           /         \
                          No          Yes
                          |            |
                          V            |
        +-------------------------+    |
        | Return False            |    |
        | - Indicate failure      |    |
        +-------------------------+    |
                                       |
                                       V
                    +---------------------------+
                    | Select Single Web Element |           
                    | - If list, choose first   |
                    +---------------------------+
                                        |
                                        V
                    +-------------------------+
                    | Move to Web Element     |
                    | - Call actions.move_to_ |
                    |   element(webelement)   |
                    +-------------------------+
                                        |
                                        V
                    +-------------------------+
                    | Type Message            |
                    | - Call type_message     |
                    |   with parameters       |
                    +-------------------------+
                                        |
                                        V
                    +-------------------------+
                    | Return True             |
                    | - Indicate success      |
                    +-------------------------+
                                        |
                                        V
                    +-------------------------+
                    |          End            |
                    +-------------------------+

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
                    if self.mode == 'debug': 
                        logger.error(f"Error typing message\n{letter=}\n{word=}\n{pprint(locator, text_color='YELLOW',bg_color='BLACK')}", ex)
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
