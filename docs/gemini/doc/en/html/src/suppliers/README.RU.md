html
<h1>Module Supplier</h1>

<h2>Overview</h2>
<p>The `Supplier` class centralizes management of suppliers, including configuration, authentication, and scenario execution. It can be extended for new suppliers through inheritance or by adding additional modules.</p>

<h2>Classes</h2>

<h3><code>Supplier</code></h3>

<p><strong>Description</strong>: The base class for all suppliers.  It serves as the foundation for managing interactions with suppliers. It handles initialization, configuration, authentication, and running scenarios for various data sources such as <code>amazon.com</code>, <code>walmart.com</code>, <code>mouser.com</code>, and <code>digikey.com</code>.  Clients can define additional suppliers.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_id</code> (int): Unique supplier identifier.</li>
  <li><code>supplier_prefix</code> (str): Supplier prefix, e.g., 'amazon', 'aliexpress'.</li>
  <li><code>supplier_settings</code> (dict): Supplier settings loaded from a JSON file.</li>
  <li><code>locale</code> (str): Localization code (default: 'en').</li>
  <li><code>price_rule</code> (str): Price calculation rules (e.g., VAT rules).</li>
  <li><code>related_modules</code> (module): Helper modules for working with a specific supplier.</li>
  <li><code>scenario_files</code> (list): List of scenario files to execute.</li>
  <li><code>current_scenario</code> (dict): Currently running scenario.</li>
  <li><code>login_data</code> (dict): Authentication data.</li>
  <li><code>locators</code> (dict): Dictionary of web element locators.</li>
  <li><code>driver</code> (Driver): WebDriver instance for interacting with the supplier's website.</li>
  <li><code>parsing_method</code> (str): Data parsing method (e.g., 'webdriver', 'api', 'xls', 'csv').</li>
</ul>


<p><strong>Methods</strong>:</p>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Constructor of the <code>Supplier</code> class.</p>

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Initialization of a Supplier instance.

    Args:
        supplier_prefix (str): Supplier prefix.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): WebDriver type. Defaults to 'default'.

    Raises:
        DefaultSettingsException: If default settings are not configured correctly.
    """
```

<h3><code>_payload</code></h3>

<p><strong>Description</strong>: Loads supplier settings and initializes WebDriver.</p>

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes WebDriver.

    Args:
        webdriver (str | Driver | bool): WebDriver type.

    Returns:
        bool: Returns True if loading was successful.
    """
```

<h3><code>login</code></h3>

<p><strong>Description</strong>: Handles authentication on the supplier's website.</p>

```python
def login(self) -> bool:
    """Performs user authentication on the supplier's website.

    Returns:
        bool: Returns True if login was successful.
    """
```

<h3><code>run_scenario_files</code></h3>

<p><strong>Description</strong>: Executes one or more scenario files.</p>

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Runs the provided scenario files.

    Args:
        scenario_files (str | List[str], optional): List or path to scenario files.

    Returns:
        bool: Returns True if scenarios were executed successfully.
    """
```

<h3><code>run_scenarios</code></h3>

<p><strong>Description</strong>: Executes specified scenarios.</p>

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Runs specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to execute.

    Returns:
        bool: Returns True if all scenarios were executed successfully.
    """
```


<h2>Functions</h2>
<!-- No functions defined in this document. -->


<h2>How it Works</h2>

<p>...</p>


<h2>Class Diagram</h2>

<pre><code>
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
</code></pre>