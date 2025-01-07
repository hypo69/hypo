## \file /src/webdriver/crawlee_python/crawlee_python.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.crawlee_python 
    :platform: Windows, Unix
    :synopsis: Crawlee Python Crawler

This module provides a custom implementation of `PlaywrightCrawler` using the Crawlee library. It allows you to configure browser settings, handle requests, and extract data from web pages.

Example usage:

.. code-block:: python

    if __name__ == "__main__":
        async def main():
            crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
            await crawler.run(['https://www.example.com'])

        asyncio.run(main())
"""



from pathlib import Path
from typing import Optional, List, Dict, Any
from src import gs
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class CrawleePython:
    """
    Custom implementation of `PlaywrightCrawler` using the Crawlee library.

    Attributes:
        max_requests (int): Maximum number of requests to perform during the crawl.
        headless (bool): Whether to run the browser in headless mode.
        browser_type (str): The type of browser to use ('chromium', 'firefox', 'webkit').
        crawler (PlaywrightCrawler): The PlaywrightCrawler instance.
    """

    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
        """
        Initializes the CrawleePython crawler with the specified parameters.

        :param max_requests: Maximum number of requests to perform during the crawl.
        :type max_requests: int
        :param headless: Whether to run the browser in headless mode.
        :type headless: bool
        :param browser_type: The type of browser to use ('chromium', 'firefox', 'webkit').
        :type browser_type: str
        :param options: A list of custom options to pass to the browser.
        :type options: Optional[List[str]]
        """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.options = options or []
        self.crawler = None

    async def setup_crawler(self):
        """
        Sets up the PlaywrightCrawler instance with the specified configuration.
        """
        self.crawler = PlaywrightCrawler(
            max_requests_per_crawl=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
            launch_options={"args": self.options}
        )

        @self.crawler.router.default_handler
        async def request_handler(context: PlaywrightCrawlingContext) -> None:
            """
            Default request handler for processing web pages.

            :param context: The crawling context.
            :type context: PlaywrightCrawlingContext
            """
            context.log.info(f'Processing {context.request.url} ...')

            # Enqueue all links found on the page.
            await context.enqueue_links()

            # Extract data from the page using Playwright API.
            data = {
                'url': context.request.url,
                'title': await context.page.title(),
                'content': (await context.page.content())[:100],
            }

            # Push the extracted data to the default dataset.
            await context.push_data(data)

    async def run_crawler(self, urls: List[str]):
        """
        Runs the crawler with the initial list of URLs.

        :param urls: List of URLs to start the crawl.
        :type urls: List[str]
        """
        await self.crawler.run(urls)

    async def export_data(self, file_path: str):
        """
        Exports the entire dataset to a JSON file.

        :param file_path: Path to save the exported JSON file.
        :type file_path: str
        """
        await self.crawler.export_data(file_path)

    async def get_data(self) -> Dict[str, Any]:
        """
        Retrieves the extracted data.

        :return: Extracted data as a dictionary.
        :rtype: Dict[str, Any]
        """
        data = await self.crawler.get_data()
        return data

    async def run(self, urls: List[str]):
        """
        Main method to set up, run the crawler, and export data.

        :param urls: List of URLs to start the crawl.
        :type urls: List[str]
        """
        try:
            await self.setup_crawler()
            await self.run_crawler(urls)
            await self.export_data(str(Path(gs.path.tmp / 'results.json')))
            data = await self.get_data()
            logger.info(f'Extracted data: {data.items()}')
        except Exception as ex:
            logger.critical('Crawler failed with an error:', ex)


# Example usage
if __name__ == '__main__':
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())