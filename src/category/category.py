## \file /src/category/category.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Module for working with categories, primarily for PrestaShop.
============================================================

This module provides classes for interacting with and
processing product category data, particularly relevant for PrestaShop.

```rst
.. module:: src.category 
	:platform: Windows, Unix
	:synopsis: Module for working with categories, primarily for PrestaShop.
```
"""

import asyncio
from pathlib import Path
import os
from typing import Dict
from lxml import html
import requests

import header
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop import PrestaShop, PrestaCategory


class Category(PrestaCategory):
    """Category handler for product categories. Inherits from PrestaCategory."""
    credentials: Dict = None

    def __init__(self, api_credentials, *args, **kwargs):
        """Initializes a Category object.

        :param api_credentials: API credentials for accessing the category data.
        :param args: Variable length argument list (unused).
        :param kwargs: Keyword arguments (unused).
        """
        super().__init__(api_credentials, *args, **kwargs)

    def get_parents(self, id_category, dept):
        """Retrieves a list of parent categories.

        :param id_category: The ID of the category to retrieve parents for.
        :param dept: Depth level of the category.
        :returns: A list of parent categories.
        """
        return super().get_list_parent_categories(id_category)

    async def crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None):
        """Asynchronously crawls categories, building a hierarchical dictionary.

        :param url: The URL of the category page.
        :param depth: The depth of the crawling recursion.
        :param driver: The Selenium WebDriver instance.
        :param locator: The XPath locator for category links.
        :param dump_file: The path to the JSON file for saving results.
        :param default_category_id: The default category ID.
        :param category: (Optional) An existing category dictionary (default=None).
        :returns: The updated or new category dictionary.
        """

        if category is None:
            category = {
                'url': url,
                'name': '',
                'presta_categories': {
                    'default_category': id_category_default,
                    'additional_categories': []
                },
                'children': {}
            }

        if depth <= 0:
            return category

        try:
            driver.get(url)
            await asyncio.sleep(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Failed to locate category links on {url}")
                return category

            tasks = [
                self.crawl_categories_async(link_url, depth - 1, driver, locator, dump_file, id_category_default, new_category)
                for name, link_url in category_links
                if not self._is_duplicate_url(category, link_url)
                for new_category in [{'url': link_url, 'name': name, 'presta_categories': {'default_category': id_category_default, 'additional_categories': []}, 'children': {}}]
            ]
            await asyncio.gather(*tasks)

            return category
        except Exception as ex:
            logger.error(f"An error occurred during category crawling: ", ex)
            return category

    def crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={}):
        """
        Crawls categories recursively and builds a hierarchical dictionary.

        :param url: URL of the page to crawl.
        :param depth: Depth of recursion.
        :param driver: Selenium WebDriver instance.
        :param locator: XPath locator for finding category links.
        :param dump_file: File for saving the hierarchical dictionary.
        :param id_category_default: Default category ID.
        :param category: Category dictionary (default is empty).
        :return: Hierarchical dictionary of categories and their URLs.
        """
        if depth <= 0:
            return category

        try:
            driver.get(url)
            driver.wait(1)  # Wait for page load
            category_links = driver.execute_locator(locator)
            if not category_links:
                logger.error(f"Failed to locate category links on {url}")
                return category

            for name, link_url in category_links:
                if self._is_duplicate_url(category, link_url):
                    continue
                new_category = {
                    'url': link_url,
                    'name': name,
                    'presta_categories': {
                        'default_category': id_category_default,
                        'additional_categories': []
                    }
                }
                category[name] = new_category
                self.crawl_categories(link_url, depth - 1, driver, locator, dump_file, id_category_default, new_category)
            # Using j_loads and j_dumps for safe JSON handling
            loaded_data = j_loads(dump_file)
            category = {**loaded_data, **category}
            j_dumps(category, dump_file)
            return category
        except Exception as ex:
            logger.error(f"An error occurred during category crawling: ", ex)
            return category

    def _is_duplicate_url(self, category, url):
        """
        Checks if a URL already exists in the category dictionary.

        :param category: Category dictionary.
        :param url: URL to check.
        :return: True if the URL is a duplicate, False otherwise.
        """
        return url in (item['url'] for item in category.values())


def compare_and_print_missing_keys(current_dict, file_path):
    """
    Compares current dictionary with data in a file and prints missing keys.
    """
    try:
        data_from_file = j_loads(file_path)
    except Exception as ex:
        logger.error(f"Error loading data from file: ", ex)
        return  # Or raise the exception

    for key in data_from_file:
        if key not in current_dict:
            print(key)
