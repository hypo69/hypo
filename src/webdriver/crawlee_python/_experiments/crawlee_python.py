#! /usr/bin/python
""" Эксперименты с бибилиотекой crawlee-python """
## \file /src/webdriver/crawlee_python/_experiments/crawlee_python.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
from pathlib import Path
import header 
from src import gs
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext

async def main() -> None:
    crawler = PlaywrightCrawler(
        max_requests_per_crawl=5,  # Limit the crawl to 5 requests.
        headless=False,  # Show the browser window.
        browser_type='firefox',  # Use the Firefox browser.
    )

    # Define the default request handler, which will be called for every request.
    @crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
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

    # Run the crawler with the initial list of URLs.
    await crawler.run(['https://ksp.co.il'])

    # Export the entire dataset to a JSON file.
    await crawler.export_data(str(Path(gs.path.tmp / 'results.json')))

    # Or work with the data directly.
    data = await crawler.get_data()
    crawler.log.info(f'Extracted data: {data.items}')


if __name__ == '__main__':
    asyncio.run(main())