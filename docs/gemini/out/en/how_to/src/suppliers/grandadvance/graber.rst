rst
How to use the `graber.py` code block
========================================================================================

Description
-------------------------
This Python code defines a `Graber` class for extracting product data from the `grandadvance.co.il` website.  It leverages a `WebDriver` (likely Selenium) to interact with the site and utilizes a `ProductFields` object to structure the collected data. The `Graber` class is a subclass of a base `Graber` class and provides methods to handle specific data points (e.g., `id_product`, `name`). It also includes asynchronous (`async`) functions for efficient data retrieval. The code includes a decorator (`close_pop_up`) to handle pop-up windows, though its implementation is commented out.  The code dynamically calls various data-fetching methods based on the provided `kwards` (keyword arguments).  Crucially, it's structured to handle different product data fields in a consistent manner.


Execution steps
-------------------------
1. **Import necessary libraries:** The code imports various Python libraries like `asyncio`, `pathlib`, `dataclass`, `functools`, `pydantic`, and custom modules (`src.suppliers.graber`, `src.product.product_fields`, `src.webdriver.driver`, etc.) for web interaction, data handling, and logging.

2. **Define the `Graber` class:** This class inherits from a parent `Graber` class (`Grbr`), providing a structured way to fetch product data. The `__init__` method initializes the `supplier_prefix` and the `WebDriver` instance.

3. **Implement asynchronous `grab_page` function:**  This function is responsible for fetching product details. It utilizes the `Context.driver` to execute actions on the webpage (likely to locate and extract data) and calls a series of specific field-extraction methods (e.g., `id_product`, `name`). The critical step is calling `fetch_all_data(**kwards)`, which dynamically calls numerous methods to handle different product fields.  The `fetch_all_data` method is defined in the same class to manage the retrieval of data and handle errors gracefully.

4. **Define `fetch_all_data` method:**  This method is responsible for calling the various individual product field extraction functions such as `id_product()`, `name()`, etc, passing the relevant parameters, dynamically using keyword arguments provided by the caller.

5. **Implement individual field-extraction functions (e.g., `id_product`, `name`):**  These functions are expected to use the WebDriver to locate and extract specific product data fields. These methods are defined in the same class as `fetch_all_data()` and grab the necessary values, storing them within the `self.fields` object.

6. **Return `ProductFields` object:** The `grab_page` method returns the `ProductFields` object, containing all the retrieved product information.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.grandadvance.graber import Graber
    from src.webdriver.driver import Driver

    # Initialize the Driver (replace with your WebDriver initialization)
    driver = Driver()

    async def main():
        graber_instance = Graber(driver)
        id_product_to_fetch = "12345"  # Replace with the product ID
        try:
            product_data = await graber_instance.grab_page(driver, id_product=id_product_to_fetch)
            print(product_data)  # Access and print the fetched data
        except Exception as e:
            print(f"Error fetching product data: {e}")
        finally:
            await driver.close()

    if __name__ == "__main__":
        asyncio.run(main())