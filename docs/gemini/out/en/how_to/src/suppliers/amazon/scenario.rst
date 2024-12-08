rst
How to use the `get_list_products_in_category` function
==================================================================================

Description
-------------------------
This function retrieves a list of product URLs from a given category page on a website. It utilizes a web driver (`d`) and locators (`l`) to locate product links within the category page.  The function handles potential errors, logs warnings if no product links are found, and returns a list of URLs or `None` if there's an error or no links.

Execution steps
-------------------------
1. **Retrieve the web driver and locators:** The function takes a `Supplier` instance (`s`) as input. It accesses the web driver (`d`) and locators (`l`) associated with the category from the `Supplier` object.
2. **Error handling and logging:** It checks if the locators are present. If not, it logs an error and returns `None`.
3. **Scroll the page (if needed):**  The function calls `d.scroll()` potentially to load all the product links. (This step might not be essential depending on the website's structure.)
4. **Extract product links:**  The function uses `d.execute_locator(l['product_links'])` to retrieve the URLs of products from the category page.
5. **Handle different types of retrieved product links:** The function checks if the retrieved `list_products_in_category` is a string or a list. It converts a single string to a list if necessary.
6. **Logging and handling empty lists:** It logs the number of products found. If the list is empty, a warning is logged and `None` is returned.
7. **(Comment out) Database check:** The code includes commented-out code that would check if the product already exists in a database. This part is intended but is currently commented out.
8. **Return the list of product URLs:** The function returns the extracted list of product URLs.


Usage example
-------------------------
.. code-block:: python

    from src import Supplier  # Assuming Supplier class exists
    # ... (Your code to initialize Supplier object)...
    # Example, assuming s is a Supplier object
    supplier = Supplier(driver=your_driver, locators={'category': {'product_links':'YOUR_LOCATOR'}})

    list_of_product_urls = get_list_products_in_category(supplier)


    if list_of_product_urls:
        for url in list_of_product_urls:
            print(url)
    else:
        print("No product URLs found or an error occurred.")