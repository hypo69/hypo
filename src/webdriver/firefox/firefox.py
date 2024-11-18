## \file hypotez/src/webdriver/firefox/firefox.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.webdriver.firefox """
MODE = 'development'


""" Firefox WebDriver

This code defines a subclass of `webdriver.Firefox` called `Firefox`. 
It provides additional functionality such as the ability to launch Firefox 
in kiosk mode and the ability to set up a Firefox profile for the WebDriver.

@code
# Example usage
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    
    browser = Firefox(profile_name=profile_name, geckodriver_version=geckodriver_version, firefox_version=firefox_version)
    browser.get("https://www.example.com")
    browser.quit()
@endcode
@image html class_firefox.png
"""


import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript


from fake_useragent import UserAgent

from src import gs
from src.utils import j_loads_ns
from src.logger import logger

class Firefox(WebDriver):
    """ Subclass of `webdriver.Firefox` that provides additional functionality."""

    driver_name = 'firefox'
    
    def __init__(self, profile_name: Optional[str] = None, geckodriver_version: Optional[str] = None, firefox_version: Optional[str] = None, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """ Initializes the Firefox WebDriver with the specified launch options, profile, geckodriver version, and Firefox version.
        @param profile_name `str`: Name of the Firefox profile to use.
        @param geckodriver_version `str`: Version of the geckodriver to use.
        @param firefox_version `str`: Version of Firefox to use.
        @param user_agent `dict`: A dictionary containing user agent settings.
        """
        ...
        
        def normilize_path(path: str) -> str:
            """Replace placeholders with actual environment paths.

            Args:
                path (str): The path string with placeholders like %APPDATA% or %LOCALAPPDATA%.

            Returns:
                str: The normalized path with environment variables substituted.
            """
            if not path:
                return ""

            return str(path).replace('%APPDATA%', os.environ.get('APPDATA')).replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA'))
            ...

        service = None
        profile = None
        options = None

        settings: SimpleNamespace = j_loads_ns(Path(gs.path.src / 'webdriver' / 'firefox' / 'firefox.json'))

        geckodriver_path: str = str(Path(gs.path.root, settings.executable_path.geckodriver))
        firefox_binary_path: str = str(Path(gs.path.root, settings.executable_path.firefox_binary))

        #service
        service = Service(geckodriver_path)

        # options
        # Add arguments from options_settings
        options = Options()
        if hasattr(settings, 'options') and settings.options:
            for key, value in vars(settings.options).items():
                options.add_argument(f"--{key}={value}")

        # Add arguments from settings.headers
        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                options.add_argument(f"--{key}={value}")

        if hasattr(settings, 'headers'):
            for key, value in settings.headers.__dict__.items():
                options.add_argument(f"--{key}={value}")

        # Set a random user agent
        user_agent = UserAgent()
        options.set_preference('general.useragent.override', user_agent.random)

        #profile
        profile_directory = settings.profile_directory.os if settings.profile_directory.default == 'os' else str(Path(gs.path.src, settings.profile_directory.internal))
        
        if profile_name:
            profile_directory = str(Path(profile_directory).parent / profile_name)
        
        if '%LOCALAPPDATA%' in profile_directory:
            profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))

        profile = FirefoxProfile(profile_directory=profile_directory)
        
        try:
            logger.info("Start Firefox")
            super().__init__(service=service, options=options)

            self._payload()

        except WebDriverException as ex:
            logger.critical("""
                ---------------------------------
                    Could not start the driver
                    This can happen due to updates to Firefox
                    or if it is not installed on the OS.
                ----------------------------------""", ex)
            ...
            return
        except Exception as ex:
            logger.critical('Firefox WebDriver failed with an error:', ex)
            return

    def _payload(self):
        """ Load executor for locators an javascript scenarios """
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
        

if __name__ == "main":
    driver = Firefox()
    driver.get(r"https://google.com")