## \file /src/webdriver/bs/bs.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.bs 
    :platform: Windows, Unix
    :synopsis: Parse pages with `BeautifulSoup` and XPath

This module provides a custom implementation for parsing HTML content using BeautifulSoup and XPath.

Example usage:

.. code-block:: python

    if __name__ == "__main__":
        parser = BS()
        parser.get_url('https://example.com')
        locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
        elements = parser.execute_locator(locator)
        print(elements)
"""



import re
from pathlib import Path
from typing import Optional, Union, List
from types import SimpleNamespace
from bs4 import BeautifulSoup
from lxml import etree
import requests
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class BS:
    """
    Class for parsing HTML content using BeautifulSoup and XPath.

    Attributes:
        html_content (str): The HTML content to be parsed.
    """

    html_content: str = None

    def __init__(self, url: Optional[str] = None):
        """
        Initializes the BS parser with an optional URL.

        :param url: The URL or file path to fetch HTML content from.
        :type url: Optional[str]
        """
        if url:
            self.get_url(url)

    def get_url(self, url: str) -> bool:
        """
        Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath.

        :param url: The file path or URL to fetch HTML content from.
        :type url: str
        :return: True if the content was successfully fetched, False otherwise.
        :rtype: bool
        """
        if url.startswith('file://'):
            # Remove 'file://' prefix and clean up the path
            cleaned_url = url.replace(r'file:///', '')

            # Extract the Windows path if it's in the form of 'c:/...' or 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Exception while reading the file:', ex)
                        return False
                else:
                    logger.error('Local file not found:', file_path)
                    return False
            else:
                logger.error('Invalid file path:', cleaned_url)
                return False
        elif url.startswith('https://'):
            # Handle web URLs
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check for HTTP request errors
                self.html_content = response.text
                return True
            except requests.RequestException as ex:
                logger.error(f"Error fetching {url}:", ex)
                return False
        else:
            logger.error('Invalid URL or file path:', url)
            return False

    def execute_locator(self, locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]:
        """
        Execute an XPath locator on the HTML content.

        :param locator: The locator object containing the selector and attribute.
        :type locator: Union[SimpleNamespace, dict]
        :param url: Optional URL or file path to fetch HTML content from.
        :type url: Optional[str]
        :return: A list of elements matching the locator.
        :rtype: List[etree._Element]
        """
        if url:
            self.get_url(url)

        if not self.html_content:
            logger.error('No HTML content available for parsing.')
            return []

        soup = BeautifulSoup(self.html_content, 'lxml')
        tree = etree.HTML(str(soup))  # Convert BeautifulSoup object to lxml tree

        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        attribute = locator.attribute
        by = locator.by.upper()
        selector = locator.selector
        elements = None

        if by == 'ID':
            elements = tree.xpath(f'//*[@id="{attribute}"]')
        elif by == 'CSS':
            elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
        elif by == 'TEXT':
            elements = tree.xpath(f'//input[@type="{attribute}"]')
        else:
            elements = tree.xpath(selector)

        return elements


if __name__ == "__main__":
    parser = BS()
    parser.get_url('https://example.com')
    locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
    elements = parser.execute_locator(locator)
    print(elements)