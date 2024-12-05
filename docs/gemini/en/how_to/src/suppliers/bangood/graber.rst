rst
How to use the `graber.py` code block
========================================================================================

Description
-------------------------
This Python code defines a class `Graber` that inherits from `Grbr` (likely a base class for web scraping).  It's designed to collect product data from the Banggood website.  The code utilizes asynchronous operations (`asyncio`) and interacts with a web driver (`Driver`) for fetching data.  The `grab_page` method is central, collecting data for various product attributes.  It calls multiple functions (`id_product`, `name`, etc.) to extract specific information.  Crucially, these functions can be overloaded in subclasses to customize data retrieval logic for different products or scenarios.

Execution steps
-------------------------
1. **Initialization:** The `Graber` class is instantiated, passing a `Driver` instance. This establishes the connection to the web browser and handles interactions with the Banggood website.
2. **Data Collection (grab_page):** The `grab_page` method is called, taking the initialized driver and optional keyword arguments (e.g., `id_product`) as input.
3. **Data Fetching (fetch_all_data):** This function contains the core logic for fetching product data. It iterates through various data-retrieving functions (e.g., `id_product`, `name`, `specification`).
4. **Attribute Extraction:** Each function (`id_product`, `name`, etc.) is responsible for extracting a specific field's value from the webpage. These functions are likely defined within the `Graber` class or other related classes.
5. **Data Aggregation:** The collected data is stored and potentially processed within the `Graber` class.
6. **Return Value:** The `grab_page` method returns a `ProductFields` object containing the extracted product data.

Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from hypotez.src.suppliers.bangood.graber import Graber
    import asyncio

    async def main():
        # Initialize the driver
        driver = Driver()
        await driver.start_driver()

        # Initialize the Graber class
        graber = Graber(driver)

        # Example usage, fetching data for product with ID 123
        try:
            product_fields = await graber.grab_page(driver=driver, id_product='123')
            # Accessing specific fields (example)
            product_name = product_fields.name
            print(f"Product name: {product_name}")
            # ...Access other fields as needed
        except Exception as e:
            print(f"Error: {e}")


        # Close the driver
        await driver.close_driver()

    asyncio.run(main())