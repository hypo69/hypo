rst
How to use the Aliexpress module
========================================================================================

Description
-------------------------
This module provides the `Aliexpress` class, which integrates the functionality of the `Supplier`, `AliRequests`, and `AliApi` classes to interact with the AliExpress API.  It's designed to simplify parsing and interacting with the AliExpress platform.  The `__init__` method of the `Aliexpress` class handles initialization, including setting up a WebDriver (if specified), locale, and internal components.

Execution steps
-------------------------
1. **Import the `Aliexpress` class**:  This is not explicitly shown in the snippet but should be done in the calling code.  The necessary imports would depend on the structure of the overall project.  For example: `from src.suppliers.aliexpress import Aliexpress`.

2. **Initialize the `Aliexpress` object**:  Call the `Aliexpress` constructor, providing optional parameters.
   - `webdriver`:  Specify the WebDriver to use (e.g., 'chrome', 'mozilla', 'edge', 'default').  Set to `False` for no WebDriver.
   - `locale`:  Specify language and currency (e.g., `{'EN': 'USD'}`). Defaults to `{'EN': 'USD'}` if not provided.
   - `*args` and `**kwargs`: Provide additional positional or keyword arguments to pass to internal components (`Supplier`, `AliRequests`, `AliApi`).

3. **Handle potential exceptions**: The `Aliexpress` constructor might raise exceptions related to WebDriver initialization or API interaction problems.  Proper error handling should be implemented in the calling code to catch and manage these exceptions.

4. **Use the initialized `Aliexpress` object**: After successful initialization, the `Aliexpress` object can be used to call the other methods of the class to interact with AliExpress (not demonstrated in this example).

Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress import Aliexpress

    # Initialize without a WebDriver
    aliexpress_instance = Aliexpress()

    # Initialize with Chrome WebDriver
    aliexpress_instance_chrome = Aliexpress('chrome')

    # Example using the locale parameter.  This assumes 'AliRequests' and 'AliApi' have been defined in the module.
    aliexpress_instance_locale = Aliexpress(locale={'FR': 'EUR'})