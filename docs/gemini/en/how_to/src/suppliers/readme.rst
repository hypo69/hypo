rst
How to use the Supplier class
========================================================================================

Description
-------------------------
This class acts as a base for interacting with various data sources (suppliers) like e-commerce websites (e.g., amazon.com, walmart.com). It handles initialization, configuration, authentication, and execution of workflows for these sources.  The class is designed to standardize interactions with different suppliers, offering a unified interface for retrieving data.

Execution steps
-------------------------
1. **Initialization:** Create a `Supplier` object. Provide the `supplier_prefix` (e.g., 'amazon'), optional `locale`, and `webdriver` type.
   ```python
   supplier = Supplier(supplier_prefix='amazon', locale='en', webdriver='chrome')
   ```
2. **Loading settings and initializing WebDriver:** Call the `_payload` method to load supplier-specific settings, locate web elements, and initialize the WebDriver.  This step is crucial for successful interactions.
   ```python
   supplier._payload(webdriver='firefox')
   ```
3. **Authentication (if required):**  Call the `login` method to authenticate with the supplier's website if authentication is needed.
   ```python
   supplier.login()
   ```
4. **Executing Scenarios (or files of scenarios):**
   - **Running scenario files:** Provide a list of scenario files (e.g., JSON) to execute.
     ```python
     supplier.run_scenario_files(['example_scenario.json'])
     ```
   - **Running specific scenarios:** Provide a dictionary or list of dictionaries defining the scenarios.
     ```python
     supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
     ```

Usage example
-------------------------
.. code-block:: python

    from suppliers import Supplier  # Assuming Supplier class is in the 'suppliers' module

    # Example usage for amazon, using Chrome webdriver.
    try:
        supplier = Supplier(supplier_prefix='amazon', locale='en', webdriver='chrome')
        supplier._payload(webdriver='chrome')
        if supplier.login():
            print("Successfully logged in.")
            supplier.run_scenario_files(['amazon_product_scrape.json'])
            print("Scenarios executed successfully.")
        else:
            print("Login failed.")

    except Exception as e:
        print(f"An error occurred: {e}")