html
<h1>hypotez/src/scenario/_examples/_example_executor.py</h1>

<h2>Overview</h2>
<p>This module provides examples for the <code>executor</code> module from <code>src.scenario.executor</code>. It demonstrates how to use functions for running scenarios, handling scenario files, interacting with the PrestaShop API, and more.</p>

<h2>Classes</h2>

<h3><code>MockSupplier</code></h3>

<p><strong>Description</strong>: A mock class representing a supplier, used for testing purposes. It simulates the necessary methods and attributes for interacting with scenarios and PrestaShop.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_abs_path</code> (<code>Path</code>): The absolute path to the scenarios directory.</li>
  <li><code>scenario_files</code> (<code>list</code> of <code>Path</code>): A list of scenario files to be executed.</li>
  <li><code>current_scenario</code> (<code>Any</code>): The current scenario being executed.</li>
  <li><code>supplier_settings</code> (<code>dict</code>): Settings related to the supplier.</li>
  <li><code>related_modules</code> (<code>MockRelatedModules</code>): A mock related modules object.</li>
  <li><code>driver</code> (<code>MockDriver</code>): A mock driver object.</li>
</ul>


<h3><code>MockRelatedModules</code></h3>

<p><strong>Description</strong>: A mock class for related modules, used for testing purposes.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>get_list_products_in_category(s)</code>: Retrieves a list of product URLs in a given category.</li>
  <li><code>grab_product_page(s)</code>: Grabs the product page data.</li>
  <li><code>grab_page(s)</code>: Grabs a webpage asynchronously. (Async method)</li>
</ul>


<h3><code>MockDriver</code></h3>

<p><strong>Description</strong>: A mock class for the driver, used for testing purposes.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>get_url(url)</code>: Retrieves the URL data.</li>
</ul>


<h2>Functions</h2>

<h3><code>example_run_scenario_files</code></h3>

<p><strong>Description</strong>: Runs a list of scenario files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (<code>MockSupplier</code>): The supplier object.</li>
  <li><code>scenario_files</code> (<code>list</code> of <code>Path</code>): List of scenario files to run.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if all scenarios executed successfully, False otherwise.</li>
</ul>


<h3><code>example_run_scenario_file</code></h3>

<p><strong>Description</strong>: Runs a single scenario file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (<code>MockSupplier</code>): The supplier object.</li>
  <li><code>scenario_file</code> (<code>Path</code>): The path to the scenario file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the scenario file executed successfully, False otherwise.</li>
</ul>


<h3><code>example_run_scenario</code></h3>

<p><strong>Description</strong>: Runs a single scenario.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (<code>MockSupplier</code>): The supplier object.</li>
  <li><code>scenario</code> (<code>dict</code>): The scenario data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the scenario executed successfully, False otherwise.</li>
</ul>


<h3><code>example_insert_grabbed_data</code></h3>

<p><strong>Description</strong>: Inserts grabbed product data into PrestaShop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (<code>ProductFields</code>): The product data to be inserted.</li>
</ul>


<h3><code>example_add_coupon</code></h3>

<p><strong>Description</strong>: Adds a coupon using the PrestaShop API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials</code> (<code>dict</code>): API credentials.</li>
  <li><code>reference</code> (<code>str</code>): Product reference.</li>
  <li><code>coupon_code</code> (<code>str</code>): Coupon code.</li>
  <li><code>start_date</code> (<code>str</code>): Start date of the coupon.</li>
  <li><code>end_date</code> (<code>str</code>): End date of the coupon.</li>
</ul>


<h3><code>example_execute_PrestaShop_insert_async</code></h3>

<p><strong>Description</strong>: Executes PrestaShop insert asynchronously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (<code>ProductFields</code>): Product data to be inserted.</li>
</ul>


<h3><code>example_execute_PrestaShop_insert</code></h3>

<p><strong>Description</strong>: Executes PrestaShop insert synchronously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_fields</code> (<code>ProductFields</code>): Product data to be inserted.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the insertion was successful, False otherwise.</li>
</ul>


<p><strong>Note</strong>: This code includes placeholder comments and examples. Actual implementations would need to be fleshed out with appropriate error handling and interaction with the PrestaShop API.</p>