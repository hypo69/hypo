rst
How to use the Graber class for WallaShop product data extraction
=================================================================

Description
-------------------------
This Python code defines a `Graber` class, inheriting from a broader `Grbr` class, specifically designed for extracting product data from the WallaShop website (`wallashop.co.il`).  The `Graber` class provides functions to extract various product attributes, handling potential variations in data formats. It utilizes a web driver (likely Selenium) for interacting with the website.  A decorator (`close_pop_up`, though commented out) is available for handling pop-up windows before the main data extraction logic.  The code also includes placeholder functions for various product fields, allowing for customized data retrieval as needed.


Execution steps
-------------------------
1. **Initialization:** Create an instance of the `Graber` class, passing a `Driver` object to it.  This likely represents the web driver connection to the WallaShop site.

2. **Data Extraction:** Call the `grab_page` method, passing the `Driver` instance.  This method orchestrates the extraction of data for the product.

3. **Data Handling:** Within the `grab_page` function, a `fetch_all_data` function is defined to collect all the product fields. It calls individual functions (`id_product`, `name`, etc.) to fetch specific data points for each field, making the code organized and easier to expand.

4. **Product Field Extraction:**  Each individual product attribute is fetched using methods like `id_product`, `description`, `name`, etc., which are likely to handle the specific data extraction logic for that attribute on the WallaShop website.


Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from hypotez.src.suppliers.wallashop.graber import Graber

    # Assuming you have a Driver object initialized named 'my_driver'
    async def main():
        try:
            graber_instance = Graber(driver=my_driver)  
            product_fields = await graber_instance.grab_page(driver=my_driver)  #driver instance passed to the grab_page
            
            # Access the extracted product fields (e.g., product name)
            print(product_fields.name)
            print(product_fields.description)
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            #Close the driver when finished
            await my_driver.close()
            
    asyncio.run(main())