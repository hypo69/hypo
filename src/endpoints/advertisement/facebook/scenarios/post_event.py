## \file /src/endpoints/advertisement/facebook/scenarios/post_event.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.advertisement.facebook.scenarios 
	:platform: Windows, Unix
	:synopsis: Публикация календарного события v группах фейсбук

"""


from socket import timeout
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
from urllib.parse import urlencode
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_event.json')
)

def post_title(d: Driver, title:str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """

    # Send title for event
    if not d.execute_locator(locator = locator.event_title, message = title):
        logger.error("Failed to send event title", exc_info=False)
        return
    return True

def post_date(d: Driver, date:str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """


    if not d.execute_locator(locator = locator.start_date, message = date):
        logger.error("Failed to send event date", exc_info=False)
        return
    return True

def post_time(d: Driver, time:str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...

    if not d.execute_locator(locator = locator.start_time, message = time):
        logger.error("Failed to send event time", exc_info=False)
        return
    return True

def post_description(d: Driver, description: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...
    # Send title for event
    d.scroll(1,300,'down')
    if not d.execute_locator(locator = locator.event_description, message = description):
        logger.error("Failed to send event description", exc_info=False)
        return
    return True


def post_event(d: Driver, event: SimpleNamespace) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, event.title): 
        return

    dt, tm = event.start.split()
    if not post_date(d, dt.strip()): 
        return
    if not post_time(d, tm.strip()): 
        return

    if not post_description(d, f"{event.description}\n{event.promotional_link}"): 
        return
    if not d.execute_locator(locator = locator.event_send): 
        return
    time.sleep(30)
    #input()
    return True


