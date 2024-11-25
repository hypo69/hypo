html
<h1>Module executor</h1>

<h2>Overview</h2>
<p>This module provides functions for executing scenarios, handling scenario files, working with products, and interacting with the PrestaShop API.  It includes examples demonstrating various usage patterns.</p>

<h2>Functions</h2>

<h3><code>run_scenario_files</code></h3>

<p><strong>Description</strong>: Executes a list of scenario files sequentially.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (MockSupplier): An object representing the supplier context.  It contains scenario file paths and other relevant data.</li>
  <li><code>scenario_files</code> (list of Path): A list of file paths to the scenario files.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if all scenarios were executed successfully, False otherwise.</li>
</ul>


<h3><code>run_scenario_file</code></h3>

<p><strong>Description</strong>: Executes a single scenario file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (MockSupplier): The supplier context object.</li>
  <li><code>scenario_file</code> (Path): The file path to the scenario file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the scenario file was executed successfully, False otherwise.</li>
</ul>


<h3><code>run_scenarios</code></h3>

<p><strong>Description</strong>: Executes a list of scenarios.</p>
<!-- Function definition missing, cannot provide parameters and return values -->

<h3><code>run_scenario</code></h3>

<p><strong>Description</strong>: Executes a single scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (MockSupplier): The supplier context object.</li>
  <li><code>scenario</code> (dict): The scenario data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the scenario was executed successfully, False otherwise.</li>
</ul>


<h3><code>insert_grabbed_data</code></h3>

<p><strong>Description</strong>: Inserts grabbed product data into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (ProductFields): An object containing the product data to be inserted.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code>execute_PrestaShop_insert</code></h3>

<p><strong>Description</strong>: Synchronously executes the PrestaShop insert operation.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (ProductFields): Contains the product data for insertion.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the insert was successful, False otherwise.</li>
</ul>


<h3><code>execute_PrestaShop_insert_async</code></h3>

<p><strong>Description</strong>: Asynchronously executes the PrestaShop insert operation.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>product_fields</code> (ProductFields): Contains the product data for insertion.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li>None (Async operation)</li>
</ul>


<h3><code>add_coupon</code></h3>

<p><strong>Description</strong>: Adds a coupon to the PrestaShop database.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials</code> (dict): API credentials for PrestaShop.</li>
  <li><code>reference</code> (str): Product reference.</li>
  <li><code>coupon_code</code> (str): Coupon code.</li>
  <li><code>start_date</code> (str): Start date of the coupon.</li>
  <li><code>end_date</code> (str): End date of the coupon.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>

<!-- Add other function documentation as needed -->

<h2>Classes</h2>

<h3><code>MockSupplier</code></h3>

<p><strong>Description</strong>: A mock class representing a supplier, used for testing. It includes placeholders for scenario files, supplier settings, and related modules.</p>

<!-- Add MockSupplier class method documentation -->

<h3><code>MockRelatedModules</code></h3>
<p><strong>Description</strong>: Mock class for related modules, providing mock implementations of methods required for scenario execution, such as getting product lists in a category and grabbing product pages.</p>

<h3><code>MockDriver</code></h3>
<p><strong>Description</strong>: Mock class for a driver, mocking a function for fetching URLs, simplifying scenario testing.</p>



<h2>Examples</h2>
<p>The module contains several example functions demonstrating the usage of the various functions, as detailed in the function documentation above.</p>