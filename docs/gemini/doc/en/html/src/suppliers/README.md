html
<h1>Supplier Class Documentation</h1>

<h2>Overview</h2>
<p>This module provides documentation for the <code>Supplier</code> class, which serves as a base for managing interactions with various e-commerce suppliers.</p>

<h2>Classes</h2>

<h3><code>Supplier</code></h3>

<p><strong>Description</strong>: The <code>Supplier</code> class acts as a foundation for interacting with suppliers like Amazon, Walmart, Mouser, and Digi-Key.  It handles initialization, configuration, authentication, and scenario execution.  Custom suppliers can be added by users.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_id</code> (int): Unique identifier for the supplier.</li>
  <li><code>supplier_prefix</code> (str): Supplier prefix (e.g., 'amazon', 'aliexpress').</li>
  <li><code>supplier_settings</code> (dict): Settings specific to the supplier, loaded from a JSON file.</li>
  <li><code>locale</code> (str): Localization code (default: 'en').</li>
  <li><code>price_rule</code> (str): Rules for price calculation (e.g., VAT rules).</li>
  <li><code>related_modules</code> (module): Supplier-specific helper modules.</li>
  <li><code>scenario_files</code> (list): List of scenario files to execute.</li>
  <li><code>current_scenario</code> (dict): Currently executing scenario.</li>
  <li><code>login_data</code> (dict): Login credentials and related data.</li>
  <li><code>locators</code> (dict): Locator dictionary for web elements.</li>
  <li><code>driver</code> (Driver): WebDriver instance for supplier website interaction.</li>
  <li><code>parsing_method</code> (str): Data parsing method (e.g., 'webdriver', 'api', 'xls', 'csv').</li>
</ul>

<p><strong>Methods</strong>:</p>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Constructor for the <code>Supplier</code> class.</p>

<pre><code class="language-python">def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Initializes the Supplier instance.

    Args:
        supplier_prefix (str): Prefix for the supplier.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): WebDriver type. Defaults to 'default'.

    Raises:
        DefaultSettingsException: If default settings are not configured correctly.
    """
</code></pre>

<h4><code>_payload</code></h4>

<p><strong>Description</strong>: Loads supplier configurations and initializes the WebDriver.</p>

<pre><code class="language-python">def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes the WebDriver.

    Args:
        webdriver (str | Driver | bool): WebDriver type.

    Returns:
        bool: Returns True if payload loaded successfully.
    """
</code></pre>

<h4><code>login</code></h4>

<p><strong>Description</strong>: Handles authentication for the supplier's website.</p>

<pre><code class="language-python">def login(self) -> bool:
    """Authenticates the user on the supplier's website.

    Returns:
        bool: Returns True if login was successful.
    """
</code></pre>

<h4><code>run_scenario_files</code></h4>

<p><strong>Description</strong>: Executes one or more scenario files.</p>

<pre><code class="language-python">def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Runs the provided scenario files.

    Args:
        scenario_files (str | List[str], optional): List or single path to scenario files.

    Returns:
        bool: Returns True if all scenarios executed successfully.
    """
</code></pre>


<h4><code>run_scenarios</code></h4>

<p><strong>Description</strong>: Executes provided scenarios.</p>

<pre><code class="language-python">def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Executes the specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to execute.

    Returns:
        bool: Returns True if all scenarios executed successfully.
    """
</code></pre>

<h2>How It Works</h2>
<p>(Detailed explanation of the process is already present in the Markdown)</p>


<h2>Class Diagram</h2>
<p>(Class diagram is already present in the Markdown)</p>