rst
How to use the Supplier class
========================================================================================

Description
-------------------------
The `Supplier` class is a base class for managing data suppliers in an application. It handles interactions with various data sources (e.g., Amazon, AliExpress, Walmart) and centralizes the management of supplier-specific configurations, logins, and data collection scenarios.  It provides methods for initializing, loading configurations, logging in, and executing defined data collection scenarios.

Execution steps
-------------------------
1. **Initialization:** Create an instance of the `Supplier` class, specifying the `supplier_prefix` (e.g., `aliexpress`), `locale`, and `webdriver` (e.g., `chrome`).

   ```python
   supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
   ```

2. **Load Supplier Configuration:** Use the `_payload` method to load the supplier's configurations, including settings, locators, and initialize the web driver.  This step is typically handled internally.

   ```python
   supplier._payload(webdriver='chrome') # Assuming 'chrome' is the appropriate driver
   ```

3. **Login (if required):** Call the `login` method if authentication is needed to access the supplier's website.

   ```python
   supplier.login()
   ```

4. **Execute Scenarios:**  The class provides two methods for executing scenarios:
   * **`run_scenario_files`:** Executes scenarios defined in specified files (e.g., JSON files).

     ```python
     supplier.run_scenario_files(['example_scenario.json'])
     ```

   * **`run_scenarios`:**  Executes scenarios defined by a list of dictionaries.  This allows for more dynamic scenario execution based on specific criteria.

     ```python
     supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
     ```


Usage example
-------------------------
.. code-block:: python

    from your_module import Supplier  # Replace your_module

    # Example usage, replace with actual values
    supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

    try:
        supplier._payload(webdriver='chrome')
        if supplier.login():
            supplier.run_scenario_files(['data_collection_scenario.json'])
            print("Data collection completed successfully.")
        else:
            print("Login failed.")
    except Exception as e:
        print(f"An error occurred: {e}")