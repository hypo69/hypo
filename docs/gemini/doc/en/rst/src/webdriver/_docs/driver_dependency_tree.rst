Driver Module
============

This module provides a base class for web driver interactions.  It handles common tasks such as navigation, element interactions, and exception handling.  It relies on external libraries like Selenium and provides helper methods for common web tasks.

.. automodule:: hypotez.src.webdriver.driver
    :members:
    :undoc-members:
    :show-inheritance:


DriverBase Class
---------------

.. autoclass:: hypotez.src.webdriver.driver.DriverBase
    :members:
    :undoc-members:
    :show-inheritance:

    Methods
    ~~~~~~~

    .. automethod:: hypotez.src.webdriver.driver.DriverBase.driver_payload
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.scroll
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.locale
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.get_url
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.extract_domain
    .. automethod:: hypotez.src.webdriver.driver.DriverBase._save_cookies_localy
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.page_refresh
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.window_focus
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.wait
    .. automethod:: hypotez.src.webdriver.driver.DriverBase.delete_driver_logs



DriverMeta Class
---------------

.. autoclass:: hypotez.src.webdriver.driver.DriverMeta
    :members:
    :undoc-members:
    :show-inheritance:

    Methods
    ~~~~~~~

    .. automethod:: hypotez.src.webdriver.driver.DriverMeta.__call__


Driver Class
------------

.. autoclass:: hypotez.src.webdriver.driver.Driver
    :members:
    :undoc-members:
    :show-inheritance:

Usage Example
~~~~~~~~~~~~~

.. code-block:: python

    from hypotez.src.webdriver import Driver, Chrome, Firefox, Edge
    d = Driver(Chrome)