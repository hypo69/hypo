```python
## \file hypotez/src/webdriver/crawlee_python/crawlee_python.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.webdriver.crawlee_python 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


from pathlib import Path
from src import gs
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src.logger import logger

class CrawleePython:
    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox'):
        """ Initializes the CrawleeExperiment with the specified parameters """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.crawler = None

    async def setup_crawler(self):
        """ Sets up the PlaywrightCrawler instance """
        self.crawler = PlaywrightCrawler(
            max_requests_per_crawl=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
        )

        @self.crawler.router.default_handler
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

    async def run_crawler(self, urls: list[str]):
        """ Runs the crawler with the initial list of URLs 

        @param urls: List of URLs to start the crawl
        """
        await self.crawler.run(urls)

    async def export_data(self, file_path: str):
        """ Exports the entire dataset to a JSON file 

        @param file_path: Path to save the exported JSON file
        """
        await self.crawler.export_data(file_path)

    async def get_data(self) -> dict:
        """ Retrieves the extracted data 

        @return: Extracted data as a dictionary
        """
        data = await self.crawler.get_data()
        return data

    async def run(self, urls: list[str]):
        """ Main method to set up, run the crawler, and export data 

        @param urls: List of URLs to start the crawl
        """
        await self.setup_crawler()
        await self.run_crawler(urls)
        await self.export_data(str(Path(gs.path.tmp / 'results.json')))
        data = await self.get_data()
        logger.info(f'Extracted data: {data.items()}')


# Example usage
if __name__ == '__main__':
    async def main():
        experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
        await experiment.run(['https://ksp.co.il'])

    asyncio.run(main())
```

```
<algorithm>
* **Initialization**: The `CrawleePython` object is created, setting parameters like `max_requests`, `headless` mode, and browser type.  No data is present yet.
* **Crawler Setup**: `setup_crawler` instantiates a `PlaywrightCrawler` with the given parameters. A `@self.crawler.router.default_handler` decorator defines the `request_handler` function, which will process each URL.
* **URL Processing**: The `run_crawler` function initiates the crawl using `self.crawler.run(urls)`.  Each URL in the input list triggers a call to the `request_handler` function.
* **Data Extraction**: Inside `request_handler`, Playwright extracts the title and content (up to 100 characters) and stores them, along with the URL, in the `data` dictionary. This data is then enqueued.
* **Data Enqueuing**: `context.enqueue_links()` adds any links found on the current page to the queue for further processing.
* **Data Pushing**:  `context.push_data(data)` adds the extracted data to the crawler's dataset.
* **Exporting**: The `export_data` method, called by `run`, utilizes `self.crawler.export_data(file_path)` to save the accumulated data to a JSON file.
* **Data Retrieval**: `get_data` retrieves the complete data and returns it.
* **Logging**: The main loop logs the extracted data.

**Data Flow Example:**

```
[urls] --> run_crawler --> request_handler
                                  |
                                  V
                   [Page content] --extract--> [data] --> push_data (crawler's dataset)
                                   |
                                   V
                  [links found] --> enqueue_links --> request_handler
```
</algorithm>
```

```
<explanation>
* **Imports**:
    * `pathlib`: For working with file paths (e.g., constructing the output file path).
    * `gs`: Likely from a custom `src` package, probably handling global settings or configurations, particularly file paths.
    * `asyncio`: For asynchronous operations, crucial for handling network requests efficiently.
    * `crawlee.playwright_crawler`: Custom module from the `crawlee` package (likely part of the same project) providing the functionality to manage the web crawling process using Playwright.
    * `src.logger`: Module for logging operations within the project.  Its relationship to the `src` package structure is that it probably implements logging functionalities relevant to the specific needs of the project.
* **Classes**:
    * `CrawleePython`:  This class encapsulates the web crawling logic.
        * `__init__`: Initializes the crawler with parameters (max requests, headless mode, browser type).
        * `setup_crawler`: Sets up the `PlaywrightCrawler` instance.
        * `run_crawler`: Executes the crawl with a given set of URLs.
        * `export_data`: Saves the extracted data to a JSON file.
        * `get_data`: Retrieves the extracted data.
        * `run`: The main method orchestrates the entire crawling process.
* **Functions**:
    * `setup_crawler`: Initializes the crawling infrastructure using the provided parameters.
    * `run_crawler`: Executes the crawl for the given URLs and stores the resulting dataset.
    * `export_data`: Saves the entire dataset to a JSON file at the specified path.
    * `get_data`: Returns the collected dataset.
    * `request_handler`: Processes a single URL: fetches the title and content. (Internal method of `PlaywrightCrawler`).
* **Variables**:
    * `MODE`: A constant string defining the operation mode (e.g., 'dev', 'prod').
    * `max_requests`, `headless`, `browser_type`: Control the behavior of the crawler.
    * `urls`: The list of URLs to start the crawl.
    * `data`: Holds the extracted data for a single URL.
* **Potential Errors/Improvements**:
    * **Error Handling:** The code lacks robust error handling.  If a website is unreachable or a request fails, the program might crash.  Adding `try...except` blocks around potentially problematic operations is crucial.  For instance, `await context.page.content()` could raise an exception if the page doesn't load correctly.
    * **Rate Limiting:** The `max_requests` parameter might not be enough if the site has rate limits. Implement rate-limiting mechanisms to avoid being blocked.
    * **Robust URL Handling**: Ensure the code handles malformed or invalid URLs gracefully.
    * **Data Validation:**  Add checks to ensure the extracted `title` and `content` are not `None` before storing them.
    * **File Existence Check**:  Check if the output directory exists and create it if necessary to prevent errors.

**Relationship Chain**:

The `crawlee_python` module interacts with the `gs` (likely a global settings) package and the `logger` package to manage file paths and log messages. It critically relies on the `crawlee.playwright_crawler` package for the actual web crawling using Playwright. This suggests a layered architecture where different packages handle distinct tasks, with `crawlee_python` acting as a central controller.
</explanation>
```