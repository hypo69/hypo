rst
How to use the executor module
========================================================================================

Description
-------------------------
This document provides a usage guide for the `executor` module, demonStarting how to execute scenarios, handle scenario files, interact with the PrestaShop API, and more. It includes examples for various operations, including running multiple scenario files, single scenario files, individual scenarios, and handling product data.

Execution steps
-------------------------
1. **Import necessary modules:**  Import the required modules, including `run_scenario_files`, `run_scenario_file`, `run_scenarios`, `run_scenario`, `insert_grabbed_data`, `execute_PrestaShop_insert`, `execute_PrestaShop_insert_async`, `add_coupon`, `ProductFields`, `PrestaShop`, and other relevant modules from the `src` directory.

2. **Define a `Supplier` (or similar) class:** Create a class (e.g., `MockSupplier`) that encapsulates the necessary data and methods related to scenario execution, including scenario file paths, PrestaShop API credentials, or any other relevant settings.  This example uses mock classes `MockSupplier`, `MockRelatedModules`, and `MockDriver` for demonStartion purposes.

3. **Define example functions:** Create functions (`example_run_scenario_files`, `example_run_scenario_file`, etc.) to demonStarte the usage of the `executor` module functions, typically by instantiating the `Supplier` class and providing necessary input.  Note the use of example data (e.g., scenario file paths, URLs, product data) to populate the required parameters for each function.

4. **Execute the functions:** Call the example functions to run the desired scenarios.  The examples demonStarte executing lists of scenario files, single scenario files, and individual scenarios, including inserting product data into PrestaShop (synchronously and asynchronously) and adding coupons.

5. **Handle results:** The example functions often return a boolean value (`True` for success, `False` for failure).  The code includes checks to determine whether the scenario execution was successful and print appropriate messages to the console.

Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from src.scenario.executor import run_scenario_files
    from src.utils.jjson import j_loads_ns
    # ... other necessary imports
    # ... MockSupplier class definition (as in the input code)

    def example_run_scenario_files():
        supplier = MockSupplier()
        scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
        result = run_scenario_files(supplier, scenario_files)
        if result:
            print("All scenarios executed successfully.")
        else:
            print("Some scenarios failed.")

    # Run the example function
    example_run_scenario_files()