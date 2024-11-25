html
<h1>Module: hypotez/src/suppliers/etzmaleh/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class, a subclass of <code>Grbr</code>, responsible for gathering product fields from the Etzmaleh supplier.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for grabbing Morlevi product data. It inherits from <code>Grbr</code> and handles the specific data extraction logic for the Etzmaleh supplier.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): Prefix identifying the supplier (e.g., 'etzmaleh').</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the <code>Graber</code> instance with a driver object and sets the <code>supplier_prefix</code>.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance for interaction.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: Asynchronous function to gather product fields. Retrieves data from the Etzmaleh supplier.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The gathered product data.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
		<li><code>ExecuteLocatorException</code>: If an error occurs while executing a locator.</li>
		<li><i>(Any other exceptions potentially raised within the async calls)</i></li>
    </ul>
  </li>
</ul>



<h2>Functions</h2>


<!-- Add documentation for any functions defined in the module here.  -->


<!-- Add any additional classes or functions found in the file here.  Be sure to format them according to the instruction document. -->
</ul>