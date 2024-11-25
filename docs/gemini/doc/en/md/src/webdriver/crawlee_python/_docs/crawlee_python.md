# Crawlee Python Documentation

## Overview

This module provides a Python class, `CrawleePython`, for performing web scraping using the `crawlee` library with Playwright. It handles the setup, execution, and data export of a web crawler, allowing for efficient and customizable data collection from websites.

## Table of Contents

* [Classes](#classes)
    * [CrawleePython](#crawleepython)
        * [`__init__`](#init)
        * [`setup_crawler`](#setup_crawler)
        * [`run_crawler`](#run_crawler)
        * [`export_data`](#export_data)
        * [`get_data`](#get_data)
        * [`run`](#run)

## Classes

### `CrawleePython`

**Description**: This class encapsulates the web scraping process using Playwright and the `crawlee` library. It handles initialization, crawler setup, execution, data extraction, and export.

#### `__init__`

**Description**: Initializes the `CrawleePython` object.

**Parameters**:

- `max_requests` (int): The maximum number of requests to be made during the crawl.
- `headless` (bool): A boolean indicating whether to run the browser in headless mode. Defaults to `True`.
- `browser_type` (str): The type of browser to use (e.g., 'chromium', 'firefox'). Defaults to 'chromium'.


**Raises**:
- `ValueError`: If `max_requests` is not a positive integer.
- `TypeError`: If `headless` is not a boolean.



#### `setup_crawler`

**Description**: Configures the crawler by defining a default request handler.

**Parameters**:
- None

**Returns**:
- `None`

#### `run_crawler`

**Description**: Starts the crawling process with a list of initial URLs.

**Parameters**:
- `initial_urls` (list): A list of URLs to start the crawling process from.

**Returns**:
- `None`

**Raises**:
- `TypeError`: If `initial_urls` is not a list.



#### `export_data`

**Description**: Exports the collected data to a specified JSON file.

**Parameters**:
- `file_path` (str): The path to the JSON file where the data will be exported.

**Returns**:
- `None`

**Raises**:
- `TypeError`: If `file_path` is not a string.
- `IOError`: If there's an issue writing to the file.



#### `get_data`

**Description**: Retrieves the extracted data as a dictionary.

**Parameters**:
- None

**Returns**:
- `dict`: The extracted data as a dictionary.

#### `run`

**Description**: Orchestrates the entire web scraping process: setting up the crawler, running it, exporting the data, and printing the extracted data.

**Parameters**:
- `initial_urls` (list): The initial URLs to start the crawl.
- `file_path` (str): The path to the file for exporting the data.

**Returns**:
- `None`

**Raises**:
- `TypeError`: If `initial_urls` is not a list or `file_path` is not a string.


## Example Usage

```python
# Example usage (replace with your actual values)
import asyncio

async def main():
    crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
    await crawler.run(initial_urls=['https://news.ycombinator.com/'], file_path='data.json')

if __name__ == "__main__":
    asyncio.run(main())
```


This example demonstrates how to create a `CrawleePython` instance and use the `run` method to start the crawler. Remember to replace placeholders with your specific needs.