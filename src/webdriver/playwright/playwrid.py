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
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Playwrid(PlaywrightCrawler):
    """
    Subclass of `PlaywrightCrawler` that provides additional functionality.

    Attributes:
        driver_name (str): Name of the driver, defaults to 'playwrid'.
    """
    driver_name = 'playwrid'
    context = None

    def __init__(self, settings_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Playwright Crawler with the specified launch options, settings, and user agent.

        :param settings_name: Name of the settings file to use.
        :type settings_name: Optional[str]
        :param user_agent: The user-agent string to be used. Defaults to a random user agent.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]
        """
        settings = self._load_settings(settings_name)
        launch_options = self._set_launch_options(settings, user_agent, options)

        super().__init__(
            playwright_launch_options=launch_options,
            browser_type=settings.browser_type,
            **kwargs
        )

    def _load_settings(self, settings_name: Optional[str] = None) -> SimpleNamespace:
        """
        Loads the settings for the Playwrid Crawler.

        :param settings_name: Name of the settings file to use.
        :type settings_name: Optional[str]
        :returns: A SimpleNamespace object containing the settings.
        :rtype: SimpleNamespace
        """
        settings_path = Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        settings = j_loads_ns(settings_path)

        if settings_name:
            custom_settings_path = settings_path.parent / f'{settings_name}.json'
            if custom_settings_path.exists():
                settings = j_loads_ns(custom_settings_path)

        return settings

    def _set_launch_options(self, settings: SimpleNamespace, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
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
            "headless": settings.headless if hasattr(settings, 'headless') else True,
            "args": settings.options if hasattr(settings, 'options') else []
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
            super().run()
        except Exception as ex:
            logger.critical('Playwrid Crawler failed with an error:', ex)

    @property
    def current_url(self) -> Optional[str]:
        """
        Returns the current URL of the browser.

        :returns: The current URL.
        :rtype: Optional[str]
        """
        if self.context:
            return self.context.page.url
        return None


if __name__ == "__main__":
    browser = Playwrid(options=["--headless"])
    browser.start("https://www.example.com")