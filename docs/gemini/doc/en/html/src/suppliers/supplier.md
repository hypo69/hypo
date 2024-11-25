html
<h1>Module: hypotez/src/suppliers/supplier.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Supplier</code> class, responsible for executing scenarios for various suppliers. It handles loading supplier configurations, performing login, and running scenario files or individual scenarios.</p>

<h2>Classes</h2>

<h3><code>Supplier</code></h3>

<p><strong>Description</strong>: This class represents a supplier and manages the execution of scenarios related to that supplier. It loads configuration settings, performs login, and runs scenario files.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_id</code> (Optional[int]): Supplier identifier.</li>
  <li><code>supplier_prefix</code> (str): Prefix identifying the supplier.</li>
  <li><code>locale</code> (str): Locale code (e.g., 'en').</li>
  <li><code>price_rule</code> (Optional[str]): Price calculation rule.</li>
  <li><code>related_modules</code> (Optional[ModuleType]): Modules specific to the supplier.</li>
  <li><code>scenario_files</code> (List[str]): List of scenario files to execute.</li>
  <li><code>current_scenario</code> (Dict[str, Any]): The current scenario being executed.</li>
  <li><code>locators</code> (Dict[str, Any]): Locators for page elements.</li>
  <li><code>driver</code> (Optional[Driver]): Web driver instance.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, **data)</code>:
    <p><strong>Description</strong>: Initializes the supplier and loads configuration data.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>DefaultSettingsException</code>: If there's an error during supplier initialization.</li>
    </ul>
  </li>

  <li><code>_payload(self) -> bool</code>:
    <p><strong>Description</strong>: Loads the supplier's parameters using <code>j_loads_ns</code>.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if loading is successful, False otherwise.</li>
    </p>
  </li>

  <li><code>login(self) -> bool</code>:
    <p><strong>Description</strong>: Performs login on the supplier's website.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if login is successful, False otherwise.</li>
    </ul>
  </li>

  <li><code>run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool</code>:
    <p><strong>Description</strong>: Executes one or multiple scenario files.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>scenario_files</code> (Optional[str | List[str]]): List of scenario files to run. Defaults to <code>self.scenario_files</code> if not provided.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if all scenarios are successfully executed, False otherwise.</li>
    </ul>
  </li>

  <li><code>run_scenarios(self, scenarios: dict | List[dict]) -> bool</code>:
    <p><strong>Description</strong>: Executes a single or a list of scenarios.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>scenarios</code> (dict | List[dict]): Scenario or a list of scenarios to run.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if the scenario is successfully executed, False otherwise.</li>
    </ul>
  </li>
</ul>

<p><strong>Class Config</strong>:</p>
<ul>
  <li><code>arbitrary_types_allowed</code> (bool): Allows arbitrary types.</li>
</ul>

<p><strong>Validators</strong>:</p>
<ul>
  <li><code>check_supplier_prefix(cls, value: str) -> str</code>:
    <p><strong>Description</strong>: Validates the supplier prefix ensuring it's not empty.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ValueError</code>: If the prefix is empty.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>


<!-- Function documentation will be added here as functions are added -->