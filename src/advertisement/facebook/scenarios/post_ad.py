## \file ../src/advertisement/facebook/scenarios/post_event.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Публикация рекламного сообщения группах фейсбук"""
from socket import timeout
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
from urllib.parse import urlencode
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver import Driver
from src.advertisement.facebook.scenarios import post_title, upload_media
from src.utils import j_loads_ns, pprint
from src.logger import logger

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src, 'advertisement', 'facebook', 'locators', 'post_message.json')
)

def post_ad(d: Driver, message:SimpleNamespace) -> bool:
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


    if not post_title(d, message ):
        logger.error("Failed to send event title", exc_info=False)
        return
    if not d.execute_locator(locator = locator.foto_video_input, message = message.media_path , timeout = 20):
        return
    return True

