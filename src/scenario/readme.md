
### Module Overview: `src.scenario`

The `src.scenario` module is designed to automate interactions with suppliers using scenarios described in JSON files. Its primary task is to adapt the process of extracting and processing product data from supplier websites and synchronize this information with your system's database.

### Main Functions of the Module

1. **Read Scenarios**: The module loads scenarios from JSON files that contain information about various product categories and their URLs on the supplier's website.

2. **Interact with Websites**: Using the URLs specified in the scenarios, the module navigates to the product pages and extracts the necessary data.

3. **Process Data**: The module processes the extracted product data, converts it into the required format, and saves it into your system's database (e.g., PrestaShop).

4. **Logging Execution**: The module keeps a log of scenario executions, recording details of execution and results, which helps track success and identify errors.

### Main Components of the Module

1. **`run_scenario_files(s, scenario_files_list)`**:
   - Takes a list of scenario files and processes them sequentially.
   - Calls `run_scenario_file` to handle each scenario file.

2. **`run_scenario_file(s, scenario_file)`**:
   - Loads scenarios from the specified file and calls `run_scenario` for each scenario in the file.

3. **`run_scenario(s, scenario)`**:
   - Processes an individual scenario.
   - Navigates to the URL specified in the scenario and extracts product data.
   - Saves the extracted data into the database.

4. **`dump_journal(s, journal)`**:
   - Saves the execution log of scenarios to a file for later analysis.

5. **`main()`**:
   - Main function to run the module.

### Example Scenario

An example JSON scenario describes how to interact with specific product categories on a website. It includes:
- **URL of the Page**: For navigation and data extraction.
- **Category Name**: For identifying the category.
- **`presta_categories`**: Identifiers of categories in the PrestaShop database where products will be saved.

```json
{
    "scenarios": {
        "מינרל+לחויותלפניםמינרליםותמציותצמחים": {
            "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
            "name": "מינרל+לחויותלפניםמינרליםותמציותצמחים",
            "presta_categories": {
                "default_category": 11245,
                "additional_categories": [11288]
            }
        }
    }
}
```


#### Scenario Fields

- **`"scenario_name"`**: The name of the scenario.

  - **`"url"`**: The target address - a link to a category, section, or individual product.

  - **`"name"`**: The category name - it matches the name of the scenario.

  - **`"presta_categories"`**:
    - **`"default_category"`**: The default category ID in PrestaShop where products from this scenario will be categorized.
    - **`"additional_categories"`**: A list of additional category IDs in PrestaShop for further categorization.

    This field specifies the categories in the PrestaShop framework where the product data will be stored. During scenario execution, this information is used to update the relevant data in the database.
### How It Works

1. **Loading Scenarios**: The module loads and analyzes scenarios from files.

2. **Data Extraction**: Navigates to the URL from the scenario, extracts product links, and collects information about them.

3. **Data Saving**: Processes and saves the collected data into the database using category information from the scenario.

4. **Reports and Logging**: Maintains a log of scenario executions to track progress and record errors.

This module helps automate the collection and processing of product data from various sources, simplifying integration with different suppliers and product management systems.


## Workflow for Script Executor Module

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
     - Calls `execute_PrestaShop_insert` asynchronously.

   **6. `execute_PrestaShop_insert(f, coupon_code, start_date, end_date)`**:
   - **Purpose**: Inserts product data into PrestaShop.
   - **Steps**:
     - Uses the `PrestaShop` class to post product data.
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


## Explanation of the code in `executor.py`:

### Overview of `executor.py`

This script contains functions and methods for executing scenarios related to automated web data collection or testing. The primary goal is to fetch product data from category pages and insert this data into the PrestaShop system.

### Main Functions and Methods

1. **`dump_journal(s, journal: dict)`**

   **Purpose**: Records the state of scenario execution into a JSON file.

   **What it Does**:
   - Creates a file path for the journal.
   - Saves the current journal data to a JSON file.

2. **`run_scenario_files(s, scenario_files_list: Union[List[Path], Path]) -> bool`**

   **Purpose**: Executes a list of scenario files sequentially.

   **What it Does**:
   - Takes a list of scenario files and, for each file, calls `run_scenario_file`.
   - Logs the results of each file’s execution and updates the journal.

3. **`run_scenario_file(s, scenario_file: Union[Path, str]) -> bool`**

   **Purpose**: Loads a scenario from a file and executes it.

   **What it Does**:
   - Reads the JSON scenario file.
   - For each scenario in the file, it calls `run_scenario` to process it.

4. **`run_scenarios(s, scenarios: Union[List[dict], dict] = None, _journal=None) -> Union[List, dict, False]`**

   **Purpose**: Executes one or more scenarios.

   **What it Does**:
   - Accepts a list of scenarios or a single scenario and calls `run_scenario` for each one.
   - If no scenarios are provided, it uses the current scenario from the supplier instance.

5. **`run_scenario(supplier, scenario: dict, _journal=None) -> Union[List, dict, False]`**

   **Purpose**: Executes a specific scenario.

   **What it Does**:
   - Loads the URL for the product category.
   - Fetches product links and collects data from each product page.
   - Inserts the collected product data into the PrestaShop system.

6. **`insert_grabbed_data(product_fields: ProductFields)`**

   **Purpose**: Inserts the collected product data into PrestaShop.

   **What it Does**:
   - Calls the asynchronous function `execute_PrestaShop_insert_async` to handle the data insertion.

7. **`execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**

   **Purpose**: Asynchronously handles the insertion of product data into PrestaShop.

   **What it Does**:
   - Calls `execute_PrestaShop_insert` to perform the actual data insertion.

8. **`execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**

   **Purpose**: Inserts product data into PrestaShop.

   **What it Does**:
   - Creates a PrestaShop client and sends the product data for insertion.
   - Handles product additions or updates and manages product images.

### Workflow of the Code

```plaintext
[Scenario Files] 
       ↓ 
   run_scenario_files()
       ↓
   run_scenario_file()
       ↓
  [Scenario JSON Data]
       ↓
   run_scenario()
       ↓
[Fetch Product Data]
       ↓
[Insert Data into PrestaShop]
```

### Example Usage

1. **Running Scenario Files**:
   ```python
   scenario_files_list = [Path("path/to/scenario1.json"), Path("path/to/scenario2.json")]
   run_scenario_files(supplier_instance, scenario_files_list)
   ```

   This code runs all the scenarios from the provided files, collecting product data and inserting it into PrestaShop.

2. **Loading and Executing a Single Scenario File**:
   ```python
   scenario_file = Path("path/to/scenario.json")
   run_scenario_file(supplier_instance, scenario_file)
   ```

   This code loads the scenario from the file and executes it, collecting data and performing the necessary actions.

3. **Executing Scenarios Directly**:
   ```python
   scenarios = [{'url': 'http://example.com/category1'}, {'url': 'http://example.com/category2'}]
   run_scenarios(supplier_instance, scenarios)
   ```

   This code executes a list of scenarios.

### Simplified diagram of the process:

```plaintext
Scenario Files → Load Scenarios → Fetch Product Data → Insert Data into PrestaShop
```

### Detailed Function Descriptions

1. **`dump_journal(s, journal: dict)`**

   **Description**: Handles the process of logging scenario execution states.

   **Parameters**:
   - `s`: Supplier instance.
   - `journal`: Dictionary storing the state of scenario execution.

   **Details**:
   - Creates a journal file path and saves the `journal` data as a JSON file.

2. **`run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool`**

   **Description**: Runs a series of scenario files.

   **Parameters**:
   - `s`: Supplier instance.
   - `scenario_files_list`: List of paths to the scenario files.

   **Returns**: `True` if all scenarios are executed successfully, otherwise `False`.

   **Details**:
   - Executes scenarios from a list of files and logs the outcomes.

3. **`run_scenario_file(s, scenario_file: Path | str) -> bool`**

   **Description**: Loads and runs scenarios from a file.

   **Parameters**:
   - `s`: Supplier instance.
   - `scenario_file`: Path to the scenario file.

   **Returns**: `True` if the scenario file was executed successfully, otherwise `False`.

   **Details**:
   - Reads the scenario JSON and processes each scenario.

4. **`run_scenarios(s, scenarios: List[dict] | dict = None, _journal=None) -> List | dict | False`**

   **Description**: Executes a list or a single scenario.

   **Parameters**:
   - `s`: Supplier instance.
   - `scenarios`: List or single scenario to execute.

   **Returns**: Result of executing scenarios, or `False` if an error occurs.

   **Details**:
   - Processes the provided scenarios or defaults to `s.current_scenario`.

5. **`run_scenario(supplier, scenario: dict, _journal=None) -> List | dict | False`**

   **Description**: Executes a specific scenario.

   **Parameters**:
   - `supplier`: Supplier instance.
   - `scenario`: Dictionary containing scenario details.

   **Returns**: List of product links or `False` if an error occurs.

   **Details**:
   - Navigates to product pages, collects data, and inserts it into PrestaShop.

6. **`insert_grabbed_data(product_fields: ProductFields)`**

   **Description**: Inserts collected product data into PrestaShop.

   **Parameters**:
   - `product_fields`: Product fields object.

   **Details**:
   - Calls an async function to insert the data.

7. **`execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**

   **Description**: Asynchronously inserts product data into PrestaShop.

   **Parameters**:
   - `f`: ProductFields object.
   - `coupon_code`, `start_date`, `end_date`: Optional parameters for coupon insertion.

   **Details**:
   - Calls a synchronous function to handle the data insertion.

8. **`execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**

   **Description**: Inserts product data into PrestaShop.

   **Parameters**:
   - `f`: ProductFields object.
   - `coupon_code`, `start_date`, `end_date`: Optional parameters for coupon insertion.

   **Returns**: `True` if the insertion was successful, otherwise `False`.

   **Details**:
   - Creates a PrestaShop client and handles product addition or updates.

Here’s a detailed dependency tree for the `executor.py` module, showing how different functions and methods relate to one another:

### Dependency Tree for `executor.py`

```plaintext
└── run_scenario_files(s, scenario_files_list: Union[List[Path], Path]) -> bool
    ├── run_scenario_file(s, scenario_file: Union[Path, str]) -> bool
    │   ├── run_scenario(supplier, scenario: dict, _journal=None) -> Union[List, dict, False]
    │   │   ├── fetch_product_links(scenario)  # Fetches links from the category page
    │   │   │   ├── collect_product_data(product_link)  # Collects data for each product
    │   │   │   │   ├── insert_grabbed_data(product_fields: ProductFields)  # Inserts product data into PrestaShop
    │   │   │   │   │   ├── execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool
    │   │   │   │   │   │   ├── execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool
    │   │   │   │   │   │   │   └── PrestaShopClient  # Interacts with the PrestaShop API
    │   │   │   │   │   └── (Other methods to process and validate product data)
    │   │   │   └── (Other methods for fetching and processing data)
    │   │   ├── update_journal(scenario)  # Updates the journal
    │   │   └── (Error handling and logging)
    │   └── (Error handling and logging)
    ├── dump_journal(s, journal: dict)  # Creates or updates the journal file
    └── (General error handling and logging)

run_scenario_files(s, scenario_files_list: Union[List[Path], Path]) -> bool
│
├── run_scenario_file(s, scenario_file: Union[Path, str]) -> bool
│
└── run_scenario(supplier, scenario: dict, _journal=None) -> Union[List, dict, False]
   ├── fetch_product_links(scenario)
   │   └── collect_product_data(product_link)
   │       └── insert_grabbed_data(product_fields: ProductFields)
   │           ├── execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool
   │           │   └── execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool
   │           │       └── PrestaShopClient
   │           └── (Additional methods for data processing)
   ├── update_journal(scenario)
   └── (Error handling and logging)

### Breakdown of Methods

1. **`run_scenario_files(s, scenario_files_list: Union[List[Path], Path]) -> bool`**
   - Calls: `run_scenario_file(s, scenario_file)`

2. **`run_scenario_file(s, scenario_file: Union[Path, str]) -> bool`**
   - Calls: `run_scenario(supplier, scenario)`

3. **`run_scenario(supplier, scenario: dict, _journal=None) -> Union[List, dict, False]`**
   - Calls: `fetch_product_links(scenario)`

4. **`fetch_product_links(scenario)`**
   - Calls: `collect_product_data(product_link)`

5. **`collect_product_data(product_link)`**
   - Calls: `insert_grabbed_data(product_fields: ProductFields)`

6. **`insert_grabbed_data(product_fields: ProductFields)`**
   - Calls: `execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`

7. **`execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**
   - Calls: `execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`

8. **`execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`**
   - Uses: `PrestaShopClient`

9. **`dump_journal(s, journal: dict)`**
   - Handles: File I/O for the journal

10. **`update_journal(scenario)`**
    - Updates the journal with the current scenario state

### Functions and Dependencies

Here’s how the functions depend on each other, focusing on direct function calls:

```plaintext
run_scenario_files
    └── run_scenario_file
        └── run_scenario
            ├── fetch_product_links
            │   └── collect_product_data
            │       └── insert_grabbed_data
            │           ├── execute_PrestaShop_insert_async
            │           │   └── execute_PrestaShop_insert
            │           │       └── PrestaShopClient
            │           └── (Other methods)
            └── update_journal
```

### Representation of the dependencies:

```plaintext
[run_scenario_files]
        |
        V
[run_scenario_file]
        |
        V
[run_scenario]
        |
        V
[fetch_product_links]
        |
        V
[collect_product_data]
        |
        V
[insert_grabbed_data]
        |
        V
[execute_PrestaShop_insert_async]
        |
        V
[execute_PrestaShop_insert]
        |
        V
[PrestaShopClient]
```

### Summary

- **`run_scenario_files`** is the entry point for executing multiple scenario files.
- **`run_scenario_file`** processes each file and calls **`run_scenario`** to handle individual scenarios.
- **`run_scenario`** fetches product links, collects data, and inserts it into PrestaShop.
- **`fetch_product_links`** and **`collect_product_data`** handle data collection and interaction with product pages.
- **`insert_grabbed_data`** manages the data insertion process.
- **`execute_PrestaShop_insert_async`** and **`execute_PrestaShop_insert`** handle asynchronous and synchronous data insertion into PrestaShop.
- **`dump_journal`** and **`update_journal`** manage the journal updates.

This dependency tree should help you understand how different parts of the `executor.py` script interact and build upon one another.