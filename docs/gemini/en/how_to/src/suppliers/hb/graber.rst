rst
How to use the Graber class for scraping product fields from hb.co.il
==================================================================================

Description
-------------------------
This Python code defines a `Graber` class, inheriting from a parent `Grbr` class, for extracting product data from the `hb.co.il` website.  It handles the process of collecting various product fields from the webpage, providing a framework for customized data retrieval. The code uses asynchronous operations (`async`/`await`) and a decorator (`@close_pop_up`) for handling pop-up windows that may appear on the website.  Crucially, it allows for overriding the default field extraction logic in subclasses, making it adaptable for different products or variations in the website's structure.  There's a significant amount of commented-out code, indicating a potential for fetching many different product attributes.


Execution steps
-------------------------
1. **Initialization:** The `Graber` class is initialized with a `Driver` instance. This establishes the connection to the browser and the website. Global settings, if needed, are set using `Context`.
2. **Page Grabbing:** The `grab_page` method asynchronously fetches the product data. It invokes a series of functions (e.g., `id_product`, `name`, `price`) to extract specific product fields.  The `fetch_all_data` function acts as a central dispatcher, calling these individual functions to get different data based on the passed keyword arguments.
3. **Field Extraction:** The individual field-handling methods, such as `id_product`, `name`, and others (which are partially commented out in the provided code), perform the actual data extraction from the web page using the `Driver`. These methods likely use `WebDriver` commands to locate and retrieve specific elements or data from the webpage.
4. **Data Collection:** The extracted data is collected into the `fields` attribute of the `Graber` object, an instance variable.
5. **Return Value:** The `grab_page` method returns the collected `ProductFields` object, containing the extracted data.

Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from hypotez.src.suppliers.hb.graber import Graber
    import asyncio


    async def main():
        # Replace with your actual driver initialization
        driver = await Driver.create() 
        graber = Graber(driver)

        # Example usage, assuming you have a valid product ID
        product_id = "12345"  # Replace with the actual product ID

        try:
            product_fields = await graber.grab_page(driver, id_product=product_id)
            # Now process the product_fields object.
            print(f"Product Name: {product_fields.name}")
            print(f"Product Price: {product_fields.price}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
          await driver.close()


    asyncio.run(main())