# CrawleePython Module Documentation

## Overview

This module provides a class, `CrawleePython`, for launching and managing web crawls using Playwright. It handles setting up the crawler, running the crawl, exporting the data, and retrieving the results.  It utilizes the `crawlee` library for simplified web crawling.

## Table of Contents

* [CrawleePython](#crawleepython)
    * [setup_crawler](#setup_crawler)
    * [run_crawler](#run_crawler)
    * [export_data](#export_data)
    * [get_data](#get_data)
    * [run](#run)


## Classes

### `CrawleePython`

**Description**: This class manages the entire crawling process, from initialization to data export.

**Constructor**:

```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox'):
    """ Initializes the CrawleeExperiment with the specified parameters """
    self.max_requests = max_requests
    self.headless = headless
    self.browser_type = browser_type
    self.crawler = None
```

**Methods**:

#### `setup_crawler`

```python
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
```

#### `run_crawler`

```python
async def run_crawler(self, urls: list[str]):
    """ Runs the crawler with the initial list of URLs 

    Args:
        urls (list[str]): List of URLs to start the crawl
    """
    await self.crawler.run(urls)
```

#### `export_data`

```python
async def export_data(self, file_path: str):
    """ Exports the entire dataset to a JSON file 

    Args:
        file_path (str): Path to save the exported JSON file
    """
    await self.crawler.export_data(file_path)
```

#### `get_data`

```python
async def get_data(self) -> dict:
    """ Retrieves the extracted data 

    Returns:
        dict: Extracted data as a dictionary
    """
    data = await self.crawler.get_data()
    return data
```

#### `run`

```python
async def run(self, urls: list[str]):
    """ Main method to set up, run the crawler, and export data 

    Args:
        urls (list[str]): List of URLs to start the crawl
    """
    await self.setup_crawler()
    await self.run_crawler(urls)
    await self.export_data(str(Path(gs.path.tmp / 'results.json')))
    data = await self.get_data()
    logger.info(f'Extracted data: {data.items}')
```

## Functions

(No functions defined directly in this module outside the class methods)


## Example Usage

```python
if __name__ == '__main__':
    async def main():
        experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
        await experiment.run(['https://ksp.co.il'])

    asyncio.run(main())
```


```