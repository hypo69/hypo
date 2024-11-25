html
<h1>Module: Supplier</h1>

<h2>Overview</h2>
<p>This module defines the `Supplier` class, a base class for interacting with data providers (e.g., Amazon, AliExpress, Walmart). It provides common methods and attributes that can be used or overridden by specific provider implementations.</p>

<h2>Classes</h2>

<h3><code>Supplier</code></h3>

<p><strong>Description</strong>: This class serves as a foundation for implementing various data providers. It encapsulates common functionalities for interacting with data sources.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_id</code> (str): A unique identifier for the supplier.</li>
  <li><code>supplier_prefix</code> (str): A prefix for the supplier (e.g., 'aliexpress', 'amazon').</li>
  <li><code>supplier_settings</code> (dict): Settings for the supplier, loaded from a configuration file.</li>
  <li><code>locale</code> (str): The locale code (e.g., 'en' for English, 'ru' for Russian).</li>
  <li><code>price_rule</code> (function): The price calculation rule (e.g., adding VAT or discounts).</li>
  <li><code>related_modules</code> (module): A module containing supplier-specific functions.</li>
  <li><code>scenario_files</code> (list): A list of scenario files to be executed.</li>
  <li><code>current_scenario</code> (str): The currently running scenario.</li>
  <li><code>login_data</code> (dict): Login data for the supplier's website (if required).</li>
  <li><code>locators</code> (dict): Locators for web elements on the supplier's website pages.</li>
  <li><code>driver</code> (webdriver): The webdriver for interacting with the supplier's website.</li>
  <li><code>parsing_method</code> (str): The data parsing method (e.g., 'webdriver', 'api', 'xls', 'csv').</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | webdriver.WebDriver | bool = 'default', *attrs, **kwargs)</code>
    <ul>
      <li><strong>Description</strong>: Constructor to initialize the `Supplier` object. It initializes the supplier prefix, locale, and webdriver.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>supplier_prefix</code> (str): The prefix for the supplier.</li>
          <li><code>locale</code> (str, optional): The locale code. Defaults to 'en'.</li>
          <li><code>webdriver</code> (str | webdriver.WebDriver | bool, optional): The webdriver to use. Defaults to 'default'.</li>
          <li><code>*attrs</code>:  Variable positional arguments.</li>
          <li><code>**kwargs</code>: Keyword arguments.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: None</li>
    </ul>
  </li>
  <li><code>_payload(self, webdriver: str | webdriver.WebDriver | bool, *attrs, **kwargs) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Loads supplier settings, configuration files, and initializes the webdriver.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>webdriver</code> (str | webdriver.WebDriver | bool): The webdriver to use.</li>
          <li><code>*attrs</code>: Variable positional arguments.</li>
          <li><code>**kwargs</code>: Keyword arguments.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: bool: True if successful, False otherwise.</li>
    </ul>
  </li>
  <li><code>login(self) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Logs in to the supplier's website (if required).</li>
      <li><strong>Returns</strong>: bool: True if successful, False otherwise.</li>
    </ul>
  </li>
  <li><code>run_scenario_files(self, scenario_files: str | List[str] = None) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Executes scenarios from specified files.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>scenario_files</code> (str | list, optional): Path to the scenario file or a list of files.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: bool: True if successful, False otherwise.</li>
    </ul>
  </li>
  <li><code>run_scenarios(self, scenarios: dict | list[dict]) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Executes specified scenarios.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>scenarios</code> (dict | list): A dictionary or a list of dictionaries defining the scenarios.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: bool: True if successful, False otherwise.</li>
    </ul>
  </li>

</ul>

<h2>Functions</h2>
<!-- (No functions defined in the provided code snippet) -->

<h2>Examples</h2>
<!-- (Include example usage as provided in the code) -->

```
```
```html