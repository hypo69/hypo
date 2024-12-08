rst
How to use the `__morlevi__.py` code block
=========================================================================================

Description
-------------------------
This Python code defines functions for interacting with the Morlevi website, specifically for logging in and extracting product details.  It uses the `selenium` library for web automation and `requests` for potentially handling external APIs.  The code also utilizes custom classes and modules, like `Product`, `StringFormatter`, and `settings`, for data processing and handling. The core functionality revolves around:

1. **`login(supplier)`:**  Attempts to log into the Morlevi website, handling potential pop-ups and errors.
2. **`grab_product_page(s)`:** Extracts product data from a given product page. This includes information like SKU, title, price, description, and images.  Crucially, it handles potential price formatting issues and extracts data even if multiple elements are found for a single piece of data.
3. **`list_products_in_category_from_pagination(supplier)`:** Retrieves a list of product URLs within a specific category, handling pagination to collect all products.
4. **`get_list_products_in_category(s, scenario, presath)`:**  A higher-level function to gather products, likely calling `list_products_in_category_from_pagination`.
5. **`get_list_categories_from_site(s, scenario_file, brand='')`:**  A function to get a list of categories from the site (likely for a product search).


Execution steps
-------------------------
1. **Initialization:**  The code relies on pre-existing `supplier` objects and `locators` (likely defined in other files), which contain information about the website structure.  This object is expected to have a `driver` (a Selenium webdriver), and a `locators` dictionary.


2. **Login:** The `login` function attempts login using the provided locators. It handles scenarios where pop-up windows or errors occur during the login process, repeatedly trying login attempts and closing pop-ups until successful or maximum retries are reached.


3. **Product Data Extraction:** The `grab_product_page` function utilizes locators to extract various product attributes (title, price, description, images).  It also performs data cleanup and formatting (e.g., handling potential price formatting issues), crucial for consistent data quality.


4. **Pagination and Product List Generation:** The `list_products_in_category_from_pagination` function extracts URLs for all products on the current page, clicks through pages to get products on all pages and returns a list of URLs.


5. **Data Gathering:** The `get_list_products_in_category` function assembles the products and performs further processing on them.


6. **Category Listing (if applicable):** The `get_list_categories_from_site` function retrieves a list of categories from the Morlevi site, potentially based on a brand filter.


Usage example
-------------------------
.. code-block:: python

    # Assuming you have a 'supplier' object initialized, and locators are populated.
    from hypotez.src.suppliers.ivory import __morlevi__
    # ... (code to initialize supplier object and locators) ...
    supplier = ...

    # Attempt to login.
    success = __morlevi__.login(supplier)
    if success:
        # Grab product data.
        product = __morlevi__.grab_product_page(supplier)
        if product:
            print(product.fields['title'])  # Example of accessing product data.
            # Process product data as needed.
        else:
            print('Failed to retrieve product data.')

    else:
        print('Failed to login.')



    # Get product list
    product_list = __morlevi__.list_products_in_category_from_pagination(supplier)


    # Example of product list handling
    for product_url in product_list:
        # Do something with each product_url.
        print(product_url)