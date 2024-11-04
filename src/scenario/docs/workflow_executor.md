
### Workflow for Script Executor Module

1. **Initialization**:
   - **Supplier Instance Creation**: Instantiate the `Supplier` class with the appropriate argument (e.g., 'aliexpress').

2. **Running Scenarios**:
   - **Single File Execution**:
     ```python
     s = Supplier('aliexpress')
     s.run('file1')
     ```
   - **Multiple Files Execution**:
     ```python
     scenario_files = ['file1', 'file2']
     s.run(scenario_files)
     ```
   - **Single Scenario Execution**:
     ```python
     scenario1 = {'key': 'value'}
     s.run(scenario1)
     ```
   - **Multiple Scenarios Execution**:
     ```python
     list_of_scenarios = [scenario1, scenario2]
     s.run(list_of_scenarios)
     ```

3. **Execution Flow**:

   **1. `run_scenario_files(s, scenario_files_list)`**:
   - **Purpose**: Executes a list of scenario files.
   - **Steps**:
     - Converts `scenario_files_list` to a list if it’s a single file path.
     - Iterates over each file, calls `run_scenario_file(s, scenario_file)`.
     - Logs the success or failure of each scenario file execution.
     - Updates the journal with execution results.

   **2. `run_scenario_file(s, scenario_file)`**:
   - **Purpose**: Loads and executes scenarios from a single file.
   - **Steps**:
     - Loads scenarios from the file.
     - Calls `run_scenario(s, scenario, scenario_name)` for each scenario in the file.
     - Updates the journal and logs the results of scenario execution.

   **3. `run_scenarios(s, scenarios)`**:
   - **Purpose**: Executes a list or single scenario directly (not from files).
   - **Steps**:
     - If no scenarios are provided, defaults to the current scenario in the supplier instance.
     - Calls `run_scenario(s, scenario)` for each scenario.
     - Updates the journal and logs the results.

   **4. `run_scenario(supplier, scenario, scenario_name)`**:
   - **Purpose**: Executes a given scenario.
   - **Steps**:
     - Retrieves the URL from the scenario and fetches the category page.
     - Retrieves product links from the category.
     - For each product link:
       - Fetches the product page and extracts fields.
       - Creates a `Product` instance and attempts to insert the data into PrestaShop.
     - Logs and handles errors as necessary.

   **5. `insert_grabbed_data(product_fields)`**:
   - **Purpose**: Inserts the product data into PrestaShop.
   - **Steps**:
     - Calls `execute_prestashop_insert` asynchronously.

   **6. `execute_prestashop_insert(f, coupon_code, start_date, end_date)`**:
   - **Purpose**: Inserts product data into PrestaShop.
   - **Steps**:
     - Uses the `Prestashop` class to post product data.
     - Handles errors and logs issues.

---

**Example of Scenario File**:
```json
{
  "scenarios": {
    "feet-hand-treatment": {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
      "name": "טיפוח כפות ידיים ורגליים",
      "condition": "new",
      "presta_categories": {
        "default_category": 11259,
        "additional_categories": []
      }
    },
    "creams-butters-serums-for-body": {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/creams-butters-serums-for-body/",
      "name": "קרמים, חמאות וסרומים לגוף",
      "condition": "new",
      "presta_categories": {
        "default_category": 11260,
        "additional_categories": []
      }
    }
  }
}
```

**Detailed Description of the Dictionary**:
- **`url`**: The target address (link to a category, section, or individual product).
- **`name`**: The category name, which matches the scenario name.
- **`presta_categories`**: 
  - **`default_category`**: The default category ID in PrestaShop.
  - **`additional_categories`**: Additional category IDs in PrestaShop.

**Execution Sequence in `main()`**:
```python
s = Supplier('aliexpress')
s.run()
s.run('file1')
scenario_files = ['file1', 'file2']
s.run(scenario_files)
scenario1 = {'key': 'value'}
s.run(scenario1)
list_of_scenarios = [scenario1, scenario2]
s.run(list_of_scenarios)
```

This workflow outlines how to use the `Script Executor` module to run scenarios and manage data collection and insertion into PrestaShop.