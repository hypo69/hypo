rst
How to use the `languages.py` module
=========================================================================================

Description
-------------------------
This Python module defines a class `Language` containing constants representing various language codes.  It provides a convenient way to access and use these language codes within your application.  These codes are likely used for localization or to select appropriate language resources.

Execution steps
-------------------------
1. The module defines a class named `Language`.
2. Inside the `Language` class, several constants are defined, each representing a language code (e.g., `Language.EN` for English, `Language.RU` for Russian).
3. These constants are strings (e.g., 'EN', 'RU').
4. You can use these constants directly within your code to refer to specific languages.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.languages import Language

    # Example usage: selecting the language for an API request
    target_language = Language.ES

    # ... (rest of your code to use the target_language, e.g., setting headers for an API call) ...

    # Example showing a more complete usage, to show the use case
    headers = {
        'Accept-Language': target_language
    }

    # ... (rest of your code) ...