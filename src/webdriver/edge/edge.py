## \file hypotez/src/webdriver/edge/edge.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.webdriver.edge """
MODE = 'development'


""" Custom Edge WebDriver class with simplified configuration using fake_useragent."""

from pathlib import Path
from selenium.webdriver import Edge as WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from fake_useragent import UserAgent
from src import gs
from src.logger import logger

class Edge(WebDriver):
    """
    Subclass of `selenium.webdriver.Edge` that provides additional functionality.
    
    @param user_agent (dict): A dictionary to specify the user agent. If None, a random user agent is generated.
    """
    driver_name = 'edge'

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """ Initializes the Edge WebDriver with the specified user agent and options.
        @param user_agent `dict`: A dictionary to specify the user agent. If None, a random user agent is generated.
        """
        # Generate a random user agent if none is provided
        self.user_agent = user_agent if user_agent else UserAgent().random

        # Path to msedgedriver executable (make sure to adjust this path as needed)
        settings: SimpleNamespace = j_loads_ns(Path(gs.path.src / 'webdriver' / 'edge' / 'edge.json'))

        # Create EdgeOptions and set user agent
        options = EdgeOptions()
        options.add_argument(f'user-agent={self.user_agent}')

        try:
            logger.info("Starting Edge WebDriver")
            service = EdgeService(executable_path=str(edgedriver_path))
            super().__init__(options=options, service=service)
            self._payload()
        except WebDriverException as ex:
            logger.critical("Edge WebDriver failed to start:", ex)
            """ @todo Implement driver restart"""
            ...
            return
        except Exception as ex:
            logger.critical("Edge WebDriver crashed. General error:", ex)
            """ @todo Implement program restart"""
            ...
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

    def set_options(self, opts: list[str] = None) -> EdgeOptions:
        """Launch options for the Edge WebDriver."""
        options = EdgeOptions()
        if opts:
            for opt in opts:
                options.add_argument(opt)
        return options
