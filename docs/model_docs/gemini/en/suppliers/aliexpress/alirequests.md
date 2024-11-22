```rst
aliexpress Requests Module
==========================

.. module:: hypotez.src.suppliers.aliexpress.alirequests
   :platform: Windows, Unix
   :synopsis: This module handles requests to AliExpress using the requests library.


Module Content
-------------

This module provides a `AliRequests` class for making requests to AliExpress, handling cookies, and session management.  It leverages the `requests` library, `fake_useragent`, and `pickle` to store and retrieve cookies for improved user experience. The module also manages session cookies for maintaining a consistent connection.


Classes
-------

.. autoclass:: hypotez.src.suppliers.aliexpress.alirequests.AliRequests
   :members:
   :undoc-members:
   :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.suppliers.aliexpress.alirequests._load_webdriver_cookies_file
   :noindex:


.. autofunction:: hypotez.src.suppliers.aliexpress.alirequests._refresh_session_cookies
   :noindex:


.. autofunction:: hypotez.src.suppliers.aliexpress.alirequests._handle_session_id
   :noindex:


.. autofunction:: hypotez.src.suppliers.aliexpress.alirequests.make_get_request
   :noindex:


.. autofunction:: hypotez.src.suppliers.aliexpress.alirequests.short_affiliate_link
   :noindex:
```