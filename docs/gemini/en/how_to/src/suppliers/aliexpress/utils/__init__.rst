How to use this code block
=========================================================================================

Description
-------------------------
This Python code block imports functions from modules within the `aliexpress` supplier's utility directory.  It defines a global variable `MODE` with the value 'dev'.  Critically, it imports functions for extracting product IDs (`extract_prod_ids`), ensuring HTTPS protocol in URLs (`ensure_https`), and managing localized data (`locales`). This structure suggests a reusable set of functions for handling AliExpress-specific data processing.


Execution steps
-------------------------
1. **Global variable initialization:** The code sets the global variable `MODE` to the string 'dev'. This likely controls configuration options (e.g., for development versus production).


2. **Import statements:** The code imports functions from submodules:
    - `extract_prod_ids` likely extracts product identifiers from AliExpress data.
    - `ensure_https` modifies URLs to ensure they use the secure HTTPS protocol.
    - `locales` likely handles language-specific data or localization.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https, locales

    # Example usage of extract_prod_ids (replace with actual data)
    product_data =  {'product_list': [{"id":"123", "url":"https://example.com"}, {"id":"456", "url":"http://example.com"}]}
    product_ids = extract_prod_ids(product_data)
    print(product_ids)


    # Example usage of ensure_https (replace with actual URLs)
    url = "http://example.com/product"
    secure_url = ensure_https(url)
    print(secure_url)


    # Example usage of locales (replace with actual locale)
    locale_data = locales.get('en')  # Accessing English locale data
    if locale_data:
        print(locale_data['greeting'])
    else:
        print("Locale data not found.")


**Note:**  To use these functions effectively, you'll need to have the relevant data structures (like `product_data` in the example) prepared.  The provided example assumes the `extract_prod_ids` function expects a dictionary containing a `product_list` key.  Detailed descriptions of the `extract_prod_ids`, `ensure_https`, and `locales` functions themselves are unavailable; this guide is based on function names and their likely purpose.