rst
How to use the hypotez/src/scenario/_examples/_example_executor.py code block
==================================================================================

Description
-------------------------
This Python script provides examples for using the `executor` module functions from the `src.scenario.executor` module. It demonstrates how to run scenarios, manage scenario files, interact with the PrestaShop API, and handle various execution aspects.  The script includes functions to run lists of scenario files, single files, individual scenarios, and specific PrestaShop API operations (like adding coupons and inserting product data).  Examples utilize mock classes for testing and demonstration purposes.


Execution steps
-------------------------
1. **Import necessary modules:** The script imports required modules like `asyncio`, `Path`, and functions from `src.scenario.executor`, `src.utils.jjson`, `src.product.product_fields`, `src.endpoints.PrestaShop`.  It also includes mock classes (`MockSupplier`, `MockRelatedModules`, `MockDriver`) which are used for testing and demonstrating the logic.

2. **Define Mock Classes:**  These mock classes mimic the behavior of real classes interacting with the PrestaShop API or handling scenario files. They provide placeholders for real implementations.

3. **Implement Example Functions:**  The script defines several functions to showcase usage of the executor functions:
    * `example_run_scenario_files`: Runs a list of scenario files.
    * `example_run_scenario_file`: Runs a single scenario file.
    * `example_run_scenario`: Runs a single scenario.
    * `example_insert_grabbed_data`: Inserts grabbed product data into PrestaShop.
    * `example_add_coupon`: Adds a coupon using PrestaShop API.
    * `example_execute_PrestaShop_insert_async`: Executes PrestaShop insert asynchronously.
    * `example_execute_PrestaShop_insert`: Executes PrestaShop insert synchronously.


4. **Example Function Logic (Details):** Each example function defines the specific scenario, creates a `Supplier` instance (with mock data), and calls corresponding functions from the `executor` module like `run_scenario_files`, `run_scenario_file`, `run_scenario`, `insert_grabbed_data`, `add_coupon`,  `execute_PrestaShop_insert` and  `execute_PrestaShop_insert_async`.  Important to note that these example functions use `MockSupplier` instead of a real implementation, and expect scenario files and data are appropriately structured. The example uses `ProductFields` objects to prepare data for PrestaShop integration, supplying necessary product details.

5. **Execute Examples:**  The `if __name__ == "__main__":` block calls each example function sequentially to demonstrate their usage.


Usage example
-------------------------
.. code-block:: python

    # Example of adding a coupon. Replace placeholders with actual values.
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    try:
        add_coupon(credentials, reference, coupon_code, start_date, end_date)
        print("Coupon added successfully.")
    except Exception as e:
        print(f"Error adding coupon: {e}")