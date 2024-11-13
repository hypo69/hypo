## \file hypotez/src/suppliers/aliexpress/aliexpress.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress """
""" Base class for the supplier. 
This class inherits from `Supplier`.
It allows interaction with AliExpress in three ways:
- webdriver
- requests
- API

Examples:
    @code
    # Run without a webdriver
    a = Aliexpress()
    
    # Webdriver `Chrome`
    a = Aliexpress('chrome')
    @endcode
"""



import pickle
import requests
import threading
from requests.sessions import Session
from fake_useragent import UserAgent
from pathlib import Path
from typing import Union
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse

from src import gs  
from src.suppliers.supplier import Supplier
from .alirequests import AliRequests
from .aliapi import AliApi
from src.logger import logger  

class Aliexpress(Supplier, AliRequests, AliApi):
    """ Base class for AliExpress. 
    This class inherits from `Supplier`, `AliRequests`, and `AliApi`.
    @code
    # Run without a webdriver
    a = Aliexpress()
    
    # Webdriver `Chrome`
    a = Aliexpress('chrome')
    
    # Requests
    a = Aliexpress(requests=True)
    @endcode
    """
    ...

    
    def __init__(self, 
                 webdriver: bool | str = False, 
                 locale: str | dict = {'EN':'USD'},
                 *args, **kwargs):
        """ Initialize the Aliexpress class

        @param locale - The language of the script
        @param webdriver - Webdriver mode (default False)
        Webdriver modes: False, 'chrome', 'mozilla', 'edge', 'default'
        @param requests `bool` - Connect the `AliRequests` class
        @code
            # Run without a webdriver
            a = Aliexpress()
    
            # Webdriver `Chrome`
            a = Aliexpress('chrome')
    
        @endcode
        """
        ...
        super().__init__(supplier_prefix = 'aliexpress', locale=locale, webdriver=webdriver, *args, **kwargs)

