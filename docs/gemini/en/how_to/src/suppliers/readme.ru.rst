rst
How to use the `Supplier` class
========================================================================================

Description
-------------------------
The `Supplier` class is a base class for all information providers.  A supplier can be a manufacturer of a product, a data source, or a source of information.  Supplier sources can be target website pages, documents, databases, or tables. The `Supplier` class standardizes the actions of different suppliers within a common class structure. Each supplier has a unique prefix (see `prefixes.md` for details).

The `Supplier` class serves as a foundation for managing interactions with suppliers. It handles initialization, configuration, authentication, and running scenarios for various data sources, such as `amazon.com`, `walmart.com`, `mouser.com`, and `digikey.com`.  Clients can define additional suppliers.

This documentation details the `Supplier` class, its attributes, and methods, along with usage examples.


Execution steps
-------------------------
1. **Initialization:** Instantiate a `Supplier` object, providing the supplier prefix, locale (defaults to 'en'), and WebDriver type (defaults to 'default').  Specify additional attributes if necessary.
   ```python
   supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
   ```

2. **Loading Settings:** Call the `_payload` method to load supplier settings, locators, and initialize the WebDriver.
   ```python
   supplier._payload(webdriver='firefox')
   ```

3. **Authentication (if required):** Call the `login` method to authenticate the user on the supplier website.
   ```python
   supplier.login()
   ```

4. **Running Scenarios:** Choose one of the following options to execute scenarios:
    * **Running Scenario Files:** Call `run_scenario_files` with a list of scenario file names or a single file path to run the scenarios contained within those files.
      ```python
      supplier.run_scenario_files(['scenario1.json', 'scenario2.json'])
      ```
    * **Running Specific Scenarios:** Call `run_scenarios` with a list or dictionary of scenarios to be executed, specifying details for each scenario as needed.
      ```python
      supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
      ```
   This will execute actions defined within the scenarios.

5. **Processing Results:** The results from the executed scenarios will be available through various means depending on the scenario implementation.  Refer to individual scenario documentation (e.g., `scenario/README.RU.MD`) for details on data access and formatting.


Usage example
-------------------------
.. code-block:: python

    from suppliers.supplier import Supplier
    from suppliers.aliexpress import Aliexpress

    # Instantiate the Aliexpress supplier
    supplier = Aliexpress(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')

    # Load settings, locators, and initialize the WebDriver
    supplier._payload(webdriver='firefox')

    # Login to the AliExpress website (if required)
    supplier.login()

    # Run a specific scenario (replace with your scenario definition)
    scenario_data = {'action': 'scrape', 'target': 'product_list', 'filters': {'category': 'Electronics'}}
    supplier.run_scenarios([scenario_data])

    # Process the results -  implementation specific to the scenario being run.