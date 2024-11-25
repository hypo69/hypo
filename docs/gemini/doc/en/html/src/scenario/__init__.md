html
<h1>hypotez/src/scenario/__init__.py</h1>

<h2>Overview</h2>
<p>This module provides functions for executing scenarios for suppliers. It defines the logic for interacting with suppliers, drivers, and external systems like PrestaShop.  It handles scenario files and dictionaries for execution.</p>

<h2>Functions</h2>

<h3><code>run_scenario</code></h3>

<p><strong>Description</strong>: Executes a single scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (Supplier): The supplier object to use for the scenario.</li>
  <li><code>scenario</code> (dict): The scenario dictionary to execute.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value, but likely performs actions internally.</li>
</ul>


<h3><code>run_scenarios</code></h3>

<p><strong>Description</strong>: Executes multiple scenarios.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (Supplier): The supplier object for execution.</li>
  <li><code>scenarios</code> (list | dict): A list of scenario dictionaries or a single scenario dictionary.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value, but likely performs actions internally.</li>
</ul>


<h3><code>run_scenario_file</code></h3>

<p><strong>Description</strong>: Executes a scenario from a JSON file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (Supplier): The supplier object.</li>
  <li><code>scenario_file</code> (str): The path to the JSON scenario file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value, but likely performs actions internally.</li>
</ul>


<h3><code>run_scenario_files</code></h3>

<p><strong>Description</strong>: Executes scenarios from multiple JSON files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (Supplier): The supplier object.</li>
  <li><code>scenario_files</code> (list): A list of file paths for the scenario files.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value, but likely performs actions internally.</li>
</ul>


<h3><code>execute_PrestaShop_insert</code></h3>

<p><strong>Description</strong>: Executes an insert operation into PrestaShop (likely database).</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><i>Not documented in the input code</i></li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><i>Not documented in the input code</i></li>
</ul>


<h3><code>execute_PrestaShop_insert_async</code></h3>

<p><strong>Description</strong>: Asynchronous insert operation into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><i>Not documented in the input code</i></li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><i>Not documented in the input code</i></li>
</ul>



<p><strong>Note:</strong> The input code lacks detailed documentation for `execute_PrestaShop_insert` and `execute_PrestaShop_insert_async` parameters and return values.  These functions require additional context to provide accurate documentation.</p>