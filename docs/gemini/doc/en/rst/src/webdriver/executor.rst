hypotez/src/webdriver/executor.py
====================================

.. module:: hypotez.src.webdriver.executor
   :platform: Windows, Unix
   :synopsis: This module provides functionalities for interacting with web elements using Selenium, handling locators, and executing actions.


Module Description
------------------

This module aims to automate web interactions by providing methods to parse locators, interact with web elements (e.g., click, send messages, execute events), and retrieve attributes.  It supports error handling to improve resilience against unstable web elements.  The module also offers support for various locator types, allowing for single or multiple element interactions.


Classes
-------

.. autoclass:: ExecuteLocator
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.execute_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.evaluate_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_attribute_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_webelement_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_webelement_as_screenshot
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.execute_event
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.send_message