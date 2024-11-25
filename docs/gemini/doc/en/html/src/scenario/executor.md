html
<h1>hypotez/src/scenario/executor.py</h1>

<h2>Overview</h2>
<p>This module contains functions for executing scenarios, loading them from files, and handling the process of extracting product information and inserting it into PrestaShop.</p>

<h2>Functions</h2>

<h3><code>dump_journal</code></h3>

<p><strong>Description</strong>: Save the journal data to a JSON file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>journal</code> (dict): Dictionary containing the journal data.</li>
</ul>


<h3><code>run_scenario_files</code></h3>

<p><strong>Description</strong>: Executes a list of scenario files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>scenario_files_list</code> (List[Path] | Path): List of file paths for scenario files, or a single file path.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: if <code>scenario_files_list</code> is not a list or a Path object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if all scenarios were executed successfully, False otherwise.</li>
</ul>


<h3><code>run_scenario_file</code></h3>

<p><strong>Description</strong>: Loads and executes scenarios from a file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>scenario_file</code> (Path): Path to the scenario file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the scenario file is not found.</li>
  <li><code>json.JSONDecodeError</code>: If the scenario file is not a valid JSON.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the scenario was executed successfully, False otherwise.</li>
</ul>


<h3><code>run_scenarios</code></h3>

<p><strong>Description</strong>: Function to execute a list of scenarios (NOT FILES).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>scenarios</code> (List[dict] | dict, optional): Accepts a list of scenarios or a single scenario as a dictionary. Defaults to None. </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>List | dict | False: The result of executing the scenarios as a list or dictionary, depending on the input data type, or False in case of an error.</li>
</ul>

<p><strong>Todo</strong>:</p>
<ul>
  <li>Check the option when no scenarios are specified from all sides.</li>
</ul>


<h3><code>run_scenario</code></h3>

<p><strong>Description</strong>: Function to execute the received scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code>: Supplier instance.</li>
  <li><code>scenario</code> (dict): Dictionary containing scenario details.</li>
  <li><code>scenario_name</code> (str): Name of the scenario.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>List | dict | False: The result of executing the scenario.</li>
</ul>

<p><strong>Todo</strong>:</p>
<ul>
  <li>Check the need for the <code>scenario_name</code> parameter.</li>
</ul>

<h3><code>insert_grabbed_data</code></h3>

<p><strong>Description</strong>: Insert grabbed product data into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (ProductFields): ProductFields instance containing the product information.</li>
</ul>

<p><strong>Todo</strong>:</p>
<ul>
  <li>Move this logic to another file. In PrestaShop class.</li>
</ul>

<h3><code>execute_PrestaShop_insert_async</code></h3>
<h3><code>execute_PrestaShop_insert</code></h3>

<p><strong>Description</strong>: Insert the product into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>f</code> (ProductFields): ProductFields instance containing the product information.</li>
  <li><code>coupon_code</code> (str, optional): Optional coupon code.</li>
  <li><code>start_date</code> (str, optional): Optional start date for the promotion.</li>
  <li><code>end_date</code> (str, optional): Optional end date for the promotion.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>bool: True if the insertion was successful, False otherwise.</li>
</ul>