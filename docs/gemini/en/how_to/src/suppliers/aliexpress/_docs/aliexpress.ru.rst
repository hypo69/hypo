rst
How to use the Aliexpress module
========================================================================================

Description
-------------------------
The `aliexpress` module provides the `Aliexpress` class, which integrates functionality from the `Supplier`, `AliRequests`, and `AliApi` classes to interact with the AliExpress platform. It's designed for tasks related to parsing and API interaction with AliExpress.

Execution steps
-------------------------
1. **Import the module:**  Import the `Aliexpress` class from the `src.suppliers.aliexpress` module.  (Explicit import statements are not shown, but they would be needed to use the `Aliexpress` class in your code.)

2. **Instantiate the `Aliexpress` class:**  Create an instance of the `Aliexpress` class.  The `__init__` method takes optional parameters to configure the interaction:
   - `webdriver`: Controls whether a web driver is used for browser automation.  Possible values:
     - `False` (default): No web driver.
     - `'chrome'`, `'mozilla'`, `'edge'`, or `'default'`: Specify the web driver to use.
   - `locale`: Defines language and currency settings. Defaults to `{'EN': 'USD'}`.
   - `*args`, `**kwargs`: Pass additional positional and keyword arguments to the underlying components (`Supplier`, `AliRequests`, `AliApi`).

3. **(Optional) Configure the webdriver:**  If `webdriver` is set to a string ('chrome', 'mozilla', etc.) or 'default', appropriate drivers need to be installed and configured. If `webdriver` is `False`, no browser interaction will occur.

4. **(Optional) Configure the locale:** If a `locale` parameter is provided (either a string or a dictionary), it will be used to specify the language and currency for the API requests. Otherwise, the default settings are used (`{'EN': 'USD'}`).


5. **Initialize internal components:** The `__init__` method will create instances of `Supplier`, `AliRequests`, and `AliApi`.  These internal components handle communication with AliExpress.

6. **(Optional) Pass additional arguments:** If you have additional arguments (`*args`, `**kwargs`), these will be passed to the underlying components.

Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress import Aliexpress

    # Initialize Aliexpress without a web driver
    aliexpress_instance = Aliexpress()

    # Initialize Aliexpress with Chrome webdriver
    aliexpress_instance_chrome = Aliexpress('chrome')
    
    # Initialize Aliexpress with custom locale
    aliexpress_instance_custom_locale = Aliexpress(locale={'FR': 'EUR'})