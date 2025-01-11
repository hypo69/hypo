## \file /src/webdriver/playwright/playwrid.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.playwright 
    :platform: Windows, Unix
    :synopsis: Playwright Crawler

This module defines a subclass of `PlaywrightCrawler` called `Playwrid`. 
It provides additional functionality such as the ability to set custom browser settings, profiles, and launch options using Playwright.

Example usage:

.. code-block:: python

    if __name__ == "__main__":
        browser = Playwrid(options=["--headless"])
        browser.start("https://www.example.com")
"""

from pathlib import Path
from typing import Optional, Dict, Any, List
from types import SimpleNamespace
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext

import header
from src import gs
from src.webdriver.playwright.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Playwrid(PlaywrightCrawler , ExecuteLocator, JavaScript):
    """
    Subclass of `PlaywrightCrawler` that provides additional functionality.

    Attributes:
        driver_name (str): Name of the driver, defaults to 'playwrid'.
    """
    driver_name: str = 'playwrid'
    base_path: Path = gs.path.src / 'webdriver' / 'playwright'
    config: SimpleNamespace = j_loads_ns(base_path / 'playwrid.json')
    context = None

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Playwright Crawler with the specified launch options, settings, and user agent.

        :param settings_name: Name of the settings file to use.
        :type settings_name: Optional[str]
        :param user_agent: The user-agent string to be used. Defaults to a random user agent.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]
        """

        launch_options = self._set_launch_options(user_agent, options)

        super().__init__(
            playwright_launch_options=launch_options,
            browser_type=self.config.browser_type,
            **kwargs
        )



    def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Configures the launch options for the Playwright Crawler.

        :param settings: A SimpleNamespace object containing launch settings.
        :type settings: SimpleNamespace
        :param user_agent: The user-agent string to be used.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]
        :returns: A dictionary with launch options for Playwright.
        :rtype: Dict[str, Any]
        """
        launch_options = {
            "headless": self.config.headless if hasattr(self.config, 'headless') else True,
            "args": self.config.options if hasattr(self.config, 'options') else []
        }

        # Add custom user-agent if provided
        if user_agent:
            launch_options['user_agent'] = user_agent

        # Merge custom options with default options
        if options:
            launch_options['args'].extend(options)

        return launch_options

    def start(self, url: str) -> None:
        """
        Starts the Playwrid Crawler and navigates to the specified URL.

        :param url: The URL to navigate to.
        :type url: str
        """
        try:
            logger.info(f"Starting Playwright Crawler for {url}")
            super().run(url)
            # получаем контекст
            self.context = self.crawling_context
        except Exception as ex:
            logger.critical('Playwrid Crawler failed with an error:', ex)

    @property
    def current_url(self) -> Optional[str]:
        """
        Returns the current URL of the browser.

        :returns: The current URL.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            return self.context.page.url
        return None

    def get_page_content(self) -> Optional[str]:
        """
        Returns the HTML content of the current page.

        :returns: HTML content of the page.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            return self.context.page.content()
        return None

    def get_element_content(self, selector: str) -> Optional[str]:
        """
        Returns the inner HTML content of a single element on the page by CSS selector.

        :param selector: CSS selector for the element.
        :type selector: str
        :returns: Inner HTML content of the element, or None if not found.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(selector)
                return element.inner_html()
            except Exception as ex:
                logger.warning(f"Element with selector '{selector}' not found or error during extraction: {ex}")
                return None
        return None



        
if __name__ == "__main__":
    browser = Playwrid(options=["--headless"])
    browser.start("https://www.example.com")
    
    # Получение HTML всего документа
    html_content = browser.get_page_content()
    if html_content:
        print(html_content[:200])  # Выведем первые 200 символов для примера
    else:
        print("Не удалось получить HTML-контент.")
    
    # Получение HTML элемента по селектору
    element_content = browser.get_element_content("h1")
    if element_content:
        print("\nСодержимое элемента h1:")
        print(element_content)
    else:
         print("\nЭлемент h1 не найден.")
    
    # Получение значения элемента по xpath
    xpath_value = browser.get_element_value_by_xpath("//head/title")
    if xpath_value:
         print(f"\nЗначение элемента по XPATH //head/title: {xpath_value}")
    else:
         print("\nЭлемент по XPATH //head/title не найден")

    # Нажатие на кнопку (при наличии)
    browser.click_element("button")
    