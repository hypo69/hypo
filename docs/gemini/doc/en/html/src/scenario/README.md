html
<h1>Module Documentation: src.scenario</h1>

<h2>Overview</h2>
<p>The <code>src.scenario</code> module automates interactions with suppliers using scenarios defined in JSON files.  It extracts product data from supplier websites and synchronizes it with a database (e.g., PrestaShop).</p>

<h2>Main Functions</h2>

<h3><code>run_scenario_files(s, scenario_files_list)</code></h3>

<p><strong>Description</strong>: Processes a list of scenario files sequentially.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance (e.g., `Supplier('aliexpress')`).</li>
  <li><code>scenario_files_list</code> (<code>Union[List[Path], Path]</code>): A list of paths to scenario files, or a single file path.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if all scenarios are executed successfully, otherwise <code>False</code>.</li>
</ul>


<h3><code>run_scenario_file(s, scenario_file)</code></h3>

<p><strong>Description</strong>: Loads and executes scenarios from a single file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>scenario_file</code> (<code>Union[Path, str]</code>): Path to the scenario file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the scenario file was executed successfully, otherwise <code>False</code>.</li>
</ul>


<h3><code>run_scenarios(s, scenarios=None)</code></h3>

<p><strong>Description</strong>: Executes a list or single scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier instance.</li>
  <li><code>scenarios</code> (<code>Union[List[dict], dict] = None</code>): A list or a single scenario to execute.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Union[List, dict, False]</code>: Result of executing scenarios, or <code>False</code> if an error occurs.</li>
</ul>


<h3><code>run_scenario(supplier, scenario, scenario_name=None)</code></h3>

<p><strong>Description</strong>: Executes a given scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code>: Supplier instance.</li>
  <li><code>scenario</code> (<code>dict</code>): Dictionary containing scenario details (e.g., URL, name, categories).</li>
  <li><code>scenario_name</code> (optional): The name of the scenario.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Union[List, dict, False]</code>: List of product links, or <code>False</code> if an error occurs.</li>
</ul>


<h3><code>insert_grabbed_data(product_fields)</code></h3>

<p><strong>Description</strong>: Inserts collected product data into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code>: Product fields object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code> (implicitly returns <code>True</code> or <code>False</code> through the asynchronous call).</li>
</ul>



<h3><code>execute_PrestaShop_insert_async(f, coupon_code=None, start_date=None, end_date=None)</code></h3>

<p><strong>Description</strong>: Asynchronously handles PrestaShop data insertion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>f</code> (<code>ProductFields</code>): Product fields object.</li>
  <li><code>coupon_code</code> (optional): Coupon code for insertion.</li>
  <li><code>start_date</code> (optional): Start date for the insertion.</li>
  <li><code>end_date</code> (optional): End date for the insertion.</li>
</ul>


<h3><code>execute_PrestaShop_insert(f, coupon_code=None, start_date=None, end_date=None)</code></h3>

<p><strong>Description</strong>: Inserts product data into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>f</code> (<code>ProductFields</code>): Product fields object.</li>
  <li><code>coupon_code</code>, <code>start_date</code>, <code>end_date</code>: (optional) Coupon code, start and end dates for the insertion.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if successful, otherwise <code>False</code>.</li>
</ul>

<h3><code>dump_journal(s, journal)</code></h3>

<p><strong>Description</strong>: Saves the scenario execution journal.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): Supplier instance.</li>
  <li><code>journal</code> (dict): Dictionary containing journal data.</li>
</ul>

<h2>Classes</h2>

<p>(If there are classes in the `src.scenario` module, their documentation would be included here).</p>

<h2>Data Structures</h2>


<p>This section describes the structures used for scenarios and product data.</p>

<h2>Example Usage</h2>

<p>Example code snippets demonstrating how to use the module functions.</p>


```
```