## Usage Guide for hypotez/src/suppliers/graber.py

This guide describes how to use the `Graber` class for collecting product data from web pages.  It's a base class for all suppliers, allowing asynchronous data retrieval and handling of various product fields.

**Core Concepts**

* **`Graber` Class:** This is the central class for data collection.  Each supplier class should inherit from `Graber`.
* **`Context` Class:** Holds global settings, including the WebDriver instance (`driver`) and supplier prefix (`supplier_prefix`).  Critical for using the `close_pop_up` decorator and handling locators.
* **`close_pop_up` Decorator:** This decorator automatically attempts to close pop-up windows before executing the decorated method.  Crucial for reliable data collection, especially when dealing with pop-ups.
* **Field Retrieval (`name`, `price`, etc.):**  Methods like `name()`, `price()`, etc., are defined to fetch data for specific product fields. They use locators to identify elements on the page and `execute_locator` to extract the values.  Crucially, these methods are decorated with `@close_pop_up()`.
* **`ProductFields` Class:** Used to store collected product data in a structured way.
* **Locators (`locator`):**  `locators/product.json` file provides the locators (e.g., CSS selectors, XPath) needed for each field to find the relevant elements on the page.  The `j_loads_ns` function is used to load this file, creating a `SimpleNamespace` for easy access.
* **Error Handling:**  The `error()` method and error handling within each field retrieval method provide robust error management.

**How to Use**

1. **Create a Supplier Class:** Inherit from `Graber` and provide implementations for the required fields.

   ```python
   from hypotez.src.suppliers import Graber
   from hypotez.src import gs
   import json

   class MySupplier(Graber):
       def __init__(self, driver, supplier_prefix="my_supplier"):
           super().__init__(supplier_prefix, driver)
           # ... any custom initialization


       @Graber.close_pop_up()  # Use the Graber's decorator for cross-supplier reliability!
       async def name(self, value=None):
           # Replace with your specific logic for fetching the product name.
           #  Example using a specific locator from your 'locators/product.json'
           name = await self.driver.execute_locator(self.locator.product_name_locator)
           self.fields.name = name
           return True  # Indicate successful execution
   ```

2. **Load Locators:** Ensure you have a `locators/product.json` file for your supplier, defining locators for each field. This JSON should be structured like this (adjust paths to match your directory structure):

   ```json
   {
       "product_name_locator": "#product-name",
       "price_locator": "#product-price",
       // ... other locators
   }
   ```

3. **Instantiate `Graber`:**  Instantiate your supplier class, passing the `Driver` instance and the supplier's prefix.


4. **Set Context:** Pass the driver to the Graber using the following code.  This is fundamental for the `close_pop_up` decorator to work correctly

   ```python
   # Example instantiation - replace with your actual driver setup.
   driver = Driver(...)
   supplier = MySupplier(driver, "my_supplier")
   Context.driver = driver # Sets the global driver object
   Context.locator_for_decorator = supplier.locator # Sets the locator object for the decorator to use
   ```

5. **Collect Data:** Call the appropriate `grab_page()` method to gather all the necessary product data.

   ```python
   product_data = await supplier.grab_page()
   ```

**Important Considerations:**

* **Error Handling:** The provided `error` method and structured error handling within each retrieval method are crucial for robustness. Examine the detailed error logging (using `logger`) for precise troubleshooting.
* **Custom Logic:** The example `name` method provides a template.  You must replace the placeholder `self.fields.name = <Your implementation>` with your specific logic for extracting data based on your page structure.
* **`grab_page()`:** The `fetch_all_data()` function within `grab_page()` is a placeholder. You should replace `await self.fetch_specific_data(**kwargs)` with calls to your field-specific retrieval methods (e.g., `await self.name()`, `await self.price()`, etc.). The usage of `kwards.get("field_name", '')` demonstrates how you can pass parameters, if needed, to your `Graber` class' methods for specialized data collection.


This revised guide provides a more structured and understandable approach to using the `Graber` class, highlighting crucial elements for effective data collection with error handling and customization. Remember to replace the placeholder comments in the code with your actual implementation.