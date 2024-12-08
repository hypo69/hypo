rst
How to use the `get_list_products_in_category` function
========================================================================================

Description
-------------------------
This Python function, `get_list_products_in_category`, retrieves a list of product URLs from a given category page on a supplier's website.  It utilizes a web driver (`s.driver`) to interact with the page and extracts product links using locators.  Crucially, it handles cases where no product links are found, logging warnings as appropriate.

Execution steps
-------------------------
1. **Initialization:** The function takes a `Supplier` object (`s`) as input.  This object likely contains the web driver (`s.driver`) and locators (`s.locators`) needed to interact with the webpage.  The locators are crucial for locating elements on the category page.

2. **Locator Access and Error Handling:**  The code retrieves the relevant locators for the category page (`s.locators['category']`). It checks if locators are present. If not, it logs an error message and returns `None`.  This error handling is important for robustness.

3. **Web Page Interaction:**
    - The function executes a script to close potentially intrusive banners.
    - The page is scrolled to ensure all product links are visible. This step is critical if product listings are loaded dynamically.
    - The code attempts to retrieve a list of product links (`list_products_in_category`) from the page using the previously obtained locators (`s.locators['product']['product_links']`).


4. **Result Handling:**
    - If no product links are found, a warning message is logged.  This prevents the script from crashing.
    - The code ensures the returned value `list_products_in_category` is a list. If a single string (representing a URL) is obtained, it's wrapped in a list to maintain consistency.


5. **Output:** The function returns the `list_products_in_category` containing the URLs of the products on the category page.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.bangood import scenario  # Assuming the file is named scenario.py
    from src.suppliers import Supplier  # Example class

    # Example Supplier object (replace with your actual implementation).
    supplier = Supplier(driver=your_driver_object, locators=your_locators)

    product_urls = scenario.get_list_products_in_category(supplier)

    if product_urls:
        for url in product_urls:
            print(f"Product URL: {url}")
    else:
        print("No product URLs found.")