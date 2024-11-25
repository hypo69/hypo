html
<h1>Module hypotez/src/suppliers/cdata/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for extracting product data from a Morlevi source. It utilizes the <code>Graber</code> base class from the <code>src.suppliers</code> module and integrates with the overall application's structure.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: This class handles the data extraction process for Morlevi products. It inherits from the base <code>Graber</code> class and is responsible for initializing the extraction process and interacting with the underlying web driver.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): A string prefix identifying the supplier, set to 'cdata'.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, driver: Driver)</code>:
    <p><strong>Description</strong>: Initializes the <code>Graber</code> object. Takes a <code>Driver</code> instance for interacting with the web browser.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The web driver instance.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>No specific exceptions listed in the docstring.</li>
    </ul>
  </li>
  <li><code>grab_page(self, driver: Driver) -> ProductFields</code>:
    <p><strong>Description</strong>: Asynchronously fetches product data from the web page.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The web driver instance.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The extracted product data.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>No specific exceptions listed in the docstring.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>

<!--No functions defined in the given code snippet.-->

<h2>Global Variables</h2>
  <ul>
    <li><code>MODE</code> (str): Defines the current application mode, currently set to 'dev'.</li>
    <li><code>d</code> (Driver): A global variable, used within the `grab_page` method to hold the driver instance (this variable is not well-defined; it should be properly handled within the class).</li>

  </ul>

<p>**Note:** This documentation only covers aspects clearly visible in the provided code. Some parts of the original code, like the commented-out decorator <code>@close_pop_up</code>, are complex and would require further analysis of the full codebase to document completely.</p>