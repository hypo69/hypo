Aliexpress Module
=================

.. module:: hypotez.src.suppliers.aliexpress.aliexpress
    :platform: Windows, Unix
    :synopsis: This module provides the `Aliexpress` class, which integrates functionality from `Supplier`, `AliRequests`, and `AliApi` for working with AliExpress.


Classes
-------

.. autoclass:: Aliexpress
    :members:
    :undoc-members:
    :show-inheritance:

    
    .. automethod:: Aliexpress.__init__
        :noindex:
        :show-inheritance:
        
        :param webdriver: Webdriver mode. Supported values are:
            - `False` (default): No webdriver.
            - `'chrome'`: Use the Chrome webdriver.
            - `'mozilla'`: Use the Mozilla webdriver.
            - `'edge'`: Use the Edge webdriver.
            - `'default'`: Use the system's default webdriver.
        :type webdriver: bool | str
        :param locale: The language and currency settings for the script.
        :type locale: str | dict
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.