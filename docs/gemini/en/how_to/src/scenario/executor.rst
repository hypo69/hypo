rst
How to use the `hypotez/src/scenario/executor.py` module
========================================================================================

Description
-------------------------
This module provides functions for executing scenarios, loading them from files, extracting product information, and inserting it into PrestaShop. It handles scenario execution, error logging, and journal saving.  It utilizes various libraries like `requests`, `asyncio`, and `json` for communication and data processing. The core functions allow running individual scenario files, lists of scenario files, and directly running scenarios from a list of dictionaries. The module incorporates error handling to catch potential issues during file loading, scenario execution, and data insertion.  A central journal is used to record results of executed scenarios.


Execution steps
-------------------------
1. **Initialization**: The module imports necessary libraries like `os`, `sys`, `requests`, `asyncio`, etc.  It also imports custom modules like `gs`, `printer`, `jjson`, `Product`, `PrestaShop`, `ProductCampaignsManager`, `logger`, `ProductFieldException`. A global `_journal` dictionary is initialized to store execution results.


2. **`dump_journal` function**: This function saves the `_journal` data to a JSON file in a specified location.


3. **`run_scenario_files` function**:
    - Takes a supplier instance (`s`) and a list or single file path (`scenario_files_list`) as input.
    - If a single file path is provided, it's converted to a list.
    - The scenario files list is prioritized over the `s.scenario_files` attribute if no input is provided.
    - Iterates through each scenario file in the list.
    - Calls `run_scenario_file` to process each scenario.
    - Logs success or failure messages for each file using the `logger` module.
    - Includes error handling (`try...except`) to catch and log any exceptions during file processing.
    - Updates the `_journal` with success/failure information for each scenario file.

4. **`run_scenario_file` function**:
    - Takes a supplier instance (`s`) and a scenario file path (`scenario_file`) as input.
    - Loads the scenario data from the JSON file using `j_loads`.
    - Iterates through each scenario within the loaded data.
    - Calls `run_scenario` for each scenario, passing the supplier instance and scenario data.
    - Logs success or failure messages for each scenario using the `logger` module.
    - Includes error handling (`try...except`) to catch `FileNotFoundError` and `json.JSONDecodeError` during file loading or processing.


5. **`run_scenarios` function**:
    - Takes a supplier instance (`s`) and optional list or dictionary of scenarios as input (`scenarios`).
    - If no scenarios are provided, uses `s.current_scenario` as the default scenario.
    - Converts the input to a list if it's a single scenario.
    - Iterates through each scenario in the input list.
    - Calls `run_scenario` to execute each scenario.
    - Stores the result of each scenario execution in the `res` list.
    - Updates the `_journal` with the results.
    - Returns the `res` list, which holds the results of scenario executions.


6. **`run_scenario` function**:
    - Takes a supplier (`s`), scenario (`scenario`), and scenario name (`scenario_name`) as input.
    - Gets the driver and URL from the scenario.
    - Collects products in the category using `s.related_modules.get_list_products_in_category`.
    - Handles cases where no products are found.
    - Iterates through the products:
        - Navigates to each product page (`d.get_url`).
        - Grabs product page fields using `s.related_modules.grab_product_page` and `s.related_modules.grab_page`.
        - Creates a `Product` object from the collected data.
        - Calls `insert_grabbed_data` to insert the product data into PrestaShop.
        - Includes error handling (`try...except`) for potential errors during product processing.


7. **`insert_grabbed_data` function**: This function is responsible for inserting product data into PrestaShop using the `PrestaShop` class, handling asynchronous execution (`execute_PrestaShop_insert`).  It calls the function which handles the actual insertion.


8. **`execute_PrestaShop_insert` function**: Inserts the product data into PrestaShop using the `PrestaShop` API. It handles potential errors during insertion and logs appropriately.


Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.scenario import executor  # Import the module
    from hypotez.src import gs
    import header # Assuming you have this module


    # Create a Supplier instance (replace with your actual supplier object)
    supplier = Supplier(supplier_prefix="my_prefix", scenario_files=Path("./scenarios"))

    # Example usage (assuming scenario_files is a list of file paths)
    success = executor.run_scenario_files(supplier, supplier.scenario_files)

    if success:
        print("All scenario files processed successfully.")
    else:
        print("Errors occurred while processing one or more scenario files.")