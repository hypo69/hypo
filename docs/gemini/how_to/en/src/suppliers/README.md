# **Class** `Supplier`

### **Base class for all suppliers**

*In the context of the code, `Supplier` represents an information provider.  A supplier can be a producer of goods, data, or information.  The supplier's sources include a website's landing page, a document, a database, or a table.  This class unifies different suppliers under a standardized set of operations. Each supplier has a unique prefix. ([Details on prefixes](prefixes.md))*

The `Supplier` class serves as the foundation for managing interactions with suppliers. It handles initialization, configuration, authentication, and execution of workflows for various data sources, such as `amazon.com`, `walmart.com`, `mouser.com`, and `digikey.com`. Clients can also define additional suppliers.

---

## List of implemented suppliers:

[aliexpress](aliexpress)  - Implemented with two workflows: `webdriver` and `api`
[amazon](amazon) - `webdriver`
[bangood](bangood)  - `webdriver`
[cdata](cdata)  - `webdriver`
[chat_gpt](chat_gpt)  - Interacts with the ChatGPT interface (NOT THE MODEL!)
[ebay](ebay)  - `webdriver`
[etzmaleh](etzmaleh)  - `webdriver`
[gearbest](gearbest)  - `webdriver`
[grandadvance](grandadvance)  - `webdriver`
[hb](hb)  - `webdriver`
[ivory](ivory) - `webdriver`
[ksp](ksp) - `webdriver`
[kualastyle](kualastyle) `webdriver`
[morlevi](morlevi) `webdriver`
[visualdg](visualdg) `webdriver`
[wallashop](wallashop) `webdriver`
[wallmart](wallmart) `webdriver`

[Details on WebDriver :class: `Driver`](../webdriver)
[Details on workflows :class: `Scenario`](../scenarios)

---

## **Attributes**

- **`supplier_id`** *(int)*: Unique identifier for the supplier.
- **`supplier_prefix`** *(str)*: Supplier prefix, e.g., `'amazon'`, `'aliexpress'`.
- **`supplier_settings`** *(dict)*: Supplier settings loaded from a JSON file.  Crucially, this should contain necessary configuration such as URLs, credentials, and other required data for each supplier type.
- **`locale`** *(str)*: Localization code (default: `'en'`).
- **`price_rule`** *(str)*: Rules for price calculations (e.g., VAT rules).  This needs to be a properly formatted string defining your price calculation logic.
- **`related_modules`** *(module)*: Helper modules for specific supplier operations.
- **`scenario_files`** *(list)*: List of scenario files to be executed.  The paths should be correctly specified for the file system.
- **`current_scenario`** *(dict)*: Scenario currently being executed.
- **`login_data`** *(dict)*: Data for authentication (username, password, API keys, etc.).  This should be securely managed.
- **`locators`** *(dict)*: Dictionary of web element locators. This is essential for automating interactions with websites.
- **`driver`** *(Driver)*: WebDriver instance for interacting with the supplier's website.
- **`parsing_method`** *(str)*: Data parsing method (e.g., `'webdriver'`, `'api'`, `'xls'`, `'csv'`).  This is essential for handling different data formats.


---

## **Methods**

### **`__init__`**

**Constructor of the `Supplier` class.**

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Initializes an instance of Supplier.

    Args:
        supplier_prefix (str): The supplier's prefix.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): Type of WebDriver. Defaults to 'default'.

    Raises:
        DefaultSettingsException: If default settings are not properly configured.
        FileNotFoundError: If the supplier_settings file does not exist.
        ValueError: For invalid configurations.
    """
    # ... (Implementation details) ...
```

### **`_payload`**

**Loads supplier settings and initializes the WebDriver.**

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes the WebDriver.

    Args:
        webdriver (str | Driver | bool): Type of WebDriver.

    Returns:
        bool: Returns `True` if the loading was successful.
        Raises Exceptions:  If loading fails for any reason.
    """
    # ... (Implementation details) ...
```

### **`login`**

**Handles authentication on the supplier's website.**  **Crucially, include error handling.**

```python
def login(self) -> bool:
    """Authenticates the user on the supplier's website.

    Returns:
        bool: Returns `True` if login was successful.
        Raises Exceptions: On authentication failure, connection errors, etc.
    """
    # ... (Implementation details) ...
```

### **`run_scenario_files`**

**Executes one or more scenario files.**

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Runs the provided scenario files.

    Args:
        scenario_files (str | List[str], optional): List or path to scenario files.

    Returns:
        bool: Returns `True` if scenarios were executed successfully.
        Raises Exceptions: on file not found, invalid scenario format, etc.
    """
    # ... (Implementation details) ...
```

### **`run_scenarios`**

**Executes specified scenarios.**

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Executes specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to be executed.

    Returns:
        bool: Returns `True` if all scenarios were executed successfully.
        Raises Exceptions: for invalid scenario format, missing data, etc.
    """
    # ... (Implementation details) ...
```

---

## **How it works** (with improved clarity)

1. **Initialization (`__init__`):**  Sets up the basic supplier information (prefix, locale, WebDriver type).  Crucially, loads the `supplier_settings`.
2. **Loading Settings (`_payload`):** Loads the supplier-specific configuration (e.g., URLs, credentials, locators).  Initializes the WebDriver.  **Error handling** is vital here!
3. **Authentication (`login`):** Logs in to the supplier's website.  This method should **handle authentication failures**.
4. **Executing Scenarios (`run_scenario_files`, `run_scenarios`):** Runs the defined scenarios, processing the data and performing the desired actions.  This needs to include error handling on a per-scenario basis.


**Important Considerations:**

* **Error Handling:**  Add comprehensive error handling to each method to catch potential issues (e.g., file not found, invalid data, connection problems, authentication failures).  This is crucial for robust code.
* **Security:** Securely manage sensitive data like passwords and API keys.
* **Logging:** Implement logging to track the execution process and any encountered errors.
* **Data Validation:** Validate the format and content of data being loaded and processed.
* **Maintainability:**  Use clear naming conventions and well-commented code.