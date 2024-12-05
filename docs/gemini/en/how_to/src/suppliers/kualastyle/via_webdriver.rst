rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `get_list_products_in_category` that retrieves a list of product URLs from a category page using a web driver.  It interacts with a web browser (presumably via Selenium) to locate and extract product links. The code utilizes a `Supplier` object (not fully defined in this snippet) for accessing the driver and locators, facilitating the dynamic web page interaction.  It also performs scrolling on the page to ensure all product links are visible.


Execution steps
-------------------------
1. The function `get_list_products_in_category` takes a `Supplier` object (`s`) as input, which is assumed to hold driver instance and locators (e.g., for web elements).
2. It retrieves the driver object (`d`) and a dictionary of locators (`l`) associated with a 'category' from the `s` object.
3. It scrolls the webpage down (forward) using `d.scroll(scroll_count=10, direction="forward")`.  This ensures that all product links are in the visible area of the page, which is crucial for accurate retrieval.
4. It employs `d.execute_locator` to locate the product links within the specified page elements (via the 'product_links' key in the locators dictionary). This step uses the locator dictionary `l` to find the product links.
5. The function returns a list of product URLs (`list_products_in_category`), or `None` if no links are found.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
    # ... (Assume you have initialized Supplier object named 'supplier')

    supplier = Supplier(...) # Replace with the actual initialization
    product_urls = get_list_products_in_category(supplier)
    if product_urls:
        for url in product_urls:
            print(url)
    else:
        print("No product links found.")