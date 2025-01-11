# /src/webdriver/playwright/executor.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

import asyncio
from typing import Optional, List, Dict, Any
from pathlib import Path
from playwright.async_api import async_playwright, Page, Locator
from types import SimpleNamespace

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns
from src.logger.exceptions import WebDriverException
import re


class PlaywrightExecutor:
    """
    Executes commands based on executor-style locator commands using Playwright.
    """
    def __init__(self, browser_type: str = 'chromium', **kwargs):
        """
        Initializes the Playwright executor.

        :param browser_type: Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit').
        :type browser_type: str
        """
        self.driver = None
        self.browser_type = browser_type
        self.page: Optional[Page] = None
        self.config: SimpleNamespace = j_loads_ns(Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json'))

    async def start(self) -> None:
        """
        Initializes Playwright and launches a browser instance.
        """
        try:
            self.driver = await async_playwright().start()
            browser = await getattr(self.driver, self.browser_type).launch(headless=True, args = self.config.options)
            self.page = await browser.new_page()
        except Exception as ex:
            logger.critical('Playwright failed to start browser', ex)

    async def stop(self) -> None:
        """
        Closes Playwright browser and stops its instance.
        """
        try:
            if self.page:
                await self.page.close()
            if self.driver:
                await self.driver.stop()
                self.driver = None
            logger.info('Playwright stopped')
        except Exception as ex:
            logger.error(f'Playwright failed to close browser: {ex}')

    async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | dict | bytes | bool:
        """
        Executes actions based on locator and event.

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Optional message for events.
        :type message: Optional[str]
        :param typing_speed: Optional typing speed for events.
        :type typing_speed: float
        :returns: Result of operation
        :rtype: str | List[str] | dict | bytes | bool
         
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
            locator: dict | SimpleNamespace, message: Optional[str]
        ) -> str | List[str] | dict | bytes | bool:
            """Parses and executes locator instructions.

            :param locator: Locator data.
            :type locator: dict | SimpleNamespace
            :param message: Message to send, if applicable.
            :type message: Optional[str]
            :returns: Result of the execution.
            :rtype: str | List[str] | dict | bytes | bool
            """
            locator = (
                locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return 

            try:
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
                return await self.execute_event(locator, message, typing_speed)
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(locator)

        return await _parse_locator(locator, message)

    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """Evaluates and processes locator attributes.

        :param attribute: Attributes to evaluate.
        :type attribute: str | List[str] | dict
        :returns: Evaluated attributes.
        :rtype: Optional[str | List[str] | dict]
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
            return attr  #  Playwright не использует Key
           # return getattr(Keys, re.findall(r"%(\w+)%", attr)[0], None) if re.match(r"^%\w+%", attr) else attr

        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))

    async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
        """
        Gets the specified attribute from the web element.

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :returns: Attribute or None.
        :rtype: Optional[str | List[str] | dict]
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        element = await self.get_webelement_by_locator(locator)

        if not element:
            logger.debug(f"Element not found: {locator=}")
            return None

        def _parse_dict_string(attr_string: str) -> dict | None:
            """Parses a string like '{attr1:attr2}' into a dictionary.

            :param attr_string: String representing a dictionary-like structure.
            :type attr_string: str
            :returns: Parsed dictionary or None if parsing fails.
            :rtype: dict | None
            """
            try:
                return {k.strip(): v.strip() for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))}
            except ValueError as ex:
                logger.debug(f"Invalid attribute string format: {attr_string}\n{ex}")
                return None

        async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
            """Retrieves a single attribute from a Locator.

            :param el: The web element to retrieve attributes from.
            :type el: Locator
            :param attr: The name of attribute
            :type attr: str
            :returns: Attribute or None
            :rtype: Optional[str]
            """
            try:
                return await el.get_attribute(attr)
            except Exception as ex:
                logger.debug(f"Error getting attribute '{attr}' from element: {ex}")
                return None

        async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
            """Retrieves multiple attributes based on a dictionary.

            :param element: The web element to retrieve attributes from.
            :type element: Locator
            :param attr_dict: A dictionary where keys/values represent attribute names.
            :type attr_dict: dict
            :returns: Dictionary with attributes and their corresponding values.
            :rtype: dict
            """
            result = {}
            for key, value in attr_dict.items():
                result[key] = await _get_attribute(element, key)
                result[value] = await _get_attribute(element, value)

            return result

        if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
            attr_dict = _parse_dict_string(locator.attribute)
            if attr_dict:
                if isinstance(element, list):
                     return await asyncio.gather(*[_get_attributes_from_dict(el, attr_dict) for el in element])
                return await _get_attributes_from_dict(element, attr_dict)


        if isinstance(element, list):
            return await asyncio.gather(*[_get_attribute(el, locator.attribute) for el in element])

        return await _get_attribute(element, locator.attribute)

    async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
        """
        Gets a web element using the locator.

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :returns: Playwright Locator
        :rtype: Optional[Locator | List[Locator]]
        """
        locator = (
           SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )
        if not locator:
           raise ValueError('Некорректный локатор.')

        try:
            if locator.by.upper() == "XPATH":
                 elements = self.page.locator(f'xpath={locator.selector}')
            else:
                elements = self.page.locator(locator.selector)
            if locator.if_list == 'all':
                return await elements.all()
            elif locator.if_list == 'first':
                 return elements.first
            elif locator.if_list == 'last':
                return elements.last
            elif locator.if_list == 'even':
                list_elements = await elements.all()
                return [list_elements[i] for i in range(0, len(list_elements), 2)]
            elif locator.if_list == 'odd':
                list_elements = await elements.all()
                return [list_elements[i] for i in range(1, len(list_elements), 2)]
            elif isinstance(locator.if_list, list):
                 list_elements = await elements.all()
                 return [list_elements[i] for i in locator.if_list]
            elif isinstance(locator.if_list, int):
                 list_elements = await elements.all()
                 return list_elements[locator.if_list - 1]
            else:
                return elements
        except Exception as ex:
             logger.error(f'Ошибка поиска элемента: {locator=} \n {ex}', ex, False)
             return None

    async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
        """
        Takes a screenshot of the located web element.

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param webelement: The web element Locator.
        :type webelement: Optional[Locator]
        :returns: Screenshot in bytes or None.
        :rtype: Optional[bytes]
        """
        locator = (
           locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator)

        if not webelement:
            logger.debug(f"Не найден элемент для screenshot: {locator=}")
            return

        try:
            screenshot_bytes = await webelement.screenshot()
            return screenshot_bytes
        except Exception as ex:
            logger.error(f"Не удалось захватить скриншот\n", ex)
            return

    async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
        """
        Executes the event associated with the locator.

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Optional message for events.
        :type message: Optional[str]
        :param typing_speed: Optional typing speed for events.
        :type typing_speed: float
        :returns: Execution status.
        :rtype: str | List[str] | bytes | List[bytes] | bool
        """
        locator = (
             locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f"Element for event not found: {locator=}")
            return False

        element = element[0] if isinstance(element, list) else element
        
        for event in events:
            if event == "click()":
                try:
                    await element.click()
                    continue
                except Exception as ex:
                     logger.error(f'Ошибка при клике: {ex}\n {locator=}')
                     return False

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    continue
                logger.debug(f"Должна быть пауза, но что-то не срослось: {locator=}")
                return False

            elif event == "upload_media()":
                if not message:
                    logger.debug(f"Message is required for upload_media event. {message=}")
                    return False
                try:
                    await element.set_input_files(message) # работает в input type file
                    continue
                except Exception as ex:
                     logger.error(f'Ошибка загрузки файла: {ex}\n {locator=}')
                     return False

            elif event == "screenshot()":
                 try:
                     result.append(await self.get_webelement_as_screenshot(locator, webelement=element))
                 except Exception as ex:
                      logger.error(f'Ошибка при захвате скриншота: {ex}\n {locator=}')
                      return False

            elif event == "clear()":
                 try:
                    await element.clear()
                    continue
                 except Exception as ex:
                      logger.error(f'Ошибка при очистке поля: {ex}\n {locator=}')
                      return False

            elif event.startswith("send_keys("):
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                   for key in keys_to_send:
                        key = key.strip().strip("'")
                        if key:
                            await element.type(key)
                except Exception as ex:
                     logger.error(f'Ошибка при отправке клавиш: {ex}\n {locator=}')
                     return False

            elif event.startswith("type("):
                message = event.replace("type(", "").replace(")", "")
                if typing_speed:
                     for character in message:
                         await element.type(character)
                         await asyncio.sleep(typing_speed)
                else:
                    await element.type(message)
        return result if result else True

    async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
        """Sends a message to a web element.

        :param locator: Information about the element's location on the page.
        :type locator: dict | SimpleNamespace
        :param message: The message to be sent to the web element.
        :type message: Optional[str]
        :param typing_speed: Speed of typing the message in seconds.
        :type typing_speed: float
        :returns: Returns `True` if the message was sent successfully, `False` otherwise.
        :rtype: bool
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )
        element = await self.get_webelement_by_locator(locator)
        if not element or (isinstance(element, list) and len(element) == 0):
            return 
        element = element[0] if isinstance(element, list) else element

        if typing_speed:
            for character in message:
                await element.type(character)
                await asyncio.sleep(typing_speed)
        else:
            await element.type(message)

        return True

    async def goto(self, url: str) -> None:
        """
        Navigates to a specified URL.

        :param url: URL to navigate to.
        :type url: str
        """
        if self.page:
            try:
              await self.page.goto(url)
            except Exception as ex:
                  logger.error(f'Error navigation {url=}\n {ex}')