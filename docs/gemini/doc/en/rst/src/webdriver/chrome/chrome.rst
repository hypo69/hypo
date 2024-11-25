Chrome WebDriver
=================

.. module:: hypotez.src.webdriver.chrome.chrome
    :platform: Windows, Unix
    :synopsis: Chrome WebDriver implementation.

This module provides a custom implementation of Selenium's Chrome WebDriver. It integrates
settings defined in the `chrome.json` configuration file, such as user-agent and browser
profile settings, to allow for flexible and automated browser interactions.

Key Features:
    - Centralized configuration through JSON files.
    - Support for multiple browser profiles.
    - Enhanced logging and exception handling.


.. automodule:: hypotez.src.webdriver.chrome.chrome
    :members:
    :undoc-members:
    :show-inheritance:

Classes
-------

.. autoclass:: Chrome
    :members:
    :undoc-members:
    :show-inheritance:
    
    
    .. automethod:: Chrome.__new__
        :noindex:
    
    .. automethod:: Chrome.__init__
        :noindex:
        :show-inheritance:


Functions
---------

.. autofunction:: Chrome._payload
    :noindex: