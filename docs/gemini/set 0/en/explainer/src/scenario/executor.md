# Executor.py Code Analysis

## <input code>

```python
# ... (imports and docstrings) ...

_journal: dict = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now

def dump_journal(s, journal: dict):
    # ... (journal saving logic) ...

def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    # ... (executes a list of scenario files) ...

def run_scenario_file(s, scenario_file: Path) -> bool:
    # ... (loads and executes scenarios from a file) ...

def run_scenarios(s, scenarios: List[dict] | dict = None) -> List | dict | False:
    # ... (executes a list of scenarios) ...

def run_scenario(supplier, scenario: dict, scenario_name: str) -> List | dict | False:
    # ... (executes a single scenario) ...

def insert_grabbed_data(product_fields: ProductFields):
    # ... (inserts grabbed product data into PrestaShop) ...

async def execute_PrestaShop_insert_async(f: ProductFields, ...):
    # ... (async version of insert function) ...

def execute_PrestaShop_insert(f: ProductFields, ...):
    # ... (inserts product into PrestaShop) ...
```

## <algorithm>

**Workflow for executing scenarios:**

1. **Input:** Supplier instance (`s`), a list of scenario files (`scenario_files_list`) or a single file.


2. **Initialization:**
   - The `_journal` dictionary is initialized to store scenario execution status.
   - Current timestamp is added to the journal.

3. **File Execution Loop:**
   - Iterates through each scenario file in `scenario_files_list`.
   - Calls `run_scenario_file()` to load and execute scenarios from the file.
   - Updates the `_journal` with success/failure messages for each scenario.
   - Handles and logs any exceptions during scenario file processing.
    - **Example:**
      - `scenario_file`: `path/to/scenario_1.json`
      - Executes `run_scenario_file(supplier, path/to/scenario_1.json)`
      - Updates `_journal['scenario_files']['scenario_1.json']` with a success or failure message.

4. **Scenario Execution Loop (run_scenarios):**
   - If no scenarios are explicitly provided, it retrieves scenarios from `s.current_scenario`.
   - Iterates through the list of scenarios (`scenarios`).
   - Calls `run_scenario()` to execute each scenario.
   - Updates `_journal` with results from `run_scenario()`.
   - **Example:**
      - `scenarios`: `[{'url': 'url1', 'type': 'type1'}, {'url': 'url2', 'type': 'type2'}]`
      - Iterates through each `scenario`, calls `run_scenario(supplier, scenario)`
      - Stores the returned result from `run_scenario()` in `_journal`.

5. **Scenario Execution (run_scenario):**
   - Navigates to the scenario's URL using the supplier's driver (`d`).
   - Retrieves the list of products in the category (`list_products_in_category`).
   - **Example:**
      - `scenario`: `{'url': 'https://example.com/category', 'type': 'category'}`
      - `d.get_url('https://example.com/category')`
      - `list_products_in_category` is populated with product URLs.
   - Processes each product URL:
      - Navigates to the product URL.
      - Grabs product details (`grab_product_page`).
      - Creates `Product` object.
      - Attempts to insert the product into PrestaShop (`insert_grabbed_data`).
      - Handles potential errors during product processing.


## <mermaid>

```mermaid
graph TD
    A[Supplier Instance (s)] --> B{scenario_files_list};
    B -- valid list --> C[run_scenario_files];
    B -- invalid list --> D[Error Handling];
    C --> E{Iterate through each scenario file};
    E --> F[run_scenario_file];
    F --> G{Load scenarios};
    G --> H[Iterate through each scenario];
    H --> I[run_scenario];
    I --> J[Navigate to URL];
    J --> K[Get list of products];
    K --> L{Iterate through products};
    L --> M[Navigate to product page];
    M --> N[Grab product fields];
    N --> O[Create Product object];
    O --> P[Insert product into PrestaShop];
    P -- success --> Q[Success];
    P -- failure --> R[Error Handling];
    Q --> S[Update Journal];
    R --> S;
    S --> T[Return True/False];
```


## <explanation>

**Imports:**

- `os`, `sys`, `requests`, `asyncio`, `time`, `tempfile`, `datetime`, `math`, `pathlib`, `typing`, `json`: Standard Python libraries for various tasks like file operations, system interactions, networking, asynchronous operations, date/time handling, mathematical functions, file paths, type hinting, and JSON parsing, respectively.
- `header`: Likely a custom module.  Needs more context from the rest of the project for complete understanding.
- `gs`: Likely a custom module for global services, like timestamping.
- `src.utils.printer`, `src.utils.jjson`: Custom modules for printing formatted output and working with JSON.
- `src.product`, `src.endpoints.prestashop`, `src.db`, `src.logger`, `src.logger.exceptions`:  Modules from the project's `src` package hierarchy.  `Product`, `PrestaShop`, `ProductCampaignsManager`, `logger`, and `ProductFieldException` likely manage product data, PrestaShop integration, database interactions, logging, and exception handling, respectively.

**Classes:**

- `Product`: Likely manages product data.  Attributes like `supplier_prefix` and `presta_fields_dict` suggest product details and how they are mapped to PrestaShop fields.
- `ProductFields`: Likely a container class for product fields.  `presta_fields_dict` and `assist_fields_dict` suggest different types of product fields.
- `PrestaShop`: This class is responsible for interacting with the PrestaShop API.
- `ProductCampaignsManager`: Likely interacts with the database related to product campaigns.

**Functions:**

- `dump_journal`: Saves journal data to a JSON file.
- `run_scenario_files`: Executes a list of scenario files.
- `run_scenario_file`: Executes scenarios from a single file.
- `run_scenarios`: Executes a list of scenarios (not files).
- `run_scenario`: Executes a single scenario, fetching product information, and inserting into PrestaShop.
- `insert_grabbed_data`: Inserts product data into PrestaShop (now deprecated).
- `execute_PrestaShop_insert`:  Inserts product data into PrestaShop using the `PrestaShop` class.
- `execute_PrestaShop_insert_async`: Asynchronous version of the `execute_PrestaShop_insert` function.

**Variables:**

- `_journal`: A dictionary used to store execution results and information.
- `timestamp`: Holds the current timestamp.

**Dependencies/Relationships:**

- The code relies heavily on the structure of the `src` package, implying a modular design.
- `gs`, `header`, `src.product`, `src.endpoints.prestashop`, `src.utils.printer`, `src.utils.jjson`, `src.logger`, and `src.db` are integral parts of the larger system.

**Potential Errors/Improvements:**

- **Error Handling:** While error handling is present, exceptions are caught and logged. Consider more specific error handling based on the type of error.
- **Asynchronous Operations:** Using `asyncio` is a good choice for potentially time-consuming tasks.  Make sure the asynchronous functions (`execute_PrestaShop_insert_async`) are used correctly.  It is likely that some functions like `s.related_modules.grab_page` are also async operations.
- **`dump_journal`:** Consider if this should be handled synchronously or asynchronously; it may impact the workflow for `run_scenarios` if it's asynchronous.
- **`insert_grabbed_data` is marked for removal.** It is called using `asyncio.run()`, suggesting it was once a function requiring asynchronous execution but can be refactored or consolidated for cleaner code.


**Overall, the code structure appears to be designed for modularity and potentially handling asynchronous tasks, which is a good practice, especially in data extraction and insertion tasks.**  The use of logging is also very important for debugging.