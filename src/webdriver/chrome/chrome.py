## \file hypotez/src/webdriver/chrome/chrome.py
# -*- coding: utf-8 -*-

""" module: src.webdriver.chrome """
MODE = 'debug'
""" module: src.webdriver.chrome """
MODE = 'debug'

""" Chrome WebDriver.
Implemented using Chrome for Developers.
Chrome WebDriver  settings defined in the `chrome.json` file.

"""
...
import os
import sys
import threading
import socket
from pathlib import Path
from typing import List, Optional, Dict, Union
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript import JavaScript
from __init__ import gs
from src.utils.jjson import j_loads_ns
from src.logger import logger


class Chrome(webdriver.Chrome):
    """ Singleton class for Chrome WebDriver."""

    _instance = None
    driver_name: str = 'chrome'

    def __new__(cls, *args, **kwargs):
        """ Ensure a single instance of Chrome WebDriver. Calls window_open() if instance already exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance.window_open()  # Call window_open() if instance already exists
        return cls._instance

    def __init__(self, user_agent=None, *args, **kwargs):
        """ Initializes the Chrome WebDriver with the specified options and profile.

        Args:
            user_agent (str, optional): The user agent string to be used. Defaults to a random user agent.
        """
        ...
        try:
            # Function attributes declaration
            user_agent = user_agent if user_agent else UserAgent().random
            settings =  j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))  # Load settings from JSON file
            if not settings:
                logger.debug(f"Ошибка в файле {gs.path.src}/webdriver/chrome/chrome.json")
                ...
            options: ChromeOptions = ChromeOptions()  # Initialize options
            profile_directory: Path  # Set user data directory
            executable_path: str

            def normilize_path(path: str) -> str:
                """ Replace placeholders with actual environment paths.

                Args:
                    path (str): The path string with placeholders like %APPDATA% or %LOCALAPPDATA%.

                Returns:
                    str: The normalized path with environment variables substituted.
                """
                if not path:
                    return ""

                return str(path).replace('%APPDATA%', os.environ.get('APPDATA')).replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA'))
                ...

            # Add arguments from options_settings
            if hasattr(settings, 'options') and settings.options:

                for key, value in vars(settings.options).items():
                    options.add_argument(f"--{key}={value}")

            # Add arguments from settings.headers
            if hasattr(settings, 'headers') and settings.headers:
                for key, value in vars(settings.headers).items():
                    options.add_argument(f"--{key}={value}")

            profile_directory: str = normilize_path(
                getattr(settings.profile_directory, settings.profile_directory.default))

            executable_path: str = str(
                Path(gs.path.root, getattr(settings.executable_path, settings.executable_path.default))
            )
                                                                                                                          
            if profile_directory:
                options.add_argument(f'user-data-dir={profile_directory}')

            # Additional options
            options.binary_location = executable_path

            service = ChromeService(executable_path = executable_path) if executable_path else ChromeService()

        except Exception as ex:
            logger.error('Error setting up Chrome WebDriver.', ex)
            ...
            return

        try:
            super().__init__(options=options)
            ...
        except WebDriverException as ex:
            logger.critical("Error initializing Chrome WebDriver:", ex, True)
            ...
            return
        except Exception as ex:
            logger.critical("Chrome WebDriver crashed. General error:", ex, True)
            ...
            return

        self._payload()

    def _payload(self):
        """ Load executor for locators and JavaScript scenarios."""
        ...
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message

    def window_open(self, url: Optional[str] = None):
        """Open a new tab in the current browser window and switch to it.

        Args:
            url (Optional[str]): URL to open in the new tab. Defaults to `None`.
        """
        # Open a new tab in the current window
        self.execute_script("window.open();")
    
        # Switch to the new tab (which is the last tab in the window handles list)
        self.switch_to.window(self.window_handles[-1])

        # If a URL is provided, navigate to it
        if url:
            self.get(url)
