## \file hypotez/consultant/gemini/suppliers/aliexpress/aliexpress.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.suppliers.aliexpress """
MODE = 'debug'
```python
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

from __init__ import gs  
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
    def __init__(self, 
                 webdriver: bool | str = False, 
                 locale: str | dict = {'EN':'USD'},
                 requests: bool = False,
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
        super().__init__(supplier_prefix = 'aliexpress', locale=locale, webdriver=webdriver, *args, **kwargs)
        
        # Critical: Initialize AliRequests only if requested.
        if requests:
            self.requests_session = Session()
            self.requests_session.headers.update({'User-Agent': UserAgent().random})
            self.requests_session.cookies = RequestsCookieJar()  # Important for cookie persistence
            self._requests_initialized = True
        else:
            self._requests_initialized = False


```

**Explanation of Changes and Improvements:**

1. **`requests` Parameter:** Added a `requests: bool = False` parameter to the `__init__` method. This allows the user to explicitly decide whether to initialize the `AliRequests` part of the class.  Crucially,  the `requests` part is now initialized *only if* the `requests=True` argument is passed.

2. **`_requests_initialized` Flag:** Introduced a class variable `_requests_initialized` to track if `AliRequests` has been initialized.  This is *critical* for proper functioning. The `AliRequests` section of the class needs to be initialized only once, and if you skip this, you'll likely have undefined behavior (maybe `AttributeError` if trying to call methods that depend on it).

3. **Correct Session Initialization:**  The `requests.sessions.Session()` is properly created and the `User-Agent` header is set.  More importantly, `RequestsCookieJar()` is used to create and manage cookies.  This is essential if you want to store cookies for persistent sessions.

4. **Missing `super()` Call:** The `super().__init__()` call was missing in the previous code, which meant that the `Supplier` initialization (and likely other parts of the inheritance chain) was not called.  This is now fixed.

**How to use it:**

```python
# Example using only the base functionality
aliexpress_instance = Aliexpress()

# Example using webdriver
aliexpress_instance_webdriver = Aliexpress('chrome')


# Example using requests
aliexpress_instance_requests = Aliexpress(requests=True)
```

This revised code is significantly more robust and addresses the potential issues in the previous version. Remember to correctly install necessary libraries: `requests`, `fake-useragent`, etc. Also, make sure the `__init__.py` in your package is present and properly imports needed modules.


This improvement addresses the potential for unintended behavior and provides more control over the instantiation process, which was the key problem in the initial code.  The `_requests_initialized` flag is vital to preventing errors and making the code more maintainable and predictable. Remember that initializing `AliRequests` *must* happen only once per instance.