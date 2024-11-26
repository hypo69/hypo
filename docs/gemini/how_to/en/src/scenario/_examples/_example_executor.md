# Usage Guide for `hypotez/src/scenario/_examples/_example_executor.py`

This guide explains how to use the example functions in the `hypotez/src/scenario/_examples/_example_executor.py` file, demonstrating interactions with the `executor` module and PrestaShop API.  Crucially, it highlights how to work with the `MockSupplier`, `MockRelatedModules`, and `MockDriver` classes used for testing and demonstration.

## Introduction

This file provides examples for running scenarios, handling scenario files, and interacting with the PrestaShop API, using functions within the `src.scenario.executor` module.  The examples are designed to be understandable and adaptable for practical use.  Remember to replace placeholder values like API keys and file paths with your actual data.


##  Key Concepts and Classes

* **`MockSupplier`:** This class simulates a supplier of scenario data.  It's crucial for testing and demonstration, holding the scenario files, their paths, and simulated settings.  It's a **mock** object; you will likely replace this with an actual data source for production code.
* **`MockRelatedModules`:** This class simulates other modules needed for scenario execution, notably `get_list_products_in_category` for fetching product lists and `grab_product_page` for product detail scraping.  Replace this with your actual modules in your application.
* **`MockDriver`:** Provides mock functionality for web driver interactions. This is vital for testing in cases where the actual driver is not needed for scenario setup and execution.

## Example Usage

This file showcases various methods for executing scenarios.

### 1. Running a List of Scenario Files (`example_run_scenario_files`)

```python
scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
result = run_scenario_files(supplier, scenario_files)
```
This method executes all scenario files provided in the `scenario_files` list.  Check the `result` to see if all files processed successfully.  The `supplier` instance holds essential information about the scenario files.

### 2. Running a Single Scenario File (`example_run_scenario_file`)

```python
scenario_file = Path('scenarios/scenario1.json')
result = run_scenario_file(supplier, scenario_file)
```

Execute a single JSON scenario file. This is particularly useful for testing specific scenarios in isolation.


### 3. Running a Single Scenario (`example_run_scenario`)

```python
scenario = {
    'url': 'http://example.com/category',
    'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
}
result = run_scenario(supplier, scenario)
```
Runs a single, pre-defined scenario.  This is effective when the scenario structure is known beforehand.

### 4. Inserting Grabbed Product Data into PrestaShop (`example_insert_grabbed_data`)

```python
product_fields = ProductFields(...)  # ... Populate with the product data.
insert_grabbed_data(product_fields)
```
Demonstrates inserting data from scraped product pages into the PrestaShop database.

### 5. Adding a Coupon (`example_add_coupon`)

```python
credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
add_coupon(credentials, reference, coupon_code, start_date, end_date)
```
This example shows how to add a coupon using the PrestaShop API.  **Crucially**, replace `YOUR_API_KEY` with your actual API key.

### 6. Asynchronous PrestaShop Insert (`example_execute_PrestaShop_insert_async`)

```python
await execute_PrestaShop_insert_async(product_fields)
```
For asynchronous interactions with the PrestaShop API, use `execute_PrestaShop_insert_async`.

### 7. Synchronous PrestaShop Insert (`example_execute_PrestaShop_insert`)

```python
result = execute_PrestaShop_insert(product_fields)
```
Use this for synchronous operations with the PrestaShop API.


## Important Considerations

* **Error Handling:** The examples include basic success/failure checks (`if result:`).  Robust applications should include comprehensive error handling to gracefully manage failures during scenario execution and API calls.
* **Data Validation:**  Validate the data returned from the API and from the scenario files to prevent unexpected behavior.
* **`ProductFields`:**  Ensure the `ProductFields` object correctly reflects your data structure for accurate insertion.
* **API Keys:** Replace placeholders like `YOUR_API_KEY` with your actual API keys in the code.
* **File Paths:** Verify file paths (`scenarios/scenario1.json`) and adjust as necessary for your project structure.

This guide provides a starting point.  Adapt and expand these examples to meet your specific needs.  Remember to replace mock classes with your actual implementation, and implement thorough error handling and data validation.