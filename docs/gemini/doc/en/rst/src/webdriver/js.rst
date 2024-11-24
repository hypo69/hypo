hypotez/src/webdriver/js.py
==========================

.. module:: hypotez.src.webdriver.js
    :platform: Windows, Unix
    :synopsis: Provides JavaScript utility functions for interacting with a web page.

This module is designed to extend the capabilities of Selenium WebDriver by adding common JavaScript-based
functions for interacting with web pages, including visibility manipulations, retrieving page information,
and managing browser focus.

Key Features:
    1. Make invisible DOM elements visible for interaction.
    2. Retrieve metadata like document ready state, referrer, or page language.
    3. Manage browser window focus programmatically.


.. automodule:: hypotez.src.webdriver.js
    :members:
    :undoc-members:
    :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.webdriver.js.JavaScript.__init__
.. autofunction:: hypotez.src.webdriver.js.JavaScript.unhide_DOM_element
.. autofunction:: hypotez.src.webdriver.js.JavaScript.ready_state
.. autofunction:: hypotez.src.webdriver.js.JavaScript.window_focus
.. autofunction:: hypotez.src.webdriver.js.JavaScript.get_referrer
.. autofunction:: hypotez.src.webdriver.js.JavaScript.get_page_lang