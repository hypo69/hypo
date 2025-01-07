## \file /src/webdriver/chrome/chrome.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
```rst
.. module:: src.webdriver.chrome
    .. synonpsys: Module for Chrome WebDriver
```
Chrome WebDriver
=========================================================================================

This module contains a custom implementation of the Chrome WebDriver using Selenium. It integrates
configuration settings defined in the `chrome.json` file, such as user-agent and browser profile settings,
to enable flexible and automated browser interactions.

Key Features:
    - Centralized configuration via JSON files.
    - Support for multiple browser profiles.
    - Enhanced logging and error handling.
    - Ability to pass custom options during initialization.

Example usage
--------------------

Example of using the `Chrome` class:

.. code-block:: python

    from src.webdriver.chrome import Chrome

    # Initialize Chrome WebDriver with user-agent settings and custom options
    browser = Chrome(user_agent='Mozilla/5.0...', options=["--headless", "--disable-gpu"])
    browser.get("https://www.example.com")
    browser.quit()
"""



import os
import sys
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException

import header
from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Chrome(webdriver.Chrome):
    """
    Class for Chrome WebDriver.

    This class extends the Selenium Chrome WebDriver and provides a singleton pattern and custom configurations.
    """

    _instance = None
    """
    _instance (Chrome): The single instance of the Chrome WebDriver.
    """
    driver_name: str = 'chrome'
    """
    driver_name (str): The name of the driver ('chrome').
    """
    config: SimpleNamespace
    """
    config (SimpleNamespace): Configuration settings loaded from a JSON file.
    """

    def __new__(cls, *args, **kwargs):
        """
        Ensure a single instance of Chrome WebDriver.

        If an instance already exists, it calls `window_open()`.

        :return: The singleton instance of the Chrome WebDriver.
        :rtype: Chrome
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance.window_open()  # Open a new window if instance already exists
        return cls._instance

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs):
        """
        Initializes the Chrome WebDriver with specified options and profile.

        :param user_agent: The user-agent string to be used. Defaults to a random user agent.
        :type user_agent: Optional[str]
        :param options: A list of Chrome options to be passed during initialization.
        :type options: Optional[List[str]]
        """
        try:
            # Set user_agent or generate a random one
            user_agent = user_agent or UserAgent().random
            # Load configurations from JSON file
            self.config = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))

            # Check if the configuration is loaded
            if not self.config:
                logger.debug('Error in `chrome.json` file.')
                return

            # Initialize options
            options_obj = ChromeOptions()

            # Add arguments from the configuration's options
            if hasattr(self.config, 'options') and self.config.options:
                for option in self.config.options:
                    options_obj.add_argument(option)

            # Add custom options passed during initialization
            if options:
                for option in options:
                    options_obj.add_argument(option)

            # Add arguments from the configuration's headers
            if hasattr(self.config, 'headers') and self.config.headers:
                for key, value in vars(self.config.headers).items():
                    options_obj.add_argument(f'--{key}={value}')

            # Normalize paths
            def normalize_path(path: str) -> str:
                """
                Replace placeholders with actual environment paths.

                :param path: The path string with placeholders like %APPDATA% or %LOCALAPPDATA%.
                :type path: str
                :return: The normalized path with environment variables substituted.
                :rtype: str
                """
                if not path:
                    return ''
                return (
                    path.replace('%APPDATA%', os.environ.get('APPDATA', ''))
                    .replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA', ''))
                )

            profile_directory = Path(gs.path.root / normalize_path(self.config.profile_directory.testing))
            binary_location = Path(gs.path.root / normalize_path(self.config.binary_location.binary))

            # Check if the profile directory exists and add the argument
            if profile_directory:
                options_obj.add_argument(f'user-data-dir={profile_directory}')

            # Set the path to the executable file
            options_obj.binary_location = str(binary_location)
            # Initialize the Chrome driver service
            service = ChromeService(executable_path=str(binary_location)) if binary_location else ChromeService()

        except Exception as ex:
            logger.error('Error setting up Chrome WebDriver:', ex)
            return

        try:
            # Initialize the WebDriver
            super().__init__(options=options_obj, service=service)
        except WebDriverException as ex:
            logger.critical('Error initializing Chrome WebDriver:', ex)
            return
        except Exception as ex:
            logger.critical('Chrome WebDriver crashed. General error:', ex)
            return

        self._payload()

    def _payload(self) -> None:
        """
        Load executor for locators and JavaScript scenarios.

        This method initializes and assigns the necessary executors for web element interaction and
        JavaScript execution within the WebDriver.
        """
        js_executor = JavaScript(self)
        self.get_page_lang = js_executor.get_page_lang
        self.ready_state = js_executor.ready_state
        self.get_referrer = js_executor.get_referrer
        self.unhide_DOM_element = js_executor.unhide_DOM_element
        self.window_focus = js_executor.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message


if __name__ == "__main__":
    driver = Chrome(options=["--headless", "--disable-gpu"])
    driver.get(r"https://google.com")
