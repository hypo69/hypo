html
<h1>Supplier Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides the <code>Supplier</code> class, a base class for managing data suppliers. It handles initialization, data collection, login, and scenario execution for various sources like Amazon, AliExpress, and Walmart. It provides a structured approach to interact with different suppliers through a common interface.</p>

<h2>Classes</h2>

<h3><code>Supplier</code></h3>

<p><strong>Description</strong>: This class serves as a base class for managing data suppliers. It provides methods for initialization, configuration loading, login, and executing data collection scenarios.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_id</code>: Unique identifier for the supplier.</li>
  <li><code>supplier_prefix</code>: Prefix for the supplier (e.g., 'aliexpress').</li>
  <li><code>supplier_settings</code>: Settings for the supplier (loaded from a configuration file).</li>
  <li><code>locale</code>: Localization code (e.g., 'en').</li>
  <li><code>price_rule</code>: Rule for calculating prices.</li>
  <li><code>related_modules</code>: Module containing supplier-specific functions.</li>
  <li><code>scenario_files</code>: List of scenario files to be executed.</li>
  <li><code>current_scenario</code>: The currently executing scenario.</li>
  <li><code>login_data</code>: Login credentials for the supplier (if required).</li>
  <li><code>locators</code>: Locators for web elements on the supplier's site.</li>
  <li><code>driver</code>: Web driver for interacting with the supplier's site.</li>
  <li><code>parsing_method</code>: Method for data parsing (e.g., 'webdriver').</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs)</code>
    <ul>
      <li><strong>Description</strong>: Initializes the supplier object, setting the supplier prefix, locale, and optionally a web driver.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>supplier_prefix</code> (str): The prefix identifying the supplier.</li>
          <li><code>locale</code> (str, optional): The locale for the supplier (defaults to 'en').</li>
          <li><code>webdriver</code> (str | Driver | bool, optional): The web driver to use. Defaults to 'default'.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>_payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Loads supplier-specific configurations, locators, and initializes the web driver.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>webdriver</code> (str | Driver | bool): The web driver to use.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>bool</code>: True if loading was successful, False otherwise.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>login(self) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Handles the login process for the supplier's site (if needed).</li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>bool</code>: True if login was successful, False otherwise.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>run_scenario_files(self, scenario_files: str | List[str] = None) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Executes one or more scenario files.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>scenario_files</code> (str | List[str], optional): A string or list of strings representing the scenario files to execute.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>bool</code>: True if all scenarios ran successfully, False otherwise.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>run_scenarios(self, scenarios: dict | list[dict]) -> bool</code>
    <ul>
      <li><strong>Description</strong>: Executes a list of scenarios.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>scenarios</code> (dict | list[dict]): A dictionary or list of dictionaries defining the scenarios to run.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>bool</code>: True if all scenarios ran successfully, False otherwise.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
</ul>


<h2>Functions</h2>
<!-- No functions defined in the provided code -->