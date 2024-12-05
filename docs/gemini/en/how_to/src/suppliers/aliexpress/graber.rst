rst
How to use the `aliexpress/graber.py` code block
=========================================================================================

Description
-------------------------
This Python code defines a class `Graber` for extracting product information from AliExpress. It's a subclass of a generic `Graber` class, designed for handling AliExpress-specific product details.  The class contains asynchronous methods for fetching various product fields, including but not limited to names, descriptions, prices, and more.  It leverages Selenium WebDriver (`Driver`) for interacting with the web page.  It uses a `Context` object for potentially pre-processing web interactions.  Crucially, it offers a flexible way to handle different product attributes, enabling custom field extraction logic if needed.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports various Python modules for web scraping, data manipulation, and logging.  Crucially, it imports `Driver`, `ProductFields`, and other classes from the project's library.

2. **Define the `Graber` class:** This class inherits from the base `Graber` class, providing a framework for handling AliExpress product extraction.


3. **Initialize the `Graber` object:**  The `__init__` method initializes the `Graber` instance, setting the `supplier_prefix` and potentially overriding the `Context.locator_for_decorator` for custom logic. It also takes a `Driver` object as input, necessary for interacting with the web browser.

4. **Implement the `grab_page` method:** This method is the core of the extraction process. It utilizes a helper function `fetch_all_data`.

5. **Implement `fetch_all_data`:**  Inside `fetch_all_data`, individual methods for each product field are called.

6. **Fetch product fields:**  `fetch_all_data` calls several asynchronous methods (e.g., `id_product`, `name`, `specification`).  Each method fetches data for a particular field from the AliExpress webpage.  Methods like `self.id_product(kwards.get("id_product", ''))` retrieve data based on the input key-value pairs.

7. **Return extracted data:** The `grab_page` method returns a `ProductFields` object containing all the extracted product information.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.graber import Graber
    from src.webdriver.driver import Driver
    import asyncio
    import time

    # Replace with your actual driver instantiation logic
    async def run():
        driver = await Driver.create_driver(options=["options"])
        graber = Graber(driver)

        # Example usage:
        start_time = time.time()
        product_data = await graber.grab_page(driver, id_product="12345")
        end_time = time.time()

        if product_data:
            print(f"Product data fetched successfully in {end_time - start_time:.2f} seconds.")
            print("Product Name:", product_data.name)
            print("Product Description:", product_data.description)
            # Access other fields in a similar manner.
        else:
            print("Failed to fetch product data.")
        await driver.close()

    asyncio.run(run())