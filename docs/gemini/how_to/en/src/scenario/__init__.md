# Usage Guide for `hypotez/src/scenario/__init__.py`

This module provides functions for executing scenarios for various suppliers, primarily focusing on data ingestion and product mapping to a PrestaShop store.  The core idea is a decoupled system where scenarios define the target data, an executor handles the execution logic, and suppliers provide the data access.

## Functions

The module exposes several key functions:

* **`run_scenario_files(supplier, scenario_files)`:** Executes multiple scenario files.
    * **`supplier`:** An instance of a `Supplier` object.  This object is crucial; it handles the data retrieval from the specific supplier's system.
    * **`scenario_files`:** A list of file paths to JSON files containing scenario definitions. Each file should follow the example provided, defining scenarios with details like product URLs, names, and PrestaShop category mappings.

* **`run_scenarios(supplier, scenarios)`:** Executes multiple scenarios.
    * **`supplier`:** An instance of a `Supplier` object.
    * **`scenarios`:** A list or dictionary of scenario definitions.  A single scenario is a Python dictionary like the example in the docstring (e.g., `{"key": "value"}`).  A list of scenarios would be `[scenario1, scenario2, ...]`.

* **`run_scenario_file(supplier, scenario_file)`:** Executes a single scenario file.
    * **`supplier`:** The supplier object.
    * **`scenario_file`:** Path to the scenario JSON file.

* **`run_scenario(supplier, scenario)`:** Executes a single scenario.
    * **`supplier`:** The supplier object.
    * **`scenario`:** A single scenario dictionary.

* **`execute_PrestaShop_insert(data)`:**  (Potentially internal) Executes the PrestaShop product insertion.  `data` is assumed to be the product data formatted appropriately for insertion.

* **`execute_PrestaShop_insert_async(data)`:** (Potentially internal) Executes the PrestaShop product insertion asynchronously.  Useful for scaling and avoiding blocking the main thread.


## Scenario File Format (Example)

Scenario files are JSON documents.  Each file can contain multiple scenarios. The example in the docstring shows the structure:

```json
{
  "scenarios": {
    "feet-hand-treatment": {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
      "name": "Foot and Hand Care",
      "condition": "new",
      "presta_categories": {
        "default_category": 11259,
        "additional_categories": []
      }
    },
    // ... more scenarios ...
  }
}
```

Crucially, the `Supplier` object is responsible for interpreting and extracting the necessary data from the supplier's API or database, based on the URLs and other information in the scenario.

## `Supplier` Class Usage (Example from Docstring)

The `Supplier` class is likely a crucial component, handling the details of interacting with a specific supplier.  Note how scenarios are passed to its `run()` method:

```python
s = Supplier('aliexpress')

s.run()  # This is likely a call to handle general setup, possibly loading supplier-specific data

s.run('file1') # Execute a scenario file.
```

This code snippet demonstrates how to instantiate a `Supplier` object and then call its `run` method with scenario data to perform an action.

## `MODE` Constant

The `MODE = 'dev'` constant suggests different execution behaviors (e.g., debugging or production) are possible, but needs further documentation.

## Further Considerations

* **Error Handling:**  The code should include robust error handling to gracefully manage issues with file loading, API calls, and data processing. Detailed error messages are recommended.
* **Documentation for `Supplier`:** Include the documentation for the `Supplier` class and its methods. Explain how to create and use supplier objects.
* **Concurrency:** If you use asynchronous methods like `execute_PrestaShop_insert_async`, explain how to handle potential concurrency issues and ensure data consistency.
* **Data Validation:**  Add details about validation checks to ensure the incoming data conforms to expected formats and constraints.

This comprehensive guide provides a structured understanding of the module's functionality.  Additional details about the `Supplier` class, error handling, and other crucial aspects are necessary for complete usage instructions.