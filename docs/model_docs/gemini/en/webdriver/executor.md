```rst
webdriver Executor Module
==========================

.. module:: hypotez.src.webdriver.executor
    :platform: Windows, Unix
    :synopsis: Module for interacting with web elements using Selenium.

This module provides functionalities for locating and interacting with web elements using Selenium,
supporting various actions like clicks, sending messages, executing events, and retrieving attributes.
It handles errors robustly to enable continuous execution in case of unstable elements.  This module
is designed to be flexible with different locator types and configurations.


Functions
---------

.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.__init__
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.execute_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.evaluate_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_attribute_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_webelement_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_webelement_as_screenshot
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.execute_event
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.send_message


Classes
-------

.. autoclass:: hypotez.src.webdriver.executor.ExecuteLocator
    :members:
    :undoc-members:
    :show-inheritance:
```
