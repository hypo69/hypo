rst
How to use the scenario execution functions
=========================================================================================

Description
-------------------------
This Python code defines functions for executing scenarios, likely within a system for managing supplier data and interactions, especially with an e-commerce platform like PrestaShop. The functions (`run_scenario_files`, `run_scenarios`, and their associated helper functions) allow processing scenario data, which may represent product listings, in a structured format to update or manage inventory on the PrestaShop store.

Execution steps
-------------------------
1. **Initialization:** A `Supplier` object is created, presumably representing a specific supplier (e.g., 'aliexpress'). This object likely handles interactions with the supplier's data and the target PrestaShop store.

2. **Scenario Execution with Files:** The `run_scenario_files` function takes the `Supplier` object and a file name (or a list of file names) as input. It processes the specified scenario files.  Each scenario file likely contains structured data defining actions (e.g., product listings, updates) to be performed.

3. **Scenario Execution with Dictionaries:** The `run_scenarios` function takes the `Supplier` object and a scenario dictionary (or a list of dictionaries).  The dictionaries presumably contain the specific actions to perform, such as adding a new product with details.  The key/value pairs within the dictionary likely correspond to fields to update in the PrestaShop store.

4. **PrestaShop Interactions:** The code utilizes functions for PrestaShop integrations (`execute_PrestaShop_insert`, `execute_PrestaShop_insert_async`).  This suggests interaction with the PrestaShop API or database to update product information on the store.


5. **Main Execution (Example):**  The code snippet demonstrates how to initiate the scenario execution from a main() method or similar entry point, where a `Supplier` object is instantiated and various `run` methods are invoked.



Usage example
-------------------------
.. code-block:: python

    from hypotez.src.scenario import run_scenario_files, Supplier

    # Instantiate a Supplier object
    supplier = Supplier('aliexpress')

    # Example using a list of scenario files
    scenario_files = ['file1.json', 'file2.json']
    run_scenario_files(supplier, scenario_files)


    # Example using a single scenario file
    scenario_file = 'file1.json'
    run_scenario_files(supplier, scenario_file)



    # Example using a scenario dictionary
    scenario_data = {
        'product_id': 123,
        'name': 'Example Product',
        'price': 19.99
    }
    #Assuming run_scenarios exists in the current namespace
    run_scenarios(supplier, scenario_data)


    # Example using a list of scenario dictionaries
    scenario_list = [
        {'product_id': 456, 'name': 'Another Product', 'price': 29.99},
        {'product_id': 789, 'name': 'Last Product', 'price': 10.99}
    ]
    run_scenarios(supplier, scenario_list)