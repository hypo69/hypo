rst
How to use the `get_list_products_in_category` function
=====================================================================================

Description
-------------------------
The `get_list_products_in_category` function retrieves a list of product URLs from a category page on a website.  It handles potential pagination by iterating through the pages and collecting all product links.  It also includes error handling for cases where no product links are found.

Execution steps
-------------------------
1. **Initialization:** The function takes a `Supplier` object (`s`) as input. This object likely contains data about the current supplier, including the webdriver session, locators for elements on the page, and the current scenario.

2. **Retrieving Locators:** The function accesses the `locators` dictionary associated with the `category` section within the `s.locators` structure to find the element identifying product links.

3. **Waiting for Page Load:** The webdriver waits for 1 second (using `d.wait(1)`). This allows the page to fully load before proceeding.

4. **Handling Banners/Pop-ups:**  The function executes a locator for a "close banner" element to handle any banner pop-ups that might be present on the page.

5. **Scrolling down:** The `d.scroll()` function helps handle long pages, ensuring the necessary product links are in view.

6. **Finding Product Links (initial):** The function uses the retrieved locators to find and extract the product URLs initially.  This is done via `d.execute_locator(l['product_links'])`.

7. **Handling Missing Product Links:** If no product links are found, a warning message is logged to the console. The function returns `None` to signal an error condition.

8. **Pagination:** The code enters a `while` loop to handle pagination of product links.
   - It calls `paginator(d, l, list_products_in_category)` to determine whether the current page is a page of product listings and not a pagination element.
   - If there's more pages, it appends the retrieved list of product links to the existing list and reloads the new page.
   - If there isn't more pages, it breaks out of the loop.


9. **Formatting Product List:** The returned `list_products_in_category` is adjusted if it's a single string instead of a list: `[list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category`.


10. **Logging:**  A debug log message is displayed indicating the number of products found in the specified category.


11. **Returning the Product List:** The function returns the `list_products_in_category` containing the URLs of all the found products.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.hb import category  # Assuming this is the correct path
    from src.suppliers import Supplier

    # ... (Initialize Supplier object: s, with driver and locators) ...

    list_of_products = category.get_list_products_in_category(s)

    if list_of_products:
        for product_url in list_of_products:
            # Process each product URL
            print(f"Found product: {product_url}")
            # ... further code to process the product
    else:
        print("No products found or error occurred")