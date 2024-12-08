rst
How to use the Graber class for Amazon product data extraction
==========================================================================================

Description
-------------------------
This Python code defines a `Graber` class, inheriting from a base `Graber` class, specifically designed for extracting product data from the Amazon website.  It handles the process of collecting various product fields from a given Amazon product page using a web driver.  The class utilizes asynchronous operations (`asyncio`) for efficiency and includes error handling for web driver interactions.  Crucially, the code allows for customization of data extraction logic via overridden methods.  This facilitates tailoring the extraction process to specific needs and field requirements.  The `close_pop_up` decorator (commented out but a potential part of the implementation) is used for handling pop-up windows that may appear during web interactions. The `grab_page` method aggregates the collection of all product fields, delegating the work to individual field-specific methods for each product attribute.

Execution steps
-------------------------
1. **Initialization:** An instance of the `Graber` class is created, passing a `Driver` object responsible for interacting with the web browser. This sets up the connection to the web driver and initializes the class's internal attributes, including `supplier_prefix` which is 'amazon' in this case.
2. **Setting up global context (if needed):** The `Graber` class instance can potentially configure global context elements, including the `locator_for_decorator`. This is used for future interactions within the web driver context, particularly for actions like closing pop-up windows.
3. **Asynchronous Data Extraction:** The `grab_page` method is called asynchronously.
4. **Field-specific data retrieval:** The core of data extraction involves calling various methods within the `Graber` class, each corresponding to a specific product field.  These methods (`id_product`, `description_short`, `name`, etc.) are responsible for extracting the data for that specific field. The `fetch_all_data` function orchestrates calling all of the field-specific collection functions. These methods use the `kwards` to dynamically call each respective field-specific function, passing in the relevant arguments if needed. Each method extracts data from the web page, and the returned values are stored within the class's `fields` attribute.
5. **Data Aggregation:**  All the extracted data is consolidated and stored within the class's `fields` attribute.
6. **Return the product fields object:** The method returns the `ProductFields` object containing the collected product information.

Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from hypotez.src.suppliers.amazon.graber import Graber

    async def example_usage():
        # Replace with your actual driver initialization
        driver = Driver()
        await driver.start()

        graber = Graber(driver)

        # Example usage – replace with the actual data
        product_fields = await graber.grab_page(driver=driver, id_product='12345')

        # Access the extracted product fields
        print(product_fields)


        await driver.quit()


    if __name__ == "__main__":
        import asyncio
        asyncio.run(example_usage())