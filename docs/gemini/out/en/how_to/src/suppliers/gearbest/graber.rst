rst
How to use the `graber.py` code block
=========================================================================================

Description
-------------------------
This Python code defines a class `Graber` for retrieving product data from the Gearbest website.  It inherits from a base `Graber` class and provides methods to extract various product fields. The class utilizes `webdriver` to interact with the web page and a `ProductFields` object to store the extracted data.  It uses asynchronous operations (`asyncio`) for efficiency. Notably, it includes a structure for fetching and processing data from the Gearbest product page.  The code also handles potential exceptions during web driver interaction.  It defines methods to fetch various data points from the product page.  Customizable data extraction is supported through individual methods for each field.

Execution steps
-------------------------
1. **Initialization:** The `Graber` class is instantiated with a `Driver` object. This `Driver` object is responsible for interacting with the web browser (likely Selenium WebDriver).


2. **Data Collection (asynchronous):** The `grab_page` method is called asynchronously. This method calls a series of functions to extract product information using the WebDriver.  Important fields are pulled using methods like `id_product`, `name`, `specification`, etc.  


3. **Data Storage:** Extracted data is stored within the `ProductFields` object. This object likely holds the retrieved data in a structured format (e.g., a dictionary or a dataclass).


4. **Return Value:** The `grab_page` method returns the `ProductFields` object containing the gathered product data. This object is then accessible to other parts of the application.


Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from hypotez.src.suppliers.gearbest.graber import Graber

    async def main():
        # Initialize the WebDriver
        driver = Driver()
        await driver.setup()
        
        # Create an instance of the Graber class
        graber = Graber(driver)
        
        # Dictionary to pass data to the grab page function.
        data_to_grab = {
            'id_product': '12345' # Replace with the actual product ID
        }
        
        # Call the grab_page method and get the ProductFields object.
        product_data = await graber.grab_page(driver, data_to_grab)

        # Access the data (replace with the actual field names)
        product_id = product_data.id_product
        product_name = product_data.name

        print(f"Product ID: {product_id}")
        print(f"Product Name: {product_name}")

        # Close the WebDriver
        await driver.close()


    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())