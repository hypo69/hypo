html
<h1>Module wallmart.graber</h1>

<h2>Overview</h2>
<p>This module contains the <code>Graber</code> class for grabbing product fields from the Walmart supplier.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for capturing product information from Walmart.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): The prefix for the supplier, set to 'wallmart'.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the Graber class with a driver instance. Sets the <code>supplier_prefix</code> and initializes the parent class.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance for interaction with the web browser.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: Asynchronous function to grab product fields from the page.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance used for web interaction.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The extracted product fields.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>

<!-- No functions are defined in the module, so this section is empty -->