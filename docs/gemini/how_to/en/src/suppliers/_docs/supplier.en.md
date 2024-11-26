# Usage Guide for the `Supplier` Class

This guide explains how to use the `Supplier` class for managing data suppliers in your application.  It details the class's attributes, methods, and how to utilize them to collect data from various sources like Amazon, AliExpress, and Walmart.


## Class Overview

The `Supplier` class is a base class designed to abstract away the complexities of interacting with different data suppliers.  It handles initialization, configuration, login, and scenario execution, promoting code reusability and maintainability.


## Class Attributes

The `Supplier` class possesses several attributes to store relevant information:

* **`supplier_id`:** A unique identifier for the supplier.
* **`supplier_prefix`:** A string prefix (e.g., `aliexpress`, `amazon`) to identify the supplier.
* **`supplier_settings`:** A dictionary containing supplier-specific settings loaded from a configuration file.
* **`locale`:** The locale for the supplier (e.g., `en`, `ru`).
* **`price_rule`:** A function or rule for calculating prices (e.g., adding VAT).
* **`related_modules`:** Modules containing supplier-specific functions (e.g., data parsing).
* **`scenario_files`:** A list of scenario files to be executed.
* **`current_scenario`:** The currently executing scenario.
* **`login_data`:** Credentials for logging in to the supplier's website.
* **`locators`:** Locators for web elements on the supplier's site.
* **`driver`:** The web driver instance used for interacting with the supplier's site.  Crucially, note that the driver is _managed internally_.
* **`parsing_method`:** The method used for data parsing (e.g., `webdriver`, `api`, `xls`, `csv`).


## Methods

The `Supplier` class provides several methods for managing different aspects of supplier interaction:

* **`__init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs)`:** The constructor initializes the `supplier_prefix`, `locale`, and `webdriver`.  The `webdriver` argument can be a string indicating the desired driver (e.g., 'chrome'), a `Driver` object, or `bool` (False to indicate no browser).  Use `*attrs, **kwargs` to pass additional attributes during instantiation.

* **`_payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool`:** This method performs crucial setup tasks: Loads supplier-specific configurations (from files, for instance), locators, and initializes the web driver.  Returns `True` if successful.  It's internal but essential for the class to function correctly.

* **`login(self) -> bool`:** Handles the login process to the supplier's website, if required.  Returns `True` if login is successful, `False` otherwise.

* **`run_scenario_files(self, scenario_files: str | List[str] = None) -> bool`:** Executes one or more scenario files.  Each file should contain instructions for data collection. Returns `True` if all scenarios execute successfully; otherwise, returns `False`.

* **`run_scenarios(self, scenarios: dict | list[dict]) -> bool`:** Executes specific scenarios based on the input `scenarios` data.  Input should be either a single dictionary or a list of dictionaries.  Each dictionary represents a scenario and its parameters.  Returns `True` if all scenarios run successfully; otherwise, returns `False`.


## Usage Examples

```python
# Create a Supplier object for AliExpress, using Chrome as the driver
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Load configurations and initialize the driver
if supplier._payload():
    # Attempt login
    if supplier.login():
        # Execute scenario files
        if supplier.run_scenario_files(['scenario1.json', 'scenario2.json']):
            print("Data collection successful.")
        else:
            print("Error executing scenario files.")
    else:
        print("Login failed.")
else:
	print("Configuration failed.")

```

## Important Considerations

* **Error Handling:** The code should include robust error handling to catch exceptions during login, scenario execution, and data parsing.
* **Scenario Files:** Define the structure of your scenario files (e.g., JSON or YAML) to ensure the `Supplier` class can interpret them correctly.  Consider adding validation to ensure data integrity within those files.
* **Configuration Files:** Detail how supplier-specific configurations are structured and stored (e.g., a separate configuration file for each supplier).
* **Driver Management:**  The example shows how to manage the webdriver internally. The `Supplier` class should handle the creation, configuration, and potential closing of the driver.

This comprehensive guide should enable you to effectively utilize the `Supplier` class to manage diverse data suppliers and scenarios. Remember to adapt these examples to your specific needs and error handling strategies.