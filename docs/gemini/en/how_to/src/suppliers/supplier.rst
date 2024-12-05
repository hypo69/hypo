rst
How to use the Supplier class
=========================================================================================

Description
-------------------------
This code defines a `Supplier` class, which is a base class for different suppliers in a system.  It handles loading supplier configurations, executing scenarios, and interacting with a web driver.  Crucially, it's designed to be extended for specific suppliers, allowing for modular and reusable functionality across various providers.

Execution steps
-------------------------
1. **Initialization:** The `Supplier` class is initialized with various parameters, including `supplier_id`, `supplier_prefix`, `locale`, etc.  Crucially, it loads configuration data from a JSON file (`_payload` method).
2. **Configuration Loading:** The `_payload` method attempts to import a module associated with the `supplier_prefix` (e.g., `src.suppliers.amazon`). If the module doesn't exist, it logs an error and returns `False`. Next, it loads settings from the corresponding JSON file (e.g., `src/suppliers/amazon_settings.json`) using `j_loads_ns`.  This file is expected to contain parameters like `price_rule`, `locale`, `scenario_files`, and `locators`. Loaded data is validated and set as attributes of the `Supplier` object.  If the JSON file is not found or improperly formatted, an error is logged, and `False` is returned.
3. **Validation:** The `check_supplier_prefix` validator ensures the `supplier_prefix` isn't empty.  If it is, a `ValueError` is raised.
4. **Error Handling:** The `__init__` method includes error handling for cases where `_payload` returns `False`, raising a `DefaultSettingsException`. This robust design helps avoid runtime issues related to missing or invalid configurations.
5. **Login (optional):** The `login` method (likely) interacts with the related module to handle the login process on the specific supplier's website.
6. **Scenario Execution:** Methods `run_scenario_files` and `run_scenarios` are provided to execute predefined scenarios, which likely involve interacting with the website using the loaded `locators` data. The execution of scenarios are delegated to external functions (`run_scenario_files` and `run_scenarios`).

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.supplier import Supplier
    from hypotez.src import gs

    # Assume you have a supplier object `supplier` loaded...
    # Example - loading an Amazon supplier instance.
    supplier = Supplier(supplier_prefix='amazon')

    # Check if initialization succeeded
    if supplier._payload():
        #  Perform actions related to scenario execution or login
        if supplier.login():
            # ... your scenario execution code
            scenario_files = ['scenario1.py', 'scenario2.py']
            supplier.run_scenario_files(scenario_files)
            print("Scenarios executed successfully!")

        else:
            print("Login failed.")
    else:
        print("Failed to load supplier configuration.")