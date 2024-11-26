```
# Supplier Class Documentation

## **Class** `Supplier`
### **Base class for all suppliers**

The `Supplier` class serves as the foundation for managing supplier interactions. It handles initialization, configuration, authentication, and scenario execution for various data sources, such as `amazon.com`, `walmart.com`, `mouser.com`, and `digikey.com`. Additional suppliers can be defined by the customer.


---

## **Attributes**
- **`supplier_id`** *(int)*: Unique identifier for the supplier.
- **`supplier_prefix`** *(str)*: Supplier prefix, e.g., `'amazon'`, `'aliexpress'`.
- **`supplier_settings`** *(dict)*: Settings specific to the supplier, loaded from a JSON file.
- **`locale`** *(str)*: Localization code (default: `'en'`).
- **`price_rule`** *(str)*: Rules for price calculation (e.g., VAT rules).
- **`related_modules`** *(module)*: Supplier-specific helper modules.
- **`scenario_files`** *(list)*: List of scenario files to execute.
- **`current_scenario`** *(dict)*: Currently executing scenario.
- **`login_data`** *(dict)*: Login credentials and related data for authentication.
- **`locators`** *(dict)*: Locator dictionary for web elements.
- **`driver`** *(Driver)*: WebDriver instance for supplier website interaction.
- **`parsing_method`** *(str)*: Data parsing method (e.g., `'webdriver'`, `'api'`, `'xls'`, `'csv'`).


---

## **Methods**

### **`__init__`**
**Constructor for the `Supplier` class.**

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Initializes the Supplier instance.

    Args:
        supplier_prefix (str): Prefix for the supplier.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): WebDriver type. Defaults to 'default'.

    Raises:
        DefaultSettingsException: If default settings are not configured correctly.
    """
```

---

### **`_payload`**
**Loads supplier configurations and initializes the WebDriver.**

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes the WebDriver.

    Args:
        webdriver (str | Driver | bool): WebDriver type.

    Returns:
        bool: Returns `True` if payload loaded successfully.
    """
```


---

### **`login`**
**Handles authentication for the supplier's website.**

```python
def login(self) -> bool:
    """Authenticates the user on the supplier's website.

    Returns:
        bool: Returns `True` if login was successful.
    """
```


---

### **`run_scenario_files`**
**Executes one or more scenario files.**

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Runs the provided scenario files.

    Args:
        scenario_files (str | List[str], optional): List or single path to scenario files.

    Returns:
        bool: Returns `True` if all scenarios executed successfully.
    """
```


---

### **`run_scenarios`**
**Executes provided scenarios.**

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Executes the specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to execute.

    Returns:
        bool: Returns `True` if all scenarios executed successfully.
    """
```


---

## <algorithm>

```mermaid
graph TD
    A[Supplier Instance] --> B{__init__(supplier_prefix, locale, webdriver)};
    B --> C{_payload(webdriver)};
    C --> D[Login];
    D --> E{run_scenario_files(scenario_files)};
    E --> F{run_scenarios(scenarios)};
    F --> G[Success/Failure];
```

**Example Data Flow:**

* **`__init__`:** `supplier_prefix` = 'amazon', `locale` = 'en', `webdriver` = 'chrome'
* **`_payload`:** Loads settings from 'amazon_settings.json', initializes the 'chrome' WebDriver, populates `locators`.  This function can return False if the file doesn't exist or the settings are invalid.
* **`Login`:** Attempts to log into amazon.com, return True if successful.
* **`run_scenario_files`:** Executes scenarios specified in 'scenario1.json', 'scenario2.json'. Returns True if all scenarios complete successfully, otherwise False.
* **`run_scenarios`:** Executes scenarios passed as input to the function. Returns True if all scenarios complete successfully, otherwise False.



## <explanation>

**Imports:**  There are no explicit imports shown in the code snippet, but implicit imports for `List`, `Driver` and any other classes are likely to be present in other `src` packages related to the framework or testing library.  Missing imports would lead to errors.

**Classes:**

* **`Supplier`:** This is a base class responsible for interacting with different suppliers (e.g., Amazon, Walmart). It handles setup, authentication, and scenario execution.  It's a critical part of a larger system for data scraping or automation.
    * Attributes:  Clearly define the state of a supplier instance,  including important data like settings, locators, login information, and driver, making the object maintain state.
    * Methods:   Provide the necessary functionality like initialization (`__init__`), configuration loading (`_payload`), authentication (`login`), and scenario running (`run_scenario_files`, `run_scenarios`).  Note the use of `bool` return values.  `_payload` is crucial for loading configuration files, potentially raising an exception for error handling if config is invalid.


**Functions:**

* **`__init__`:** Initializes a `Supplier` object with a `supplier_prefix`, `locale`, and `webdriver`.  Handles optional arguments (`*attrs`, `**kwargs`) indicating flexibility to adapt to future enhancements. The `webdriver` parameter accepts either the driver name (`'chrome'`, `'firefox'`), a `Driver` object itself (for custom drivers), or `bool` to enable/disable.
* **`_payload`:** Loads configuration settings and initializes the WebDriver.  Crucially, returns a boolean to indicate success or failure. This method is a hidden helper which would be expected in most supplier-interaction cases.
* **`login`:** Attempts to log in to the supplier's website. Returns `True` if login is successful.  The implementation should handle potential exceptions or failures during the login process.
* **`run_scenario_files`:** Executes a list of scenario files.  Handles a single file as input as well.
* **`run_scenarios`:** Executes a list of predefined scenarios, making the class more flexible for varied automation actions.



**Variables:** The example variable `supplier_prefix` is a string, indicating a supplier identification string, for example `amazon`.


**Potential Errors/Improvements:**

* **Error Handling:** The code lacks specific error handling for file loading, login failures, and scenario execution errors.  Adding `try...except` blocks to each relevant method would significantly improve robustness.
* **Configuration Files:** The code assumes the existence of `supplier_settings` files.  A clearer method for loading these and specifying the path would be beneficial. Using the `pathlib` module to work with file paths would make the code more robust and portable.
* **`webdriver` Parameter:** While the flexibility of taking either a string or a `Driver` object is useful, it's imperative to document the expected behaviour with different parameters, or better yet, use a factory method to create `Driver` instances, reducing boilerplate and potential inconsistencies.

**Relationships:** This `Supplier` class is likely part of a larger framework for automated testing or data processing. The `Driver` object (mentioned as a `Driver` type hint) belongs to another part of the project (probably a testing or automation library) allowing interactions with web browsers. `scenario_files` and `scenarios` would likely reside within the same project, but this is unstated. Error handling should return appropriate exceptions for error reporting in a larger framework.