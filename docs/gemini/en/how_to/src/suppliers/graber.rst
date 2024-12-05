rst
How to use the Graber class for scraping product data
============================================================================================

Description
-------------------------
This Python code defines the `Graber` class, which is a base class for scraping product data from HTML pages of various suppliers.  It utilizes a web driver (`Driver` class) to extract data from specified fields on the page.  The locations of these fields are defined by locators stored in JSON files within a `locators` directory specific to each supplier.  The `close_pop_up` decorator is included to handle pop-up windows that might appear during the scraping process.  The class provides a series of methods (`name`, `price`, etc.) for fetching specific product data from the page.  Each method uses the web driver's `execute_locator` function to find the data based on predefined locators.

Execution steps
-------------------------
1. **Import the `Graber` class and necessary libraries:**
   ```python
   import asyncio
   from hypotez.src.suppliers import Graber
   from hypotez.src.webdriver.driver import Driver
   # ...other imports
   ```

2. **Initialize a `Driver` object:**
   ```python
   driver = Driver()  # Or use your specific Driver initialization
   ```

3. **Create an instance of the `Graber` class:**
   ```python
   supplier_prefix = "graber"  # Replace with the supplier prefix
   graber_instance = Graber(supplier_prefix, driver)
   ```

4. **Load locators:**
   This step assumes locators for your specific supplier are stored in a JSON file named `product.json` in the correct `locators` directory:
   ```python
   locators_path = gs.path.src / "suppliers" / supplier_prefix / "locators" / "product.json"
   graber_instance.locator = j_loads_ns(locators_path)
   ```

5. **Call the relevant methods for product data scraping:**
   ```python
   try:
       await graber_instance.grab_page(id_product="123") #Replace "123" with actual product ID
   except Exception as ex:
       print(f"Error: {ex}")
   ```
    This example calls the `grab_page` method and passing an `id_product` value.  The code will use the `execute_locator` function to get the product data from the specific page. The result will be filled into `graber_instance.fields`.

6. **Access the extracted product data:**
   ```python
   product_fields = graber_instance.fields
   print(product_fields.name)
   print(product_fields.price)
   # Access other fields similarly
   ```

Usage example
-------------------------
.. code-block:: python

    import asyncio
    from hypotez.src.suppliers import Graber
    from hypotez.src.webdriver.driver import Driver
    from hypotez.src import gs

    async def main():
        driver = Driver()
        supplier_prefix = "graber"
        graber = Graber(supplier_prefix, driver)
        # ...(Load locators, potentially handle exceptions as in the example)

        try:
            result = await graber.grab_page(id_product=123)
            pprint(result.fields) # Print the extracted product information.
        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            await driver.close()  # Always close the driver

    if __name__ == "__main__":
        asyncio.run(main())

```

**Important Notes:**

* **Error Handling:** The code includes `try...except` blocks to catch potential errors during the `execute_locator` calls.  Robust error handling is crucial for real-world scraping.
* **`grab_page`:** The `grab_page` method is a placeholder; you need to implement the `fetch_specific_data` function within it to retrieve the relevant data points for your needs.
* **`close_pop_up` Decorator:** The `@close_pop_up` decorator is essential for closing pop-up windows if encountered during the scrape.  You should set `Context.locator_for_decorator` appropriately within the `Graber` class to utilize the decorator for a given field.
* **`ProductFields`:** Ensure the `ProductFields` class is defined elsewhere and appropriately handles the data types of the scraped fields (e.g., strings, numbers).
* **Locators (`locator`):**  The `graber.locator` attribute, populated from the JSON file, holds the locators necessary for `execute_locator` calls.  This JSON file structure must be correct and match the HTML elements on the supplier's webpage.
* **`gs.path`:**  Ensure the `gs` module and the `gs.path` variable are properly defined to point to your project's resource directory.


This comprehensive RST example clarifies the usage of the code, outlining the necessary steps and considerations for integrating it into your project. Remember to replace placeholders like `"graber"` and `"123"` with the appropriate values for your specific scraping tasks. Remember to include error handling and proper initialization of the driver.