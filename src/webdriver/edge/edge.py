## \file /src/webdriver/edge/edge.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module::  src.webdriver.edge
   :platform: Windows, Unix
   :synopsis: Custom Edge WebDriver class with simplified configuration using fake_useragent.

"""



import os
from pathlib import Path
from typing import Optional, List
from selenium.webdriver import Edge as WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from fake_useragent import UserAgent
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class Edge(WebDriver):
    """
    Custom Edge WebDriver class for enhanced functionality.

    Attributes:
        driver_name (str): Name of the WebDriver used, defaults to 'edge'.
    """
    driver_name: str = 'edge'

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Edge WebDriver with the specified user agent and options.

        :param user_agent: The user-agent string to be used. If `None`, a random user agent is generated.
        :type user_agent: Optional[str]
        :param options: A list of Edge options to be passed during initialization.
        :type options: Optional[List[str]]
        """
        self.user_agent = user_agent or UserAgent().random
        settings = j_loads_ns(Path(gs.path.src, 'webdriver', 'edge', 'edge.json'))

        # Initialize Edge options
        options_obj = EdgeOptions()
        options_obj.add_argument(f'user-agent={self.user_agent}')

        # Add custom options passed during initialization
        if options:
            for option in options:
                options_obj.add_argument(option)

        # Add arguments from the configuration's options
        if hasattr(settings, 'options') and settings.options:
            for option in settings.options:
                options_obj.add_argument(option)

        # Add arguments from the configuration's headers
        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                options_obj.add_argument(f'--{key}={value}')

        try:
            logger.info('Starting Edge WebDriver')
            edgedriver_path = settings.executable_path.default  # Ensure this is correctly defined in your JSON file
            service = EdgeService(executable_path=str(edgedriver_path))
            super().__init__(options=options_obj, service=service)
            self._payload()
        except WebDriverException as ex:
            logger.critical('Edge WebDriver failed to start:', ex)
            return
        except Exception as ex:
            logger.critical('Edge WebDriver crashed. General error:', ex)
            return

    def _payload(self) -> None:
        """
        Load executors for locators and JavaScript scenarios.
        """
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

    def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:  
        """  
        Create and configure launch options for the Edge WebDriver.  

        :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.  
        :return: Configured `EdgeOptions` object.  
        """  
        options = EdgeOptions()  
        if opts:  
            for opt in opts:  
                options.add_argument(opt)  
        return options  


if __name__ == "__main__":
    driver = Edge(options=["--headless", "--disable-gpu"])
    driver.get("https://www.example.com")