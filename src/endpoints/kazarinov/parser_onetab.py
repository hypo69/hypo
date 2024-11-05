## \file ./src/endpoints/kazarinov/parser_onetab.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import requests
from bs4 import BeautifulSoup
from typing import Optional, List
from types import SimpleNamespace
from lxml import etree
from pathlib import Path

import header
from src import gs
from src.utils.jjson import j_loads_ns
from src.utils import pprint
from src.logger import logger

def prepare_one_tab(target_page_url:str) -> tuple | bool:
    """ """
    return fetch_target_urls_onetab(target_page_url)



def fetch_target_urls_onetab(target_page_url: str) -> tuple[str, list] | bool:
    """Fetches target URLs from the specified OneTab URL.

    This function sends a GET request to the provided URL, parses the HTML content,
    and extracts all URLs from anchor tags with the class 'tabLink'.

    Args:
        url (str): The URL to fetch the target URLs from.

    Returns:
        Optional[List[str]]: A list of extracted URLs or `None` if the request fails.
    
    Raises:
        requests.exceptions.RequestException: If there's an error with the request.
    """
    ...
    try:
        response = requests.get(target_page_url, timeout=10)
        response.raise_for_status()  # Checks for HTTP errors
        if response.status_code != 200:
            logger.debug(f"Ошибка response\n{pprint(response)}")
            return False, False, False
        ...
        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")
        urls = [a['href'] for a in soup.find_all("a", class_="tabLink")]
        element = soup.find('div', class_='tabGroupLabel')
        data = element.get_text() if element else None
        if not data:
            return False, False, False
        parts = data.split(maxsplit=1)  # Разбиваем только на 2 части
        price = int(parts[0])
        mexiron_name = parts[1] if len(parts) > 1 else gs.now
        return price, mexiron_name, urls
    except requests.exceptions.RequestException as ex:
        logger.error(f"Failed to fetch the URL: ",ex)
        return False, False, False
