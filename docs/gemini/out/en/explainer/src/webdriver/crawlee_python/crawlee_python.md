# Crawlee Python Script Analysis

## <input code>

```python
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.webdriver.crawlee_python \n\t:platform: Windows, Unix\n\t:synopsis:\n\n"""\n\n\n\nfrom pathlib import Path\nfrom src import gs\nimport asyncio\nfrom crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext\nfrom src.logger import logger\n\nclass CrawleePython:\n    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox'):\n        """ Initializes the CrawleeExperiment with the specified parameters """\n        self.max_requests = max_requests\n        self.headless = headless\n        self.browser_type = browser_type\n        self.crawler = None\n\n    async def setup_crawler(self):\n        """ Sets up the PlaywrightCrawler instance """\n        self.crawler = PlaywrightCrawler(\n            max_requests_per_crawl=self.max_requests,\n            headless=self.headless,\n            browser_type=self.browser_type,\n        )\n\n        @self.crawler.router.default_handler\n        async def request_handler(context: PlaywrightCrawlingContext) -> None:\n            context.log.info(f'Processing {context.request.url} ...')\n\n            # Enqueue all links found on the page.\n            await context.enqueue_links()\n\n            # Extract data from the page using Playwright API.\n            data = {\n                'url': context.request.url,\n                'title': await context.page.title(),\n                'content': (await context.page.content())[:100],\n            }\n\n            # Push the extracted data to the default dataset.\n            await context.push_data(data)\n\n    async def run_crawler(self, urls: list[str]):\n        """ Runs the crawler with the initial list of URLs \n        \n        @param urls: List of URLs to start the crawl\n        """\n        await self.crawler.run(urls)\n\n    async def export_data(self, file_path: str):\n        """ Exports the entire dataset to a JSON file \n        \n        @param file_path: Path to save the exported JSON file\n        """\n        await self.crawler.export_data(file_path)\n\n    async def get_data(self) -> dict:\n        """ Retrieves the extracted data \n        \n        @return: Extracted data as a dictionary\n        """\n        data = await self.crawler.get_data()\n        return data\n\n    async def run(self, urls: list[str]):\n        """ Main method to set up, run the crawler, and export data \n        \n        @param urls: List of URLs to start the crawl\n        """\n        await self.setup_crawler()\n        await self.run_crawler(urls)\n        await self.export_data(str(Path(gs.path.tmp / 'results.json')))\n        data = await self.get_data()\n        logger.info(f'Extracted data: {data.items}\')\n\n\n# Example usage\nif __name__ == '__main__':\n    async def main():\n        experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')\n        await experiment.run(['https://ksp.co.il'])\n\n    asyncio.run(main())\n```

## <algorithm>

**Step 1:** Initialize `CrawleePython` object.

*   Input: `max_requests`, `headless`, `browser_type`.
*   Output: `CrawleePython` object with attributes `max_requests`, `headless`, `browser_type`, and `crawler` (initially None).
*   Example: `experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')`


**Step 2:** `setup_crawler()`

*   Input: `CrawleePython` object
*   Output: `self.crawler` (a `PlaywrightCrawler` instance).
*   Example: Sets up a `PlaywrightCrawler` instance with configured parameters, creates a `request_handler`.
*   Interacts with:  `PlaywrightCrawler` (`PlaywrightCrawlingContext`)

**Step 3:** `request_handler` (inside `setup_crawler`)

*   Input: `PlaywrightCrawlingContext`.
*   Output: None.
*   Example: logs URL being processed, enqueue links found on the page, extracts data (`url`, `title`, and `content` up to 100 characters), and pushes data to the default dataset.
*   Interacts with:  `PlaywrightCrawlingContext`.

**Step 4:** `run_crawler()`

*   Input: `CrawleePython` object and a list of `urls`.
*   Output: None.
*   Example: Executes the `run` method of `self.crawler`, initiating the crawl with the given URLs.
*   Interacts with:  `self.crawler` (PlaywrightCrawler)


**Step 5:** `export_data()`

*   Input: `CrawleePython` object and `file_path`.
*   Output: None.
*   Example: Exports the extracted data to the specified JSON file.
*   Interacts with: `self.crawler`.

**Step 6:** `get_data()`

*   Input: `CrawleePython` object.
*   Output: Extracted data as a dictionary.
*   Example: Retrieves the extracted data from the crawler.


**Step 7:** `run()` (main method)

*   Input: A list of `urls`.
*   Output: None.
*   Example: Calls `setup_crawler()`, `run_crawler()`, `export_data()`, `get_data()`.


## <mermaid>

```mermaid
graph TD
    A[CrawleePython] --> B(setup_crawler);
    B --> C{PlaywrightCrawler};
    C --> D[request_handler];
    D --> E(Enqueue Links);
    D --> F(Extract Data);
    D --> G(Push Data);
    F -- title, content --> H[Data];
    E --> H;
    G --> H;
    A --> I(run_crawler);
    I --> J[Run Crawling];
    A --> K(export_data);
    K --> L(Export to JSON);
    A --> M(get_data);
    M --> N[Retrieve Data];
    N --> O(logger.info);
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#ccf,stroke:#333,stroke-width:2px;
    style C fill:#ccf,stroke:#333,stroke-width:2px;
    style D fill:#ccf,stroke:#333,stroke-width:2px;
    style E fill:#ccf,stroke:#333,stroke-width:2px;
    style F fill:#ccf,stroke:#333,stroke-width:2px;
    style G fill:#ccf,stroke:#333,stroke-width:2px;
    style H fill:#ccf,stroke:#333,stroke-width:2px;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style J fill:#ccf,stroke:#333,stroke-width:2px;
    style K fill:#ccf,stroke:#333,stroke-width:2px;
    style L fill:#ccf,stroke:#333,stroke-width:2px;
    style M fill:#ccf,stroke:#333,stroke-width:2px;
    style N fill:#ccf,stroke:#333,stroke-width:2px;
    style O fill:#ccf,stroke:#333,stroke-width:2px;
    subgraph cluster_dependencies
        style cluster_dependencies fill:#ccf,stroke:#333,stroke-width:2px;
        from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
        from src import gs
        from src.logger import logger
    end
```

**Dependencies Analysis:**

*   `pathlib`: Provides path manipulation tools.
*   `gs`: Likely a custom module (`src.gs`) for global settings or file system interaction.
*   `asyncio`: Enables asynchronous programming for handling I/O operations efficiently.
*   `crawlee.playwright_crawler`: Likely a custom module (`crawlee.playwright_crawler`) for web crawling with Playwright.  Crucial for the crawling logic.
*   `src.logger`: A custom logging module.


## <explanation>

*   **Imports**:
    *   `pathlib`: Used for path manipulation, especially handling file paths.
    *   `gs`:  Probably for interacting with global settings or file paths, likely used here for storing temporary or other project-level data.
    *   `asyncio`: For writing asynchronous code, vital for handling web requests and I/O operations.
    *   `crawlee.playwright_crawler`:  A custom module likely for web scraping with Playwright, including the `PlaywrightCrawler` and `PlaywrightCrawlingContext` classes, providing the crawl functionality.
    *   `src.logger`: This module is for logging information.
*   **Classes**:
    *   `CrawleePython`: This class orcheStartes the web crawling process.
        *   `__init__`: Initializes attributes like `max_requests`, `headless`, `browser_type`, and the crawler instance (`self.crawler`, initially None).
        *   `setup_crawler`: Sets up the `PlaywrightCrawler` and adds a `request_handler`.
        *   `request_handler`: (inner function) Handles each URL by extracting data, enqueuing further links, and pushing data to a central storage.
        *   `run_crawler`: Executes the crawl on the provided URLs.
        *   `export_data`: Saves the extracted data to a JSON file.
        *   `get_data`: Retrieves the collected data.
        *   `run`: OrcheStartes the complete process (setup, crawl, export, data retrieval)

*   **Functions**:
    *   `setup_crawler`: Configures and initiates the `PlaywrightCrawler`.
    *   `run_crawler`: Starts the crawling process with the given URLs.
    *   `export_data`: Saves the gathered data to a file.
    *   `get_data`: Retrieves the gathered data.
    *   `run`: The main method, orcheStarting the crawl setup, execution, and data export.


*   **Variables**:
    *   `MODE`: A string variable likely used for different execution modes (e.g., `'dev'`, `'prod'`).
    *   `max_requests`: Integer, limits the number of concurrent requests for crawling.
    *   `headless`: Boolean, controls if the browser should run in headless mode (without a visible UI).
    *   `browser_type`: String, specifies which browser to use (e.g., 'firefox', 'chromium').


*   **Potential Errors/Improvements**:
    *   Error Handling: The code lacks explicit error handling (try-except blocks). Adding `try-except` around asynchronous operations could prevent crashes and provide feedback on issues.
    *   Data Validation: Check if the extracted data (`title`, `content`) is valid before storing it.  Validate the URLs, handling `None` values or malformed URLs properly.


*   **Relationships with other parts of the project**: The `src.gs` module is strongly dependent, as it is used for file paths.  `crawlee.playwright_crawler` is a crucial component containing the Playwright crawling logic.  The logging (`src.logger`) is an important part for tracking operations, errors and data.

The code appears to be a functional web crawler using Playwright, likely part of a larger system for extracting data from websites.  The use of asynchronous operations (`asyncio`) is appropriate for efficient web scraping.