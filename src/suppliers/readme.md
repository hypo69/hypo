

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

## **How It Works**

1. **Initialization**:
   - The `__init__` method sets up the supplier prefix, locale, and WebDriver.  
     Example:
     ```python
     supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
     ```

2. **Configuration Loading**:
   - `_payload` loads the configuration and initializes locators and WebDriver.  
     Example:
     ```python
     supplier._payload(webdriver='firefox')
     ```

3. **Authentication**:
   - `login` handles user login to the supplier's website.  
     Example:
     ```python
     supplier.login()
     ```

4. **Scenario Execution**:
   - **Run scenario files**:
     ```python
     supplier.run_scenario_files(['example_scenario.json'])
     ```
   - **Run specific scenarios**:
     ```python
     supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
     ```

---

## **Class Diagram**

```plaintext
Supplier
├── Attributes
│   ├── supplier_id: int
│   ├── supplier_prefix: str
│   ├── supplier_settings: dict
│   ├── locale: str
│   ├── price_rule: str
│   ├── related_modules: module
│   ├── scenario_files: list
│   ├── current_scenario: dict
│   ├── login_data: dict
│   ├── locators: dict
│   ├── driver: Driver
│
├── Methods
│   ├── __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs)
│   ├── _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool
│   ├── login(self) -> bool
│   ├── run_scenario_files(self, scenario_files: str | List[str] = None) -> bool
│   ├── run_scenarios(self, scenarios: dict | list[dict]) -> bool
```

---
