## \file src/webdriver/javascript/js.py
## \file ../src/webdriver/javascript/js.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""Module containing JavaScript helper functions for Selenium WebDriver.

This module provides utility functions to interact with JavaScript through Selenium WebDriver.
Examples:
    # Initialize JavaScript helper
    js_helper = JavaScript(driver_instance)
    
    # Use JavaScript methods
    js_helper.window_focus()
    referrer = js_helper.get_referrer()
"""

from src import gs
from src.logger import logger


class JavaScript:
    """Provides JavaScript utility functions for interacting with a web page."""

    def __init__(self, driver):
        """Initializes the JavaScript helper with a Selenium WebDriver instance.

        Args:
            driver (`src.webdriver.Driver`): Selenium WebDriver instance to execute JavaScript.
        """
        self.driver = driver

    def unhide_DOM_element(self, element) -> bool:
        """Makes an invisible DOM element visible by modifying its style properties.

        Args:
            element: The WebElement object to make visible.

        Returns:
            bool: True if the script executes successfully, False otherwise.
        """
        script = """
        arguments[0].style.opacity = 1;
        arguments[0].style.transform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.MozTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.WebkitTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.msTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.OTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].scrollIntoView(true);
        return true;
        """
        try:
            self.driver.execute_script(script, element)
            return True
        except Exception as ex:
            logger.error("Error in unhide_DOM_element:", ex)
            return False

    @property
    def ready_state(self) -> str:
        """Retrieves the document loading status.

        Returns:
            str: 'loading' if the document is still loading, 'complete' if loading is finished.
        """
        try:
            return self.driver.execute_script("return document.readyState;")
        except Exception as ex:
            logger.error("Error retrieving document.readyState:", ex)
            return ""

    def window_focus(self) -> None:
        """Sets focus to the browser window using JavaScript.

        Attempts to bring the browser window to the foreground.
        """
        try:
            self.driver.execute_script("window.focus();")
        except Exception as ex:
            logger.error("Error executing window.focus():", ex)

    def get_referrer(self) -> str:
        """Retrieves the referrer URL of the current document.

        Returns:
            str: The referrer URL, or an empty string if unavailable.
        """
        try:
            return self.driver.execute_script("return document.referrer;") or ""
        except Exception as ex:
            logger.error("Error retrieving document.referrer:", ex)
            return ""

    def get_page_lang(self) -> str:
        """Retrieves the language of the current page.

        Returns:
            str: The language code of the page, or an empty string if unavailable.
        """
        try:
            return (
                self.driver.execute_script("return document.documentElement.lang;")
                or ""
            )
        except Exception as ex:
            logger.error("Error retrieving document.documentElement.lang:", ex)
            return ""
