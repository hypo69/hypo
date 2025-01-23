## \file /src/webdriver/playwright/executor.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.webdriver.playwright.executor
    :platform: Windows, Unix
    :synopsis: This module provides functionalities to interact with web elements using Playwright based on provided locators.
               It handles parsing locators, interacting with elements, and error handling.
"""
import asyncio
import re
from typing import Optional, List, Union
from pathlib import Path
from playwright.async_api import async_playwright, Page, Locator
from types import SimpleNamespace

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class PlaywrightExecutor:
    """
    Executes commands based on executor-style locator commands using Playwright.
    """

    def __init__(self, browser_type: str = 'chromium', **kwargs):
        """
        Initializes the Playwright executor.

        Args:
            browser_type: Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit').
        """
        self.driver = None
        self.browser_type = browser_type
        self.page: Optional[Page] = None
        self.config: SimpleNamespace = j_loads_ns(
            Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        )

    async def start(self) -> None:
        """
        Initializes Playwright and launches a browser instance.
        """
        try:
            self.driver = await async_playwright().start()
            browser = await getattr(self.driver, self.browser_type).launch(headless=True, args=self.config.options)
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

    async def execute_locator(
            self,
            locator: Union[dict, SimpleNamespace],
            message: Optional[str] = None,
            typing_speed: float = 0,
            timeout: Optional[float] = 0,
            timeout_for_event: Optional[str] = 'presence_of_element_located',
    ) -> Union[str, list, dict, Locator, bool, None]:
        """
        Executes actions on a web element based on the provided locator.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            message: Optional message for events.
            typing_speed: Optional typing speed for events.
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').

        Returns:
             The result of the operation, which can be a string, list, dict, Locator, bool, or None.
        """
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        if not getattr(locator, "attribute", None) and not getattr(locator, "selector", None):
            logger.debug("Empty locator provided.")
            return None

        async def _parse_locator(
                locator: SimpleNamespace, message: Optional[str]
        ) -> Union[str, list, dict, Locator, bool, None]:
            """Parses and executes locator instructions."""
            if locator.event and locator.attribute and locator.mandatory is None:
                logger.debug("Locator with event and attribute but missing mandatory flag. Skipping.")
                return None

            if isinstance(locator.attribute, str) and isinstance(locator.by, str):
                try:
                    if locator.attribute:
                        locator.attribute = await self.evaluate_locator(locator.attribute)
                        if locator.by == "VALUE":
                            return locator.attribute
                except Exception as ex:
                    logger.debug(f"Error getting attribute by 'VALUE': {locator}, error: {ex}")
                    return None

                if locator.event:
                    return await self.execute_event(locator, message, typing_speed)

                if locator.attribute:
                    return await self.get_attribute_by_locator(locator)

                return await self.get_webelement_by_locator(locator)

            elif isinstance(locator.selector, list) and isinstance(locator.by, list):
                if locator.sorted == "pairs":
                    elements_pairs = []

                    for attribute, by, selector, event, timeout, timeout_for_event, locator_description in zip(
                        locator.attribute,
                        locator.by,
                        locator.selector,
                        locator.event,
                        locator.timeout,
                        locator.timeout_for_event,
                        locator.locator_description,
                    ):
                        l = SimpleNamespace(
                            **{
                                "attribute": attribute,
                                "by": by,
                                "selector": selector,
                                "event": event,
                                "timeout": timeout,
                                "timeout_for_event": timeout_for_event,
                                "locator_description": locator_description,
                            }
                        )
                        elements_pairs.append(await _parse_locator(l, message))

                    zipped_pairs = list(zip_longest(*elements_pairs, fillvalue=None))
                    return zipped_pairs

            else:
                logger.warning("Locator does not contain 'selector' and 'by' lists or invalid 'sorted' value.")

        return await _parse_locator(locator, message)


    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Evaluates and processes locator attributes.

        Args:
            attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

        Returns:
            The evaluated attribute, which can be a string, list of strings, or dictionary.
        """

        async def _evaluate(attr: str) -> Optional[str]:
            return attr

        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))

    async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
        """
        Gets the specified attribute from the web element.

        Args:
            locator: Locator data (dict or SimpleNamespace).

        Returns:
            Attribute or None.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        element = await self.get_webelement_by_locator(locator)

        if not element:
            logger.debug(f"Element not found: {locator=}")
            return None

        def _parse_dict_string(attr_string: str) -> dict | None:
            """Parses a string like '{attr1:attr2}' into a dictionary."""
            try:
                return {k.strip(): v.strip() for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))}
            except ValueError as ex:
                logger.debug(f"Invalid attribute string format: {attr_string}", ex)
                return None

        async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
            """Retrieves a single attribute from a Locator."""
            try:
                return await el.get_attribute(attr)
            except Exception as ex:
                logger.debug(f"Error getting attribute '{attr}' from element: {ex}")
                return None

        async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
            """Retrieves multiple attributes based on a dictionary."""
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

        Args:
            locator: Locator data (dict or SimpleNamespace).

        Returns:
            Playwright Locator
        """
        locator = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )
        if not locator:
            logger.error("Invalid locator provided.")
            return None
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
            logger.error(f'Ошибка поиска элемента: {locator=}', ex)
            return None

    async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
        """
        Takes a screenshot of the located web element.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            webelement: The web element Locator.

        Returns:
             Screenshot in bytes or None.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator)

        if not webelement:
            logger.debug(f"Element not found for screenshot: {locator=}")
            return None
        try:
             return await webelement.screenshot()
        except Exception as ex:
            logger.error(f"Failed to take screenshot: {locator=}", ex)
            return None


    async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]:
        """
        Executes the event associated with the locator.

         Args:
            locator: Locator data (dict or SimpleNamespace).
            message: Optional message for events.
            typing_speed: Optional typing speed for events.

        Returns:
           Execution status.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
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
                     logger.error(f"Error during click event: {locator=}", ex)
                     return False

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    continue
                logger.debug(f"Pause event parsing failed: {locator=}")
                return False

            elif event == "upload_media()":
                if not message:
                    logger.debug(f"Message is required for upload_media event: {message!r}")
                    return False
                try:
                    await element.set_input_files(message)
                    continue
                except Exception as ex:
                     logger.error(f"Error during file upload: {locator=}, {message=}", ex)
                     return False

            elif event == "screenshot()":
                 try:
                     result.append(await self.get_webelement_as_screenshot(locator, webelement=element))
                 except Exception as ex:
                      logger.error(f"Error during taking screenshot: {locator=}", ex)
                      return False

            elif event == "clear()":
                 try:
                     await element.clear()
                     continue
                 except Exception as ex:
                      logger.error(f"Error during clearing field: {locator=}", ex)
                      return False

            elif event.startswith("send_keys("):
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    for key in keys_to_send:
                        key = key.strip().strip("'")
                        if key:
                            await element.type(key)
                except Exception as ex:
                    logger.error(f"Error sending keys: {locator=}", ex)
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

        Args:
             locator: Information about the element's location on the page.
             message: The message to be sent to the web element.
             typing_speed: Speed of typing the message in seconds.

        Returns:
            Returns `True` if the message was sent successfully, `False` otherwise.
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        element = await self.get_webelement_by_locator(locator)
        if not element or (isinstance(element, list) and len(element) == 0):
             logger.debug(f"Element for send message not found: {locator=}")
             return False
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

        Args:
            url: URL to navigate to.
        """
        if self.page:
            try:
                 await self.page.goto(url)
            except Exception as ex:
                   logger.error(f'Error during navigation to {url=}', ex)