rst
How to use the graber.py code block
=========================================================================================

Description
-------------------------
This Python code defines a `Graber` class for extracting product data from the `ksp.co.il` website.  It extends a base `Graber` class and provides asynchronous methods for fetching various product attributes. The code includes a decorator (`close_pop_up`) for handling potential pop-up windows before data retrieval. It differentiates between desktop and mobile versions of the website.  The `grab_page` method is asynchronous and collects data from the page, invoking a series of dedicated functions (`id_product`, `name`, etc.) to extract specific fields.  The extracted data is stored in the `self.fields` object.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports various modules such as `asyncio`, `Path`, `SimpleNamespace`, `pydantic`, and others, providing the needed functionalities for asynchronous operations, file system interaction, data classes, and data validation.

2. **Define the `Graber` class:** This class inherits from the base `Grbr` class, responsible for gathering product information.

3. **Initialize the `Graber` object:** An instance of the `Graber` class is created, passing a `Driver` object as an argument.  This indicates that the `Graber` class requires a driver to interact with the website.

4. **Determine website type:** Checks if the current URL is related to a mobile version of the website.  If it is, the appropriate locator (specific to mobile) is loaded.

5. **Fetch data:**  The `grab_page` function is called to start the process of collecting product fields. The primary data extraction logic resides within an `async def fetch_all_data()` function.


6. **Extract individual fields:**  Within the `fetch_all_data` function, the code calls methods like `id_product`, `name`, `specification`, etc., to fetch specific product attributes.  The data returned by these functions is stored in the `self.fields` attribute.  The method takes optional `kwards` as an argument, to provide specific identifiers for the product if needed.

7. **Return the collected data:**  Finally, the `grab_page` function returns the collected data (`self.fields`) representing the product data in a structured format.

Usage example
-------------------------
.. code-block:: python

    import asyncio
    from src.suppliers.ksp.graber import Graber
    from src.webdriver.driver import Driver

    async def main():
        # Replace with your actual driver instantiation
        driver = Driver()
        await driver.start_driver()
        graber = Graber(driver)
        try:
            # Replace 'your_product_id' with the actual product ID.
            product_fields = await graber.grab_page(driver, id_product='your_product_id')
            print(product_fields.id_product)  # Accessing the product ID
            print(product_fields.name) # Accessing the product name
            print(product_fields.specification) # Accessing the product specification

        except Exception as e:
            print(f"Error: {e}")

        finally:
            await driver.quit_driver()


    if __name__ == "__main__":
        asyncio.run(main())