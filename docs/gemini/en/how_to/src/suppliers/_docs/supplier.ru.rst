How to use the `Supplier` class
=========================================================================================

Description
-------------------------
The `Supplier` class is a base class for interacting with data providers (e.g., Amazon, AliExpress, Walmart) in your application.  It defines common attributes and methods that can be used or overridden by specific implementations for different providers.  It handles tasks like configuration loading, web driver initialization, login (if required), and running predefined scenarios for data extraction.

Execution steps
-------------------------
1. **Initialization:** Create an instance of the `Supplier` class, providing the `supplier_prefix` (e.g., 'aliexpress'), desired `locale`, and optionally a `webdriver` type.
   ```python
   supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
   ```

2. **Configuration Loading:** Call the `_payload` method to load configuration files specific to the supplier. This includes locators for web elements, scenario files, and other necessary settings. The `webdriver` argument is also passed here, crucial for browser initialization.
   ```python
   supplier._payload(webdriver='chrome')  # or supplier._payload('chrome')
   ```

3. **Login (if required):** If the data provider requires authentication, call the `login` method to log in.
   ```python
   supplier.login()
   ```

4. **Running Scenario Files:** Execute data extraction scenarios defined in files.  Pass a list of file names to the `run_scenario_files` method.
   ```python
   supplier.run_scenario_files(['example_scenario.json'])
   ```
   *Alternatively, you can run scenarios using specific instructions.*: Use the `run_scenarios` method passing a list of dictionaries, each dict representing a scenario with an `action` (e.g., `scrape`) and the required parameters (`target`, etc.):
   ```python
   supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
   ```

5. **Data Processing:** The `run_scenario_files` or `run_scenarios` methods handle the actual data extraction tasks based on the provided scenario files or parameters.  Subsequent steps to process and use the extracted data are outside this base class.


Usage example
-------------------------
```python
from your_module import Supplier  # Replace 'your_module'

# Assuming you have a 'Supplier' class defined elsewhere in your code
# and appropriate scenario files (e.g., example_scenario.json)

# Create a Supplier object for AliExpress
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Load configurations
supplier._payload(webdriver='chrome')

# Attempt login (replace with actual login logic if needed)
supplier.login()

# Run scenarios from files
supplier.run_scenario_files(['example_scenario.json'])


# Run specific scenarios
supplier.run_scenarios([
    {'action': 'scrape', 'target': 'product_list', 'output_file': 'products.json'}
])

# Further processing and use of the extracted data would happen here...
```

**Important Notes:**

* Replace placeholders like `'example_scenario.json'` with the actual file names.
* Adapt the `_payload` function if your configurations are loaded differently.
* Ensure the `Supplier` class is correctly defined with the specified methods and attributes.
* The `login` method is a placeholder, you'll need to implement the actual login procedure for your specific data provider.
* The `webdriver` parameter in `_payload` needs appropriate handling (e.g., setting up the webdriver object) to be effective.